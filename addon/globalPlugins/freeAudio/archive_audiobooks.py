# -*- coding: utf-8 -*-
# freeAudio - Audio Books (general Internet Archive audio books) integration
#
# Searches and resolves playable media from the Internet Archive's
# (https://archive.org/) community-uploaded audio books - every audio item
# tagged "audiobook" that is NOT already covered by this add-on's two
# dedicated archive.org sources (LibriVox and the Project Gutenberg Open
# Audiobook Collection, see librivox.py / gutenberg_audiobooks.py).
#
# WHY THIS SOURCE EXISTS: a survey of archive.org's audio collections
# (probe_archive_collections.py, run against the live site) found that the
# "Audio Books & Poetry" collection is mostly LibriVox again, and the
# "Non-English Audio" collection holds almost no audio books, so neither
# adds anything. What does add something is archive.org's own "audiobook"
# subject tag across all audio items: it includes audio books in other
# languages, notably ~100 Turkish ones (language "tur") - e.g. uploads by
# seslikitap.net and NTV Tarih's "1001 Gece Masalları" - none of which
# LibriVox or the Gutenberg collection carry.
#
# CONTENT NOTE: unlike LibriVox (volunteer-read public domain) and the
# Gutenberg collection (one machine-narrated corpus), these are ordinary
# user uploads. Quality, narration, subject matter and licensing vary from
# item to item (e.g. some are CC BY-NC-SA, many state no licence at all),
# which is why this source is OFF by default and has to be switched on in
# freeAudio's settings ("Audio book sources"). freeAudio only streams or
# downloads the files for personal listening, exactly as it does for the
# other sources.
#
# Structure mirrors gutenberg_audiobooks.py (same two archive.org JSON
# endpoints: advancedsearch.php and metadata/<identifier>), and
# ArchiveAudiobook/ArchiveLibrary are attribute- and method-compatible with
# GetemBook/LibrivoxBook/GutenbergAudiobook, so radioDialog.py's Audio Books
# tab drives all four sources through the same generic code - see
# RadioDialog._audiobook_module_for()/_audiobook_library_for().
#
# What differs from the other two archive.org sources is file picking:
# uploads are inconsistent about the file-format label ("VBR MP3", "MP3",
# "128Kbps MP3", ...) and track numbering, so _chapters_from_metadata()
# works down a priority list of labels, falls back to any audio file by
# extension, and sorts by track number with a natural (number-aware) name
# sort as the tie-breaker.

import json
import logging
import os
import re
import urllib.error
import urllib.parse
import urllib.request
import uuid

import addonHandler
addonHandler.initTranslation()
_tr = globals()["_"]
_ = _tr
del _tr
ngettext = globals().get("ngettext", lambda s, p, n: s if n == 1 else p)

import globalVars

from . import archiveQuery

log = logging.getLogger(__name__)

# Items in these collections belong to the dedicated LibriVox / Project
# Gutenberg sources and are excluded here so nothing shows up twice.
EXCLUDED_COLLECTIONS = ("librivoxaudio", "gutenberg-audiobooks")
# Every search is scoped to audio items tagged as an audio book, minus the
# collections above.
SEARCH_SCOPE = (
	'mediatype:(audio) AND subject:(audiobook OR audiobooks OR "audio book" OR "audio books")'
	+ "".join(" AND NOT collection:(%s)" % c for c in EXCLUDED_COLLECTIONS)
)
ARCHIVE_ADVANCED_SEARCH_URL = "https://archive.org/advancedsearch.php"
ARCHIVE_METADATA_URL = "https://archive.org/metadata/"
ARCHIVE_DOWNLOAD_BASE = "https://archive.org/download/"
ARCHIVE_DETAILS_BASE = "https://archive.org/details/"
ARCHIVE_DETAILS_URL_RE = re.compile(
	r"^https?://(?:www\.)?archive\.org/details/([A-Za-z0-9._-]+)", re.IGNORECASE)
USER_AGENT = "freeAudio-NVDA/1.0"
_MAX_RESPONSE_BYTES = 10 * 1024 * 1024  # 10 MB

_AUDIO_DOWNLOAD_EXTENSIONS = frozenset({
	".mp3", ".m4a", ".m4b", ".aac", ".ogg", ".oga", ".opus",
	".wav", ".flac", ".mp4", ".wma", ".aiff", ".aif",
})
# Extensions picked up by the last-resort extension match - playable audio
# only (no .mp4/.wma, which are as likely to be video/other).
_FALLBACK_EXTENSIONS = (".mp3", ".m4a", ".m4b", ".ogg", ".opus", ".flac", ".wav")
REQUEST_TIMEOUT = 15
SEARCH_TIMEOUT = 20
RESULTS_PER_QUERY = 100

# Tried in order against each item's file listing; the first label that
# matches anything wins, so an item never gets the same track twice in
# different encodings. "VBR MP3" is what the survey found on every sampled
# item (Turkish uploads included); the rest cover uploads encoded or labelled
# differently.
_AUDIO_FORMAT_PRIORITY = (
	"VBR MP3", "MP3", "128Kbps MP3", "64Kbps MP3", "96Kbps MP3", "160Kbps MP3",
	"192Kbps MP3", "256Kbps MP3", "320Kbps MP3", "32Kbps MP3", "Ogg Vorbis",
	"MPEG4", "Flac", "Opus",
)


# --------------------------------------------------------------------- #
# Search
# --------------------------------------------------------------------- #

def _fetch(url, timeout=REQUEST_TIMEOUT):
	headers = {
		"User-Agent": USER_AGENT,
		"Accept": "application/json, application/xml;q=0.9, text/xml;q=0.8, */*;q=0.5",
	}
	req = urllib.request.Request(url, headers=headers)
	try:
		with urllib.request.urlopen(req, timeout=timeout) as resp:
			raw = resp.read(_MAX_RESPONSE_BYTES + 1)
			if len(raw) > _MAX_RESPONSE_BYTES:
				raise RuntimeError("Response too large (>10 MB) for %s" % url)
			charset = resp.headers.get_content_charset() or "utf-8"
			return raw.decode(charset, errors="replace")
	except urllib.error.HTTPError as e:
		try:
			body = e.read().decode("utf-8", errors="replace")[:300].strip()
		except Exception:
			body = ""
		detail = (" | response body: %s" % body) if body else " | (no response body)"
		raise RuntimeError("HTTP %s for %s%s" % (e.code, url, detail)) from e


def _first_str(value):
	"""archive.org returns a field as either a bare string or a list of
	strings depending on the item - normalizes either shape to one string."""
	if isinstance(value, list):
		return str(value[0]) if value else ""
	return str(value) if value is not None else ""


def _strip_html(text):
	return re.sub(r"<[^>]+>", "", text or "").strip()


def _parse_archive_doc(doc):
	"""One 'doc' entry from advancedsearch.php (or the equivalent built from a
	metadata response) -> ArchiveAudiobook, with archive_id set so
	resolve_media() knows which item's file listing to fetch."""
	identifier = _first_str(doc.get("identifier")).strip()
	# Translators: Fallback book title when archive.org returns no title metadata for a search result.
	title = _first_str(doc.get("title")).strip() or _("Unknown")

	creators = doc.get("creator")
	if isinstance(creators, list):
		author = ", ".join(c.strip() for c in (str(x) for x in creators) if c.strip())
	else:
		author = _first_str(creators).strip()

	language = _first_str(doc.get("language")).strip()
	description = _strip_html(_first_str(doc.get("description")))
	runtime = _first_str(doc.get("runtime")).strip()

	book = ArchiveAudiobook(
		title=title, detail_url=ARCHIVE_DETAILS_BASE + identifier, author=author,
		description=description, language=language,
	)
	book.archive_id = identifier
	if runtime and language:
		book.format_label = "%s, %s" % (language, runtime)
	elif runtime:
		book.format_label = runtime
	elif language:
		book.format_label = language
	return book


def search_archive_audiobooks(query, limit=RESULTS_PER_QUERY):
	"""Searches archive.org audio books outside LibriVox and the Project
	Gutenberg collection (see SEARCH_SCOPE) for *query*, matched against title
	OR creator. Returns (list_of_ArchiveAudiobook, error_message)."""
	query = (query or "").strip()
	if not query:
		# Translators: Error returned by search_archive_audiobooks() when the user submits an empty search box.
		return [], _("Please enter a search term.")

	data = None
	for search_q in archiveQuery.build_queries(query, base=SEARCH_SCOPE):
		params = [
			("q", search_q),
			("fl[]", "identifier"),
			("fl[]", "title"),
			("fl[]", "creator"),
			("fl[]", "language"),
			("fl[]", "description"),
			("fl[]", "runtime"),
			("rows", str(limit)),
			("page", "1"),
			("output", "json"),
		]
		url = "%s?%s" % (ARCHIVE_ADVANCED_SEARCH_URL, urllib.parse.urlencode(params))
		try:
			response_text = _fetch(url, timeout=SEARCH_TIMEOUT)
		except Exception as e:
			log.warning("freeAudio Internet Archive audio books: search failed: %s", e)
			return [], str(e)
		try:
			data = json.loads(response_text)
		except ValueError as e:
			log.warning("freeAudio Internet Archive audio books: could not parse search response: %s", e)
			return [], str(e)
		if (((data or {}).get("response") or {}).get("docs")):
			break

	docs = (((data or {}).get("response") or {}).get("docs")) or []
	books = []
	for doc in docs:
		try:
			books.append(_parse_archive_doc(doc))
		except Exception as e:
			log.warning("freeAudio Internet Archive audio books: could not parse one result: %s", e)
	return books, None


# --------------------------------------------------------------------- #
# Book model
# --------------------------------------------------------------------- #

class ArchiveAudiobook:
	"""A single general-archive.org audio book. Attribute- and method-
	compatible with getem.GetemBook/librivox.LibrivoxBook/
	gutenberg_audiobooks.GutenbergAudiobook so radioDialog.py's generic Audio
	Books tab code works unmodified against this source too."""

	def __init__(self, title, detail_url, author="", narrator="", format_label="",
			description="", publisher="", language="", archive_id=""):
		# Translators: Fallback ArchiveAudiobook.title when no title was supplied at construction.
		self.title = title or _("Unknown")
		self.detail_url = detail_url
		self.author = author
		# Uploads rarely say who reads; kept for attribute compatibility and
		# shown only when an item actually names a narrator.
		self.narrator = narrator
		self.format_label = format_label
		self.description = description
		self.publisher = publisher
		self.language = language
		# archive.org item identifier - resolve_media() fetches the file
		# listing from archive.org's metadata API with it.
		self.archive_id = archive_id
		# Populated lazily by resolve_media(): [{"title": str, "url": str}, ...]
		self.chapters = []
		self.last_chapter_index = 0
		self.audio_profile = None

	def identity_key(self):
		return self.detail_url

	def to_dict(self):
		"""Same station-like dict shape as getem.GetemBook.to_dict() - see
		its docstring, and in particular why "getem_detail_url" is reused
		verbatim for every audio book source."""
		return {
			"name": self.title,
			"url": "",
			"url_resolved": "",
			"stationuuid": "archive-audiobook-" + str(uuid.uuid5(uuid.NAMESPACE_URL, self.detail_url)),
			"countrycode": "",
			"tags": "podcast,audiobook",
			"media_kind": "audiobook",
			"getem_detail_url": self.detail_url,
			"author": self.author,
			"narrator": self.narrator,
			"publisher": self.publisher,
			"audiobook_format": self.format_label,
			"audiobook_chapter_count": len(self.chapters),
			"description": self.description,
			# Translators: Fixed source label for general Internet Archive audio books, shown in the station-details dialog and the Audio Books tab.
			"audiobook_source": _("Internet Archive"),
		}

	def to_library_dict(self):
		return {
			"title": self.title,
			"author": self.author,
			"narrator": self.narrator,
			"format_label": self.format_label,
			"description": self.description,
			"publisher": self.publisher,
			"language": self.language,
			"archive_id": self.archive_id,
			"detail_url": self.detail_url,
			"chapters": self.chapters,
			"last_chapter_index": self.last_chapter_index,
			"audio_profile": self.audio_profile,
		}

	@classmethod
	def from_dict(cls, data):
		book = cls(
			title=data.get("title", ""),
			detail_url=data.get("detail_url", ""),
			author=data.get("author", ""),
			narrator=data.get("narrator", ""),
			format_label=data.get("format_label", ""),
			description=data.get("description", ""),
			publisher=data.get("publisher", ""),
			language=data.get("language", ""),
			archive_id=data.get("archive_id", ""),
		)
		book.chapters = data.get("chapters", []) or []
		book.last_chapter_index = data.get("last_chapter_index", 0) or 0
		book.audio_profile = data.get("audio_profile") or None
		return book


# --------------------------------------------------------------------- #
# Media resolution
# --------------------------------------------------------------------- #

def resolve_media(book, session=None):
	"""Fills in *book*.chapters with every audio file found for it.
	*session* is accepted but unused - kept so radioDialog.py can call this
	like getem.resolve_media(). Returns (book, error_message)."""
	if not book.archive_id:
		# Translators: Error returned by resolve_media() when the book has no linked archive.org item id, so no audio files can be looked up.
		return book, _("This book has no archive.org item to read audio files from.")
	return _resolve_via_archive_org(book)


def looks_like_book_url(text):
	"""Whether *text* looks like an archive.org item link."""
	return bool(ARCHIVE_DETAILS_URL_RE.match((text or "").strip()))


def get_book_by_url(url):
	"""Resolves a book from an archive.org "details" URL, but only if it is
	an audio item that does NOT belong to LibriVox or the Project Gutenberg
	collection (those have their own sources) - so that a pasted link for one
	of those isn't claimed here. Returns (book_or_None, error_message)."""
	match = ARCHIVE_DETAILS_URL_RE.match((url or "").strip())
	if not match:
		# Translators: Error returned by get_book_by_url() when the pasted URL doesn't match archive.org's book-details link pattern.
		return None, _("This doesn't look like an archive.org book link.")
	return _resolve_book_by_identifier(match.group(1))


def _resolve_book_by_identifier(identifier):
	url = ARCHIVE_METADATA_URL + urllib.parse.quote(identifier, safe="")
	try:
		response_text = _fetch(url, timeout=REQUEST_TIMEOUT)
	except Exception as e:
		return None, str(e)
	try:
		data = json.loads(response_text)
	except ValueError as e:
		return None, str(e)

	meta = data.get("metadata") or {}
	if not meta or not meta.get("identifier"):
		# Translators: Error returned when the archive.org identifier from a pasted link does not resolve to any item at all.
		return None, _("Could not find a book at this address on archive.org.")

	collections = meta.get("collection")
	if isinstance(collections, str):
		collections = [collections]
	collections = {str(c).strip().lower() for c in (collections or [])}
	if _first_str(meta.get("mediatype")).strip().lower() != "audio" or collections & set(EXCLUDED_COLLECTIONS):
		# Translators: Error returned when a pasted archive.org link is not an audio item, or belongs to LibriVox or the Project Gutenberg collection, which have their own sources.
		return None, _("This archive.org item is not a general audio book (LibriVox and Project Gutenberg titles have their own sources).")

	book = _parse_archive_doc({
		"identifier": identifier,
		"title": meta.get("title"),
		"creator": meta.get("creator"),
		"language": meta.get("language"),
		"description": meta.get("description"),
		"runtime": meta.get("runtime"),
	})
	return _chapters_from_metadata(book, data)


def _natural_key(text):
	return [int(p) if p.isdigit() else p.casefold() for p in re.split(r"(\d+)", text or "")]


def _chapters_from_metadata(book, data):
	"""Fills in *book*.chapters from an archive.org metadata response. Works
	down _AUDIO_FORMAT_PRIORITY and takes the first label that matches
	anything; if none does, takes every file with a playable audio extension.
	Ordered by track number, then by a number-aware name sort. Returns
	(book, error_message)."""
	files = [f for f in (data.get("files") or []) if isinstance(f, dict)]
	server = data.get("server") or data.get("d1") or ""
	item_dir = data.get("dir") or ""

	def _file_url(name):
		if server and item_dir:
			return "https://%s%s/%s" % (server, item_dir, urllib.parse.quote(name))
		return ARCHIVE_DOWNLOAD_BASE + urllib.parse.quote(book.archive_id, safe="") + "/" + urllib.parse.quote(name)

	def _sort_key(f):
		track = (f.get("track") or "").split("/")[0].strip()
		try:
			return (0, int(track), _natural_key(f.get("name") or ""))
		except (TypeError, ValueError):
			return (1, 0, _natural_key(f.get("name") or ""))

	picked = []
	for label in _AUDIO_FORMAT_PRIORITY:
		picked = [f for f in files if (f.get("format") or "") == label and f.get("name")]
		if picked:
			break
	if not picked:
		picked = [
			f for f in files
			if f.get("name") and (f.get("name") or "").lower().endswith(_FALLBACK_EXTENSIONS)
		]
	picked.sort(key=_sort_key)

	chapters = []
	for f in picked:
		name = f.get("name") or ""
		title = (f.get("title") or "").strip() or os.path.splitext(os.path.basename(name))[0]
		chapters.append({"title": title, "url": _file_url(name)})

	if not chapters:
		# Translators: Error returned by the chapter-listing step when archive.org has no playable audio file for the resolved book.
		return book, _("No playable audio file was found for this book on archive.org.")

	book.chapters = chapters
	return book, None


def _resolve_via_archive_org(book):
	url = ARCHIVE_METADATA_URL + urllib.parse.quote(book.archive_id, safe="")
	try:
		response_text = _fetch(url, timeout=REQUEST_TIMEOUT)
	except Exception as e:
		return book, str(e)
	try:
		data = json.loads(response_text)
	except ValueError as e:
		return book, str(e)
	return _chapters_from_metadata(book, data)


# --------------------------------------------------------------------- #
# Streaming and downloads - same shapes as gutenberg_audiobooks.py, so
# radioDialog.py's code works unmodified against this source too.
# --------------------------------------------------------------------- #

def get_stream_url(chapter_url, referer=None):
	return chapter_url


def _fetch_audio_file(chapter_url, dest_path, referer=None, session=None, progress_callback=None):
	headers = {"User-Agent": USER_AGENT, "Accept": "audio/mpeg, audio/*;q=0.9, */*;q=0.5"}
	req = urllib.request.Request(chapter_url, headers=headers)
	tmp_path = dest_path + ".part"
	with urllib.request.urlopen(req, timeout=60) as resp:
		try:
			total = int(resp.headers.get("Content-Length") or 0)
		except (TypeError, ValueError):
			total = 0
		written = 0
		with open(tmp_path, "wb") as f:
			while True:
				chunk = resp.read(65536)
				if not chunk:
					break
				f.write(chunk)
				written += len(chunk)
				if progress_callback:
					progress_callback(written, total)

	if written == 0:
		try:
			os.remove(tmp_path)
		except OSError:
			pass
		# Translators: Raised internally when a chapter/book download completes but produced a zero-byte file; caught and shown to the user as a download failure.
		raise RuntimeError(_("The downloaded file was empty."))

	os.replace(tmp_path, dest_path)
	return dest_path


def download_chapter_to(chapter_url, out_path, referer=None, session=None, progress_callback=None):
	if os.path.exists(out_path):
		raise FileExistsError(out_path)
	return _fetch_audio_file(chapter_url, out_path, referer=referer, session=session, progress_callback=progress_callback)


def _chapter_file_extension(chapter_url):
	url_path = urllib.parse.urlparse(chapter_url).path
	ext = os.path.splitext(url_path)[1].lower()
	if ext not in _AUDIO_DOWNLOAD_EXTENSIONS:
		ext = ".mp3"
	return ext


def safe_book_title(book):
	return "".join(c for c in book.title if c.isalnum() or c in " .-_")[:60].strip()


def download_target(book, chapter):
	from . import recorder
	out_dir = recorder._recordings_dir()
	safe_book = safe_book_title(book)
	chapter_title = chapter.get("title") or ""
	safe_chapter = "".join(c for c in chapter_title if c.isalnum() or c in " .-_")[:60].strip()
	ext = _chapter_file_extension(chapter["url"])
	if safe_chapter and safe_chapter != safe_book:
		filename = f"{safe_book} - {safe_chapter}{ext}"
	else:
		filename = f"{safe_book}{ext}"
	return os.path.join(out_dir, filename), filename


def book_download_dir(book):
	from . import recorder
	out_dir = recorder._recordings_dir()
	# Translators: Fallback folder name used when saving a downloaded book, if the book's title is empty or has no usable characters.
	return os.path.join(out_dir, safe_book_title(book) or _("Untitled"))


def download_book_chapter_target(book, chapter, chapter_index):
	out_dir = book_download_dir(book)
	chapter_title = (chapter.get("title") or "").strip()
	safe_chapter = "".join(c for c in chapter_title if c.isalnum() or c in " .-_")[:60].strip()
	ext = _chapter_file_extension(chapter["url"])
	width = len(str(len(book.chapters)))
	number = str(chapter_index + 1).zfill(width)
	safe_book = safe_book_title(book)
	if safe_chapter and safe_chapter != safe_book:
		filename = f"{number} - {safe_chapter}{ext}"
	else:
		filename = f"{number}{ext}"
	return os.path.join(out_dir, filename)


# --------------------------------------------------------------------- #
# Library persistence - same shape as the other sources' libraries.
# --------------------------------------------------------------------- #

class ArchiveLibrary:
	"""The user's saved general-archive.org audio books. Persisted in its own
	JSON file; RadioDialog._merged_library_books() combines every source's
	library into one shelf for display."""

	def __init__(self):
		self._books = []
		self._load()

	def _get_path(self):
		return os.path.join(globalVars.appArgs.configPath, "freeAudio_archive_audiobooks_library.json")

	def _load(self):
		path = self._get_path()
		if not os.path.exists(path):
			return
		try:
			with open(path, "r", encoding="utf-8") as f:
				data = json.load(f)
			self._books = [ArchiveAudiobook.from_dict(item) for item in data if isinstance(item, dict)]
		except Exception as e:
			log.warning("freeAudio Internet Archive audio books: failed to load library: %s", e)

	def save(self):
		try:
			path = self._get_path()
			tmp_path = path + ".tmp"
			with open(tmp_path, "w", encoding="utf-8") as f:
				json.dump([b.to_library_dict() for b in self._books], f, ensure_ascii=False, indent=4)
			os.replace(tmp_path, path)
		except Exception as e:
			log.warning("freeAudio Internet Archive audio books: failed to save library: %s", e)

	def get_books(self):
		return list(self._books)

	def get_book_by_key(self, key):
		for book in self._books:
			if book.identity_key() == key:
				return book
		return None

	def is_in_library(self, book):
		return self.get_book_by_key(book.identity_key()) is not None

	def add_book(self, book):
		if self.is_in_library(book):
			return False
		self._books.append(book)
		self.save()
		return True

	def remove_book(self, book):
		existing = self.get_book_by_key(book.identity_key())
		if not existing:
			return False
		self._books.remove(existing)
		self.save()
		return True

	def mark_progress(self, book, chapter_index):
		existing = self.get_book_by_key(book.identity_key())
		if not existing:
			return
		existing.last_chapter_index = chapter_index
		self.save()
