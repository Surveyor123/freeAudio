# freeAudio - doplněk NVDA

freeAudio je plnohodnotný doplněk internetového rádia, podcastů, audioknih a místního jukeboxu pro čtečku obrazovky NVDA. Z jednoduchého způsobu poslechu internetových rozhlasových stanic se postupně vyvinul v kompletní, plně přístupné centrum poslechu - každá obrazovka, dialog a ovládací prvek je od základu navržen pro použití s klávesnicí a čtečkou obrazovky, bez nutnosti myši v kterémkoli kroku.

## Co freeAudio umí

- **Internetové rádio** - Procházejte a vyhledávejte mezi více než 50 000 stanicemi z adresáře [Radio Browser](https://www.radio-browser.info/), doplněného o výsledky z TuneIn a iHeartRadio. Ukládejte oblíbené stanice, měňte jejich pořadí a přejděte přímo na kteroukoli z nich globální klávesovou zkratkou odkudkoli ve Windows - viz [Adresář Radio Browser](#adresář-radio-browser) a [Oblíbené](#oblíbené).
- **Podcasty** - Přihlaste se k odběru libovolného kanálu RSS/Atom, nebo vyhledávejte v adresáři podcastů Apple a před přihlášením k odběru si poslechněte náhled epizod. Pozice přehrávání se ukládá automaticky a pokračuje tam, kde jste skončili - viz [Podcasty](#podcasty).
- **Audioknihy** - Vyhledávejte a přehrávejte nebo stahujte knihy ze tří zdrojů: [GETEM](https://getem.boun.edu.tr/), digitální knihovny Univerzity Boğaziçi pro zrakově postižené, [LibriVox](https://librivox.org/), projektu audioknih z veřejné domény čtených dobrovolníky, a kolekce otevřených audioknih Project Gutenberg - poslední dva nevyžadují účet - s automatickým pokračováním napříč vícedílnými díly - viz [Audioknihy (GETEM, LibriVox a Project Gutenberg)](#audioknihy-getem-librivox-a-project-gutenberg).
- **Místní jukebox** - Prohledávejte zvukové soubory uložené na jakémkoli připojeném disku podle názvu, nebo si vytvořte osobní knihovnu souborů a složek, a přehrávejte je se stejnými nástroji pro pokračování, posouvání, rychlost a transpozici, jaké používají podcasty a audioknihy - viz [Místní jukebox](#místní-jukebox).
- **Nahrávání** - Nahrávejte právě hrající obsah okamžitě, automaticky zachyťte jednu skladbu při jejím začátku a konci, nebo naplánujte jednorázová či opakovaná nahrávání - to vše bez přerušení přehrávání - viz [Nahrávání](#nahrávání).
- **Časový posun (přetočení živého rádia)** - Pozastavte a přetočte živou stanici jako DVR, a poté se kdykoli vraťte zpět k živému vysílání - viz [Časový posun (přetočení živého rádia)](#časový-posun-přetočení-živého-rádia).
- **Rozpoznávání hudby a oblíbené skladby** - Rozpoznávejte skladby bez metadat pomocí technologie Shazam, ukládejte oblíbené skladby do textového souboru a vyhledávejte jejich texty - viz [Rozpoznávání hudby](#rozpoznávání-hudby) a [Oblíbené skladby](#oblíbené-skladby).
- **Zvukové profily a efekty** - Ukládejte samostatná nastavení hlasitosti, efektů, ekvalizéru a rychlosti přehrávání pro každou stanici, podcast, audioknihu nebo skladbu jukeboxu, a používejte efekty v reálném čase (Chorus, Reverb, zesílení ekvalizéru a další) prostřednictvím backendu BASS - viz [Zvukový profil stanice](#zvukový-profil-stanice).
- **Transpozice (posun výšky tónu)** - Posuňte výšku tónu podcastů, audioknih a skladeb jukeboxu nahoru nebo dolů bez změny jejich rychlosti pomocí přibalené komponenty `bass_fx` - viz [Transpozice (posun výšky tónu)](#transpozice-posun-výšky-tónu).
- **Zrcadlení zvuku** - Odesílejte stejný datový tok do dvou zvukových výstupních zařízení najednou, například do reproduktorů i sluchátek zároveň - viz [Zrcadlo zvuku](#zrcadlo-zvuku).
- **Režim Obligato (hudba na pozadí)** - Opakovaně přehrávejte zvolenou oblíbenou stanici tiše na pozadí, na vlastním výstupním zařízení a s vlastní hlasitostí, bez ohledu na to, co (nebo zda vůbec něco) hraje jako hlavní médium - viz [Režim hudby na pozadí (Obligato)](#režim-hudby-na-pozadí-obligato).
- **Časovače** - Naplánujte spuštění přehrávání oblíbené stanice, nebo naplánujte zastavení přehrávání, v konkrétní čas - viz [Časovač](#časovač).
- **Rozsáhlý přístup z klávesnice a přes braillský řádek** - Ke každé funkci se dostanete zcela z klávesnice, s globálními zkratkami fungujícími odkudkoli ve Windows, přímými klávesovými zkratkami pro jednotlivé oblíbené stanice a volitelným braillským výstupem pro všechna mluvená oznámení FreeRadia.

## Adresář Radio Browser

freeAudio používá pro svůj katalog stanic otevřenou databázi [Radio Browser](https://www.radio-browser.info/). Radio Browser je komunitou spravovaný bezplatný katalog, který obsahuje více než 50 000 internetových rozhlasových stanic z celého světa. Nevyžaduje žádnou registraci ani účet a jeho rozhraní API je přístupné všem. Každá stanice obsahuje adresu, zemi, žánr, jazyk a informace o datovém toku; stanice jsou řazeny podle hlasů uživatelů. freeAudio se k tomuto API připojuje prostřednictvím zrcadlových serverů umístěných v Německu, Nizozemsku a Rakousku; pokud je jeden server nedostupný, automaticky se přepne na další.

Aby prohlížeč zůstal responzivní a nebylo nutné zatěžovat API při každém vyhledávání nebo změně země, udržuje freeAudio na disku místní mezipaměť (cache) katalogu stanic. Tato mezipaměť se automaticky obnovuje na pozadí v pravidelných intervalech, takže zobrazený seznam je obvykle již aktuální bez jakéhokoli zásahu z vaší strany. Okamžitou opětovnou synchronizaci můžete kdykoli vynutit tlačítkem **Aktualizovat seznam stanic** – viz Prohlížeč stanic níže.

## Přidání stanice do aplikace Radio Browser

Pokud se vámi hledaná stanice nenachází v adresáři Radio Browser, můžete ji sami odeslat na adrese [https://www.radio-browser.info/add](https://www.radio-browser.info/add). Není potřeba žádný účet ani registrace.

Vyplňte formulář na této stránce:

- **URL streamu** *(povinný údaj)* - přímá adresa URL audio streamu, končící na `.mp3`, `.aac`, `.ogg` nebo podobně. Nejedná se o adresu webové stránky stanice, ale o adresu surového streamu, kterou byste vložili do přehrávače médií. Většina stanic zveřejňuje adresu URL svého streamu na svých webových stránkách nebo v sekci "Poslouchat živě".
- **Název stanice** *(povinný údaj)* - název stanice, jak by se měl zobrazovat v adresáři.
- **Homepage** - adresa webové stránky stanice.
- **Země a jazyk** - vyberte zemi a jazyk vysílání z rozevíracích seznamů.
- **Štítky** - žánrová nebo tematická klíčová slova oddělená čárkami, například `news`, `jazz`, `classical`. Používají se pro vyhledávání a filtrování.
- **URL loga** - přímý odkaz na obrázek loga stanice, pokud je k dispozici.

Po odeslání je stanice zkontrolována a přidána do veřejného adresáře. Po přijetí se automaticky objeví ve vyhledávání freeAudio a v seznamu zemí, protože adresář je obnovován z živého API.

## Požadavky

- NVDA 2025.1	 nebo novější
- Windows 10 nebo novější
- Připojení k internetu

## Instalace

Stáhněte si soubor `.nvda-addon`, stiskněte na něm Enter a po výzvě restartujte NVDA.

## Klávesové zkratky

Všechny klávesové zkratky lze znovu přiřadit v nabídce NVDA → Předvolby → Vstupní gesta → freeAudio. Tyto zkratky fungují odkudkoli, bez ohledu na to, které okno má fokus.

Některé z těchto zkratek se překrývají se zkratkami, které používá sám systém Windows. Pokud chcete zachovat vlastní zkratku Windows bez opětovného přiřazení zkratky freeAudio, stiskněte těsně před kombinací kláves `NVDA+F2` (Předat další klávesu) — NVDA odešle tuto jednu kombinaci kláves přímo do Windows místo toho, aby ji zachytila pro freeAudio.

| Zkratka | Funkce | Popis |
|---|---|---|
| `Ctrl+Win+R` | Otevřít prohlížeč stanic | Otevře okno prohlížeče, pokud je zavřené, nebo jej přenese do popředí, pokud je již otevřené. |
| `Ctrl+Win+O` | Otevřít kartu Podcasty | Otevře prohlížeč stanic (pokud je zavřený) nebo jej přenese do popředí a přepne přímo na kartu **Podcasty**. |
| `Ctrl+Win+L` | Otevřít kartu Audioknihy | Otevře prohlížeč stanic (pokud je zavřený) nebo jej přenese do popředí a přepne přímo na kartu **Audioknihy**. |
| `Ctrl+Win+U` | Otevřít kartu Jukebox | Otevře prohlížeč stanic (pokud je zavřený) nebo jej přenese do popředí a přepne přímo na kartu **Jukebox**, zaměřenou na vyhledávací pole disku. |
| `Ctrl+Win+P` | Pozastavit / obnovit | Pozastaví aktuální stanici, pokud se přehrává; obnoví, pokud je pozastavena. Pokud nic nepřehrává, spustí poslední stanici nebo otevře seznam oblíbených stanic v závislosti na vašem nastavení. Dvěma rychlými stisky za sebou přejdete přímo na zvolenou kartu. Třikrát stisknout tlačítko může v závislosti na nastavení spustit samostatnou akci. |
| `Ctrl+Win+S` | Stop | Úplně zastaví aktuální stanici a resetuje přehrávač. |
| `Ctrl+Win+→` | Další oblíbená stanice | Přesune na další stanici v seznamu oblíbených. Na konci seznamu se vrátí na začátek. |
| `Ctrl+Win+←` | Předchozí oblíbená stanice | Přesune na předchozí stanici v seznamu oblíbených. Přeskočí na konec, když je na začátku. |
| `Ctrl+Win+↑` | Zvýšení hlasitosti | Zvýší hlasitost o 5; maximálně 200. |
| `Ctrl+Win+↓` | Snížení hlasitosti | Sníží hlasitost o 5; minimálně 0. |
| `Ctrl+Win+V` | Přidat k oblíbeným / stáhnout médium | Přidá aktuálně přehrávanou stanici do seznamu oblíbených nebo stáhne aktuálně přehrávanou epizodu podcastu či audioknihu. Oznámí, pokud je stanice již v seznamu nebo pokud bylo médium již staženo. Neplatí, když se přehrává skladba z jukeboxu: freeAudio oznámí, že zkratka je určena pouze pro stanice, podcasty nebo audioknihy. |
| `Ctrl+Win+Shift+K` | Zvýšit rychlost přehrávání | Zvýší rychlost přehrávání epizody podcastu, audioknihy nebo skladby jukeboxu o 0,1× (se zachováním výšky tónu). Rozsah: 0,5× až 2,0×. |
| `Ctrl+Win+Shift+J` | Snížit rychlost přehrávání | Sníží rychlost přehrávání epizody podcastu, audioknihy nebo skladby jukeboxu o 0,1×. |
| `Shift+Win+K` | Transponovat nahoru | Zvýší výšku tónu epizody podcastu, audioknihy nebo skladby jukeboxu v krocích 1/8 celého tónu (0,25 půltónu), bez změny rychlosti. Rozsah: −12,00 až +12,00 půltónu. Viz [Transpozice (posun výšky tónu)](#transpozice-posun-výšky-tónu). |
| `Shift+Win+J` | Transponovat dolů | Sníží výšku tónu v krocích 1/8 celého tónu, bez změny rychlosti. |
| `Ctrl+Win+I` | Informace o stanici | Oznámí název aktuálně přehrávané stanice, epizody podcastu, audioknihy nebo skladby jukeboxu. Dvojím stisknutím zobrazíte v dialogovém okně podrobnosti, jako je země, žánr a datový tok. Třikrát stiskněte pro zkopírování informací o aktuální skladbě (metadata ICY) do schránky, pokud jsou k dispozici; pokud metadata nejsou k dispozici, spustí se místo toho rozpoznávání hudby Shazam. Čtyřnásobným stisknutím vynutíte rozpoznání hudby v případě nesprávných metadat ICY. |
| `Ctrl+Win+M` | Zrcadlení zvuku | Zrcadlí aktuální datový tok nebo médium na další výstupní zvukové zařízení současně. Dalším stisknutím zrcadlení zastavíte. |
| `Ctrl+Win+Shift+M` | Režim Obligato (hudba na pozadí) | Opakovaně přehrává zvolenou oblíbenou stanici tiše na pozadí, na vlastním výstupním zařízení a s vlastní hlasitostí, bez ohledu na to, co hraje v hlavním přehrávači. První stisknutí otevře dialog pro výběr stanice, výstupního zařízení a relativní hlasitosti. Dalším stisknutím jej zastavíte. |
| `Ctrl+Win+E` | Okamžité nahrávání | Jedním stisknutím spustíte nahrávání aktuální stanice; dalším stisknutím nahrávání zastavíte. Stisknutím **dvakrát** spustíte **nahrávání skladby** - soubor je pojmenován podle aktuální skladby a nahrávání se automaticky zastaví při změně skladby. Dalším dvojím stisknutím v době, kdy je nahrávání skladby aktivní, jej předčasně zastavíte. Přehrávání pokračuje bez přerušení ve všech režimech nahrávání. K dispozici pouze pro stanice, které vysílají metadata ICY. |
| `Ctrl+Win+W` | Otevřít složku s nahrávkami | Otevře složku s nahranými soubory v Průzkumníku souborů. |
| `Ctrl+Win+J` | Časový posun zpět / posun vzad v podcastu, audioknize a jukeboxu | Pro živé rádio: přetočí o 15 sekund zpět. První stisknutí vstoupí do režimu časového posunu; každé další stisknutí posune o dalších 15 sekund zpět, až do limitu vyrovnávací paměti nastaveného v nastavení FreeRadia. Vyžaduje povolení vyrovnávací paměti časového posunu v Nastavení. Pro epizodu podcastu, audioknihu nebo skladbu jukeboxu tento klíč posouvá v rámci souboru, a škáluje se podle způsobu stisku: **podržení** posouvá o 5 sekund za opakování; **jedno záměrné stisknutí** posune o 12 sekund zpět; **dvě stisknutí** rychle za sebou posunou o 1 minutu; **tři a více stisknutí** posune o 5 minut. Na jednu sekvenci stisknutí proběhne pouze jedno posunutí, velikostně odpovídající počtu stisknutí - stisknutí se nesčítají. Funguje bez ohledu na nastavení časového posunu. |
| `Ctrl+Win+K` | Časový posun vpřed / posun vpřed v podcastu, audioknize a jukeboxu | Pro živé rádio: posune o 15 sekund vpřed v režimu časového posunu. Po dosažení živého vysílání se přehrávání automaticky vrátí na přímý přenos a tento příkaz nebude mít žádný efekt, dokud znovu nepřetočíte zpět. Pro epizodu podcastu, audioknihu nebo skladbu jukeboxu tento klíč posouvá vpřed v rámci souboru se stejným škálováním stisknutí/podržení jako `Ctrl+Win+J` výše (podržení = 5 sekund za opakování; 1 stisknutí = 12 sekund; 2 stisknutí = 1 minuta; 3+ stisknutí = 5 minut). Funguje bez ohledu na nastavení časového posunu. |
| `Ctrl+Win+T` | Přepnout vyrovnávací paměť časového posunu | Okamžitě zapne nebo vypne vyrovnávací paměť časového posunu, v souladu se zaškrtávacím políčkem v Nastavení. Vypnutí okamžitě vrátí zpět na živé vysílání a zastaví zachytávání na pozadí. Nemá vliv na přehrávání podcastů, audioknih nebo jukeboxu. |
| *(nepřiřazeno)* | Vybrat výstupní zařízení | Otevře na vyžádání seznam dostupných hlavních výstupních zařízení. Seznam se zobrazí pouze v případě, že BASS rozpozná více než jedno fyzické výstupní zařízení. Přiřazení kombinace kláves pomocí NVDA Menu → Předvolby → Vstupní gesta → freeAudio. |
| *(nepřiřazeno)* | Přepnout oznámení o ztlumení | Přepíná nastavení oznámení o ztlumení za chodu. Přiřazení kombinace kláves pomocí NVDA Menu → Předvolby → Vstupní gesta → freeAudio. |
| *(nepřiřazeno)* | Přehrát oblíbenou stanici přímo | Každá stanice v seznamu oblíbených se zobrazuje jako samostatná položka v nabídce NVDA → Předvolby → Vstupní gesta → **freeAudio Stations**. Přiřaďte klávesovou zkratku libovolné stanici a spusťte ji okamžitě odkudkoli bez nutnosti otevírat prohlížeč. |

Další / předchozí zkratky navigují pouze v seznamu oblíbených stanic; nefungují se seznamem všech stanic. Když je seznam zaměřen v okně prohlížeče, slouží ke stejnému účelu klávesy se šipkou doleva a doprava - viz Zkratky v dialogu.

## Prohlížeč stanic

Aplikace freeAudio přidává do nabídky NVDA menu nástroje také podnabídku **freeAudio**. Z ní můžete přímo otevřít Průzkumníka stanic a Nastavení FreeRadia.

Okno otevřené pomocí `Ctrl+Win+R` obsahuje osm záložek: Všechny stanice, Oblíbené, Nahrávání, Časovač, Oblíbené skladby, Podcasty, Audioknihy a Jukebox. Mezi kartami můžete přecházet pomocí `Ctrl+Tab` nebo pomocí kláves `Alt+1` až `Alt+8`.

Po otevření karty Všechny stanice se automaticky načte 1 000 nejčastěji volených stanic z Prohlížeče rádií. Výběrem země z rozbalovacího seznamu se seznam aktualizuje a zobrazí se stanice dané země. Zadáním do vyhledávacího pole se okamžitě provede kompletní vyhledávání v celé databázi aplikace Radio Browser současně podle názvu, země a žánru.

Při vyhledávání jsou výsledky z Radio Browser doplněny o stanice z TuneIn a iHeartRadio (jsou-li k dispozici). Tyto externí zdroje jsou prohledávány na pozadí a jejich výsledky jsou automaticky sloučeny do seznamu, což vám poskytuje přístup k ještě více stanicím bez jakékoli další akce.

V rozbalovacím seznamu **Výstupní zařízení** v dolní části okna prohlížeče - mimo karty - jsou uvedena všechna výstupní zvuková zařízení rozpoznaná rozhraním BASS. Výběrem zařízení se na něj okamžitě přesměruje zvukový výstup a volba se trvale uloží; stejné zařízení se automaticky použije při příští relaci. Pokud vybrané zařízení není připojeno, doplněk se automaticky vrátí k výchozímu nastavení systému. Stisknutím `F11` kdekoli v Prohlížeči stanic otevřete jednodušší výběr zařízení na vyžádání. Tento výběr se nezobrazuje automaticky a otevře se pouze v případě, že BASS rozpozná více než jedno fyzické výstupní zařízení. Pokud je k dispozici pouze jedno zařízení, výběr není potřeba a freeAudio použije výchozí systémový výstup. Tato funkce je funkční pouze v případě, že je aktivní backend BASS.

Ovládací prvky **Hlasitosti** (0-200) a **Efekty** ve stejné oblasti lze nastavit kdykoli, když je okno otevřené. V seznamu efektů lze současně aktivovat funkce Chorus, Compressor, Distortion, Echo, Flanger, Gargle, Reverb, EQ: Bass Boost, EQ: Treble Boost a EQ: Vocal Boost; změny se okamžitě aplikují na aktivní proud. Každý efekt lze také okamžitě přepnout klávesovými zkratkami `Ctrl+1` až `Ctrl+0`, aniž byste museli opustit klávesnici – viz Klávesové zkratky pro efekty níže. Tyto ovládací prvky jsou plně funkční pouze v případě, že je aktivní backend BASS.

Pokud je aktivován jeden nebo více EQ efektů, automaticky se zobrazí **ovládací prvek zesílení** pro každé aktivní pásmo. Zesílení lze nastavit v rozsahu od −15 dB do +15 dB; výchozí hodnoty jsou basy +9 dB, výšky +9 dB a vokál +6 dB. Ovládací prvky se zobrazují pouze pro zaškrtnutá EQ pásma a automaticky se skryjí, když je efekt odznačen. Hodnoty se trvale ukládají a obnoví se při příštím spuštění.

V dolní části okna se nachází také tlačítko **Přehrát/Pozastavit**. Pokud není přehrávána žádná stanice, spustí vybranou stanici; pokud je již přehrávána stanice, pozastaví přehrávání.

Tlačítko **Aktualizovat seznam stanic** okamžitě znovu synchronizuje místní katalog stanic s API Radio Browser, místo aby se čekalo na pravidelnou aktualizaci na pozadí. Během aktualizace je tlačítko deaktivováno a NVDA oznámí, že aktualizace probíhá; pokud jej stisknete znovu ještě před dokončením aktuální aktualizace, NVDA vás upozorní, že již jedna probíhá. Po dokončení aktualizace NVDA oznámí, že seznam stanic byl aktualizován, a aktuálně zobrazené výsledky vyhledávání nebo seznam podle země se automaticky obnoví, aby odrážely nová data.

Je-li v seznamu vybrána stanice, tlačítko **Podrobnosti o stanici** zobrazí v samostatném dialogovém okně informace, jako je země, jazyk, žánr, formát, datový tok, webová stránka a adresa URL streamu. Každé pole se zobrazuje ve vlastním textovém poli určeném pouze pro čtení; mezi poli se můžete pohybovat pomocí klávesy Tab a všechny informace najednou zkopírovat do schránky pomocí tlačítka **Kopírovat vše do schránky**. Toto tlačítko je k dispozici na kartách Všechny stanice i Oblíbené.

### Kontextová nabídka stanice

Klepnutím pravým tlačítkem na stanici v seznamu Všechny stanice nebo Oblíbené, případně jejím vybráním a stiskem klávesy Nabídka nebo `Shift+F10`, otevřete kontextovou nabídku s rychlými akcemi:

- **Podrobnosti o stanici** — totéž jako tlačítko Podrobnosti o stanici popsané výše.
- **Přidat do oblíbených** *(karta Všechny stanice)* / **Odstranit stanici** *(karta Oblíbené)*.
- **Přejmenovat stanici** *(karta Oblíbené)* — totéž jako `F9`.
- **Uložit zvukový profil pro tuto stanici** / **Vymazat zvukový profil** *(karta Oblíbené)* — viz Zvukový profil stanice.
- **Otestovat adresu URL** — zkontroluje, zda je datový tok vybrané stanice aktuálně dostupný, aniž by spustil přehrávání, a oznámí výsledek (dostupné, nebo důvod selhání, například chybu HTTP nebo vypršení časového limitu).

Zobrazí se pouze položky relevantní pro aktuální kartu a výběr.

### Zkratky v dialogovém okně

Následující klávesy fungují pouze při aktivním okně Průzkumník stanic.

### Klávesy F

| Zkratka | Funkce | Popis |
|---|---|---|
| `F1` | Průvodce nápovědou | Otevře soubor nápovědy doplňku ve výchozím prohlížeči. Nejprve se vyhledá průvodce pro aktivní jazyk NVDA; pokud není nalezen, otevře se výchozí průvodce. |
| `F2` | co se přehrává | Oznámí aktuálně přehrávanou stanici a název skladby. Dvojím stisknutím zobrazíte v dialogovém okně podrobnosti, jako je země, žánr a datový tok. Třikrát stiskněte pro zkopírování informací o aktuální skladbě (metadata ICY) do schránky, pokud jsou k dispozici; pokud metadata nejsou k dispozici, spustí se místo toho rozpoznávání hudby Shazam. Čtyřnásobným stisknutím vynutíte rozpoznání hudby v případě nesprávných metadat ICY. |
| `F3` | Předchozí položka | Na kartě Všechny stanice nebo Oblíbené: přesune na předchozí stanici a okamžitě zahájí přehrávání. Na kartě Podcasty: přesune na předchozí epizodu v seznamu epizod a přehraje ji. Na kartě Audioknihy: přesune na předchozí knihu a začne ji přehrávat. Na kartě Jukebox: přesune na předchozí skladbu ve vybrané položce jukeboxu a přehraje ji. |
| `F4` | Další položka | Na kartě Všechny stanice nebo Oblíbené: přesune na další stanici a okamžitě zahájí přehrávání. Na kartě Podcasty: přesune na další epizodu a přehraje ji. Na kartě Audioknihy: přesune na další knihu a začne ji přehrávat. Na kartě Jukebox: přesune na další skladbu ve vybrané položce jukeboxu a přehraje ji. |
| `Shift+F3` | Předchozí kanál / část / položka | Na kartě Podcasty: přejde o jeden kanál výše v seznamu odběrů. Na kartě Audioknihy: přesune na předchozí část aktuálně přehrávané knihy. Na kartě Jukebox: přejde o jednu položku jukeboxu (soubor nebo složku) výše v hlavním seznamu. |
| `Shift+F4` | Další kanál / část / položka | Na kartě Podcasty: přejde o jeden kanál níže v seznamu odběrů. Na kartě Audioknihy: přesune na další část aktuálně přehrávané knihy. Na kartě Jukebox: přejde o jednu položku jukeboxu níže v hlavním seznamu. |
| `F5` | Snížení hlasitosti | Sníží hlasitost o 5 (minimálně 0). |
| `F6` | Zvýšení hlasitosti | Zvýší hlasitost o 5 (maximálně 200). |
| `F7` | Pozastavení / obnovení | Pozastaví přehrávání stanice; obnoví přehrávání, pokud je pozastaveno a je načteno médium. |
| `F8` | Stop | Úplně zastaví aktuální stanici a resetuje přehrávač. |
| `F9` | Přejmenovat | Otevře dialogové okno pro přejmenování zaměřené stanice na kartě oblíbené. |
| `F11` | Vybrat výstupní zařízení | Otevře výběr hlavního výstupního zařízení, pokud BASS rozpozná více než jedno fyzické výstupní zařízení. Aktuální zařízení je předem vybráno; Enter volbu použije a uloží. |

### Seznam a navigační zkratky

| Zkratka | Funkce | Popis |
|---|---|---|
| `→` | Další položka | Když je zaměřen seznam stanic (Všechny stanice / Oblíbené), přejde na další stanici a okamžitě ji přehraje. Když je zaměřen seznam epizod (Podcasty), přejde na další epizodu a přehraje ji. Na konci seznamu se nabalí na začátek. |
| `←` | Předchozí položka | Když je zaměřen seznam stanic, přejde na předchozí stanici a přehraje ji. Když je zaměřen seznam epizod, přejde na předchozí epizodu a přehraje ji. Přeskočí na konec, když je na začátku. |
| `Ctrl+→` | Další epizoda / kniha / skladba | Na kartě Podcasty: přejde na další epizodu a přehraje ji. Na kartě Audioknihy (zaměřen seznam knihovny): přejde na další knihu. Na kartě Jukebox (zaměřen seznam položek nebo skladeb): přejde na další skladbu ve vybrané položce jukeboxu a přehraje ji. |
| `Ctrl+←` | Předchozí epizoda / kniha / skladba | Na kartě Podcasty: přejde na předchozí epizodu a přehraje ji. Na kartě Audioknihy: přejde na předchozí knihu. Na kartě Jukebox: přejde na předchozí skladbu ve vybrané položce jukeboxu a přehraje ji. |
| `Enter` | Přehrát / Přidat | V seznamu stanic nebo epizod: začne okamžitě přehrávat vybranou položku. Ve výsledcích vyhledávání na kartě Jukebox: přidá vybraný soubor do jukeboxu. V seznamu položek nebo skladeb na kartě Jukebox: přehraje zaměřenou položku přímo. |
| `Mezerník` | Přehrát / Pozastavit / Náhled | Pozastaví, pokud se něco přehrává; v opačném případě spustí přehrávání vybrané položky. Ve výsledcích vyhledávání na kartě Jukebox: přepne náhled (přehrát/zastavit) vybraného souboru. V seznamu položek nebo skladeb na kartě Jukebox: pozastaví, pokud se přehrává, jinak přehraje zaměřenou položku. |
| `Ctrl+Tab` | Další karta | Přepne na další kartu (Všechny stanice → Oblíbené → Nahrávání → Časovač → Oblíbené skladby → Podcasty → Audioknihy → Jukebox). |
| `Ctrl+Shift+Tab` | Předchozí karta | Přepne na předchozí kartu. |
| `Escape` | Skrýt | Skryje okno; doplněk pokračuje v přehrávání na pozadí. |

### Klávesové zkratky pro hlasitost

| Zkratka | Funkce | Popis |
|---|---|---|
| `Ctrl+↑` | Zvýšení hlasitosti | Zvýší hlasitost o 5. Funguje pouze při otevřeném okně prohlížeče. |
| `Ctrl+↓` | Snížení hlasitosti | Sníží hlasitost o 5. Funguje pouze při otevřeném okně prohlížeče. |

### Klávesové zkratky pro efekty

| Zkratka | Funkce | Popis |
|---|---|---|
| `Ctrl+1` | Přepnout Chorus | Zapne nebo vypne efekt Chorus a okamžitě jej použije na aktivní datový tok. |
| `Ctrl+2` | Přepnout Compressor | Zapne nebo vypne efekt Compressor a okamžitě jej použije na aktivní datový tok. |
| `Ctrl+3` | Přepnout Distortion | Zapne nebo vypne efekt Distortion a okamžitě jej použije na aktivní datový tok. |
| `Ctrl+4` | Přepnout Echo | Zapne nebo vypne efekt Echo a okamžitě jej použije na aktivní datový tok. |
| `Ctrl+5` | Přepnout Flanger | Zapne nebo vypne efekt Flanger a okamžitě jej použije na aktivní datový tok. |
| `Ctrl+6` | Přepnout Gargle | Zapne nebo vypne efekt Gargle a okamžitě jej použije na aktivní datový tok. |
| `Ctrl+7` | Přepnout Reverb | Zapne nebo vypne efekt Reverb a okamžitě jej použije na aktivní datový tok. |
| `Ctrl+8` | Přepnout EQ: Bass Boost | Zapne nebo vypne pásmo EQ: Bass Boost a okamžitě jej použije na aktivní datový tok. |
| `Ctrl+9` | Přepnout EQ: Treble Boost | Zapne nebo vypne pásmo EQ: Treble Boost a okamžitě jej použije na aktivní datový tok. |
| `Ctrl+0` | Přepnout EQ: Vocal Boost | Zapne nebo vypne pásmo EQ: Vocal Boost a okamžitě jej použije na aktivní datový tok. |

Každá zkratka odpovídá zaškrtnutí nebo odškrtnutí příslušné položky v seznamu **Efekty**: NVDA oznámí, zda byl efekt zapnut nebo vypnut, změna se automaticky uloží a ovládací prvek zesílení pro dané pásmo (pokud existuje) se podle toho zobrazí nebo skryje. K dispozici pouze v případě, že je aktivní backend BASS.

### Klávesové zkratky Alt

| Zkratka | Funkce | Popis |
|---|---|---|
| `Alt+R` | Přejít na vyhledávací pole | Přesune fokus na textové pole pro vyhledávání. Vyhledá v rádiovém prohlížeči text ve vyhledávacím poli; současně se vyhledává název, země a žánr. |
| `Alt+V` | Přidat / odebrat oblíbené | Přidá vybranou stanici do oblíbených; pokud již v seznamu je, odebere ji. |
| `Alt+1` | Všechny stanice | Přepne na kartu Všechny stanice. |
| `Alt+2` | Oblíbené | Přepne na kartu Oblíbené. |
| `Alt+3` | Nahrávání | Přepne na kartu Nahrávání. |
| `Alt+4` | Časovač | Přepne na kartu Časovač. |
| `Alt+5` | Oblíbené skladby | Přepne na kartu Oblíbené skladby. |
| `Alt+6` | Podcasty | Přepne na kartu Podcasty. |
| `Alt+7` | Audioknihy | Přepne na kartu Audioknihy. |
| `Alt+8` | Jukebox | Přepne na kartu Jukebox, zaměřenou na vyhledávací pole disku. |
| `Alt+K` | Zavřít | Zavře okno; doplněk pokračuje v přehrávání na pozadí. |

## Oblíbené

Seznam oblíbených stanic je trvale uložená osobní sbírka stanic. Chcete-li přidat stanici, vyberte ji v seznamu a stiskněte tlačítko Přidat do oblíbených nebo použijte klávesovou zkratku `Alt+V`. Stejná klávesová zkratka odstraní stanici, která je již v seznamu, když je vybrána.

Oblíbené lze přehrávat pomocí kláves `Ctrl+Win+→` a `Ctrl+Win+←`; tyto klávesové zkratky fungují, i když není otevřeno okno prohlížeče.

Chcete-li stanici ze seznamu oblíbených odstranit, vyberte ji a stiskněte tlačítko **Odstranit stanici** nebo klávesu `Odstranit`. Po odstranění se zaměření a výběr automaticky přesunou na další stanici v seznamu. Pokud byla odstraněná stanice poslední, přesune se fokus na předchozí stanici. Pokud se seznam vyprázdní, fokus se přesune na tlačítko Play.

### Označení a odstranění více položek

Oblíbené, oblíbené skladby, knihovna audioknih a seznam jukeboxu podporují označení několika položek a jejich společné odstranění v jednom kroku:

- Stiskněte **`.`** (tečku) na zvýrazněné položce pro její označení nebo zrušení označení. NVDA oznámí změnu a řádek označené položky je označen jako „(označeno)“, aby byl její stav jasný při procházení seznamu.
- Stisknutím **`Shift+Home`** označíte nebo odznačíte všechny položky od aktuální až po první položku v seznamu, nebo **`Shift+End`** totéž dolů po poslední položku. Zda bude rozsah označen nebo odznačen, se rozhoduje podle aktuálního stavu aktuální položky, takže se celý rozsah vždy v jednom kroku pohybuje stejným směrem. Fokus se poté přesune na vzdálenější konec rozsahu a NVDA oznámí, kolik položek se změnilo.
- Stiskněte **`Delete`** pro odstranění všech označených položek najednou. Pokud není nic označeno, `Delete` stále odstraní pouze aktuálně vybranou položku, jako dříve.
- Kontextová nabídka pravého tlačítka (klávesa Nabídka / `Shift+F10`) každého seznamu obsahuje příkaz **Odstranit vybrané**, aktivní pouze tehdy, je-li označena alespoň jedna položka, který dělá totéž.
- Před jakýmkoli odstraněním se zobrazí jedno potvrzovací dialogové okno shrnující, kolik položek bude odstraněno.

Označení jsou specifická pro každý seznam a po odstranění položek (nebo jejich jednotlivém odznačení) se vymažou; mezi relacemi se neukládají.

### Export a import oblíbených stanic

Záložka Oblíbené obsahuje dvě tlačítka pro zálohu a obnovu seznamu stanic:

**Exportovat oblíbené…** — uloží celý seznam oblíbených do souboru. V dialogu uložení si můžete vybrat ze dvou formátů:
- **JSON** (`.json`) — úplná záloha zachovávající názvy stanic, adresy URL streamů a veškerá metadata. Doporučeno pro pozdější obnovu seznamu nebo jeho přenos na jiný počítač.
- **Playlist M3U** (`.m3u`) — standardní formát playlistu kompatibilní s většinou mediálních přehrávačů a rozhlasových aplikací. Upozorňujeme, že M3U neukládá všechna metadata stanice, takže obnova z M3U může mít méně podrobností než záloha JSON.

**Importovat oblíbené…** — načte stanice z dříve exportovaného souboru JSON nebo M3U. Po výběru souboru se zobrazí dotaz, jak stanice přidat:
- **Ano (sloučit)** — přidá importované stanice do stávajícího seznamu bez odebrání aktuálních oblíbených. Duplicitní stanice se nepřidávají dvakrát.
- **Ne (nahradit)** — zcela vymaže aktuální seznam oblíbených a nahradí ho obsahem importovaného souboru.
- **Zrušit** — vrátí se do prohlížeče bez provedení jakýchkoli změn.

Po úspěšném importu se automaticky obnoví seznam oblíbených, seznam stanic naplánovaných nahrávání a seznam stanic časovače.

### Organizace oblíbených do skupin

Oblíbené mohou patřit do složky/skupiny, což se v seznamu zobrazuje jako přípona „— Skupina" za názvem stanice (například „NPR Newscast — NPR").

- **Import z M3U** — pokud soubor používá značku `group-title` (konvence používaná programem DVBViewer a většinou ostatních editorů a přehrávačů M3U) k organizaci stanic do složek, freeAudio ji přečte a při importu zachová skupinu každé stanice. Export oblíbených zpět do M3U zapíše stejnou značku, takže struktura složek přežije cestu tam i zpět přes freeAudio.
- **Ruční přiřazení nebo odebrání skupiny** — označte jednu nebo více oblíbených stanic pomocí `.` (viz [Označení a odstranění více položek](#označení-a-odstranění-více-položek) výše), poté zvolte **Přiřadit ke skupině…** z kontextové nabídky (klávesa Nabídka / `Shift+F10`) a zadejte název skupiny. Ponechte pole prázdné, chcete-li označené oblíbené ze skupiny odebrat. Pokud není nic označeno, příkaz se použije na aktuálně vybranou oblíbenou stanici.
- **Filtrování podle skupiny** — pole Filtr nad seznamem oblíbených odpovídá také názvům skupin a přijímá více slov, z nichž každé může odpovídat jinému poli. Například zadání `Houston Classical` najde „Houston Public Media Classical", i když se tato přesná fráze nikde nevyskytuje — „Houston" odpovídá skupině a „Classical" odpovídá názvu stanice.

### Změna pořadí oblíbených stanic

Když je na kartě Oblíbené vybrána stanice, stisknutím tlačítka `čárka` přejděte do režimu přesunu - ozve se pípnutí. Pomocí šipek přejděte na cílovou pozici a znovu stiskněte `čárku`. Stanice se umístí na zvolenou pozici a nové nastavení se okamžitě uloží. Dalším stisknutím `čárky` na stejné pozici se přesun zruší.

### Přímé klávesové zkratky pro oblíbené stanice

Každá stanice v seznamu oblíbených je zaregistrována jako samostatný skript v dialogovém okně Vstupní gesta NVDA, v kategorii **freeAudio Stations**. Libovolné stanici můžete přiřadit klávesovou zkratku a stisknout ji odkudkoli — bez nutnosti otevírat okno prohlížeče.

Přiřazení klávesové zkratky:

1. Otevřete nabídku NVDA → Předvolby → Vstupní gesta.
2. Rozbalte kategorii **freeAudio Stations**.
3. Vyhledejte stanici podle názvu, vyberte ji a stiskněte **Přidat**.
4. Stiskněte požadovanou kombinaci kláves a potvrďte.

Po stisknutí zkratky se stanice okamžitě spustí. Pokud stanici odeberete z oblíbených, její položka z kategorie zmizí a případná přiřazená zkratka se automaticky odstraní. Když do oblíbených přidáte novou stanici, ihned se v kategorii zobrazí — není třeba znovu otevírat dialog Vstupní gesta.

### Přidání vlastní stanice

Chcete-li přidat stanici, která se nenachází v Prohlížeči rádií, použijte tlačítko Přidat vlastní stanici. V zobrazeném dialogovém okně zadejte název stanice a adresu URL streamu a přidejte ji přímo mezi oblíbené. Vlastní stanice lze přehrávat a měnit jejich pořadí stejně jako ostatní oblíbené stanice.

V tomto dialogovém okně jsou k dispozici dvě další tlačítka:

- **Otestovat adresu URL** — před přidáním stanice zkontroluje zadanou adresu URL streamu a oznámí, zda je dostupná. Užitečné pro zachycení překlepu nebo nefunkčního odkazu dříve, než skončí ve vašem seznamu oblíbených.
- **Přidat do adresáře Radio Browser…** — otevře [stránku pro odeslání do Radio Browser](https://www.radio-browser.info/add) ve výchozím prohlížeči, abyste mohli stanici po ověření její funkčnosti sdílet se širší komunitou Radio Browser. Co formulář pro odeslání očekává, najdete výše v části Přidání stanice do aplikace Radio Browser.

### Zvukový profil stanice

Karta Oblíbené obsahuje dvě tlačítka pro správu nastavení zvuku jednotlivých stanic:

**Uložit zvukový profil pro tuto stanici** - uloží aktuální úroveň hlasitosti, aktivní efekty a hodnoty zesílení EQ jako profil vázaný na danou stanici. Kdykoli tato stanice začne přehrávat, automaticky se použijí její uložené hlasitost, efekty a nastavení zesílení, které jsou nadřazeny globálnímu výchozímu nastavení.

**Vymazat zvukový profil** - odstraní uložený zvukový profil z vybrané stanice. Po vymazání se stanice vrátí ke globálnímu nastavení hlasitosti, efektů a zesílení EQ. Toto tlačítko je aktivní pouze v případě, že vybraná stanice již má uložený profil.

Obě tlačítka se nacházejí pod seznamem oblíbených stanic a jsou aktivní pouze v případě, že je vybrána stanice ze seznamu.

## Rozpoznávání hudby

Třikrát stisknete klávesy `Ctrl+Win+I`, čímž spustíte rozpoznávání hudby založené na technologii Shazam pro aktuálně přehrávaný stream. Rozpoznávání se spustí pouze v případě, že nejsou k dispozici metadata ICY (informace o skladbě vysílané stanicí); pokud jsou metadata přítomna, zkopírují se místo toho do schránky.

Rozpoznávání funguje následovně: pomocí ffmpeg se ze streamu zachytí krátký zvukový vzorek, aplikuje se algoritmus otisků Shazam a výsledek se odešle na servery Shazam. Pokud je rozpoznání úspěšné, NVDA oznámí název skladby, interpreta, album a rok vydání a automaticky je zkopíruje do schránky. Pokud je povolena možnost **Uložit oblíbené skladby do textového souboru**, je výsledek rozpoznání rovněž připojen do souboru `likedSongs.txt`.

**Zvuková zpětná vazba:** Při zahájení rozpoznávání zazní dvě stoupající pípnutí a při jeho ukončení dvě klesající pípnutí. Během procesu se každé 2 sekundy ozve krátké pípnutí.

**Požadavky:** Je vyžadován soubor ffmpeg.exe. Automaticky se použije soubor ffmpeg.exe umístěný ve složce doplňku; pokud je v jiném umístění, cestu k němu lze nastavit v Nastavení. Stáhněte si soubor ffmpeg ze stránek [ffmpeg.org](https://ffmpeg.org/download.html).

**Poznámka ke stanicím vkládajícím reklamy:** některé stanice přehrávají krátkou reklamu při každém novém připojení ke svému streamu, oddělenou od vysílání, které již posloucháte. Rozpoznávání se vyhýbá vzorkování této reklamy tím, že místo otevření nového připojení znovu použije stávající připojení FreeRadia k datovému toku na pozadí (stejné, jaké se používá pro Časový posun) — díky tomu rozpozná to, co skutečně hraje, a ne reklamu. Toto funguje automaticky a nevyžaduje žádné nastavení.

## Zrcadlo zvuku

Klávesová zkratka `Ctrl+Win+M` zrcadlí aktuálně přehrávaný datový tok na druhé výstupní zvukové zařízení současně. To je užitečné pro poslech na dvou různých zařízeních současně, například na reproduktorech a sluchátkách.

Při prvním stisknutí se zobrazí dialogové okno výběru se seznamem dostupných výstupních zařízení. Po výběru zařízení se zahájí zrcadlení a hlavní přehrávání pokračuje bez přerušení. Dalším stisknutím zkratky se zrcadlení zastaví.

**Případy použití:**
- **Reproduktory + sluchátka** - Nechte hosta sledovat stejné vysílání na sluchátkách, zatímco vy budete poslouchat přes reproduktory počítače.
- **Nastavení nahrávání** - Hlavní výstup nasměrujte do reproduktorů a druhý výstup do externího rekordéru nebo zvukového rozhraní pro externí nahrávání.
- **Více místností** - Přehrávejte současně přes reproduktor Bluetooth a vestavěný reproduktor; k přenosu zvuku do jiné místnosti není třeba žádný další software.
- **Vzdálené monitorování** - Při sdílení obrazovky nebo relaci vzdálené plochy může místní i vzdálená strana slyšet stejný stream současně.

## Režim hudby na pozadí (Obligato)

Klávesová zkratka `Ctrl+Win+Shift+M` přehrává oblíbenou stanici tiše na pozadí, a to na zcela samostatném zvukovém enginu odděleném od hlavního přehrávače - jako jemná hudební kulisa běžící pod tím, co právě děláte.

Při prvním stisknutí se otevře dialogové okno se třemi ovládacími prvky:

- **Stanice na pozadí** - seznam vašich oblíbených stanic, ze kterého vyberete, která se bude na pozadí opakovaně přehrávat. Vyžaduje alespoň jednu oblíbenou položku; pokud je váš seznam oblíbených prázdný, freeAudio vás vyzve, abyste nejprve přidali stanici (`Ctrl+Win+V` během přehrávání stanice).
- **Zvukový výstup** - přes které zařízení se stanice na pozadí přehrává: **Stejné jako hlavní výstup** (výchozí), **Výchozí zařízení systému**, nebo libovolné konkrétní zařízení, které freeAudio dokáže rozpoznat.
- **Hlasitost na pozadí** - jak hlasitě se stanice na pozadí přehrává, vyjádřeno jako procento aktuální hlasitosti hlavního přehrávače (25 %, 50 %, 75 %, 100 %, 125 % nebo 150 %). Vaše volby se uloží pro příště.

Po spuštění pokračuje stanice na pozadí v přehrávání nezávisle na hlavním přehrávači - přepnutí stanice, podcastu nebo audioknihy v hlavním přehrávači, nebo jeho úplné zastavení, režim Obligato nijak nepřeruší. Automaticky zůstávají s hlavním přehrávačem propojené dvě věci:

- **Hlasitost** - hlasitost na pozadí je průběžně udržována na zvoleném procentu aktuální hlasitosti hlavního přehrávače, takže zvýšení nebo snížení hlavní hlasitosti (`Ctrl+Win+↑`/`↓`) stejným poměrem změní i hudbu na pozadí.
- **Pozastavení** - pozastavení hlavního přehrávače (`Ctrl+Win+P`) pozastaví i stanici na pozadí a obnovení hlavního přehrávače ji zase obnoví. Úplné zastavení hlavního přehrávače se za pozastavení nepovažuje, takže stanice na pozadí hraje dál.

Kdykoli režim Obligato zastavíte opětovným stisknutím `Ctrl+Win+Shift+M`.

## Nahrávání

Nahrávky se ve výchozím nastavení ukládají do složky `Dokumenty\freeAudio Recordings\`. Název souboru obsahuje název stanice (nebo název skladby v režimu nahrávání skladeb) a čas zahájení nahrávání. Složku nahrávek lze kdykoli změnit v nabídce NVDA → Předvolby → Nastavení → freeAudio → **Složka nahrávek**.

Nastavení **Výstupní formát nahrávky** určuje, jak se dokončené nahrávky ukládají:
- **Původní formát streamu** zapíše stream přesně tak, jak byl přijat. Vysílání HLS tak může vytvořit soubor `.ts`.
- **Pouze zvuk, původní kodek** odstraní vrstvu videa/kontejneru, aniž by přeekódoval zvuk. Například zvuk AAC z nahrávky HLS `.ts` se obvykle uloží jako `.m4a` při zachování kvality vysílání.
- **MP3** převede zvuk po nahrání pomocí zvoleného datového toku. Převod používá `ffmpeg.exe` dodávaný s FreeRadiem a probíhá na pozadí, aby NVDA zůstalo responzivní. Pokud převod selže, zachová se původní nahrávka.

**Okamžité nahrávání:** Během přehrávání stanice stiskněte jednou klávesy `Ctrl+Win+E`. Dalším stisknutím nahrávání zastavíte. Přehrávání pokračuje po celou dobu bez přerušení.

**Nahrávání skladby:** Během přehrávání stanice, která vysílá metadata ICY, stiskněte dvakrát po sobě tlačítko `Ctrl+Win+E`. Nahrávání se spustí okamžitě a je pojmenováno podle názvu aktuální skladby. Při změně skladby se nahrávání automaticky zastaví a NVDA oznámí název uloženého souboru. Pokud chcete nahrávání ukončit dříve, než skladba skončí, stiskněte znovu dvakrát klávesy `Ctrl+Win+E`. Pokud aktuální stanice nevysílá metadata ICY, nahrávání skladby není k dispozici a NVDA vás o tom informuje.

**Naplánované nahrávání:** V prohlížeči otevřete kartu Nahrávání. Vyberte stanici z oblíbených, zadejte čas začátku ve formátu HH:MM a dobu trvání v minutách, vyberte jeden nebo více aktivních dnů a nastavte režim opakování a nahrávání:

Pole **Filtr** nad seznamem stanic vám umožní v reálném čase zúžit seznam oblíbených, takže rychle najdete stanici, kterou chcete naplánovat.

**Aktivní dny:** Zaškrtněte jeden nebo více dní v týdnu. V jednorázovém režimu se pro každý vybraný den vytvoří samostatná položka plánování; každá položka se nastaví na nejbližší příští výskyt daného dne. V opakujícím se režimu se nahrávání opakuje pouze ve vybraných dnech. Pokud nejsou vybrány žádné dny, nahrávání není omezeno na konkrétní dny.

**Režim opakování:**
- **Nahrát jednou** — vytvoří jednorázové nahrávání pro každý vybraný den. Každá položka se nastaví na nejbližší příští výskyt daného dne; pokud dnešní čas již uplynul, položka se automaticky přesune na příští týden.
- **Opakovat každý týden** — opakuje se každý týden ve vybraných aktivních dnech, dokud není odstraněno ze seznamu plánování.

**Uložit nahrávku do:** Pro každé naplánované nahrávání si můžete vybrat uložení do výchozí složky nahrávek nebo do vlastní složky. Pomocí tlačítka **Procházet...** vyberte složku interaktivně. Pokud se zvolená složka stane nedostupnou, nahrávka se uloží do výchozí složky a budete o tom informováni.

**Režim nahrávání:**
- **Nahrávat při poslechu** — přehrává a nahrává současně prostřednictvím backendu BASS.
- **Pouze nahrávání** — nahrává tiše na pozadí bez jakéhokoli zvukového výstupu; nahrávací engine se připojuje přímo ke streamu.

Po přidání plánu se zobrazí v seznamu níže. Pomocí tlačítka **Odebrat vybrané** smažete plán, nebo **Upravit vybrané** upravíte jeho čas, trvání, opakování, aktivní dny, režim nahrávání nebo výstupní složku.

NVDA oznámí, kdy nahrávání začne a kdy skončí. Pokud je NVDA restartována v průběhu plánovaného nahrávání, nahrávání se při spuštění automaticky obnoví.

Stejně jako u rozpoznávání hudby, i okamžité nahrávání a nahrávání skladby znovu použijí stávající připojení FreeRadia k datovému toku na pozadí, pokud je k dispozici, místo otevření nového — nahrávka tak zachytí to, co skutečně hraje, i u stanic, které by jinak novému připojení nabídly čerstvou reklamu. Toto se nevztahuje na plánovaná nahrávání v režimu **Pouze nahrávání**, protože v okamžiku jejich spuštění ještě žádná stanice nehraje.

## Časový posun (přetočení živého rádia)

Časový posun umožňuje přetočit aktuálně poslouchanou stanici jako DVR nebo kazetový přehrávač — zastavte okamžik, vraťte se o několik minut zpět a dožeňte živé vysílání, kdy chcete. Přehrávání se přitom nemusí zastavit: přetočení zpět i dopředu probíhá okamžitě na stejném zvukovém streamu.

Tato funkce je **ve výchozím nastavení vypnutá**. Zapněte ji v NVDA Menu → Předvolby → Nastavení → freeAudio → **Zapnout vyrovnávací paměť časového posunu (přetočení živého rádia)**, nebo ji kdykoli okamžitě přepněte pomocí `Ctrl+Win+T`.

> **Poznámka:** freeAudio nyní neustále udržuje malé zachytávání aktuálně přehrávané stanice na pozadí — nejen když je toto nastavení zapnuté — protože Rozpoznávání hudby i Nahrávání se na něj spoléhají kvůli chování vyhýbajícímu se reklamám popsanému v těchto částech. Když je toto nastavení **vypnuté**, toto zachytávání na pozadí se drží na přibližně posledních 45 sekundách a `Ctrl+Win+J`/`Ctrl+Win+K` zůstávají nedostupné — mění se pouze velikost vyrovnávací paměti, ne to, zda běží. Zapnutím tohoto nastavení se stejné zachytávání zvětší na plnou vyrovnávací paměť pro přetáčení popsanou níže.

### Jak to funguje

Po zapnutí freeAudio nepřetržitě zachytává aktuálně přehrávanou stanici do místní průběžné vyrovnávací paměti na pozadí. Ta pojme zhruba **posledních 10 minut** zvuku; starší audio je automaticky odstraňováno z čela fronty s příchodem nového, takže vyrovnávací paměť vždy představuje „nedávnou minulost" vzhledem k živé hraně. Doba vyrovnávací paměti je určena v nastavení.

- **`Ctrl+Win+J`** — Přetočit o 15 sekund zpět. První stisk přepne z živého přehrávání do přehrávání s časovým posunem, přičemž začíná 15 sekund za živou hranou. Každý další stisk posune o dalších 15 sekund zpět, až do limitu vyrovnávací paměti.
- **`Ctrl+Win+K`** — Přetočit o 15 sekund dopředu v režimu časového posunu. Po dosažení živé hrany se přehrávání automaticky přepne zpět na živý stream a NVDA oznámí „Zpět na živé vysílání".
- **`Ctrl+Win+T`** — Celou funkci zapne nebo vypne. Vypnutí v režimu časového posunu okamžitě vrátí na živé vysílání a zastaví zachytávání na pozadí pro aktuální stanici.

Zachytávání na pozadí běží celou dobu, kdy je aktivní časový posun, takže živá hrana pokračuje dopředu, i když posloucháte něco z několik minut staré záznamu — přesně jako skutečný DVR.

### Zapnutí a zahřátí vyrovnávací paměti

Vyrovnávací paměť se začne plnit, jakmile stanice začne hrát (pokud je funkce zapnuta), nebo v okamžiku, kdy funkci zapnete za poslechu stanice. Proto je přetočení možné teprve po skutečném zachycení několika sekund zvuku — pokud stisknete `Ctrl+Win+J` ihned po přepnutí stanic, NVDA vás upozorní, že ve vyrovnávací paměti zatím není dostatek zvuku. Stačí chvíli počkat a zkusit znovu.

Přepnutí na jinou stanici vždy restartuje vyrovnávací paměť pro novou stanici; zvuk předchozí stanice je zahozen.

### Podporované streamy

Časový posun funguje se stejným rozsahem streamů, které freeAudio již podporuje:

- Obyčejné HTTP/HTTPS streamy (MP3, AAC, OGG atd.), včetně serverů ve stylu Shoutcast/Icecast.
- **HLS (`.m3u8`) streamy** — freeAudio přeloží hlavní playlist stanice, sleduje mediální playlist a stahuje segmenty na pozadí, aby udržela vyrovnávací paměť plnou.

V ojedinělém případě, kdy playlist stanice vůbec nelze přečíst (například poškozený nebo nedostupný manifest `.m3u8`), NVDA sdělí, že přetočení pro danou stanici není k dispozici.

### Požadavky a omezení

- **Vyžaduje backend BASS**, který freeAudio vždy používá pro přehrávání (viz [Přehrávání](#přehrávání)).
- Doba vyrovnávací paměti je určena v nastavení.
- Vyrovnávací paměť je na každou stanici zvlášť: přepnutí stanic, zastavení přehrávání nebo restart NVDA ji vynuluje.
- Přehrávání s časovým posunem používá vlastní místní soubor vyrovnávací paměti a nevytváří uloženou nahrávku — pokud chcete zvuk trvale uchovat, použijte zároveň Okamžité nahrávání (`Ctrl+Win+E`).

## Časovač

Otevřete kartu Časovač v prohlížeči stanice (`Alt+4`). Lze přidat dva typy časovače:

Při výběru stanice pro časovač alarmu vám pole **Filtr** nad seznamem stanic umožní v reálném čase zúžit seznam oblíbených.

**Alarm - spuštění rádia:** Automaticky začne v zadaný čas přehrávat vybranou stanici z oblíbených. Vyberte stanici a zadejte čas ve formátu HH:MM.

**Sleep - zastavení rádia:** Zastaví přehrávání v zadaný čas. Po spuštění časovače se hlasitost postupně snižuje po dobu 60 sekund, než se přehrávání zastaví. Není třeba vybírat žádnou stanici, stačí zadat čas.

Platí pro oba typy, pokud zadaný čas již uplynul, je akce naplánována na následující den. Pokud již existuje časovač ve stejnou dobu (bez ohledu na typ), přidání nového časovače je zablokováno; uživatel je informován o konfliktu a vyzván k odebrání stávající položky. Na kartě jsou uvedeny čekající časovače; vyberte jeden z nich a stisknutím tlačítka Odebrat vybraný časovač jej zrušte.

**Opakované časovače:** V části **Opakování** zvolte **Opakovat každý týden** místo výchozí jednorázové možnosti, aby se časovač spouštěl každý týden, nikoli jednou. Seznam zaškrtávacích políček **Aktivní dny** vám pak umožní vybrat, ve které dny v týdnu se opakuje; pokud necháte všechny dny nezaškrtnuté, opakuje se každý den. Opakovaný časovač se spouští podle plánu, dokud jej neodstraníte ze seznamu čekajících časovačů — nejde o jednorázovou položku, která po spuštění zmizí.

## Podcasty

freeAudio obsahuje plnohodnotný přehrávač podcastů. Můžete se přihlásit k odběru libovolného RSS nebo Atom kanálu podcastu, procházet epizody, přehrávat je, stahovat je a pokračovat v přehrávání tam, kde jste skončili — to vše plně přístupně.

### Přístup na kartu Podcasty

Otevřete Průzkumníka stanic pomocí `Ctrl+Win+R` a přepněte na kartu **Podcasty** pomocí `Ctrl+Tab` nebo `Alt+6`. Karta je rozdělena do tří hlavních oblastí:

1. **Hledat a přidat** — horní část pro objevování nových podcastů, včetně seznamu náhledu, který zobrazuje epizody právě vybraného výsledku hledání.
2. **Odběry** — seznam kanálů, které odebíráte.
3. **Epizody** — seznam epizod vybraného kanálu s ovládacími prvky přehrávání.

### Přidání kanálu podcastu

Kanál podcastu můžete přidat dvěma způsoby:

**Podle adresy URL:**
- **Hledat** vložte úplnou adresu URL kanálu RSS nebo Atom (např. `https://example.com/feed.xml`).
- Stiskněte Enter.
- freeAudio kanál načte, ověří a přidá jej do vašich odběrů. Pokud je kanál platný, uslyšíte potvrzení s názvem kanálu. Pokud se to nezdaří, chybová zpráva vysvětlí důvod.

**Vyhledáváním:**
- Do pole **Hledat** zadejte klíčové slovo (název podcastu, téma nebo jméno moderátora) a stiskněte Enter.
- freeAudio prohledá adresář podcastů iTunes a zobrazí odpovídající podcasty v seznamu **Výsledky hledání**.
- Výběrem výsledku se daný kanál na pozadí načte a jeho epizody se zobrazí v seznamu **Epizody vybraného výsledku** hned pod ním, takže si můžete prohlédnout, co pořad skutečně obsahuje, než se rozhodnete pro odběr — viz níže část Náhled epizod před přihlášením k odběru.
- Jakmile jste s tím, co vidíte, spokojeni, vyberte výsledek a buď stiskněte `Enter`, nebo otevřete jeho kontextovou nabídku (klávesa Nabídka / `Shift+F10`, případně kliknutí pravým tlačítkem) a zvolte **Přihlásit k odběru**, čímž jej přidáte do svých odběrů. Kanál se přidá okamžitě a zobrazí se v seznamu odběrů. Neexistuje samostatné tlačítko „Přidat vybrané z hledání" — jediným způsobem přihlášení k odběru z výsledků hledání je `Enter` nebo kontextová nabídka, což udržuje rozhraní jednoduché a přístupné.

> **Tip:** Do pole hledání můžete zadat i přímo adresu URL kanálu — pokud vypadá jako platná adresa URL, doplněk se ji pokusí přidat jako kanál bez hledání.

**Kontextová nabídka pro výsledky hledání:** Klepnutím pravým tlačítkem na výsledek hledání, případně jeho vybráním a stiskem klávesy Nabídka / `Shift+F10`, otevřete nabídku s jedinou akcí **Přihlásit k odběru**, totožnou se stisknutím `Enter` na daném výsledku.

### Náhled epizod před přihlášením k odběru

Před přihlášením k odběru si můžete poslechnout epizody podcastu přímo z výsledků hledání. Kdykoli vyberete podcast v seznamu **Výsledky hledání**, freeAudio daný kanál načte a jeho epizody — název a datum vydání — zobrazí v seznamu **Epizody vybraného výsledku** níže.

- Vyberte epizodu v tomto náhledovém seznamu a stiskněte `Enter`, nebo otevřete její kontextovou nabídku (klávesa Nabídka / `Shift+F10`, případně kliknutí pravým tlačítkem) a zvolte **Náhled**, čímž ji začnete přehrávat pomocí běžného přehrávače. Všechny obvyklé ovládací prvky přehrávání (pozastavení, hlasitost, časový posun atd.) na ní fungují stejně jako na jakékoli jiné stanici nebo epizodě.
- Během náhledu epizody se ve stejné kontextové nabídce místo **Náhled** zobrazí **Zastavit náhled** — zvolte jej, nebo znovu stiskněte `Enter` na dané epizodě, čímž náhled zastavíte.
- Náhled vás k ničemu nepřihlašuje; slouží čistě k poslechu před rozhodnutím. Samotný seznam náhledu je dočasný — nahradí se, jakmile vyberete jiný výsledek hledání, a neukládá se nikam trvale tak jako vaše skutečné odběry.

### Správa odběrů

Jakmile přidáte několik kanálů, zobrazí se v seznamu **Odběry**. Každá položka zobrazuje název kanálu a počet dostupných epizod.

- **Vyberte kanál**, chcete-li zobrazit jeho epizody ve spodním seznamu. Textové pole pouze pro čtení **Podrobnosti o kanálu** pod seznamem odběrů zobrazuje název kanálu, autora, popis, počet epizod a adresu URL.
- **Obnovte kanál** — vyberte jej a stiskněte tlačítko **Obnovit kanál** (dostupné také přes kontextovou nabídku, viz níže), abyste načetli nejnovější epizody. Všechny kanály se také automaticky obnovují na pozadí při otevření karty Podcasty, takže obvykle vidíte nejnovější epizody bez ručního zásahu.
- **Odeberte kanál** — vyberte jej a stiskněte `Delete`, nebo jej odeberte ze svých odběrů pomocí kontextové nabídky. Před odebráním budete požádáni o potvrzení.

**Kontextová nabídka pro kanály:** Klepnutím pravým tlačítkem na kanál, případně jeho vybráním a stiskem klávesy Nabídka / `Shift+F10`, otevřete nabídku s těmito položkami:
- **Obnovit kanál** — nyní načte nové epizody.
- **Uložit zvukový profil pro tento podcast** / **Vymazat zvukový profil** — viz [Zvukový profil podcastu](#zvukový-profil-podcastu) níže.
- **Odebrat kanál** — smaže odběr.
- **Kopírovat adresu URL kanálu** — zkopíruje adresu URL kanálu do schránky.

### Procházení a přehrávání epizod

Vyberte kanál v seznamu odběrů; jeho epizody se zobrazí v seznamu **Epizody** níže. Každá epizoda zobrazuje:
- Své číslo epizody (1 = nejstarší epizoda v kanálu, číslováno vzestupně k nejnovější).
- Datum vydání (je-li k dispozici).
- Svůj název.
- Předponu **„Přehráno"**, pokud byla epizoda přehrána celá.
- Příponu s délkou: buď celkovou délku (pokud ještě nebyla přehrána), nebo uplynulý/celkový průběh (pokud byla přehrána částečně).

**Přehrávání:**
- Vyberte epizodu a stiskněte `Enter` nebo `Mezerník` pro zahájení přehrávání. Pokud byla epizoda dříve přehrána částečně, pokračuje tam, kde jste skončili.
- Řádek se během přehrávání epizody *neaktualizuje* — to je záměrné, aby NVDA opakovaně neohlašoval řádek, zatímco na něm setrváváte. Jeho příznak „Přehráno" a délka se aktualizují okamžitě ve chvíli, kdy epizodu pozastavíte nebo skončí přehrávání, takže zobrazení je vždy přesné právě ve chvíli, kdy na tom záleží; jen se neaktualizuje vteřinu po vteřině během přehrávání.
- Použijte `F3` / `F4` na kartě Podcasty pro přechod na předchozí / další epizodu a její okamžité přehrání. Můžete také použít `←` / `→`, když je zaměřen seznam epizod, nebo `Ctrl+←` / `Ctrl+→` kdekoli na kartě Podcasty — obojí funguje stejně.
- Použijte `Shift+F3` / `Shift+F4` pro přechod mezi kanály bez přehrávání epizod.
- Stiskněte `Mezerník` během přehrávání epizody pro pozastavení nebo obnovení přehrávání.

**Pokračování v přehrávání:** freeAudio automaticky ukládá vaši pozici v každé epizodě podcastu — okamžitě při pozastavení nebo dokončení epizody a dále každých 15 sekund na pozadí, dokud posloucháte, takže pád nebo neočekávané restartování nezpůsobí velkou ztrátu postupu. Pokud přehrávání zastavíte nebo pozastavíte a vrátíte se později, epizoda pokračuje od uložené pozice. Pokud epizodu přehrajete až do samého konce (v posledních 3 sekundách), označí se jako **„Přehráno"** a nebude pokračovat — příště začne od začátku a v seznamu se zobrazí předpona „Přehráno".

**Kontextová nabídka pro epizody:** Klepnutím pravým tlačítkem na epizodu, případně jejím vybráním a stiskem klávesy Nabídka / `Shift+F10`, otevřete nabídku s těmito položkami:
- **Přehrát epizodu** — zahájí přehrávání.
- **Stáhnout epizodu** — stáhne soubor epizody do vaší složky nahrávek.
- **Uložit zvukový profil pro tento podcast** / **Vymazat zvukový profil** — stejné příkazy jako ve vlastní kontextové nabídce kanálu, dostupné i zde pro pohodlí, abyste se nemuseli vracet do seznamu odběrů. Vždy ukládají jeden profil pro celý podcast, ne samostatný profil pro tuto epizodu — viz [Zvukový profil podcastu](#zvukový-profil-podcastu) níže.
- **Kopírovat adresu URL epizody** — zkopíruje přímou adresu URL zvuku do schránky.

### Stahování epizod

Vyberte epizodu a klikněte na tlačítko **Stáhnout epizodu** (nebo použijte kontextovou nabídku). Epizoda se stáhne do vaší složky nahrávek (`Dokumenty\freeAudio Recordings\` ve výchozím nastavení). Název souboru vychází z názvu epizody a zjištěné přípony souboru (`.mp3`, `.m4a`, `.ogg` atd.). NVDA oznámí zahájení a dokončení stahování. Pokud soubor již existuje, budete informováni a stahování se přeskočí.

### Filtrování epizod

Nad seznamem epizod je pole **Filtr**. Během psaní se seznam epizod okamžitě filtruje tak, aby zobrazoval epizody, jejichž název obsahuje zadaný text, nebo jejichž číslo epizody se s ním přesně shoduje — takže zadání `47` vás okamžitě přesune na epizodu 47, i když se „47" v jejím názvu nikde neobjevuje. NVDA po každé změně oznámí počet odpovídajících epizod. Stisknutím šipky dolů v poli filtru přesunete fokus přímo do filtrovaného seznamu.

### Podrobnosti o přehrávání podcastů

Epizody podcastů se přehrávají pomocí **backendu BASS** (stejný engine, který se používá pro rozhlasové streamy a od této verze jediný backend, který freeAudio používá). Protože se epizody stahují postupně a lze v nich posouvat, můžete při přehrávání podcastu použít klávesové zkratky časového posunu vzad/vpřed (`Ctrl+Win+J`/`Ctrl+Win+K`) k posouvání v rámci epizody. Pozice se automaticky ukládá, takže můžete později pokračovat.

**Odstupňované posouvání:** Na rozdíl od pevného 15sekundového přetočení u živého rádia se posouvání v rámci podcastu, audioknihy nebo skladby jukeboxu odstupňovává podle způsobu stisku klávesy, takže můžete provést malou opravu nebo skočit o velký kus bez opakovaného stiskávání:

- **Podržení klávesy** (automatické opakování) posouvá o **5 sekund** za opakování — stejné malé množství, jaké tato zkratka vždy používala u souborů.
- **Jedno záměrné stisknutí** posune o **12 sekund**.
- **Dvě stisknutí** za sebou v rychlém sledu posunou o **1 minutu**.
- **Tři a více stisknutí** posune o **5 minut**; další stisknutí ve stejné sérii už dál neeskalují.

Záměrné stisknutí se krátce podrží, než se posun skutečně provede, pro případ, že přijde další stisknutí - k posunu dojde pouze jednou za sérii stisknutí, o velikosti odpovídající celkovému počtu stisknutí, nikoli součtu jednotlivých hodnot. Po posunu NVDA oznámí výslednou uplynulou/zbývající pozici v epizodě, nikoli jen „X sekund vpřed/vzad".

**Rychlost přehrávání:** Rychlost přehrávání epizod podcastů, audioknih a skladeb jukeboxu můžete upravit pomocí `Ctrl+Win+Shift+K` (rychleji) a `Ctrl+Win+Shift+J` (pomaleji). Rychlost se mění v krocích po 0,1× v rozsahu od 0,5× do 2,0×, se zachováním výšky tónu.

**Transpozice (posun výšky tónu):** Nezávisle na rychlosti přehrávání můžete posunout výšku tónu epizody podcastu, audioknihy nebo skladby jukeboxu nahoru nebo dolů pomocí `Shift+Win+K` / `Shift+Win+J` — viz [Transpozice (posun výšky tónu)](#transpozice-posun-výšky-tónu).

**Zvukový efekt při pokračování:** Kdykoli epizoda pokračuje z uložené pozice, freeAudio krátce přehraje na samostatném kanálu jemný zvukový efekt připomínající zavádění kazety, zatímco se posouvá zpět na vaše uložené místo, místo aby nechalo mezitím slyšitelně hrát vlastní zvuk epizody od 0:00. To se děje automaticky, kdykoli je aktivní backend BASS, a je to nezávislé na nastavení **Přechod při přepnutí stanice** - to nastavení ovlivňuje pouze přepínání mezi živými rozhlasovými stanicemi, nikoli pokračování podcastů nebo audioknih.

### Zvukový profil podcastu

Klepněte pravým tlačítkem na podcast v seznamu Odběry, nebo klepněte pravým tlačítkem na kteroukoli z jeho epizod, a zvolte **Uložit zvukový profil pro tento podcast**, čímž uložíte aktuální hlasitost, efekty, zisk ekvalizéru a/nebo rychlost přehrávání jako profil svázaný s tímto podcastem. Kdykoli se přehraje jakákoli epizoda tohoto podcastu, uložená nastavení se automaticky použijí a přepíší globální výchozí hodnoty. Protože je příkaz dostupný jak z kontextové nabídky kanálu, tak z kontextové nabídky epizody, můžete se k němu dostat, aniž byste se museli vracet do seznamu odběrů - v obou případech se vždy ukládá jeden profil pro celý podcast, ne samostatný profil pro každou epizodu.

Dialogové okno s 15 možnostmi vám umožní vybrat přesně, co chcete uložit:
- **Pouze hlasitost**
- **Pouze efekty**
- **Hlasitost a efekty**
- **Hlasitost a rychlost přehrávání**
- **Efekty a rychlost přehrávání**
- **Pouze rychlost přehrávání**
- **Hlasitost, efekty a rychlost přehrávání**
- **Pouze transpozice**
- **Hlasitost a transpozice**
- **Efekty a transpozice**
- **Rychlost přehrávání a transpozice**
- **Hlasitost, efekty a transpozice**
- **Hlasitost, rychlost přehrávání a transpozice**
- **Efekty, rychlost přehrávání a transpozice**
- **Hlasitost, efekty, rychlost přehrávání a transpozice**

Do profilu se zapíší pouze vybrané položky; cokoli, co vynecháte, si ponechá to, co v něm již bylo uloženo. Například výběrem možnosti **Pouze rychlost přehrávání** u podcastu, který již má uložený profil hlasitosti/efektů, aktualizujete pouze rychlost a zbytek zůstane nedotčen.

**Vymazat zvukový profil** odstraní uložený profil z podcastu, z kterékoli z obou nabídek. Je aktivní pouze tehdy, když má podcast aktuálně uložený profil.

### Ukládání dat podcastů

Vaše odběry se ukládají do souboru `freeAudio_podcasts.json` ve složce uživatelské konfigurace NVDA. Pozice epizod se ukládají samostatně do souboru `podcast_positions.json` na stejném místě. Oba soubory jsou ve formátu prostého JSON a lze je zálohovat nebo přenést do jiného počítače.

## Audioknihy (GETEM, LibriVox a Project Gutenberg)

freeAudio obsahuje přehrávač audioknih, který vyhledává, přehrává a stahuje knihy ze tří zdrojů:

- **[GETEM](https://getem.boun.edu.tr/)** - digitální knihovna provozovaná Centrem pro zrakově postižené Univerzity Boğaziçi. Ke streamování nebo stažení zvuku knihy vyžaduje bezplatné členství (procházení nikoli) - viz [Přihlášení](#přihlášení) níže.
- **[LibriVox](https://librivox.org/)** - projekt audioknih z veřejné domény čtených dobrovolníky. Není potřeba žádný účet ani přihlášení; celý jeho katalog, včetně samotných zvukových souborů, je veřejnou doménou a volně dostupný.
- **Kolekce otevřených audioknih Project Gutenberg** - audioknihy z veřejné domény namluvené lidmi i počítačem, hostované na [archive.org](https://archive.org/), doplněk textové knihovny Project Gutenberg. Stejně jako LibriVox nevyžaduje žádný účet ani přihlášení.

Výsledky ze všech tří zdrojů se zobrazují společně v jednom sloučeném seznamu **Výsledky hledání** a jednom sloučeném seznamu **Knihovna** - není zde žádná samostatná karta ani rozevírací nabídka pro přepínání mezi nimi. Zdroj každé knihy (GETEM, LibriVox nebo Project Gutenberg) je zobrazen jako popisek vedle jejího názvu a v jejích podrobnostech, takže vždy poznáte, na kterou se díváte. Knihy z kteréhokoli zdroje můžete vyhledávat, prohlížet náhled, přidávat, přehrávat a stahovat úplně stejným způsobem; přehrávat vícedílná díla s automatickým pokračováním napříč díly; a stahovat knihy pro poslech offline - to vše plně přístupně.

Kterýkoli ze zdrojů lze vypnout jednotlivě v **NVDA Menu → Předvolby → Nastavení → freeAudio** pomocí seznamu zaškrtávacích políček **Zdroje audioknih**, pokud chcete prohledávat pouze některé z nich. Všechny tři jsou ve výchozím nastavení zapnuté.

> **Poznámka:** Poslech knihy z GETEM vyžaduje bezplatné členství v GETEM. Procházení katalogu GETEM účet nevyžaduje, ale přeložení a přehrání zvuku knihy z GETEM ano - viz [Přihlášení](#přihlášení) níže. Knihy z LibriVox a Project Gutenberg nikdy nevyžadují účet.

### Přístup na kartu Audioknihy

Otevřete Průzkumníka stanic pomocí `Ctrl+Win+R` a přepněte na kartu **Audioknihy** pomocí `Ctrl+Tab` nebo `Alt+7`. Karta má tři hlavní oblasti:

1. **Hledat** - textové pole pro prohledání všech zapnutých katalogů najednou, se seznamem výsledků, který se zobrazí po spuštění hledání.
2. **Knihovna** - seznam knih, které jste přidali z kteréhokoli zdroje, kde je přehráváte, stahujete a spravujete.
3. **Podrobnosti** - pole pouze pro čtení zobrazující zdroj, název, autora, vypravěče, vydavatele, formát, počet dílů, popis a adresu URL katalogu vybrané knihy, v kterémkoli ze seznamů.

### Přihlášení

GETEM vyžaduje registrované členství pro streamování nebo stahování skutečného zvuku knihy, ačkoli samotný katalog lze volně prohledávat. Zadejte své uživatelské jméno a heslo GETEM jednou v **NVDA Menu → Předvolby → Nastavení → freeAudio**; uloží se zašifrovaně na disk (prostřednictvím Windows Data Protection API, svázané s vaším uživatelským účtem Windows) a poté se automaticky znovu použijí. Pokud se pokusíte přehrát nebo stáhnout knihu z GETEM před zadáním přihlašovacích údajů, freeAudio vás vyzve, abyste je nejprve přidali v Nastavení.

LibriVox a Project Gutenberg nevyžadují žádný krok přihlášení - jejich výsledky a zvuk lze okamžitě vyhledávat, poslechnout jako náhled, přehrávat a stahovat, bez zadávání jakýchkoli přihlašovacích údajů.

### Vyhledávání audioknih

Zadejte hledaný výraz do pole hledání a stiskněte `Enter`. freeAudio prohledá zdroje zapnuté v Nastavení a sloučí výsledky do jednoho seznamu:

- **GETEM** se prohledává podle názvu, autora, vypravěče, tématu a vydavatele najednou, protože vlastní vyhledávací formulář GETEM podporuje zúžení podle všech těchto polí dohromady, nikoli jediné hledání napříč jedním z nich. Zobrazují se pouze díla skutečně dostupná ve zvukové podobě (lidské nebo počítačové čtení, audiopopis, rozhlasová hra, mluvené knihy DAISY atd.); braillské, velkotiskové a jiné nezvukové formáty se automaticky vyfiltrují.
- **LibriVox** se prohledává podle názvu nebo autora/čtenáře ve svém katalogu veřejné domény.
- **Project Gutenberg** se prohledává podle názvu nebo autora v kolekci otevřených audioknih na archive.org.

Vložení adresy URL stránky katalogu/podrobností knihy přímo do pole hledání (stránka katalogu GETEM nebo stránka „details“ archive.org pro knihu z LibriVox nebo Project Gutenberg) vyřeší tuto jednu knihu přímo namísto spuštění vyhledávání podle klíčových slov.

NVDA oznámí, kolik audioknih bylo celkem nalezeno.

Výběrem výsledku se zobrazí jeho podrobnosti - autor, vypravěč, vydavatel, formát a počet dílů - v poli podrobností níže.

**Náhled:** Vyberte výsledek a stiskněte `Mezerník`, nebo otevřete jeho kontextovou nabídku (klávesa Nabídka / `Shift+F10`, případně kliknutí pravým tlačítkem) a zvolte **Náhled**, čímž ji začnete přehrávat od prvního dílu, aniž byste ji přidali do knihovny. Během náhledu knihy se ve stejné kontextové nabídce místo toho zobrazí **Zastavit náhled** - zvolte jej, nebo znovu stiskněte `Mezerník`, čímž náhled zastavíte. Náhled neukládá vaši pozici poslechu, protože ta se sleduje pouze u knih již ve vaší knihovně.

**Přidání do knihovny:** Vyberte výsledek a stiskněte `Enter`, nebo použijte jeho kontextovou nabídku a zvolte **Přidat do knihovny**. freeAudio vás informuje, pokud tam kniha již je.

### Vaše knihovna

Knihy, které jste přidali, se zobrazují v seznamu **Knihovna**, s názvem, autorem a formátem. Výběrem jedné se zobrazí její podrobnosti níže.

- Stiskněte `Enter` nebo `Mezerník` pro přehrání vybrané knihy. Pokud není nic načteno, `Mezerník` ji spustí; pokud již něco hraje, `Mezerník` to místo toho pozastaví, v souladu se zbytkem přehrávače.
- Použijte `F3` / `F4` na kartě Audioknihy pro přechod na předchozí / další **knihu** ve vaší knihovně a její spuštění. `Ctrl+←` / `Ctrl+→` dělají totéž, když je zaměřen seznam knihovny.
- Použijte `Shift+F3` / `Shift+F4` pro přechod mezi **díly** aktuálně přehrávané knihy - opak karty Podcasty, kde F3/F4 přecházejí mezi epizodami a Shift+F3/F4 mezi kanály. Je to proto, že kniha je jedinou položkou knihovny i tehdy, když má více dílů, takže jemnější navigace „po dílech" je zde umístěna na klávesách se Shift.

**Kontextová nabídka pro položky knihovny:** Klepnutím pravým tlačítkem na knihu, případně jejím vybráním a stiskem klávesy Nabídka / `Shift+F10`, otevřete nabídku s těmito položkami:
- **Přehrát médium** - zahájí přehrávání, totéž co `Enter`.
- **Stáhnout knihu** - stáhne všechny díly knihy; viz [Stahování audioknih](#stahování-audioknih) níže.
- **Kopírovat adresu URL** - zkopíruje adresu URL stránky katalogu knihy do schránky (stránku katalogu GETEM u knihy z GETEM, nebo stránku podrobností archive.org u knihy z LibriVox nebo Project Gutenberg).
- **Uložit zvukový profil pro tuto knihu** / **Vymazat zvukový profil** - viz [Zvukový profil audioknihy](#zvukový-profil-audioknihy) níže.
- **Odebrat z knihovny** - smaže knihu z vaší knihovny.

Můžete také označit několik knih najednou a odstranit je všechny společně — viz [Označení a odstranění více položek](#označení-a-odstranění-více-položek) v části Oblíbené.

### Přehrávání a pokračování

Vícedílné dílo je v přehrávači považováno za jedinou položku, ne za samostatný řádek pro každý díl - stejně jako je epizoda podcastu jedinou položkou bez ohledu na to, jak je doručena. freeAudio si pamatuje, který díl jste naposledy poslouchali, a při příštím přehrání této knihy v něm automaticky pokračuje, dokonce i po restartu NVDA.

Když jeden díl skončí, freeAudio automaticky spustí další díl téže knihy - nemusíte jej vybírat ručně. To se stane, i když je v danou chvíli okno Průzkumníka stanic zavřené; díl „nyní hraje" zobrazený v seznamu Knihovna se automaticky znovu synchronizuje při příštím otevření okna.

Přehrávání probíhá prostřednictvím malého lokálního relé namísto stažení celého dílu předem, takže poslech začne, jakmile dorazí první bajty - stejné chování okamžitého startu jako u podcastů. Všechny obvyklé ovládací prvky přehrávače (pozastavení, hlasitost, časový posun, rychlost přehrávání, transpozice, výstupní zařízení atd.) fungují u audioknihy stejně jako u stanice nebo epizody podcastu.

Stejně jako u podcastů přehraje pokračování knihy z uložené pozice krátký zvukový efekt zavádění kazety, zatímco freeAudio posouvá zpět na vaše uložené místo - viz poznámka **Zvukový efekt při pokračování** v [Podrobnosti o přehrávání podcastů](#podrobnosti-o-přehrávání-podcastů).

### Zvukový profil audioknihy

Klepněte pravým tlačítkem na knihu v seznamu Knihovna a zvolte **Uložit zvukový profil pro tuto knihu**, čímž uložíte aktuální hlasitost, efekty, zisk ekvalizéru a/nebo rychlost přehrávání jako profil svázaný s touto knihou. Kdykoli se kniha (nebo kterýkoli z jejích dílů) přehraje, uložená nastavení se automaticky použijí a přepíší globální výchozí hodnoty. Funguje to úplně stejně jako [Zvukový profil podcastu](#zvukový-profil-podcastu) výše, včetně stejné sady možností uložení (hlasitost, efekty a/nebo rychlost přehrávání, v jakékoli kombinaci) a stejného chování dílčí aktualizace.

**Vymazat zvukový profil** odstraní uložený profil z knihy; je aktivní pouze tehdy, když má kniha aktuálně uložený profil.

### Stahování audioknih

Vyberte knihu ve své knihovně a zvolte **Stáhnout knihu** z její kontextové nabídky, čímž uložíte každý díl do vlastní složky (pojmenované podle knihy) uvnitř vaší složky nahrávek (ve výchozím nastavení `Dokumenty\freeAudio Recordings\`). Soubory jsou očíslovány tak, aby se díly vždy řadily zpět do pořadí poslechu, bez ohledu na to, jak je pojmenovává samotný GETEM. NVDA po dokončení stahování oznámí, kolik dílů bylo uloženo; pokud se některý díl nezdaří, spolu s počtem se oznámí i poslední chyba.

### Ukládání dat audioknih

Každý zdroj si vede vlastní soubor knihovny, i když se na kartě Audioknihy zobrazují sloučené. Vaše knihovna GETEM (přidané knihy a postup poslechu) se ukládá do `freeAudio_getem_library.json`, vaše knihovna LibriVox se ukládá samostatně do `freeAudio_librivox_library.json` a vaše knihovna Project Gutenberg se ukládá samostatně do `freeAudio_gutenberg_library.json` — všechny tři ve složce uživatelské konfigurace NVDA. Vaše zašifrované přihlašovací údaje GETEM se ukládají samostatně do `freeAudio_getem_credentials.bin` na stejném místě a lze je dešifrovat pouze stejným uživatelským účtem Windows, který je uložil. LibriVox a Project Gutenberg nemají žádný soubor s přihlašovacími údaji, protože ani jeden nevyžaduje účet.

## Místní jukebox

Karta **Jukebox** ve FreeRadiu vám dává dva způsoby přehrávání zvukových souborů, které již máte v počítači: prohledávání všech připojených disků podle názvu souboru, nebo vytvoření trvalé osobní knihovny souborů a složek. Cokoli odtud přehrajete, dostane stejné zacházení jako podcast nebo audiokniha — automatické pokračování, odstupňované přetáčení vpřed/vzad, rychlost přehrávání, transpozice výšky tónu a zvukové profily pro jednotlivé položky fungují úplně stejně.

### Přístup na kartu Jukebox

Otevřete prohlížeč stanic pomocí `Ctrl+Win+R` a přepněte na kartu **Jukebox** pomocí `Ctrl+Tab` nebo `Alt+8`, nebo ji otevřete přímo odkudkoli globální zkratkou `Ctrl+Win+U`. Karta je rozdělena do tří hlavních oblastí:

1. **Hledat na disku** — textové pole, které prohledává všechny místně připojené, připravené disky a hledá zvukové soubory, jejichž název obsahuje zadaný text. Stisknutím `Enter` spustíte hledání.
2. **Výsledky hledání** — seznam, který se zobrazí po spuštění hledání a zobrazuje odpovídající soubory. Do té doby je skrytý, takže karta zůstává přehledná, když není co hledat.
3. **Jukebox a skladby** — trvalý seznam položek, které jste přidali, následovaný seznamem skladeb ve vybrané položce (u položky souboru pouze tento jeden soubor; u položky složky každý zvukový soubor v ní nalezený).

Tlačítka **Přidat soubor…**, **Přidat složku…** a **Odebrat** se nacházejí pod seznamem skladeb.

### Hledání souborů na disku

Zadejte libovolnou část názvu souboru do pole **Hledat na disku** a stiskněte `Enter`. freeAudio prochází všechny místně připojené disky — pevné disky, USB disky, paměťové karty, připojené síťové disky — a hledá zvukové soubory (`.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a`, `.m4b`, `.aac`, `.wma`, `.opus` a několik dalších), jejichž název souboru obsahuje hledaný text. Hledání probíhá na pozadí, takže NVDA zůstává responzivní.

- **Mezerník** na výsledku hledání jej zobrazí jako náhled — spustí přehrávání přes normální přehrávač. Opětovným stisknutím **Mezerníku** na stejném souboru náhled zastavíte.
- **Enter** na výsledku hledání jej přidá do vašeho jukeboxu.
- Kontextová nabídka (klávesa Nabídka / `Shift+F10`, případně kliknutí pravým tlačítkem) nabízí stejné dvě akce: **Náhled** / **Zastavit náhled** a **Přidat do jukeboxu**.
- Spuštění nového hledání zruší jakékoli dosud běžící hledání, takže pomalé hledání na velkém disku nikdy nezdrží nové.

### Budování vašeho jukeboxu

Seznam Jukebox je vaše trvalá osobní knihovna. Lze přidat dva druhy položek:

- **Přidat soubor…** — otevře výběr souborů, který vám umožní přidat jeden nebo více jednotlivých zvukových souborů. Všechny vybrané soubory se přidají najednou.
- **Přidat složku…** — otevře výběr složek, který vám umožní vybrat více složek najednou. Každý zvukový soubor nalezený v každé zvolené složce, včetně jejích podsložek, je považován za jednu ze **skladeb** této složky. Každá složka se přidá jako vlastní samostatná položka v seznamu Jukebox; soubory v ní jsou uvedeny v seznamu Skladby, když je složka vybrána. NVDA po zavření výběru oznámí, kolik složek bylo přidáno.
- **Odebrat** — smaže aktuálně vybranou položku z vašeho jukeboxu. Odebrání položky složky neodstraní žádné soubory z disku; pouze zapomene složku. Můžete také označit několik položek najednou a odstranit je všechny společně — viz [Označení a odstranění více položek](#označení-a-odstranění-více-položek) v části Oblíbené.

Seznam Jukebox se ukládá automaticky, takže přežije restartování NVDA. Obsah složky se skenuje na vyžádání a ukládá do mezipaměti, takže přidání složky je okamžité i u velmi velkých sbírek — úplné skenování proběhne při prvním výběru této složky. Pokud přidáte soubory do složky mimo freeAudio, použijte položku **Znovu prohledat složku** v kontextové nabídce složky, abyste je zachytili.

### Přidávání položek z Průzkumníka Windows

Dva další příkazy, dostupné pouze tehdy, když je v seznamu souborů Průzkumníka Windows (seznam Podrobnosti/ikony — nikoli adresní řádek, strom složek, pás karet nebo vyhledávací pole) zaměřen soubor nebo složka, vám umožní zcela přeskočit dialogy Přidat soubor…/Přidat složku… výše:

- **Přehrát zaměřený soubor ve freeAudio** — přehraje zvýrazněný zvukový soubor přímo, aniž by musel být již ve vašem seznamu Jukebox. Funguje pouze na soubory; při použití na složku vám sdělí, abyste složku přidali do jukeboxu místo toho.
- **Přidat zaměřenou položku do jukeboxu freeAudio** — přidá zvýrazněný soubor nebo složku do vašeho seznamu Jukebox, přesně jako kdybyste použili **Přidat soubor…** nebo **Přidat složku…** výše.

Ani jeden z příkazů nemá ve výchozím stavu přiřazenou klávesu. Přiřaďte ji z nabídky NVDA → Předvolby → Vstupní gesta → freeAudio **při zaměření uvnitř okna Průzkumníka souborů**.

### Přehrávání z jukeboxu

- **Enter** na položce Jukebox ji přehraje přímo: u položky souboru soubor samotný; u položky složky její první skladbu.
- **Mezerník** na položce Jukebox pozastaví přehrávání, pokud něco hraje; v opačném případě přehraje zaměřenou položku.
- **Enter** nebo **Mezerník** v seznamu Skladby přehraje zaměřenou skladbu. **Mezerník** nejprve pozastaví, pokud již něco hraje.
- **F3 / F4** na kartě Jukebox přecházejí mezi skladbami v aktuálně vybrané položce a přehrávají okamžitě.
- **Shift+F3 / Shift+F4** přecházejí mezi položkami v seznamu Jukebox (soubory a složky), což odpovídá tomu, jak tyto klávesy přecházejí mezi kanály na kartě Podcasty.
- **Ctrl+← / Ctrl+→** při zaměření seznamu položek nebo skladeb dělají totéž co F3/F4 v seznamu skladeb — předchozí / další skladba.

### Podrobnosti o přehrávání v jukeboxu

Každá skladba přehraná z jukeboxu dostane plné zacházení místního média:

- **Pokračování:** freeAudio si pamatuje vaši pozici v každé skladbě, ukládá ji při pozastavení a pravidelně během přehrávání, a při dalším přehrání z ní pokračuje — dokonce i po restartu NVDA.
- **Odstupňované posouvání:** `Ctrl+Win+J` / `Ctrl+Win+K` posouvají v rámci skladby se stejným škálováním stisknutí/podržení jako podcasty a audioknihy — podržení na 5 sekund za opakování, jedno stisknutí na 12 sekund, dvě stisknutí na 1 minutu, tři nebo více stisknutí na 5 minut.
- **Rychlost přehrávání:** `Ctrl+Win+Shift+J` / `Ctrl+Win+Shift+K` upravují rychlost v krocích po 0,1× od 0,5× do 2,0×, se zachováním výšky tónu.
- **Transpozice:** `Shift+Win+J` / `Shift+Win+K` mění výšku tónu bez změny rychlosti — viz [Transpozice (posun výšky tónu)](#transpozice-posun-výšky-tónu).
- **Zvukový profil:** Hlasitost, efekty, ekvalizér a rychlost skladby lze uložit globálně přehráním skladby s příslušně nastavenými hodnotami — Jukebox v současnosti neposkytuje nabídku profilu pro jednotlivé skladby, takže platí aktuální globální nastavení.

> **Poznámka:** Vyrovnávací paměť časového posunu (používaná pro přetáčení živého rádia) se pro skladby jukeboxu záměrně **nespouští** — jsou to již lokální soubory s možností posouvání, takže zachytávání na pozadí nemá žádný účel a pouze by spotřebovávalo místo na disku. Přetáčení vpřed i vzad stále funguje, protože působí přímo na přehrávaný soubor.

## Transpozice (posun výšky tónu)

Transpozice posouvá **výšku tónu** přehrávaného obsahu nahoru nebo dolů bez změny jeho **rychlosti** — opak „efektu čipmanka", který byste získali pouhým zrychlením skladby. Je užitečná pro přizpůsobení přirozeného rozsahu konkrétního vypravěče, transponování hudby do příjemnějšího klíče, nebo jen úpravu nahrávky, aby vám pohodlněji seděla v uších.

Transpozice je k dispozici pro **podcasty**, **audioknihy** a **skladby jukeboxu** — stejné „lokální, posouvatelné médium schopné tempa", na které se již vztahují zkratky rychlosti přehrávání. Není k dispozici pro živé rozhlasové stanice, které nemají pevnou výšku tónu k posunu.

- **`Shift+Win+K`** — Zvýší výšku tónu o jeden krok.
- **`Shift+Win+J`** — Sníží výšku tónu o jeden krok.

Každý krok je **osmina celého tónu** — tedy **0,25 půltónu** (celý tón jsou 2 půltóny, takže 8 kroků tvoří celý tón a 48 kroků tvoří oktávu). Rozsah je **−12,00 až +12,00 půltónu**, tj. jedna celá oktáva nahoru nebo dolů. NVDA po každém kroku oznámí novou hodnotu, například „**+1,25 půltónu**"; návrat na 0,0 oznámí „**Normální výška tónu**".

Transpozice se pamatuje napříč skladbami, stejně jako rychlost přehrávání: nastavení jednou při přehrávání skladby znamená, že další skladba schopná tempa, kterou přehrajete, začne se stejným posunem, pokud to její vlastní uložený zvukový profil nepřepíše. Přehrání skladby bez uložené hodnoty transpozice resetuje posun zpět na 0,0 (Normální výška tónu), stejně jako stejné pravidlo již platí pro rychlost.

## Oblíbené skladby

Pokud je povolena možnost **Uložit oblíbené skladby do textového souboru**, informace o skladbě zkopírované do schránky trojím stisknutím kláves `Ctrl+Win+I` se také přidají po řádcích do souboru `Dokumenty\freeAudio Recordings\likedSongs.txt`.

U stanic, které vysílají metadata ICY, se název skladby a interpret uloží přímo. Na stanicích bez metadat ICY se do stejného souboru uloží výsledek rozpoznání Shazam - oba zdroje sdílejí stejný seznam. Soubor se vytvoří automaticky, pokud neexistuje; každý záznam se připojí na konec souboru a předchozí záznamy se nikdy nemažou.

## Karta Oblíbené skladby

Karta **Oblíbené skladby** v prohlížeči stanic zobrazuje všechny stopy uložené v `likedSongs.txt`. Seznam se automaticky znovu načte ze souboru pokaždé, když se karta otevře. Klepnutím pravým tlačítkem na skladbu, případně jejím vybráním a stiskem klávesy Nabídka / `Shift+F10`, otevřete kontextovou nabídku se stejnými akcemi popsanými níže.

Pole **Filtr** nad seznamem umožňuje v reálném čase zúžit zobrazené stopy. Zadejte libovolnou část názvu skladby nebo jména interpreta a seznam se okamžitě aktualizuje po každém stisknutí klávesy. NVDA po každé změně oznamuje počet nalezených výsledků. Stisknutím šipky `dolů` v poli filtru přesunete fokus přímo do seznamu.

Po výběru stopy ze seznamu jsou k dispozici následující akce:

- **Přehrát na Spotify:** Pokusí se přímo otevřít desktopovou aplikaci Spotify. Pokud aplikace není nainstalována, přejde na web Spotify a automaticky přehraje první výsledek.
- **Přehrát na YouTube (`Alt+O`):** Vyhledá vybranou stopu na YouTube a otevře výsledky ve výchozím prohlížeči.
- **Zobrazit text písně:** Načte a zobrazí text vybrané skladby. Text písně je načítán z [lrclib.net](https://lrclib.net) (zdarma, bez nutnosti účtu). Během probíhajícího vyhledávání na pozadí je oznámena krátká zpráva „Načítání textu písně…". Pokud je text nalezen, otevře se v dialogu pouze pro čtení, kde jej můžete číst pomocí NVDA a zkopírovat do schránky. Pokud text není nalezen, NVDA to oznámí. Tlačítko je po dobu probíhající akce dočasně deaktivováno, aby se zabránilo duplicitním požadavkům.
- **Odebrat (`Alt+M`):** Odstraní vybranou stopu z `likedSongs.txt` a aktualizuje seznam. Klávesa `Delete` toto tlačítko také spustí, je-li fokus na seznamu. Můžete také označit několik skladeb najednou a odstranit je všechny společně — viz [Označení a odstranění více položek](#označení-a-odstranění-více-položek) v části Oblíbené.
- **Obnovit (`Alt+E`):** Znovu načte seznam ze souboru.

Tlačítka Spotify, YouTube, Zobrazit text písně a Odebrat jsou aktivní pouze tehdy, když je v seznamu vybrána skutečná skladba.

### Služba textů písní

freeAudio používá [lrclib.net](https://lrclib.net) k načítání textů písní — bezplatná, otevřená databáze nevyžadující klíč API ani účet. Proces vyhledávání analyzuje řetězec stopy uložený v `likedSongs.txt` a postupně zkouší volnější dotazy, dokud nenajde text písně:

1. Přesná shoda s celým jménem interpreta a vyčištěným názvem (rušivé přípony jako „Remastered", „Live" nebo roční tagy se před vyhledáváním odstraní).
2. Přesná shoda s celým jménem interpreta a původním názvem (pokud čištění název změnilo).
3. Přesná shoda pouze s prvním jménem interpreta a vyčištěným názvem (pro řetězce s více interprety, např. „Interpret A & Interpret B").
4. Fuzzy vyhledávání s prvním jménem interpreta a vyčištěným názvem.
5. Fuzzy vyhledávání se surým řetězcem stopy jako poslední možnost.

Jsou-li dostupné textové verze textu, zobrazí se tak, jak jsou. Jsou-li dostupné pouze časově synchronizované LRC texty, odstraní se časová razítka a zobrazí se prostý text. O instrumentálních skladbách se hlásí, že text nebyl nalezen.

## Nastavení

Následující možnosti lze konfigurovat v nabídce NVDA → Předvolby → Nastavení → freeAudio:

| Volba | Popis |
|---|---|
| Hlas pro změnu skladby | Zvolte, zda se automaticky oznamované změny skladeb vyslovují pomocí syntetizátoru NVDA nebo vybraného hlasu SAPI5. |
| Hlas SAPI5 | Když je **Hlas pro změnu skladby** nastaven na SAPI5, vybere, který nainstalovaný hlas SAPI5 se používá k oznamování změn skladeb. Seznam se naplňuje na pozadí z hlasů nainstalovaných v systému. |
| Zvukové výstupní zařízení (BASS backend) | Nastavuje zvukové výstupní zařízení pro přehrávání rádia. Seznam obsahuje všechna zařízení kompatibilní s BASS v systému a možnost "Výchozí systém". Změny se použijí okamžitě po uložení; pokud je vybrané zařízení odpojeno, doplněk se automaticky vrátí k výchozímu nastavení systému a oznámí změnu. Aktivní pouze v případě, že je používán backend BASS. |
| Režim obnovení zvukových zařízení (BASS backend) | Řídí, jak freeAudio obnovuje čísla výstupních zařízení BASS. Režim **Spolehlivý** (výchozí) zkoumá zařízení živě a přesněji sleduje změny Bluetooth/USB, ale může mírně zpomalit změny zařízení. Režim **Rychlý** používá aktuální seznam zařízení BASS a je rychlejší, ale čísla zařízení mohou zůstat zastaralá, dokud není BASS nebo NVDA restartováno. |
| Hlasitost | Nastavuje počáteční hlasitost doplňku (0-200). Zde se také projeví změny provedené během přehrávání pomocí `Ctrl+Win+↑` / `Ctrl+Win+↓`. |
| Zvukové efekty | Nastavuje, které efekty (Chorus, Compressor, Distortion, Echo, Flanger, Gargle, Reverb a tři zesílení EQ) jsou aktivní při spuštění NVDA nebo zahájení přehrávání stanice. Lze zaškrtnout více efektů současně, v souladu se seznamem Efekty v Prohlížeči stanic. Aktivní pouze při použití backendu BASS. |
| Zesílení EQ (basy / výšky / vokál) | Nastavuje úroveň zesílení v dB pro každé pásmo EQ (od −15 do +15). Tyto hodnoty se použijí, když je příslušný EQ efekt aktivní, a ukládají se globálně. Pro každou stanici lze nastavit vlastní hodnoty pomocí tlačítka **Uložit zvukový profil** na záložce Oblíbené. Aktivní pouze při použití backendu BASS. |
| Přechod mezi stanicemi (backend BASS) | Ovládá chování přechodu při přepínání mezi **živými rozhlasovými stanicemi**. **Instant cut** (výchozí nastavení) zastaví předchozí stanici bezprostředně před spuštěním nové. **Krátký přechod (1 sekunda)** a **Normální přechod (2 sekundy)** spustí novou stanici okamžitě bez mezery a poté postupně ukončí předchozí stanici na pozadí, jakmile je potvrzena aktivita nového streamu. **Zvukový efekt ladění stanice** okamžitě zastaví předchozí stanici a před spuštěním nové přehraje zvukový efekt ladění stanice. Nemá žádný účinek a žádný vliv na výkon, pokud je nastaveno na okamžitý střih. K dispozici pouze při použití backendu BASS. Nevztahuje se na podcasty, audioknihy ani skladby jukeboxu — jejich pokračování vždy přehraje vlastní krátký zvukový efekt kazety bez ohledu na toto nastavení; viz [Podrobnosti o přehrávání podcastů](#podrobnosti-o-přehrávání-podcastů). |
| Obnovit poslední stanici při spuštění NVDA | Je-li tato funkce povolena, při každém spuštění NVDA se automaticky obnoví naposledy přehrávaná stanice. |
| Automatické oznamování změn skladeb (metadata ICY) | Je-li povoleno, NVDA automaticky načte nový název skladby při každé změně na stanici, která vysílá metadata ICY. Při přepnutí na novou stanici se také okamžitě ohlásí první stopa. Ve výchozím nastavení zakázáno. |
| Ztlumení oznámení | Je-li povoleno, NVDA neoznamuje změny stanic, změny stavu přehrávání (přehrávání, pozastavení, zastavení) ani události nahrávání (spuštěno, zastaveno, ukončeno). Chybová hlášení, zpětná vazba oblíbených položek, výsledky rozpoznávání hudby a oznámení o aktualizacích nejsou ovlivněny. Lze přepínat i za běhu pomocí nepřiřazeného vstupního gesta. Ve výchozím nastavení vypnuto. |
| Braillské zprávy | Je-li povoleno, freeAudio také odesílá svá oznámení přímo na braillský displej. To je užitečné pro názvy skladeb, změny stanic, stav přehrávání a změny hlasitosti. Ve výchozím nastavení vypnuto. |
| Zapnout vyrovnávací paměť časového posunu (přetočení živého rádia) | Zapíná nebo vypíná ovládací prvky přetáčení (`Ctrl+Win+J`/`Ctrl+Win+K`) a zvětšuje zachytávání na pozadí z ~45 sekund až na dobu určenou v nastavení. Malé zachytávání aktuálně přehrávané stanice na pozadí běží vždy, i když je tato volba vypnutá — viz poznámka v části Časový posun níže. Lze také okamžitě přepnout pomocí `Ctrl+Win+T`. Vyžaduje backend BASS. Ve výchozím nastavení zakázáno — úplné podrobnosti najdete v části Časový posun níže. |
| Uložení oblíbených skladeb do textového souboru | Pokud je tato funkce povolena, informace o skladbě zkopírované do schránky trojím stisknutím kláves `Ctrl+Win+I` se také připojí do souboru `Dokumenty\freeAudio Recordings\likedSongs.txt`. Pokud nejsou k dispozici žádná metadata ICY, uloží se výsledek rozpoznání Shazam do stejného souboru. Ve výchozím nastavení vypnuto. |
| Při stisknutí klávesové zkratky Ctrl+Win+P bez aktivního přehrávání | Určuje, co se stane, když je tato klávesová zkratka stisknuta a nic se nepřehrává: spustí poslední stanici nebo otevře seznam oblíbených. |
| Trvání vyrovnávací paměti časového posunu | Nastavuje maximální délku vyrovnávací paměti pro přetáčení. Možnosti se pohybují od 10 minut do 5 hodin. Delší vyrovnávací paměti spotřebovávají více dočasného místa na disku. |
| Při dvojím stisknutí klávesové zkratky Ctrl+Win+P | Určuje, co se stane, když je tato klávesová zkratka stisknuta dvakrát za sebou: nic nedělat, otevřít seznam oblíbených položek, otevřít kartu nahrávání nebo otevřít kartu časovače. Pokud je vybrána možnost "nedělat nic", první stisknutí reaguje okamžitě bez zpoždění. |
| Při trojím stisknutí klávesové zkratky Ctrl+Win+P | Vybírá, co se stane při trojím stisknutí klávesové zkratky v rychlém sledu za sebou: neudělat nic, otevřít seznam oblíbených položek, otevřít kartu vyhledávání, otevřít kartu záznamu nebo otevřít kartu časovače. |
| Automatická kontrola aktualizací | Je-li tato volba povolena, spustí se při každém spuštění aplikace NVDA kontrola aktualizací na pozadí; pokud je nalezena nová verze, jste o tom informováni. Pokud je zakázána, automatická kontrola se zastaví, ale ruční kontrola zůstane k dispozici. |
| Cesta k souboru ffmpeg.exe | Cesta k souboru ffmpeg.exe, který se používá pro rozpoznávání hudby. Pokud zůstane prázdná, použije se automaticky soubor ffmpeg.exe ve složce doplňku. |
| Složka nahrávek | Nastaví složku, do které se ukládají nahrané soubory. Pokud zůstane prázdná, použije se výchozí umístění `Documents\freeAudio Recordings\`. Tlačítko Procházet umožňuje interaktivní výběr složky. Změny se projeví okamžitě po uložení. |
| Zdroje audioknih | Seznam zaškrtávacích políček vybírající, které zdroje audioknih (**GETEM**, **LibriVox**, **Project Gutenberg**) se prohledávají a zobrazují na kartě Audioknihy. Všechny tři jsou ve výchozím nastavení zapnuté. Odškrtnutím zdroje skryjete jeho knihy ze sloučených výsledků hledání a seznamu knihovny, aniž byste smazali cokoli, co jste z něj již přidali — viz [Audioknihy (GETEM, LibriVox a Project Gutenberg)](#audioknihy-getem-librivox-a-project-gutenberg). |
| Uživatelské jméno GETEM / Heslo GETEM | Vaše přihlašovací údaje pro členství v audioknihách [GETEM](https://getem.boun.edu.tr/), potřebné ke streamování nebo stažení zvuku knihy — viz [Přihlášení](#přihlášení). Ukládají se zašifrovaně na disk prostřednictvím Windows Data Protection API, svázané s vaším uživatelským účtem Windows; nikdy se neukládají jako prostý text. Ponecháním obou polí prázdných a uložením odstraníte všechny uložené přihlašovací údaje. LibriVox a Project Gutenberg nevyžadují žádný účet a nemají žádné ekvivalentní pole. |
| Výstupní formát nahrávky | Zachová původní stream, extrahuje zvuk beze změny kodeku nebo převede dokončené nahrávky na MP3. Výchozí hodnotou je původní formát streamu. |
| Datový tok nahrávání MP3 | Nastaví datový tok použitý, když je výstupní formát nahrávky MP3. Výchozí hodnota je 128 kb/s. |
| Zakázat kontrolu připojení k internetu před přehráváním | Doporučeno pro uživatele, u kterých dochází ke zpoždění před zahájením přehrávání stanice. Užitečné také v případě blokování DNS. |

## Ztlumit oznámení

Pokud je v Nastavení povoleno **Ztlumit oznámení**, NVDA ztiší následující automatická oznámení:

- Název stanice, když se začne přehrávat nová stanice
- Změny stavu přehrávání: přehrávání, pozastavení, zastavení
- Režim Obligato: spuštěn / zastaven
- události nahrávání: spuštěno, zastaveno, dokončeno (okamžité nahrávání, nahrávání skladeb a plánované nahrávání)
- Oznámení o změně skladby ICY, i když je povolena také funkce **Automatické oznamování změn skladeb**.

Záměrně nejsou **ovlivněna** následující oznámení: chybová hlášení, zpětná vazba oblíbených položek (přidáno / již v seznamu), výsledky rozpoznávání hudby a oznámení o aktualizacích.

Nastavení lze přepnout v nabídce NVDA → Předvolby → Nastavení → freeAudio nebo kdykoli okamžitě prostřednictvím nepřiřazeného vstupního gesta (přiřaďte je v nabídce NVDA → Předvolby → Vstupní gesta → freeAudio). Při přepínání NVDA jednou oznámí "Notifications muted" (Oznámení ztlumena) nebo "Notifications unmuted" (Oznámení odtlumena), aby potvrdila změnu.

## Automatické oznamování změn stopy

Pokud je v Nastavení povolena možnost **Auto-announce track changes**, freeAudio přibližně každých 5 sekund na pozadí kontroluje tok metadat ICY aktivní stanice. Když se skladba změní, nový název se automaticky načte pomocí NVDA - není nutné stisknout klávesu.

Při přepnutí na novou stanici se informace o první skladbě oznámí ihned po navázání spojení. Pokud přepnete na stanici, která nevysílá metadata ICY, systém zůstane zticha a informace o skladbě předchozí stanice se neopakují.

Tato funkce je ve výchozím nastavení vypnutá a lze ji přepnout v nabídce NVDA → Předvolby → Nastavení → freeAudio.

## Přehrávání

freeAudio používá **BASS** jako svůj jediný backend přehrávání pro vše — internetové rádio, podcasty, audioknihy a skladby jukeboxu. Není nutná samostatná instalace; je dodáván spolu s doplňkem. Podpora VLC, PotPlayer a Windows Media Player jako záložních backendů byla odstraněna; vždy se používá BASS.

BASS odesílá zvuk přímo do zvukového zásobníku systému Windows a zobrazuje se ve směšovači hlasitosti systému Windows jako nezávislý zdroj zvuku s názvem "pythonw.exe", odděleně od NVDA. To znamená, že zvuk FreeRadia proudí na zcela odděleném kanálu od řeči NVDA: rádio se během řeči NVDA nevypíná, nemísí se s ním ani není ovlivněno vlastním nastavením zvuku NVDA. Uživatel může nastavit hlasitost rádia nezávisle na NVDA ve směšovači hlasitosti systému Windows. Podporuje protokoly HTTP, HTTPS a většinu formátů vložených streamů.

Epizody podcastů, kapitoly audioknih a skladby jukeboxu se přehrávají přes BASS, protože dokáže otevřít stream jako soubor, ve kterém lze posouvat (i během stahování), což umožňuje přesné sledování pozice, odstupňované přetáčení vpřed/vzad, rychlost přehrávání, transpozici výšky tónu a pokračování. Zrcadlení zvuku, časový posun a posouvání/pokračování podcastů/audioknih/jukeboxu všechny závisí na BASS a jsou vždy k dispozici.

## Kontrola aktualizací

freeAudio automaticky kontroluje nové verze prostřednictvím služby GitHub.

**Automatická kontrola:** Probíhá tiše na pozadí 15 sekund po spuštění NVDA. Pokud je nalezena nová verze, jste o tom informováni; pokud není nalezena žádná, nezobrazí se žádná zpráva.

**Ruční kontrola:** Lze spustit na vyžádání z NVDA Nástroje → freeAudio → **Zkontrolovat aktualizace...**. Při spuštění tímto způsobem se výsledek oznámí i v případě, že je verze aktuální.

**Když je nalezena aktualizace:** Otevře se dialogové okno zobrazující číslo verze a vaši nainstalovanou verzi.

- Pokud je na GitHub release k dispozici přímo stažitelný soubor `.nvda-addon`, zobrazí se tlačítko **Stáhnout a nainstalovat**. Po potvrzení se soubor stáhne na pozadí, NVDA oznámí zahájení stahování a automaticky se otevře vlastní instalační obrazovka NVDA.
- Pokud není k dispozici přímý odkaz ke stažení, zobrazí se tlačítko **Otevřít stránku** a v výchozím prohlížeči se otevře stránka release na GitHubu.

**Vypnutí automatických kontrol:** Vypněte možnost **Automaticky kontrolovat aktualizace** v NVDA Menu → Předvolby → Nastavení → freeAudio.

## Poděkování a zásluhy

* **Původní základ a koncepty:** Upřímné díky **Gary Mp** ([GaryMp/freeradio](https://github.com/GaryMp/freeradio)) za původní koncepty rádiového doplňku a základní struktury pro správu oblíbených, které posloužily jako výchozí základ tohoto projektu.
* **Nástroje AI a LLM:** Vděčné poděkování moderním nástrojům velkých jazykových modelů (LLM), včetně Claude, ChatGPT a Gemini, za pomoc během vývoje, refaktoringu kódu a implementace funkcí.
* **Adresářová služba:** Adresář stanic je poháněn pomocí [Radio Browser API](https://www.radio-browser.info/).
* **Komunita:** Upřímné díky všem členům komunity NVDA a překladatelům za jejich trvalou podporu, zpětnou vazbu a příspěvky k lokalizaci.

## Licence

GPL v2