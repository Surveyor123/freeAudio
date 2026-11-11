# -*- coding: utf-8 -*-
# freeAudio - Builds archive.org advancedsearch queries for the audio book
# sources (librivox.py, gutenberg_audiobooks.py).
#
# archive.org's index is queried with a quoted phrase against title/creator.
# That is exact: "Moonstone, The" finds nothing for "The Moonstone", "Alice
# Wonderland" finds nothing for "Alice's Adventures in Wonderland", and
# "Doyle, Arthur Conan" does not match "Arthur Conan Doyle". build_queries()
# returns a short list of progressively more tolerant queries; callers try
# them in order and stop at the first that returns results, so a search that
# already worked behaves exactly as before (the first query is the original
# phrase query) and the extra requests only happen when nothing was found.

import re

_STOPWORDS = frozenset({"the", "a", "an", "of", "and", "or", "not", "to", "in", "on", "by"})
_TRAILING_ARTICLE_RE = re.compile(r"^(?P<rest>.+?),\s*(?P<art>the|a|an)\s*$", re.IGNORECASE)
_HONORIFIC_RE = re.compile(r"\b(?:sir|dr|mr|mrs|ms|prof|professor|rev)\.?\s+", re.IGNORECASE)
_WORD_RE = re.compile(r"\w+", re.UNICODE)


def _phrase(text):
	"""Text made safe inside a quoted Lucene phrase."""
	return text.replace('"', "").replace("\\", " ").strip()


def _tidy_phrase(text):
	"""'Moonstone, The' -> 'The Moonstone'; 'Doyle, Arthur Conan' ->
	'Arthur Conan Doyle'; honorifics and stray punctuation removed."""
	text = _HONORIFIC_RE.sub("", text).strip()
	m = _TRAILING_ARTICLE_RE.match(text)
	if m:
		text = "%s %s" % (m.group("art"), m.group("rest"))
	elif text.count(",") == 1:
		last, first = (p.strip() for p in text.split(","))
		if last and first and len(last.split()) <= 2:
			text = "%s %s" % (first, last)
	text = re.sub(r"[^\w\s'’-]", " ", text, flags=re.UNICODE)
	return re.sub(r"\s+", " ", text).strip()


def _meaningful_words(text):
	words = []
	for w in _WORD_RE.findall(text.lower()):
		if len(w) < 2 or w in _STOPWORDS or w in words:
			continue
		words.append(w)
	return words


def build_queries(query, collection=None, base=None):
	"""Queries to try, most exact first. *collection* is the archive.org
	collection tag the source filters on; alternatively *base* is a complete
	scope clause (e.g. 'mediatype:(audio) AND subject:(audiobook)') used in
	its place. Returns [] for an empty query."""
	query = (query or "").strip()
	if not query:
		return []
	coll = base or "collection:(%s)" % collection
	queries = []

	def add(clause):
		q = "%s AND (%s)" % (coll, clause)
		if q not in queries:
			queries.append(q)

	original = _phrase(query)
	add('title:("%s") OR creator:("%s")' % (original, original))

	tidy = _phrase(_tidy_phrase(query))
	if tidy and tidy.lower() != original.lower():
		add('title:("%s") OR creator:("%s")' % (tidy, tidy))

	words = _meaningful_words(_tidy_phrase(query))
	if len(words) >= 2:
		# Every word must appear, but each may be in the title OR the
		# creator field - "Doyle Sherlock" finds Doyle's Sherlock Holmes.
		add(" AND ".join("(title:%s OR creator:%s)" % (w, w) for w in words))
	return queries
