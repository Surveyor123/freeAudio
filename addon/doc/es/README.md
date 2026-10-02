# freeAudio — NVDA Add-on

freeAudio es un complemento completo para el lector de pantalla NVDA que incluye radio por internet, podcasts y audiolibros. Lo que comenzó como una forma sencilla de escuchar emisoras de radio por internet se ha convertido en un centro de escucha completo y totalmente accesible: cada pantalla, diálogo y control está diseñado desde cero para su uso con teclado y lector de pantalla, sin necesidad de usar el ratón en ningún momento.

## Lo Que freeAudio Puede Hacer

- **Radio por Internet** — Explore y busque entre más de 50.000 emisoras desde el directorio de [Radio Browser](https://www.radio-browser.info/), con resultados complementados por TuneIn e iHeartRadio. Guarda favoritos, reordénalos y salta directamente a cualquiera de ellos con un atajo de teclado global desde cualquier lugar en Windows — consulta las secciones [El Directorio de Radio Browser](#radio-browser-directory) y [Favoritos](#favourites).
- **Podcasts** — Suscríbete a cualquier fuente RSS/Atom o busca en el directorio de podcasts de Apple y escucha un adelanto de los episodios antes de suscribirte. La posición de reproducción se guarda automáticamente y se reanuda donde la dejaste — consulta la sección [Podcasts](#podcasts).
- **Audiolibros** — Busca y reproduce en streaming o descarga libros desde las tres fuentes: [GETEM](https://getem.boun.edu.tr/), la biblioteca digital de la Universidad de Boğaziçi para personas con discapacidad visual, [LibriVox](https://librivox.org/), el proyecto de audiolibros de dominio público leídos por voluntarios y la Colección Abierta de Audiolibros del Proyecto Gutenberg — las dos últimas no necesitan cuenta — con reanudación automática para obras en varias partes — consulta la sección [Audiolibros (GETEM, LibriVox y el Proyecto Gutenberg)](#audio-books-getem-librivox-and-project-gutenberg).
- **Jukebox Local** — Busca archivos de audio almacenados en cualquier unidad conectada por nombre de archivo, o cree una biblioteca personal de archivos y carpetas, y reprodúzcalos con las mismas herramientas de reanudación, búsqueda, velocidad y tono que utilizan los podcasts y audiolibros — consulta la sección [Jukebox Local](#local-jukebox).
- **Grabación** — Graba al instante lo que se está reproduciendo, captura automáticamente una sola canción cuando empieza y termina, o programa grabaciones únicas y recurrentes, todo ello sin interrumpir la reproducción — consulta la sección [Grabación](#recording).
- **Desplazamiento temporal (rebobinar radio en directo)** — Pausa y rebobina una emisora ​​en directo como si fuera un grabador de vídeo digital, y luego vuelve a verla en directo cuando quieras — consulta la sección [Desplazamiento temporal (rebobinar radio en directo)](#time-shift-rewind-live-radio).
- **Reconocimiento de música y canciones favoritas** — Identifica pistas sin metadatos mediante el reconocimiento basado en Shazam, guarda las canciones favoritas en un archivo de texto y busca sus letras — consulta las secciones [Reconocimiento de Música](#music-recognition) y [Canciones favoritas](#liked-songs).
- **Perfiles de audio y efectos** — Guarda por separado los ajustes de volumen, de los efectos, de los ecualizadores y  de la velocidad de reproducción por estación, por podcast, por audiolibro o por pista del jukebox, y aplica efectos en tiempo real (Coro, Reverberación, EQ boosts, y más) a través del BASS backend — consulta la sección [Perfil de Audio de la Estación](#station-audio-profile).
- **Transposición (cambio de tono)** — Modifica el tono de podcasts, audiolibros y pistas del jukebox hacia arriba o hacia abajo sin cambiar su velocidad, utilizando el componente `bass_fx` incluido — consulta la sección [Transposición (Cambio de Tono)](#transpose-pitch-shift).
- **Espejo de audio** — Envia la misma transmision a dos dispositivos de salida de audio a la vez, tales como altavoces y auriculares — consulta la sección [Espejo de Audio](#audio-mirror).
- **Modo Obligato (música de fondo)** — Reproduce discretamente tu emisora favorita en segundo plano, con su propio dispositivo de salida y volumen, independientemente de lo que se esté reproduciendo (o no) independientemente del medio principal — consulta la sección [Modo Obligato](#obligato-mode).
- **Temporizadores** — Programa tu emisora ​​favorita para que empiece a reproducirse, o programa que la reproducción se detenga, a una hora específica — consulta la sección [Temporizador](#timer).
- **Acceso al teclado extendido y braille** — Todas las funciones son accesibles completamente desde el teclado, con accesos directos globales que funcionan desde cualquier lugar de Windows, Teclas de acceso directo para cada emisora ​​favorita y salida de braille opcional para todas las notificaciones habladas de freeAudio.

## El Directorio de Radio Browser

freeAudio utiliza la base de datos abierta de [Radio Browser](https://www.radio-browser.info/) por su catálogo de estaciones. Radio Browser es un directorio gratuito impulsado por la comunidad que alberga más de 50.000 estaciones de radio por Internet de todo el mundo. No se requiere registro ni cuenta y su API está abierta a todos. Cada estación incluye información sobre dirección, país, género, idioma y bitrate; las estaciones se clasifican según los votos de los usuarios. freeAudio se conecta a esta API a través de servidores espejo ubicados en Alemania, Países Bajos y Austria; Si un servidor es inaccesible, pasa automáticamente al siguiente.

Para mantener el navegador receptivo y evitar acceder a la API en cada búsqueda o cambio de país, freeAudio mantiene un caché local del catálogo de estaciones en el disco. Este caché se actualiza automáticamente en segundo plano según una programación periódica, por lo que la lista que ve normalmente ya está actualizada sin que usted tenga que realizar ninguna acción. También puedes forzar una resincronización inmediata en cualquier momento con el botón **Actualizar lista de estaciones** — consulta la sección [Navegador de Estaciones](#station-browser) más abajo.

## Añadir una estación a Radio Browser

Si una estación que está buscando no aparece en el directorio de Radio Browser, puedes enviarlo tú mismo a [https://www.radio-browser.info/add](https://www.radio-browser.info/add). No es necesario tener cuenta ni registrarse.

Llene el formulario en esta página:

- **Stream URL** *(requerido)* — la URL directa del flujo de audio, terminando en `.mp3`, `.aac`, `.ogg` o similar. Esta no es la dirección del sitio web de la estación; esta es la dirección del flujo  bruto de transmisión que pegarías en un reproductor multimedia. La mayoría de las estaciones publican la URL de su flujo de transmisión en su sitio web o en su sección "Escuchar en directo".
- **Station name** *(requerido)* — el nombre de la estación como debería aparecer en el directorio.
- **Homepage** — la dirección del sitio web de la estación.
- **Country and language** — seleccione el país y el idioma de transmisión en las listas desplegables.
- **Tags** — palabras clave separadas por comas, por genre o topic, por ejemplo `news`, `jazz`, `classical`. Estos se utilizan para buscar y filtrar.
- **Logo URL** — un enlace directo a la imagen del logotipo de la estación, si está disponible.

Después del envío, la estación se revisa y se añade al directorio público. Una vez aceptado, aparecerá automáticamente en los listados de países y de búsqueda de freeAudio, ya que el directorio se actualiza desde la API en directo.

## Requisitos

- NVDA 2025.1 o posterior
- Windows 10 o posterior
- Conexión a Internet

## Instalación

Descarga el archivo `.nvda-addon`, pulsa Intro y reinicia NVDA cuando se te solicite.

## Atajos de teclado

Todos los atajos se pueden reasignar desde el Menú NVDA → Preferencias → Gestos de Entrada → freeAudio. Estos atajos funcionan desde cualquier lugar, independientemente de qué ventana tenga el foco.

Algunos de estos atajos coinciden con los que usa Windows. Si prefieres conservar el atajo de Windows sin reasignar el de freeAudio, pulsa `NVDA+F2` (Dejar pasar la siguiente tecla) justo antes de la combinación de teclas — NVDA enviará esa combinación directamente a Windows en lugar de interceptarla para freeAudio.

| Atajo | Función | Descripción |
|---|---|---|
| `Ctrl+Win+R` | Abrir el navegador de estaciones | Abre la ventana del navegador si está cerrada o la trae al segundo plano si ya está abierta. |
| `Ctrl+Win+O` | Abrir la pestaña Podcasts | Abre el navegador de estaciones (si está cerrado) o lo trae al primer plano y cambia directamente a la pestaña **Podcasts**. |
| `Ctrl+Win+L` | Abrir la pestaña Audiolibros | Abre el navegador de estaciones (si está cerrado) o lo trae al primer plano y cambia directamente a la pestaña **Audiolibros**. |
| `Ctrl+Win+U` | Abrir la pestaña Jukebox | Abre el navegador de estaciones (si está cerrado) o lo trae al primer plano y cambia directamente a la pestaña **Jukebox**, enfocado en el cuadro de búsqueda de dispositivos. |
| `Ctrl+Win+P` | Pausar / reanudar | Pausa la estación actual si se está reproduciendo; se reanuda cuando está en pausa. Si no se reproduce nada, inicia la última estación o abre la lista de favoritos según su configuración. Al pulsar dos veces en sucesión rápida, irás directamente a la pestaña que elijas. Pulsar tres veces puede activar una acción separada dependiendo de su configuración. |
| `Ctrl+Win+S` | Detener | Detiene completamente la estación actual y reinicia el reproductor. |
| `Ctrl+Win+→` | Siguiente favorito | Salta  a la siguiente estación en la lista de favoritos. Vuelve al principio y al final de la lista. |
| `Ctrl+Win+←` | Favorito anterior | Salta a la estación anterior en la lista de favoritos. Salta al final cuando está al principio. |
| `Ctrl+Win+↑` | Aumentar el volumen | Aumenta el volumen de 5 ; máximo 100. |
| `Ctrl+Win+↓` | Disminuir el volumen | Disminuye el volumen de 5 ; mínimo 0. |
| `Ctrl+Win+V` | Añadir a favoritos / Descargar el Medio | Añade la estación que se está reproduciendo actualmente a la lista de favoritos o descarga el episodio del podcast  o el audiolibro que se está reproduciendo. Anuncia si la emisora ya está en la lista o si el medio ya se había descargado. No aplicable cuando se está reproduciendo una pista del jukebox: freeAudio indica que el acceso directo solo sirve para emisoras, podcasts o audiolibros. |
| `Ctrl+Win+Shift+K` | Aumentar la velocidad de reproducción | Aumenta la velocidad de reproducción de un episodio de podcast, de un audiolibro o de una pista del jukebox de 0.1x (preservación de la altura). Rango: 0.5x a 2.0x. |
| `Ctrl+Win+Shift+J` | Disminuir la velocidad de reproducción | Disminuye la velocidad de reproducción de un episodio de podcast, de un audiolibro o de una pista del jukebox de 0.1x. |
| `Shift+Win+K` | Transposición hacia arriba | Sube el tono de un episodio de podcast, audiolibro o pista del jukebox en pasos de 1/8 de tono completo (0.25 semitonos), sin cambiar su velocidad. Rango: -12.00 a +12.00 semitonos. Consulta la sección [Transposición (Cambio de Tono)](#transpose-pitch-shift). |
| `Shift+Win+J` | Transposición hacia abajo | Baja el tono en pasos de 1/8 de tono completo, sin cambiar la velocidad. |
| `Ctrl+Win+I` | Información de la Estación | Anuncia el nombre de la estación que se está reproduciendo actualmente, episodio de podcast, audiolibro o pista del jukebox. Pulsa dos veces para mostrar los detalles como el país, el género y el bitrate en un diálogo. Pulsa tres veces para copiar la información de la pista actual (metadatos ICY) al portapapeles si está disponible; Si no hay metadatos presentes, inicia el reconocimiento de música de Shazam en su lugar. Pulsa cuatro veces para forzar el reconocimiento de música en caso de metadatos ICY incorrectos. |
| `Ctrl+Win+M` | Espejo de audio | Poner en espejo el flujo actual o medio hacia un dispositivo de salida de audio adicional simultáneamente. Pulsa nuevamente para detener la puesta en espejo. |
| `Ctrl+Win+Shift+M` | Modo Obligato (música de fondo) | Reproduce en bucle una emisora ​​favorita de forma silenciosa en segundo plano, con su propio dispositivo de salida y volumen, independientemente de lo que esté sonando como medio principal. Al pulsar por primera vez, se abrirá un cuadro de diálogo para seleccionar la emisora, el dispositivo de salida y el volumen. Vuelva a pulsar para detenerlo. |
| `Ctrl+Win+E` | Grabación instantánea | Pulsa una vez para comenzar a grabar la estación actual; pulsa nuevamente para detener. Pulsa **dos veces** para comenzar una **grabación de la canción**: El archivo lleva el nombre de la pista actual y la grabación se detiene automáticamente cuando cambia la pista. Pulsa nuevamente dos veces mientras la grabación de una canción está activa para detenerla antes de tiempo. La reproducción continúa sin interrupción en todos los modos de grabación. Solo disponible para estaciones que transmiten metadatos ICY. |
| `Ctrl+Win+W` | Abrir la carpeta de grabaciones | Abre la carpeta que contiene los archivos guardados en el Explorador de archivos. |
| `Ctrl+Win+J` | Retroceso del desplazamiento temporal / podcast, audiolibro & jukebox buscar hacia atrás | Para la radio en directo: retrocede 15 segundos. La primera pulsación entra en el modo de desplazamiento temporal; cada pulsación adicional retrocede 15 segundos más, hasta el límite del búfer configurado en los ajustes de freeAudio. Requiere que el búfer de desplazamiento temporal esté habilitado en Ajustes. Para un podcast, un audiolibro o una pista del jukebox, esta tecla busca dentro del archivo y se ajusta según cómo la pulses: **manteniéndola pulsada** retrocede 5 segundos por repetición, igual que antes; **una sola pulsación deliberada** retrocede 12 segundos; **dos pulsaciones rápidas** retroceden 1 minuto; **tres o más pulsaciones** retroceden 5 minutos. Solo se realiza una búsqueda por secuencia de pulsaciones, cuyo tamaño corresponde a la cantidad de pulsaciones realizadas — las pulsaciones no se suman. Funciona independientemente de la configuración del desplazamiento temporal. |
| `Ctrl+Win+K` | Avance rápido del desplazamiento temporal / podcast, audiolibro & jukebox buscar hacia adelante | Para la radio en directo: avanza 15 segundos mientras se está en modo de desplazamiento temporal. Una vez alcanzado el borde del directo, la reproducción vuelve automáticamente al directo y este comando no tiene efecto hasta que se retroceda de nuevo. Para un podcast, un audiolibro o una pista del jukebox, esta tecla avanza en el archivo usando la misma escala de pulsación prolongada que `Ctrl+Win+J` (mantener pulsado = 5 segundos por repetición; 1 pulsación = 12 segundos; 2 pulsaciones = 1 minuto; 3 o más pulsaciones = 5 minutos). Funciona independientemente de la configuración de desplazamiento temporal. |
| `Ctrl+Win+T` | Alternar búfer de desplazamiento temporal | Habilita o deshabilita el búfer de desplazamiento temporal al instante, reflejando la casilla de Ajustes. Al deshabilitarlo, vuelve inmediatamente al directo si estaba en modo de desplazamiento temporal y detiene la captura en segundo plano. No afecta a la reproducción de podcasts, audiolibros ni jukebox.  |
| *(no asignado)* | Seleccionar dispositivo de salida | Abre una lista bajo demanda de los principales dispositivos de salida disponibles. La lista se muestra solo cuando el BASS detecta más de un dispositivo de salida físico. Asignar una combinación de teclas a través del Menú NVDA → Preferencias → Gestos de Entrada → freeAudio. |
| *((no asignado)* | Alternar notificaciones silenciosas | Alternar la configuración de Silenciar notificaciones sobre la marcha. Asignar una combinación de teclas a través del Menú NVDA → Preferencias → Gestos de Entrada → freeAudio. |
| *(no asignado)* | Reproducir estación favorita directamente | Cada estación de la lista de favoritos aparece como una entrada individual en el Menú NVDA → Preferencias → Gestos de Entrada → **Estaciones freeAudio**. Asigna un atajo de teclado a cualquier estación para iniciarla al instante desde cualquier lugar, sin abrir el navegador. |

Los atajos siguientes/anteriores sólo recorren la lista de favoritos; No funcionan con la lista de todas las estaciones. Cuando una lista tiene el foco en la ventana del navegador, las teclas de flecha izquierda y derecha tienen el mismo propósito — ver la sección de Atajos en el cuadro de diálogo.

## Navegador de Estaciones

freeAudio también añade un subMenú **freeAudio** en el Menú Herramientas de NVDA. Desde allí puede abrir directamente el Navegador de Estaciones y los Ajustes de freeAudio.

La ventana abierta con `Ctrl+Win+R` contiene ocho pestañas: Todas las estaciones, Favoritos, Grabación, Temporizador, Canciones favoritas, Podcasts,  Audiolibros y Jukebox. Puedes navegar entre las pestañas con `Ctrl+Tab` o usando `Alt+1` hasta `Alt+8`.

Cuando se abre la pestaña Todas las estaciones, las 1000 estaciones más votadas se cargan automáticamente desde Radio Browser. Al seleccionar un país de la lista desplegable, se actualiza la lista para mostrar estaciones de ese país. Al escribir en el cuadro de búsqueda se realiza instantáneamente una búsqueda completa en toda la base de datos de Radio Browser simultáneamente por nombre, país y género.

Al buscar, los resultados de Radio Browser se complementan con estaciones de TuneIn e iHeartRadio (cuando estén disponibles). Estas fuentes externas se buscan en segundo plano y sus resultados se combinan en la lista automáticamente, lo que le brinda acceso a aún más estaciones sin ninguna acción adicional.

La lista desplegable **Dispositivo de salida** en la parte inferior de la ventana del navegador (fuera de las pestañas) enumera todos los dispositivos de salida de audio reconocidos por BASS. Al seleccionar un dispositivo, se redirige inmediatamente la salida de audio a él y se guarda la elección de forma permanente; el mismo dispositivo se utiliza automáticamente en la siguiente sesión. Si el dispositivo seleccionado no está conectado, el complemento vuelve automáticamente al valor predeterminado del sistema. Pulse `F11` para abrir un selector de dispositivos bajo demanda más simple desde cualquier lugar del Navegador de estaciones. El selector no se muestra automáticamente y se abre solo cuando el BASS detecta más de un dispositivo de salida físico. Cuando solo hay uno disponible, no es necesario realizar ninguna selección y freeAudio utiliza la salida predeterminada del sistema.

Los controles de **Volumen** (0–200) y **Efectos** en la misma área se puede ajustar en cualquier momento cuando la ventana está abierta. Desde la lista de Efectos, Coro, Compresión, Distorsión, Eco, Flanger, Gargle, Reverberación, EQ: Bass Boost, EQ: Treble Boost y EQ: Vocal Boost se puede activar simultáneamente; Los cambios se aplican instantáneamente al flujo activo. Cada efecto también se puede alternar instantáneamente con `Ctrl+1` hasta `Ctrl+0` sin salir del teclado — consulta la sección [Atajos del Efecto](#effect-shortcuts).

Cuando uno o más efectos de EQ están habilitados, aparece un **control de ganancia** para cada banda activa. La ganancia se puede configurar entre −15 dB y +15 dB; los valores predeterminados son Bass +9 dB, Treble +9 dB, y Vocal +6 dB. Los controles de ganancia se muestran solo para las bandas de EQ que están marcadas actualmente y se ocultan automáticamente cuando un efecto de EQ no está marcado. Los valores de ganancia se guardan globalmente y se restauran en la siguiente sesión.

El botón **Reproducir/Pausar** También se encuentra en la parte inferior de la ventana. Si no se reproduce ninguna estación, se inicia la estación seleccionada; si ya se está reproduciendo una emisora, la reproducción se interrumpe.

El botón **Actualizar lista de estaciones** vuelve a sincronizar el catálogo de estaciones locales desde la API Radio Browser inmediatamente, en lugar de esperar la actualización periódica en segundo plano. Mientras se ejecuta la actualización, el botón está desactivado y NVDA anuncia que hay una actualización en curso; Si lo pulsas nuevamente antes de que finalice la actualización actual, NVDA te informará que ya hay una en marcha. Una vez que se completa la actualización, NVDA anuncia que la lista de estaciones se ha actualizado y los resultados de búsqueda o la lista de países mostrados actualmente se actualizan automáticamente para reflejar los nuevos datos.

Cuando se selecciona una estación en la lista, el botón **Detalles de la estación** muestra información como el país, el idioma, el género, el formato, el bitrate, el sitio web y el flujo URL en un cuadro de diálogo separado. Cada campo aparece en su propio cuadro de texto de solo lectura; puedes moverte entre los campos con Tab y copia toda la información al portapapeles de una vez con el botón **Copiar todo al portapapeles**. Este botón está disponible en las pestañas Todas las estaciones y Favoritos.

### Menú Contextual de la Estación

Haga clic derecho en una estación en la lista Todas las estaciones o Favoritos, o selecciónela y pulse la tecla Aplicaciones o `Shift+F10`, para abrir un menú contextual con acciones rápidas:

- **Detalles de la estación** — igual que el botón Detalles de la estación descrito anteriormente.
- **Añadir a favoritos** *(pestaña Todas las estaciones)* / **Eliminar estación** *(pestaña Favoritos)*.
- **Renombrar la estación** *(pestaña Favoritos)* — igual que `F9`.
- **Guardar perfil de audio para esta estación** / **Borrar perfil de audio** *(pestaña Favoritos)* — consulta la sección [Perfil de Audio de la Estación](#station-audio-profile).
- **Probar URL** — comprueba si se puede acceder actualmente al flujo de la estación seleccionada sin iniciar la reproducción y anuncia el resultado (accesible o el motivo del error, como un error HTTP o tiempo de espera de red).

Sólo los elementos relevantes para la pestaña y selección actual se muestran como disponibles.

### Atajos en el cuadro de diálogo

Las siguientes teclas solo funcionan cuando la ventana del Navegador de Estaciones está activa.

#### Teclas F

| Atajo | Función | Descripción |
|---|---|---|
| `F1` | Guía de ayuda | Abre el archivo de ayuda del complemento en el navegador predeterminado. Primero se busca la guía del idiomas NVDA activo; si no se encuentra, se abre la guía predeterminada. |
| `F2` | Que esta reproduciendo | Anuncia la estación que se está reproduciendo actualmente y el nombre de la pista. Pulsa dos veces para mostrar los detalles como el país, el género y el bitrate en un diálogo. Pulsa tres veces para copiar la información de la pista actual (metadatos ICY) al portapapeles si está disponible; si no hay metadatos presentes, inicia el reconocimiento de música de Shazam en su lugar. Pulsa cuatro veces para forzar el reconocimiento de música en caso de metadatos ICY incorrectos. |
| `F3` | Elemento anterior | En la pestaña Todas las estaciones o Favoritos: salta a la estación anterior  y comienza a reproducir inmediatamente. En la pestaña Podcasts: salta al episodio anterior en la lista de episodios y lo reproduce. En la pestaña Audiolibros: salta al libro anterior y comienza a reproducirlo. En la pestaña Jukebox: salta a la pista anterior del elemento seleccionado en el jukebox y lo reproduce. |
| `F4` | Elemento siguiente | En la pestaña Todas las estaciones o Favoritos: salta a la siguiente estación  y comienza a reproducir inmediatamente. En la pestaña Podcasts: salta al siguiente episodio y lo reproduce. En la pestaña Audiolibros: salta al siguiente libro y comienza a reproducirlo. En la pestaña Jukebox: salta a la siguiente pista del elemento seleccionado en el jukebox y lo reproduce. |
| `Shift+F3` | Feed anterior / parte / elemento | En la pestaña Podcasts: mueve hacia arriba un feed en la lista de suscripciones. En la pestaña Audiolibros: salta a la parte anterior del libro que se está reproduciendo. En la pestaña Jukebox: mueve hacia arriba una entrada en la lista principal del jukebox (archivo o carpeta). |
| `Shift+F4` | Feed siguiente / parte / elemento | En la pestaña Podcasts: mueve hacia abajo un feed en la lista de suscripciones. En la pestaña Audiolibros: salta a la siguiente parte del libro que se está reproduciendo. En la pestaña Jukebox: mueve hacia abajo una entrada en la lista principal del jukebox. |
| `F5` | Disminuir el volumen | Disminuye el volumen de 5 (mínimo 0). |
| `F6` | Aumentar el volumen | Aumenta el volumen de 5 (máximo 200). |
| `F7` | Pausar/reanudar | Pausa la estación actual si se está reproduciendo; se reanuda cuando está en pausa y el medio está cargado. |
| `F8` | Detener | Detiene completamente la estación actual y reinicia el reproductor. |
| `F9` | Renombrar | Abre el cuadro de diálogo para renombrar la estación enfocada en la pestaña Favoritos. |
| `F11` | Seleccionar dispositivo de salida | Abre el selector principal de dispositivos de salida cuando el BASS detecta más de un dispositivo de salida físico. El dispositivo actual está preseleccionado; Intro aplica y guarda la elección. |

#### Lista y Atajos de Navegación

| Atajo | Función | Descripción |
|---|---|---|
| `→` | Elemento siguiente | Cuando una lista de estaciones esté enfocada (Todas las estaciones/Favoritos), salta a la siguiente estación y la reproduce inmediatamente. Cuando la lista de episodios esté enfocada (Podcasts), salta al siguiente episodio y lo reproduce. Vuelve al principio al final de la lista. |
| `←` | Elemento anterior | Cuando una lista de estaciones esté enfocada, salta a la estación anterior y la reproduce inmediatamente. Cuando la lista de episodios esté enfocada, salta al episodio anterior y lo reproduce. Salta al final cuando está al principio. |
| `Ctrl+→` | Episodio siguiente / libro / pista | En la pestaña Podcasts: salta al siguiente episodio y lo reproduce. En la pestaña Audiolibros (con la lista de la biblioteca enfocada): salta al siguiente libro. En la pestaña Jukebox (con la lista de entradas o la lista de pistas enfocadas): salta a la siguiente pista del elemento seleccionado en el jukebox y lo reproduce. |
| `Ctrl+←` | Episodio anterior / libro / pista | En la pestaña Podcasts: salta al episodio anterior y lo reproduce. En la pestaña Audiolibros: salta al libro anterior. En la pestaña Jukebox: salta a la pista anterior del elemento seleccionado en el jukebox y lo reproduce. |
| `Intro` | Reproducir / Añadir | En la lista de estaciones o episodios: reproduce inmediatamente el elemento seleccionado. En los resultados de búsqueda de la pestaña Jukebox: añade el archivo seleccionado al jukebox. En la lista de entradas o pistas de la pestaña Jukebox: reproduce directamente el elemento enfocado. |
| `Espacio` | Reproducir/Pausar/Vista previa | Se pausa si algo se está reproduciendo; de lo contrario, comienza a reproducir el elemento seleccionado. En los resultados de búsqueda de la pestaña Jukebox: activa o desactiva la vista previa (reproducir/detener) del archivo seleccionado. En la lista de entradas o pistas de la pestaña Jukebox: pausa la reproducción si está en curso; de lo contrario, reproduce el elemento enfocado. |
| `Ctrl+Tab` | Pestaña siguiente | Pasa a la siguiente pestaña (Todas las estaciones → Favoritos → Grabación → Temporizador → Canciones favoritas → Podcasts → Audiolibros → Jukebox). |
| `Ctrl+Shift+Tab` | Pestaña anterior | Pasa a la pestaña anterior. |
| `Escape` | Ocultar | Oculta la ventana; el complemento continúa reproduciéndose en segundo plano. |

#### Atajos de Volumen

| Atajo | Función | Descripción |
|---|---|---|
| `Ctrl+↑` | Aumentar el volumen | Aumenta el volumen de 5. Funciona sólo cuando la ventana del navegador está abierta. |
| `Ctrl+↓` | Disminuir el volumen | Disminuye el volumen de 5. Funciona sólo cuando la ventana del navegador está abierta. |

#### Atajos del Efecto

| Atajo | Función | Descripción |
|---|---|---|
| `Ctrl+1` | Alternar Coro | Activa o desactiva el efecto Coro y lo aplica al flujo activo al instante. |
| `Ctrl+2` | Alternar Compresión | Activa o desactiva el efecto Compresión y lo aplica al flujo activo al instante. |
| `Ctrl+3` | Alternar Distorsión | Activa o desactiva el efecto Distorsión y lo aplica al flujo activo al instante. |
| `Ctrl+4` | Alternar Eco | Activa o desactiva el efecto Eco y lo aplica al flujo activo al instante. |
| `Ctrl+5` | Alternar Flanger | Activa o desactiva el efecto Flanger y lo aplica al flujo activo al instante. |
| `Ctrl+6` | Alternar Gargle | Activa o desactiva el efecto Gargle y lo aplica al flujo activo al instante. |
| `Ctrl+7` | Alternar Reverberación | Activa o desactiva el efecto Reverberación y lo aplica al flujo activo al instante. |
| `Ctrl+8` | Alternar EQ: Bass Boost | Activa o desactiva la banda EQ Bass Boost y lo aplica al flujo activo al instante. |
| `Ctrl+9` | Alternar EQ: Treble Boost | Activa o desactiva la banda EQ Treble Boost y lo aplica al flujo activo al instante. |
| `Ctrl+0` | Alternar EQ: Vocal Boost | Activa o desactiva la banda EQ Vocal Boost y lo aplica al flujo activo al instante. |

Cada atajo refleja marcado o desmarcado en la entrada correspondiente en la lista **Efectos**: NVDA anuncia si el efecto fue habilitado o deshabilitado, el cambio se guarda automáticamente y el control de ganancia del EQ para esa banda (si corresponde) aparece o desaparece en consecuencia.

#### Atajos de la Tecla Alt

| Atajo | Función | Descripción |
|---|---|---|
| `Alt+R` | Ir al cuadro de búsqueda | Mueve el foco al cuadro de texto de búsqueda. Busca en Radio Browser con el texto en el campo de búsqueda; el nombre, el país y el género se buscan simultáneamente. |
| `Alt+V` | Añadir/Eliminar un favorito | Añade la estación seleccionada a los favoritos; lo elimina si ya está en la lista. |
| `Alt+1` | Todas las estaciones | Cambia a la pestaña Todas las estaciones. |
| `Alt+2` | Favoritos | Cambia a la pestaña Favoritos. |
| `Alt+3` | Grabación | Cambia a la pestaña Grabación. |
| `Alt+4` | Temporizador | Cambia a la pestaña Temporizador. |
| `Alt+5` | Canciones favoritas | Cambia a la pestaña Canciones favoritas. |
| `Alt+6` | Podcasts | Cambia a la pestaña Podcasts. |
| `Alt+7` | Audiolibros | Cambia a la pestaña Audiolibros. |
| `Alt+8` | Jukebox | Cambia a la pestaña Jukebox, enfocado en el cuadro de búsqueda de dispositivos. |
| `Alt+K` | Cerrar | Cierra la ventana; el complemento continúa reproduciéndose en segundo plano. |

## Favoritos

La lista de favoritos es una colección de emisoras personales almacenada permanentemente. Para añadir una estación, selecciónela de la lista y pulse el botón Añadir a favoritos o usa el atajo `Alt+V`. El mismo atajo elimina una estación que ya está en la lista cuando se selecciona.

Los favoritos se pueden jugar con `Ctrl+Win+→` y `Ctrl+Win+←`; estos atajos funcionan incluso cuando la ventana del navegador no está abierta.

Para eliminar una emisora ​​de la lista de favoritos, selecciónela y pulse el botón **Eliminar estación** o la tecla `Suprimir`. Después de la eliminación, el foco y la selección pasan automáticamente a la siguiente estación de la lista. Si la estación eliminada fue la última, el foco se mueve a la estación anterior. Si la lista queda vacía, el foco se mueve al botón Reproducir.

### Marcado y Eliminación de Varios Elementos

En las lista de Favoritos, de Canciones favoritas, de la biblioteca de Audiolibros y de la del Jukebox permiten seleccionar varios elementos y eliminarlos juntos en un solo paso:

- Pulsa **`.`** (punto) sobre un elemento resaltado para marcarlo o desmarcarlo. NVDA anuncia el cambio y la fila del elemento marcado se etiqueta como "(marcado)" para que su estado permanezca visible mientras sigues desplazándote por la lista.
- Pulsa **`Shift+Inicio`** para marcar o desmarcar cada elemento desde el elemento actual hasta el primero de la lista, o **`Shift+Fin`** para hacer lo mismo hasta el último elemento. Que el rango esté marcado o no lo está depende del estado del elemento actual, por lo que todo el rango siempre se mueve de la misma manera en una sola acción. A continuación, el foco se desplaza al extremo opuesto del rango y NVDA anuncia cuántos elementos han cambiado.
- Pulsa **`Suprimir`** para eliminar todos los elementos marcados a la vez. Si no hay nada marcado, `Suprimir` seguirá eliminando solo el elemento seleccionado, como antes.
- El menú contextual accesible haciendo clic derecho (Tecla Aplicaciones / `Shift+F10`) de cada lista incluye un comando **Eliminar seleccionado**, habilitado solo cuando al menos un elemento está marcado, que hace lo mismo.
- Antes de eliminar cualquier elemento, un único cuadro de diálogo de confirmación resume cuántos elementos se van a eliminar.

Las marcas se aplican a cada lista y se borran una vez que se eliminan los elementos (o se desmarcan individualmente); no se guardan entre sesiones.

### Exportar e Importar Favoritos

La pestaña Favoritos incluye dos botones para hacer copias de seguridad y restaurar tu lista de estaciones:

**Exportar favoritos…** — guarda toda tu lista de favoritos en un archivo. Un cuadro de diálogo te permite elegir entre dos formatos:
- **JSON** (`.json`) — una copia de seguridad completa que conserva los nombres de las estaciones, las URLs del Stream de transmisión y todos los metadatos. Recomendado para restaurar tu lista más adelante o moverla a otro equipo.
- **Lista de reproducción M3U** (`.m3u`) — un formato de lista de reproducción estándar compatible con la mayoría de reproductores multimedia y aplicaciones de radio. Ten en cuenta que M3U no almacena todos los metadatos de la estación, por lo que restaurar desde M3U puede resultar en menos detalles que una copia de seguridad JSON.

**Importar favoritos…** — carga estaciones desde un archivo JSON o M3U exportado previamente. Después de seleccionar el archivo, se te pregunta cómo agregar las estaciones:
- **Sí (Fusionar)** — añade las estaciones importadas a tu lista existente sin eliminar ningún favorito actual. Las estaciones duplicadas no se añaden dos veces.
- **No (Reemplazar)** — borra completamente tu lista de favoritos actual y la reemplaza con el contenido del archivo importado.
- **Cancelar** — regresa al navegador sin realizar ningún cambio.

Tras una importación exitosa, la lista de favoritos, la lista de estaciones de grabación programada y la lista de estaciones del temporizador se actualizan automáticamente.

### Reordenar Favoritos en Grupos

Los favoritos pueden pertenecer a una carpeta o grupo, que se muestra con el sufijo "— Grupo" después del nombre de la emisora ​​en la lista  (por ejemplo, "NPR Newscast — NPR").

- **Importar desde M3U** — si el archivo utiliza la etiqueta  `group-title` (la convención utilizada por DVBViewer y la mayoría de los editores y reproductores de M3U) para organizar las emisoras en carpetas, freeAudio la lee y conserva el grupo de cada emisora ​​al importarla. Al exportar tus favoritos de nuevo a M3U, se escribe la misma etiqueta, por lo que la estructura de carpetas se mantiene tras el procesamiento en freeAudio.
- **Asignar o eliminar un grupo manualmente** — marque uno o más favoritos con el `.` (consulta la sección [Marcado y Eliminación de Varios Elementos](#marking-and-removing-multiple-items) arriba), luego  seleccione  **Asignar al grupo…** en el menú contextual (Tecla Aplicaciones / `Shift+F10`) e ingrese el nombre del grupo. Deje el campo vacío para eliminar los favoritos marcados de su grupo. Si no hay nada marcado, el comando se aplicará al favorito seleccionado actualmente.
- **Filtrado por grupo** — el campo Filtrar que aparece encima de la lista de favoritos también compara con los nombres de los grupos y acepta varias palabras, cada una de las cuales puede coincidir con un campo diferente. Por ejemplo, al escribir `Houston Classical` se encuentra  "Houston Public Media Classical" aunque esa frase exacta no aparece en ningún sitio — "Houston" coincide con el grupo y  "Classical" coincide con el nombre de la emisora.

### Reordenar Favoritos

Con una estación seleccionada en la pestaña Favoritos, pulse la `coma` para entrar en modo de desplazamiento; escuchará un pitido. Navegue hasta la posición de destino con las teclas de flecha, luego pulse la `coma` nuevamente. La estación se coloca en la posición elegida y la nueva organización queda inmediatamente registrada. Al pulsar la `coma` nuevamente en la misma posición se cancela el desplazamiento.

### Atajos de Teclado Directos para Estaciones Favoritas

Cada estación de la lista de favoritos está registrada como un script independiente en el cuadro de diálogo Gestos de Entrada de NVDA, dentro de la categoría **Estaciones freeAudio**. Puedes asignar cualquier atajo de teclado a cualquier estación y pulsarlo desde cualquier lugar — sin necesidad de abrir la ventana del navegador.

Para asignar un atajo:

1. Abre el Menú NVDA → Preferencias → Gestos de Entrada.
2. Expande la categoría **Estaciones freeAudio**.
3. Busca la estación por nombre, selecciónala y pulsa **Añadir**.
4. Pulsa la combinación de teclas deseada y confirma.

El atajo inicia la estación de inmediato. Si la estación se elimina de favoritos, su entrada desaparece de la categoría y cualquier atajo asignado se borra automáticamente por NVDA. Cuando se añade una nueva estación a favoritos, aparece en la categoría al instante — no es necesario volver a abrir el cuadro de diálogo Gestos de Entrada.

### Añadir una Estación Personalizada

Para añadir una estación que no está en Radio Browser, use el botón Añadir una estación personalizada. En el cuadro de diálogo que aparece, ingresa el nombre de la estación y la URL del flujo  de transmisión para añadirla directamente a tus favoritos. Las estaciones personalizadas se pueden escuchar y reorganizar como cualquier otro favorito.

Dos botones adicionales están disponibles en este cuadro de diálogo:

- **Probar URL** — comprueba la URL del flujo que ingresó antes de añadir la estación y anuncia si es accesible. Útil para detectar un error tipográfico o un enlace muerto antes de que termine en su lista de favoritos.
- **Añadir al directorio de Radio Browser…** — abre la [página de envío de Radio Browser](https://www.radio-browser.info/add) en su navegador predeterminado, para que pueda compartir la estación con la comunidad más amplia de Radio Browser una vez que haya confirmado que funciona. Consulta la sección [Añadir una estación a Radio Browser](#adding-a-station-to-radio-browser) más arriba para saber qué espera el formulario de envío.

### Perfil de Audio de la Estación

La pestaña Favoritos incluye dos botones para administrar los ajustes de audio por estación:

**Guardar perfil de audio para esta estación** — guarda el nivel de volumen actual y los efectos activos (coro, EQ, etc.), y valores de ganancia de EQ como un perfil vinculado a esa estación específica. Cada vez que esa estación comienza a reproducirse, sus ajustes de volumen, efectos y ganancia guardadas se aplican automáticamente, anulando los valores predeterminados globales.

**Borrar perfil de audio** — elimina el perfil de audio guardado de la estación seleccionada. Después de borrar, la estación vuelve a los ajustes globales de volumen,  efectos y ganancia de EQ. Este botón solo está activo cuando la estación seleccionada ya tiene un perfil guardado.

Los dos botones están ubicados debajo de la lista de favoritos y solo se activan cuando se selecciona una estación de la lista.

## Reconocimiento de Música

Pulse tres veces `Ctrl+Win+I` activa el reconocimiento de música basado en Shazam para el flujo que se está reproduciendo actualmente. El reconocimiento sólo comienza cuando no hay metadatos ICY (información de la pista transmitida por la estación) disponibles; si hay metadatos presentes, se copian al portapapeles en su lugar.

El reconocimiento funciona de la siguiente manera: se captura una breve muestra de audio a partir del flujo usando ffmpeg, se aplica el algoritmo de huellas digital de Shazam y el resultado se envía a los servidores de Shazam. Si el reconocimiento tiene éxito, el título de la canción, el artista, el álbum y el año de lanzamiento serán anunciados por NVDA y copiado automáticamente al portapapeles. Si la opción **Guardar las canciones favoritas en un archivo de texto** esta activado, el resultado del reconocimiento también se añade a `likedSongs.txt`.

**Retorno de audio:** Suenan dos pitidos ascendentes cuando comienza el reconocimiento y dos pitidos descendentes cuando finaliza. Suena un pitido corto cada 2 segundos mientras el proceso está en progreso.

**Requisito:** ffmpeg.exe requerido. Un ffmpeg.exe colocado en la carpeta del complementos se utiliza automáticamente; si está en una ubicación diferente, la ruta se puede establecer en las Opciones. Descargar ffmpeg desde [ffmpeg.org](https://ffmpeg.org/download.html).

**Una nota sobre las estaciones que insertan anuncios publicitarios:** algunas estaciones muestran un anuncio publicitario breve en cada nueva conexión realizada a su flujo, aparte de la transmisión que ya estás escuchando. El reconocimiento evita muestrear ese anuncio publicitario al reutilizar la conexión del flujo en segundo plano existente de freeAudio (la misma que se usa para el [Desplazamiento temporal (rebobinar radio en directo)](#time-shift-rewind-live-radio)) en lugar de abrir una nueva, por lo que identifica lo que realmente se está reproduciendo en lugar de un anuncio publicitario. Esto funciona automáticamente y no necesita configuración.

## Espejo de Audio

El atajo `Ctrl+Win+M` pone los espejos del flujo que se está reproduciendo actualmente en un segundo dispositivo de salida de audio simultáneamente. Esto es útil para escuchar en dos dispositivos diferentes al mismo tiempo, como altavoces y auriculares.

Al pulsar por primera vez, aparece un cuadro de diálogo de selección que enumera los dispositivos de salida disponibles. Una vez elegido el dispositivo, comienza la puesta en espejo y la reproducción principal continúa sin interrupción. Al pulsar el atajo nuevamente se detiene la la puesta en espejo.

**Casos de uso:**
- **Altavoces + auriculares** — Dejar que un invitado siga el mismo programa con los auriculares mientras tu escuchas a través de los altavoces de la computadora.
- **Configuración de grabación** — Dirija la salida principal a los altavoces  y la segunda salida a una grabadora externa o interfaz de audio para captura externa.
- **Multihabitación** — Reproduzca simultáneamente a través de un altavoz Bluetooth y el altavoz incorporado; no se necesita software adicional para transportar el audio a otra habitación.
- **Monitoreo remoto** — En una sesión de pantalla compartida o de escritorio remoto, tanto el lado local como el remoto pueden escuchar el mismo flujo simultáneamente.

## Modo Obligato

El atajo `Ctrl+Win+Shift+M` reproduce tu emisora favorita en segundo plano, con un motor de audio completamente independiente del reproductor principal, como una suave música de fondo que suena de fondo mientras haces lo que haces.

Al pulsar por primera vez, se abre un cuadro de diálogo con tres controles:

- **Estación de fondo** — una lista de tus emisoras favoritas para elegir cuál se reproduce en segundo plano. Requiere al menos una emisora ​​favorita; si tu lista de favoritas está vacía, freeAudio te indicará que primero añadas una emisora (`Ctrl+Win+V` mientras se reproduce una emisora).
- **Salida de audio** — dispositivo a través del cual se reproduce la estación de fondo: **Igual que la salida principal** (predeterminado), **Predeterminado del sistema** o cualquier dispositivo específico que freeAudio pueda detectar.
- **Volumen de fondo** — el volumen de la emisora de fondo se expresa como un porcentaje del volumen actual de la emisora principal (25 %, 50 %, 75 %, 100 %, 125 % o 150 %). Sus preferencias se guardarán para la próxima vez.

Una vez iniciada, la emisora de fondo sigue funcionando independientemente del reproductor principal — cambiar de emisora, escuchar podcasts o audiolibros en el reproductor principal, o apagarlo por completo, no interrumpe el modo Obligato. Dos elementos permanecen vinculados automáticamente al reproductor principal:

- **Volumen** — el volumen de fondo se mantiene continuamente en el porcentaje elegido del volumen actual del reproductor principal, por lo que subir o bajar el volumen principal (`Ctrl+Win+↑`/`↓`) ajusta la música de fondo de la misma manera.
- **Pausar** — al pausar el reproductor principal (`Ctrl+Win+P`) también se pausa la emisora de fondo, y al reanudar el reproductor principal, esta se reanuda. Si se detiene completamente el reproductor principal, no se considera una pausa, por lo que la emisora de fondo continúa reproduciéndose.

Vuelva a pulsar `Ctrl+Win+Shift+M` en cualquier momento para detener el modo Obligato.

## Grabación

Las grabaciones se guardan de forma predeterminada en `Documentos\freeAudio Recordings\`. El nombre del archivo incluye el nombre de la estación (o el título de la canción, en modo de grabación de canciones) y la hora de inicio de la grabación. La carpeta de grabaciones se puede cambiar en cualquier momento desde el Menú NVDA → Preferencias → Opciones → freeAudio → **Carpeta de grabaciones**.

La configuración **Formato de salida de grabación** controla cómo se guardan las grabaciones completadas:
- **Formato de flujo original** escribe el flujo exactamente como se recibió. Por lo tanto, una transmision HLS puede generar un archivo `.ts` .
- **Solo audio, codec original** elimina la capa de vídeo/contenedor sin volver a codificar el audio. Por ejemplo, el audio AAC de una grabación HLS `.ts` normalmente se guarda como `.m4a`, preservando la calidad de la transmisión.
- **MP3** convierte el audio después de grabar usando la velocidad de bits seleccionada. La conversión utiliza el `ffmpeg.exe` incluido con freeAudio y se ejecuta en segundo plano para que NVDA siga respondiendo. Si la conversión falla, se conserva la grabación original.

**Grabación instantánea:** Mientras se reproduce una estación, pulse una vez `Ctrl+Win+E`. Pulse nuevamente para detener. La reproducción continúa sin interrupción.

**Grabación de la canción:** Pulse `Ctrl+Win+E` **dos veces** en sucesión rápida mientras se reproduce una estación que transmite metadatos ICY. La grabación comienza inmediatamente y lleva el nombre del título de la pista actual. Cuando cambia la pista, la grabación se detiene automáticamente y NVDA anuncia el nombre del archivo grabado. Si desea terminar la grabación antes del final de la pista, ppulse `Ctrl+Win+E` dos veces nuevamente. Si la estación actual no transmite metadatos ICY, la grabación de la canción no está disponible y NVDA te lo notificará.

**Grabación programada:** Abra la pestaña Grabación en el navegador. Seleccione una estación de sus favoritos, ingrese la hora de inicio en formato HH:MM y la duración en minutos, seleccione uno o más días activos y, luego elige el modo de recurrencia y el modo de grabación:

Un campo **Filtrar** encima de la lista de estaciones le permite limitar la lista de favoritos en tiempo real, para que pueda encontrar rápidamente la estación que desea programar.

**Días activos:** Marque uno o más días de la semana. En el modo de Solo grabación, se crea una entrada separada para cada día seleccionado, colocada en la próxima ocurrencia de ese día. En el modo de Recurrencia, la grabación se repite únicamente en los días marcados. Si no se selecciona ningún día, la grabación no se restringe a días concretos.

**Modo de recurrencia:**
- **Grabar una vez** — crea una grabación única para cada día seleccionado. Cada entrada se coloca en la próxima ocurrencia de ese día; si la hora de hoy ya pasó, la entrada se traslada automáticamente a la semana siguiente.
- **Repetir semanalmente** — se repite cada semana en los días activos seleccionados hasta que se elimine de la lista de programación.

**Guarde la grabación en:** Para cada grabación programada, puede optar por guardarla en la carpeta de grabaciones predeterminada o en una carpeta personalizada. Utilice el botón **Examinar...** para seleccionar una carpeta de forma interactiva. Si la carpeta elegida deja de estar disponible, la grabación vuelve a la carpeta predeterminada y se le notifica.

**Modo de grabación:**
- **Grabar mientras escuchas** — reproduce y graba simultáneamente a través del BASS backend.
- **Solo grabación** — Graba silenciosamente en segundo plano sin ninguna salida de audio; El motor de grabación se conecta directamente al flujo de  transmisión.

Una vez que se añade una programación, aparece en la lista de abajo. Utilice el botón **Eliminar seleccionado** para eliminar una programación o **Editar seleccionado** para modificar su hora, duración, recurrencia, días activos, modo de grabación o carpeta de salida.

NVDA anuncia cuándo comienza y cuándo termina una grabación. Si NVDA se reinicia mientras hay una grabación programada activa, la grabación se reanuda automáticamente al iniciar.

Al igual que el reconocimiento de música, la grabación instantánea y de canciones reutiliza la conexión del flujo en segundo plano existente de freeAudio cuando está disponible, en lugar de abrir una nueva, por lo que una grabación captura lo que realmente se transmite incluso en estaciones que de otro modo mostrarían un anuncio publicitario nuevo en una conexión nueva. Esto no se aplica a las grabaciones programadas **Solo grabación**, ya que ninguna estación se está reproduciendo  al momento donde ellas empiezan.

## Desplazamiento temporal (rebobinar radio en directo)

El desplazamiento temporal permite rebobinar la emisora que estás escuchando, como un DVR o una cinta de casete: pausa el momento, retrocede unos minutos y vuelve al directo cuando quieras. La reproducción no tiene que detenerse: rebobinar y avanzar ocurren al instante en el mismo flujo de audio.

Esta función está **deshabilitada por defecto**. Actívala desde el Menú NVDA → Preferencias → Opciones → freeAudio → **Activar búfer de desplazamiento temporal (rebobinar radio en directo, ~10 minutos)**, o actívala al instante en cualquier momento con `Ctrl+Win+T`.

> **Nota:** freeAudio ahora conserva en todo momento una pequeña captura en segundo plano de la estación que se está reproduciendo — no solo cuando esta configuración está habilitada — porque el [Reconocimiento de Música](#music-recognition) y la [Grabación](#recording) dependen de ella para el comportamiento de evasión del anuncio publicitario descrita en estas secciones. Cuando esta configuración está **deshabilitada**, esta captura en segundo plano se conserva durante aproximadamente 45 segundos y `Ctrl+Win+J`/`Ctrl+Win+K` permanecen no disponibles — solo cambia el tamaño del búfer, no si se ejecuta. Al habilitar la configuración aumenta la misma captura hasta el rebobinado completo del búfer de ~10 minutos que se describe a continuación.

### Cómo funciona

Una vez habilitado, freeAudio captura continuamente la emisora en reproducción a un búfer local rotativo en segundo plano. El búfer almacena aproximadamente los **últimos 10 minutos** de audio; el audio más antiguo se descarta automáticamente por el frente a medida que llega audio nuevo, de modo que el búfer siempre representa el "pasado reciente" relativo al borde del directo.
El tiempo de búfer se determina en los ajustes.

- **`Ctrl+Win+J`** — Retroceder 15 segundos. La primera pulsación te lleva de la reproducción en directo a la reproducción con desplazamiento temporal, comenzando 15 segundos detrás del borde del directo. Cada pulsación adicional retrocede 15 segundos más.
- **`Ctrl+Win+K`** — Avanzar 15 segundos en modo desplazamiento temporal. Al alcanzar el borde del directo, la reproducción vuelve automáticamente al stream en directo y NVDA anuncia «Volver al directo».
- **`Ctrl+Win+T`** — Activa o desactiva toda la función. Desactivarla mientras se está en modo de desplazamiento temporal vuelve inmediatamente al directo y detiene la captura en segundo plano de la emisora actual.

La captura en segundo plano sigue funcionando todo el tiempo que se está en modo de desplazamiento temporal, de modo que el borde del directo sigue avanzando incluso mientras escuchas algo de hace unos minutos, exactamente como un DVR real.

### Habilitación y calentamiento del búfer

El búfer empieza a llenarse tan pronto como una emisora comienza a reproducirse (una vez habilitada la función), o en el momento en que habilitas la función mientras ya escuchas una emisora. Por ello, el retroceso solo es posible una vez que se hayan capturado realmente unos segundos de audio. Si pulsas `Ctrl+Win+J` inmediatamente después de cambiar de emisora, NVDA te avisará de que todavía no hay suficiente audio en el búfer. Espera unos segundos e inténtalo de nuevo.

Cambiar a una emisora diferente siempre reinicia el búfer para la nueva emisora; el audio almacenado de la emisora anterior se descarta.

### Flujos compatibles

El desplazamiento temporal funciona con la misma gama de flujos que freeAudio ya admite:

- Flujos HTTP/HTTPS simples (MP3, AAC, OGG, etc.), incluidos servidores de tipo Shoutcast/Icecast.
- **Flujos HLS (`.m3u8`)** — freeAudio resuelve la lista de reproducción maestra de la emisora, sigue la lista de reproducción de medios y descarga segmentos en segundo plano para mantener el búfer lleno.

En el raro caso de que la lista de reproducción de una emisora no pueda leerse en absoluto (por ejemplo, un manifiesto `.m3u8` roto o inalcanzable), NVDA te indicará que el retroceso no está disponible para esa emisora concreta.

### Requisitos y limitaciones

- **Requiere el BASS backend**, que freeAudio siempre utiliza para la reproducción (consulta la sección [Reproducción](#playback)).
- El búfer se establece en los ajustes.
- El búfer es por emisora: cambiar de emisora, detener la reproducción o reiniciar NVDA lo borra y empieza de nuevo.
- La reproducción con desplazamiento temporal usa su propio archivo de búfer local y no produce una grabación guardada. Si quieres conservar el audio de forma permanente, usa también la Grabación instantánea (`Ctrl+Win+E`).

## Temporizador

Abra la pestaña Temporizador en el navegador de estaciones (`Alt+4`). Se pueden añadir dos tipos de temporizador:

Al elegir una estación para un temporizador de alarma, un campo **Filtrar** encima de la lista de estaciones le permite limitar la lista de favoritos en tiempo real.

**Alarma — iniciar la radio:** Comienza a reproducir automáticamente una estación seleccionada de sus favoritos a la hora especificada. Elija una estación e ingrese la hora en formato HH:MM.

**Apagado — detener la radio:** Detiene la reproducción a la hora especificada. Cuando suena el temporizador, el volumen se reduce gradualmente durante 60 segundos antes de que se detenga la reproducción. No es necesaria ninguna selección de estación; simplemente ingrese la hora.

Para ambos tipos, si la hora ingresada ya pasó, la acción se programa para el día siguiente. Si ya existe un temporizador a la misma hora (independientemente del tipo), no se permite añadir uno nuevo; se informa al usuario del conflicto y se le pide que elimine primero la entrada existente. Los temporizadores pendientes se enumeran en la pestaña; seleccione uno y pulse el botón Eliminar el temporizador seleccionado para cancelarlo.

**Temporizadores recurrentes:** Bajo **Recurrencia**, elige **Repetir semanalmente** en lugar de la opción predeterminada de Solo una vez para que el temporizador se ejecute cada semana en lugar de Solo una vez. Una lista de verificación de **Días activos** luego te permite elegir los días de la semana donde se repetirá; si deja todos los días sin marcar, se repetirá todos los días. Un temporizador recurrente se seguirá  ejecutando según lo programado hasta que lo elimine de la lista de temporizadores pendientes — no se trata de una entrada única que desaparece tras su ejecución.

## Podcasts

freeAudio incluye un reproductor de podcasts con todas las funciones. Puede suscribirse a cualquier fuente de podcast RSS o Atom, explorar episodios, reproducirlos, descargarlos y reanudar la reproducción desde donde la dejó — todo totalmente accesible.

### Accediendo a la Pestaña Podcasts

Abra el navegador de estaciones con `Ctrl+Win+R` y cambia a la pestaña **Podcasts** usando `Ctrl+Tab` o `Alt+6`. La pestaña está organizada en tres áreas principales:

1. **Buscar y añadir** — sección superior para descubrir nuevos podcasts, incluida una lista de vista previa que muestra los episodios de cualquier resultado de búsqueda seleccionado actualmente.
2. **Suscripciones** — lista de tus feeds suscritos.
3. **Episodios** — lista de episodios del feed seleccionado, con controles de reproducción.

### Añadiendo un Feed de Podcast

Puedes añadir un feed de podcast de dos maneras:

**Por URL:**
- En el campo **Buscar**, pegue la URL completa del feed RSS o Atom (por ejemplo `https://example.com/feed.xml`).
- Pulse Intro.
- freeAudio busca el feed, lo valida y lo añade a tus suscripciones. Si el feed es válido, escuchará una confirmación con el título del feed. Si falla, un mensaje de error explica el motivo.

**Por búsqueda:**
- En el campo **Buscar**, escriba una palabra clave (título del podcast, tema o nombre del host) y pulse Intro.
- freeAudio busca en el directorio de podcasts de iTunes y muestra los podcasts coincidentes en la lista **Resultados de la búsqueda**.
- Al seleccionar un resultado, se obtiene ese feed en segundo plano y se enumeran sus episodios en la lista **Episodios en resultado seleccionado** justo debajo, para que pueda obtener una vista previa de lo que realmente contiene el programa antes de decidir suscribirse — consulta la sección [Vista previa de Episodios Antes de Suscribirse](#previewing-episodes-before-subscribing) más abajo.
- Una vez que esté satisfecho con lo que ve, seleccione el resultado y pulse `Intro`, o abra su menú contextual (tecla Aplicaciones / `Shift+F10`, o haga clic con el botón derecho) y elija **Suscríbete**, para añadirlo a sus suscripciones. El feed se añade  inmediatamente y aparece en su lista de suscripciones. No hay un botón separado para  "Añadir seleccionado desde la búsqueda" — `Intro` o el menú contextual es la única forma de suscribirse desde los resultados de la búsqueda, manteniendo la interfaz limpia y accesible.

> **Consejo:** También puedes escribir la URL de un feed directamente en el campo de búsqueda — si parece una URL válida, el complemento intentará añadirla como un feed sin buscar.

**Menú contextual para resultados de búsqueda:** Haga clic derecho en un resultado de búsqueda, o selecciónelo y pulse la tecla Aplicaciones / `Shift+F10`, para abrir un menú con una única acción **Suscríbete**, idéntico al de pulsar `Intro` en el resultado.

### Vista previa de Episodios Antes de Suscribirse

Antes de comprometerte con una suscripción, puedes escuchar los episodios de un podcast directamente desde los resultados de la búsqueda. Siempre que seleccione un podcast en la lista **Resultados de la búsqueda**, freeAudio recupera ese feed y muestra sus episodios (título y fecha de publicación) en la lista **Episodios en resultado seleccionado** que se encuentra debajo.

- Seleccione un episodio en esa lista de vista previa y pulse `Intro`, o abra su menú contextual (tecla Aplicaciones / `Shift+F10`, o haga clic derecho) y elija **Vista previa**, para comenzar a reproducirlo a través del reproductor normal. Todos los controles de reproducción habituales (pausar, volumen, desplazamiento temporal, etc.) funcionan exactamente como lo harían en cualquier otra estación o episodio.
- Mientras se obtiene la vista previa de un episodio, el mismo menú contextual muestra **Detener vista previa** en lugar de **Vista previa** — selecciónelo o pulse `Intro` nuevamente en ese episodio para detenerlo.
- La vista previa no te suscribe a nada; es puramente para escuchar antes de decidir. La lista de vista previa en sí es temporal — se reemplaza tan pronto como selecciona un resultado de búsqueda diferente y no persiste en ningún lugar como lo hacen sus suscripciones reales.

### Administrar Suscripciones

Una vez que haya añadido algunos feeds, aparecerán en la lista **Suscripciones**. Cada entrada muestra el título del feed y la cantidad de episodios disponibles.

- **Seleccione un feed** para ver sus episodios en la lista inferior. El cuadro de texto de solo lectura **Detalles del feed** debajo de la lista de suscripciones muestra el título del feed, el autor, la descripción, el recuento de episodios y la URL.
- **Actualizar un feed** — selecciónelo y pulse el botón **Actualizar Feed** (disponible a través del menú contextual, ver más abajo) para obtener los últimos episodios. Todos los feeds también se actualizan automáticamente en segundo plano cuando abres la pestaña Podcasts, por lo que normalmente ves los episodios más recientes sin intervención manual.
- **Eliminar un feed** — selecciónelo y pulse `Suprimir` o use el menú contextual para eliminarlo de sus suscripciones. Se le pedirá confirmación antes de la eliminación.

**Menú contextual para feeds:** Haga clic con el botón derecho en un feed o selecciónelo y pulse la tecla Aplicaciones / `Shift+F10`, para abrir un menú con:
- **Actualizar Feed** — busca nuevos episodios ahora.
- **Guardar perfil de audio para este podcast** / **Borrar perfil de audio** — consulta la sección [Perfil de Audio del Podcast](#podcast-audio-profile).
- **Eliminar Feed** — elimina la suscripción.
- **Copiar URL del feed** — copia la URL del feed al portapapeles.

### Explorar y Reproducir Episodios

Seleccione un feed en la lista de suscripciones; sus episodios aparecen en la lista **Episodios** debajo. Cada episodio muestra:
- Su número de episodio (1 = el episodio más antiguo del feed, contando hasta el más nuevo).
- Su fecha de publicación (si está disponible).
- Su título.
- Un prefijo **"Escuchado"** si el episodio se ha reproducido por completo.
- Un sufijo de duración, ya sea la duración total (si nunca se jugó) o el progreso transcurrido/total (si se jugó parcialmente).

**Reproducción:**
- Seleccione un episodio y pulse `Intro` o `Espacio` para comenzar a reproducirlo. Si un episodio se reprodujo parcialmente antes, se reanuda desde donde lo dejó.
- La fila *no* se actualiza mientras se reproduce el episodio —esto es intencional, por lo que NVDA no vuelve a anunciar repetidamente la fila mientras estás sentado en ella. Su indicador "Escuchado" y su duración se actualizan inmediatamente en el momento en que pausas el episodio o termina de reproducirse, por lo que la visualización siempre es precisa justo cuando importa; simplemente no avanza segundo a segundo durante la reproducción.
- Utilice `F3` / `F4` en la pestaña Podcasts para saltar al episodio anterior/siguiente y reproducirlo inmediatamente. También puedes usar `←` / `→` mientras la lista de episodios está enfocada, o `Ctrl+←` / `Ctrl+→` en cualquier lugar de la pestaña Podcasts — ambos funcionan de manera idéntica.
- Utilice `Shift+F3` / `Shift+F4` para moverse entre feeds  sin reproducir episodios.
- Pulse `Espacio` mientras se reproduce un episodio para pausar o reanudar la reproducción.

**Reanudación de la reproducción:** freeAudio guarda tu posición en cada episodio del podcast automáticamente — inmediatamente cada vez que haces una pausa o finaliza el episodio, y cada 15 segundos en segundo plano mientras sigues escuchando, por lo que un bloqueo o un reinicio inesperado no perderá mucho progreso. Si detiene o pausa la reproducción y regresa más tarde, el episodio se reanuda desde la posición guardada. Si reproduce el episodio hasta el final (dentro de los últimos 3 segundos), se marca como "Escuchado" y no se reanudará — la próxima vez comienza desde el principio y el prefijo "Escuchado" aparece en la lista.

**Menú contextual para episodios:** Haga clic con el botón derecho en un episodio o selecciónelo y pulse la tecla Aplicaciones / `Shift+F10`, para abrir un menú con:
- **Reproducir episodio** — inicia la reproducción.
- **Descargar episodio** — descarga el archivo del episodio a tu carpeta de grabaciones.
- **Guardar perfil de audio para este podcast** / **Borrar perfil de audio** — las mismas órdenes que el menú contextual del propio feed, incluidos aquí para mayor comodidad, para que no tengas que volver a la lista de suscripciones. Siguen guardando un único perfil para todo el podcast, no uno aparte para este episodio — consulta la sección [Perfil de Audio del Podcast](#podcast-audio-profile).
- **Copiar URL del episodio** — copia la URL del audio directo al portapapeles.

### Descargando Episodios

Seleccione un episodio y haga clic en el botón **Descargar episodio** (o use el menú contextual). El episodio se descarga a su carpeta de grabaciones (`Documentos\freeAudio Recordings\` por defecto). El nombre del archivo se basa en el título del episodio y la extensión del archivo detectado (`.mp3`, `.m4a`, `.ogg`, etc.). NVDA anuncia cuándo comienza y finaliza la descarga. Si el archivo ya existe, se le informa y se omite la descarga.

### Filtrado de Episodios

Encima de la lista de episodios hay un campo  **Filtrar**. A medida que escribe, la lista de episodios se filtra en tiempo real para mostrar episodios cuyo título contiene el texto escrito, o cuyo número de episodio coincide exactamente con él — por lo que al escribir  `47` salta directamente al episodio 47 incluso si "47" no aparece en ninguna parte de su título. NVDA anuncia el número de episodios coincidentes después de cada cambio. Pulse la flecha `Abajo` desde el campo Filtrar para mover el foco directamente a la lista filtrada.

### Detalles de Reproducción del Podcast

Los episodios de podcast se reproducen utilizando el **BASS backend** (el mismo motor que se utiliza para los flujos de radio y, a partir de esta versión, el único sistema de reproducción que usa freeAudio). Debido a que los episodios se descargan progresivamente y se pueden buscar, puedes usar los atajos del desplazamiento temporal: rebobinar/avanzar (`Ctrl+Win+J`/`Ctrl+Win+K`) mientras reproduces un podcast para buscar dentro del episodio. La posición se guarda automáticamente para que puedas retomarla más tarde.

**Búsqueda escalonada:** A diferencia del rebobinado fijo de 15 segundos de la radio en directo, la búsqueda dentro de un podcast o audiolibro se adapta a la forma en que pulses la tecla, de modo que puedes hacer una pequeña corrección o saltar mucho sin pulsaciones repetidas:

- **Mantener pulsada la tecla** (repetición automática) retrocede o avanza **5 segundos** por repetición, la misma pequeña cantidad que este atajo siempre ha utilizado para los archivos.
- **Una pulsación deliberada** busca **12 segundos**.
- **Dos pulsaciones** en rápida sucesión busca **1 minuto**.
- **Tres o más pulsaciones** busca **5 minutos**; las pulsaciones adicionales en la misma ráfaga no provocan una escalada mayor.

Se mantiene pulsado un instante antes de realizar la búsqueda, por si acaso se produce otra pulsación; solo se realiza una búsqueda por secuencia de pulsaciones, cuyo tamaño depende del número total de pulsaciones, no de la suma de las pulsaciones individuales. Tras la búsqueda, NVDA anuncia la posición transcurrida/restante del episodio, en lugar de simplemente indicar "X segundos hacia adelante/atrás".

**Velocidad de reproducción:** Puede ajustar la velocidad de reproducción de los episodios del podcast, audiolibros y pistas del jukebox usando `Ctrl+Win+Shift+K` (más rápido) y `Ctrl+Win+Shift+J` (más lento). La velocidad cambia por incrementos de 0.1x, desde 0.5x hasta 2.0x, con la altura preservada.

**Transposición (cambio de tono):** Independientemente de la velocidad de reproducción, puede cambiar el tono de un episodio de podcast, audiolibro o pista del jukebox hacia arriba o hacia abajo con `Shift+Win+K` / `Shift+Win+J` — consulta la sección [Transposición (Cambio de Tono)](#transpose-pitch-shift).

**Reanudar efecto de sonido:** Siempre que un episodio se reanuda desde una posición guardada, freeAudio reproduce brevemente un suave efecto de sonido de carga de casete en un canal separado mientras busca el punto guardado, en lugar de dejar que el audio del episodio se reproduzca audiblemente desde 0:00 mientras tanto. Esto es independiente del ajuste de la **Transición de cambio de estación** — ese ajuste solo afecta al cambio entre emisoras de radio en directo, y no la reanudación de podcasts o audiolibros.

### Perfil de Audio del Podcast

Haz clic con el botón derecho en un podcast de la Lista de suscripciones, o haga clic con el botón derecho en cualquiera de sus episodios y elija **Guardar perfil de audio para este podcast** para guardar el volumen actual, efectos, ganancias EQ y/o velocidad de reproducción como un perfil vinculado a ese podcast. Cada vez que se reproduce un episodio de ese podcast, la configuración guardada se aplica automáticamente, anulando los valores predeterminados globales. Debido a que la órden está disponible tanto en el menú contextual del feed como en el menú contextual del episodio, puedes acceder a ella sin volver a la Lista de suscripciones — de cualquier forma, siempre guarda un perfil para todo el podcast, no uno separado para cada episodio.

Un cuadro de diálogo con 15 opciones te permite elegir exactamente qué guardar:
- **Solo volumen**
- **Solo efectos**
- **Volumen y efectos**
- **Volumen y velocidad de reproducción**
- **Efectos y velocidad de reproducción**
- **Solo velocidad de reproducción**
- **Volumen, efectos y velocidad de reproducción**
- **Solo transposición de tono**
- **Volumen y transposición de tono**
- **Efectos y transposición de tono**
- **Velocidad de reproducción y transposición de tono**
- **Volumen, efectos y transposición de tono**
- **Volumen, velocidad de reproducción y transposición de tono**
- **Efectos, velocidad de reproducción y transposición de tono**
- **Volumen, efectos, velocidad de reproducción y transposición de tono**

Solo los elementos que elijas se escribirán en el perfil; lo que se omita conservará lo que ya estaba guardado para ello. Por ejemplo, al elegir **Solo velocidad de reproducción** en un podcast que ya tiene un perfil de volumen/efectos guardado, solo se actualiza la velocidad y el resto permanece sin cambios.

**Borrar perfil de audio** elimina el perfil guardado del podcast, desde cualquiera de los menús contextuales. Solo está habilitado cuando el podcast tiene un perfil guardado.

### Almacenamiento de Datos del Podcast

Tus suscripciones se almacenan en `freeAudio_podcasts.json` en la carpeta de configuración de usuario de NVDA. Las posiciones de los episodios se almacenan por separado en `podcast_positions.json` en la misma ubicación. Ambos archivos son JSON simples y se puede realizar una copia de seguridad o transferirlos a otra computadora.

## Audiolibros (GETEM, LibriVox y el Proyecto Gutenberg)

freeAudio incluye un reproductor de audiolibros que busca, reproduce y descarga libros de tres fuentes:

- **[GETEM](https://getem.boun.edu.tr/)** — la biblioteca digital dirigida por el Centro Universitario Boğaziçi para personas con discapacidad visual. Se requiere una membresía gratuita para transmitir o descargar el audio de un libro (la navegación no requiere membresía gratuita) — consulta la sección [Iniciar Sesión](#signing-in) más abajo.
- **[LibriVox](https://librivox.org/)** — el proyecto de audiolibros de dominio público leídos por voluntarios. No se necesita ninguna cuenta ni inicio de sesión; todo su catálogo, incluidos los propios archivos de audio, es de dominio público y de libre acceso.
- **Proyecto Gutenberg Colección Abierta de Audiolibros** — audiolibros de dominio público narrados por humanos y por computadora alojados en [archive.org](https://archive.org/), complemento de la biblioteca de textos del Proyecto Gutenberg. Al igual que LibriVox, no se necesita ninguna cuenta ni inicio de sesión.

Los resultados de las tres fuentes aparecen juntos en una única lista combinada de **Resultados de la búsqueda** y en una única lista combinada de **Biblioteca** — no hay ninguna pestaña o menú desplegable separado para cambiar entre ellos. La fuente de cada libro (GETEM, LibriVox o el Proyecto Gutenberg) se muestra como una etiqueta junto a su título y en sus detalles, para que siempre sepas cuál estás viendo. Puedes buscar, previsualizar, añadir, reproducir y descargar libros de cualquier fuente exactamente igual; reproducir obras divididas en partes con reanudación automática entre ellas; y descargar libros para escucharlos sin conexión — todo ello con total accesibilidad.

Cualquier fuente se puede desactivar desde el **Menú NVDA → Preferencias → Opciones → freeAudio** con la lista de verificación **Fuentes de audiolibros**, si solo quieres buscar en algunas de ellas. Las tres están habilitadas por defecto.

> **Nota:** Para escuchar un audiolibro de GETEM se requiere una membresía gratuita de GETEM. Navegar por el catálogo de GETEM no requiere una cuenta, pero resolver y reproducir el audio de un libro de GETEM sí — consulta la sección [Iniciar Sesión](#signing-in) abajo. Los libros de LibriVox y el Proyecto Gutenberg nunca requieren una cuenta.

### Acceso a la Pestaña Audiolibros

Abra el navegador de estaciones con `Ctrl+Win+R` y cambie a la pestaña  **Audiolibros** usando `Ctrl+Tab` o `Alt+7`. La pestaña tiene tres áreas principales:

1. **Buscar** — un campo de texto para buscar en todos los catálogos habilitados a la vez, con una lista de resultados que aparece una vez que se ejecuta la búsqueda.
2. **Biblioteca** — la lista de libros que ha añadido de cualquier fuente, donde puede reproducirlos, descargarlos y administrarlos.
3. **Detalles** — un cuadro de solo lectura que muestra la fuente, el título, autor, narrador, editorial, formato, número de partes, descripción y URL del catálogo del libro seleccionado, en cualquier lista.

### Iniciar Sesión

GETEM requiere ser miembro registrado para reproducir en streaming o descargar el audio real de un libro, aunque el catálogo en sí se puede buscar libremente. Ingresa tu nombre de usuario y contraseña de GETEM una vez en  **Menú NVDA → Preferencias → Opciones → freeAudio**; se almacenan cifrados en el disco (a través de la API de protección de datos de Windows, vinculados a su cuenta de usuario de Windows) y luego se reutilizan automáticamente. Si intenta reproducir o descargar un libro GETEM antes de ingresar las credenciales, freeAudio le indica que las agregue primero  en las Opciones.

LibriVox y el Proyecto Gutenberg no requiere ningún paso de inicio de sesión: sus resultados y audios se pueden buscar, previsualizar, reproducir y descargar inmediatamente, sin necesidad de introducir credenciales.

### Búsqueda de Audiolibros

Escriba un término de búsqueda en el campo de búsqueda y pulse `Intro`. freeAudio busca en las fuentes que estén habilitadas en los ajustes y combina los resultados en una sola lista:

- **GETEM** permite realizar búsquedas simultáneas por título, autor, narrador, tema y editorial, ya que su formulario de búsqueda interno solo permite combinar todos estos criterios. Únicamente se muestran las obras disponibles en formato de audio (narración humana o computarizada, audiodescripción, radionovelas, audiolibros DAISY, etc.); los documentos en braille, letra grande y otros formatos que no sean de audio se excluyen automáticamente.
- **LibriVox** permite realizar búsquedas por título o autor/lector en su catálogo de dominio público.
- **Proyecto Gutenberg** permite realizar búsquedas por título o autor en la Colección Abierta de Audiolibros en archive.org.

Al pegar la URL de la página de catálogo/detalles de un libro directamente en el campo de búsqueda (una página de catálogo de GETEM o una página de "detalles" de archive.org para un título de LibriVox o Proyecto Gutenberg), permite encontrar este libro directamente en lugar de realizar una búsqueda por palabras clave.

NVDA anuncia cuántos audiolibros se encontraron en total.

Al seleccionar un resultado, se muestran sus detalles — autor, narrador, editor, formato y recuento de partes — en el cuadro de detalles debajo.

**Vista previa:** Seleccione un resultado y  pulse `Espacio`, o abra su menú contextual (tecla Aplicaciones / `Shift+F10`, o haga clic derecho) y elija **Vista previa**, para comenzar a reproducirlo desde su primera parte sin añadirlo a su biblioteca. Mientras se obtiene la vista previa de un libro, el mismo menú contextual muestra **Detener vista previa** en su lugar — selecciónelo o pulse `Espacio` nuevamente para detenerlo. La vista previa de un libro no guarda su posición de escucha, ya que solo se realiza un seguimiento de los libros que ya están en su biblioteca.

**Añadir a su biblioteca:** Seleccione un resultado y  pulse `Intro`, o use su menú contextual y elija **Añadir a la biblioteca**, para  añadirlo. freeAudio te dice si el libro ya está ahí.

### Tu Biblioteca

Los libros que ha añadido aparecen en la lista **Biblioteca**, mostrando el título, el autor y el formato. Al seleccionar uno se muestran sus detalles debajo.

- Pulse `Intro` o `Espacio` para reproducir el libro seleccionado. Si no se carga nada, `Espacio` lo inicia; si ya se está reproduciendo algo, `Espacio` lo pausa en cambio, coincide con el resto del reproductor.
- Utilice `F3` / `F4` en la pestaña Audiolibros para pasar al **libro** anterior/siguiente de su biblioteca y comenzar a reproducirlo. `Ctrl+←` / `Ctrl+→` hacen lo mismo mientras la lista de bibliotecas está enfocada.
- Utilice `Shift+F3` / `Shift+F4` para moverse entre **partes** del libro que se reproduce actualmente — al revés de la pestaña Podcasts, donde F3/F4 se mueve entre episodios y Shift+F3/F4 se mueve entre feeds. Esto se debe a que un libro es una sola entrada de biblioteca incluso cuando tiene varias partes, por lo que la navegación más detallada por "partes" se encuentra aquí en las teclas modificadas por Shift.

**Menú contextual para entradas de la biblioteca:** Haga clic con el botón derecho en un libro o selecciónelo y pulse la tecla Aplicaciones / `Shift+F10`, para abrir un menú con:
- **Reproducir medios** — comienza a reproducir, igual que `Intro`.
- **Descargar libro** — descarga cada parte del libro; consulta la sección [Descarga de Audiolibros](#downloading-audio-books) más abajo.
- **Copiar la URL** — copia la URL de la página del catálogo del libro al portapapeles (la página del catálogo GETEM para un libro GETEM, o la página de detalles de archive.org para un libro LibriVox o  un libro del Proyecto Gutenberg).
- **Guardar perfil de audio para este libro** / **Borrar perfil de audio** — consulta la sección [Perfil de audio del Audiolibro](#audio-book-audio-profile) más abajo.
- **Eliminar de la biblioteca** — elimina el libro de tu biblioteca.

También puedes marcar varios libros a la vez y eliminarlos todos juntos — consulta la sección [Marcado y Eliminación de Varios Elementos](#marking-and-removing-multiple-items) bajo la sección Favoritos.

### Reproducción y Reanudación

Un trabajo de varias partes se trata como un elemento único en el reproductor, no como una fila por parte — de la misma manera que un episodio de podcast es un elemento único independientemente de cómo se entregue. freeAudio recuerda qué parte escuchaste por última vez y la reanuda automáticamente la próxima vez que reproduzcas ese libro, incluso después de reiniciar NVDA.

Cuando termina una parte, freeAudio inicia automáticamente la siguiente parte del mismo libro — no es necesario seleccionarla manualmente. Esto sucede incluso si la ventana del Navegador de estaciones está cerrada en ese momento; la parte "Ahora está sonando" aparecerá en la lista de la biblioteca y se resincronizará automáticamente la próxima vez que se abra la ventana.

La reproducción se transmite a través de un pequeño relé local en lugar de descargar primero la parte completa, por lo que la escucha comienza tan pronto como llegan los primeros bytes — el mismo comportamiento de inicio inmediato que utilizan los podcasts. Todos los controles habituales del reproductor (pausa, volumen, desplazamiento temporal , velocidad de reproducción, transposición, dispositivo de salida, etc.) funcionan en un audiolibro exactamente como lo harían en una estación o episodio de podcast.

Al igual que con los podcasts, al reanudar un libro desde su posición guardada se reproduce un breve efecto de sonido de carga de casete mientras freeAudio busca la posición guardada — consulta la nota **Reanudar efecto de sonido** en la sección [Detalles de Reproducción del Podcast](#podcast-playback-details).

### Perfil de audio del Audiolibro

Haz clic con el botón derecho en un libro de tu lista de la biblioteca y elige **Guardar perfil de audio para este libro** para guardar el volumen actual, efectos, ganancias EQ y/o velocidad de reproducción como un perfil vinculado a ese libro. Cada vez que se reproduce el libro (o cualquiera de sus partes), la configuración guardada se aplica automáticamente, anulando los valores predeterminados globales. Esto funciona exactamente igual que el [Perfil de Audio del Podcast](#podcast-audio-profile) arriba, incluyendo el mismo conjunto de opciones de guardado (volumen, efectos y/o velocidad de reproducción, en cualquier combinación) y el mismo comportamiento de actualización parcial.

**Borrar perfil de audio** eimina el perfil guardado del libro; solo se habilita cuando el libro tiene un perfil guardado.

### Descarga de Audiolibros

Seleccione un libro en su biblioteca y elija **Descargar libro** en su menú contextual para guardar cada parte en su propia carpeta (que lleva el nombre del libro) dentro de su carpeta de grabaciones (`Documentos\freeAudio Recordings\` por defecto). Los archivos están numerados para que las partes siempre vuelvan a ordenarse en orden de escucha, independientemente de cómo las llame  en GETEM. NVDA anuncia cuántas partes se guardaron una vez finalizada la descarga; Si una  parte falla, el último error se informa junto con el recuento.

### Almacenamiento de Datos de Audiolibros

Cada fuente conserva su propio archivo de biblioteca, aunque se muestren combinados en la pestaña Audiolibros. Tu biblioteca GETEM (libros añadidos y su progreso de escucha) se almacena en `freeAudio_getem_library.json`, su biblioteca LibriVox se almacena por separado en `freeAudio_librivox_library.json` y su biblioteca del Proyecto Gutenberg se almacena por separado en `freeAudio_gutenberg_library.json` — los tres en la carpeta de configuración de usuario de NVDA. Sus credenciales GETEM cifradas se almacenan por separado en `freeAudio_getem_credentials.bin` en la misma ubicación, y solo pueden ser descifradas por la misma cuenta de usuario de Windows que las guardó. LibriVox y el Proyecto Gutenberg no tienen archivo de credenciales, ya que ninguno requiere una cuenta.

## Jukebox Local

La pestaña **Jukebox** de freeAudio te ofrece dos maneras de reproducir archivos de audio que ya están en tu computadora: buscar archivos por nombre en todas las unidades conectadas o crear una biblioteca personal de archivos y carpetas. Todo lo que reproduzcas desde aquí se gestionará igual que un podcast o un audiolibro — reanudación automática, rebobinado/avance rápido por niveles, velocidad de reproducción, transposición de tono y perfiles de audio por elemento funcionan exactamente igual.

### Accediendo a la Pestaña Jukebox

Abra el navegador de estaciones con `Ctrl+Win+R` y cambia a la pestaña **Jukebox** con `Ctrl+Tab` o `Alt+8`, o ábrela directamente desde cualquier lugar con el atajo global `Ctrl+Win+U`. La pestaña está organizada en tres áreas principales:

1. **Buscar en dispositivos** — un campo de texto que busca archivos de audio en todas las unidades conectadas localmente y listas para usar cuyo nombre contenga el texto escrito. Pulsa `Intro` para iniciar la búsqueda.
2. **Resultados de la búsqueda** — una lista que aparece una vez realizada la búsqueda, mostrando los archivos coincidentes. Permanece oculta hasta entonces, para que la pestaña se mantenga despejada cuando no haya nada que buscar.
3. **Jukebox y Pistas** — la lista permanente de elementos que has añadido, seguida de la lista de pistas de la entrada seleccionada (para una entrada de archivo, solo ese archivo; para una entrada de carpeta, cada archivo de audio encontrado en su interior).

Los botones **Añadir un archivo…**, **Añadir una carpeta…** y **Eliminar** se encuentran debajo de la lista de pistas.

### Buscando Archivos en Dispositivos

Escribe cualquier parte del nombre de un archivo en el campo **Buscar en dispositivos** y pulsa `Intro`. freeAudio busca en todas las unidades conectadas localmente — discos duros, unidades USB, tarjetas de memoria, unidades de red mapeadas — buscando archivos de audio (`.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a`, `.m4b`, `.aac`, `.wma`, `.opus`, y varios más) cuyo nombre contenga el texto de búsqueda. La búsqueda se ejecuta en segundo plano, por lo que NVDA sigue funcionando sin problemas.

- **Espacio** en un resultado de búsqueda para previsualizarlo — e iniciar la reproducción con el reproductor normal. Vuelve a pulsar **Espacio** en el mismo archivo para detener la previsualización.
- **Intro** en un resultado de búsqueda para añadirlo a tu jukebox.
- El menú contextual (Tecla Aplicaciones / `Shift+F10`, o clic derecho) ofrece las mismas dos acciones: **Vista previa** / **Detener vista previa** y **Añadir al Jukebox**.
- Al iniciar una nueva búsqueda, se cancela cualquier búsqueda en curso, por lo que una búsqueda lenta en un disco grande nunca retrasa una nueva.

### Creando Tu Jukebox

La lista del Jukebox es tu biblioteca personal permanente. Se pueden añadir dos tipos de elementos:

- **Añadir un archivo…** — abre un selector de archivos que te permite añadir uno o más archivos de audio individuales. Todos los archivos seleccionados se añaden a la vez.
- **Añadir una carpeta…** — abre un selector de carpetas que te permite seleccionar varias carpetas a la vez. Cada archivo de audio que se encuentre dentro de la carpeta seleccionada, incluyendo sus subcarpetas, Se trata como una de las **pistas** de esa carpeta. Cada carpeta se añade como una entrada individual en tu lista del Jukebox; los archivos que contiene se muestran en la lista de pistas cuando se selecciona la carpeta. Una vez que se cierra el selector, NVDA anuncia cuántas carpetas se han añadido.
- **Eliminar** — elimina la entrada seleccionada actualmente de tu Jukebox. Eliminar una entrada de carpeta no elimina ningún archivo del disco o dispositivo; simplemente olvida la carpeta. También puedes marcar varias entradas a la vez y eliminarlas todas juntas — consulta la sección [Marcado y Eliminación de Varios Elementos](#marking-and-removing-multiple-items) bajo la sección Favoritos.

Tu lista del Jukebox se guarda automáticamente, por lo que se conserva incluso después de reiniciar NVDA. El contenido de las carpetas se escanea bajo demanda y se almacena en caché, por lo que añadir una carpeta es instantáneo, incluso para colecciones muy grandes — el escaneo completo se realiza la primera vez que seleccionas esa carpeta. Si añades archivos a una carpeta fuera de freeAudio, usa el elemento **Volver a escanear la carpeta** en el menú contextual de la carpeta para que se incluyan.

### Añadiendo Elementos desde el Explorador de Windows

Otros dos comandos, disponibles únicamente cuando un archivo o carpeta está enfocada en la lista de archivos del Explorador de Windows (la lista Detalles/Iconos, no la barra de direcciones, la vista en árbol de carpetas, la cinta de opciones ni el cuadro de búsqueda), permiten omitir por completo los cuadros de diálogo Añadir un archivo…/Añadir una carpeta… mencionados anteriormente:

- **Reproducir el archivo enfocado con freeAudio** — reproduce directamente el archivo de audio resaltado, sin necesidad de que esté ya en tu lista del Jukebox. Solo funciona con archivos; si lo usas en una carpeta, te indica que añadas la carpeta al Jukebox.
- **Añadir el elemento enfocado al jukebox de freeAudio** — añade el archivo o carpeta resaltado a tu lista del Jukebox, exactamente como si hubieras usado **Añadir un archivo…** o **Añadir una carpeta…** mencionados anteriormente.

Ninguno de estos comandos tiene una tecla predeterminada asignada. Asigne una desde el menú NVDA → Preferencias → Gestos de Entrada → freeAudio **mientras se encuentra enfocado dentro de una ventana del Explorador de archivos**.

### Reproduciendo desde el Jukebox

- **Intro** en una entrada del Jukebox para reproducirla directamente: si se trata de una entrada de archivo, el archivo en sí; para una entrada de carpeta, su primera pista.
- **Espacio** en una entrada del Jukebox para pausar la reproducción si hay algo reproduciéndose; de lo contrario, reproduce la entrada enfocada.
- **Intro** o **Espacio** en la lista de pistas para reproducir la pista enfocada. **Espacio** pausa primero si ya hay algo reproduciéndose.
- **F3 / F4** en la pestaña Jukebox para cambiar de pista dentro de la entrada seleccionada actualmente y reproducir inmediatamente.
- **Shift+F3 / Shift+F4** para cambiar entre las entradas de la lista del Jukebox (archivos y carpetas), de forma similar a como estas teclas se mueven entre los feeds en la pestaña Podcasts.
- **Ctrl+← / Ctrl+→** mientras la lista de entradas o pistas está enfocada realiza la misma función que F3/F4 en la lista de pistas — pista anterior/siguiente.

### Detalles de Reproducción del Jukebox

Cada pista reproducida desde el Jukebox recibe el tratamiento completo de los medios locales:

- **Reanudar:** freeAudio recuerda tu posición en cada pista , la guarda al pausarla y periódicamente durante la reproducción, y reanuda la reproducción desde ese punto cuando la reproduces de nuevo — incluso después de reiniciar NVDA.
- **Búsqueda por niveles:** `Ctrl+Win+J` / `Ctrl+Win+K` permite buscar dentro de la pista con la misma escala  de pulsación/mantener pulsado que los podcasts y audiolibros — mantén pulsado para 5 segundos por repetición, una pulsación para 12 segundos, dos pulsaciones para 1 minuto, tres o más pulsaciones para 5 minutos.
- **Velocidad de reproducción:** `Ctrl+Win+Shift+J` / `Ctrl+Win+Shift+K` ajusta la velocidad en pasos de 0.1x desde 0.5x hasta 2.0x, conservando el tono.
- **Transposición:** `Shift+Win+J` / `Shift+Win+K` cambia el tono sin modificar la velocidad — consulta la sección [Transposición (Cambio de Tono)](#transpose-pitch-shift).
- **Perfil de audio:** El volumen, los efectos, la ecualización y la velocidad de una pista se pueden guardar globalmente reproduciéndola con la configuración adecuada — actualmente, el Jukebox no ofrece un menú de perfil por pista, por lo que se aplican los ajustes globales actuales.

> **Nota:** El búfer de desplazamiento temporal (utilizado para rebobinar la radio en directo) **no** se inicia para las pistas del Jukebox — estas ya son archivos locales con capacidad de búsqueda, por lo que una captura en segundo plano no tiene sentido y solo consumiría espacio en disco. El rebobinado y el avance rápido siguen funcionando porque actúan directamente sobre el archivo que se está reproduciendo.

## Transposición (Cambio de Tono)

La transposición cambia el **tono** de lo que se está reproduciendo, tanto hacia arriba como hacia abajo, sin modificar su **velocidad** — es lo contrario del "efecto de chirrido" que se obtiene al acelerar una pista. Resulta útil para ajustar el registro natural de un narrador en particular, transponer música a una tonalidad más agradable,o simplemente ajustar una grabación para que suene más cómoda.

La transposición está disponible para **podcasts**, **audiolibros** y **pistas  del jukebox** — los mismos "local, búsqueda, medios con capacidad de tempo" a los que ya se aplican los atajos de velocidad de reproducción. No está disponible para emisoras de radio en directo, ya que no tienen un tono fijo que se pueda modificar.

- **`Shift+Win+K`** — Sube el tono de un paso.
- **`Shift+Win+J`** — Baja el tono de un paso.

Cada paso equivale a **un octavo de tono completo** — es decir, **0.25 semitonos** (un tono completo son  2 semitonos, por lo que  8 pasos forman un tono completo, y 48 pasos forman una octava). El rango es de **−12.00 a +12.00 semitonos**, es decir, una octava completa hacia arriba o hacia abajo. NVDA anuncia el nuevo valor después de cada paso, por ejemplo, "**+1.25 semitonos**"; al volver a 0.0 se anuncia "**Tono normal**".

La transposición se recuerda en todas las pistas, de la misma manera que se recuerda la velocidad de reproducción: configurarla una vez mientras se reproduce una pista significa que la siguiente pista con capacidad de tempo que reproduzcas comenzará con el mismo cambio, a menos que el perfil de audio guardado de esa pista lo anule. Reproducir una pista sin un valor de transposición guardado restablece el cambio hacia atrás a 0.0 (Tono normal), al igual que la misma regla que ya se aplica a la velocidad.

## Canciones favoritas

Cuando la opción **Guardar las canciones favoritas en un archivo de texto** está activado, la información de la pista se copia al portapapeles pulsando tres veces `Ctrl+Win+I` también se añade línea por línea a `Documentos\freeAudio Recordings\likedSongs.txt`.

En las estaciones que transmiten metadatos ICY, el título de la pista y el artista se guardan directamente. En las estaciones sin metadatos ICY, el resultado del reconocimiento de Shazam se guarda en el mismo archivo; ambas fuentes comparten la misma lista. El archivo se crea automáticamente si no existe; cada entrada se añade al final del archivo y las entradas anteriores nunca se eliminan.

## Pestaña de Canciones favoritas

La pestaña **Canciones favoritas** en el navegador de estaciones se muestran todas las pistas guardadas en `likedSongs.txt`. La lista se recarga automáticamente desde el archivo cada vez que se abre la pestaña. Haga clic derecho en una canción, o selecciónela y pulse la tecla Aplicaciones / `Shift+F10`, para abrir un menú contextual con las mismas acciones que se describen a continuación.

Un campo **Filtrar** encima de la lista permite limitar las pistas mostradas en tiempo real. Escribe cualquier parte del título de una canción o nombre del artista y la lista se actualiza instantáneamente a cada pulsación. NVDA anuncia el número de resultados coincidentes tras cada cambio. Pulsa la flecha `Abajo` desde el campo Filtrar para mover el foco directamente a la lista.

Seleccionar una pista de la lista permite las siguientes acciones:

- **Reproducir en Spotify:** Intenta abrir la aplicación de escritorio de Spotify directamente. Si la aplicación no está instalada, vuelve al sitio web de Spotify y automáticamente comienza a reproducir el primer resultado.
- **Reproducir en YouTube (`Alt+O`):** Busca en YouTube la pista seleccionada y abre los resultados en el navegador predeterminado.
- **Mostrar letra:** Obtiene y muestra la letra de la pista seleccionada. Las letras se obtienen de [lrclib.net](https://lrclib.net) (gratuito, sin cuenta requerida). Se anuncia un breve mensaje "Obteniendo letra…" mientras la búsqueda se ejecuta en segundo plano. Si se encuentran letras, se abren en un cuadro de diálogo de solo lectura donde puedes leerlas con NVDA y copiarlas al portapapeles. Si no se encuentran letras, NVDA lo anuncia. El botón se desactiva temporalmente mientras se realiza una búsqueda para evitar solicitudes duplicadas.
- **Eliminar (`Alt+M`):** Elimina la pista seleccionada de `likedSongs.txt` y  actualiza la lista. La tecla `Suprimir` también activa este botón cuando la lista está enfocada. También puedes marcar varias canciones a la vez y eliminarlas todas juntas — consulta la sección [Marcado y Eliminación de Varios Elementos](#marking-and-removing-multiple-items) bajo la sección Favoritos.
- **Refrescar (`Alt+E`):** Vuelve a cargar la lista desde el archivo.

Los botones Spotify, YouTube, Mostrar letra y Eliminar sólo se activan cuando se selecciona una pista real en la lista.

### Servicio de letras

freeAudio usa [lrclib.net](https://lrclib.net) para obtener letras — una base de datos gratuita y abierta que no requiere clave de API ni cuenta. El proceso de búsqueda analiza la cadena de pista almacenada en `likedSongs.txt` y prueba consultas progresivamente más amplias hasta encontrar letras:

1. Coincidencia exacta con el nombre completo del artista y el título limpio (los sufijos de ruido como "Remastered", "Live" o etiquetas de año se eliminan antes de buscar).
2. Coincidencia exacta con el nombre completo del artista y el título original (si la limpieza lo cambió).
3. Coincidencia exacta con solo el primer nombre de artista y el título limpio (para cadenas de múltiples artistas como "Artista A & Artista B").
4. Búsqueda difusa con el primer nombre de artista y el título limpio.
5. Búsqueda difusa con la cadena de pista sin procesar como último recurso.

Cuando hay letras en texto plano disponibles, se muestran tal cual. Cuando solo hay letras LRC sincronizadas por tiempo, se eliminan las marcas de tiempo y se muestra el texto plano. Las pistas instrumentales se reportan como no encontradas.

## Opciones

Las siguientes opciones se pueden configurar desde el Menú NVDA → Preferencias → Opciones → freeAudio:

| Opción | Descripción |
|---|---|
| Deshabilitar el BASS backend | Cuando esté habilitado, freeAudio no utilizará el motor BASS incluido y, en su lugar, dependerá de VLC, PotPlayer, o Windows Media Player. Reinicia NVDA para que este cambio surta efecto. |
| Voz de cambio de pista | Elige si los cambios de pista anunciados automáticamente se verbalizan usando el sintetizador NVDA o una voz SAPI5 seleccionada. |
| Dispositivo de salida de audio | Establece el dispositivo de salida de audio para la reproducción de la radio. La lista incluye todos los dispositivos del sistema BASS-compatible más una opción "valor predeterminado del sistema". Los cambios se aplican inmediatamente después de guardarlos; Si el dispositivo seleccionado se desconecta, el complemento vuelve automáticamente al valor predeterminado del sistema y anuncia el cambio. |
| Modo de actualización del dispositivo de audio | Controla cómo freeAudio actualiza los números de dispositivos de salida de BASS. El modo **Confiable** (predeterminado) analiza los dispositivos en vivo y rastrea los cambios de Bluetooth/USB con mayor precisión, pero puede hacer que los cambios del dispositivo sean un poco más lentos. El modo **Rápido** utiliza la lista actual de dispositivos de BASS y es más rápido, pero los números de dispositivos pueden permanecer obsoletos hasta que se reinicie el BASS o NVDA. |
| Volumen | Establece el volumen cuando se inicia el complemento (0–200). Los cambios realizados durante la reproducción con `Ctrl+Win+↑` / `Ctrl+Win+↓` también se reflejan aquí. |
| Efecto de audio predeterminado | Establece el efecto de audio aplicado cuando se inicia NVDA o una estación comienza a reproducirse. El efecto seleccionado corresponde a la lista de efectos en el navegador de estaciones. |
| Ganancia de EQ (Bass / Treble / Vocal) | Establece el nivel de ganancia en dB para cada banda de EQ (−15 a +15). Estos valores se aplican cuando el efecto EQ correspondiente está activo y se guardan globalmente. Las reemplazos por estación se pueden almacenar utilizando el botón **Guardar perfil de audio** en la pestaña Favoritos. |
| Transición de cambio de estación | Controla el comportamiento de transición al conmutar entre las **estaciones de radio en directo**. **Corte instantáneo** (por defecto) detiene la estación anterior justo antes de que comience la nueva. **Fundido encadenado corto (1 segundo)** y **Fundido encadenado normal (2 segundos)** inicia inmediatamente la nueva estación sin interrupción, luego desaparece gradualmente la estación anterior en segundo plano una vez confirmado el nuevo flujo activo. **Efecto de sonido de sintonización de estación** detiene la estación anterior inmediatamente y reproduce un efecto de sonido de sintonizador de estación antes de que comience la nueva. No tiene ningún efecto ni impacto en el rendimiento cuando se establece en Corte instantáneo. No se aplica a podcasts ni audiolibros — su reanudación siempre reproduce un breve efecto de sonido de casete, independientemente de este ajuste; consulta la sección [Detalles de Reproducción del Podcast](#podcast-playback-details). |
| Reanudar la última estación al iniciar NVDA | Cuando está habilitado, la última estación escuchada se reinicia automáticamente cada vez que se inicia NVDA. |
| Anunciar automáticamente los cambios de pista (metadatos ICY) | Cuando está habilitado, NVDA lee automáticamente el nombre de la nueva pista cada vez que cambia en una estación que transmite metadatos ICY. La primera canción también se anuncia inmediatamente al cambiar a una nueva estación. Deshabilitado por defecto. |
| Silenciar notificaciones | Cuando está habilitado, NVDA no anuncia cambios de estación, cambios de estado de reproducción (reproducir, pausar, detener) o eventos de grabación (iniciado, detenido, terminado). Mensajes de error, comentarios sobre favoritos, resultados de reconocimiento de música y notificaciones de las actualizaciones no se ven afectadas. También se puede activar sobre la marcha mediante un gesto de entrada no asignado. Deshabilitado por defecto. |
| Mensajes braille | Cuando está habilitado, freeAudio también envía sus notificaciones directamente a la pantalla braille. Esto es útil para títulos de pistas, cambios de estación, estado de reproducción y cambios de volumen. Deshabilitado por defecto. |
| Activar búfer de desplazamiento temporal (rebobinar radio en directo, ~10 minutos) | Activa o desactiva los controles de rebobinado `Ctrl+Win+J`/`Ctrl+Win+K`) y aumenta la captura en segundo plano de ~45 segundos a ~10 minutos. Una pequeña captura en segundo plano de la emisora ​​en reproducción siempre se ejecuta, incluso cuando está deshabilitada — consulta la nota en la sección **Desplazamiento temporal (rebobinar radio en directo)** a continuación. También se puede alternar al instante con `Ctrl+Win+T`. Deshabilitado por defecto — consulta la sección **Desplazamiento temporal (rebobinar radio en directo)** a continuación para obtener más detalles. |
| Guardar las canciones favoritas en un archivo de texto | Cuando está habilitado, la información de la pista se copia al portapapeles pulsando `Ctrl+Win+I` tres veces y también se añade a `Documentos\freeAudio Recordings\likedSongs.txt`. Si no hay metadatos ICY disponibles, el resultado del reconocimiento de Shazam se guarda en el mismo archivo. Deshabilitado por defecto. |
| Cuando Ctrl+Win+P se pulsa sin reproducción activa | Determina qué sucede cuando se pulsa este atajo y no hay nada  en reproducción: iniciar la última estación o abrir la lista de favoritos. |
| Duración del búfer de desplazamiento temporal | Establece la longitud máxima del búfer de rebobinado. Las opciones van desde 10 minutos hasta 5 horas. Los buffers más largos consumen más espacio temporal en el disco. |
| Cuando Ctrl+Win+P se pulsa dos veces | Selecciona lo que sucede cuando se pulsa el atajo dos veces en sucesión rápida: no hacer nada, abrir la lista de favoritos, abrir la pestaña de grabación o abrir la pestaña del temporizador. Cuando "No hacer nada" es seleccionado, la primera pulsación responde instantáneamente sin demora. |
| Cuando Ctrl+Win+P se pulsa tres veces | Selecciona lo que sucede cuando se pulsa el atajo tres veces en sucesión rápida: no hacer nada, abrir la lista de favoritos, abrir búsqueda de emisoras, abrir la pestaña de grabación o abrir la pestaña del temporizador. |
| Buscar actualizaciones automáticamente al iniciar | Cuando está habilitado, una verificación de actualización en segundo plano se ejecuta cada vez que se inicia NVDA; se le notificará si se encuentra una nueva versión. Cuando está deshabilitado, los controles automáticos se detienen pero los controles manuales permanecen disponibles. |
| Ruta ffmpeg.exe | Ruta de acceso al ffmpeg.exe usado para el reconocimiento de música. Si se deja vacío, un ffmpeg.exe en la carpeta del complementos se usa automáticamente. |
| Carpeta de grabaciones | Establece la carpeta donde se guardan los archivos grabados. Si se deja en blanco, la ubicación predeterminada `Documentos\freeAudio Recordings\` se utiliza. Un botón Explorar carpeta le permite seleccionar la carpeta de forma interactiva. Los cambios entran en vigor inmediatamente después de guardarlos. |
| Fuentes audiolibro | Una lista de verificación para seleccionar qué fuentes de audiolibros (**GETEM**, **LibriVox**, **Proyecto Gutenberg**) se buscan y se muestran en la pestaña Audiolibros. Las tres están habilitadas por defecto. Al desmarcar una fuente, sus libros se ocultan de los resultados de búsqueda combinados y de la lista de la biblioteca sin eliminar nada de lo que ya hayas añadido desde ella — consulta la sección [Audiolibros (GETEM, LibriVox y el Proyecto Gutenberg)](#audio-books-getem-librivox-and-project-gutenberg). |
| Nombre de usuario de GETEM / Contraseña de GETEM | Sus credenciales de membresía de audiolibros [GETEM](https://getem.boun.edu.tr/), necesarias para escuchar o descargar el audio de un libro — consulta la sección [Iniciar sesión](#signing-in). Almacenadas cifradas en disco a través de la API de protección de datos de Windows, vinculadas a su cuenta de usuario de Windows; nunca se almacenan como texto sin formato. Si deja ambos campos vacíos y guarda, se eliminarán las credenciales almacenadas. LibriVox y el Proyecto Gutenberg no requieren cuenta y no tienen un campo equivalente. |
| Formato de salida de grabación | Conserva el flujo original, extrae el audio sin cambiar su codec o convierte grabaciones completas a MP3. El valor predeterminado es el formato de flujo original. |
| Velocidad de bits de grabación de MP3 | Establece la velocidad de bits utilizada cuando el formato de salida de grabación es MP3. El valor predeterminado es 128 kbps. |
| Desactivar la verificación de conectividad a Internet antes de reproducir | Recomendado para usuarios que experimentan un retraso antes de que una estación comience a reproducirse. También es útil cuando el DNS está bloqueado. |

## Silenciar Notificaciones

Cuando **Silenciar notificaciones** está habilitado en las Opciones, NVDA silencia los siguientes anuncios automáticos:

- Nombre de la estación cuando comienza a reproducirse una nueva estación
- Cambios de estado de reproducción: reproducir, pausar, detener
- Modo Obligato: iniciado / detenido
- Eventos de grabación: iniciado, detenido, terminado (grabaciones instantáneas, de canciones y programadas)
- Anuncios de cambio de pista ICY, incluso cuando **Anunciar automáticamente los cambios de pista**   también está habilitado

Los siguientes anuncios **no** se ven afectados intencionalmente: mensajes de error, comentarios sobre favoritos (añadido / ya en la lista), resultados de reconocimiento de música y notificaciones de actualización.

La configuración se puede alternar desde el Menú NVDA → Preferencias → Opciones → freeAudio, o instantáneamente en cualquier momento mediante un gesto de entrada no asignado (asignar uno desde el Menú NVDA → Preferencias → Gestos de Entrada → freeAudio). Cuando está habilitado, NVDA anuncia una vez "Notificaciones silenciadas" o "Notificaciones reactivadas" para confirmar el cambio.

## Anunciar automáticamente los cambios de pista

Cuando la opción **Anunciar automáticamente los cambios de pista** se activa en las Opciones, freeAudio comprueba el flujo de metadatos ICY de la estación activa en segundo plano aproximadamente cada 5 segundos. Cuando cambia la pista, NVDA lee automáticamente el nuevo título; no es necesario pulsar ninguna tecla.

Al cambiar a una nueva emisora, la información de la primera pista se anuncia tan pronto como se establece la conexión. Si cambia a una estación que no transmite metadatos ICY, el sistema permanece en silencio y la información de la pista de la estación anterior no se repite.

Esta función está desactivada de forma predeterminada y se puede alternar desde el Menú NVDA → Preferencias → Opciones → freeAudio.

## Reproducción

freeAudio utiliza **BASS** como único motor de reproducción para todo: radio por internet, podcasts y audiolibros. No requiere instalación adicional; viene incluido con el complemento. Se ha eliminado la compatibilidad con VLC, PotPlayer y Windows Media Player como motores de reproducción alternativos; siempre se utiliza BASS.

BASS envía el audio directamente a la pila de audio de Windows y aparece en el mezclador de volumen de Windows como una fuente de audio independiente llamada "pythonw.exe", separada de NVDA. Esto significa que el audio de freeAudio circula en un canal completamente separado del habla de NVDA: la radio no se corta, no se mezcla ni se ve afectada por la propia configuración de audio de NVDA mientras NVDA está hablando. El usuario puede ajustar el volumen de la radio independientemente de NVDA en el Mezclador de volumen de Windows. Admite HTTP, HTTPS y la mayoría de los formatos de flujo integrados.

Los episodios de podcasts, los capítulos de audiolibros y las pistas del jukebox se reproducen a través de BASS porque éste puede abrir el flujo como un archivo buscable (incluso durante la descarga), lo que permite un seguimiento preciso de la posición, rebobinado/avance rápido por niveles, velocidad de lectura, transposición de tono y reanudación. La puesta en espejo  de audio, el desplazamiento temporal, así como la búsqueda y la reanudación de podcasts/audiolibros/jukebox dependen de BASS y están siempre disponibles.

## Comprobación de Actualización

freeAudio busca automáticamente nuevas versiones a través de GitHub.

**Comprobación automática:** Se ejecuta silenciosamente en segundo plano 15 segundos después de que se inicia NVDA. Si se encuentra una nueva versión, se le notificará; si no se encuentra ninguno, no se muestra ningún mensaje.

**Comprobación manual:** Se puede activar a solicitud desde Herramientas NVDA → freeAudio → **Buscar actualizaciones…**. Cuando se inicia de esta manera, el resultado se anuncia incluso si la versión está actualizada.

**Cuando se encuentra una actualización:** Se abre un cuadro de diálogo que muestra el número de versión y la versión instalada.

- Si hay un archivo `.nvda-addon` directamente descargable disponible en la release de GitHub, se muestra un botón **Descargar y Instalar**. Una vez confirmado, el archivo se descarga en segundo plano, NVDA anuncia cuándo comienza la descarga y La propia pantalla de instalación se abre automáticamente.
- Si no hay ningún enlace de descarga directa disponible,, un botón **Abrir la página** se muestra y la página de la release en GitHub se abre en el navegador predeterminado.

**Para desactivar las comprobaciones automáticas:** Deshabilitar la opción **Buscar actualizaciones automáticamente al iniciar** desde el Menú NVDA → Preferencias → Opciones → freeAudio.

## Agradecimientos & Créditos

* **Fundamentos y conceptos originales:** Un sincero agradecimiento a **Gary Mp** ([GaryMp/freeradio](https://github.com/GaryMp/freeradio)) por los conceptos originales del complemento de radio y las estructuras principales de gestión de favoritos que sirvieron como base fundamental para este proyecto.
* **Herramientas de IA y LLM:** Agradecemos sinceramente a las herramientas modernas de modelos de lenguaje a gran escala (LLM, por sus siglas en inglés) (incluidas Claude, ChatGPT y Gemini) por su ayuda durante las fases de desarrollo, refactorización de código e implementación de funciones.
* **Servicio de directorio:** Directorio de estaciones impulsado por la [API de Radio Browser](https://www.radio-browser.info/).
* **Comunidad:** Nuestro más sincero agradecimiento a todos los miembros de la comunidad NVDA y a los traductores por su continuo apoyo, comentarios y contribuciones a la localización.

## Licencia

GPL v2