# freeAudio — NVDA Add-on

freeAudio is een volledig uitgeruste add-on voor internetradio, podcasts, luisterboeken en een lokale jukebox voor de NVDA-schermlezer. Wat begon als een eenvoudige manier om naar internetradiostations te luisteren, is uitgegroeid tot een complete, volledig toegankelijke luisterhub — elk scherm, dialoogvenster en bedieningselement is vanaf de grond opgebouwd voor gebruik met toetsenbord en schermlezer, zonder dat op enig moment een muis nodig is.

## Wat freeAudio kan

- **Internetradio** — Blader door en zoek in meer dan 50.000 stations uit de [Radio Browser](https://www.radio-browser.info/)-directory, met resultaten aangevuld door TuneIn en iHeartRadio. Sla favorieten op, herschik ze en spring direct naar elk station met een globale sneltoets vanaf elke locatie in Windows — zie [Radio Browser-directory](#radio-browser-directory) en [Favorieten](#favorieten).
- **Podcasts** — Abonneer je op elke RSS/Atom-feed, of doorzoek Apple's podcastdirectory en bekijk afleveringen voordat je je abonneert. De afspeelpositie wordt automatisch opgeslagen en hervat waar je gebleven was — zie [Podcasts](#podcasts).
- **Luisterboeken** — Zoek, stream en download boeken uit drie bronnen: [GETEM](https://getem.boun.edu.tr/), de digitale bibliotheek van de Boğaziçi Universiteit voor slechtzienden; [LibriVox](https://librivox.org/), het door vrijwilligers voorgelezen publiek-domein luisterboekproject; en de Project Gutenberg Open Audiobook Collection. LibriVox en Project Gutenberg vereisen geen account. Werken met meerdere delen worden automatisch hervat waar je gebleven was — zie [Luisterboeken (GETEM, LibriVox en Project Gutenberg)](#luisterboeken-getem-librivox-en-project-gutenberg).
- **Lokale jukebox** — Zoek audiobestanden op elke aangesloten schijf op bestandsnaam, of bouw een persoonlijke bibliotheek van bestanden en mappen, en speel ze af met dezelfde hervat-, spoel-, snelheids- en toonhoogtetools die podcasts en luisterboeken gebruiken — zie [Lokale jukebox](#lokale-jukebox).
- **Bladwijzers** — Plaats een bladwijzer op de huidige positie van elk deel van een luisterboek, elke podcastaflevering of elk jukeboxnummer, en spring er later naar terug. Een bladwijzer kan een tekstnotitie of een opgenomen spraaknotitie bevatten die wordt afgespeeld wanneer het afspelen de bladwijzer bereikt, en met twee bladwijzers kan de sectie ertussen worden herhaald — zie [Bladwijzers](#bladwijzers).
- **Opnemen** — Neem direct op wat er speelt, neem één nummer op van begin tot eind, neem elk nummer op een station op in een eigen bestand tot je stopt, of plan eenmalige en terugkerende opnames — allemaal zonder het afspelen te onderbreken — zie [Opnemen](#opnemen).
- **Tijdverschuiving (live radio terugspoelen)** — Pauzeer en spoel een live station terug als een DVR, en haal de live-uitzending weer in wanneer je maar wilt — zie [Tijdverschuiving (live radio terugspoelen)](#tijdverschuiving-live-radio-terugspoelen).
- **Muziekherkenning en gelikete nummers** — Identificeer nummers zonder metadata met op Shazam gebaseerde herkenning, sla gelikete nummers op in een tekstbestand en zoek hun songteksten op — zie [Muziekherkenning](#muziekherkenning) en [Gelikete nummers](#gelikete-nummers).
- **Audioprofielen en effecten** — Sla aparte volume-, effect-, EQ- en afspeelsnelheidsinstellingen op per station, per podcast, per luisterboek of per jukeboxnummer, en pas realtime-effecten toe (Chorus, Reverb, EQ-versterkingen en meer) via de BASS-backend — zie [Audio-profiel van station](#audio-profiel-van-station).
- **Transponeren (toonhoogteverschuiving)** — Verschuif de toonhoogte van podcasts, luisterboeken en jukeboxnummers omhoog of omlaag zonder de snelheid te wijzigen, met behulp van de meegeleverde `bass_fx`-component — zie [Transponeren (toonhoogteverschuiving)](#transponeren-toonhoogteverschuiving).
- **Audio duplicatie** — Stuur dezelfde stream tegelijk naar twee audio-uitvoerapparaten, zoals luidsprekers en een hoofdtelefoon — zie [Audio duplicatie](#audio-duplicatie).
- **Obligato-modus (achtergrondmuziek)** — Herhaal een gekozen favoriet station zacht op de achtergrond, op een eigen uitvoerapparaat en volume, ongeacht wat er als hoofdmedia speelt (of niet speelt) — zie [Obligato-modus](#obligato-modus).
- **Timers** — Plan dat een favoriet station begint te spelen, of plan dat het afspelen stopt, op een specifiek tijdstip — zie [Timer](#timer).
- **Diepe toetsenbord- en braille-toegang** — Elke functie is volledig bereikbaar vanaf het toetsenbord, met globale sneltoetsen die overal in Windows werken (inclusief `Ctrl+Win+F3` / `Ctrl+Win+F4` om tussen stations, afleveringen, boeken en nummers te wisselen zonder het venster te openen), directe sneltoetsen voor individuele favoriete stations, jukeboxitems en luisterboeken, en optionele braille-uitvoer voor alle gesproken meldingen van freeAudio.

## Radio Browser-directory

freeAudio gebruikt de open database van [Radio Browser](https://www.radio-browser.info/) voor zijn stationcatalogus. Radio Browser is een door de gemeenschap beheerde, gratis directory die meer dan 50.000 internetradiostations van over de hele wereld host. Er is geen registratie of account vereist en de API is voor iedereen open. Elk station bevat informatie over adres, land, genre, taal en bitrate; stations worden gerangschikt op basis van stemmen van gebruikers. freeAudio maakt verbinding met deze API via mirror-servers in Duitsland, Nederland en Oostenrijk; als een server onbereikbaar is, schakelt hij automatisch over naar de volgende.

Om de verkenner responsief te houden en niet bij elke zoekopdracht of landwijziging de API te belasten, houdt freeAudio een lokale cache van de stationcatalogus op schijf bij. Deze cache wordt automatisch op de achtergrond ververst op een periodiek schema, zodat de lijst die je ziet meestal al up-to-date is zonder dat je iets hoeft te doen. Je kunt op elk moment ook zelf een directe hersynchronisatie afdwingen met de knop **Stationslijst bijwerken** — zie [Stationsverkenner](#stationsverkenner) hieronder.

## Een station toevoegen aan Radio Browser

Als een station dat je zoekt niet in de Radio Browser-directory staat, kun je het zelf aanmelden op [https://www.radio-browser.info/add](https://www.radio-browser.info/add). Er is geen account of registratie nodig.

Vul het formulier op die pagina in:

- **Stream URL** *(verplicht)* — de directe URL van de audiostream, eindigend op `.mp3`, `.aac`, `.ogg` of vergelijkbaar. Dit is niet het websiteadres van het station; het is het onbewerkte stream-adres dat je in een mediaspeler zou plakken. De meeste stations publiceren hun stream-URL op hun website of in hun "Luister live"-sectie.
- **Stationnaam** *(verplicht)* — de naam van het station zoals die in de directory moet verschijnen.
- **Homepage** — het websiteadres van het station.
- **Land en taal** — selecteer het land en de uitzendtaal uit de vervolgkeuzelijsten.
- **Tags** — genre- of onderwerptrefwoorden gescheiden door komma's, bijvoorbeeld `nieuws`, `jazz`, `klassiek`. Deze worden gebruikt voor zoeken en filteren.
- **Logo URL** — een directe link naar de logo-afbeelding van het station, indien beschikbaar.

Na het indienen wordt het station beoordeeld en toegevoegd aan de openbare directory. Zodra het geaccepteerd is, verschijnt het automatisch in de zoek- en landoverzichten van freeAudio, aangezien de directory wordt ververst vanuit de live API.

## Vereisten

- NVDA 2025.1 of later
- Windows 10 of later
- Internetverbinding

## Installatie

Download het `.nvda-addon`-bestand, druk op Enter op het bestand en herstart NVDA wanneer daarom wordt gevraagd.

## Sneltoetsen

Alle sneltoetsen kunnen opnieuw worden toegewezen via NVDA-menu → Opties → Invoerhandelingen → freeAudio. Deze sneltoetsen werken overal, ongeacht welk venster de focus heeft.

Sommige van deze sneltoetsen overlappen met sneltoetsen die Windows zelf gebruikt. Als je liever Windows' eigen sneltoets wilt behouden zonder die van freeAudio opnieuw toe te wijzen, druk je op `NVDA+F2` (Volgende toets doorgeven) direct vóór de toetsencombinatie — NVDA stuurt die ene toetsencombinatie dan rechtstreeks naar Windows in plaats van deze voor freeAudio te onderscheppen.

| Sneltoets | Functie | Beschrijving |
|---|---|---|
| `Ctrl+Win+R` | Stationsverkenner openen | Opent het stationsverkenner-venster als het gesloten is, of brengt het naar de voorgrond als het al geopend is. |
| `Ctrl+Win+O` | Tabblad Podcasts openen | Opent de stationsverkenner (indien gesloten) of brengt deze naar de voorgrond, en schakelt direct naar het tabblad **Podcasts**. |
| `Ctrl+Win+L` | Tabblad Luisterboeken openen | Opent de stationsverkenner (indien gesloten) of brengt deze naar de voorgrond, en schakelt direct naar het tabblad **Luisterboeken**. |
| `Ctrl+Win+U` | Tabblad Jukebox openen | Opent de stationsverkenner (indien gesloten) of brengt deze naar de voorgrond, en schakelt direct naar het tabblad **Jukebox**, met focus op het zoekveld voor apparaten. |
| `Ctrl+Win+P` | Pauze / hervatten | Pauzeert het huidige station indien het speelt; hervat indien gepauzeerd. Als er niets speelt, wordt het laatste station gestart of de favorietenlijst geopend, afhankelijk van je instelling. Twee keer snel achter elkaar drukken springt direct naar een tabblad naar keuze. Drie keer drukken kan een aparte actie activeren, afhankelijk van je instelling. |
| `Ctrl+Win+S` | Stoppen | Stopt het huidige station volledig en reset de speler. |
| `Ctrl+Win+→` | Volgende favoriet | Gaat naar het volgende station in de favorietenlijst. Begint weer bij het begin aan het einde van de lijst. |
| `Ctrl+Win+←` | Vorige favoriet | Gaat naar het vorige station in de favorietenlijst. Springt naar het einde aan het begin van de lijst. |
| `Ctrl+Win+F3` | Vorig item | De `F3`-toets van de stationsverkenner, beschikbaar bij gesloten venster. Wat de toets doet, hangt af van wat er wordt afgespeeld: **radio** — vorig station; **podcast** — vorige aflevering; **luisterboek** — vorig boek; **jukebox** — vorig nummer in de map. Aan het begin van een lijst wordt "Al bij het eerste …" aangekondigd. Als er niets wordt afgespeeld, wordt de toets ongewijzigd doorgegeven. Zie [Items overslaan met gesloten stationsverkenner](#items-overslaan-met-gesloten-stationsverkenner). |
| `Ctrl+Win+F4` | Volgend item | De `F4`-toets van de stationsverkenner, beschikbaar bij gesloten venster: volgend station, volgende podcastaflevering, volgend luisterboek of volgend jukeboxnummer, afhankelijk van wat er wordt afgespeeld. |
| `Ctrl+Win+Shift+F3` | Vorige feed / vorig deel / vorig item | De `Shift+F3`-toets van de stationsverkenner, beschikbaar bij gesloten venster: **radio** — vorig station (zoals `Ctrl+Win+F3`); **podcast** — vorige geabonneerde podcast; **luisterboek** — vorig deel van het boek; **jukebox** — vorig jukeboxitem (bestand of map). |
| `Ctrl+Win+Shift+F4` | Volgende feed / volgend deel / volgend item | De `Shift+F4`-toets van de stationsverkenner, beschikbaar bij gesloten venster: volgend station, volgende geabonneerde podcast, volgend deel van een luisterboek of volgend jukeboxitem, afhankelijk van wat er wordt afgespeeld. |
| `Ctrl+Win+↑` | Volume omhoog | Verhoogt het volume met 5; maximum 200. |
| `Ctrl+Win+↓` | Volume omlaag | Verlaagt het volume met 5; minimum 0. |
| `Ctrl+Win+V` | Toevoegen aan favorieten / media downloaden | Voegt het momenteel spelende station toe aan de favorietenlijst of downloadt de momenteel spelende podcastaflevering of het luisterboek. Geeft aan of het station al in de lijst staat of als de media al is gedownload. Niet van toepassing wanneer een jukeboxnummer speelt: freeAudio meldt dat de sneltoets alleen voor stations, podcasts of luisterboeken is. |
| `Ctrl+Win+Shift+K` | Afspeelsnelheid verhogen | Verhoogt de afspeelsnelheid van een podcastaflevering, luisterboek of jukeboxnummer met 0,1x (met behoud van toonhoogte). Bereik: 0,5x tot 2,0x. |
| `Ctrl+Win+Shift+J` | Afspeelsnelheid verlagen | Verlaagt de afspeelsnelheid met 0,1x. |
| `Shift+Win+K` | Transponeren omhoog | Verhoogt de toonhoogte van een podcastaflevering, luisterboek of jukeboxnummer in stappen van 1/8 hele toon (0,25 halve toon), zonder de snelheid te wijzigen. Bereik: −12,00 tot +12,00 halve tonen. Zie [Transponeren (toonhoogteverschuiving)](#transponeren-toonhoogteverschuiving). |
| `Shift+Win+J` | Transponeren omlaag | Verlaagt de toonhoogte in stappen van 1/8 hele toon, zonder de snelheid te wijzigen. |
| `Ctrl+Win+F12` | Bladwijzer toevoegen | Voegt een bladwijzer toe op de huidige afspeelpositie van een deel van een luisterboek, een podcastaflevering of een jukeboxnummer. Niet beschikbaar voor live radiostations. Zie [Bladwijzers](#bladwijzers). |
| `Ctrl+Win+I` | Stationinformatie | Kondigt de naam van het momenteel spelende station aan. Druk twee keer om details zoals land, genre en bitrate in een dialoogvenster te tonen. Druk drie keer om de huidige trackinformatie (ICY-metadata) naar het klembord te kopiëren indien beschikbaar; als er geen metadata aanwezig is, wordt in plaats daarvan Shazam-muziekherkenning gestart. Druk vier keer om muziekherkenning te forceren in geval van foutieve ICY-metadata. Terwijl een opname loopt, wordt de naam ervan ook aangekondigd; tijdens een opname van elk nummer is dit het nummer dat op dat moment wordt opgenomen. |
| `Ctrl+Win+M` | Audio duplicatie | Dupliceert de huidige stream tegelijkertijd naar een extra audio-uitvoerapparaat. Druk opnieuw om het dupliceren te stoppen. |
| `Ctrl+Win+Shift+M` | Obligato-modus (achtergrondmuziek) | Herhaalt een gekozen favoriet station zacht op de achtergrond, op een eigen uitvoerapparaat en volume, ongeacht wat er als hoofdmedia speelt. De eerste keer drukken opent een dialoogvenster om het station, uitvoerapparaat en relatieve volume te kiezen. Druk opnieuw om het te stoppen. |
| `Ctrl+Win+E` | Opnemen (direct / nummer / elk nummer) | Druk eenmaal om het opnemen van het huidige station te starten; druk opnieuw om te stoppen. Druk **tweemaal** om het **huidige nummer** op te nemen: het bestand wordt vernoemd naar het nummer en de opname stopt automatisch wanneer het nummer verandert. Druk **driemaal** om **elk nummer** op te nemen tot je stopt: elk nummer wordt in een eigen bestand opgeslagen. Druk tweemaal terwijl een nummer- of elk-nummer-opname loopt om deze te stoppen. Het afspelen gaat in alle opnamemodi ononderbroken door. Nummer- en elk-nummer-opname werken alleen op stations die tracktitels (ICY-metadata) in de stream meesturen, en elk-nummer-opname werkt niet op HLS (`.m3u8`)-stations. Zie [Opnemen](#opnemen). |
| `Ctrl+Win+W` | Map met opnames openen | Opent de map met opgenomen bestanden in de Verkenner. |
| `Ctrl+Win+J` | Tijdverschuiving terugspoelen / zoeken terug in podcast, luisterboek en jukebox | Voor live radio: spoelt 15 seconden terug. De eerste druk activeert de Tijdverschuivingsmodus; elke volgende druk gaat 15 seconden verder terug, tot de limiet van de buffer die is ingesteld in de freeAudio-instellingen. Vereist dat de tijdverschuivingsbuffer is ingeschakeld in de instellingen. Voor een podcast, luisterboek of jukeboxnummer zoekt deze toets in het bestand en schaalt afhankelijk van hoe je drukt: **ingedrukt houden** herhaalt 5 seconden per herhaling terug; **één bewuste druk** zoekt 12 seconden terug; **twee drukken** snel achter elkaar zoeken 1 minuut terug; **drie of meer drukken** zoeken 5 minuten terug. Er vindt slechts één zoekactie per drukreeks plaats. Werkt ongeacht de tijdverschuivingsinstelling. |
| `Ctrl+Win+K` | Tijdverschuiving vooruitspoelen / zoeken vooruit in podcast, luisterboek en jukebox | Voor live radio: spoelt 15 seconden vooruit tijdens tijdverschuiving. Zodra het live moment is bereikt, keert het afspelen automatisch terug naar live en doet deze toets niets totdat je weer terugspoelt. Voor een podcast, luisterboek of jukeboxnummer zoekt deze toets vooruit in het bestand met dezelfde druk/ingedrukt-houden-schaal als `Ctrl+Win+J` hierboven (ingedrukt houden = 5 seconden per herhaling; 1 druk = 12 seconden; 2 drukken = 1 minuut; 3+ drukken = 5 minuten). Werkt ongeacht de tijdverschuivingsinstelling. |
| `Ctrl+Win+Alt+J` | Nauwkeurig terugspoelen (1 seconde) | Spoelt precies 1 seconde terug, voor kleine correcties. Op een podcast, luisterboek of jukeboxnummer zoekt het 1 seconde terug in het bestand; op live radio gaat het 1 seconde terug in de tijdverschuivingsbuffer (de buffer moet ingeschakeld zijn, en de eerste druk activeert de tijdverschuivingsmodus zoals `Ctrl+Win+J`). Zie [Nauwkeurig zoeken (1 seconde)](#nauwkeurig-zoeken-1-seconde). |
| `Ctrl+Win+Alt+K` | Nauwkeurig vooruitspoelen (1 seconde) | Gaat precies 1 seconde vooruit. Op een podcast, luisterboek of jukeboxnummer zoekt het 1 seconde vooruit in het bestand; op live radio gaat het 1 seconde vooruit tijdens tijdverschuiving. Zie [Nauwkeurig zoeken (1 seconde)](#nauwkeurig-zoeken-1-seconde). |
| `Ctrl+Win+T` | Tijdverschuivingsbuffer in-/uitschakelen | Schakelt de tijdverschuivingsbuffer direct in of uit, overeenkomstig het selectievakje in de instellingen. Uitschakelen keert bij Tijdverschuiving direct terug naar live afspelen en stopt de achtergrondopname. Geen effect op podcast-, luisterboek- of jukeboxafspelingen. |
| *(niet toegewezen)* | Uitvoerapparaat selecteren | Opent een lijst op aanvraag van de beschikbare hoofd-uitvoerapparaten. De lijst wordt alleen getoond wanneer BASS meer dan één fysiek uitvoerapparaat detecteert. Wijs een toetsencombinatie toe via NVDA-menu → Opties → Invoerhandelingen → freeAudio. |
| *(niet toegewezen)* | Meldingen dempen in-/uitschakelen | Schakelt de instelling Meldingen dempen direct in of uit. Wijs een toetsencombinatie toe via NVDA-menu → Opties → Invoerhandelingen → freeAudio. |
| *(niet toegewezen)* | Favoriet station direct afspelen | Elk station in je favorietenlijst verschijnt als een apart item in NVDA-menu → Opties → Invoerhandelingen → **freeAudio Stations**. Wijs een sneltoets toe aan een station om het direct af te spelen vanaf elke locatie, zonder de stationsverkenner te openen. |
| *(niet toegewezen)* | Jukeboxitem direct afspelen | Elk bestand of elke map in je jukeboxlijst verschijnt als een apart item in NVDA-menu → Opties → Invoerhandelingen → **freeAudio Jukebox**. Zie [Directe sneltoetsen voor jukeboxitems](#directe-sneltoetsen-voor-jukeboxitems). |
| *(niet toegewezen)* | Luisterboek direct afspelen | Elk boek in je luisterboekenbibliotheek — van GETEM, LibriVox of Project Gutenberg — verschijnt als een apart item in NVDA-menu → Opties → Invoerhandelingen → **freeAudio Luisterboeken**. Wijs een sneltoets toe aan een boek om het direct te hervatten vanaf elke locatie, zonder de stationsverkenner te openen. Zie [Directe sneltoetsen voor luisterboeken](#directe-sneltoetsen-voor-luisterboeken). |

`Ctrl+Win+→` / `Ctrl+Win+←` navigeren alleen door de favorietenlijst; ze werken niet met de lijst met alle stations — gebruik `Ctrl+Win+F4` / `Ctrl+Win+F3` (zie hieronder) om te navigeren door de lijst waaruit het huidige station is gestart. Wanneer een lijst is gefocust in de stationsverkenner, dienen de linker- en rechterpijltjestoetsen hetzelfde doel — zie [In-dialoog sneltoetsen](#in-dialoog-sneltoetsen).

### Items overslaan met gesloten stationsverkenner

In de stationsverkenner doen `F3`, `F4`, `Shift+F3` en `Shift+F4` verschillende dingen, afhankelijk van het actieve tabblad. De globale versies — `Ctrl+Win+F3`, `Ctrl+Win+F4`, `Ctrl+Win+Shift+F3` en `Ctrl+Win+Shift+F4` — werken overal in Windows, of het venster nu open is of niet. Omdat er geen tabblad is om naar te kijken, beslist freeAudio op basis van **wat er op dit moment wordt afgespeeld**:

| Wordt afgespeeld | `Ctrl+Win+F3` / `Ctrl+Win+F4` | `Ctrl+Win+Shift+F3` / `Ctrl+Win+Shift+F4` |
|---|---|---|
| Radiostation | Vorig / volgend station in de lijst waaruit het voor het laatst is gestart (resultaten van Alle stations of Favorieten); aan de uiteinden gaat het rond. Staat het station niet in die lijst, dan wordt de favorietenlijst gebruikt. | Hetzelfde als zonder `Shift`. |
| Podcastaflevering | Vorige / volgende aflevering van dezelfde feed. | Vorige / volgende geabonneerde podcast. Omdat er geen lijst is om een feed in te markeren, wordt de eerste vermelde aflevering afgespeeld. |
| Luisterboek | Vorig / volgend boek in je bibliotheek, hervat bij het deel waar je het laatst naar luisterde. | Vorig / volgend deel van het huidige boek. |
| Jukeboxnummer | Vorig / volgend nummer van de map die wordt afgespeeld. | Vorig / volgend item in de jukeboxlijst; een map hervat waar hij de vorige keer was gebleven. |

Goed om te weten:

- Als er niets wordt afgespeeld, wordt de toetsencombinatie ongewijzigd aan Windows doorgegeven, net als bij `Ctrl+Win+→` / `Ctrl+Win+←`.
- Aan beide uiteinden van een lijst (behalve bij radio, dat rondgaat) kondigt NVDA "Al bij het eerste …" of "Al bij het laatste …" aan en verandert er niets. Een jukeboxnummer dat niet als onderdeel van een map is gestart, heeft geen buren en meldt hetzelfde.
- **Automatisch doorgaan wordt niet onderbroken.** Na het overslaan binnen een jukeboxmap of een luisterboek begint het volgende nummer of deel nog steeds vanzelf wanneer het huidige afloopt, met de stationsverkenner open of gesloten. Op volgende drukken bij het laatste nummer van een map zet de opgeslagen positie van de map niet terug.
- De afleveringenlijst van een podcast wordt alleen tijdens de huidige NVDA-sessie in het geheugen bewaard. Is die nog niet geladen — bijvoorbeeld direct na het starten van NVDA — dan vraagt NVDA je de stationsverkenner te openen en die podcast één keer te selecteren; daarna werken de toetsen ook bij gesloten venster.
- Als de stationsverkenner open is, werkt het overslaan van een luisterboek met het toetsenbord ook het "nu afspelen"-boek en -deel van het venster bij, zodat het eigen automatisch doorgaan vanaf de juiste plek verdergaat.

Net als elk freeAudio-commando kunnen deze worden opnieuw toegewezen via NVDA-menu → Opties → Invoerhandelingen → freeAudio.

## Stationsverkenner

freeAudio voegt ook een **freeAudio**-submenu toe aan het NVDA-menu Extra. Van daaruit kun je direct de Stationsverkenner en freeAudio-instellingen openen.

Het venster dat met `Ctrl+Win+R` wordt geopend, bevat acht tabbladen: Alle stations, Favorieten, Opname, Timer, Gelikete nummers, Podcasts, Luisterboeken en Jukebox. Je kunt tussen tabbladen navigeren met `Ctrl+Tab` of met `Alt+1` tot en met `Alt+8`. De tabbladen Podcasts, Luisterboeken en Jukebox kunnen worden uitgeschakeld met de instelling **Modules** (zie [Instellingen](#instellingen)); uitgeschakelde tabbladen worden niet getoond.

Wanneer het tabblad Alle stations opent, worden de 1.000 meest gestemde stations automatisch geladen vanuit Radio Browser. Het selecteren van een land in de vervolgkeuzelijst werkt de lijst bij om de stations van dat land te tonen. Typen in het zoekveld voert direct een volledige zoekopdracht uit over de gehele Radio Browser-database op naam, land en genre.

Bij het zoeken worden resultaten van Radio Browser aangevuld met stations van TuneIn en iHeartRadio (indien beschikbaar). Deze externe bronnen worden op de achtergrond doorzocht en hun resultaten worden automatisch in de lijst samengevoegd, zodat je toegang krijgt tot nog meer stations zonder extra actie.

De **Uitvoerapparaat** vervolgkeuzelijst onderaan de stationsverkenner — buiten de tabbladen — bevat alle door BASS herkende audio-uitvoerapparaten. Het selecteren van een apparaat leidt de audio-uitvoer direct daarnaartoe en slaat de keuze permanent op; hetzelfde apparaat wordt automatisch in de volgende sessie gebruikt. Als het geselecteerde apparaat niet is verbonden, valt de add-on automatisch terug op de systeemstandaard. Druk op `F11` om een eenvoudigere apparaatkiezer op aanvraag te openen vanuit de hele stationsverkenner. De kiezer wordt niet automatisch getoond en opent alleen wanneer BASS meer dan één fysiek uitvoerapparaat detecteert. Wanneer er maar één beschikbaar is, is geen selectie nodig en gebruikt freeAudio de standaarduitvoer van het systeem.

De **Volume** (0–200) en **Effecten** besturingen in hetzelfde gebied kunnen op elk moment worden aangepast terwijl het venster geopend is. Uit de Effecten-lijst kunnen Chorus, Compressor, Distortion, Echo, Flanger, Gargle, Reverb, EQ: Bass Boost, EQ: Treble Boost en EQ: Vocal Boost tegelijkertijd worden ingeschakeld; wijzigingen worden direct toegepast op de actieve stream. Elk effect kan ook direct worden in- of uitgeschakeld met `Ctrl+1` tot en met `Ctrl+0`, zonder het toetsenbord te verlaten — zie [Effectsneltoetsen](#effectsneltoetsen) hieronder.

Wanneer een of meer EQ-effecten zijn ingeschakeld, verschijnt een **gain-regeling** voor elke actieve band. De gain kan worden ingesteld tussen -15 dB en +15 dB; de standaardwaarden zijn Bass +9 dB, Treble +9 dB en Vocal +6 dB. De gain-regelingen worden alleen getoond voor de EQ-banden die momenteel zijn aangevinkt, en worden automatisch verborgen wanneer een EQ-effect wordt uitgeschakeld. Gain-waarden worden globaal opgeslagen en hersteld in de volgende sessie.

De **Afspelen/Pauze**-knop bevindt zich ook onderaan het venster. Als er geen station speelt, wordt het geselecteerde station gestart; als er al een station speelt, wordt het afspelen gepauzeerd.

De knop **Stationslijst bijwerken** synchroniseert de lokale stationcatalogus onmiddellijk opnieuw met de Radio Browser-API, in plaats van te wachten op de periodieke achtergrondverversing. Terwijl de verversing bezig is, is de knop uitgeschakeld en meldt NVDA dat er een verversing bezig is; als je nogmaals drukt voordat de huidige verversing klaar is, laat NVDA weten dat er al een bezig is. Zodra de verversing is voltooid, meldt NVDA dat de stationslijst is bijgewerkt en worden de op dat moment getoonde zoekresultaten of landweergave automatisch ververst om de nieuwe gegevens te tonen.

Wanneer een station in de lijst is geselecteerd, toont de **Stationsinformatie**-knop informatie zoals land, taal, genre, formaat, bitrate, website en stream-URL in een apart dialoogvenster. Elk veld verschijnt in zijn eigen alleen-lezen tekstvak; je kunt tussen velden bewegen met Tab en alle informatie in één keer naar het klembord kopiëren met de **Alles naar klembord kopiëren**-knop. Deze knop is beschikbaar in zowel de tabbladen Alle stations als Favorieten.

### Contextmenu van station

Klik met de rechtermuisknop op een station in de lijst Alle stations of Favorieten, of selecteer het en druk op de Toepassingentoets of `Shift+F10`, om een contextmenu met snelle acties te openen:

- **Stationdetails** — hetzelfde als de hierboven beschreven knop Stationdetails.
- **Toevoegen aan favorieten** *(tabblad Alle stations)* / **Station verwijderen** *(tabblad Favorieten)*.
- **Station hernoemen** *(tabblad Favorieten)* — hetzelfde als `F9`.
- **Audioprofiel voor dit station opslaan** / **Audioprofiel wissen** *(tabblad Favorieten)* — zie [Audio-profiel van station](#audio-profiel-van-station).
- **URL testen** — controleert of de stream van het geselecteerde station momenteel bereikbaar is zonder afspelen te starten, en kondigt het resultaat aan (bereikbaar, of de reden van mislukking, zoals een HTTP-fout of netwerktime-out).

Alleen de items die relevant zijn voor het huidige tabblad en de huidige selectie worden als beschikbaar getoond.

### In-dialoog sneltoetsen

De volgende toetsen werken alleen terwijl het Stationsverkenner-venster actief is.

#### F-toetsen

| Sneltoets | Functie | Beschrijving |
|---|---|---|
| `F1` | Helpgids | Opent het helpbestand van de add-on in de standaardbrowser. De gids voor de actieve NVDA-taal wordt eerst gezocht; indien niet gevonden, wordt de standaardgids geopend. |
| `F2` | Wat speelt er | Kondigt het momenteel spelende station en de tracknaam aan. Druk twee keer om details zoals land, genre en bitrate in een dialoogvenster te tonen. Druk drie keer om de huidige trackinformatie (ICY-metadata) naar het klembord te kopiëren indien beschikbaar; als er geen metadata aanwezig is, wordt in plaats daarvan Shazam-muziekherkenning gestart. Druk vier keer om muziekherkenning te forceren in geval van foutieve ICY-metadata. Terwijl een opname loopt, wordt de naam ervan ook aangekondigd. |
| `F3` | Vorig item | Op de tabbladen Alle stations of Favorieten: gaat naar het vorige station en begint direct met afspelen. Op het tabblad Podcasts: gaat naar de vorige aflevering in de afleveringenlijst en speelt deze af. Op het tabblad Luisterboeken: gaat naar het vorige boek en begint met afspelen. Op het tabblad Jukebox: gaat naar het vorige nummer in het geselecteerde jukeboxitem en speelt het af; in een map blijven de volgende nummers automatisch starten. Het globale equivalent is `Ctrl+Win+F3` — zie [Items overslaan met gesloten stationsverkenner](#items-overslaan-met-gesloten-stationsverkenner). |
| `F4` | Volgend item | Op de tabbladen Alle stations of Favorieten: gaat naar het volgende station en begint direct met afspelen. Op het tabblad Podcasts: gaat naar de volgende aflevering en speelt deze af. Op het tabblad Luisterboeken: gaat naar het volgende boek en begint met afspelen. Op het tabblad Jukebox: gaat naar het volgende nummer in het geselecteerde jukeboxitem en speelt het af; in een map blijven de volgende nummers automatisch starten. Het globale equivalent is `Ctrl+Win+F4`. |
| `Shift+F3` | Vorige feed / vorig deel / vorig item | Op het tabblad Podcasts: gaat één feed omhoog in de abonnementenlijst. Op het tabblad Luisterboeken: gaat naar het vorige deel van het momenteel spelende boek. Op het tabblad Jukebox: gaat één jukeboxitem (bestand of map) omhoog in de hoofdlijst. Het globale equivalent is `Ctrl+Win+Shift+F3`, dat het item ook afspeelt. |
| `Shift+F4` | Volgende feed / volgend deel / volgend item | Op het tabblad Podcasts: gaat één feed omlaag in de abonnementenlijst. Op het tabblad Luisterboeken: gaat naar het volgende deel van het momenteel spelende boek. Op het tabblad Jukebox: gaat één jukeboxitem omlaag in de hoofdlijst. Het globale equivalent is `Ctrl+Win+Shift+F4`, dat het item ook afspeelt. |
| `F5` | Volume omlaag | Verlaagt het volume met 5 (minimum 0). |
| `F6` | Volume omhoog | Verhoogt het volume met 5 (maximum 200). |
| `F7` | Pauze / hervatten | Pauzeert als een station speelt; hervat als gepauzeerd en media geladen is. |
| `F8` | Stoppen | Stopt het huidige station volledig en reset de speler. |
| `F9` | Naam wijzigen | Opent dialoogvenster voor naam wijzigen van het geselecteerde station in het tabblad Favorieten. |
| `F11` | Uitvoerapparaat selecteren | Opent de hoofd-uitvoerapparaatkiezer wanneer BASS meer dan één fysiek uitvoerapparaat detecteert. Het huidige apparaat is vooraf geselecteerd; Enter past de keuze toe en slaat deze op. |
| `F12` | Bladwijzer toevoegen | Voegt een bladwijzer toe op de huidige afspeelpositie van een deel van een luisterboek, een podcastaflevering of een jukeboxnummer — het in-venster-equivalent van `Ctrl+Win+F12`. Zie [Bladwijzers](#bladwijzers). |

#### Lijst- en navigatiesneltoetsen

| Sneltoets | Functie | Beschrijving |
|---|---|---|
| `→` | Volgend item / Zoeken vooruit | Op een stationlijst (Alle stations / Favorieten): gaat naar het volgende station en speelt het direct af, met terugkeer naar het begin aan het einde van de lijst. Op de itemlijsten van Podcasts, Luisterboeken of Jukebox (en de bladwijzerlijst eronder), terwijl er iets is geladen en speelt: zoekt vooruit — hetzelfde als het globale `Ctrl+Win+K`-commando (zie [Afspeeldetails van podcasts](#afspeeldetails-van-podcasts) voor hoe tikken en ingedrukt houden de stap veranderen). Op de afleveringenlijst van Podcasts specifiek, als er nog niets is geladen, gaat het terug naar het volgende item en speelt het af. |
| `←` | Vorig item / Zoeken achteruit | Op een stationlijst: gaat naar het vorige station en speelt het af, met sprong naar het einde aan het begin van de lijst. Op de itemlijsten van Podcasts, Luisterboeken of Jukebox (en de bladwijzerlijst eronder), terwijl er iets is geladen en speelt: zoekt achteruit — hetzelfde als het globale `Ctrl+Win+J`-commando. Op de afleveringenlijst van Podcasts, als er nog niets is geladen, gaat het terug naar het vorige item en speelt het af. |
| `Shift+→` | Transponeren omhoog | Op de itemlijsten van Podcasts, Luisterboeken of Jukebox en hun bladwijzerlijsten: verhoogt de toonhoogte van de huidige weergave met één stap (0,25 halve toon), hetzelfde als het globale `Shift+Win+K`-commando. |
| `Shift+←` | Transponeren omlaag | Op de itemlijsten van Podcasts, Luisterboeken of Jukebox en hun bladwijzerlijsten: verlaagt de toonhoogte van de huidige weergave met één stap (0,25 halve toon), hetzelfde als het globale `Shift+Win+J`-commando. |
| `Page Up` | Afspeelsnelheid omhoog | Op de itemlijsten van Podcasts, Luisterboeken of Jukebox en hun bladwijzerlijsten: verhoogt de afspeelsnelheid, hetzelfde als het globale `Ctrl+Win+Shift+K`-commando. |
| `Page Down` | Afspeelsnelheid omlaag | Op de itemlijsten van Podcasts, Luisterboeken of Jukebox en hun bladwijzerlijsten: verlaagt de afspeelsnelheid, hetzelfde als het globale `Ctrl+Win+Shift+J`-commando. |
| `Alt+→` | Nauwkeurig zoeken vooruit (1 seconde) | In elk tabblad van de stationsverkenner, terwijl er iets is geladen: zoekt precies 1 seconde vooruit, hetzelfde als het globale `Ctrl+Win+Alt+K`-commando. Zie [Nauwkeurig zoeken (1 seconde)](#nauwkeurig-zoeken-1-seconde). |
| `Alt+←` | Nauwkeurig zoeken achteruit (1 seconde) | In elk tabblad van de stationsverkenner, terwijl er iets is geladen: zoekt precies 1 seconde achteruit, hetzelfde als het globale `Ctrl+Win+Alt+J`-commando. |
| `Ctrl+→` | Volgende aflevering / boek / nummer | Op het tabblad Podcasts: gaat naar de volgende aflevering en speelt deze af. Op het tabblad Luisterboeken (bibliotheeklijst gefocust): gaat naar het volgende boek. Op het tabblad Jukebox (lijst met items of nummers gefocust): gaat naar het volgende nummer in het geselecteerde jukeboxitem en speelt het af. |
| `Ctrl+←` | Vorige aflevering / boek / nummer | Op het tabblad Podcasts: gaat naar de vorige aflevering en speelt deze af. Op het tabblad Luisterboeken: gaat naar het vorige boek. Op het tabblad Jukebox: gaat naar het vorige nummer in het geselecteerde jukeboxitem en speelt het af. |
| `Enter` | Afspelen / Toevoegen | Op een station- of afleveringenlijst: start direct het afspelen van het geselecteerde item. Op de zoekresultaten van het tabblad Jukebox: voegt het geselecteerde bestand toe aan de jukebox. Op de items- of nummerlijst van het tabblad Jukebox: speelt het gefocuste item direct af. |
| `Space` | Afspelen / Pauze / Voorbeeld | Pauzeert als er iets speelt; anders start het afspelen van het geselecteerde item. Op de zoekresultaten van het tabblad Jukebox: schakelt het voorbeeld (afspelen/stoppen) van het geselecteerde bestand. Op de items- of nummerlijst van het tabblad Jukebox: pauzeert als er iets speelt, anders speelt het gefocuste item af. |
| `Ctrl+Tab` | Volgend tabblad | Schakelt naar het volgende tabblad (Alle stations → Favorieten → Opname → Timer → Gelikete nummers → Podcasts → Luisterboeken → Jukebox). |
| `Ctrl+Shift+Tab` | Vorig tabblad | Schakelt naar het vorige tabblad. |
| `Escape` | Verbergen | Verbergt het venster; de add-on blijft op de achtergrond doorspelen. |

#### Volumesneltoetsen

| Sneltoets | Functie | Beschrijving |
|---|---|---|
| `Ctrl+↑` | Volume omhoog | Verhoogt het volume met 5. Werkt alleen terwijl de stationsverkenner geopend is. |
| `Ctrl+↓` | Volume omlaag | Verlaagt het volume met 5. Werkt alleen terwijl de stationsverkenner geopend is. |

#### Effectsneltoetsen

| Sneltoets | Functie | Beschrijving |
|---|---|---|
| `Ctrl+1` | Chorus in-/uitschakelen | Schakelt het Chorus-effect in of uit en past het direct toe op de actieve stream. |
| `Ctrl+2` | Compressor in-/uitschakelen | Schakelt het Compressor-effect in of uit en past het direct toe op de actieve stream. |
| `Ctrl+3` | Distortion in-/uitschakelen | Schakelt het Distortion-effect in of uit en past het direct toe op de actieve stream. |
| `Ctrl+4` | Echo in-/uitschakelen | Schakelt het Echo-effect in of uit en past het direct toe op de actieve stream. |
| `Ctrl+5` | Flanger in-/uitschakelen | Schakelt het Flanger-effect in of uit en past het direct toe op de actieve stream. |
| `Ctrl+6` | Gargle in-/uitschakelen | Schakelt het Gargle-effect in of uit en past het direct toe op de actieve stream. |
| `Ctrl+7` | Reverb in-/uitschakelen | Schakelt het Reverb-effect in of uit en past het direct toe op de actieve stream. |
| `Ctrl+8` | EQ: Bass Boost in-/uitschakelen | Schakelt de Bass Boost EQ-band in of uit en past deze direct toe op de actieve stream. |
| `Ctrl+9` | EQ: Treble Boost in-/uitschakelen | Schakelt de Treble Boost EQ-band in of uit en past deze direct toe op de actieve stream. |
| `Ctrl+0` | EQ: Vocal Boost in-/uitschakelen | Schakelt de Vocal Boost EQ-band in of uit en past deze direct toe op de actieve stream. |

Elke sneltoets komt overeen met het aan- of uitvinken van het bijbehorende item in de **Effecten**-lijst: NVDA meldt of het effect is in- of uitgeschakeld, de wijziging wordt automatisch opgeslagen en de gain-regeling voor die band (indien van toepassing) verschijnt of verdwijnt dienovereenkomstig.

#### Alt-toets sneltoetsen

| Sneltoets | Functie | Beschrijving |
|---|---|---|
| `Alt+R` | Ga naar zoekveld | Verplaatst de focus naar het zoektekstvak. Doorzoekt Radio Browser met de tekst in het zoekveld; naam, land en genre worden tegelijkertijd doorzocht. |
| `Alt+V` | Favoriet toevoegen / verwijderen | Voegt het geselecteerde station toe aan favorieten; verwijdert het als het al in de lijst staat. |
| `Alt+1` | Alle stations | Schakelt naar het tabblad Alle stations. |
| `Alt+2` | Favorieten | Schakelt naar het tabblad Favorieten. |
| `Alt+3` | Opname | Schakelt naar het tabblad Opname. |
| `Alt+4` | Timer | Schakelt naar het tabblad Timer. |
| `Alt+5` | Gelikete nummers | Schakelt naar het tabblad Gelikete nummers. |
| `Alt+6` | Podcasts | Schakelt naar het tabblad Podcasts. |
| `Alt+7` | Luisterboeken | Schakelt naar het tabblad Luisterboeken. |
| `Alt+8` | Jukebox | Schakelt naar het tabblad Jukebox, met focus op het zoekveld voor apparaten. |
| `Alt+K` | Sluiten | Sluit het venster; de add-on blijft op de achtergrond doorspelen. |
## Favorieten

De favorietenlijst is een persoonlijke verzameling stations die permanent wordt opgeslagen. Om een station toe te voegen, selecteer je het in de lijst en druk je op de knop Toevoegen aan favorieten of gebruik je de `Alt+V` sneltoets. Dezelfde sneltoets verwijdert een station dat al in de lijst staat wanneer het is geselecteerd.

Favorieten kunnen worden afgespeeld met `Ctrl+Win+→` en `Ctrl+Win+←`; deze sneltoetsen werken zelfs als de stationsverkenner niet geopend is.

Om een station uit de favorietenlijst te verwijderen, selecteer je het en druk je op de knop **Station verwijderen** of de `Delete`-toets. Na verwijdering verplaatst de focus en selectie zich automatisch naar het volgende station in de lijst. Als het verwijderde station het laatste was, verplaatst de focus zich naar het vorige station. Als de lijst leeg wordt, verplaatst de focus zich naar de Afspelen-knop.

### Meerdere items markeren en verwijderen

Favorieten, Gelikete nummers, de Luisterboekenbibliotheek en de Jukeboxlijst ondersteunen allemaal het markeren van meerdere items en het in één stap verwijderen ervan:

- Druk op **`.`** (punt) op een gemarkeerd item om het te markeren of de markering op te heffen. NVDA kondigt de wijziging aan, en de rij van een gemarkeerd item wordt aangeduid als "(gemarkeerd)", zodat de status duidelijk blijft terwijl je door de lijst blijft pijlen.
- Druk op **`Shift+Home`** om elk item vanaf het huidige tot het eerste item in de lijst te markeren of de markering op te heffen, of **`Shift+End`** om hetzelfde te doen tot het laatste item. Of het bereik wordt gemarkeerd of de markering wordt opgeheven, wordt bepaald door de huidige status van het item, zodat het hele bereik altijd dezelfde kant op beweegt in één actie. De focus verplaatst zich daarna naar het verre einde van het bereik, en NVDA kondigt aan hoeveel items zijn gewijzigd.
- Druk op **`Delete`** om alle gemarkeerde items in één keer te verwijderen. Als er niets is gemarkeerd, verwijdert `Delete` nog steeds alleen het momenteel geselecteerde item, zoals voorheen.
- Het contextmenu met rechtermuisknop (Toepassingentoets / `Shift+F10`) van elke lijst bevat een **Geselecteerde verwijderen**-commando, dat alleen is ingeschakeld wanneer ten minste één item is gemarkeerd, en dat hetzelfde doet.
- Voordat er iets wordt verwijderd, vat een enkel bevestigingsdialoogvenster samen hoeveel items op het punt staan te worden verwijderd.

Markeringen zijn per lijst en worden gewist zodra je de items verwijdert (of ze afzonderlijk de markering opheft); ze worden niet tussen sessies opgeslagen.

De bladwijzerlijsten op de tabbladen Podcasts, Luisterboeken en Jukebox gebruiken dezelfde `.`-markering, en gemarkeerde bladwijzers zijn waarop de commando's **Geselecteerde verwijderen** en **Herhalen tussen gemarkeerde bladwijzers** inwerken — zie [Bladwijzers](#bladwijzers).

### Favorieten exporteren en importeren

Het tabblad Favorieten bevat twee knoppen voor het maken van een back-up en het herstellen van je stationlijst:

**Favorieten exporteren…** — slaat je volledige favorietenlijst op naar een bestand. Een dialoogvenster laat je kiezen tussen twee formaten:

- **JSON** (`.json`) — een volledige back-up die stationnamen, stream-URL's en alle metadata behoudt. Aanbevolen voor het later herstellen van je lijst of het verplaatsen naar een andere computer.
- **M3U-afspeellijst** (`.m3u`) — een standaard afspeellijstformaat dat compatibel is met de meeste mediaspelers en radio-apps. Merk op dat M3U niet alle station-metadata opslaat, dus herstellen vanuit M3U kan resulteren in minder details dan een JSON-back-up.

**Favorieten importeren…** — laadt stations uit een eerder geëxporteerd JSON- of M3U-bestand. Na het selecteren van het bestand wordt gevraagd hoe de stations moeten worden toegevoegd:

- **Ja (Samenvoegen)** — voegt de geïmporteerde stations toe aan je bestaande lijst zonder huidige favorieten te verwijderen. Dubbele stations worden niet twee keer toegevoegd.
- **Nee (Vervangen)** — wist je huidige favorietenlijst volledig en vervangt deze door de inhoud van het geïmporteerde bestand.
- **Annuleren** — keert terug naar de stationsverkenner zonder wijzigingen aan te brengen.

Na een succesvolle import worden de favorietenlijst, de stationlijst voor geplande opnames en de stationlijst voor timers automatisch vernieuwd.

### Favorieten in groepen organiseren

Favorieten kunnen bij een map/groep horen, die wordt getoond als een "— Groep"-suffix achter de stationnaam in de lijst (bijvoorbeeld "NPR Newscast — NPR").

- **Importeren uit M3U** — als het bestand de `group-title`-tag gebruikt (de conventie die door DVBViewer en de meeste andere M3U-editors en -spelers wordt gebruikt) om stations in mappen te organiseren, leest freeAudio deze en behoudt de groep van elk station bij het importeren. Bij het exporteren van je favorieten terug naar M3U wordt dezelfde tag geschreven, zodat de mapstructuur een rondreis door freeAudio overleeft.
- **Een groep handmatig toewijzen of verwijderen** — markeer een of meer favorieten met `.` (zie [Meerdere items markeren en verwijderen](#meerdere-items-markeren-en-verwijderen) hierboven), kies vervolgens **Toewijzen aan Groep…** in het contextmenu (Toepassingentoets / `Shift+F10`) en typ een groepsnaam. Laat het veld leeg om de gemarkeerde favorieten uit hun groep te verwijderen. Als er niets is gemarkeerd, is het commando van toepassing op de momenteel geselecteerde favoriet.
- **Filteren op groep** — het Filter-veld boven de favorietenlijst komt ook overeen met groepsnamen en accepteert meerdere woorden die elk op een ander veld kunnen passen. Als je bijvoorbeeld `Houston Classical` typt, wordt "Houston Public Media Classical" gevonden, zelfs als die exacte zin nergens voorkomt — "Houston" komt overeen met de groep en "Classical" met de stationnaam.

### Favorieten opnieuw rangschikken

Met een station geselecteerd in het tabblad Favorieten, druk je op `komma` om de verplaats-modus te activeren — je hoort een pieptoon. Navigeer naar de doelpositie met de pijltoetsen en druk nogmaals op `komma`. Het station wordt op de gekozen positie geplaatst en de nieuwe volgorde wordt direct opgeslagen. Nogmaals op `komma` drukken op dezelfde positie annuleert de verplaatsing.

### Directe sneltoetsen voor favoriete stations

Elk station in je favorietenlijst wordt geregistreerd als een apart script in het dialoogvenster Invoerhandelingen van NVDA, onder de categorie **freeAudio Stations**. Je kunt elke sneltoets toewijzen aan elk station en deze vanaf elke locatie indrukken — je hoeft de stationsverkenner niet eerst te openen.

Een sneltoets toewijzen:

1. Open NVDA-menu → Opties → Invoerhandelingen.
2. Vouw de categorie **freeAudio Stations** uit.
3. Zoek het station op naam, selecteer het en druk op **Toevoegen**.
4. Druk de gewenste toetscombinatie in en bevestig.

De sneltoets activeert het station onmiddellijk. Als het station later uit je favorieten wordt verwijderd, verdwijnt het item uit de categorie en wordt elke eraan toegewezen sneltoets automatisch gewist door NVDA. Wanneer een nieuw station aan favorieten wordt toegevoegd, verschijnt het direct in de categorie — het dialoogvenster Invoerhandelingen hoeft niet opnieuw te worden geopend.

### Een aangepast station toevoegen

Om een station toe te voegen dat niet in Radio Browser staat, gebruik je de knop Aangepast station toevoegen. In het dialoogvenster dat verschijnt, voer je de stationnaam en stream-URL in om het direct aan je favorieten toe te voegen. Aangepaste stations kunnen worden afgespeeld en opnieuw worden gerangschikt, net als elke andere favoriet.

In dit dialoogvenster zijn twee extra knoppen beschikbaar:

- **URL testen** — controleert de stream-URL die je hebt ingevoerd voordat het station wordt toegevoegd, en kondigt aan of deze bereikbaar is. Handig om een typefout of dode link te ontdekken voordat deze in je favorietenlijst terechtkomt.
- **Toevoegen aan Radio Browser-directory…** — opent de [Radio Browser-indieningspagina](https://www.radio-browser.info/add) in je standaardbrowser, zodat je het station kunt delen met de bredere Radio Browser-gemeenschap zodra je hebt bevestigd dat het werkt. Zie [Een station toevoegen aan Radio Browser](#een-station-toevoegen-aan-radio-browser) hierboven voor wat het indieningsformulier verwacht.

### Audio-profiel van station

Het tabblad Favorieten bevat twee knoppen voor het beheren van audio-instellingen per station:

**Audio-profiel voor dit station opslaan** — slaat het huidige volumeniveau, actieve effecten (chorus, EQ, enz.) en EQ-gainwaarden op als een profiel dat gekoppeld is aan dat specifieke station. Telkens wanneer dat station begint te spelen, worden de opgeslagen volume-, effect- en gain-instellingen automatisch toegepast, waarbij de globale standaardwaarden worden overschreven.

**Audio-profiel wissen** — verwijdert het opgeslagen audioprofiel van het geselecteerde station. Na het wissen valt het station terug op de globale volume-, effect- en EQ-gain-instellingen. Deze knop is alleen actief wanneer het geselecteerde station al een opgeslagen profiel heeft.

Beide knoppen bevinden zich onder de favorietenlijst en zijn alleen ingeschakeld wanneer een station in de lijst is geselecteerd.

## Muziekherkenning

Drie keer drukken op `Ctrl+Win+I` activeert Shazam-gebaseerde muziekherkenning voor de momenteel spelende stream. Herkenning start alleen wanneer er geen ICY-metadata (trackinformatie uitgezonden door het station) beschikbaar is; als er metadata aanwezig is, wordt deze in plaats daarvan naar het klembord gekopieerd. Vier keer drukken op `Ctrl+Win+I` forceert herkenning, zelfs wanneer het station metadata uitzendt, wat helpt wanneer die metadata onjuist is.

Herkenning werkt als volgt: een kort audiofragment wordt vastgelegd van de stream met ffmpeg (dat zich identificeert zoals een mediaspeler, zodat stations die onbekende programma's weigeren toch antwoorden), het Shazam-vingerafdrukalgoritme wordt toegepast en het resultaat wordt naar de servers van Shazam gestuurd. Als de herkenning slaagt, worden de tracktitel, artiest, album en releasejaar door NVDA aangekondigd en automatisch naar het klembord gekopieerd. Als de optie **Gelikete nummers opslaan in een tekstbestand** is ingeschakeld, wordt het herkenningsresultaat ook toegevoegd aan `likedSongs.txt`.

Als ffmpeg de stream niet rechtstreeks kan lezen — bijvoorbeeld omdat het station de verbinding weigert, of omdat het streamadres eindigt op `.nsv` (typisch voor SHOUTcast-servers), waardoor ffmpeg het audioformaat verkeerd detecteert — neemt freeAudio zelf een kort fragment van de stream op en laat ffmpeg dat bestand decoderen. Dit gebeurt automatisch; er is geen instelling voor.

**Audiofeedback:** Twee stijgende piepjes klinken wanneer de herkenning start, en twee dalende piepjes wanneer deze eindigt. Een korte pieptoon klinkt elke 2 seconden terwijl het proces loopt.

**Vereiste:** ffmpeg.exe is vereist. Een ffmpeg.exe die in de add-on-map is geplaatst, wordt automatisch gebruikt; als deze op een andere locatie staat, kan het pad worden ingesteld in de Instellingen. Download ffmpeg van [ffmpeg.org](https://ffmpeg.org/download.html).

**Een opmerking over stations die reclame invoegen:** sommige stations sturen een korte advertentie naar elke gloednieuwe verbinding die met hun stream wordt gemaakt, los van de uitzending waarnaar je al aan het luisteren bent. Herkenning vermijdt het bemonsteren van die advertentie door de bestaande achtergrondstreamverbinding van freeAudio te hergebruiken (dezelfde die wordt gebruikt voor [Tijdverschuiving (live radio terugspoelen)](#tijdverschuiving-live-radio-terugspoelen)) in plaats van een nieuwe te openen, zodat het herkent wat er daadwerkelijk speelt in plaats van een advertentie. Dit werkt automatisch en vereist geen configuratie.

## Audio duplicatie

De `Ctrl+Win+M` sneltoets dupliceert de momenteel spelende stream naar een tweede audio-uitvoerapparaat. Dit is handig om naar twee verschillende apparaten tegelijk te luisteren, zoals luidsprekers en een hoofdtelefoon.

Bij de eerste keer drukken verschijnt een selectiedialoogvenster met de beschikbare uitvoerapparaten. Zodra een apparaat is gekozen, begint het dupliceren en gaat het hoofdafspelen ononderbroken door. Nogmaals op de sneltoets drukken stopt het dupliceren.

**Gebruiksscenario's:**

- **Luidsprekers + hoofdtelefoon** — Laat een gast dezelfde uitzending volgen op een hoofdtelefoon terwijl jij via de computerluidsprekers luistert.
- **Opname-setup** — Routeer de hoofduitvoer naar luidsprekers en de tweede uitvoer naar een externe recorder of audio-interface voor externe vastlegging.
- **Multi-room** — Speel tegelijkertijd af via een Bluetooth-luidspreker en de ingebouwde luidspreker; geen extra software nodig om audio naar een andere kamer te brengen.
- **Monitoring op afstand** — In een sessie voor het delen van schermen of extern bureaublad kunnen zowel de lokale als de externe kant tegelijkertijd naar dezelfde stream luisteren.

## Obligato-modus

De `Ctrl+Win+Shift+M` sneltoets speelt een favoriet station zacht op de achtergrond op een volledig aparte audio-engine van de hoofdspeler — als een zachte muzikale achtergrond die onder alles doorloopt wat je daadwerkelijk doet.

Bij de eerste keer drukken opent een dialoogvenster met drie bedieningselementen:

- **Achtergrondstation** — een lijst met je favoriete stations om te kiezen welke op de achtergrond wordt herhaald. Vereist ten minste één favoriet; als je favorietenlijst leeg is, vertelt freeAudio je eerst een station toe te voegen (`Ctrl+Win+V` terwijl een station speelt).
- **Audio-uitvoer** — via welk apparaat het achtergrondstation speelt: **Zelfde als hoofduitvoer** (standaard), **Systeemstandaard**, of een specifiek apparaat dat freeAudio kan zien.
- **Achtergrondvolume** — hoe luid het achtergrondstation speelt, als percentage van het huidige volume van de hoofdspeler (25%, 50%, 75%, 100%, 125% of 150%). Je keuzes worden onthouden voor de volgende keer.

Eenmaal gestart, blijft het achtergrondstation onafhankelijk van de hoofdspeler spelen — het wisselen van stations, podcasts of luisterboeken op de hoofdspeler, of het volledig stoppen ervan, onderbreekt de Obligato-modus niet. Twee dingen blijven automatisch gekoppeld aan de hoofdspeler:

- **Volume** — het achtergrondvolume wordt continu op het gekozen percentage gehouden van wat het huidige volume van de hoofdspeler ook is, dus het verhogen of verlagen van het hoofdvolume (`Ctrl+Win+↑`/`↓`) schaalt de achtergrondmuziek op dezelfde manier.
- **Pauze** — het pauzeren van de hoofdspeler (`Ctrl+Win+P`) pauzeert ook het achtergrondstation, en het hervatten van de hoofdspeler hervat het. Een volledige stop van de hoofdspeler wordt niet als pauze behandeld, dus het achtergrondstation blijft daardoor doorspelen.

Druk op elk moment opnieuw op `Ctrl+Win+Shift+M` om de Obligato-modus te stoppen.

## Opnemen

Opnames worden standaard opgeslagen in `Documents\freeAudio Recordings\`. De bestandsnaam bevat de stationnaam (of de nummertitel, in de nummer-opnamemodus) en de starttijd van de opname. De opnamemap kan op elk moment worden gewijzigd via NVDA-menu → Opties → Instellingen → freeAudio → **Opnamemap**.

De instelling **Opname-uitvoerformaat** bepaalt hoe voltooide opnames worden opgeslagen:

- **Origineel streamformaat** schrijft de stream precies zoals ontvangen. Een HLS-uitzending kan daardoor een `.ts`-bestand opleveren.
- **Alleen audio, originele codec** verwijdert de video/containerlaag zonder de audio opnieuw te coderen. AAC-audio van een HLS `.ts`-opname wordt bijvoorbeeld normaal opgeslagen als `.m4a`, met behoud van uitzendkwaliteit.
- **MP3** converteert de audio na het opnemen met de geselecteerde bitsnelheid. Conversie gebruikt de `ffmpeg.exe` die met freeAudio is meegeleverd en draait op de achtergrond zodat NVDA responsief blijft. Als conversie mislukt, blijft de originele opname behouden.

**Direct opnemen:** Terwijl een station speelt, druk je eenmaal op `Ctrl+Win+E`. Druk nogmaals om te stoppen. Het afspelen gaat gedurende de hele tijd ononderbroken door.

**Nummeropname (huidig nummer):** Druk **tweemaal** snel achter elkaar op `Ctrl+Win+E` terwijl een station dat ICY-metadata uitzendt aan het spelen is. De opname start een moment na de tweede druk — freeAudio wacht even in geval je een derde keer drukt — en is vernoemd naar de huidige tracktitel. Wanneer het station het volgende nummer aankondigt, stopt de opname op dat punt en kondigt NVDA de opgeslagen bestandsnaam aan. Om de opname vroegtijdig te beëindigen, druk je nogmaals tweemaal op `Ctrl+Win+E`. Als het huidige station geen ICY-metadata uitzendt, is nummeropname niet beschikbaar en zal NVDA dit melden.

**Elk-nummer-opname:** Druk **driemaal** snel achter elkaar op `Ctrl+Win+E` om elk nummer op te nemen dat het station speelt tot je stopt. freeAudio houdt één verbinding open en begint bij elke trackwissel een nieuw bestand, zodat er niets tussen nummers verloren gaat. Elk nummer wordt opgeslagen als een eigen bestand, vernoemd naar het nummer en de tijd waarop het begon. Wanneer de opname start, kondigt NVDA aan dat elk nummer wordt opgenomen en geeft de huidige titel. Om te stoppen, druk je tweemaal op `Ctrl+Win+E`; NVDA kondigt aan hoeveel nummers zijn opgeslagen.

Een paar details over elk-nummer-opname:

- Het eerste nummer (opgenomen vanaf het moment dat je de toetsen indrukte) en het laatste nummer (afgebroken wanneer je stopt) zijn onvolledig, dus hun bestandsnamen bevatten **(partial)** — bijvoorbeeld `Artiest - Titel (partial) - 2026-10-09 10-15.mp3`.
- Fragmenten korter dan 15 seconden — jingles, advertentiesticks, of een titel die tussen twee waarden flikkert — worden weggegooid in plaats van opgeslagen.
- Het vereist dat het station zijn tracktitels in de audiostream zelf meestuurt (ICY-metadata). HLS (`.m3u8`)-stations, en servers die geen titels op die manier versturen, kunnen niet in nummers worden opgesplitst; NVDA vertelt je dit en er wordt niets opgenomen.
- Terwijl het loopt, kondigt `Ctrl+Win+I` het nummer aan dat op dat moment wordt opgenomen, niet het nummer waarmee het begon.

**Geplande opname:** Open het tabblad Opnemen in de stationsverkenner. Selecteer een station uit je favorieten, voer de starttijd in UU:MM-formaat in en de duur in minuten, selecteer een of meer actieve dagen, kies vervolgens een herhalingsmodus en een opnamemodus:

Een **Filter**-veld boven de stationlijst laat je de favorietenlijst in realtime beperken, zodat je snel het station kunt vinden dat je wilt plannen.

**Actieve dagen:** Vink een of meer dagen van de week aan. In de modus "eenmalige opname" wordt voor elke geselecteerde dag een apart item gemaakt, elk geplaatst op de eerstvolgende komende gelegenheid van die dag. In de herhalingsmodus herhaalt de opname zich alleen op de aangevinkte dagen. Als er geen dagen zijn aangevinkt, is de opname niet beperkt tot specifieke dagen.

**Herhaling:**

- **Eenmalig opnemen** — neemt eenmaal op op elke geselecteerde dag. Elk item wordt geplaatst op de eerstvolgende komende gelegenheid van die dag; als de geselecteerde tijd vandaag al is verstreken, verplaatst het item zich automatisch naar dezelfde dag volgende week.
- **Wekelijks herhalen** — herhaalt elke week op de geselecteerde actieve dagen totdat het uit de planningslijst wordt verwijderd.

**Opname opslaan in:** Voor elke geplande opname kun je kiezen om op te slaan in de standaardopnamemap of een aangepaste map. Gebruik de knop **Bladeren...** om interactief een map te selecteren. Als de gekozen map niet meer beschikbaar is, valt de opname terug op de standaardmap en word je op de hoogte gesteld.

**Opnamemodus:**

- **Opnemen tijdens luisteren** — speelt af en neemt tegelijkertijd op via de BASS-backend.
- **Alleen opnemen** — neemt stil op de achtergrond op zonder audio-uitvoer; de opname-engine maakt direct verbinding met de stream.

Zodra een planning is toegevoegd, verschijnt deze in de lijst eronder. Gebruik de knop **Geselecteerde verwijderen** om een planning te verwijderen, of **Geselecteerde bewerken** om de tijd, duur, herhaling, actieve dagen, opnamemodus of uitvoermap te wijzigen.

NVDA kondigt aan wanneer een opname start en wanneer deze eindigt. Als NVDA opnieuw wordt opgestart terwijl een geplande opname actief is, wordt de opname bij het opstarten automatisch hervat.

**Hoe opnames verbinden:** Directe opname, nummeropname en elk-nummer-opname openen hun eigen verbinding met het station in plaats van te kopiëren wat je hoort, dus een directe opname of elk-nummer-opname blijft doorgaan wanneer je het afspelen pauzeert of naar een ander station schakelt — het gaat verder met het station waarmee het begon. Het stoppen van het afspelen met `Ctrl+Win+S` terwijl een opname loopt, vraagt eerst om bevestiging, omdat het ook de opname beëindigt. De keerzijde van een aparte verbinding is dat een station dat bij elke gloednieuwe verbinding een korte advertentie serveert, die advertentie aan het begin van het bestand kan plaatsen.

## Tijdverschuiving (live radio terugspoelen)

Met Tijdverschuiving kun je het station waarnaar je momenteel luistert terugspoelen, zoals een DVR of een cassettebandje — pauzeer het moment, ga een paar minuten terug en haal de live-uitzending in wanneer je maar wilt. Het afspelen hoeft hiervoor nooit te stoppen: terugspoelen en vooruitspoelen gebeuren beide onmiddellijk op dezelfde audiostream.

Deze functie is **standaard uitgeschakeld**. Schakel het in via NVDA-menu → Opties → Instellingen → freeAudio → **Tijdverschuivingsbuffer inschakelen (live radio terugspoelen)**, of schakel het op elk gewenst moment direct in met `Ctrl+Win+T`.

> **Opmerking:** freeAudio houdt altijd een kleine achtergrondopname van het momenteel spelende station actief — niet alleen wanneer deze instelling is ingeschakeld — omdat [Muziekherkenning](#muziekherkenning) hierop vertrouwt voor het advertentievermijdingsgedrag dat in die sectie wordt beschreven. Wanneer deze instelling **uit** staat, blijft die achtergrondopname beperkt tot ongeveer de laatste 45 seconden en blijven `Ctrl+Win+J`/`Ctrl+Win+K` onbeschikbaar — alleen de buffergrootte verandert, niet of hij actief is. Het inschakelen van deze instelling laat dezelfde opname groeien tot de volledige terugspoelbuffer die hieronder wordt beschreven.

### Hoe het werkt

Eenmaal ingeschakeld, legt freeAudio op de achtergrond continu het momenteel spelende station vast in een rollende lokale buffer, onafhankelijk van het normale afspelen. De buffer bevat de meest recente audio, tot de lengte die is ingesteld met de instelling **Duur van tijdverschuivingsbuffer**; oudere audio wordt automatisch aan de voorkant verwijderd naarmate er nieuwe audio binnenkomt, zodat de buffer altijd "het recente verleden" ten opzichte van de live-uitzending vertegenwoordigt.

- **`Ctrl+Win+J`** — 15 seconden terugspoelen. De eerste druk schakelt je van live afspelen naar Tijdverschuivingsmodus, beginnend 15 seconden achter de live-uitzending. Elke volgende druk gaat nog eens 15 seconden verder terug, tot de limiet van de buffer.
- **`Ctrl+Win+K`** — 15 seconden vooruitspoelen tijdens Tijdverschuiving. Zodra je de live-uitzending bereikt, schakelt het afspelen automatisch terug naar de live-stream en kondigt NVDA "Terug naar live" aan — je hoeft niets extra's te doen om het normale luisteren te hervatten.
- **`Ctrl+Win+Alt+J`** / **`Ctrl+Win+Alt+K`** — Hetzelfde terug- en vooruitspoelen, maar in stappen van 1 seconde in plaats van 15, voor fijne aanpassingen. Zie [Nauwkeurig zoeken (1 seconde)](#nauwkeurig-zoeken-1-seconde).
- **`Ctrl+Win+T`** — Schakelt de hele functie in of uit. Uitschakelen terwijl je Tijdverschuiving gebruikt, brengt je onmiddellijk terug naar live afspelen en stopt de achtergrondopname voor het huidige station.

Achtergrondopname blijft de hele tijd draaien terwijl je Tijdverschuiving gebruikt, dus de live-uitzending blijft bijgehouden worden, zelfs terwijl je naar iets van een paar minuten oud luistert — precies zoals bij een echte DVR.

### Inschakelen en buffer vullen

De buffer begint te vullen zodra een station begint te spelen (zodra de functie is ingeschakeld) of op het moment dat je de functie inschakelt terwijl je al naar een station luistert. Vanwege dit is terugspoelen pas mogelijk nadat er daadwerkelijk een paar seconden audio is vastgelegd — als je direct na het wisselen van station op `Ctrl+Win+J` drukt, zal NVDA je laten weten dat er nog niet genoeg gebufferde audio is. Wacht gewoon een paar seconden en probeer het opnieuw.

Overstappen naar een ander station herstart altijd de buffer voor het nieuwe station; de gebufferde audio van het vorige station wordt verwijderd.

### Ondersteunde streams

Tijdverschuiving werkt met hetzelfde bereik van streams dat freeAudio al ondersteunt:

- Gewone HTTP/HTTPS-streams (MP3, AAC, OGG, enz.), inclusief Shoutcast/Icecast-stijl servers.
- **HLS (`.m3u8`) streams** — freeAudio lost de hoofdafspeellijst van het station op, volgt de media-afspeellijst en downloadt segmenten op de achtergrond om de buffer gevuld te houden, op dezelfde manier als bij gewone streams.

In het zeldzame geval dat de afspeellijst van een station helemaal niet kan worden gelezen (bijvoorbeeld een defect of onbereikbaar `.m3u8`-manifest), zal NVDA je vertellen dat terugspoelen niet beschikbaar is voor dat specifieke station.

### Vereisten en beperkingen

- **Vereist de BASS-backend**, die freeAudio altijd voor afspelen gebruikt (zie [Afspelen](#afspelen)).
- De lengte van de buffer wordt ingesteld met de instelling **Duur van tijdverschuivingsbuffer** — zie [Instellingen](#instellingen).
- De buffer is per station: wisselen van station, stoppen met afspelen of opnieuw opstarten van NVDA wist deze en begint opnieuw.
- Tijdverschuivingsmodus gebruikt zijn eigen lokale bufferbestand en genereert geen opgeslagen opname — als je de audio permanent wilt behouden, gebruik dan ook Direct opnemen (`Ctrl+Win+E`).

## Timer

Open het tabblad Timer in de Stationsverkenner (`Alt+4`). Er kunnen twee soorten timers worden toegevoegd:

Bij het kiezen van een station voor een wekkertimer laat een **Filter**-veld boven de stationlijst je de favorietenlijst in realtime beperken.

**Wekker — radio starten:** Start automatisch het afspelen van een geselecteerd station uit je favorieten op de opgegeven tijd. Kies een station en voer de tijd in HH:MM-formaat in.

**Slaaptimer — radio stoppen:** Stopt het afspelen op de opgegeven tijd. Wanneer de timer afgaat, wordt het volume gedurende 60 seconden geleidelijk verlaagd voordat het afspelen stopt. Er is geen stationsselectie nodig; voer gewoon de tijd in.

Voor beide typen geldt: als de ingevoerde tijd al is verstreken, wordt de actie gepland voor de volgende dag. Het toevoegen van een timer wordt geblokkeerd als er al een andere timer — van welk type dan ook — op hetzelfde tijdstip bestaat; een bericht informeert je over het conflict en vraagt je om het bestaande item eerst te verwijderen. Lopende timers worden vermeld in het tabblad; selecteer er een en druk op de knop Geselecteerde timer verwijderen om deze te annuleren.

**Terugkerende timers:** Kies onder **Herhaling** de optie **Wekelijks herhalen** in plaats van de standaard eenmalige optie om de timer elke week te laten afgaan in plaats van één keer. Een **Actieve dagen**-checklist laat je vervolgens kiezen op welke dagen van de week hij wordt herhaald; als je alle dagen uitgevinkt laat, wordt hij elke dag herhaald. Een terugkerende timer blijft volgens schema afgaan tot je hem uit de lijst met lopende timers verwijdert — het is geen eenmalig item dat na afgaan verdwijnt.

## Podcasts

freeAudio bevat een volledig uitgeruste podcastspeler. Je kunt je abonneren op elke RSS- of Atom-podcastfeed, afleveringen bekijken, afspelen, downloaden en het afspelen hervatten waar je gebleven was — allemaal volledig toegankelijk.

### Toegang tot het tabblad Podcasts

Open de stationsverkenner met `Ctrl+Win+R` en schakel naar het tabblad **Podcasts** met `Ctrl+Tab` of `Alt+6`. Het tabblad is georganiseerd in drie hoofdgebieden:

1. **Zoeken en toevoegen** — bovenste gedeelte voor het ontdekken van nieuwe podcasts, inclusief een voorbeeldlijst die de afleveringen toont van welk zoekresultaat dan ook dat momenteel is geselecteerd.
2. **Abonnementen** — lijst van je geabonneerde feeds.
3. **Afleveringen** — lijst van afleveringen voor de geselecteerde feed, met afspeelbediening. Een **Bladwijzers**-lijst direct eronder toont de bladwijzers van de geselecteerde aflevering — zie [Bladwijzers](#bladwijzers).

### Een podcastfeed toevoegen

Je kunt een podcastfeed op twee manieren toevoegen:

**Via URL:**

- Plak in het **Zoeken**-veld de volledige RSS- of Atom-feed-URL (bijvoorbeeld `https://example.com/feed.xml`).
- Druk op Enter.
- freeAudio haalt de feed op, valideert deze en voegt deze toe aan je abonnementen. Als de feed geldig is, hoor je een bevestiging met de feedtitel. Als het mislukt, legt een foutmelding uit waarom.

**Via zoeken:**

- Typ in het **Zoeken**-veld een trefwoord (podcasttitel, onderwerp of naam van de presentator) en druk op Enter.
- freeAudio doorzoekt de iTunes-podcastdirectory en toont overeenkomende podcasts in de lijst **Zoekresultaten**.
- Door een resultaat te selecteren wordt die feed op de achtergrond opgehaald en worden de afleveringen getoond in de lijst **Afleveringen in geselecteerd resultaat** er direct onder, zodat je kunt bekijken wat de show daadwerkelijk bevat voordat je besluit je te abonneren — zie [Afleveringen bekijken voordat je je abonneert](#afleveringen-bekijken-voordat-je-je-abonneert) hieronder.
- Als je tevreden bent met wat je ziet, selecteer je het resultaat en druk je op `Enter`, of open je het contextmenu (Toepassingentoets / `Shift+F10`, of rechtermuisknop) en kies je **Abonneren**, om het aan je abonnementen toe te voegen. De feed wordt onmiddellijk toegevoegd en verschijnt in je abonnementenlijst. Er is geen aparte knop "Geselecteerde uit zoekresultaten toevoegen" — `Enter` of het contextmenu is de enige manier om je vanuit zoekresultaten te abonneren, wat de interface schoon en toegankelijk houdt.

> **Tip:** Je kunt ook rechtstreeks een feed-URL in het zoekveld typen — als het op een geldige URL lijkt, probeert de add-on deze als feed toe te voegen zonder te zoeken.

**Contextmenu voor zoekresultaten:** Klik met de rechtermuisknop op een zoekresultaat, of selecteer het en druk op de Toepassingentoets / `Shift+F10`, om een menu met één actie **Abonneren** te openen, identiek aan het indrukken van `Enter` op het resultaat.

### Afleveringen bekijken voordat je je abonneert

Voordat je je vastlegt op een abonnement, kun je naar de afleveringen van een podcast luisteren rechtstreeks vanuit de zoekresultaten. Telkens wanneer je een podcast selecteert in de lijst **Zoekresultaten**, haalt freeAudio die feed op en toont de afleveringen — titel en publicatiedatum — in de lijst **Afleveringen in geselecteerd resultaat** eronder.

- Selecteer een aflevering in die voorbeeldlijst en druk op `Enter`, of open het contextmenu (Toepassingentoets / `Shift+F10`, of rechtermuisknop) en kies **Voorbeeld**, om deze via de normale speler af te spelen. Alle gebruikelijke afspeelbediening (pauze, volume, tijdverschuiving, enz.) werkt erop precies zoals op elk ander station of elke andere aflevering.
- Terwijl een aflevering wordt bekeken, toont hetzelfde contextmenu **Stop voorbeeld** in plaats van **Voorbeeld** — kies het, of druk nogmaals op `Enter` op die aflevering, om te stoppen.
- Een voorbeeld bekijken abonneert je nergens op; het is puur om te luisteren voordat je besluit. De voorbeeldlijst zelf is tijdelijk — deze wordt vervangen zodra je een ander zoekresultaat selecteert, en wordt nergens bewaard zoals je werkelijke abonnementen.

### Abonnementen beheren

Zodra je enkele feeds hebt toegevoegd, verschijnen ze in de lijst **Abonnementen**. Elk item toont de feedtitel en het aantal beschikbare afleveringen.

- **Selecteer een feed** om de afleveringen in de onderste lijst te zien. Het alleen-lezen tekstvak **Feedeigenschappen** onder de abonnementenlijst toont de feedtitel, auteur, beschrijving, het aantal afleveringen en de URL.
- **Een feed vernieuwen** — selecteer deze en druk op de knop **Werk feed bij** (beschikbaar via het contextmenu, zie hieronder) om de nieuwste afleveringen op te halen. Alle feeds worden ook automatisch op de achtergrond vernieuwd wanneer je het tabblad Podcasts opent, dus je ziet meestal de meest recente afleveringen zonder handmatige tussenkomst.
- **Een feed verwijderen** — selecteer deze en druk op `Delete` of gebruik het contextmenu om deze uit je abonnementen te verwijderen. Je wordt om bevestiging gevraagd voordat deze wordt verwijderd.

**Contextmenu voor feeds:** Klik met de rechtermuisknop op een feed, of selecteer deze en druk op de Toepassingentoets / `Shift+F10`, om een menu te openen met:

- **Werk feed bij** — haal nu nieuwe afleveringen op.
- **Audioprofiel voor deze podcast opslaan** / **Audioprofiel wissen** — zie [Podcast-audioprofiel](#podcast-audioprofiel).
- **Feed verwijderen** — verwijder het abonnement.
- **Kopieer de feed-URL** — kopieer de feed-URL naar het klembord.

### Afleveringen bekijken en afspelen

Selecteer een feed in de abonnementenlijst; de afleveringen verschijnen in de lijst **Afleveringen** eronder. Elke aflevering toont:

- Het afleveringsnummer (1 = de oudste aflevering in de feed, oplopend tot de nieuwste).
- De publicatiedatum (indien beschikbaar).
- De titel.
- Een **"[geluisterd]"**-prefix als de aflevering volledig is afgespeeld.
- Een duursuffix, ofwel de totale duur (als er nooit naar is geluisterd) of de verstreken/totale voortgang (als er gedeeltelijk naar is geluisterd).

**Afspelen:**

- Selecteer een aflevering en druk op `Enter` of `Space` om deze te starten. Als er eerder gedeeltelijk naar een aflevering is geluisterd, wordt deze hervat waar je gebleven was.
- De rij wordt *niet* bijgewerkt terwijl de aflevering speelt — dit is opzettelijk, zodat NVDA de rij niet herhaaldelijk opnieuw aankondigt terwijl je erop staat. De "geluisterd"-markering en duur worden onmiddellijk vernieuwd op het moment dat je de aflevering pauzeert of deze afloopt, dus de weergave is altijd nauwkeurig precies wanneer het ertoe doet; hij telt alleen niet seconde voor seconde op tijdens het afspelen.
- Gebruik `F3` / `F4` op het tabblad Podcasts om naar de vorige / volgende aflevering te gaan en deze direct af te spelen. Je kunt ook `←` / `→` gebruiken terwijl de afleveringenlijst is gefocust, of `Ctrl+←` / `Ctrl+→` overal op het tabblad Podcasts — beide werken identiek.
- Gebruik `Shift+F3` / `Shift+F4` om tussen feeds te wisselen zonder afleveringen af te spelen.
- Druk op `Space` terwijl een aflevering speelt om het afspelen te pauzeren of te hervatten.

**Afspelen hervatten:** freeAudio slaat je positie in elke podcastaflevering automatisch op — onmiddellijk wanneer je pauzeert of de aflevering afloopt, en elke 15 seconden op de achtergrond terwijl je blijft luisteren, zodat een crash of onverwachte herstart niet veel voortgang verliest. Als je het afspelen stopt of pauzeert en later terugkomt, wordt de aflevering hervat vanaf de opgeslagen positie. Als je de aflevering tot het allerlaatste einde afspeelt (binnen de laatste 3 seconden), wordt deze gemarkeerd als "[geluisterd]" en wordt deze niet hervat — de volgende keer begint deze vanaf het begin, en de "[geluisterd]"-prefix verschijnt in de lijst.

**Contextmenu voor afleveringen:** Klik met de rechtermuisknop op een aflevering, of selecteer deze en druk op de Toepassingentoets / `Shift+F10`, om een menu te openen met:

- **Aflevering afspelen** — start het afspelen.
- **Aflevering downloaden** — download het afleveringsbestand naar je opnamemap.
- **Audioprofiel voor deze podcast opslaan** / **Audioprofiel wissen** — dezelfde commando's als het contextmenu van de feed zelf, hier voor het gemak opgenomen zodat je niet terug hoeft naar de abonnementenlijst. Ze slaan nog steeds één profiel op voor de hele podcast, niet een apart profiel voor deze aflevering — zie [Podcast-audioprofiel](#podcast-audioprofiel).
- **Kopieer de URL van de aflevering** — kopieer de directe audio-URL naar het klembord.

### Afleveringen downloaden

Selecteer een aflevering en klik op de knop **Aflevering downloaden** (of gebruik het contextmenu). De aflevering wordt gedownload naar je opnamemap (`Documents\freeAudio Recordings\` standaard). De bestandsnaam is gebaseerd op de afleveringstitel en de gedetecteerde bestandsextensie (`.mp3`, `.m4a`, `.ogg`, enz.). NVDA kondigt aan wanneer de download start en eindigt. Als het bestand al bestaat, word je geïnformeerd en wordt de download overgeslagen.

### Afleveringen filteren

Boven de afleveringenlijst staat een **Filter**-veld. Terwijl je typt, wordt de afleveringenlijst in realtime gefilterd om afleveringen te tonen waarvan de titel de getypte tekst bevat, of waarvan het afleveringsnummer er exact mee overeenkomt — dus door `47` te typen spring je direct naar aflevering 47, zelfs als "47" nergens in de titel voorkomt. NVDA kondigt na elke wijziging het aantal overeenkomende afleveringen aan. Druk op de pijl-omlaag vanuit het filterveld om de focus direct in de gefilterde lijst te verplaatsen.

### Afspeeldetails van podcasts

Podcastafleveringen worden afgespeeld via de **BASS-backend** (dezelfde engine die voor radiostreams wordt gebruikt, en de enige afspeelbackend die freeAudio gebruikt). Omdat afleveringen progressief worden gedownload en doorzoekbaar zijn, kun je tijdens het afspelen van een podcast de tijdverschuivingssneltoetsen (`Ctrl+Win+J`/`Ctrl+Win+K`) gebruiken om binnen de aflevering te zoeken. De positie wordt automatisch opgeslagen zodat je later kunt hervatten.

**Getrapt zoeken:** In tegenstelling tot het vaste 15-seconden terugspoelen van live radio, schaalt het zoeken binnen een podcast, luisterboek of jukeboxnummer met hoe je de toets indrukt, zodat je een kleine correctie kunt maken of een heel eind kunt springen zonder herhaald drukken:

- **De toets ingedrukt houden** (automatische herhaling) stapt **5 seconden** per herhaling terug of vooruit — dezelfde kleine stap die de sneltoets op bestanden gebruikt.
- **Eén bewuste druk** zoekt **12 seconden**.
- **Twee drukken** snel achter elkaar zoeken **1 minuut**.
- **Drie of meer drukken** zoeken **5 minuten**; verdere drukken in dezelfde reeks escaleren niet verder.

Een bewuste druk wordt even vastgehouden voordat er daadwerkelijk wordt gezocht, voor het geval er nog een druk komt — er vindt slechts één zoekactie per drukreeks plaats, geschaald naar het uiteindelijke aantal drukken, niet de som van elke druk. Na een zoekactie kondigt NVDA de resulterende verstreken/resterende positie in de aflevering aan in plaats van alleen "X seconden vooruit/achteruit".

### Nauwkeurig zoeken (1 seconde)

Voor kleine correcties, zoals het opnieuw afspelen van een woord dat je net hebt gemist, heeft freeAudio een apart paar commando's die altijd precies **1 seconde** verplaatsen, ongeacht hoe je ze indrukt:

- **`Ctrl+Win+Alt+J`** — 1 seconde terug, vanaf elke locatie in Windows.
- **`Ctrl+Win+Alt+K`** — 1 seconde vooruit, vanaf elke locatie in Windows.
- **`Alt+←`** / **`Alt+→`** — dezelfde twee commando's binnen de stationsverkenner, op elk tabblad.

Op een podcastaflevering, een deel van een luisterboek of een jukeboxnummer werken ze precies zoals de normale zoekcommando's, alleen met een stap van 1 seconde: NVDA kondigt de resulterende verstreken/resterende positie aan, en op een luisterboek of jukeboxmap gedragen de deel- en nummergrenzen zich zoals beschreven voor `Ctrl+Win+J` / `Ctrl+Win+K` (een zoekactie vooruit voorbij het einde gaat verder naar het volgende deel of nummer; een terugspoeling voorbij het begin stopt eerst op 0:00 en alleen een tweede terugspoeling binnen 10 seconden gaat terug naar het vorige deel of nummer).

Op een live radiostation verplaatsen ze 1 seconde in de tijdverschuivingsbuffer. Net als bij `Ctrl+Win+J` moet de buffer zijn ingeschakeld in de instellingen, en de eerste terugspoeling schakelt over van live afspelen naar afspelen met tijdverschuiving. Een vooruitspoeling die binnen ongeveer 2 seconden van de live-uitzending eindigt, keert terug naar live en kondigt "Terug naar live" aan.

**Afspeelsnelheid:** Je kunt de afspeelsnelheid van podcastafleveringen, luisterboeken en jukeboxnummers aanpassen met `Ctrl+Win+Shift+K` (sneller) en `Ctrl+Win+Shift+J` (langzamer). De snelheid verandert in stappen van 0,1x, variërend van 0,5x tot 2,0x, met behoud van toonhoogte.

**Transponeren (toonhoogteverschuiving):** Onafhankelijk van de afspeelsnelheid kun je de toonhoogte van een podcastaflevering, luisterboek of jukeboxnummer omhoog of omlaag verschuiven met `Shift+Win+K` / `Shift+Win+J` — zie [Transponeren (toonhoogteverschuiving)](#transponeren-toonhoogteverschuiving).

**Geluidseffect bij hervatten:** Telkens wanneer een aflevering wordt hervat vanaf een opgeslagen positie, speelt freeAudio kort een zacht cassette-laden-geluidseffect af op een apart kanaal terwijl het terugspoelt naar je opgeslagen plek, in plaats van de eigen audio van de aflevering hoorbaar vanaf 0:00 te laten spelen. Dit is onafhankelijk van de instelling **Vloeiende stationsovergang** — die instelling beïnvloedt alleen het wisselen tussen live radiostations, niet het hervatten van podcasts of luisterboeken.

### Podcast-audioprofiel

Klik met de rechtermuisknop op een podcast in de Abonnementenlijst, of op een van zijn afleveringen, en kies **Audioprofiel voor deze podcast opslaan** om het huidige volume, de effecten, de EQ-gains en/of de afspeelsnelheid op te slaan als een profiel dat aan die podcast is gekoppeld. Telkens wanneer een aflevering van die podcast speelt, worden de opgeslagen instellingen automatisch toegepast, waarbij de globale standaardwaarden worden overschreven. Omdat het commando beschikbaar is via zowel het contextmenu van de feed als dat van de aflevering, kun je het bereiken zonder terug te schakelen naar de Abonnementenlijst — hoe dan ook slaat het altijd één profiel op voor de hele podcast, niet een apart profiel per aflevering.

Een dialoogvenster met 15 opties laat je precies kiezen wat je wilt opslaan:

- **Alleen volume**
- **Alleen effecten**
- **Volume en effecten**
- **Volume en afspeelsnelheid**
- **Effecten en afspeelsnelheid**
- **Alleen afspeelsnelheid**
- **Volume, effecten en afspeelsnelheid**
- **Alleen toonhoogte transponeren**
- **Volume en toonhoogte transponeren**
- **Effecten en toonhoogte transponeren**
- **Afspeelsnelheid en toonhoogte transponeren**
- **Volume, effecten en toonhoogtetranspositie**
- **Volume, afspeelsnelheid en toonhoogte transponeren**
- **Effecten, afspeelsnelheid en toonhoogte transponeren**
- **Volume, effecten, afspeelsnelheid en toonhoogtetranspositie**

Alleen de onderdelen die je kiest, worden naar het profiel geschreven; alles wat je weglaat, behoudt wat er al voor was opgeslagen. Als je bijvoorbeeld **Alleen afspeelsnelheid** kiest op een podcast die al een opgeslagen volume-/effectenprofiel heeft, wordt alleen de snelheid bijgewerkt en blijft de rest ongewijzigd.

**Audioprofiel wissen** verwijdert het opgeslagen profiel van de podcast, vanuit beide contextmenu's. Het is alleen ingeschakeld wanneer de podcast momenteel een opgeslagen profiel heeft.

### Opslag van podcastgegevens

Je abonnementen worden opgeslagen in `freeAudio_podcasts.json` in de NVDA-gebruikersconfiguratiemap. Afleveringsposities worden apart opgeslagen in `podcast_positions.json` op dezelfde locatie. Beide bestanden zijn gewone JSON en kunnen worden geback-upt of naar een andere computer worden overgebracht.
## Luisterboeken (GETEM, LibriVox en Project Gutenberg)

freeAudio bevat een luisterboekenspeler die boeken zoekt, afspeelt en downloadt uit drie bronnen:

- **[GETEM](https://getem.boun.edu.tr/)** — de digitale bibliotheek van het Centrum voor Slechtzienden van de Boğaziçi Universiteit. Vereist een gratis lidmaatschap om de audio van een boek te streamen of te downloaden (bladeren niet) — zie [Aanmelden](#aanmelden) hieronder.
- **[LibriVox](https://librivox.org/)** — het door vrijwilligers voorgelezen publiek-domein luisterboekproject. Er is geen account of aanmelding van welke aard dan ook nodig; de hele catalogus, inclusief de audiobestanden zelf, is publiek domein en openlijk toegankelijk.
- **Project Gutenberg Open Audiobook Collection** — door mensen en computers voorgelezen publiek-domein luisterboeken gehost op [archive.org](https://archive.org/), metgezel van de Project Gutenberg-tekstbibliotheek. Net als LibriVox is er geen account of aanmelding nodig.

Resultaten uit alle drie de bronnen verschijnen samen in één samengevoegde lijst **Zoekresultaten** en één samengevoegde lijst **Bibliotheek** — er is geen apart tabblad of vervolgkeuzelijst om tussen hen te wisselen. De bron van elk boek (GETEM, LibriVox of Project Gutenberg) wordt getoond als een label naast de titel, en in de details, zodat je altijd kunt zien naar welke je kijkt. Je kunt boeken uit elke bron op precies dezelfde manier zoeken, bekijken, toevoegen, afspelen en downloaden; werken met meerdere delen afspelen met automatisch hervatten tussen delen; en boeken downloaden voor offline luisteren — allemaal volledig toegankelijk.

Elke bron kan afzonderlijk worden uitgeschakeld via **NVDA-menu → Opties → Instellingen → freeAudio** met de checklist **Luisterboekbronnen**, als je er slechts enkele wilt doorzoeken. Alle drie zijn standaard ingeschakeld.

> **Opmerking:** Naar een GETEM-boek luisteren vereist een gratis GETEM-lidmaatschap. Bladeren door de catalogus van GETEM vereist geen account, maar het ophalen en afspelen van de audio van een GETEM-boek wel — zie [Aanmelden](#aanmelden) hieronder. LibriVox- en Project Gutenberg-boeken vereisen nooit een account.

### Toegang tot het tabblad Luisterboeken

Open de stationsverkenner met `Ctrl+Win+R` en schakel naar het tabblad **Luisterboeken** met `Ctrl+Tab` of `Alt+7`. Het tabblad heeft drie hoofdgebieden:

1. **Zoeken** — een tekstveld om alle ingeschakelde catalogi tegelijk te doorzoeken, met een resultatenlijst die verschijnt zodra een zoekopdracht is uitgevoerd.
2. **Bibliotheek** — de lijst met boeken die je uit elke bron hebt toegevoegd, waar je ze afspeelt, downloadt en beheert. Een **Bladwijzers**-lijst direct eronder toont de bladwijzers van het geselecteerde boek — zie [Bladwijzers](#bladwijzers).
3. **Details** — een alleen-lezen vak met de bron, titel, auteur, verteller, uitgever, formaat, het aantal delen, de beschrijving en de catalogus-URL van welk boek dan ook dat in een van beide lijsten is geselecteerd.

### Aanmelden

GETEM vereist dat je een geregistreerd lid bent om de daadwerkelijke audio van een boek te streamen of te downloaden, ook al kan de catalogus zelf vrij worden doorzocht. Voer je GETEM-gebruikersnaam en wachtwoord één keer in via **NVDA-menu → Opties → Instellingen → freeAudio**; ze worden versleuteld op schijf opgeslagen (via de Windows Data Protection API, gekoppeld aan je Windows-gebruikersaccount) en daarna automatisch hergebruikt. Als je probeert een GETEM-boek af te spelen of te downloaden voordat je inloggegevens hebt ingevoerd, vertelt freeAudio je eerst dat je ze in de Instellingen moet toevoegen.

LibriVox en Project Gutenberg hebben helemaal geen aanmeldingsstap nodig — hun resultaten en audio kunnen onmiddellijk worden doorzocht, bekeken, afgespeeld en gedownload, zonder inloggegevens in te voeren.

### Luisterboeken zoeken

Typ een zoekterm in het zoekveld en druk op `Enter`. freeAudio doorzoekt de bronnen die in de Instellingen zijn ingeschakeld en voegt de resultaten samen in één lijst:

- **GETEM** wordt doorzocht op titel, auteur, verteller, onderwerp en uitgever tegelijk, omdat GETEM's eigen zoekformulier alleen het beperken op alle tegelijk ondersteunt in plaats van één zoekopdracht over elk ervan. Alleen werken die daadwerkelijk beschikbaar zijn als audio (menselijke of computervoorlezing, audiodescriptie, hoorspel, DAISY-sprekende boeken, enz.) worden getoond; braille, grootletterdruk en andere niet-audioformaten worden automatisch uitgefilterd.
- **LibriVox** wordt doorzocht op titel of auteur/lezer in zijn publiek-domein catalogus.
- **Project Gutenberg** wordt doorzocht op titel of auteur in de Open Audiobook Collection op archive.org.

Het rechtstreeks plakken van de catalogus-/detailpagina-URL van een boek in het zoekveld (een GETEM-cataloguspagina, of een archive.org "details"-pagina voor een LibriVox- of Project Gutenberg-titel) herleidt dat enkele boek direct in plaats van een trefwoordzoekopdracht uit te voeren.

NVDA kondigt aan hoeveel luisterboeken in totaal zijn gevonden. Door een resultaat te selecteren worden de details getoond — auteur, verteller, uitgever, formaat en het aantal delen — in het detailsvak eronder.

**Voorbeeld bekijken:** Selecteer een resultaat en druk op `Space`, of open het contextmenu (Toepassingentoets / `Shift+F10`, of rechtermuisknop) en kies **Voorbeeld**, om het vanaf het eerste deel af te spelen zonder het aan je bibliotheek toe te voegen. Terwijl een boek wordt bekeken, toont hetzelfde contextmenu **Stop voorbeeld** in plaats daarvan — kies het, of druk nogmaals op `Space`, om te stoppen. Een boek bekijken slaat je luisterpositie niet op, aangezien die alleen wordt bijgehouden voor boeken die al in je bibliotheek staan.

**Toevoegen aan je bibliotheek:** Selecteer een resultaat en druk op `Enter`, of gebruik het contextmenu en kies **Toevoegen aan bibliotheek**, om het toe te voegen. freeAudio vertelt je of het boek er al staat.

### Je bibliotheek

Boeken die je hebt toegevoegd verschijnen in de lijst **Bibliotheek**, met titel, auteur en formaat. Door er een te selecteren worden de details eronder getoond.

- Druk op `Enter` of `Space` om het geselecteerde boek af te spelen. Als er niets is geladen, start `Space` het; als er al iets speelt, pauzeert `Space` het in plaats daarvan, overeenkomstig de rest van de speler.
- Gebruik `F3` / `F4` op het tabblad Luisterboeken om naar het vorige / volgende **boek** in je bibliotheek te gaan en het af te spelen. `Ctrl+←` / `Ctrl+→` doen hetzelfde terwijl de bibliotheeklijst is gefocust.
- Gebruik `Shift+F3` / `Shift+F4` om in plaats daarvan tussen **delen** van het momenteel spelende boek te wisselen — het omgekeerde van het tabblad Podcasts, waar F3/F4 tussen afleveringen wisselen en Shift+F3/F4 tussen feeds. Dit komt omdat een boek één bibliotheekitem is, zelfs als het meerdere delen heeft, dus de fijnmazigere "deel"-navigatie hier op de Shift-gemodificeerde toetsen zit.
- Met de stationsverkenner gesloten doen `Ctrl+Win+F3` / `Ctrl+Win+F4` (vorig / volgend boek) en `Ctrl+Win+Shift+F3` / `Ctrl+Win+Shift+F4` (vorig / volgend deel) hetzelfde — zie [Items overslaan met gesloten stationsverkenner](#items-overslaan-met-gesloten-stationsverkenner).

**Contextmenu voor bibliotheekitems:** Klik met de rechtermuisknop op een boek, of selecteer het en druk op de Toepassingentoets / `Shift+F10`, om een menu te openen met:

- **Media afspelen** — begin met afspelen, hetzelfde als `Enter`.
- **Boek downloaden** — download elk deel van het boek; zie [Luisterboeken downloaden](#luisterboeken-downloaden) hieronder.
- **Kopieer de URL** — kopieer de cataloguspagina-URL van het boek naar het klembord (de GETEM-cataloguspagina voor een GETEM-boek, of de archive.org detailpagina voor een LibriVox- of Project Gutenberg-boek).
- **Audioprofiel voor dit boek opslaan** / **Audioprofiel wissen** — zie [Luisterboek-audioprofiel](#luisterboek-audioprofiel) hieronder.
- **Verwijder uit bibliotheek** — verwijder het boek uit je bibliotheek.

Je kunt ook meerdere boeken tegelijk markeren en ze allemaal samen verwijderen — zie [Meerdere items markeren en verwijderen](#meerdere-items-markeren-en-verwijderen) onder Favorieten.

### Afspelen en hervatten

Een werk met meerdere delen wordt in de speler als één item behandeld, niet als één rij per deel — op dezelfde manier waarop een podcastaflevering één item is ongeacht hoe deze wordt geleverd. freeAudio onthoudt welk deel je het laatst hebt beluisterd en hervat daar automatisch de volgende keer dat je dat boek afspeelt, zelfs na een herstart van NVDA.

Wanneer een deel eindigt, start freeAudio automatisch het volgende deel van hetzelfde boek — je hoeft het niet handmatig te selecteren. Dit gebeurt zelfs als het Stationsverkenner-venster op dat moment gesloten is; het "nu afspelen"-deel dat in de Bibliotheeklijst wordt getoond, wordt automatisch opnieuw gesynchroniseerd de volgende keer dat het venster wordt geopend.

Het afspelen streamt via een kleine lokale relay in plaats van eerst het hele deel te downloaden, zodat het luisteren begint zodra de eerste bytes binnenkomen — hetzelfde onmiddellijke-startgedrag dat podcasts gebruiken. Alle gebruikelijke spelerbediening (pauze, volume, tijdverschuiving, afspeelsnelheid, transponeren, uitvoerapparaat, enz.) werkt op een luisterboek precies zoals op een station of podcastaflevering.

Net als bij podcasts speelt het hervatten van een boek vanaf de opgeslagen positie een kort cassette-laden-geluidseffect af terwijl freeAudio naar je opgeslagen plek spoelt — zie de **Geluidseffect bij hervatten**-opmerking in [Afspeeldetails van podcasts](#afspeeldetails-van-podcasts).

### Luisterboek-audioprofiel

Klik met de rechtermuisknop op een boek in je Bibliotheeklijst en kies **Audioprofiel voor dit boek opslaan** om het huidige volume, de effecten, de EQ-gains en/of de afspeelsnelheid op te slaan als een profiel dat aan dat boek is gekoppeld. Telkens wanneer het boek (of een van zijn delen) speelt, worden de opgeslagen instellingen automatisch toegepast, waarbij de globale standaardwaarden worden overschreven. Dit werkt precies hetzelfde als [Podcast-audioprofiel](#podcast-audioprofiel) hierboven, inclusief dezelfde set opslagopties (volume, effecten en/of afspeelsnelheid, in elke combinatie) en hetzelfde gedeeltelijke-updategedrag.

**Audioprofiel wissen** verwijdert het opgeslagen profiel van het boek; het is alleen ingeschakeld wanneer het boek momenteel een opgeslagen profiel heeft.

### Luisterboeken downloaden

Selecteer een boek in je bibliotheek en kies **Boek downloaden** in het contextmenu om elk deel op te slaan in een eigen map (vernoemd naar het boek) in je opnamemap (`Documents\freeAudio Recordings\` standaard). Bestanden worden genummerd zodat de delen altijd terug sorteren in luistervolgorde, ongeacht hoe GETEM ze zelf noemt. NVDA kondigt aan hoeveel delen zijn opgeslagen wanneer de download is voltooid; als een deel mislukt, wordt de laatste fout samen met het aantal gerapporteerd.

### Directe sneltoetsen voor luisterboeken

Elk boek in je Luisterboekenbibliotheek — of het nu van GETEM, LibriVox of Project Gutenberg komt — wordt geregistreerd als een apart script in het dialoogvenster Invoerhandelingen van NVDA, onder de categorie **freeAudio Luisterboeken**, precies zoals [Directe sneltoetsen voor favoriete stations](#directe-sneltoetsen-voor-favoriete-stations) en [Directe sneltoetsen voor jukeboxitems](#directe-sneltoetsen-voor-jukeboxitems). Je kunt elke sneltoets aan elk boek toewijzen en deze vanaf elke locatie indrukken — je hoeft de stationsverkenner niet eerst te openen. Standaard zijn er geen sneltoetsen toegewezen.

Een sneltoets toewijzen:

1. Open NVDA-menu → Opties → Invoerhandelingen.
2. Vouw de categorie **freeAudio Luisterboeken** uit.
3. Zoek het boek op titel (elk item heet "*titel* afspeelsneltoets"), selecteer het en druk op **Toevoegen**.
4. Druk de gewenste toetscombinatie in en bevestig.

De sneltoets start het boek onmiddellijk en hervat bij het deel dat je het laatst hebt beluisterd; de positie binnen dat deel wordt op dezelfde manier hersteld als wanneer je het boek vanuit de bibliotheeklijst afspeelt. Als de lijst met delen van het boek nog niet is opgehaald, zegt NVDA "Laden: *titel*" en begint het afspelen zodra deze gereed is (een GETEM-boek vereist je opgeslagen aanmelding — zie [Aanmelden](#aanmelden)). Wanneer een deel eindigt, start het volgende automatisch, met of zonder de stationsverkenner open.

Wanneer je een boek aan de bibliotheek toevoegt of er een verwijdert, wordt de categorie **freeAudio Luisterboeken** onmiddellijk bijgewerkt — het dialoogvenster Invoerhandelingen hoeft niet opnieuw te worden geopend om de wijziging te zien wanneer je het de volgende keer opent. Als een boek wordt verwijderd, verdwijnt het item en wordt elke eraan toegewezen sneltoets automatisch gewist door NVDA; mocht een verouderde sneltoets toch afgaan, dan zegt NVDA dat het luisterboek niet langer in de bibliotheek staat.

### Opslag van luisterboekgegevens

Elke bron houdt zijn eigen bibliotheekbestand bij, ook al worden ze samengevoegd weergegeven op het tabblad Luisterboeken. Je GETEM-bibliotheek (toegevoegde boeken en hun luistervoortgang) wordt opgeslagen in `freeAudio_getem_library.json`, je LibriVox-bibliotheek wordt apart opgeslagen in `freeAudio_librivox_library.json`, en je Project Gutenberg-bibliotheek wordt apart opgeslagen in `freeAudio_gutenberg_library.json` — alle drie in de NVDA-gebruikersconfiguratiemap. Je versleutelde GETEM-inloggegevens worden apart opgeslagen in `freeAudio_getem_credentials.bin` op dezelfde locatie, en kunnen alleen worden ontsleuteld door dezelfde Windows-gebruikersaccount die ze heeft opgeslagen. LibriVox en Project Gutenberg hebben geen inloggegevensbestand, aangezien geen van beide een account vereist.

## Lokale jukebox

Het tabblad **Jukebox** van freeAudio geeft je twee manieren om audiobestanden af te spelen die al op je computer staan: zoek elke aangesloten schijf op bestandsnaam, of bouw een blijvende persoonlijke bibliotheek van bestanden en mappen. Wat je hier ook afspeelt, krijgt dezelfde behandeling als een podcast of luisterboek — automatisch hervatten, getrapt terug-/vooruitspoelen, afspeelsnelheid, toonhoogtetranspositie en audioprofielen per item werken allemaal precies hetzelfde.

### Toegang tot het tabblad Jukebox

Open de stationsverkenner met `Ctrl+Win+R` en schakel naar het tabblad **Jukebox** met `Ctrl+Tab` of `Alt+8`, of open het rechtstreeks vanaf elke locatie met de globale sneltoets `Ctrl+Win+U`. Het tabblad is georganiseerd in drie hoofdgebieden:

1. **Zoek op apparaten** — een tekstveld dat elke lokaal aangesloten, gereed zijnde schijf doorzoekt op audiobestanden waarvan de bestandsnaam de getypte tekst bevat. Druk op `Enter` om de zoekopdracht te starten.
2. **Zoekresultaten** — een lijst die verschijnt zodra een zoekopdracht is uitgevoerd, met de overeenkomende bestanden. Tot dan verborgen, zodat het tabblad overzichtelijk blijft wanneer er niets te zoeken is.
3. **Jukebox en Nummers** — de blijvende lijst met items die je hebt toegevoegd, gevolgd door de lijst met nummers in welk item dan ook dat is geselecteerd (voor een bestandsitem gewoon dat ene bestand; voor een mapitem elk audiobestand dat erin is gevonden). Een **Bladwijzers**-lijst volgt de Nummers-lijst en toont de bladwijzers van het geselecteerde nummer — zie [Bladwijzers](#bladwijzers).

De knoppen **Bestand toevoegen…**, **Map toevoegen…**, **Verwijderen**, **Jukebox exporteren…** en **Jukebox importeren…** staan onderaan het tabblad.

### Bestanden op apparaten zoeken

Typ een willekeurig deel van een bestandsnaam in het veld **Zoek op apparaten** en druk op `Enter`. freeAudio doorloopt elke lokaal aangesloten schijf — vaste schijven, USB-schijven en geheugenkaarten — op zoek naar audiobestanden (`.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a`, `.m4b`, `.aac`, `.wma`, `.opus` en nog enkele meer) waarvan de bestandsnaam de zoektekst bevat. De zoekopdracht draait op de achtergrond, zodat NVDA responsief blijft. Netwerkschijven worden standaard overgeslagen, omdat het doorzoeken van een netwerkshare een zoekopdracht van één seconde kan veranderen in een die minuten duurt, of kan vastlopen als de share niet bereikbaar is. Om ze mee te nemen, schakel je **Neem netwerkstations mee in de zoekopdracht in de jukebox** in de instellingen in.

- **Space** op een zoekresultaat bekijkt het — start het afspelen via de normale speler. Druk nogmaals op **Space** op hetzelfde bestand om het voorbeeld te stoppen.
- **Enter** op een zoekresultaat voegt het toe aan je jukebox.
- Het contextmenu (Toepassingentoets / `Shift+F10`, of rechtermuisknop) biedt dezelfde twee acties: **Voorbeeld** / **Stop voorbeeld** en **Toevoegen aan jukebox**.
- Het starten van een nieuwe zoekopdracht annuleert een nog lopende zoekopdracht, zodat een langzame zoekopdracht op een grote schijf nooit een nieuwe vertraagt.

### Je jukebox opbouwen

De Jukebox-lijst is je blijvende persoonlijke bibliotheek. Er kunnen twee soorten items worden toegevoegd:

- **Bestand toevoegen…** — opent een bestandskiezer waarmee je een of meer afzonderlijke audiobestanden kunt toevoegen. Alle gekozen bestanden worden in één keer toegevoegd.
- **Map toevoegen…** — opent een mapkiezer waarmee je meerdere mappen tegelijk kunt selecteren. Elk audiobestand in elke gekozen map, inclusief in de submappen, wordt behandeld als een van de **nummers** van die map. Elke map wordt als een eigen enkel item in je Jukebox-lijst toegevoegd; de bestanden erin worden in de Nummers-lijst getoond wanneer de map is geselecteerd. NVDA kondigt aan hoeveel mappen zijn toegevoegd wanneer de kiezer sluit.
- **Verwijderen** — verwijdert het momenteel geselecteerde item uit je Jukebox. Het verwijderen van een mapitem verwijdert geen enkel bestand van schijf of apparaat; het vergeet de map gewoon. Je kunt ook meerdere items tegelijk markeren en ze allemaal samen verwijderen — zie [Meerdere items markeren en verwijderen](#meerdere-items-markeren-en-verwijderen) onder Favorieten.

Je Jukebox-lijst wordt automatisch opgeslagen, zodat deze NVDA-herstarts overleeft. Mapinhoud wordt op aanvraag gescand en gecached, zodat het toevoegen van een map direct gebeurt, zelfs voor zeer grote collecties — de volledige scan gebeurt de eerste keer dat je die map selecteert. Als je bestanden aan een map toevoegt buiten freeAudio, gebruik dan het item **Map opnieuw scannen** in het contextmenu van de map om ze op te pikken.

### Items toevoegen vanuit Windows Verkenner

Nog twee commando's, alleen beschikbaar terwijl een bestand of map is gefocust in de bestandenlijst van Windows Verkenner (de lijst Details/Pictogrammen — niet de adresbalk, de mappenstructuur, het lint of het zoekvak), laten je de dialoogvensters Bestand toevoegen…/Map toevoegen… hierboven volledig overslaan:

- **Speel het bestand met focus af met freeAudio** — speelt het gemarkeerde audiobestand rechtstreeks af, zonder dat het al in je Jukebox-lijst hoeft te staan. Werkt alleen op bestanden; gebruik op een map vertelt je de map in plaats daarvan aan de jukebox toe te voegen.
- **Voeg het item met focus toe aan de freeAudio-jukebox** — voegt het gemarkeerde bestand of de gemarkeerde map toe aan je Jukebox-lijst, precies alsof je **Bestand toevoegen…** of **Map toevoegen…** hierboven had gebruikt.

Geen van beide commando's heeft een standaardtoets toegewezen. Wijs er een toe via NVDA-menu → Opties → Invoerhandelingen → freeAudio **terwijl je gefocust bent in een Verkenner-venster**.

### Afspelen vanuit de jukebox

- **Enter** op een Jukebox-item speelt het direct af: voor een bestandsitem het bestand zelf; voor een mapitem de map in volgorde — beginnend bij het nummer dat is gemarkeerd in de Nummers-lijst of, als er geen is gemarkeerd, vanaf waar de map de vorige keer was gebleven (het eerste nummer als er nooit naar is geluisterd). Wanneer een nummer eindigt, start het volgende nummer in de map automatisch.
- **Space** op een Jukebox-item pauzeert het afspelen als er iets speelt; anders speelt het het gefocuste item af.
- **Enter** of **Space** op de Nummers-lijst speelt het gefocuste nummer af. **Space** pauzeert eerst als er al iets speelt. Een nummer dat op deze manier is gestart, speelt op zichzelf en gaat niet verder naar het volgende nummer wanneer het eindigt; gebruik `F3` / `F4` of speel het mapitem zelf af voor continue weergave.
- **F3 / F4** op het tabblad Jukebox wisselen tussen nummers binnen het momenteel geselecteerde item en spelen direct af. In een mapitem wordt het nummer afgespeeld als onderdeel van de map, zodat de volgende nummers nog steeds automatisch starten wanneer het eindigt.
- **Shift+F3 / Shift+F4** wisselen tussen items in de Jukebox-lijst (bestanden en mappen), waarmee wordt weerspiegeld hoe deze toetsen tussen feeds op het tabblad Podcasts wisselen.
- **Ctrl+← / Ctrl+→** terwijl de items- of nummerlijst is gefocust doen hetzelfde als F3/F4 op de nummerlijst — vorig / volgend nummer, met automatische voortzetting in een map.
- Met de stationsverkenner gesloten doen `Ctrl+Win+F3` / `Ctrl+Win+F4` (vorig / volgend nummer) en `Ctrl+Win+Shift+F3` / `Ctrl+Win+Shift+F4` (vorig / volgend item) hetzelfde — zie [Items overslaan met gesloten stationsverkenner](#items-overslaan-met-gesloten-stationsverkenner).

### Afspeeldetails van de jukebox

Elk nummer dat vanuit de Jukebox wordt afgespeeld, krijgt de volledige lokale-media-behandeling:

- **Hervatten:** freeAudio onthoudt je positie in elk nummer, slaat deze op bij pauzeren en periodiek tijdens het afspelen, en hervat vanaf dat punt wanneer je het opnieuw afspeelt — zelfs na een NVDA-herstart.
- **Automatisch volgend nummer:** wanneer een nummer dat als onderdeel van een map is afgespeeld eindigt, start het volgende nummer in die map vanzelf, of de stationsverkenner nu open of gesloten is, en blijft dit doen nadat je nummers hebt overgeslagen met `F3` / `F4` of `Ctrl+Win+F3` / `Ctrl+Win+F4`. Wanneer het laatste nummer is afgelopen, wordt de opgeslagen positie van de map gewist zodat deze de volgende keer weer vanaf het eerste nummer begint. Handmatig op "volgende" drukken bij het laatste nummer wist deze niet.
- **Getrapt zoeken:** `Ctrl+Win+J` / `Ctrl+Win+K` zoeken binnen het nummer met dezelfde druk/ingedrukt-houden-schaal als podcasts en luisterboeken — ingedrukt houden voor 5 seconden per herhaling, één druk voor 12 seconden, twee drukken voor 1 minuut, drie of meer drukken voor 5 minuten. `Ctrl+Win+Alt+J` / `Ctrl+Win+Alt+K` zoeken precies 1 seconde — zie [Nauwkeurig zoeken (1 seconde)](#nauwkeurig-zoeken-1-seconde).
- **Afspeelsnelheid:** `Ctrl+Win+Shift+J` / `Ctrl+Win+Shift+K` passen de snelheid aan in stappen van 0,1x van 0,5x tot 2,0x, met behoud van toonhoogte.
- **Transponeren:** `Shift+Win+J` / `Shift+Win+K` verschuiven de toonhoogte zonder de snelheid te wijzigen — zie [Transponeren (toonhoogteverschuiving)](#transponeren-toonhoogteverschuiving).
- **Audioprofiel:** Het volume, de effecten, de EQ en de snelheid van een nummer kunnen globaal worden opgeslagen door een nummer af te spelen terwijl de juiste instellingen zijn ingesteld — de Jukebox biedt momenteel geen profielmenu per nummer, dus de huidige globale instellingen zijn van toepassing.

> **Opmerking:** De tijdverschuivingsbuffer (gebruikt voor het terugspoelen van live radio) wordt opzettelijk **niet** gestart voor Jukebox-nummers — het zijn al doorzoekbare lokale bestanden, dus een achtergrondopname heeft geen doel en zou alleen schijfruimte verbruiken. Terugspoelen en vooruitspoelen werken nog steeds omdat ze direct op het afgespeelde bestand inwerken.

### Jukeboxitems hernoemen

Kies **Hernoemen…** in het contextmenu van een Jukebox-item (Toepassingentoets / `Shift+F10`) om het een aangepaste weergavenaam te geven. De aangepaste naam vervangt de bestands- of mapnaam in de Jukebox-lijst en wordt in de `#EXTINF`-regel geschreven wanneer het item naar M3U wordt geëxporteerd (zie [De jukeboxbibliotheek exporteren en importeren](#de-jukeboxbibliotheek-exporteren-en-importeren) hieronder). Laat het veld leeg om de aangepaste naam te wissen en terug te vallen op de originele bestands- of mapnaam.

### De jukebox in groepen organiseren

Jukebox-items kunnen bij een groep horen, die wordt getoond als een "— Groep"-suffix achter de itemnaam in de lijst, precies zoals [Favorieten in groepen organiseren](#favorieten-in-groepen-organiseren):

- Markeer een of meer items met `.` (zie [Meerdere items markeren en verwijderen](#meerdere-items-markeren-en-verwijderen) hierboven), kies vervolgens **Toewijzen aan Groep…** in het contextmenu en typ een groepsnaam. Laat het veld leeg om de gemarkeerde items uit hun groep te verwijderen. Als er niets is gemarkeerd, is het commando van toepassing op het momenteel geselecteerde item.
- Het Filter-veld boven de Jukebox-lijst komt ook overeen met groepsnamen, op dezelfde manier als bij Favorieten.

### De jukebox opnieuw rangschikken

Met een item geselecteerd in de Jukebox-lijst, druk je op `komma` om de verplaats-modus te activeren — je hoort een pieptoon. Navigeer naar de doelpositie met de pijltoetsen en druk nogmaals op `komma`. Het item wordt op de gekozen positie geplaatst en de nieuwe volgorde wordt direct opgeslagen. Nogmaals op `komma` drukken op dezelfde positie annuleert de verplaatsing.

### De jukeboxbibliotheek exporteren en importeren

Het tabblad Jukebox bevat twee knoppen voor het maken van een back-up en het herstellen van je bibliotheek, onderaan het tabblad:

**Jukebox exporteren…** — slaat je volledige Jukebox-lijst op naar een bestand. Een dialoogvenster laat je kiezen tussen twee formaten:

- **JSON** (`.json`) — een volledige back-up die het pad, de aangepaste naam, de groep en het opgeslagen audioprofiel van elk item behoudt. Aanbevolen voor het later herstellen van je bibliotheek of het verplaatsen naar een andere computer.
- **M3U-afspeellijst** (`.m3u`) — een lichter formaat dat compatibel is met de meeste mediaspelers, met het pad van elk item en de aangepaste naam (indien aanwezig) in een voorafgaande `#EXTINF`-regel. Groepen en audioprofielen worden niet in M3U opgenomen, dus herstellen vanuit M3U verliest dat detail.

**Jukebox importeren…** — laadt items uit een eerder geëxporteerd JSON- of M3U-bestand. Na het selecteren van het bestand wordt gevraagd hoe de items moeten worden toegevoegd:

- **Ja (Samenvoegen)** — voegt de geïmporteerde items toe aan je bestaande bibliotheek zonder huidige items te verwijderen. Items waarvan het pad overeenkomt met een item dat al in je bibliotheek staat, worden niet twee keer toegevoegd.
- **Nee (Vervangen)** — wist je huidige Jukebox-lijst volledig en vervangt deze door de inhoud van het geïmporteerde bestand.
- **Annuleren** — keert terug naar de stationsverkenner zonder wijzigingen aan te brengen.

### Directe sneltoetsen voor jukeboxitems

Elk item in je Jukebox-lijst wordt geregistreerd als een apart script in het dialoogvenster Invoerhandelingen van NVDA, onder de categorie **freeAudio Jukebox**, precies zoals [Directe sneltoetsen voor favoriete stations](#directe-sneltoetsen-voor-favoriete-stations). Je kunt elke sneltoets aan elk item toewijzen en deze vanaf elke locatie indrukken — je hoeft de stationsverkenner niet eerst te openen.

Een sneltoets toewijzen:

1. Open NVDA-menu → Opties → Invoerhandelingen.
2. Vouw de categorie **freeAudio Jukebox** uit.
3. Zoek het item op naam, selecteer het en druk op **Toevoegen**.
4. Druk de gewenste toetscombinatie in en bevestig.

De sneltoets speelt het item onmiddellijk af — voor een bestandsitem het bestand zelf; voor een mapitem het nummer waar de map de vorige keer was gebleven (het eerste nummer als er nooit naar is geluisterd), waarna de volgende nummers automatisch spelen, zelfs met de stationsverkenner gesloten. Als het item later uit je Jukebox wordt verwijderd, verdwijnt het item uit de categorie en wordt elke eraan toegewezen sneltoets automatisch gewist door NVDA. Wanneer een nieuw item wordt toegevoegd, verschijnt het direct in de categorie — het dialoogvenster Invoerhandelingen hoeft niet opnieuw te worden geopend.

## Bladwijzers

Met bladwijzers kun je een plek markeren in een **deel van een luisterboek**, een **podcastaflevering** of een **jukeboxnummer** en er later naar terugkeren. Ze zijn niet beschikbaar voor live radiostations, die geen vaste posities hebben om naar terug te keren.

### Een bladwijzer toevoegen

- Druk op **`Ctrl+Win+F12`** vanaf elke locatie in Windows, of **`F12`** terwijl de stationsverkenner actief is, om een bladwijzer toe te voegen op de huidige afspeelpositie.
- NVDA kondigt de naam en positie van de bladwijzer aan, bijvoorbeeld "Bladwijzer toegevoegd: Bladwijzer 2, 12:30".
- Als er niets speelt, of een live radiostation speelt, vertelt freeAudio je dit en wordt er geen bladwijzer toegevoegd.

De standaardnaam van een bladwijzer is zijn **rangtelwoordpositie** onder de bladwijzers van het item, vroegste eerst: "Bladwijzer 1", "Bladwijzer 2", enzovoort. Omdat het nummer de positie volgt in het item, hernummert het toevoegen van een eerdere bladwijzer de latere die nog een standaardnaam hebben. Bladwijzers die je hebt hernoemd, behouden hun eigen naam.

### De bladwijzerlijst

Elk van de tabbladen Podcasts, Luisterboeken en Jukebox heeft een **Bladwijzers**-lijst direct naast het item waartoe deze behoort:

- **Podcasts** — direct onder de Afleveringenlijst, met de bladwijzers van de geselecteerde aflevering.
- **Luisterboeken** — direct onder de Bibliotheeklijst, met de bladwijzers van elk deel van het geselecteerde boek. Wanneer een boek meerdere delen heeft, begint elke rij met de titel van het deel.
- **Jukebox** — direct onder de Nummers-lijst, met de bladwijzers van het geselecteerde nummer.

Elke rij toont de naam en positie van de bladwijzer. Een **[tekst]**- of **[spraaknotitie]**-markering wordt toegevoegd wanneer de bladwijzer een tekstnotitie of een spraaknotitie heeft, en **(gemarkeerd)** wanneer je deze met `.` hebt gemarkeerd. De lijst volgt de selectie erboven en wordt ook vernieuwd wanneer je een bladwijzer toevoegt met `Ctrl+Win+F12` terwijl het venster open is.

Terwijl een bladwijzerlijst is gefocust, werken de afspeeltoetsen van het tabblad erboven ook daar: `←` / `→` zoeken, `Shift+←` / `Shift+→` transponeren, `Page Up` / `Page Down` wijzigen de afspeelsnelheid, `Ctrl+←` / `Ctrl+→` schakelen naar de vorige of volgende aflevering, boek of nummer, en `Alt+←` / `Alt+→` zoeken met 1 seconde.

| Toets | Actie |
|---|---|
| `.` | Markeert of heft de markering op van de gefocuste bladwijzer. Zie [Meerdere items markeren en verwijderen](#meerdere-items-markeren-en-verwijderen). |
| `Enter` | Speelt af vanaf de gefocuste bladwijzer. |
| `Space` | Pauzeert als er iets speelt; anders speelt het af vanaf de gefocuste bladwijzer. |
| `Delete` | Verwijdert elke gemarkeerde bladwijzer, of de gefocuste als er geen is gemarkeerd. Er verschijnt eerst een bevestigingsdialoogvenster. |
| Toepassingentoets / `Shift+F10` | Opent het contextmenu van de bladwijzer. |

### Contextmenu van bladwijzer

- **Afspelen vanaf bladwijzer** — als het item al is geladen, springt het afspelen naar de bladwijzer; anders begint het item vanaf die positie te spelen.
- **Hernoemen…** — geeft de bladwijzer een aangepaste naam. Laat het veld leeg om terug te keren naar de standaardnaam.
- **Geselecteerde verwijderen** — verwijdert de gemarkeerde bladwijzers, of de gefocuste als er geen is gemarkeerd.
- **Tekst toevoegen of bewerken…** — opent een meerregelig veld voor een tekstnotitie. Laat het leeg om de tekst te verwijderen.
- **Spraaknotitie toevoegen…** — opent een dialoogvenster dat onmiddellijk na verschijnen begint met opnemen van de standaardmicrofoon. Druk op **Stoppen en opslaan** om de opname aan de bladwijzer te koppelen, of op **Annuleren** om deze te verwerpen. Het toevoegen van een nieuwe spraaknotitie vervangt de vorige.
- **Notities wissen** — verwijdert zowel de tekstnotitie als de spraaknotitie van de gefocuste bladwijzer. Alleen ingeschakeld wanneer de bladwijzer een notitie heeft.
- **Herhalen tussen gemarkeerde bladwijzers** — zie hieronder. Ingeschakeld wanneer ten minste twee bladwijzers zijn gemarkeerd.
- **Herhalen stoppen** — schakelt de herhalingsmodus uit. Ingeschakeld terwijl een herhaling actief is.

### Wat er gebeurt wanneer het afspelen een bladwijzer bereikt

Tijdens normaal afspelen, wanneer de positie een bladwijzer bereikt, speelt freeAudio **twee korte piepjes**. Als de bladwijzer geen notitie heeft, gaat het afspelen gewoon door.

Als de bladwijzer een tekstnotitie en/of een spraaknotitie heeft, wordt het afspelen **gepauzeerd**, wordt de tekst uitgesproken door de huidige synthesizer van NVDA en wordt de spraaknotitie afgespeeld, waarna het afspelen **hervat waar het was gebleven**. Als je het afspelen stopt of iets anders start terwijl de notitie wordt afgespeeld, wordt het afspelen niet hervat.

Bladwijzers worden gedetecteerd tijdens normaal afspelen. Zoeken of springen voorbij een bladwijzer activeert deze niet.

### De sectie tussen bladwijzers herhalen

Markeer twee of meer bladwijzers van **hetzelfde item** met `.`, kies vervolgens **Herhalen tussen gemarkeerde bladwijzers**. Het afspelen springt naar de vroegste gemarkeerde bladwijzer en herhaalt tussen de vroegste en de laatste gemarkeerde bladwijzer, en NVDA kondigt de twee posities aan. Dit is handig voor het doornemen van een moeilijk te volgen passage, een taal-leerzinnetje of een muziekstuk dat je aan het oefenen bent. Kies **Herhalen stoppen** om terug te keren naar normaal afspelen. De herhaling wordt niet tussen sessies opgeslagen, en als een ander item begint te spelen, wordt het herhalingsbereik genegeerd en na ongeveer 20 seconden verwijderd.

### Opslag van bladwijzergegevens

Bladwijzers worden opgeslagen in `freeAudio_bookmarks.json` in de NVDA-gebruikersconfiguratiemap, en spraaknotities worden opgeslagen als `.wav`-bestanden in de map `freeAudio_bookmark_audio` ernaast. Beide kunnen worden geback-upt of naar een andere computer worden overgebracht. Het verwijderen van een bladwijzer verwijdert ook het bijbehorende spraaknotitiebestand. Alle bladwijzers en spraaknotities kunnen in één keer worden verwijderd met het item **Bladwijzers** van het opruimdialoogvenster — zie [Opruimen: instellingen terugzetten en opgeslagen gegevens verwijderen](#opruimen-instellingen-terugzetten-en-opgeslagen-gegevens-verwijderen).

Elke bladwijzer hoort bij de eigen hervat-sleutel van het item — de URL van de aflevering, de stabiele catalogus-URL van het luisterboekdeel, of het bestandspad van het jukeboxnummer. Een jukeboxbestand dat buiten freeAudio wordt verplaatst of hernoemd, wordt daarom als een ander item behandeld en toont zijn oude bladwijzers niet.

## Transponeren (toonhoogteverschuiving)

Transponeren verschuift de **toonhoogte** van wat er speelt omhoog of omlaag zonder de **snelheid** te wijzigen — het tegenovergestelde van het "chipmunk-effect" dat je zou krijgen door een nummer simpelweg sneller af te spelen. Het is handig voor het afstemmen op het natuurlijke bereik van een bepaalde verteller, het transponeren van muziek naar een vriendelijkere toonaard, of gewoon het aanpassen van een opname zodat deze comfortabeler in je oren klinkt.

Transponeren is beschikbaar voor **podcasts**, **luisterboeken** en **jukeboxnummers** — dezelfde "lokale, doorzoekbare, tempo-geschikte" media waarop de sneltoetsen voor afspeelsnelheid al van toepassing zijn. Het is niet beschikbaar voor live radiostations, die geen vaste toonhoogte hebben om te verschuiven.

- **`Shift+Win+K`** — Verhoogt de toonhoogte met één stap.
- **`Shift+Win+J`** — Verlaagt de toonhoogte met één stap.

Elke stap is **een achtste van een hele toon** — dat wil zeggen **0,25 halve toon** (een hele toon is 2 halve tonen, dus 8 stappen maken een hele toon, en 48 stappen maken een octaaf). Het bereik is **−12,00 tot +12,00 halve tonen**, dat wil zeggen één volledig octaaf omhoog of omlaag. NVDA kondigt de nieuwe waarde na elke stap aan, bijvoorbeeld "**+1,25 halve tonen**"; terugkeren naar 0,0 kondigt "**Normale toonhoogte**" aan.

Transponeren wordt onthouden tussen nummers, op dezelfde manier als afspeelsnelheid: het één keer instellen terwijl een nummer speelt, betekent dat het volgende tempo-geschikte nummer dat je afspeelt met dezelfde verschuiving begint, tenzij het eigen opgeslagen audioprofiel van dat nummer dit overschrijft. Het afspelen van een nummer zonder opgeslagen transponatiewaarde zet de verschuiving terug naar 0,0 (Normale toonhoogte), net zoals dezelfde regel al geldt voor snelheid.

## Gelikete nummers

Wanneer de optie **Gelikete nummers opslaan in een tekstbestand** is ingeschakeld, wordt trackinformatie die naar het klembord is gekopieerd door drie keer op `Ctrl+Win+I` te drukken, ook regel voor regel toegevoegd aan `Documents\freeAudio Recordings\likedSongs.txt`.

Op stations die ICY-metadata uitzenden, worden de tracktitel en artiest direct opgeslagen. Op stations zonder ICY-metadata wordt het Shazam-herkenningsresultaat in hetzelfde bestand opgeslagen — beide bronnen delen dezelfde lijst. Het bestand wordt automatisch aangemaakt als het niet bestaat; elk item wordt aan het einde van het bestand toegevoegd en eerdere items worden nooit verwijderd.

## Tabblad Gelikete nummers

Het tabblad **Gelikete nummers** in de Stationsverkenner toont alle nummers die zijn opgeslagen in `likedSongs.txt`. De lijst wordt automatisch opnieuw geladen vanuit het bestand telkens wanneer het tabblad wordt geopend. Klik met de rechtermuisknop op een nummer, of selecteer het en druk op de Toepassingentoets / `Shift+F10`, om een contextmenu te openen met dezelfde acties die hieronder worden beschreven.

Een **Filter**-veld boven de lijst laat je de weergegeven nummers in realtime beperken. Typ een willekeurig deel van een songtitel of artiestnaam en de lijst wordt bij elke toetsaanslag direct bijgewerkt. NVDA kondigt na elke wijziging het aantal overeenkomende resultaten aan. Druk op de pijl-omlaag vanuit het filterveld om de focus direct in de lijst te verplaatsen.

Het selecteren van een nummer uit de lijst maakt de volgende acties mogelijk:

- **Afspelen op Spotify:** Probeert de Spotify-desktop-app direct te openen. Als de app niet is geïnstalleerd, valt deze terug op de Spotify-website en begint automatisch met het afspelen van het eerste resultaat.
- **Afspelen op YouTube (`Alt+O`):** Doorzoekt YouTube op het geselecteerde nummer en opent de resultaten in de standaardbrowser.
- **Songtekst weergeven:** Haalt de songtekst voor het geselecteerde nummer op en toont deze. Songteksten worden opgehaald van [lrclib.net](https://lrclib.net) (gratis, geen account vereist). Een kort "Songtekst ophalen…" bericht wordt aangekondigd terwijl de zoekopdracht op de achtergrond loopt. Als songteksten worden gevonden, openen ze in een alleen-lezen dialoogvenster waar je ze met NVDA kunt lezen en naar het klembord kunt kopiëren. Als er geen songteksten worden gevonden, kondigt NVDA dit aan. De knop is tijdelijk uitgeschakeld terwijl een ophaalactie bezig is om dubbele verzoeken te voorkomen.
- **Verwijderen (`Alt+M`):** Verwijdert het geselecteerde nummer uit `likedSongs.txt` en werkt de lijst bij. De `Delete`-toets activeert ook deze knop wanneer de lijst gefocust is. Je kunt ook meerdere nummers tegelijk markeren en ze allemaal samen verwijderen — zie [Meerdere items markeren en verwijderen](#meerdere-items-markeren-en-verwijderen) onder Favorieten.
- **Vernieuwen (`Alt+E`):** Laadt de lijst opnieuw vanuit het bestand.

De knoppen Spotify, YouTube, Songtekst weergeven en Verwijderen zijn alleen ingeschakeld wanneer een echt nummer is geselecteerd in de lijst.

### Songtekst-service

freeAudio gebruikt [lrclib.net](https://lrclib.net) om songteksten op te halen — een gratis, open database die geen API-sleutel of account vereist. Het opzoekproces ontleedt de trackstring die is opgeslagen in `likedSongs.txt` en probeert achtereenvolgens ruimere zoekopdrachten totdat songteksten worden gevonden:

1. Exacte overeenkomst met de volledige artiestnaam en opgeschoonde titel (ruissuffixen zoals "Remastered", "Live" of jaartags worden verwijderd vóór het zoeken).
2. Exacte overeenkomst met de volledige artiestnaam en de originele titel (als opschonen deze heeft gewijzigd).
3. Exacte overeenkomst met alleen de eerste artiestnaam en de opgeschoonde titel (voor multi-artiest-strings zoals "Artiest A & Artiest B").
4. Fuzzy search met de eerste artiestnaam en de opgeschoonde titel.
5. Fuzzy search met de ruwe trackstring als laatste redmiddel.

Wanneer platte songteksten beschikbaar zijn, worden ze getoond zoals ze zijn. Wanneer alleen tijd-gesynchroniseerde LRC-songteksten beschikbaar zijn, worden de tijdstempels verwijderd en wordt de platte tekst getoond. Instrumentale nummers worden gerapporteerd als niet gevonden.
## Instellingen

De volgende opties kunnen worden geconfigureerd via NVDA-menu → Opties → Instellingen → freeAudio:

| Optie | Beschrijving |
|---|---|
| Stem voor nummerwisseling | Kies of automatisch aangekondigde nummerwisselingen worden uitgesproken met de NVDA-synthesizer of met een geselecteerde SAPI5-stem. |
| SAPI5-stem | Wanneer **Stem voor nummerwisseling** op SAPI5 is ingesteld, selecteert welke geïnstalleerde SAPI5-stem wordt gebruikt om nummerwisselingen aan te kondigen. De lijst wordt op de achtergrond gevuld met de stemmen die op het systeem zijn geïnstalleerd. |
| Audio-uitvoerapparaat | Stelt het audio-uitvoerapparaat in voor radio-afspelen. De lijst bevat alle BASS-compatibele apparaten op het systeem plus een optie "Systeemstandaard". Wijzigingen worden direct na opslaan toegepast; als het geselecteerde apparaat is losgekoppeld, valt de add-on automatisch terug op de systeemstandaard en kondigt de wijziging aan. |
| Vernieuwingsmodus voor audioapparaten | Bepaalt hoe freeAudio de BASS-uitvoerapparaatnummers vernieuwt. **Betrouwbaar** (standaard) peilt apparaten live en volgt Bluetooth/USB-wijzigingen nauwkeuriger, maar kan apparaatwisselingen iets langzamer maken. **Snel** gebruikt de huidige BASS-apparatenlijst en is sneller, maar apparaatnummers kunnen verouderd blijven tot BASS of NVDA opnieuw wordt gestart. |
| Volume | Stelt het startvolume van de add-on in (0–100). Tijdens het afspelen kan `Ctrl+Win+↑` het volume verhogen tot 200, maar het startvolume dat hier wordt opgeslagen, is beperkt tot 100. |
| Audio-effecten | Stelt in welke effecten (Chorus, Compressor, Distortion, Echo, Flanger, Gargle, Reverb en de drie EQ-versterkingen) actief zijn wanneer NVDA start of een station begint te spelen. Meerdere effecten kunnen tegelijk worden aangevinkt, overeenkomstig de Effecten-lijst in de Stationsverkenner. |
| EQ-gain (Bass / Treble / Vocal) | Stelt het gain-niveau in dB in voor elke EQ-band (−15 tot +15). Deze waarden zijn van toepassing wanneer het bijbehorende EQ-effect actief is en worden globaal opgeslagen. Overschrijvingen per station kunnen worden opgeslagen met de knop **Audioprofiel opslaan** in het tabblad Favorieten. |
| Vloeiende stationsovergang | Regelt het overgangsgedrag bij het wisselen tussen **live radiostations**. **Directe overgang** (standaard) stopt het vorige station onmiddellijk voordat het nieuwe begint. **Korte crossfade (1 seconde)** en **Normale crossfade (2 seconden)** starten het nieuwe station direct zonder pauze, en vervagen vervolgens geleidelijk het vorige station op de achtergrond zodra de nieuwe stream als actief is bevestigd. **Stationsafstemgeluidseffect** stopt het vorige station onmiddellijk en speelt een stationsafstemgeluid af voordat het nieuwe begint. Heeft geen effect en geen prestatie-impact bij instelling op "Directe overgang". Niet van toepassing op podcasts, luisterboeken of jukeboxnummers — het hervatten daarvan speelt altijd zijn eigen korte cassette-geluidseffect af, ongeacht deze instelling; zie [Afspeeldetails van podcasts](#afspeeldetails-van-podcasts). |
| Laatste station hervatten bij NVDA-opstart | Indien ingeschakeld, start het laatst gespeelde station automatisch elke keer dat NVDA opstart. |
| Automatisch trackwijzigingen aankondigen (ICY-metadata) | Indien ingeschakeld, leest NVDA automatisch de nieuwe tracknaam telkens wanneer deze verandert op een station dat ICY-metadata uitzendt. De eerste track wordt ook direct aangekondigd bij het overschakelen naar een nieuw station. Standaard uitgeschakeld. |
| Meldingen dempen | Indien ingeschakeld, kondigt NVDA geen zenderwijzigingen, wijzigingen in afspeelstatus (spelen, pauze, stoppen) of opnamegebeurtenissen (gestart, gestopt, voltooid) aan. Foutmeldingen, feedback over favorieten, resultaten van muziekherkenning en update-meldingen worden niet beïnvloed. Kan ook direct worden in-/uitgeschakeld via een niet-toegewezen invoergebaar. Standaard uitgeschakeld. |
| freeAudio-berichten op de brailleleesregel weergeven | Indien ingeschakeld, stuurt freeAudio zijn meldingen ook rechtstreeks naar de brailleleesregel. Dit is handig voor tracktitels, zenderwijzigingen, afspeelstatus en volumewijzigingen. Standaard uitgeschakeld. |
| Tijdverschuivingsbuffer inschakelen (live radio terugspoelen) | Schakelt de terugspoelbediening (`Ctrl+Win+J`/`Ctrl+Win+K`) in of uit en vergroot de achtergrondopname van ~45 seconden tot de **Duur van tijdverschuivingsbuffer**. Een kleine achtergrondopname van het momenteel spelende station draait altijd, zelfs wanneer dit is uitgeschakeld — zie de opmerking in de sectie [Tijdverschuiving (live radio terugspoelen)](#tijdverschuiving-live-radio-terugspoelen) hierboven. Kan ook direct worden in-/uitgeschakeld met `Ctrl+Win+T`. Standaard uitgeschakeld — zie de sectie [Tijdverschuiving (live radio terugspoelen)](#tijdverschuiving-live-radio-terugspoelen) hierboven voor volledige details. Het heeft geen effect op podcasts en luisterboeken. |
| Duur van tijdverschuivingsbuffer | Stelt de maximale lengte van de terugspoelbuffer in. Opties variëren van 10 minuten tot 5 uur. Langere buffers verbruiken meer tijdelijke schijfruimte. |
| Gelikete nummers opslaan in een tekstbestand | Indien ingeschakeld, wordt trackinformatie die naar het klembord is gekopieerd door drie keer op `Ctrl+Win+I` te drukken, ook toegevoegd aan `Documents\freeAudio Recordings\likedSongs.txt`. Als er geen ICY-metadata beschikbaar is, wordt het Shazam-herkenningsresultaat in hetzelfde bestand opgeslagen. Standaard uitgeschakeld. |
| Wanneer Ctrl+Win+P wordt ingedrukt zonder actief afspelen | Bepaalt wat er gebeurt wanneer deze sneltoets wordt ingedrukt en er niets speelt: het laatste station starten of de favorietenlijst openen. |
| Wanneer Ctrl+Win+P tweemaal wordt ingedrukt | Selecteert wat er gebeurt wanneer de sneltoets twee keer snel achter elkaar wordt ingedrukt: niets doen, favorietenlijst openen, opnametabblad openen of timertabblad openen. Wanneer "niets doen" is geselecteerd, reageert de eerste druk onmiddellijk zonder vertraging. |
| Wanneer Ctrl+Win+P driemaal wordt ingedrukt | Selecteert wat er gebeurt wanneer de sneltoets drie keer snel achter elkaar wordt ingedrukt: niets doen, favorietenlijst openen, station zoeken openen, opnametabblad openen of timertabblad openen. |
| Automatisch controleren op updates | Indien ingeschakeld, wordt elke keer dat NVDA opstart een achtergrondcontrole op updates uitgevoerd; je krijgt een melding als er een nieuwe versie is gevonden. Indien uitgeschakeld, stoppen automatische controles, maar blijven handmatige controles beschikbaar. |
| Nu controleren op updates | Een knop die onmiddellijk op een nieuwe versie controleert, zelfs wanneer automatische controles zijn uitgeschakeld. Terwijl de controle loopt, toont de knop "Controleren...". |
| Pad naar ffmpeg.exe | Pad naar de ffmpeg.exe die wordt gebruikt voor muziekherkenning. Indien leeg gelaten, wordt automatisch een ffmpeg.exe in de add-on-map gebruikt. |
| Map voor opnames | Stelt de map in waar opgenomen bestanden worden opgeslagen. Indien leeg gelaten, wordt de standaardlocatie `Documents\freeAudio Recordings\` gebruikt. Een Bladeren-knop laat je de map interactief selecteren. Wijzigingen worden direct na het opslaan van kracht. |
| Modules | Een checklist van de optionele onderdelen van freeAudio: **Podcasts**, **Luisterboeken** en **Jukebox**. Alle drie zijn standaard ingeschakeld. Het uitvinken van een onderdeel verwijdert het tabblad uit de Stationsverkenner en de bijbehorende commando's uit het dialoogvenster Invoerhandelingen van NVDA, zonder iets te verwijderen dat je er hebt opgeslagen (abonnementen, bibliotheek, Jukebox-lijst); opnieuw aanvinken brengt alles terug. Wijzigingen worden van kracht de volgende keer dat de Stationsverkenner wordt geopend. |
| Neem netwerkstations mee in de zoekopdracht in de jukebox | Indien ingeschakeld, doorzoekt **Zoek op apparaten** in de Jukebox ook netwerkschijven. Standaard uitgeschakeld, omdat het doorzoeken van een netwerkshare minuten kan duren, of kan vastlopen als de share niet bereikbaar is. |
| Luisterboekbronnen | Een checklist die selecteert welke luisterboekbronnen (**GETEM**, **LibriVox**, **Project Gutenberg**) worden doorzocht en getoond op het tabblad Luisterboeken. Alle drie zijn standaard ingeschakeld. Het uitvinken van een bron verbergt de boeken uit die bron uit de samengevoegde zoekresultaten en bibliotheeklijst, zonder iets te verwijderen dat je er al hebt toegevoegd — zie [Luisterboeken (GETEM, LibriVox en Project Gutenberg)](#luisterboeken-getem-librivox-en-project-gutenberg). |
| GETEM-gebruikersnaam / GETEM-wachtwoord | Je lidmaatschapsgegevens voor [GETEM](https://getem.boun.edu.tr/)-luisterboeken, nodig om de audio van een boek te streamen of te downloaden — zie [Aanmelden](#aanmelden). Versleuteld op schijf opgeslagen via de Windows Data Protection API, gekoppeld aan je Windows-gebruikersaccount; nooit als platte tekst opgeslagen. Het leeg laten van beide velden en opslaan verwijdert eventuele opgeslagen inloggegevens. LibriVox en Project Gutenberg vereisen geen account en hebben geen equivalent veld. |
| Opname-uitvoerformaat | Behoudt de originele stream, extraheert audio zonder de codec te wijzigen, of converteert voltooide opnames naar MP3. De standaard is het originele streamformaat. |
| Bitsnelheid MP3-opname | Stelt de bitsnelheid in die wordt gebruikt wanneer het opname-uitvoerformaat MP3 is. De standaard is 128 kb/s. |
| Schakel de internetverbindingscontrole uit voor het afspelen | Aanbevolen voor gebruikers die een vertraging ervaren voordat een station begint te spelen. Ook handig wanneer DNS is geblokkeerd. |
| Opruimen: instellingen terugzetten en opgeslagen gegevens verwijderen... | Een knop die een dialoogvenster opent voor het terugzetten van de instellingen van freeAudio en het verwijderen van de gegevens die het heeft opgeslagen — zie [Opruimen: instellingen terugzetten en opgeslagen gegevens verwijderen](#opruimen-instellingen-terugzetten-en-opgeslagen-gegevens-verwijderen). |

### Opruimen: instellingen terugzetten en opgeslagen gegevens verwijderen

De knop **Opruimen: instellingen terugzetten en opgeslagen gegevens verwijderen...** onderaan de instellingenpagina van freeAudio opent het dialoogvenster **Instellingen terugzetten / opgeslagen gegevens verwijderen**. Het toont als selectievakjes wat freeAudio in de NVDA-configuratiemap opslaat. **Standaard is niets aangevinkt.** Elk item toont hoeveel ruimte het inneemt, of "niets opgeslagen":

- **Instellingen** — worden teruggezet naar de standaardwaarden. De opnamemap en de optie **Gelikete nummers opslaan in een tekstbestand** blijven behouden.
- **Favoriete stations**
- **Cache van de stationlijst** — wordt indien nodig opnieuw gedownload.
- **Podcast-abonnementen**
- **Luisterboekenbibliotheken** — GETEM, LibriVox en Project Gutenberg.
- **Opgeslagen GETEM-aanmelding** — de opgeslagen gebruikersnaam en het wachtwoord.
- **Jukeboxlijst** — je muziekbestanden worden niet verwijderd.
- **Opgeslagen hervatposities** — podcasts, luisterboeken en jukeboxmappen.
- **Bladwijzers** — elke bladwijzer, inclusief de tekstnotitie en spraaknotitie.
- **Slaaptimers en wekkers**
- **Geplande opnameschema's** — de opnamen zelf worden niet verwijderd.

**Alles selecteren** vinkt elk item aan. **Geselecteerde items terugzetten / verwijderen** voert je keuze uit; als er niets is aangevinkt, zegt freeAudio "Er is niets geselecteerd." **Annuleren** (of `Escape`) sluit het dialoogvenster zonder iets te doen.

Voordat er iets wordt gewijzigd, toont freeAudio de aangevinkte items, waarschuwt dat dit niet ongedaan kan worden gemaakt en vraagt je om te bevestigen; het standaardantwoord is **Nee**. Daarna zegt een bericht "Klaar.", of toont het de items die niet konden worden verwijderd — meestal omdat een bestand in gebruik is. Als de Stationsverkenner open is wanneer opgeslagen gegevens worden verwijderd, wordt deze gesloten, en wordt deze de volgende keer dat je hem opent opnieuw opgebouwd uit de resterende gegevens.

Opnames, de opnamemap en het tekstbestand met gelikete nummers worden **nooit** aangeraakt, en een reset van de instellingen zorgt er niet voor dat freeAudio opnieuw gegevens importeert uit de eerdere FreeRadio-add-on.

Na een reset van de instellingen worden de waarden die nog op de instellingenpagina worden getoond niet opgeslagen wanneer je op OK drukt, dus ze kunnen de reset niet ongedaan maken. Het wordt aanbevolen NVDA opnieuw te starten, zodat elke instelling van kracht wordt.

## Meldingen dempen

Wanneer **Meldingen dempen** is ingeschakeld in de Instellingen, onderdrukt NVDA de volgende automatische aankondigingen:

- Stationnaam wanneer een nieuw station begint te spelen
- Wijzigingen in afspeelstatus: spelen, pauze, stoppen
- Obligato-modus: gestart / gestopt
- Opnamegebeurtenissen: gestart, gestopt, voltooid (directe, nummer-, elk-nummer- en geplande opnames)
- Aankondigingen van ICY-trackwijzigingen, zelfs wanneer **Automatisch trackwijzigingen aankondigen** ook is ingeschakeld
- De melding dat een station in een speciale compatibiliteitsmodus wordt afgespeeld (zie [Afspelen](#afspelen))

De volgende aankondigingen worden opzettelijk **niet** beïnvloed: foutmeldingen, feedback over favorieten (toegevoegd / al in lijst), resultaten van muziekherkenning en update-meldingen.

De instelling kan worden in-/uitgeschakeld via NVDA-menu → Opties → Instellingen → freeAudio, of op elk gewenst moment direct via een niet-toegewezen invoergebaar (wijs er een toe via NVDA-menu → Opties → Invoerhandelingen → freeAudio). Wanneer in-/uitgeschakeld, kondigt NVDA eenmaal "Meldingen gedempt" of "Meldingen weer ingeschakeld" aan om de wijziging te bevestigen.

## Automatisch trackwijzigingen aankondigen

Wanneer de optie **Automatisch trackwijzigingen aankondigen** is ingeschakeld in Instellingen, controleert freeAudio de ICY-metadata-stream van het actieve station op de achtergrond ongeveer elke 5 seconden. Wanneer de track verandert, wordt de nieuwe titel automatisch door NVDA gelezen — geen toetsaanslag vereist.

Bij het overschakelen naar een nieuw station wordt de eerste trackinformatie aangekondigd zodra de verbinding tot stand is gebracht. Als je overschakelt naar een station dat geen ICY-metadata uitzendt, blijft het systeem stil en wordt de trackinformatie van het vorige station niet herhaald.

Deze functie is standaard uitgeschakeld en kan worden in-/uitgeschakeld via NVDA-menu → Opties → Instellingen → freeAudio.

## Afspelen

freeAudio gebruikt **BASS** als zijn enige afspeelbackend voor alles — internetradio, podcasts, luisterboeken en jukeboxnummers. Er is geen afzonderlijke installatie vereist; deze wordt meegeleverd met de add-on. freeAudio gebruikt geen VLC, PotPlayer of Windows Media Player.

BASS stuurt audio direct naar de Windows-audiostack en verschijnt in de Windows-volumemixer als een onafhankelijke audiobron genaamd "pythonw.exe", los van NVDA. Dit betekent dat freeAudio-audio via een volledig gescheiden kanaal stroomt van NVDA-spraak: de radio valt niet uit, mixt niet met, of wordt niet beïnvloed door de eigen audio-instellingen van NVDA terwijl NVDA spreekt. De gebruiker kan het radiovolume onafhankelijk van NVDA aanpassen in de Windows-volumemixer. Ondersteunt HTTP, HTTPS en de meeste ingesloten stream-formaten.

Podcastafleveringen, luisterboekhoofdstukken en jukeboxnummers worden via BASS afgespeeld omdat het de stream kan openen als een doorzoekbaar bestand (zelfs tijdens het downloaden), waardoor nauwkeurige positietracking, getrapt terug-/vooruitspoelen, afspeelsnelheid, toonhoogtetranspositie en hervatten mogelijk zijn. Audio duplicatie, tijdverschuiving en het zoeken en hervatten van podcasts, luisterboeken en jukeboxnummers zijn allemaal afhankelijk van BASS en altijd beschikbaar.

**HLS-stations die een compatibiliteitsmodus nodig hebben:** een paar HLS (`.m3u8`)-stations verpakken hun audio op een manier die BASS niet soepel kan lezen — het blijft de stream opnieuw openen, wat klinkt als constant haperen. Voor deze stations (momenteel de ABC Australia-radiostromen) verpakt freeAudio dezelfde audio automatisch opnieuw, zonder deze opnieuw te coderen, in een conventionele lay-out, met behulp van een kleine server die alleen op je eigen computer draait, en speelt die in plaats daarvan af. Er hoeft niets te worden geconfigureerd. De eerste keer dat je zo'n station afspeelt na het starten van NVDA, kondigt NVDA aan: "Dit station gebruikt een speciale afspeelmodus om haperingen te voorkomen." Deze aankondiging volgt de instelling **Meldingen dempen**.

## Update-controle

freeAudio controleert automatisch op nieuwe versies via GitHub.

**Automatische controle:** Draait stil op de achtergrond 15 seconden nadat NVDA is opgestart. Als een nieuwe versie is gevonden, krijg je een melding; als er geen wordt gevonden, wordt er geen bericht getoond.

**Handmatige controle:** Kan op verzoek worden geactiveerd via NVDA-menu → Extra → freeAudio → **Controleren op updates…**. Wanneer op deze manier gestart, wordt het resultaat aangekondigd, zelfs als de versie up-to-date is.

**Wanneer een update is gevonden:** Er opent een dialoogvenster met het versienummer en je geïnstalleerde versie.

- Als er een direct downloadbaar `.nvda-addon`-bestand beschikbaar is op de GitHub-release, wordt een knop **Downloaden en installeren** getoond. Zodra bevestigd, wordt het bestand op de achtergrond gedownload, kondigt NVDA aan wanneer de download start en opent NVDA's eigen installatiescherm automatisch.
- Als er geen directe downloadlink beschikbaar is, wordt een knop **Pagina openen** getoond en opent de GitHub-releasepagina in de standaardbrowser.

**Automatische controles uitschakelen:** Schakel de optie **Automatisch controleren op updates** uit via NVDA-menu → Opties → Instellingen → freeAudio.

## Dankbetuigingen en credits

- **Oorspronkelijke basis en concepten:** Oprechte dank aan **Gary Mp** ([GaryMp/freeradio](https://github.com/GaryMp/freeradio)) voor de oorspronkelijke radioconcepten en kernstructuren voor favorietenbeheer die als fundamentele basis voor dit project dienden.
- **AI- en LLM-tools:** Dank aan moderne Large Language Model (LLM)-tools (waaronder Claude, ChatGPT en Gemini) voor ondersteuning tijdens de ontwikkeling, code-refactoring en feature-implementatiefasen.
- **Directory-service:** Stationcatalogus mogelijk gemaakt door de [Radio Browser API](https://www.radio-browser.info/).
- **Gemeenschap:** Oprechte dank aan alle NVDA-gemeenschapsleden en vertalers voor hun voortdurende ondersteuning, feedback en lokalisatiebijdragen.

## Licentie

GPL v2