# freeAudio — dodatek do NVDA

freeAudio to pełnowartościowy dodatek do czytnika ekranu NVDA, łączący radio internetowe, podcasty, audiobooki i lokalny jukebox. To, co zaczęło się jako prosty sposób na odtwarzanie internetowych stacji radiowych, wyrosło na kompletne, w pełni dostępne centrum słuchania — każdy ekran, okno dialogowe i kontrolka zostały zaprojektowane od podstaw z myślą o obsłudze klawiaturą i czytnikiem ekranu, bez konieczności użycia myszy w jakimkolwiek momencie.

## Co potrafi freeAudio

- **Radio internetowe** — przeglądaj i wyszukuj ponad 50 000 stacji z katalogu [Radio Browser](https://www.radio-browser.info/), z wynikami uzupełnianymi o TuneIn i iHeartRadio. Zapisuj ulubione, zmieniaj ich kolejność i przechodź do dowolnej z nich globalnym skrótem klawiszowym z dowolnego miejsca w systemie Windows — zobacz [Katalog Radio Browser](#katalog-radio-browser) i [Ulubione](#ulubione).
- **Podcasty** — subskrybuj dowolny kanał RSS/Atom albo przeszukuj katalog podcastów Apple i odsłuchuj odcinki przed subskrypcją. Pozycja odtwarzania jest zapisywana automatycznie i wznawiana w miejscu, w którym skończyłeś — zobacz [Podcasty](#podcasty).
- **Audiobooki** — wyszukuj i odtwarzaj lub pobieraj książki z trzech źródeł: [GETEM](https://getem.boun.edu.tr/), biblioteki cyfrowej Uniwersytetu Boğaziçi dla osób z dysfunkcją wzroku, [LibriVox](https://librivox.org/), wolontariackiego projektu audiobooków z domeny publicznej, oraz Open Audiobook Collection Projektu Gutenberg — dwa ostatnie nie wymagają konta — z automatycznym wznawianiem w dziełach wieloczęściowych — zobacz [Audiobooki (GETEM, LibriVox i Project Gutenberg)](#audiobooki-getem-librivox-i-project-gutenberg).
- **Lokalny Jukebox** — wyszukuj pliki audio zapisane na dowolnym podłączonym dysku według nazwy pliku albo zbuduj osobistą bibliotekę plików i folderów i odtwarzaj je z tymi samymi narzędziami wznawiania, przewijania, prędkości i wysokości dźwięku, których używają podcasty i audiobooki — zobacz [Lokalny Jukebox](#lokalny-jukebox).
- **Nagrywanie** — nagrywaj to, co gra, natychmiast, przechwytuj pojedynczy utwór automatycznie od jego początku do końca albo planuj nagrania jednorazowe i cykliczne — bez przerywania odtwarzania — zobacz [Nagrywanie](#nagrywanie).
- **Time-shift (cofanie radia na żywo)** — wstrzymuj i cofaj stację na żywo jak w DVR, a następnie wracaj do transmisji na żywo, kiedy chcesz — zobacz [Time-shift (cofanie radia na żywo)](#time-shift-cofanie-radia-na-żywo).
- **Rozpoznawanie muzyki i polubione utwory** — rozpoznawaj utwory bez metadanych za pomocą rozpoznawania opartego na Shazam, zapisuj polubione utwory do pliku tekstowego i wyszukuj ich teksty — zobacz [Rozpoznawanie muzyki](#rozpoznawanie-muzyki) i [Polubione utwory](#polubione-utwory).
- **Profile audio i efekty** — zapisuj osobne ustawienia głośności, efektów, EQ i prędkości odtwarzania dla każdej stacji, podcastu, audiobooka lub utworu z jukeboksa oraz stosuj efekty w czasie rzeczywistym (Chorus, Pogłos, wzmocnienia EQ i inne) przez backend BASS — zobacz [Profil audio stacji](#profil-audio-stacji).
- **Transpozycja (zmiana wysokości dźwięku)** — podwyższaj lub obniżaj wysokość dźwięku podcastów, audiobooków i utworów z jukeboksa bez zmiany ich prędkości, za pomocą dołączonego komponentu `bass_fx` — zobacz [Transpozycja (zmiana wysokości dźwięku)](#transpozycja-zmiana-wysokości-dźwięku).
- **Kopia dźwięku** — wysyłaj ten sam strumień jednocześnie na dwa urządzenia wyjściowe audio, na przykład na głośniki i słuchawki — zobacz [Kopia dźwięku](#kopia-dźwięku).
- **Tryb Obligato (muzyka w tle)** — odtwarzaj w pętli wybraną ulubioną stację cicho w tle, na własnym urządzeniu wyjściowym i z własną głośnością, niezależnie od tego, co gra (lub nie gra) jako główne media — zobacz [Tryb Obligato](#tryb-obligato).
- **Timery** — zaplanuj rozpoczęcie odtwarzania ulubionej stacji lub zatrzymanie odtwarzania o określonej godzinie — zobacz [Timer](#timer).
- **Głęboki dostęp z klawiatury i brajla** — każda funkcja jest dostępna wyłącznie z klawiatury, z globalnymi skrótami działającymi z dowolnego miejsca w systemie Windows, bezpośrednimi skrótami do poszczególnych ulubionych stacji oraz opcjonalnym wyjściem brajlowskim dla wszystkich komunikatów głosowych freeAudio.

## Katalog Radio Browser

freeAudio używa otwartej bazy [Radio Browser](https://www.radio-browser.info/) jako katalogu stacji. Radio Browser to bezpłatny katalog zarządzany przez społeczność, zawierający ponad 50 000 internetowych stacji radiowych z całego świata. Nie wymaga rejestracji ani konta, a jego API jest otwarte dla wszystkich. Każda stacja zawiera adres, kraj, gatunek, język i informacje o przepływności; stacje są sortowane według głosów użytkowników. freeAudio łączy się z tym API przez serwery lustrzane w Niemczech, Holandii i Austrii; jeśli jeden serwer jest niedostępny, automatycznie przełącza się na następny.

Aby przeglądarka pozostawała responsywna i nie obciążała API przy każdym wyszukiwaniu lub zmianie kraju, freeAudio przechowuje na dysku lokalną kopię (cache) katalogu stacji. Ta kopia jest automatycznie odświeżana w tle według okresowego harmonogramu, więc wyświetlana lista jest zwykle już aktualna bez żadnego działania z Twojej strony. W dowolnym momencie możesz też wymusić natychmiastową ponowną synchronizację przyciskiem **Aktualizuj listę stacji** — zobacz [Przeglądarka stacji](#przeglądarka-stacji) poniżej.

## Dodawanie stacji do Radio Browser

Jeśli szukanej stacji nie ma w katalogu Radio Browser, możesz dodać ją samodzielnie na stronie [https://www.radio-browser.info/add](https://www.radio-browser.info/add). Konto ani rejestracja nie są potrzebne.

Wypełnij formularz na tej stronie:

- **Stream URL** *(wymagane)* — bezpośredni adres URL strumienia audio, kończący się na przykład na `.mp3`, `.aac`, `.ogg` lub podobnie. Nie jest to adres strony internetowej stacji, tylko surowy adres strumienia, który można wkleić do odtwarzacza multimedialnego. Większość stacji publikuje go na swojej stronie albo w sekcji „Słuchaj na żywo”.
- **Station name** *(wymagane)* — nazwa stacji, która ma pojawić się w katalogu.
- **Homepage** — adres strony internetowej stacji.
- **Country and language** — wybierz kraj i język nadawania z list rozwijanych.
- **Tags** — słowa kluczowe gatunku lub tematu, rozdzielone przecinkami, na przykład `news`, `jazz`, `classical`. Są używane do wyszukiwania i filtrowania.
- **Logo URL** — bezpośredni link do obrazu logo stacji, jeśli jest dostępny.

Po wysłaniu stacja zostanie sprawdzona i dodana do publicznego katalogu. Po zaakceptowaniu pojawi się automatycznie w wyszukiwaniu i listach krajów freeAudio, ponieważ katalog jest odświeżany z aktywnego API.

## Wymagania

- NVDA 2025.1 lub nowszy
- Windows 10 lub nowszy
- Połączenie z internetem

## Instalacja

Pobierz plik `.nvda-addon`, naciśnij na nim Enter i uruchom NVDA ponownie, gdy pojawi się taka prośba.

## Skróty klawiszowe

Wszystkie skróty można zmienić w menu NVDA → Preferencje → Zdarzenia wejścia → freeAudio. Skróty działają z dowolnego miejsca, niezależnie od tego, które okno ma fokus.

Niektóre z tych skrótów pokrywają się ze skrótami używanymi przez sam system Windows. Jeśli wolisz zachować skrót systemu Windows bez zmieniania skrótu freeAudio, naciśnij `NVDA+F2` (przepuść następny klawisz) tuż przed daną kombinacją klawiszy — NVDA przekaże tę jedną kombinację bezpośrednio do systemu Windows, zamiast przechwytywać ją dla freeAudio.

| Skrót | Funkcja | Opis |
|---|---|---|
| `Ctrl+Win+R` | Otwórz przeglądarkę stacji | Otwiera okno przeglądarki, jeśli jest zamknięte, albo przenosi je na wierzch, jeśli jest już otwarte. |
| `Ctrl+Win+O` | Otwórz kartę Podcasty | Otwiera przeglądarkę stacji (jeśli jest zamknięta) albo przenosi ją na wierzch i przełącza bezpośrednio na kartę **Podcasty**. |
| `Ctrl+Win+L` | Otwórz kartę Audiobooki | Otwiera przeglądarkę stacji (jeśli jest zamknięta) albo przenosi ją na wierzch i przełącza bezpośrednio na kartę **Audiobooki**. |
| `Ctrl+Win+U` | Otwórz kartę Jukebox | Otwiera przeglądarkę stacji (jeśli jest zamknięta) albo przenosi ją na wierzch i przełącza bezpośrednio na kartę **Jukebox**, z fokusem w polu wyszukiwania na urządzeniach. |
| `Ctrl+Win+P` | Wstrzymaj / wznów | Wstrzymuje aktualną stację, jeśli gra; wznawia ją, jeśli jest wstrzymana. Jeśli nic nie gra, uruchamia ostatnią stację albo otwiera listę ulubionych, zależnie od ustawienia. Dwukrotne szybkie naciśnięcie przechodzi bezpośrednio do wybranej karty. Trzykrotne naciśnięcie może wywołać osobną akcję, zależnie od ustawienia. |
| `Ctrl+Win+S` | Stop | Całkowicie zatrzymuje aktualną stację i resetuje odtwarzacz. |
| `Ctrl+Win+→` | Następna ulubiona | Przechodzi do następnej stacji na liście ulubionych. Po dojściu do końca wraca na początek listy. |
| `Ctrl+Win+←` | Poprzednia ulubiona | Przechodzi do poprzedniej stacji na liście ulubionych. Na początku listy skacze na jej koniec. |
| `Ctrl+Win+↑` | Głośniej | Zwiększa głośność o 5; maksimum to 200. |
| `Ctrl+Win+↓` | Ciszej | Zmniejsza głośność o 5; minimum to 0. |
| `Ctrl+Win+V` | Dodaj do ulubionych / Pobierz media | Dodaje aktualnie odtwarzaną stację do listy ulubionych albo pobiera aktualnie odtwarzany odcinek podcastu lub audiobook. Informuje, jeśli stacja już jest na liście lub jeśli media zostały już pobrane. Nie dotyczy odtwarzania utworu z jukeboksa: freeAudio informuje wtedy, że skrót jest przeznaczony tylko dla stacji, podcastów i audiobooków. |
| `Ctrl+Win+Shift+K` | Zwiększ prędkość odtwarzania | Zwiększa prędkość odtwarzania odcinka podcastu, audiobooka lub utworu z jukeboksa o 0,1x (z zachowaniem wysokości dźwięku). Zakres: od 0,5x do 2,0x. |
| `Ctrl+Win+Shift+J` | Zmniejsz prędkość odtwarzania | Zmniejsza prędkość odtwarzania odcinka podcastu, audiobooka lub utworu z jukeboksa o 0,1x. |
| `Shift+Win+K` | Transpozycja w górę | Podwyższa wysokość dźwięku odcinka podcastu, audiobooka lub utworu z jukeboksa co 1/8 całego tonu (0,25 półtonu), bez zmiany prędkości. Zakres: od −12,00 do +12,00 półtonów. Zobacz [Transpozycja (zmiana wysokości dźwięku)](#transpozycja-zmiana-wysokości-dźwięku). |
| `Shift+Win+J` | Transpozycja w dół | Obniża wysokość dźwięku co 1/8 całego tonu, bez zmiany prędkości. |
| `Ctrl+Win+I` | Informacje o stacji | Odczytuje nazwę aktualnie odtwarzanej stacji, odcinka podcastu, audiobooka lub utworu z jukeboksa. Naciśnij dwa razy, aby pokazać szczegóły, takie jak kraj, gatunek i przepływność, w oknie dialogowym. Naciśnij trzy razy, aby skopiować informacje o aktualnym utworze, czyli metadane ICY, do schowka, jeśli są dostępne; jeśli metadanych nie ma, rozpoczyna rozpoznawanie muzyki przez Shazam. Naciśnij cztery razy, aby wymusić rozpoznawanie muzyki, gdy metadane ICY są błędne. |
| `Ctrl+Win+M` | Kopia dźwięku | Kopiuje bieżący strumień lub media równolegle na dodatkowe urządzenie wyjściowe audio. Ponowne naciśnięcie zatrzymuje kopiowanie. |
| `Ctrl+Win+Shift+M` | Tryb Obligato (muzyka w tle) | Odtwarza w pętli wybraną ulubioną stację cicho w tle, na własnym urządzeniu wyjściowym i z własną głośnością, niezależnie od tego, co gra jako główne media. Pierwsze naciśnięcie otwiera okno wyboru stacji, urządzenia wyjściowego i względnej głośności. Naciśnij ponownie, aby je zatrzymać. |
| `Ctrl+Win+E` | Nagrywanie natychmiastowe | Naciśnij raz, aby rozpocząć nagrywanie bieżącej stacji; naciśnij ponownie, aby zatrzymać. Naciśnij **dwa razy**, aby rozpocząć **nagrywanie utworu** — plik otrzyma nazwę bieżącego utworu, a nagrywanie zatrzyma się automatycznie po zmianie utworu. Dwukrotne naciśnięcie podczas aktywnego nagrywania utworu zatrzyma je wcześniej. Odtwarzanie trwa bez przerwy we wszystkich trybach nagrywania. Funkcja jest dostępna tylko dla stacji nadających metadane ICY. |
| `Ctrl+Win+W` | Otwórz folder nagrań | Otwiera w Eksploratorze plików folder z nagraniami. |
| `Ctrl+Win+J` | Cofnięcie time-shift / przewijanie wstecz w podcaście, audiobooku i jukeboksie | W radiu na żywo: cofa o 15 sekund. Pierwsze naciśnięcie wchodzi w tryb time-shift; każde kolejne cofa o kolejne 15 sekund, do limitu bufora ustawionego w ustawieniach freeAudio. Wymaga włączonego bufora time-shift w Ustawieniach. W podcaście, audiobooku lub utworze z jukeboksa ten klawisz przewija w obrębie pliku, a długość skoku zależy od sposobu naciśnięcia: **przytrzymanie** przewija wstecz o 5 sekund przy każdym powtórzeniu, tak jak dotychczas; **pojedyncze świadome naciśnięcie** cofa o 12 sekund; **dwa szybkie naciśnięcia** cofają o 1 minutę; **trzy lub więcej naciśnięć** cofa o 5 minut. Dla całej serii naciśnięć wykonywane jest tylko jedno przewinięcie, o długości odpowiadającej liczbie naciśnięć — naciśnięcia nie sumują się. Działa niezależnie od ustawienia time-shift. |
| `Ctrl+Win+K` | Przewijanie do przodu time-shift / przewijanie do przodu w podcaście, audiobooku i jukeboksie | W radiu na żywo: przewija o 15 sekund do przodu w trybie time-shift. Po osiągnięciu krawędzi na żywo odtwarzanie automatycznie wraca do live i polecenie nie działa, dopóki ponownie nie cofniesz. W podcaście, audiobooku lub utworze z jukeboksa ten klawisz przewija do przodu w obrębie pliku, z tym samym skalowaniem naciśnięć i przytrzymania co `Ctrl+Win+J` powyżej (przytrzymanie = 5 sekund na powtórzenie; 1 naciśnięcie = 12 sekund; 2 naciśnięcia = 1 minuta; 3 i więcej = 5 minut). Działa niezależnie od ustawienia time-shift. |
| `Ctrl+Win+T` | Przełącz bufor time-shift | Włącza lub wyłącza bufor time-shift na bieżąco, odzwierciedlając pole wyboru w Ustawieniach. Wyłączenie natychmiast wraca do live (jeśli w trybie time-shift) i zatrzymuje przechwytywanie w tle. Nie wpływa na odtwarzanie podcastów, audiobooków ani jukeboksa. |
| *(nieprzypisane)* | Wybierz urządzenie wyjściowe | Otwiera na żądanie listę dostępnych głównych urządzeń wyjściowych. Lista pojawia się tylko wtedy, gdy BASS wykryje więcej niż jedno fizyczne urządzenie wyjściowe. Skrót można przypisać w menu NVDA → Preferencje → Zdarzenia wejścia → freeAudio. |
| *(nieprzypisane)* | Przełącz wyciszenie powiadomień | Przełącza ustawienie Wycisz powiadomienia w locie. Przypisz skrót w menu NVDA → Preferencje → Zdarzenia wejścia → freeAudio. |
| *(nieprzypisane)* | Odtwórz ulubioną stację bezpośrednio | Każda stacja z listy ulubionych pojawia się jako osobna pozycja w menu NVDA → Preferencje → Zdarzenia wejścia → **freeAudio Stations**. Przypisz skrót klawiszowy dowolnej stacji i uruchamiaj ją natychmiast z dowolnego miejsca, bez otwierania przeglądarki. |

Skróty następnej i poprzedniej stacji poruszają się tylko po liście ulubionych; nie działają z listą wszystkich stacji. Gdy fokus znajduje się na liście w oknie przeglądarki, lewa i prawa strzałka pełnią tę samą funkcję — zobacz Skróty w oknie dialogowym.

## Przeglądarka stacji

freeAudio dodaje też podmenu **freeAudio** do menu Narzędzia NVDA. Można z niego bezpośrednio otworzyć przeglądarkę stacji i ustawienia freeAudio.

Okno otwierane skrótem `Ctrl+Win+R` zawiera osiem kart: Wszystkie stacje, Ulubione, Nagrywanie, Timer, Polubione utwory, Podcasty, Audiobooki i Jukebox. Między kartami można przełączać się skrótem `Ctrl+Tab` albo skrótami od `Alt+1` do `Alt+8`.

Po otwarciu karty Wszystkie stacje automatycznie ładowanych jest 1000 najczęściej głosowanych stacji z Radio Browser. Wybranie kraju z listy rozwijanej aktualizuje listę i pokazuje stacje z tego kraju. Pisanie w polu wyszukiwania natychmiast uruchamia pełne wyszukiwanie w całej bazie Radio Browser, jednocześnie po nazwie, kraju i gatunku.

Podczas wyszukiwania wyniki z Radio Browser są uzupełniane stacjami z TuneIn i iHeartRadio (gdy są dostępne). Te zewnętrzne źródła są przeszukiwane w tle, a ich wyniki są automatycznie dołączane do listy, dzięki czemu masz dostęp do jeszcze większej liczby stacji bez żadnych dodatkowych działań.

Lista **Urządzenie wyjściowe** na dole okna przeglądarki, poza kartami, zawiera wszystkie urządzenia audio rozpoznane przez BASS. Wybranie urządzenia natychmiast przekierowuje na nie dźwięk i zapisuje wybór na stałe; to samo urządzenie będzie użyte automatycznie w następnej sesji. Jeśli wybrane urządzenie nie jest podłączone, dodatek sam wraca do domyślnego urządzenia systemowego. Naciśnij `F11`, aby z dowolnego miejsca w Przeglądarce stacji otworzyć prostsze okno wyboru urządzenia. Nie pojawia się ono automatycznie i jest otwierane tylko wtedy, gdy BASS wykryje więcej niż jedno fizyczne urządzenie wyjściowe. Gdy dostępne jest tylko jedno urządzenie, wybór nie jest potrzebny, a freeAudio korzysta z domyślnego urządzenia systemowego.

Kontrolki **Głośność** (0–200) i **Efekty** w tym samym obszarze można zmieniać w dowolnej chwili, gdy okno jest otwarte. Z listy efektów można jednocześnie włączyć Chorus, Kompresor, Przesterowanie, Echo, Flanger, Gargle, Pogłos, EQ: wzmocnienie basu, EQ: wzmocnienie sopranów i EQ: wzmocnienie wokalu; zmiany są natychmiast stosowane do aktywnego strumienia. Każdy efekt można też natychmiast przełączyć skrótami od `Ctrl+1` do `Ctrl+0`, bez odrywania rąk od klawiatury — zobacz [Skróty efektów](#skróty-efektów).

Gdy włączony jest co najmniej jeden efekt EQ, dla każdego aktywnego pasma pojawia się **kontrolka wzmocnienia**. Wzmocnienie można ustawić od −15 dB do +15 dB; wartości domyślne to bas +9 dB, soprany +9 dB i wokal +6 dB. Kontrolki są widoczne tylko dla aktualnie zaznaczonych pasm EQ i znikają automatycznie po odznaczeniu efektu. Wartości wzmocnienia są zapisywane globalnie i przywracane w następnej sesji.

Przycisk **Odtwórz/Wstrzymaj** również znajduje się na dole okna. Jeśli nic nie gra, uruchamia zaznaczoną stację; jeśli stacja już gra, wstrzymuje odtwarzanie.

Przycisk **Aktualizuj listę stacji** natychmiast synchronizuje ponownie lokalny katalog stacji z API Radio Browser, zamiast czekać na okresowe odświeżanie w tle. Podczas odświeżania przycisk jest nieaktywny, a NVDA ogłasza, że trwa odświeżanie; jeśli naciśniesz go ponownie przed zakończeniem bieżącego odświeżania, NVDA poinformuje, że jedno jest już w toku. Po zakończeniu odświeżania NVDA ogłasza, że lista stacji została zaktualizowana, a aktualnie wyświetlane wyniki wyszukiwania lub lista danego kraju są automatycznie odświeżane, aby odzwierciedlić nowe dane.

Po zaznaczeniu stacji na liście przycisk **Szczegóły stacji** pokazuje informacje takie jak kraj, język, gatunek, format, przepływność, strona internetowa i adres URL strumienia w osobnym oknie. Każde pole znajduje się w osobnym, tylko do odczytu, polu tekstowym; można przechodzić między nimi klawiszem Tab i skopiować wszystkie informacje naraz przyciskiem **Kopiuj wszystko do schowka**. Ten przycisk jest dostępny na kartach Wszystkie stacje i Ulubione.

### Menu kontekstowe stacji

Kliknij prawym przyciskiem myszy stację na liście Wszystkie stacje lub Ulubione, albo zaznacz ją i naciśnij klawisz Menu kontekstowe (Applications) lub `Shift+F10`, aby otworzyć menu kontekstowe z szybkimi akcjami:

- **Szczegóły stacji** — to samo, co opisany wyżej przycisk Szczegóły stacji.
- **Dodaj do ulubionych** *(karta Wszystkie stacje)* / **Usuń stację** *(karta Ulubione)*.
- **Zmień nazwę stacji** *(karta Ulubione)* — to samo, co `F9`.
- **Zapisz profil audio dla tej stacji** / **Wyczyść profil audio** *(karta Ulubione)* — zobacz [Profil audio stacji](#profil-audio-stacji).
- **Testuj adres URL** — sprawdza, czy strumień wybranej stacji jest aktualnie dostępny, bez rozpoczynania odtwarzania, i ogłasza wynik (dostępny albo powód niepowodzenia, np. błąd HTTP lub przekroczenie limitu czasu sieci).

Wyświetlane są tylko pozycje odpowiednie dla bieżącej karty i zaznaczenia.

### Skróty w oknie dialogowym

Poniższe klawisze działają tylko wtedy, gdy aktywne jest okno Przeglądarka stacji.

#### Klawisze funkcyjne

| Skrót | Funkcja | Opis |
|---|---|---|
| `F1` | Pomoc | Otwiera plik pomocy dodatku w domyślnej przeglądarce. Najpierw szukana jest pomoc w aktywnym języku NVDA; jeśli jej nie ma, otwierana jest wersja domyślna. |
| `F2` | Co jest odtwarzane | Odczytuje aktualnie odtwarzaną stację i nazwę utworu. Dwukrotne naciśnięcie pokazuje szczegóły, takie jak kraj, gatunek i przepływność, w oknie dialogowym. Trzykrotne naciśnięcie kopiuje informacje o utworze, czyli metadane ICY, do schowka, jeśli są dostępne; jeśli ich nie ma, uruchamia rozpoznawanie muzyki przez Shazam. Czterokrotne naciśnięcie wymusza rozpoznawanie muzyki przy błędnych metadanych ICY. |
| `F3` | Poprzedni element | Na kartach Wszystkie stacje i Ulubione: przechodzi do poprzedniej stacji i natychmiast rozpoczyna odtwarzanie. Na karcie Podcasty: przechodzi do poprzedniego odcinka na liście odcinków i go odtwarza. Na karcie Audiobooki: przechodzi do poprzedniej książki i zaczyna ją odtwarzać. Na karcie Jukebox: przechodzi do poprzedniego utworu w zaznaczonym elemencie jukeboksa i go odtwarza. |
| `F4` | Następny element | Na kartach Wszystkie stacje i Ulubione: przechodzi do następnej stacji i natychmiast rozpoczyna odtwarzanie. Na karcie Podcasty: przechodzi do następnego odcinka i go odtwarza. Na karcie Audiobooki: przechodzi do następnej książki i zaczyna ją odtwarzać. Na karcie Jukebox: przechodzi do następnego utworu w zaznaczonym elemencie jukeboksa i go odtwarza. |
| `Shift+F3` | Poprzedni kanał / część / element | Na karcie Podcasty: przechodzi o jeden kanał w górę na liście subskrypcji. Na karcie Audiobooki: przechodzi do poprzedniej części aktualnie odtwarzanej książki. Na karcie Jukebox: przechodzi o jeden element jukeboksa (plik lub folder) w górę na liście głównej. |
| `Shift+F4` | Następny kanał / część / element | Na karcie Podcasty: przechodzi o jeden kanał w dół na liście subskrypcji. Na karcie Audiobooki: przechodzi do następnej części aktualnie odtwarzanej książki. Na karcie Jukebox: przechodzi o jeden element jukeboksa w dół na liście głównej. |
| `F5` | Ciszej | Zmniejsza głośność o 5, minimum 0. |
| `F6` | Głośniej | Zwiększa głośność o 5, maksimum 200. |
| `F7` | Wstrzymaj / wznów | Wstrzymuje, jeśli stacja gra; wznawia, jeśli odtwarzanie jest wstrzymane i media są załadowane. |
| `F8` | Stop | Całkowicie zatrzymuje aktualną stację i resetuje odtwarzacz. |
| `F9` | Zmień nazwę | Otwiera okno zmiany nazwy dla stacji z fokusem na karcie Ulubione. |
| `F11` | Wybierz urządzenie wyjściowe | Otwiera okno wyboru głównego urządzenia wyjściowego, gdy BASS wykryje więcej niż jedno fizyczne urządzenie. Bieżące urządzenie jest wstępnie zaznaczone; Enter stosuje i zapisuje wybór. |

#### Skróty listy i nawigacji

| Skrót | Funkcja | Opis |
|---|---|---|
| `→` | Następny element / przewiń do przodu | Na liście stacji (Wszystkie stacje / Ulubione) przechodzi do następnej stacji i odtwarza ją natychmiast, wracając na początek po dojściu do końca listy. Na listach elementów Podcastów, Audiobooków lub Jukeboksa, gdy coś jest załadowane i gra, zamiast tego przewija do przodu — tak samo jak globalne polecenie `Ctrl+Win+K` (zobacz Przewijanie stopniowane powyżej). Na liście odcinków Podcastów, jeśli nic jeszcze nie jest załadowane, przechodzi do następnego odcinka i go odtwarza. |
| `←` | Poprzedni element / przewiń wstecz | Na liście stacji przechodzi do poprzedniej stacji i odtwarza ją, skacząc na koniec listy po dojściu do jej początku. Na listach elementów Podcastów, Audiobooków lub Jukeboksa, gdy coś jest załadowane i gra, zamiast tego przewija wstecz — tak samo jak globalne polecenie `Ctrl+Win+J`. Na liście odcinków Podcastów, jeśli nic jeszcze nie jest załadowane, przechodzi do poprzedniego odcinka i go odtwarza. |
| `Shift+→` | Transpozycja w górę | Na listach elementów Podcastów, Audiobooków lub Jukeboksa: podwyższa wysokość bieżącego odtwarzania o półton, tak samo jak globalne polecenie `Shift+Win+K`. |
| `Shift+←` | Transpozycja w dół | Na listach elementów Podcastów, Audiobooków lub Jukeboksa: obniża wysokość bieżącego odtwarzania o półton, tak samo jak globalne polecenie `Shift+Win+J`. |
| `Page Up` | Zwiększ prędkość odtwarzania | Na listach elementów Podcastów, Audiobooków lub Jukeboksa: zwiększa prędkość odtwarzania, tak samo jak globalne polecenie `Ctrl+Win+Shift+K`. |
| `Page Down` | Zmniejsz prędkość odtwarzania | Na listach elementów Podcastów, Audiobooków lub Jukeboksa: zmniejsza prędkość odtwarzania, tak samo jak globalne polecenie `Ctrl+Win+Shift+J`. |
| `Ctrl+→` | Następny odcinek / książka / utwór | Na karcie Podcasty: przechodzi do następnego odcinka i go odtwarza. Na karcie Audiobooki (fokus na liście biblioteki): przechodzi do następnej książki. Na karcie Jukebox (fokus na liście elementów albo utworów): przechodzi do następnego utworu w zaznaczonym elemencie jukeboksa i go odtwarza. |
| `Ctrl+←` | Poprzedni odcinek / książka / utwór | Na karcie Podcasty: przechodzi do poprzedniego odcinka i go odtwarza. Na karcie Audiobooki: przechodzi do poprzedniej książki. Na karcie Jukebox: przechodzi do poprzedniego utworu w zaznaczonym elemencie jukeboksa i go odtwarza. |
| `Enter` | Odtwórz / dodaj | Na liście stacji lub odcinków: natychmiast odtwarza zaznaczony element. W wynikach wyszukiwania na karcie Jukebox: dodaje zaznaczony plik do jukeboksa. Na liście elementów lub utworów na karcie Jukebox: odtwarza zaznaczony element bezpośrednio. |
| `Space` | Odtwórz / wstrzymaj / podgląd | Wstrzymuje, jeśli coś gra; w przeciwnym razie rozpoczyna odtwarzanie zaznaczonego elementu. W wynikach wyszukiwania na karcie Jukebox: przełącza podgląd (odtwarzanie/zatrzymanie) zaznaczonego pliku. Na liście elementów lub utworów na karcie Jukebox: wstrzymuje, jeśli coś gra, w przeciwnym razie odtwarza zaznaczony element. |
| `Ctrl+Tab` | Następna karta | Przełącza na następną kartę (Wszystkie stacje → Ulubione → Nagrywanie → Timer → Polubione utwory → Podcasty → Audiobooki → Jukebox). |
| `Ctrl+Shift+Tab` | Poprzednia karta | Przełącza na poprzednią kartę. |
| `Escape` | Ukryj | Ukrywa okno; dodatek nadal odtwarza w tle. |

#### Skróty głośności

| Skrót | Funkcja | Opis |
|---|---|---|
| `Ctrl+↑` | Głośniej | Zwiększa głośność o 5. Działa tylko wtedy, gdy okno przeglądarki jest otwarte. |
| `Ctrl+↓` | Ciszej | Zmniejsza głośność o 5. Działa tylko wtedy, gdy okno przeglądarki jest otwarte. |

#### Skróty efektów

| Skrót | Funkcja | Opis |
|---|---|---|
| `Ctrl+1` | Przełącz Chorus | Włącza lub wyłącza efekt Chorus i natychmiast stosuje go do aktywnego strumienia. |
| `Ctrl+2` | Przełącz Kompresor | Włącza lub wyłącza efekt Kompresor i natychmiast stosuje go do aktywnego strumienia. |
| `Ctrl+3` | Przełącz Przesterowanie | Włącza lub wyłącza efekt Przesterowanie i natychmiast stosuje go do aktywnego strumienia. |
| `Ctrl+4` | Przełącz Echo | Włącza lub wyłącza efekt Echo i natychmiast stosuje go do aktywnego strumienia. |
| `Ctrl+5` | Przełącz Flanger | Włącza lub wyłącza efekt Flanger i natychmiast stosuje go do aktywnego strumienia. |
| `Ctrl+6` | Przełącz Gargle | Włącza lub wyłącza efekt Gargle i natychmiast stosuje go do aktywnego strumienia. |
| `Ctrl+7` | Przełącz Pogłos | Włącza lub wyłącza efekt Pogłos i natychmiast stosuje go do aktywnego strumienia. |
| `Ctrl+8` | Przełącz EQ: wzmocnienie basu | Włącza lub wyłącza pasmo EQ: wzmocnienie basu i natychmiast stosuje je do aktywnego strumienia. |
| `Ctrl+9` | Przełącz EQ: wzmocnienie sopranów | Włącza lub wyłącza pasmo EQ: wzmocnienie sopranów i natychmiast stosuje je do aktywnego strumienia. |
| `Ctrl+0` | Przełącz EQ: wzmocnienie wokalu | Włącza lub wyłącza pasmo EQ: wzmocnienie wokalu i natychmiast stosuje je do aktywnego strumienia. |

Każdy skrót odpowiada zaznaczeniu lub odznaczeniu odpowiedniej pozycji na liście **Efekty**: NVDA ogłasza, czy efekt został włączony czy wyłączony, zmiana jest zapisywana automatycznie, a kontrolka wzmocnienia dla danego pasma (jeśli dotyczy) pojawia się lub znika odpowiednio.

#### Skróty Alt

| Skrót | Funkcja | Opis |
|---|---|---|
| `Alt+R` | Przejdź do pola wyszukiwania | Przenosi fokus do pola wyszukiwania. Radio Browser przeszukuje tekst z tego pola jednocześnie po nazwie, kraju i gatunku. |
| `Alt+V` | Dodaj / usuń ulubioną | Dodaje zaznaczoną stację do ulubionych; usuwa ją, jeśli jest już na liście. |
| `Alt+1` | Wszystkie stacje | Przełącza na kartę Wszystkie stacje. |
| `Alt+2` | Ulubione | Przełącza na kartę Ulubione. |
| `Alt+3` | Nagrywanie | Przełącza na kartę Nagrywanie. |
| `Alt+4` | Timer | Przełącza na kartę Timer. |
| `Alt+5` | Polubione utwory | Przełącza na kartę Polubione utwory. |
| `Alt+6` | Podcasty | Przełącza na kartę Podcasty. |
| `Alt+7` | Audiobooki | Przełącza na kartę Audiobooki. |
| `Alt+8` | Jukebox | Przełącza na kartę Jukebox, z fokusem w polu wyszukiwania na urządzeniach. |
| `Alt+K` | Zamknij | Zamyka okno; dodatek nadal odtwarza w tle. |

## Ulubione

Lista ulubionych to osobista kolekcja stacji zapisywana na stałe. Aby dodać stację, zaznacz ją na liście i naciśnij przycisk Dodaj do ulubionych albo użyj skrótu `Alt+V`. Ten sam skrót usuwa stację, która już jest na liście, gdy jest zaznaczona.

Ulubione można odtwarzać skrótami `Ctrl+Win+→` i `Ctrl+Win+←`; działają one nawet wtedy, gdy okno przeglądarki nie jest otwarte.

Aby usunąć stację z listy ulubionych, zaznacz ją i naciśnij przycisk **Usuń stację** albo klawisz `Delete`. Po usunięciu fokus i zaznaczenie automatycznie przechodzą na następną stację na liście. Jeśli usunięto ostatnią stację, fokus przechodzi na poprzednią. Jeśli lista stanie się pusta, fokus przechodzi na przycisk Odtwórz.

### Zaznaczanie i usuwanie wielu elementów

Ulubione, Polubione utwory, biblioteka Audiobooków i lista Jukeboksa umożliwiają zaznaczenie kilku elementów i usunięcie ich razem jednym krokiem:

- Naciśnij **`.`** (kropka) na wyróżnionym elemencie, aby go zaznaczyć lub odznaczyć. NVDA ogłasza zmianę, a wiersz zaznaczonego elementu jest oznaczany jako „(zaznaczony)”, dzięki czemu jego stan pozostaje czytelny, gdy poruszasz się dalej po liście.
- Naciśnij **`Shift+Home`**, aby zaznaczyć lub odznaczyć wszystkie elementy od bieżącego do pierwszego na liście, albo **`Shift+End`**, aby zrobić to samo do ostatniego elementu. To, czy zakres zostanie zaznaczony, czy odznaczony, zależy od stanu bieżącego elementu, więc cały zakres zawsze zmienia się w jedną stronę w jednej akcji. Po wykonaniu fokus przechodzi na dalszy koniec zakresu, a NVDA ogłasza, ile elementów się zmieniło.
- Naciśnij **`Delete`**, aby usunąć wszystkie zaznaczone elementy naraz. Jeśli nic nie jest zaznaczone, `Delete` nadal usuwa tylko aktualnie wybrany element, tak jak dotychczas.
- Menu kontekstowe każdej listy (klawisz Menu kontekstowe / `Shift+F10`) zawiera polecenie **Usuń zaznaczone**, aktywne tylko wtedy, gdy zaznaczony jest co najmniej jeden element, które robi to samo.
- Przed usunięciem pojawia się jedno okno potwierdzenia podsumowujące, ile elementów zostanie usuniętych.

Zaznaczenia są przypisane do danej listy i znikają po usunięciu elementów (lub po ich indywidualnym odznaczeniu); nie są zapisywane między sesjami.

### Eksportowanie i importowanie ulubionych

Karta Ulubione zawiera dwa przyciski do tworzenia kopii zapasowej listy stacji i jej przywracania:

**Eksportuj ulubione…** — zapisuje całą listę ulubionych do pliku. Okno dialogowe zapisu umożliwia wybór jednego z dwóch formatów:
- **JSON** (`.json`) — pełna kopia zapasowa zachowująca nazwy stacji, adresy URL strumieni i wszystkie metadane. Zalecany do późniejszego przywrócenia listy lub przeniesienia jej na inny komputer.
- **Lista odtwarzania M3U** (`.m3u`) — standardowy format listy odtwarzania zgodny z większością odtwarzaczy multimedialnych i aplikacji radiowych. Należy pamiętać, że format M3U nie przechowuje wszystkich metadanych stacji, więc przywracanie z pliku M3U może skutkować mniejszą ilością szczegółów niż kopia zapasowa JSON.

**Importuj ulubione…** — ładuje stacje z wcześniej wyeksportowanego pliku JSON lub M3U. Po wybraniu pliku pojawi się pytanie o sposób dodania stacji:
- **Tak (Scal)** — dodaje importowane stacje do istniejącej listy bez usuwania bieżących ulubionych. Zduplikowane stacje nie są dodawane dwukrotnie.
- **Nie (Zastąp)** — całkowicie usuwa bieżącą listę ulubionych i zastępuje ją zawartością importowanego pliku.
- **Anuluj** — powraca do przeglądarki bez wprowadzania żadnych zmian.

Po udanym imporcie lista ulubionych, lista stacji zaplanowanych nagrań i lista stacji timera są odświeżane automatycznie.

### Porządkowanie ulubionych w grupy

Ulubione mogą należeć do folderu/grupy, pokazywanej na liście jako przyrostek „— Grupa” po nazwie stacji (na przykład „NPR Newscast — NPR”).

- **Import z M3U** — jeśli plik używa znacznika `group-title` (konwencji stosowanej przez DVBViewer i większość innych edytorów oraz odtwarzaczy M3U) do porządkowania stacji w foldery, freeAudio odczytuje go i podczas importu zachowuje grupę każdej stacji. Eksport ulubionych z powrotem do M3U zapisuje ten sam znacznik, więc struktura folderów przetrwa pełny cykl przez freeAudio.
- **Ręczne przypisywanie lub usuwanie grupy** — zaznacz jedno lub więcej ulubionych klawiszem `.` (zobacz [Zaznaczanie i usuwanie wielu elementów](#zaznaczanie-i-usuwanie-wielu-elementów) powyżej), a następnie wybierz **Przypisz do grupy…** z menu kontekstowego (klawisz Menu kontekstowe / `Shift+F10`) i wpisz nazwę grupy. Pozostaw pole puste, aby zamiast tego usunąć zaznaczone ulubione z ich grupy. Jeśli nic nie jest zaznaczone, polecenie dotyczy aktualnie wybranej ulubionej.
- **Filtrowanie według grupy** — pole Filtr nad listą ulubionych dopasowuje również nazwy grup i akceptuje wiele słów, z których każde może pasować do innego pola. Na przykład wpisanie `Houston Classical` znajdzie „Houston Public Media Classical”, chociaż ta dokładna fraza nigdzie nie występuje — „Houston” pasuje do grupy, a „Classical” do nazwy stacji.

### Zmiana kolejności ulubionych

Po zaznaczeniu stacji na karcie Ulubione naciśnij `przecinek`, aby wejść w tryb przenoszenia — usłyszysz sygnał. Przejdź strzałkami do pozycji docelowej, a następnie naciśnij `przecinek` ponownie. Stacja zostanie umieszczona w wybranym miejscu, a nowa kolejność zapisana natychmiast. Ponowne naciśnięcie przecinka w tej samej pozycji anuluje przenoszenie.

### Bezpośrednie skróty klawiszowe do ulubionych stacji

Każda stacja z listy ulubionych jest zarejestrowana jako osobny skrypt w oknie Zdarzeń wejścia NVDA, w kategorii **freeAudio Stations**. Możesz przypisać dowolny skrót klawiszowy do dowolnej stacji i nacisnąć go z dowolnego miejsca — bez konieczności otwierania okna przeglądarki.

Aby przypisać skrót:

1. Otwórz menu NVDA → Preferencje → Zdarzenia wejścia.
2. Rozwiń kategorię **freeAudio Stations**.
3. Znajdź stację po nazwie, zaznacz ją i naciśnij **Dodaj**.
4. Naciśnij żądaną kombinację klawiszy i potwierdź.

Po naciśnięciu skrótu stacja uruchamia się natychmiast. Jeśli stacja zostanie usunięta z ulubionych, jej wpis zniknie z kategorii, a przypisany skrót zostanie automatycznie wyczyszczony przez NVDA. Po dodaniu nowej stacji do ulubionych pojawia się ona w kategorii od razu — nie trzeba ponownie otwierać okna Zdarzeń wejścia.

### Dodawanie własnej stacji

Aby dodać stację, której nie ma w Radio Browser, użyj przycisku Dodaj własną stację. W wyświetlonym oknie wpisz nazwę stacji i adres URL strumienia, aby dodać ją bezpośrednio do ulubionych. Własne stacje można odtwarzać i przenosić tak samo jak pozostałe ulubione.

W tym oknie dialogowym dostępne są dwa dodatkowe przyciski:

- **Testuj adres URL** — sprawdza wpisany adres URL strumienia przed dodaniem stacji i ogłasza, czy jest on dostępny. Przydatne do wykrycia literówki lub martwego łącza, zanim trafi ono do listy ulubionych.
- **Dodaj do katalogu Radio Browser…** — otwiera [stronę zgłoszeniową Radio Browser](https://www.radio-browser.info/add) w domyślnej przeglądarce, dzięki czemu po potwierdzeniu działania stacji można podzielić się nią z szerszą społecznością Radio Browser. Zobacz sekcję [Dodawanie stacji do Radio Browser](#dodawanie-stacji-do-radio-browser) powyżej, aby dowiedzieć się, czego oczekuje formularz zgłoszeniowy.

### Profil audio stacji

Karta Ulubione zawiera dwa przyciski do zarządzania ustawieniami audio dla konkretnej stacji:

**Zapisz profil audio dla tej stacji** — zapisuje bieżący poziom głośności, aktywne efekty (chorus, EQ itd.) oraz wartości wzmocnienia EQ jako profil przypisany do konkretnej stacji. Za każdym razem, gdy ta stacja zacznie grać, zapisane ustawienia głośności, efektów i wzmocnień zostaną zastosowane automatycznie, zastępując ustawienia globalne.

**Wyczyść profil audio** — usuwa zapisany profil audio zaznaczonej stacji. Po wyczyszczeniu stacja wraca do globalnych ustawień głośności, efektów i wzmocnień EQ. Przycisk jest aktywny tylko wtedy, gdy zaznaczona stacja ma zapisany profil.

Oba przyciski znajdują się pod listą ulubionych i są aktywne tylko po zaznaczeniu stacji na liście.

## Rozpoznawanie muzyki

Trzykrotne naciśnięcie `Ctrl+Win+I` uruchamia rozpoznawanie muzyki przez Shazam dla aktualnie odtwarzanego strumienia. Rozpoznawanie zaczyna się tylko wtedy, gdy nie są dostępne metadane ICY, czyli informacje o utworze nadawane przez stację; jeśli metadane są dostępne, zostaną zamiast tego skopiowane do schowka.

Rozpoznawanie działa tak: krótka próbka audio jest przechwytywana ze strumienia przy użyciu ffmpeg, stosowany jest algorytm odcisku audio Shazama, a wynik wysyłany jest na serwery Shazama. Jeśli rozpoznawanie się powiedzie, NVDA odczyta tytuł utworu, wykonawcę, album i rok wydania oraz automatycznie skopiuje je do schowka. Jeśli opcja **Zapisuj polubione utwory do pliku tekstowego** jest włączona, wynik zostanie też dopisany do `likedSongs.txt`.

**Informacja dźwiękowa:** dwa rosnące sygnały oznaczają start rozpoznawania, a dwa opadające sygnały jego koniec. Krótki sygnał jest odtwarzany co 2 sekundy, gdy proces trwa.

**Wymaganie:** potrzebny jest `ffmpeg.exe`. Plik `ffmpeg.exe` umieszczony w folderze dodatku zostanie użyty automatycznie; jeśli znajduje się gdzie indziej, ścieżkę można ustawić w Ustawieniach. Pobierz ffmpeg ze strony [ffmpeg.org](https://ffmpeg.org/download.html).

**Uwaga dotycząca stacji wstawiających reklamy:** niektóre stacje wysyłają krótką reklamę do każdego nowego połączenia nawiązanego z ich strumieniem, oddzielnie od audycji, której już słuchasz. Rozpoznawanie unika próbkowania tej reklamy, ponownie wykorzystując istniejące połączenie freeAudio ze strumieniem w tle (to samo, które jest używane dla [Time-shift (cofanie radia na żywo)](#time-shift-cofanie-radia-na-żywo)) zamiast otwierać nowe, dzięki czemu rozpoznaje to, co faktycznie gra, a nie reklamę. Działa to automatycznie i nie wymaga konfiguracji.

## Kopia dźwięku

Skrót `Ctrl+Win+M` kopiuje aktualnie odtwarzany strumień na drugie urządzenie wyjściowe audio równocześnie z głównym odtwarzaniem. Przydaje się to do słuchania na dwóch różnych urządzeniach jednocześnie, na przykład przez głośniki i słuchawki.

Po pierwszym naciśnięciu pojawia się okno wyboru z listą dostępnych urządzeń wyjściowych. Po wybraniu urządzenia rozpoczyna się kopiowanie, a główne odtwarzanie trwa bez przerwy. Ponowne naciśnięcie skrótu zatrzymuje kopiowanie.

**Przykłady użycia:**
- **Głośniki + słuchawki** — pozwól drugiej osobie słuchać tej samej audycji w słuchawkach, podczas gdy Ty słuchasz przez głośniki komputera.
- **Konfiguracja nagrywania** — skieruj główne wyjście na głośniki, a drugie na zewnętrzny rejestrator albo interfejs audio w celu zewnętrznego nagrywania.
- **Kilka pomieszczeń** — odtwarzaj równocześnie przez głośnik Bluetooth i wbudowany głośnik; bez dodatkowego oprogramowania, aby przenieść dźwięk do innego pomieszczenia.
- **Monitorowanie zdalne** — podczas udostępniania ekranu albo pracy przez zdalny pulpit strumień może być słyszany jednocześnie po stronie lokalnej i zdalnej.

## Tryb Obligato

Skrót `Ctrl+Win+Shift+M` odtwarza ulubioną stację cicho w tle, na zupełnie osobnym silniku audio niż główny odtwarzacz — jak delikatne tło muzyczne grające pod tym, co akurat robisz.

Po pierwszym naciśnięciu otwiera się okno z trzema kontrolkami:

- **Stacja w tle** — lista Twoich ulubionych stacji, z której wybierasz, która ma grać w pętli w tle. Wymaga co najmniej jednej ulubionej; jeśli lista ulubionych jest pusta, freeAudio informuje, że najpierw trzeba dodać stację (`Ctrl+Win+V`, gdy stacja gra).
- **Wyjście audio** — urządzenie, przez które gra stacja w tle: **Takie samo jak główne wyjście** (domyślnie), **Domyślne systemowe** albo dowolne konkretne urządzenie widoczne dla freeAudio.
- **Głośność w tle** — jak głośno gra stacja w tle, jako procent bieżącej głośności głównego odtwarzacza (25%, 50%, 75%, 100%, 125% lub 150%). Twoje wybory są zapamiętywane na przyszłość.

Po uruchomieniu stacja w tle gra niezależnie od głównego odtwarzacza — przełączanie stacji, podcastów lub audiobooków w głównym odtwarzaczu albo jego całkowite zatrzymanie nie przerywa trybu Obligato. Dwie rzeczy pozostają automatycznie powiązane z głównym odtwarzaczem:

- **Głośność** — głośność w tle jest stale utrzymywana na wybranym procencie aktualnej głośności głównego odtwarzacza, więc zwiększanie lub zmniejszanie głośności głównej (`Ctrl+Win+↑`/`↓`) skaluje muzykę w tle w ten sam sposób.
- **Pauza** — wstrzymanie głównego odtwarzacza (`Ctrl+Win+P`) wstrzymuje też stację w tle, a wznowienie głównego odtwarzacza ją wznawia. Pełne zatrzymanie głównego odtwarzacza nie jest traktowane jako pauza, więc stacja w tle gra dalej.

Naciśnij `Ctrl+Win+Shift+M` ponownie w dowolnym momencie, aby zatrzymać tryb Obligato.

## Nagrywanie

Nagrania są domyślnie zapisywane w `Documents\freeAudio Recordings\`. Nazwa pliku zawiera nazwę stacji albo tytuł utworu w trybie nagrywania utworu oraz czas rozpoczęcia nagrywania. Folder nagrań można w dowolnej chwili zmienić w menu NVDA → Preferencje → Ustawienia → freeAudio → **Folder nagrań**.

Ustawienie **Format zapisu nagrań** określa sposób zapisywania zakończonych nagrań:
- **Oryginalny format strumienia** zapisuje transmisję dokładnie tak, jak została odebrana. Dlatego transmisja HLS może utworzyć plik `.ts`.
- **Tylko dźwięk, oryginalny kodek** usuwa warstwę obrazu lub kontenera bez ponownego kodowania dźwięku. Na przykład dźwięk AAC z nagrania HLS w pliku `.ts` jest zwykle zapisywany jako `.m4a`, z zachowaniem jakości transmisji.
- **MP3** po zakończeniu nagrania konwertuje dźwięk z wybraną przepływnością. Konwersja korzysta z pliku `ffmpeg.exe` dołączonego do freeAudio i działa w tle, aby NVDA pozostawał responsywny. Jeśli konwersja się nie powiedzie, zachowany zostanie plik oryginalny.

**Nagrywanie natychmiastowe:** podczas odtwarzania stacji naciśnij `Ctrl+Win+E` raz. Naciśnij ponownie, aby zatrzymać. Odtwarzanie trwa bez przerwy.

**Nagrywanie utworu:** naciśnij `Ctrl+Win+E` **dwa razy** szybko, gdy gra stacja nadająca metadane ICY. Nagrywanie rozpoczyna się natychmiast i otrzymuje nazwę bieżącego tytułu. Po zmianie utworu nagrywanie zatrzymuje się automatycznie, a NVDA ogłasza zapisaną nazwę pliku. Jeśli chcesz zakończyć wcześniej, zanim utwór się skończy, naciśnij `Ctrl+Win+E` dwa razy ponownie. Jeśli bieżąca stacja nie nadaje metadanych ICY, nagrywanie utworu jest niedostępne i NVDA o tym poinformuje.

**Nagrywanie zaplanowane:** otwórz kartę Nagrywanie w przeglądarce. Wybierz stację z ulubionych, wpisz godzinę rozpoczęcia w formacie GG:MM i czas trwania w minutach, wybierz jeden lub więcej aktywnych dni, a następnie ustaw tryb powtarzania i tryb nagrywania:

Pole **Filtr** nad listą stacji pozwala zawężać listę ulubionych w czasie rzeczywistym, aby szybko znaleźć stację, którą chcesz zaplanować.

**Aktywne dni:** zaznacz jeden lub więcej dni tygodnia. W trybie jednorazowym dla każdego wybranego dnia tworzona jest osobna pozycja, ustawiona na najbliższe wystąpienie tego dnia. W trybie cyklicznym nagrywanie powtarza się tylko w zaznaczonych dniach. Jeśli nie zaznaczono żadnych dni, nagrywanie nie jest ograniczone do konkretnych dni.

**Tryb powtarzania:**
- **Nagraj raz** — nagrywa jednorazowo w każdym wybranym dniu. Każda pozycja jest ustawiona na najbliższe wystąpienie tego dnia; jeśli dzisiejsza godzina już minęła, pozycja jest automatycznie przenoszona na ten sam dzień następnego tygodnia.
- **Powtarzaj co tydzień** — powtarza się co tydzień w wybranych aktywnych dniach, dopóki nie zostanie usunięte z listy harmonogramu.

**Zapisz nagranie w:** dla każdego zaplanowanego nagrania możesz wybrać zapis w domyślnym folderze nagrań albo we własnym folderze. Przycisk **Przeglądaj...** pozwala wybrać folder interaktywnie. Jeśli wybrany folder stanie się niedostępny, nagranie zostanie zapisane w folderze domyślnym, a Ty zostaniesz o tym powiadomiony.

**Tryb nagrywania:**
- **Nagrywaj podczas słuchania** — odtwarza i nagrywa jednocześnie przez backend BASS.
- **Tylko nagrywaj** — nagrywa cicho w tle bez wyjścia audio; silnik nagrywania łączy się bezpośrednio ze strumieniem.

Po dodaniu harmonogramu pojawia się on na liście poniżej. Przycisk **Usuń zaznaczone** usuwa harmonogram, a **Edytuj zaznaczone** pozwala zmienić jego godzinę, czas trwania, tryb powtarzania, aktywne dni, tryb nagrywania lub folder docelowy.

NVDA ogłasza rozpoczęcie i zakończenie nagrywania. Jeśli NVDA zostanie uruchomiony ponownie podczas aktywnego zaplanowanego nagrywania, nagrywanie zostanie automatycznie wznowione po uruchomieniu.

Podobnie jak rozpoznawanie muzyki, nagrywanie natychmiastowe i nagrywanie utworu ponownie wykorzystują istniejące połączenie freeAudio ze strumieniem w tle, gdy jest dostępne, zamiast otwierać nowe, dzięki czemu nagranie rejestruje to, co faktycznie jest nadawane, nawet na stacjach, które w przeciwnym razie wysłałyby świeżą reklamę do nowego połączenia. Nie dotyczy to zaplanowanych nagrań w trybie **Tylko nagrywaj**, ponieważ w chwili ich rozpoczęcia żadna stacja jeszcze nie gra.

## Time-shift (cofanie radia na żywo)

Time-shift pozwala cofnąć aktualnie słuchaną stację jak DVR lub kaseta magnetofonowa — zatrzymaj chwilę, cofnij się o kilka minut i dogoń transmisję na żywo, kiedy chcesz. Odtwarzanie nie musi się zatrzymywać: cofanie i przewijanie do przodu odbywają się natychmiast na tym samym strumieniu audio.

Ta funkcja jest **domyślnie wyłączona**. Włącz ją w menu NVDA → Preferencje → Ustawienia → freeAudio → **Włącz bufor time-shift (cofanie radia na żywo)** lub przełącz natychmiast w dowolnym momencie za pomocą `Ctrl+Win+T`.

> **Uwaga:** freeAudio utrzymuje teraz niewielkie przechwytywanie aktualnie odtwarzanej stacji w tle przez cały czas — nie tylko wtedy, gdy to ustawienie jest włączone — ponieważ zarówno [Rozpoznawanie muzyki](#rozpoznawanie-muzyki), jak i [Nagrywanie](#nagrywanie) polegają na nim w kwestii opisanego w tych sekcjach unikania reklam. Gdy to ustawienie jest **wyłączone**, przechwytywanie w tle jest ograniczone do mniej więcej ostatnich 45 sekund, a `Ctrl+Win+J`/`Ctrl+Win+K` pozostają niedostępne — zmienia się tylko rozmiar bufora, a nie to, czy działa. Włączenie tego ustawienia powiększa to samo przechwytywanie do pełnego bufora cofania opisanego niżej.

### Jak to działa

Po włączeniu freeAudio ciągle przechwytuje aktualnie odtwarzaną stację do lokalnego, obracającego się bufora w tle, niezależnie od normalnego odtwarzania. Bufor przechowuje mniej więcej **ostatnie minuty** audio; starsze audio jest automatycznie usuwane z przodu wraz z napływaniem nowego, dzięki czemu bufor zawsze reprezentuje „niedawną przeszłość” względem krawędzi na żywo.
Czas bufora określa się w ustawieniach.

- **`Ctrl+Win+J`** — cofnij o 15 sekund. Pierwsze naciśnięcie przełącza z odtwarzania na żywo na odtwarzanie z time-shiftem, zaczynając 15 sekund za krawędzią na żywo. Każde kolejne naciśnięcie cofa o kolejne 15 sekund, do limitu bufora.
- **`Ctrl+Win+K`** — przewiń do przodu o 15 sekund w trybie time-shift. Po osiągnięciu krawędzi na żywo odtwarzanie automatycznie przełącza się z powrotem do strumienia na żywo, a NVDA ogłasza „Powrót do transmisji na żywo” — nie musisz robić nic więcej, aby wrócić do normalnego słuchania.
- **`Ctrl+Win+T`** — włącza lub wyłącza całą funkcję. Wyłączenie w trybie time-shift natychmiast wraca do live i zatrzymuje przechwytywanie w tle dla bieżącej stacji.

Przechwytywanie w tle działa przez cały czas, gdy jesteś w time-shifcie, więc krawędź na żywo przesuwa się do przodu, nawet gdy słuchasz czegoś sprzed kilku minut — dokładnie jak prawdziwy DVR.

### Włączenie i rozgrzewanie bufora

Bufor zaczyna się wypełniać, gdy tylko stacja zaczyna grać (po włączeniu funkcji) lub w momencie, gdy włączasz funkcję już podczas słuchania stacji. Dlatego cofanie jest możliwe dopiero po rzeczywistym przechwyceniu kilku sekund audio — jeśli naciśniesz `Ctrl+Win+J` natychmiast po przełączeniu stacji, NVDA poinformuje, że w buforze nie ma jeszcze wystarczająco dużo audio. Poczekaj kilka sekund i spróbuj ponownie.

Przełączenie na inną stację zawsze restartuje bufor dla nowej stacji; zbuforowane audio poprzedniej stacji jest odrzucane.

### Obsługiwane strumienie

Time-shift działa z tą samą gamą strumieni, które freeAudio już obsługuje:

- Zwykłe strumienie HTTP/HTTPS (MP3, AAC, OGG itd.), w tym serwery w stylu Shoutcast/Icecast.
- **Strumienie HLS (`.m3u8`)** — freeAudio rozwiązuje główną playlistę stacji, śledzi playlistę mediów i pobiera segmenty w tle, aby bufor był stale wypełniony, tak samo jak w przypadku zwykłych strumieni.

W rzadkim przypadku, gdy playlista stacji nie może zostać w ogóle odczytana (np. uszkodzony lub niedostępny manifest `.m3u8`), NVDA poinformuje, że cofanie nie jest dostępne dla tej konkretnej stacji.

### Wymagania i ograniczenia

- **Wymaga backendu BASS**, którego freeAudio zawsze używa do odtwarzania (zobacz [Odtwarzanie](#odtwarzanie)).
- Czas bufora określa się w ustawieniach.
- Bufor jest przypisany do stacji: zmiana stacji, zatrzymanie odtwarzania lub restart NVDA czyści go i zaczyna od nowa.
- Odtwarzanie z time-shiftem używa własnego lokalnego pliku bufora i nie tworzy zapisanego nagrania — jeśli chcesz trwale zachować audio, użyj również Nagrywania natychmiastowego (`Ctrl+Win+E`).

## Timer

Otwórz kartę Timer w przeglądarce stacji (`Alt+4`). Można dodać dwa typy timerów:

Podczas wybierania stacji dla timera alarmowego pole **Filtr** nad listą stacji pozwala zawężać listę ulubionych w czasie rzeczywistym.

**Alarm — uruchom radio:** automatycznie zaczyna odtwarzać wybraną stację z ulubionych o wskazanej godzinie. Wybierz stację i wpisz czas w formacie GG:MM.

**Uśpienie — zatrzymaj radio:** zatrzymuje odtwarzanie o wskazanej godzinie. Po uruchomieniu timera głośność jest stopniowo zmniejszana przez 60 sekund, zanim odtwarzanie zostanie zatrzymane. Nie trzeba wybierać stacji; wystarczy wpisać czas.

Dla obu typów, jeśli podana godzina już minęła, akcja zostanie zaplanowana na następny dzień. Jeśli o tej samej godzinie istnieje już timer (niezależnie od typu), dodanie nowego jest zablokowane; zostaniesz poinformowany o konflikcie i poproszony o usunięcie istniejącej pozycji. Oczekujące timery są widoczne na karcie; zaznacz jeden i naciśnij przycisk Usuń wybrany timer, aby go anulować.

**Timery cykliczne:** w polu **Powtarzanie** wybierz **Powtarzaj co tydzień** zamiast domyślnej opcji jednorazowej, aby timer uruchamiał się co tydzień, a nie jednorazowo. Lista **Aktywne dni** pozwala wtedy wybrać dni tygodnia, w które timer się powtarza; pozostawienie wszystkich dni niezaznaczonych powtarza go codziennie. Timer cykliczny uruchamia się zgodnie z harmonogramem, dopóki nie usuniesz go z listy oczekujących timerów — nie jest jednorazową pozycją, która znika po uruchomieniu.

## Podcasty

freeAudio zawiera pełnowartościowy odtwarzacz podcastów. Możesz subskrybować dowolny kanał podcastu RSS lub Atom, przeglądać odcinki, odtwarzać je, pobierać i wznawiać odtwarzanie od miejsca, w którym skończyłeś — wszystko w pełni dostępne.

### Dostęp do karty Podcasty

Otwórz przeglądarkę stacji skrótem `Ctrl+Win+R` i przełącz się na kartę **Podcasty** za pomocą `Ctrl+Tab` lub `Alt+6`. Karta składa się z trzech głównych obszarów:

1. **Wyszukiwanie i dodawanie** — górna część do odkrywania nowych podcastów, wraz z listą podglądu pokazującą odcinki aktualnie zaznaczonego wyniku wyszukiwania.
2. **Subskrypcje** — lista subskrybowanych kanałów.
3. **Odcinki** — lista odcinków zaznaczonego kanału, z kontrolkami odtwarzania.

### Dodawanie kanału podcastu

Kanał podcastu można dodać na dwa sposoby:

**Przez adres URL:**
- W polu **Szukaj** wklej pełny adres URL kanału RSS lub Atom (np. `https://example.com/feed.xml`).
- Naciśnij Enter.
- freeAudio pobiera kanał, sprawdza go i dodaje do Twoich subskrypcji. Jeśli kanał jest poprawny, usłyszysz potwierdzenie z tytułem kanału. Jeśli się nie powiedzie, komunikat o błędzie wyjaśni dlaczego.

**Przez wyszukiwanie:**
- W polu **Szukaj** wpisz słowo kluczowe (tytuł podcastu, temat lub nazwę prowadzącego) i naciśnij Enter.
- freeAudio przeszukuje katalog podcastów iTunes i wyświetla pasujące podcasty na liście **Wyniki wyszukiwania**.
- Zaznaczenie wyniku pobiera ten kanał w tle i wyświetla jego odcinki na liście **Odcinki w zaznaczonym wyniku** tuż poniżej, dzięki czemu możesz zobaczyć, co faktycznie zawiera audycja, zanim zdecydujesz się na subskrypcję — zobacz [Podgląd odcinków przed subskrypcją](#podgląd-odcinków-przed-subskrypcją) poniżej.
- Gdy będziesz zadowolony z tego, co widzisz, zaznacz wynik i naciśnij `Enter` albo otwórz jego menu kontekstowe (klawisz Menu kontekstowe / `Shift+F10` lub prawy przycisk myszy) i wybierz **Subskrybuj**, aby dodać go do subskrypcji. Kanał jest dodawany natychmiast i pojawia się na liście subskrypcji. Nie ma osobnego przycisku „Dodaj zaznaczone z wyszukiwania” — jedynym sposobem subskrypcji z wyników wyszukiwania jest `Enter` lub menu kontekstowe, co utrzymuje interfejs czytelny i dostępny.

> **Wskazówka:** Adres URL kanału możesz też wpisać bezpośrednio w polu wyszukiwania — jeśli wygląda na poprawny adres URL, dodatek spróbuje dodać go jako kanał bez wyszukiwania.

**Menu kontekstowe wyników wyszukiwania:** kliknij prawym przyciskiem myszy wynik wyszukiwania albo zaznacz go i naciśnij klawisz Menu kontekstowe / `Shift+F10`, aby otworzyć menu z jedną akcją **Subskrybuj**, identyczną z naciśnięciem `Enter` na wyniku.

### Podgląd odcinków przed subskrypcją

Zanim zdecydujesz się na subskrypcję, możesz odsłuchać odcinki podcastu bezpośrednio z wyników wyszukiwania. Za każdym razem, gdy zaznaczysz podcast na liście **Wyniki wyszukiwania**, freeAudio pobiera ten kanał i pokazuje jego odcinki — tytuł i datę publikacji — na liście **Odcinki w zaznaczonym wyniku** poniżej.

- Zaznacz odcinek na liście podglądu i naciśnij `Enter` albo otwórz jego menu kontekstowe (klawisz Menu kontekstowe / `Shift+F10` lub prawy przycisk myszy) i wybierz **Podgląd**, aby zacząć go odtwarzać w normalnym odtwarzaczu. Wszystkie zwykłe kontrolki odtwarzania (pauza, głośność, time-shift itd.) działają na nim dokładnie tak samo jak na każdej innej stacji lub odcinku.
- Podczas podglądu odcinka to samo menu kontekstowe pokazuje **Zatrzymaj podgląd** zamiast **Podgląd** — wybierz tę pozycję albo naciśnij ponownie `Enter` na tym odcinku, aby zatrzymać.
- Podgląd nie subskrybuje niczego; służy wyłącznie do posłuchania przed decyzją. Sama lista podglądu jest tymczasowa — jest zastępowana, gdy tylko zaznaczysz inny wynik wyszukiwania, i nie jest nigdzie zapisywana tak jak Twoje faktyczne subskrypcje.

### Zarządzanie subskrypcjami

Po dodaniu kilku kanałów pojawiają się one na liście **Subskrypcje**. Każda pozycja pokazuje tytuł kanału i liczbę dostępnych odcinków.

- **Zaznacz kanał**, aby zobaczyć jego odcinki na liście poniżej. Tylko do odczytu pole tekstowe **Szczegóły kanału** pod listą subskrypcji pokazuje tytuł kanału, autora, opis, liczbę odcinków i adres URL.
- **Odśwież kanał** — zaznacz go i naciśnij przycisk **Odśwież kanał** (dostępny przez menu kontekstowe, zobacz niżej), aby pobrać najnowsze odcinki. Wszystkie kanały są też automatycznie odświeżane w tle po otwarciu karty Podcasty, więc zwykle widzisz najnowsze odcinki bez ręcznej interwencji.
- **Usuń kanał** — zaznacz go i naciśnij `Delete` albo użyj menu kontekstowego, aby usunąć go z subskrypcji. Przed usunięciem zostaniesz poproszony o potwierdzenie.

**Menu kontekstowe kanałów:** kliknij prawym przyciskiem myszy kanał albo zaznacz go i naciśnij klawisz Menu kontekstowe / `Shift+F10`, aby otworzyć menu z pozycjami:
- **Odśwież kanał** — pobierz nowe odcinki teraz.
- **Zapisz profil audio dla tego podcastu** / **Wyczyść profil audio** — zobacz [Profil audio podcastu](#profil-audio-podcastu).
- **Usuń kanał** — usuń subskrypcję.
- **Kopiuj adres URL kanału** — skopiuj adres URL kanału do schowka.

### Przeglądanie i odtwarzanie odcinków

Zaznacz kanał na liście subskrypcji; jego odcinki pojawią się na liście **Odcinki** poniżej. Każdy odcinek pokazuje:
- Numer odcinka (1 = najstarszy odcinek w kanale, numeracja rośnie do najnowszego).
- Datę publikacji (jeśli jest dostępna).
- Tytuł.
- Przedrostek **„Przesłuchany”**, jeśli odcinek został w pełni odtworzony.
- Przyrostek z czasem trwania: całkowity czas (jeśli nigdy nie odtwarzano) albo postęp upłynęło/łącznie (jeśli odtworzono częściowo).

**Odtwarzanie:**
- Zaznacz odcinek i naciśnij `Enter` lub `Space`, aby go odtworzyć. Jeśli odcinek był wcześniej częściowo odtwarzany, wznawia od miejsca, w którym skończyłeś.
- Wiersz *nie* aktualizuje się podczas odtwarzania odcinka — jest to celowe, aby NVDA nie odczytywał wielokrotnie wiersza, na którym się znajdujesz. Jego flaga „Przesłuchany” i czas trwania są odświeżane natychmiast po wstrzymaniu odcinka albo gdy się skończy, więc wyświetlane dane są zawsze dokładne dokładnie wtedy, gdy mają znaczenie; po prostu nie odliczają sekund podczas odtwarzania.
- Użyj `F3` / `F4` na karcie Podcasty, aby przejść do poprzedniego / następnego odcinka i natychmiast go odtworzyć. Możesz też użyć `←` / `→`, gdy fokus jest na liście odcinków, albo `Ctrl+←` / `Ctrl+→` w dowolnym miejscu karty Podcasty — oba sposoby działają identycznie.
- Użyj `Shift+F3` / `Shift+F4`, aby przechodzić między kanałami bez odtwarzania odcinków.
- Naciśnij `Space` podczas odtwarzania odcinka, aby wstrzymać lub wznowić odtwarzanie.

**Wznawianie odtwarzania:** freeAudio zapisuje Twoją pozycję w każdym odcinku podcastu automatycznie — natychmiast po wstrzymaniu lub zakończeniu odcinka oraz co 15 sekund w tle, gdy dalej słuchasz, więc awaria lub nieoczekiwany restart nie spowoduje utraty dużej części postępu. Jeśli zatrzymasz lub wstrzymasz odtwarzanie i wrócisz później, odcinek wznowi się od zapisanej pozycji. Jeśli odtworzysz odcinek do samego końca (w ostatnich 3 sekundach), zostanie oznaczony jako „Przesłuchany” i nie będzie wznawiany — następnym razem zacznie się od początku, a na liście pojawi się przedrostek „Przesłuchany”.

**Menu kontekstowe odcinków:** kliknij prawym przyciskiem myszy odcinek albo zaznacz go i naciśnij klawisz Menu kontekstowe / `Shift+F10`, aby otworzyć menu z pozycjami:
- **Odtwórz odcinek** — rozpocznij odtwarzanie.
- **Pobierz odcinek** — pobierz plik odcinka do folderu nagrań.
- **Zapisz profil audio dla tego podcastu** / **Wyczyść profil audio** — te same polecenia co w menu kontekstowym kanału, umieszczone tu dla wygody, aby nie trzeba było wracać do listy subskrypcji. Nadal zapisują jeden profil dla całego podcastu, a nie osobny dla tego odcinka — zobacz [Profil audio podcastu](#profil-audio-podcastu).
- **Kopiuj adres URL odcinka** — skopiuj bezpośredni adres URL audio do schowka.

### Pobieranie odcinków

Zaznacz odcinek i kliknij przycisk **Pobierz odcinek** (albo użyj menu kontekstowego). Odcinek zostanie pobrany do folderu nagrań (domyślnie `Documents\freeAudio Recordings\`). Nazwa pliku jest oparta na tytule odcinka i wykrytym rozszerzeniu pliku (`.mp3`, `.m4a`, `.ogg` itd.). NVDA ogłasza rozpoczęcie i zakończenie pobierania. Jeśli plik już istnieje, zostaniesz o tym poinformowany, a pobieranie zostanie pominięte.

### Filtrowanie odcinków

Nad listą odcinków znajduje się pole **Filtr**. Podczas pisania lista odcinków jest filtrowana w czasie rzeczywistym i pokazuje odcinki, których tytuł zawiera wpisany tekst lub których numer dokładnie mu odpowiada — więc wpisanie `47` przenosi od razu do odcinka 47, nawet jeśli „47” nie występuje nigdzie w jego tytule. NVDA ogłasza liczbę pasujących odcinków po każdej zmianie. Naciśnij strzałkę `w dół` w polu filtru, aby przenieść fokus bezpośrednio do przefiltrowanej listy.

### Szczegóły odtwarzania podcastów

Odcinki podcastów są odtwarzane przez **backend BASS** (ten sam silnik, który obsługuje strumienie radiowe i — w tej wersji — jedyny backend odtwarzania używany przez freeAudio). Ponieważ odcinki są pobierane progresywnie i można w nich przewijać, podczas odtwarzania podcastu możesz używać skrótów cofania/przewijania time-shift (`Ctrl+Win+J`/`Ctrl+Win+K`), aby przewijać w obrębie odcinka. Pozycja jest zapisywana automatycznie, więc możesz wznowić później.

**Przewijanie stopniowane:** w przeciwieństwie do stałego 15-sekundowego cofania w radiu na żywo, przewijanie w podcaście, audiobooku lub utworze z jukeboksa zależy od sposobu naciśnięcia klawisza, dzięki czemu możesz wykonać małą korektę albo skoczyć daleko bez wielokrotnych naciśnięć:

- **Przytrzymanie klawisza** (autopowtarzanie) przewija wstecz lub do przodu o **5 sekund** przy każdym powtórzeniu — tyle samo, ile ten skrót zawsze robił dla plików.
- **Jedno świadome naciśnięcie** przewija o **12 sekund**.
- **Dwa naciśnięcia** w krótkim odstępie przewijają o **1 minutę**.
- **Trzy lub więcej naciśnięć** przewija o **5 minut**; kolejne naciśnięcia w tej samej serii nie zwiększają już skoku.

Świadome naciśnięcie jest przez krótką chwilę wstrzymywane, zanim faktycznie przewinie, na wypadek gdyby miało nastąpić kolejne — dla całej serii naciśnięć wykonywane jest tylko jedno przewinięcie, o długości odpowiadającej ostatecznej liczbie naciśnięć, a nie sumie ich wartości. Po przewinięciu NVDA ogłasza uzyskaną pozycję upłynęło/pozostało w odcinku, a nie tylko „X sekund do przodu/wstecz”.

**Prędkość odtwarzania:** prędkość odtwarzania odcinków podcastów, audiobooków i utworów z jukeboksa można zmieniać skrótami `Ctrl+Win+Shift+K` (szybciej) i `Ctrl+Win+Shift+J` (wolniej). Prędkość zmienia się co 0,1x, w zakresie od 0,5x do 2,0x, z zachowaniem wysokości dźwięku.

**Transpozycja (zmiana wysokości dźwięku):** niezależnie od prędkości odtwarzania możesz podwyższać lub obniżać wysokość dźwięku odcinka podcastu, audiobooka lub utworu z jukeboksa skrótami `Shift+Win+K` / `Shift+Win+J` — zobacz [Transpozycja (zmiana wysokości dźwięku)](#transpozycja-zmiana-wysokości-dźwięku).

**Dźwięk wznowienia:** za każdym razem, gdy odcinek jest wznawiany od zapisanej pozycji, freeAudio na krótko odtwarza na osobnym kanale cichy dźwięk wkładanej kasety, podczas gdy przewija do zapisanego miejsca, zamiast pozwalać, aby własne audio odcinka było w międzyczasie słyszalnie odtwarzane od 0:00. Jest to niezależne od ustawienia **Sposób przełączania stacji** — to ustawienie dotyczy tylko przełączania między stacjami radiowymi na żywo, a nie wznawiania podcastów lub audiobooków.

### Profil audio podcastu

Kliknij prawym przyciskiem myszy podcast na liście Subskrypcje albo dowolny z jego odcinków i wybierz **Zapisz profil audio dla tego podcastu**, aby zapisać bieżącą głośność, efekty, wzmocnienia EQ i/lub prędkość odtwarzania jako profil przypisany do tego podcastu. Za każdym razem, gdy odtwarzany jest dowolny odcinek tego podcastu, zapisane ustawienia są stosowane automatycznie, zastępując ustawienia globalne. Ponieważ polecenie jest dostępne zarówno w menu kontekstowym kanału, jak i odcinka, możesz je wywołać bez wracania do listy subskrypcji — w obu przypadkach zapisuje ono jeden profil dla całego podcastu, a nie osobny dla każdego odcinka.

Okno z 15 opcjami pozwala wybrać dokładnie, co zapisać:
- **Tylko głośność**
- **Tylko efekty**
- **Głośność i efekty**
- **Głośność i prędkość odtwarzania**
- **Efekty i prędkość odtwarzania**
- **Tylko prędkość odtwarzania**
- **Głośność, efekty i prędkość odtwarzania**
- **Tylko transpozycja wysokości**
- **Głośność i transpozycja wysokości**
- **Efekty i transpozycja wysokości**
- **Prędkość odtwarzania i transpozycja wysokości**
- **Głośność, efekty i transpozycja wysokości**
- **Głośność, prędkość odtwarzania i transpozycja wysokości**
- **Efekty, prędkość odtwarzania i transpozycja wysokości**
- **Głośność, efekty, prędkość odtwarzania i transpozycja wysokości**

Do profilu zapisywane są tylko wybrane elementy; wszystko, co pominiesz, zachowuje to, co było już zapisane. Na przykład wybranie **Tylko prędkość odtwarzania** dla podcastu, który ma już zapisany profil głośności/efektów, zaktualizuje tylko prędkość i pozostawi resztę bez zmian.

**Wyczyść profil audio** usuwa zapisany profil podcastu z obu menu kontekstowych. Pozycja jest aktywna tylko wtedy, gdy podcast ma obecnie zapisany profil.

### Przechowywanie danych podcastów

Subskrypcje są zapisywane w pliku `freeAudio_podcasts.json` w folderze konfiguracji użytkownika NVDA. Pozycje odcinków są przechowywane osobno w `podcast_positions.json` w tej samej lokalizacji. Oba pliki są zwykłym JSON i można je archiwizować lub przenosić na inny komputer.

## Audiobooki (GETEM, LibriVox i Project Gutenberg)

freeAudio zawiera odtwarzacz audiobooków, który wyszukuje, odtwarza i pobiera książki z trzech źródeł:

- **[GETEM](https://getem.boun.edu.tr/)** — biblioteka cyfrowa prowadzona przez Centrum Osób z Dysfunkcją Wzroku Uniwersytetu Boğaziçi. Strumieniowanie lub pobieranie dźwięku książki wymaga bezpłatnego członkostwa (przeglądanie go nie wymaga) — zobacz [Logowanie](#logowanie) poniżej.
- **[LibriVox](https://librivox.org/)** — wolontariacki projekt audiobooków z domeny publicznej. Nie jest potrzebne żadne konto ani logowanie; cały jego katalog, łącznie z samymi plikami audio, należy do domeny publicznej i jest otwarcie dostępny.
- **Project Gutenberg Open Audiobook Collection** — audiobooki z domeny publicznej czytane przez lektorów lub syntezator, hostowane na [archive.org](https://archive.org/), towarzysz biblioteki tekstów Projektu Gutenberg. Podobnie jak w LibriVox, nie jest potrzebne konto ani logowanie.

Wyniki ze wszystkich trzech źródeł pojawiają się razem na jednej połączonej liście **Wyniki wyszukiwania** i jednej połączonej liście **Biblioteka** — nie ma osobnej karty ani listy rozwijanej do przełączania między nimi. Źródło każdej książki (GETEM, LibriVox lub Project Gutenberg) jest pokazywane jako etykieta obok jej tytułu oraz w jej szczegółach, więc zawsze wiesz, na co patrzysz. Możesz wyszukiwać, podglądać, dodawać, odtwarzać i pobierać książki z dowolnego źródła dokładnie w ten sam sposób; odtwarzać dzieła wieloczęściowe z automatycznym wznawianiem między częściami; oraz pobierać książki do słuchania offline — wszystko w pełni dostępne.

Każde źródło można osobno wyłączyć w menu **NVDA → Preferencje → Ustawienia → freeAudio** za pomocą listy **Źródła audiobooków**, jeśli chcesz przeszukiwać tylko niektóre z nich. Wszystkie trzy są domyślnie włączone.

> **Uwaga:** Słuchanie książki z GETEM wymaga bezpłatnego członkostwa w GETEM. Przeglądanie katalogu GETEM nie wymaga konta, ale uzyskanie i odtwarzanie dźwięku książki z GETEM — tak — zobacz [Logowanie](#logowanie) poniżej. Książki z LibriVox i Project Gutenberg nigdy nie wymagają konta.

### Dostęp do karty Audiobooki

Otwórz przeglądarkę stacji skrótem `Ctrl+Win+R` i przełącz się na kartę **Audiobooki** za pomocą `Ctrl+Tab` lub `Alt+7`. Karta ma trzy główne obszary:

1. **Szukaj** — pole tekstowe do przeszukiwania wszystkich włączonych katalogów naraz, z listą wyników, która pojawia się po uruchomieniu wyszukiwania.
2. **Biblioteka** — lista książek dodanych z dowolnego źródła, na której je odtwarzasz, pobierasz i nimi zarządzasz.
3. **Szczegóły** — pole tylko do odczytu pokazujące źródło, tytuł, autora, lektora, wydawcę, format, liczbę części, opis i adres URL katalogu zaznaczonej książki, na obu listach.

### Logowanie

GETEM wymaga bycia zarejestrowanym członkiem, aby strumieniować lub pobierać faktyczny dźwięk książki, chociaż sam katalog można swobodnie przeszukiwać. Wpisz swoją nazwę użytkownika i hasło GETEM jeden raz w menu **NVDA → Preferencje → Ustawienia → freeAudio**; są one przechowywane na dysku w postaci zaszyfrowanej (przez Windows Data Protection API, powiązane z Twoim kontem użytkownika systemu Windows) i automatycznie używane później. Jeśli spróbujesz odtworzyć lub pobrać książkę z GETEM przed wpisaniem danych logowania, freeAudio poinformuje, że najpierw trzeba je dodać w Ustawieniach.

LibriVox i Project Gutenberg w ogóle nie wymagają logowania — ich wyniki i dźwięk można wyszukiwać, podglądać, odtwarzać i pobierać od razu, bez wpisywania żadnych danych logowania.

### Wyszukiwanie audiobooków

Wpisz wyszukiwane hasło w polu wyszukiwania i naciśnij `Enter`. freeAudio przeszukuje źródła włączone w Ustawieniach i łączy wyniki w jedną listę:

- **GETEM** jest przeszukiwany jednocześnie po tytule, autorze, lektorze, temacie i wydawcy, ponieważ formularz wyszukiwania GETEM pozwala tylko zawężać według wszystkich tych pól razem, a nie przeszukiwać pojedynczo dowolne z nich. Pokazywane są tylko dzieła faktycznie dostępne jako audio (narracja ludzka lub komputerowa, audiodeskrypcja, słuchowisko radiowe, książki mówione DAISY itd.); braille, duży druk i inne formaty bez dźwięku są automatycznie odfiltrowywane.
- **LibriVox** jest przeszukiwany po tytule lub autorze/lektorze w jego katalogu z domeny publicznej.
- **Project Gutenberg** jest przeszukiwany po tytule lub autorze w Open Audiobook Collection na archive.org.

Wklejenie adresu URL strony katalogowej/szczegółów książki bezpośrednio w polu wyszukiwania (strony katalogu GETEM albo strony „details” na archive.org dla tytułu z LibriVox lub Project Gutenberg) rozpoznaje tę jedną książkę bezpośrednio, zamiast uruchamiać wyszukiwanie po słowach kluczowych.

NVDA ogłasza, ile audiobooków znaleziono łącznie.

Zaznaczenie wyniku pokazuje jego szczegóły — autora, lektora, wydawcę, format i liczbę części — w polu szczegółów poniżej.

**Podgląd:** zaznacz wynik i naciśnij `Space` albo otwórz jego menu kontekstowe (klawisz Menu kontekstowe / `Shift+F10` lub prawy przycisk myszy) i wybierz **Podgląd**, aby zacząć odtwarzanie od jego pierwszej części bez dodawania do biblioteki. Podczas podglądu książki to samo menu kontekstowe pokazuje w jego miejsce **Zatrzymaj podgląd** — wybierz tę pozycję albo naciśnij ponownie `Space`, aby zatrzymać. Podgląd książki nie zapisuje pozycji odsłuchu, ponieważ jest ona śledzona tylko dla książek znajdujących się już w bibliotece.

**Dodawanie do biblioteki:** zaznacz wynik i naciśnij `Enter` albo użyj jego menu kontekstowego i wybierz **Dodaj do biblioteki**, aby go dodać. freeAudio informuje, jeśli książka już tam jest.

### Twoja biblioteka

Dodane książki pojawiają się na liście **Biblioteka**, z tytułem, autorem i formatem. Zaznaczenie jednej pokazuje jej szczegóły poniżej.

- Naciśnij `Enter` lub `Space`, aby odtworzyć zaznaczoną książkę. Jeśli nic nie jest załadowane, `Space` ją uruchamia; jeśli coś już gra, `Space` zamiast tego wstrzymuje odtwarzanie, zgodnie z resztą odtwarzacza.
- Użyj `F3` / `F4` na karcie Audiobooki, aby przejść do poprzedniej / następnej **książki** w bibliotece i zacząć ją odtwarzać. `Ctrl+←` / `Ctrl+→` robią to samo, gdy fokus jest na liście biblioteki.
- Użyj `Shift+F3` / `Shift+F4`, aby zamiast tego przechodzić między **częściami** aktualnie odtwarzanej książki — odwrotnie niż na karcie Podcasty, gdzie F3/F4 przechodzą między odcinkami, a Shift+F3/F4 między kanałami. Dzieje się tak, ponieważ książka jest jedną pozycją biblioteki nawet wtedy, gdy ma kilka części, więc dokładniejsza nawigacja po „częściach” znajduje się tu na klawiszach z Shiftem.

**Menu kontekstowe pozycji biblioteki:** kliknij prawym przyciskiem myszy książkę albo zaznacz ją i naciśnij klawisz Menu kontekstowe / `Shift+F10`, aby otworzyć menu z pozycjami:
- **Odtwórz media** — rozpocznij odtwarzanie, tak samo jak `Enter`.
- **Pobierz książkę** — pobierz wszystkie części książki; zobacz [Pobieranie audiobooków](#pobieranie-audiobooków) poniżej.
- **Kopiuj adres URL** — skopiuj adres URL strony katalogowej książki do schowka (stronę katalogu GETEM dla książki z GETEM albo stronę szczegółów archive.org dla książki z LibriVox lub Project Gutenberg).
- **Zapisz profil audio dla tej książki** / **Wyczyść profil audio** — zobacz [Profil audio audiobooka](#profil-audio-audiobooka) poniżej.
- **Usuń z biblioteki** — usuń książkę z biblioteki.

Możesz też zaznaczyć kilka książek naraz i usunąć je razem — zobacz [Zaznaczanie i usuwanie wielu elementów](#zaznaczanie-i-usuwanie-wielu-elementów) w sekcji Ulubione.

### Odtwarzanie i wznawianie

Dzieło wieloczęściowe jest w odtwarzaczu traktowane jako jedna pozycja, a nie osobny wiersz dla każdej części — tak samo jak odcinek podcastu jest jedną pozycją niezależnie od sposobu dostarczenia. freeAudio zapamiętuje, której części słuchałeś ostatnio, i wznawia od niej automatycznie przy następnym odtwarzaniu tej książki, nawet po restarcie NVDA.

Gdy jedna część się kończy, freeAudio automatycznie uruchamia następną część tej samej książki — nie musisz jej zaznaczać ręcznie. Dzieje się tak nawet wtedy, gdy okno Przeglądarki stacji jest w tym czasie zamknięte; „aktualnie odtwarzana” część pokazana na liście Biblioteka jest automatycznie synchronizowana przy następnym otwarciu okna.

Odtwarzanie jest strumieniowane przez niewielki lokalny przekaźnik, zamiast najpierw pobierać całą część, więc słuchanie zaczyna się, gdy tylko dotrą pierwsze bajty — tak samo natychmiastowy start, jak w podcastach. Wszystkie zwykłe kontrolki odtwarzacza (pauza, głośność, time-shift, prędkość odtwarzania, transpozycja, urządzenie wyjściowe itd.) działają na audiobooku dokładnie tak samo jak na stacji lub odcinku podcastu.

Podobnie jak w podcastach, wznowienie książki od zapisanej pozycji odtwarza krótki dźwięk wkładanej kasety, gdy freeAudio przewija do zapisanego miejsca — zobacz uwagę o **Dźwięku wznowienia** w [Szczegółach odtwarzania podcastów](#szczegóły-odtwarzania-podcastów).

### Profil audio audiobooka

Kliknij prawym przyciskiem myszy książkę na liście Biblioteka i wybierz **Zapisz profil audio dla tej książki**, aby zapisać bieżącą głośność, efekty, wzmocnienia EQ i/lub prędkość odtwarzania jako profil przypisany do tej książki. Za każdym razem, gdy książka (lub dowolna z jej części) jest odtwarzana, zapisane ustawienia są stosowane automatycznie, zastępując ustawienia globalne. Działa to dokładnie tak samo jak [Profil audio podcastu](#profil-audio-podcastu) powyżej, łącznie z tym samym zestawem opcji zapisu (głośność, efekty i/lub prędkość odtwarzania, w dowolnej kombinacji) i tym samym zachowaniem częściowej aktualizacji.

**Wyczyść profil audio** usuwa zapisany profil książki; pozycja jest aktywna tylko wtedy, gdy książka ma obecnie zapisany profil.

### Pobieranie audiobooków

Zaznacz książkę w bibliotece i wybierz **Pobierz książkę** z jej menu kontekstowego, aby zapisać każdą część w osobnym folderze (nazwanym od książki) wewnątrz folderu nagrań (domyślnie `Documents\freeAudio Recordings\`). Pliki są numerowane, aby części zawsze układały się w kolejności słuchania, niezależnie od tego, jak nazywa je sam GETEM. NVDA ogłasza, ile części zapisano po zakończeniu pobierania; jeśli któraś część się nie powiedzie, obok liczby zgłaszany jest ostatni błąd.

### Przechowywanie danych audiobooków

Każde źródło ma własny plik biblioteki, chociaż na karcie Audiobooki są wyświetlane razem. Twoja biblioteka GETEM (dodane książki i postęp słuchania) jest zapisywana w `freeAudio_getem_library.json`, biblioteka LibriVox jest zapisywana osobno w `freeAudio_librivox_library.json`, a biblioteka Project Gutenberg osobno w `freeAudio_gutenberg_library.json` — wszystkie trzy w folderze konfiguracji użytkownika NVDA. Zaszyfrowane dane logowania GETEM są przechowywane osobno w `freeAudio_getem_credentials.bin` w tej samej lokalizacji i mogą zostać odszyfrowane tylko przez to samo konto użytkownika systemu Windows, które je zapisało. LibriVox i Project Gutenberg nie mają pliku z danymi logowania, ponieważ żaden z nich nie wymaga konta.

## Lokalny Jukebox

Karta **Jukebox** we freeAudio daje dwa sposoby odtwarzania plików audio, które już znajdują się na Twoim komputerze: wyszukiwanie plików według nazwy na każdym podłączonym dysku albo budowanie trwałej osobistej biblioteki plików i folderów. Wszystko, co odtwarzasz stąd, jest traktowane tak samo jak podcast lub audiobook — automatyczne wznawianie, stopniowane przewijanie wstecz/do przodu, prędkość odtwarzania, transpozycja wysokości dźwięku i profile audio dla poszczególnych elementów działają dokładnie tak samo.

### Dostęp do karty Jukebox

Otwórz przeglądarkę stacji skrótem `Ctrl+Win+R` i przełącz się na kartę **Jukebox** za pomocą `Ctrl+Tab` lub `Alt+8`, albo otwórz ją bezpośrednio z dowolnego miejsca globalnym skrótem `Ctrl+Win+U`. Karta składa się z trzech głównych obszarów:

1. **Szukaj na urządzeniach** — pole tekstowe, które przeszukuje każdy lokalnie podłączony, gotowy dysk w poszukiwaniu plików audio, których nazwa zawiera wpisany tekst. Naciśnij `Enter`, aby rozpocząć wyszukiwanie.
2. **Wyniki wyszukiwania** — lista pojawiająca się po uruchomieniu wyszukiwania, pokazująca pasujące pliki. Do tego czasu jest ukryta, aby karta pozostawała przejrzysta, gdy nie ma czego szukać.
3. **Jukebox i Utwory** — trwała lista dodanych elementów, a za nią lista utworów w zaznaczonej pozycji (dla pliku — tylko ten jeden plik; dla folderu — każdy plik audio znaleziony w jego wnętrzu).

Przyciski **Dodaj plik…**, **Dodaj folder…**, **Usuń**, **Eksportuj Jukebox…** i **Importuj Jukebox…** znajdują się pod listą Utwory.

### Wyszukiwanie plików na urządzeniach

Wpisz dowolną część nazwy pliku w polu **Szukaj na urządzeniach** i naciśnij `Enter`. freeAudio przeszukuje każdy lokalnie podłączony dysk — dyski stałe, dyski USB, karty pamięci, zmapowane dyski sieciowe — w poszukiwaniu plików audio (`.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a`, `.m4b`, `.aac`, `.wma`, `.opus` i kilku innych), których nazwa zawiera szukany tekst. Wyszukiwanie działa w tle, więc NVDA pozostaje responsywny.

- **Space** na wyniku wyszukiwania uruchamia podgląd — rozpoczyna odtwarzanie w normalnym odtwarzaczu. Naciśnij **Space** ponownie na tym samym pliku, aby zatrzymać podgląd.
- **Enter** na wyniku wyszukiwania dodaje go do jukeboksa.
- Menu kontekstowe (klawisz Menu kontekstowe / `Shift+F10` lub prawy przycisk myszy) oferuje te same dwie akcje: **Podgląd** / **Zatrzymaj podgląd** i **Dodaj do Jukeboksa**.
- Rozpoczęcie nowego wyszukiwania anuluje każde wyszukiwanie, które jeszcze trwa, więc wolne przeszukiwanie dużego dysku nigdy nie opóźnia świeżego.

### Budowanie jukeboksa

Lista Jukebox to Twoja trwała osobista biblioteka. Można dodać dwa rodzaje elementów:

- **Dodaj plik…** — otwiera okno wyboru plików, w którym możesz dodać jeden lub więcej pojedynczych plików audio. Wszystkie wybrane pliki są dodawane naraz.
- **Dodaj folder…** — otwiera okno wyboru folderów, w którym możesz wybrać kilka folderów naraz. Każdy plik audio znaleziony wewnątrz każdego wybranego folderu, także w jego podfolderach, jest traktowany jako jeden z **utworów** tego folderu. Każdy folder jest dodawany jako osobna pojedyncza pozycja na liście Jukebox; pliki w nim zawarte są wyświetlane na liście Utwory po zaznaczeniu folderu. NVDA ogłasza, ile folderów dodano po zamknięciu okna wyboru.
- **Usuń** — usuwa aktualnie zaznaczoną pozycję z jukeboksa. Usunięcie pozycji folderu nie usuwa żadnych plików z dysku ani urządzenia; jedynie zapomina folder. Możesz też zaznaczyć kilka pozycji naraz i usunąć je razem — zobacz [Zaznaczanie i usuwanie wielu elementów](#zaznaczanie-i-usuwanie-wielu-elementów) w sekcji Ulubione.

Lista Jukebox jest zapisywana automatycznie, więc przetrwa restarty NVDA. Zawartość folderów jest skanowana na żądanie i buforowana, więc dodanie folderu jest natychmiastowe nawet dla bardzo dużych kolekcji — pełne skanowanie odbywa się przy pierwszym zaznaczeniu tego folderu. Jeśli dodasz pliki do folderu poza freeAudio, użyj pozycji **Przeskanuj folder ponownie** w menu kontekstowym folderu, aby je uwzględnić.

### Dodawanie elementów z Eksploratora Windows

Dwa dodatkowe polecenia, dostępne tylko wtedy, gdy w liście plików Eksploratora Windows (liście Szczegóły/Ikony — nie na pasku adresu, w drzewie folderów, we wstążce ani w polu wyszukiwania) zaznaczony jest plik lub folder, pozwalają całkowicie pominąć opisane wyżej okna Dodaj plik…/Dodaj folder…:

- **Odtwórz zaznaczony plik we freeAudio** — odtwarza wyróżniony plik audio bezpośrednio, bez konieczności wcześniejszego dodawania go do listy Jukebox. Działa tylko na plikach; użycie go na folderze informuje, że folder należy zamiast tego dodać do jukeboksa.
- **Dodaj zaznaczony element do jukeboksa freeAudio** — dodaje wyróżniony plik lub folder do listy Jukebox, dokładnie tak, jakbyś użył **Dodaj plik…** lub **Dodaj folder…** powyżej.

Żadne z tych poleceń nie ma domyślnego skrótu. Przypisz skrót w menu NVDA → Preferencje → Zdarzenia wejścia → freeAudio **podczas gdy fokus jest w oknie Eksploratora plików**.

### Odtwarzanie z jukeboksa

- **Enter** na pozycji Jukeboksa odtwarza ją bezpośrednio: dla pliku — sam plik; dla folderu — jego pierwszy utwór.
- **Space** na pozycji Jukeboksa wstrzymuje odtwarzanie, jeśli cokolwiek gra; w przeciwnym razie odtwarza zaznaczoną pozycję.
- **Enter** lub **Space** na liście Utwory odtwarza zaznaczony utwór. **Space** najpierw wstrzymuje, jeśli coś już gra.
- **F3 / F4** na karcie Jukebox przechodzą między utworami w obrębie aktualnie zaznaczonej pozycji i odtwarzają je natychmiast.
- **Shift+F3 / Shift+F4** przechodzą między pozycjami na liście Jukebox (plikami i folderami), podobnie jak te klawisze przechodzą między kanałami na karcie Podcasty.
- **Ctrl+← / Ctrl+→**, gdy fokus jest na liście pozycji lub utworów, robią to samo co F3/F4 na liście utworów — poprzedni / następny utwór.

### Szczegóły odtwarzania z jukeboksa

Każdy utwór odtwarzany z Jukeboksa otrzymuje pełne traktowanie lokalnych mediów:

- **Wznawianie:** freeAudio zapamiętuje Twoją pozycję w każdym utworze, zapisuje ją przy pauzie i okresowo podczas odtwarzania, a następnie wznawia od tego miejsca przy ponownym odtwarzaniu — nawet po restarcie NVDA.
- **Przewijanie stopniowane:** `Ctrl+Win+J` / `Ctrl+Win+K` przewijają w obrębie utworu z tym samym skalowaniem naciśnięć/przytrzymania co w podcastach i audiobookach — przytrzymanie: 5 sekund na powtórzenie, jedno naciśnięcie: 12 sekund, dwa naciśnięcia: 1 minuta, trzy lub więcej: 5 minut.
- **Prędkość odtwarzania:** `Ctrl+Win+Shift+J` / `Ctrl+Win+Shift+K` zmieniają prędkość co 0,1x od 0,5x do 2,0x, z zachowaniem wysokości dźwięku.
- **Transpozycja:** `Shift+Win+J` / `Shift+Win+K` zmieniają wysokość dźwięku bez zmiany prędkości — zobacz [Transpozycja (zmiana wysokości dźwięku)](#transpozycja-zmiana-wysokości-dźwięku).
- **Profil audio:** głośność, efekty, EQ i prędkość utworu można zapisać globalnie, odtwarzając utwór przy odpowiednio ustawionych parametrach — Jukebox nie udostępnia obecnie menu profilu dla pojedynczego utworu, więc obowiązują bieżące ustawienia globalne.

> **Uwaga:** bufor time-shift (używany do cofania radia na żywo) celowo **nie** jest uruchamiany dla utworów z Jukeboksa — są to lokalne pliki, w których i tak można przewijać, więc przechwytywanie w tle nie miałoby sensu i tylko zajmowałoby miejsce na dysku. Cofanie i przewijanie do przodu nadal działają, ponieważ operują bezpośrednio na odtwarzanym pliku.

### Zmiana nazw pozycji Jukeboksa

Wybierz **Zmień nazwę…** z menu kontekstowego pozycji Jukeboksa (klawisz Menu kontekstowe / `Shift+F10`), aby nadać jej własną nazwę wyświetlaną. Własna nazwa zastępuje nazwę pliku lub folderu na liście Jukebox i jest zapisywana w wierszu `#EXTINF` podczas eksportu pozycji do M3U (zobacz [Eksportowanie i importowanie biblioteki Jukeboksa](#eksportowanie-i-importowanie-biblioteki-jukeboksa) poniżej). Pozostaw pole puste, aby usunąć własną nazwę i wrócić do oryginalnej nazwy pliku lub folderu.

### Porządkowanie Jukeboksa w grupy

Pozycje Jukeboksa mogą należeć do grupy, pokazywanej na liście jako przyrostek „— Grupa” po nazwie pozycji, dokładnie tak jak w [Porządkowaniu ulubionych w grupy](#porządkowanie-ulubionych-w-grupy):

- Zaznacz jedną lub więcej pozycji klawiszem `.` (zobacz [Zaznaczanie i usuwanie wielu elementów](#zaznaczanie-i-usuwanie-wielu-elementów) powyżej), a następnie wybierz **Przypisz do grupy…** z menu kontekstowego i wpisz nazwę grupy. Pozostaw pole puste, aby zamiast tego usunąć zaznaczone pozycje z ich grupy. Jeśli nic nie jest zaznaczone, polecenie dotyczy aktualnie wybranej pozycji.
- Pole Filtr nad listą Jukebox również dopasowuje nazwy grup, tak samo jak w Ulubionych.

### Zmiana kolejności w Jukeboksie

Po zaznaczeniu pozycji na liście Jukebox naciśnij `przecinek`, aby wejść w tryb przenoszenia — usłyszysz sygnał. Przejdź strzałkami do pozycji docelowej, a następnie naciśnij `przecinek` ponownie. Pozycja zostanie umieszczona w wybranym miejscu, a nowa kolejność zapisana natychmiast. Ponowne naciśnięcie przecinka w tej samej pozycji anuluje przenoszenie.

### Eksportowanie i importowanie biblioteki Jukeboksa

Karta Jukebox zawiera dwa przyciski do tworzenia kopii zapasowej i przywracania biblioteki, pod listą Utwory:

**Eksportuj Jukebox…** — zapisuje całą listę Jukebox do pliku. Okno dialogowe zapisu umożliwia wybór jednego z dwóch formatów:
- **JSON** (`.json`) — pełna kopia zapasowa zachowująca ścieżkę każdej pozycji, własną nazwę, grupę i zapisany profil audio. Zalecany do późniejszego przywrócenia biblioteki lub przeniesienia jej na inny komputer.
- **Lista odtwarzania M3U** (`.m3u`) — lżejszy format zgodny z większością odtwarzaczy multimedialnych, zawierający ścieżkę każdej pozycji wraz z jej własną nazwą (jeśli istnieje) w poprzedzającym wierszu `#EXTINF`. Grupy i profile audio nie są zawarte w M3U, więc przywracanie z M3U powoduje utratę tych szczegółów.

**Importuj Jukebox…** — ładuje pozycje z wcześniej wyeksportowanego pliku JSON lub M3U. Po wybraniu pliku pojawi się pytanie o sposób dodania pozycji:
- **Tak (Scal)** — dodaje importowane pozycje do istniejącej biblioteki bez usuwania bieżących pozycji. Pozycje, których ścieżka odpowiada już istniejącej w bibliotece, nie są dodawane dwukrotnie.
- **Nie (Zastąp)** — całkowicie usuwa bieżącą listę Jukebox i zastępuje ją zawartością importowanego pliku.
- **Anuluj** — powraca do przeglądarki bez wprowadzania żadnych zmian.

### Bezpośrednie skróty klawiszowe do pozycji Jukeboksa

Każda pozycja na liście Jukebox jest zarejestrowana jako osobny skrypt w oknie Zdarzeń wejścia NVDA, w kategorii **freeAudio Jukebox**, dokładnie tak jak w [Bezpośrednich skrótach klawiszowych do ulubionych stacji](#bezpośrednie-skróty-klawiszowe-do-ulubionych-stacji). Możesz przypisać dowolny skrót klawiszowy do dowolnej pozycji i nacisnąć go z dowolnego miejsca — bez konieczności otwierania okna przeglądarki.

Aby przypisać skrót:

1. Otwórz menu NVDA → Preferencje → Zdarzenia wejścia.
2. Rozwiń kategorię **freeAudio Jukebox**.
3. Znajdź pozycję po nazwie, zaznacz ją i naciśnij **Dodaj**.
4. Naciśnij żądaną kombinację klawiszy i potwierdź.

Skrót odtwarza pozycję natychmiast — dla pliku sam plik, dla folderu jego pierwszy utwór. Jeśli pozycja zostanie później usunięta z Jukeboksa, jej wpis zniknie z kategorii, a przypisany skrót zostanie automatycznie wyczyszczony przez NVDA. Po dodaniu nowej pozycji pojawia się ona w kategorii od razu — nie trzeba ponownie otwierać okna Zdarzeń wejścia.

## Transpozycja (zmiana wysokości dźwięku)

Transpozycja podwyższa lub obniża **wysokość** odtwarzanego dźwięku bez zmiany jego **prędkości** — jest przeciwieństwem „efektu wiewiórki”, który dostałbyś, po prostu przyspieszając utwór. Przydaje się do dopasowania do naturalnego zakresu danego lektora, transponowania muzyki do wygodniejszej tonacji albo po prostu do takiego dostosowania nagrania, aby lepiej brzmiało dla Twoich uszu.

Transpozycja jest dostępna dla **podcastów**, **audiobooków** i **utworów z jukeboksa** — tych samych „lokalnych, przewijalnych mediów z obsługą tempa”, do których stosują się skróty prędkości odtwarzania. Nie jest dostępna dla stacji radiowych na żywo, które nie mają ustalonej wysokości dźwięku do zmiany.

- **`Shift+Win+K`** — podwyższa wysokość o jeden krok.
- **`Shift+Win+J`** — obniża wysokość o jeden krok.

Każdy krok to **jedna ósma całego tonu**, czyli **0,25 półtonu** (cały ton to 2 półtony, więc 8 kroków to cały ton, a 48 kroków to oktawa). Zakres wynosi **od −12,00 do +12,00 półtonów**, czyli jedną pełną oktawę w górę lub w dół. NVDA ogłasza nową wartość po każdym kroku, na przykład „**+1,25 półtonu**”; powrót do 0,0 ogłasza „**Normalna wysokość**”.

Transpozycja jest zapamiętywana między utworami, tak samo jak prędkość odtwarzania: ustawienie jej raz podczas odtwarzania utworu sprawia, że następny utwór obsługujący zmianę tempa zaczyna z tym samym przesunięciem, chyba że jego własny zapisany profil audio to zmienia. Odtworzenie utworu bez zapisanej wartości transpozycji resetuje przesunięcie do 0,0 (Normalna wysokość), tak jak ta sama zasada obowiązuje już dla prędkości.

## Polubione utwory

Gdy włączona jest opcja **Zapisuj polubione utwory do pliku tekstowego**, informacje o utworze skopiowane do schowka trzykrotnym naciśnięciem `Ctrl+Win+I` są także dopisywane w kolejnych wierszach do `Documents\freeAudio Recordings\likedSongs.txt`.

Na stacjach nadających metadane ICY tytuł utworu i wykonawca są zapisywane bezpośrednio. Na stacjach bez metadanych ICY do tego samego pliku zapisywany jest wynik rozpoznawania przez Shazam — oba źródła używają jednej listy. Plik jest tworzony automatycznie, jeśli nie istnieje; każdy wpis jest dopisywany na końcu pliku, a poprzednie wpisy nigdy nie są usuwane.

## Karta Polubione utwory

Karta **Polubione utwory** w przeglądarce stacji wyświetla wszystkie ścieżki zapisane w `likedSongs.txt`. Lista jest automatycznie przeładowywana z pliku za każdym razem, gdy karta jest otwierana. Kliknij prawym przyciskiem myszy utwór albo zaznacz go i naciśnij klawisz Menu kontekstowe / `Shift+F10`, aby otworzyć menu kontekstowe z tymi samymi akcjami, które opisano poniżej.

Pole **Filtr** nad listą pozwala zawężać wyświetlane utwory w czasie rzeczywistym. Wpisz dowolną część tytułu piosenki lub nazwy wykonawcy, a lista zaktualizuje się natychmiast po każdym naciśnięciu klawisza. NVDA ogłasza liczbę pasujących wyników po każdej zmianie. Naciśnij strzałkę `w dół` w polu filtru, aby przenieść fokus bezpośrednio do listy.

Zaznaczenie utworu na liście włącza następujące akcje:

- **Odtwórz na Spotify:** próbuje bezpośrednio otworzyć aplikację komputerową Spotify. Jeśli aplikacja nie jest zainstalowana, otwiera witrynę Spotify i automatycznie odtwarza pierwszy wynik.
- **Odtwórz na YouTube (`Alt+O`):** wyszukuje wybrany utwór na YouTube i otwiera wyniki w domyślnej przeglądarce.
- **Pokaż tekst:** pobiera i wyświetla tekst wybranego utworu. Teksty są pobierane z [lrclib.net](https://lrclib.net) (bezpłatnie, bez konta). Krótki komunikat „Pobieranie tekstu…” jest ogłaszany, gdy wyszukiwanie odbywa się w tle. Jeśli tekst zostanie znaleziony, otworzy się w oknie dialogowym tylko do odczytu, gdzie możesz go przeczytać za pomocą NVDA i skopiować do schowka. Jeśli tekst nie zostanie znaleziony, NVDA to ogłosi. Przycisk jest tymczasowo wyłączony podczas trwającego pobierania, aby zapobiec powielaniu żądań.
- **Usuń (`Alt+M`):** usuwa wybrany utwór z `likedSongs.txt` i aktualizuje listę. Klawisz `Delete` również aktywuje ten przycisk, gdy lista ma fokus. Możesz też zaznaczyć kilka utworów naraz i usunąć je razem — zobacz [Zaznaczanie i usuwanie wielu elementów](#zaznaczanie-i-usuwanie-wielu-elementów) w sekcji Ulubione.
- **Odśwież (`Alt+E`):** przeładowuje listę z pliku.

Przyciski Spotify, YouTube, Pokaż tekst i Usuń są aktywne tylko wtedy, gdy na liście wybrany jest prawdziwy utwór.

### Serwis tekstów piosenek

freeAudio używa [lrclib.net](https://lrclib.net) do pobierania tekstów piosenek — bezpłatnej, otwartej bazy danych niewymagającej klucza API ani konta. Proces wyszukiwania analizuje ciąg ścieżki zapisany w `likedSongs.txt` i próbuje coraz luźniejszych zapytań, aż do znalezienia tekstu:

1. Dokładne dopasowanie przy użyciu pełnej nazwy wykonawcy i oczyszczonego tytułu (szumowe przyrostki takie jak „Remastered”, „Live” lub tagi roku są usuwane przed wyszukiwaniem).
2. Dokładne dopasowanie przy użyciu pełnej nazwy wykonawcy i oryginalnego tytułu (jeśli czyszczenie go zmieniło).
3. Dokładne dopasowanie przy użyciu tylko pierwszej nazwy wykonawcy i oczyszczonego tytułu (dla ciągów z wieloma wykonawcami, np. „Wykonawca A & Wykonawca B”).
4. Wyszukiwanie rozmyte przy użyciu pierwszej nazwy wykonawcy i oczyszczonego tytułu.
5. Wyszukiwanie rozmyte przy użyciu surowego ciągu ścieżki jako ostatnia deska ratunku.

Gdy dostępne są zwykłe teksty, są wyświetlane tak jak są. Gdy dostępne są tylko zsynchronizowane czasowo teksty LRC, znaczniki czasu są usuwane i wyświetlany jest zwykły tekst. Utwory instrumentalne są zgłaszane jako nieznalezione.

## Ustawienia

Poniższe opcje można skonfigurować w menu NVDA → Preferencje → Ustawienia → freeAudio:

| Opcja | Opis |
|---|---|
| Głos ogłaszania zmian utworów | Wybierz, czy automatycznie ogłaszane zmiany utworów są odczytywane przez syntezator NVDA, czy przez wybrany głos SAPI5. |
| Głos SAPI5 | Gdy **Głos ogłaszania zmian utworów** jest ustawiony na SAPI5, wybiera, który zainstalowany głos SAPI5 jest używany do ogłaszania zmian utworów. Lista jest wypełniana w tle na podstawie głosów zainstalowanych w systemie. |
| Urządzenie wyjściowe audio | Ustawia urządzenie wyjściowe audio dla odtwarzania radia. Lista zawiera wszystkie urządzenia zgodne z BASS w systemie oraz opcję „Domyślne systemowe”. Zmiany są stosowane natychmiast po zapisaniu; jeśli wybrane urządzenie zostanie odłączone, dodatek automatycznie wróci do domyślnego urządzenia systemowego i ogłosi zmianę. |
| Tryb odświeżania urządzeń audio | Kontroluje sposób odświeżania numerów urządzeń wyjściowych BASS. Tryb **Niezawodny** (domyślny) sprawdza urządzenia na żywo i dokładniej śledzi zmiany Bluetooth/USB, ale może lekko spowolnić zmianę urządzenia. Tryb **Szybki** używa bieżącej listy urządzeń BASS i działa szybciej, ale numery urządzeń mogą pozostać nieaktualne do restartu BASS albo NVDA. |
| Głośność | Ustawia początkową głośność dodatku (0–200). Zmiany wykonane podczas odtwarzania skrótami `Ctrl+Win+↑` / `Ctrl+Win+↓` są również odzwierciedlane tutaj. |
| Efekty audio | Ustawia, które efekty (Chorus, Kompresor, Przesterowanie, Echo, Flanger, Gargle, Pogłos i trzy wzmocnienia EQ) są aktywne przy starcie NVDA albo rozpoczęciu odtwarzania stacji. Można zaznaczyć wiele efektów naraz, tak jak na liście Efekty w Przeglądarce stacji. |
| Wzmocnienie EQ (bas / soprany / wokal) | Ustawia poziom wzmocnienia w dB dla każdego pasma EQ (−15 do +15). Wartości obowiązują, gdy odpowiedni efekt EQ jest aktywny, i są zapisywane globalnie. Nadpisania dla pojedynczej stacji można zapisać przyciskiem **Zapisz profil audio** na karcie Ulubione. |
| Sposób przełączania stacji | Kontroluje zachowanie podczas przełączania między **stacjami radiowymi na żywo**. **Natychmiastowe przełączenie** (domyślne) od razu zatrzymuje poprzednią stację przed uruchomieniem nowej. **Krótkie płynne przejście (1 sekunda)** i **Normalne płynne przejście (2 sekundy)** uruchamiają nową stację bez przerwy, a potem stopniowo wyciszają poprzednią w tle, gdy nowy strumień zostanie potwierdzony jako aktywny. **Dźwiękowy efekt strojenia stacji** natychmiast zatrzymuje poprzednią stację i odtwarza dźwięk strojenia radia przed uruchomieniem nowej. Przy ustawieniu Natychmiastowe przełączenie nie ma wpływu na wydajność. Nie dotyczy podcastów, audiobooków ani utworów z jukeboksa — ich wznawianie zawsze odtwarza własny krótki dźwięk kasety, niezależnie od tego ustawienia; zobacz [Szczegóły odtwarzania podcastów](#szczegóły-odtwarzania-podcastów). |
| Wznów ostatnią stację przy starcie NVDA | Gdy włączone, ostatnio odtwarzana stacja jest automatycznie uruchamiana przy każdym starcie NVDA. |
| Automatycznie ogłaszaj zmiany utworów (metadane ICY) | Gdy włączone, NVDA automatycznie odczytuje nową nazwę utworu za każdym razem, gdy zmieni się na stacji nadającej metadane ICY. Pierwszy utwór jest ogłaszany również natychmiast po przełączeniu na nową stację. Domyślnie wyłączone. |
| Wycisz powiadomienia | Gdy włączone, NVDA nie ogłasza zmian stacji, zmian stanu odtwarzania (odtwórz, pauza, stop) ani zdarzeń nagrywania (rozpoczęte, zatrzymane, zakończone). Komunikaty błędów, informacje o ulubionych, wyniki rozpoznawania muzyki i powiadomienia aktualizacji nie są wyciszane. Można też przełączać w locie przez nieprzypisane zdarzenie wejścia. Domyślnie wyłączone. |
| Komunikaty brajlowskie | Gdy włączone, freeAudio wysyła swoje powiadomienia także bezpośrednio na linijkę brajlowską. Przydaje się to przy tytułach utworów, zmianach stacji, stanie odtwarzania i zmianach głośności. Domyślnie wyłączone. |
| Włącz bufor time-shift (cofanie radia na żywo) | Włącza lub wyłącza sterowanie cofaniem (`Ctrl+Win+J`/`Ctrl+Win+K`) i powiększa przechwytywanie w tle z ~45 sekund do czasu określonego w ustawieniach. Niewielkie przechwytywanie w tle aktualnie odtwarzanej stacji działa zawsze, nawet gdy ta opcja jest wyłączona — zobacz uwagę w sekcji **Time-shift (cofanie radia na żywo)** poniżej. Można też natychmiast przełączyć za pomocą `Ctrl+Win+T`. Domyślnie wyłączone — pełne szczegóły znajdziesz w sekcji **Time-shift (cofanie radia na żywo)** poniżej. |
| Zapisuj polubione utwory do pliku tekstowego | Gdy włączone, informacje o utworze skopiowane do schowka trzykrotnym naciśnięciem `Ctrl+Win+I` są też dopisywane do `Documents\freeAudio Recordings\likedSongs.txt`. Jeśli metadane ICY nie są dostępne, do tego samego pliku zapisany zostaje wynik rozpoznawania przez Shazam. Domyślnie wyłączone. |
| Gdy Ctrl+Win+P zostanie naciśnięty bez aktywnego odtwarzania | Określa, co stanie się po naciśnięciu skrótu, gdy nic nie gra: uruchomienie ostatniej stacji albo otwarcie listy ulubionych. |
| Czas trwania bufora time-shift | Ustawia maksymalną długość bufora cofania. Dostępne opcje sięgają od 10 minut do 5 godzin. Dłuższe bufory zajmują więcej tymczasowego miejsca na dysku. |
| Gdy Ctrl+Win+P zostanie naciśnięty dwa razy | Wybiera akcję po dwukrotnym szybkim naciśnięciu skrótu: nic nie rób, otwórz listę ulubionych, otwórz kartę nagrywania albo otwórz kartę timera. Gdy wybrane jest „nic nie rób”, pierwsze naciśnięcie reaguje natychmiast, bez opóźnienia. |
| Gdy Ctrl+Win+P zostanie naciśnięty trzy razy | Wybiera akcję po trzykrotnym szybkim naciśnięciu skrótu: nic nie rób, otwórz listę ulubionych, otwórz wyszukiwanie stacji, otwórz kartę nagrywania albo otwórz kartę timera. |
| Sprawdzaj aktualizacje automatycznie | Gdy włączone, przy każdym starcie NVDA działa w tle sprawdzanie aktualizacji; jeśli zostanie znaleziona nowa wersja, pojawi się powiadomienie. Gdy wyłączone, automatyczne sprawdzanie jest zatrzymane, ale ręczne nadal działa. |
| Ścieżka do ffmpeg.exe | Ścieżka do `ffmpeg.exe` używanego do rozpoznawania muzyki. Jeśli pozostanie pusta, automatycznie użyty zostanie `ffmpeg.exe` z folderu dodatku. |
| Folder nagrań | Ustawia folder, w którym zapisywane są nagrania. Jeśli pozostanie pusty, używana jest domyślna lokalizacja `Documents\freeAudio Recordings\`. Przycisk Przeglądaj pozwala wybrać folder interaktywnie. Zmiany działają natychmiast po zapisaniu. |
| Źródła audiobooków | Lista wyboru określająca, które źródła audiobooków (**GETEM**, **LibriVox**, **Project Gutenberg**) są przeszukiwane i pokazywane na karcie Audiobooki. Wszystkie trzy są domyślnie włączone. Odznaczenie źródła ukrywa jego książki na połączonej liście wyników i w bibliotece, bez usuwania czegokolwiek, co już z niego dodałeś — zobacz [Audiobooki (GETEM, LibriVox i Project Gutenberg)](#audiobooki-getem-librivox-i-project-gutenberg). |
| Nazwa użytkownika GETEM / Hasło GETEM | Dane logowania członkowskiego do audiobooków [GETEM](https://getem.boun.edu.tr/), potrzebne do strumieniowania lub pobierania dźwięku książki — zobacz [Logowanie](#logowanie). Przechowywane na dysku w postaci zaszyfrowanej przez Windows Data Protection API, powiązanej z Twoim kontem użytkownika systemu Windows; nigdy nie są zapisywane jako zwykły tekst. Pozostawienie obu pól pustych i zapisanie usuwa wszystkie zapisane dane logowania. LibriVox i Project Gutenberg nie wymagają konta i nie mają odpowiedniego pola. |
| Format zapisu nagrań | Zachowuje oryginalny strumień, wyodrębnia sam dźwięk bez zmiany kodeka albo konwertuje zakończone nagrania do MP3. Domyślnie zachowywany jest oryginalny format strumienia. |
| Przepływność nagrań MP3 | Ustawia przepływność używaną, gdy wybrany jest format MP3. Domyślna wartość to 128 kb/s. |
| Wyłącz sprawdzanie połączenia internetowego przed odtwarzaniem | Zalecane dla użytkowników, u których występuje opóźnienie przed rozpoczęciem odtwarzania stacji. Przydatne również, gdy DNS jest blokowany. |

## Wyciszanie powiadomień

Gdy w ustawieniach włączone jest **Wycisz powiadomienia**, NVDA wycisza następujące automatyczne komunikaty:

- nazwa stacji po rozpoczęciu odtwarzania nowej stacji;
- zmiany stanu odtwarzania: odtwórz, pauza, stop;
- tryb Obligato: uruchomiony / zatrzymany;
- zdarzenia nagrywania: rozpoczęte, zatrzymane, zakończone (nagrania natychmiastowe, utworów i zaplanowane);
- komunikaty o zmianie utworu ICY, nawet gdy włączone jest też **Automatycznie ogłaszaj zmiany utworów**.

Celowo **nie** są wyciszane: komunikaty błędów, informacje o ulubionych (dodano / już na liście), wyniki rozpoznawania muzyki i powiadomienia aktualizacji.

Ustawienie można przełączyć w menu NVDA → Preferencje → Ustawienia → freeAudio albo natychmiast w dowolnym momencie przez nieprzypisane zdarzenie wejścia (przypisz je w menu NVDA → Preferencje → Zdarzenia wejścia → freeAudio). Po przełączeniu NVDA odczyta raz „Powiadomienia wyciszone” albo „Powiadomienia włączone”, aby potwierdzić zmianę.

## Automatyczne ogłaszanie zmian utworów

Gdy w ustawieniach włączona jest opcja **Automatycznie ogłaszaj zmiany utworów**, freeAudio sprawdza w tle strumień metadanych ICY aktywnej stacji mniej więcej co 5 sekund. Po zmianie utworu nowy tytuł jest automatycznie odczytywany przez NVDA — bez naciskania klawiszy.

Po przełączeniu na nową stację pierwsza informacja o utworze jest ogłaszana zaraz po nawiązaniu połączenia. Jeśli przełączysz na stację, która nie nadaje metadanych ICY, system pozostanie cichy, a informacje z poprzedniej stacji nie będą powtarzane.

Funkcja jest domyślnie wyłączona i można ją przełączyć w menu NVDA → Preferencje → Ustawienia → freeAudio.

## Odtwarzanie

freeAudio używa **BASS** jako jedynego backendu odtwarzania dla wszystkiego — radia internetowego, podcastów, audiobooków i utworów z jukeboksa. Nie jest wymagana osobna instalacja; BASS jest dołączony do dodatku. Obsługa VLC, PotPlayera i Windows Media Playera jako zapasowych backendów została usunięta; zawsze używany jest BASS.

BASS wysyła dźwięk bezpośrednio do stosu audio Windows i pojawia się w mikserze głośności Windows jako niezależne źródło audio o nazwie „pythonw.exe”, oddzielone od NVDA. Oznacza to, że dźwięk freeAudio płynie całkowicie osobnym kanałem niż mowa NVDA: radio nie zanika, nie miesza się i nie jest zależne od ustawień audio NVDA, gdy NVDA mówi. Użytkownik może regulować głośność radia niezależnie od NVDA w mikserze głośności Windows. Obsługuje HTTP, HTTPS i większość osadzonych formatów strumieni.

Odcinki podcastów, rozdziały audiobooków i utwory z jukeboksa są odtwarzane przez BASS, ponieważ może on otworzyć strumień jako przewijalny plik (nawet podczas pobierania), co umożliwia precyzyjne śledzenie pozycji, stopniowane cofanie/przewijanie do przodu, prędkość odtwarzania, transpozycję wysokości dźwięku i wznawianie. Kopia dźwięku, time-shift oraz przewijanie i wznawianie podcastów/audiobooków/jukeboksa zależą od BASS i są zawsze dostępne.

## Sprawdzanie aktualizacji

freeAudio automatycznie sprawdza nowe wersje przez GitHuba.

**Sprawdzanie automatyczne:** działa cicho w tle 15 sekund po starcie NVDA. Jeśli zostanie znaleziona nowa wersja, pojawi się powiadomienie; jeśli nie, nie pojawia się żaden komunikat.

**Sprawdzanie ręczne:** można uruchomić na żądanie z menu NVDA → Narzędzia → freeAudio → **Sprawdź aktualizacje…**. Przy ręcznym uruchomieniu wynik jest ogłaszany nawet wtedy, gdy wersja jest aktualna.

**Gdy znajdzie się aktualizacja:** otwiera się okno z numerem nowej wersji i wersją zainstalowaną.

- Jeśli w wydaniu GitHuba jest dostępny bezpośrednio pobieralny plik `.nvda-addon`, pojawia się przycisk **Pobierz i zainstaluj**. Po potwierdzeniu plik jest pobierany w tle, NVDA ogłasza rozpoczęcie pobierania, a następnie automatycznie otwiera własny ekran instalacji NVDA.
- Jeśli nie ma bezpośredniego linku pobierania, pojawia się przycisk **Otwórz stronę**, który otwiera stronę wydania GitHuba w domyślnej przeglądarce.

**Aby wyłączyć automatyczne sprawdzanie:** wyłącz opcję **Sprawdzaj aktualizacje automatycznie** w menu NVDA → Preferencje → Ustawienia → freeAudio.

## Podziękowania i autorzy

* **Pierwotna podstawa i koncepcje:** szczere podziękowania dla **Gary Mp** ([GaryMp/freeradio](https://github.com/GaryMp/freeradio)) za pierwotne koncepcje dodatku radiowego i podstawowe struktury zarządzania ulubionymi, które posłużyły jako fundament tego projektu.
* **Narzędzia AI i LLM:** wdzięczne uznanie dla nowoczesnych narzędzi opartych na dużych modelach językowych (LLM) (w tym Claude, ChatGPT i Gemini) za pomoc na etapach tworzenia, refaktoryzacji kodu i implementacji funkcji.
* **Usługa katalogowa:** katalog stacji dostarczany przez [Radio Browser API](https://www.radio-browser.info/).
* **Społeczność:** szczere podziękowania dla wszystkich członków społeczności NVDA i tłumaczy za ich nieustanne wsparcie, uwagi i wkład w lokalizację.

## Licencja

GPL v2
