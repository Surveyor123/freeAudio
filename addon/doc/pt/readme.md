# freeAudio — Complemento para o NVDA

freeAudio é um complemento completo de rádio pela Internet, podcasts, audiolivros e jukebox local para o leitor de ecrã NVDA. O que começou como uma forma simples de transmitir estações de rádio pela Internet tornou-se um centro de escuta completo e totalmente acessível — cada ecrã, caixa de diálogo e controlo é concebido de raiz para uso com teclado e leitor de ecrã, sem necessidade de rato em momento algum.

## O Que o freeAudio Pode Fazer

- **Rádio pela Internet** — Navegue e pesquise mais de 50 000 estações no diretório [Radio Browser](https://www.radio-browser.info/), com resultados complementados por TuneIn e iHeartRadio. Guarde favoritos, reordene-os e aceda diretamente a qualquer um deles com um atalho de teclado global a partir de qualquer parte do Windows — veja [Diretório Radio Browser](#diretório-radio-browser) e [Favoritos](#favoritos).
- **Podcasts** — Subscreva qualquer feed RSS/Atom, ou pesquise no diretório de podcasts da Apple e pré-visualize episódios antes de subscrever. A posição de reprodução é guardada automaticamente e retoma onde ficou — veja [Podcasts](#podcasts).
- **Audiolivros** — Pesquise e transmita ou descarregue livros de três fontes: [GETEM](https://getem.boun.edu.tr/), a biblioteca digital da Universidade de Boğaziçi para pessoas com deficiência visual, [LibriVox](https://librivox.org/), o projeto de audiolivros de domínio público lidos por voluntários, e a Coleção de Audiolivros Abertos do Project Gutenberg — os dois últimos não requerem conta — com retoma automática em obras de várias partes — veja [Audiolivros (GETEM, LibriVox e Project Gutenberg)](#audiolivros-getem-librivox-e-project-gutenberg).
- **Jukebox local** — Pesquise ficheiros de áudio armazenados em qualquer unidade ligada pelo nome do ficheiro, ou construa uma biblioteca pessoal de ficheiros e pastas, e reproduza-os com as mesmas ferramentas de retoma, procura, velocidade e transposição que os podcasts e audiolivros usam — veja [Jukebox local](#jukebox-local).
- **Marcadores** — Coloque um marcador na posição atual de qualquer parte de um audiolivro, episódio de podcast ou faixa do jukebox e volte a ela quando quiser. Um marcador pode ter uma nota de texto ou uma nota de voz gravada, reproduzida quando a reprodução chega a esse ponto, e a secção entre dois marcadores pode ser repetida — veja [Marcadores](#marcadores).
- **Gravação** — Grave de imediato o que está a tocar, grave uma única música do princípio ao fim, grave todas as músicas de uma estação, cada uma no seu próprio ficheiro, até parar, ou agende gravações únicas e recorrentes — tudo sem interromper a reprodução — veja [Gravação](#gravação).
- **Time-Shift (recuar na rádio em direto)** — Pause e recue numa estação em direto como um DVR, e depois volte ao direto sempre que quiser — veja [Time-Shift (Recuar na Rádio em Direto)](#time-shift-recuar-na-rádio-em-direto).
- **Reconhecimento musical e músicas gostadas** — Identifique faixas sem metadados usando reconhecimento baseado em Shazam, guarde músicas gostadas num ficheiro de texto e consulte as suas letras — veja [Reconhecimento Musical](#reconhecimento-musical) e [Músicas Gostadas](#músicas-gostadas).
- **Perfis e efeitos de áudio** — Guarde definições separadas de volume, efeitos, equalizador e velocidade de reprodução por estação, por podcast, por audiolivro ou por faixa de jukebox, e aplique efeitos em tempo real (Chorus, Reverb, reforços de equalizador e mais) através do motor BASS — veja [Perfil de Áudio da Estação](#perfil-de-áudio-da-estação).
- **Transposição (alteração de tom)** — Desloque o tom de podcasts, audiolivros e faixas de jukebox para cima ou para baixo sem alterar a sua velocidade, usando o componente `bass_fx` incluído — veja [Transposição (Alteração de Tom)](#transposição-alteração-de-tom).
- **Espelhamento de áudio** — Envie o mesmo fluxo para dois dispositivos de saída de áudio em simultâneo, como colunas e auscultadores ao mesmo tempo — veja [Espelho de Áudio](#espelho-de-áudio).
- **Modo Obligato (música de fundo)** — Reproduza em ciclo uma estação favorita escolhida discretamente em segundo plano, no seu próprio dispositivo de saída e volume, independentemente do que estiver (ou não) a tocar como média principal — veja [Modo de Música de Fundo (Obligato)](#modo-de-música-de-fundo-obligato).
- **Temporizadores** — Agende o início da reprodução de uma estação favorita, ou agende a paragem da reprodução, a uma hora específica — veja [Temporizador](#temporizador).
- **Acesso profundo por teclado e braille** — Todas as funcionalidades são acessíveis inteiramente pelo teclado, com atalhos globais que funcionam a partir de qualquer parte do Windows (incluindo `Ctrl+Win+F3` / `Ctrl+Win+F4` para saltar entre estações, episódios, livros e faixas sem abrir a janela), teclas de atalho diretas para estações favoritas, entradas do jukebox e audiolivros individuais, e saída braille opcional para todas as notificações faladas do freeAudio.

## Diretório Radio Browser

freeAudio utiliza a base de dados aberta [Radio Browser](https://www.radio-browser.info/) para o seu catálogo de estações. O Radio Browser é um diretório gratuito gerido pela comunidade com mais de 50.000 estações de rádio online de todo o mundo. Não é necessário registo e a API é aberta a todos. Cada estação inclui endereço, país, género, idioma e bitrate; as estações são classificadas por votos dos utilizadores. O freeAudio liga-se à API através de servidores espelho localizados na Alemanha, Países Baixos e Áustria; se um servidor estiver inacessível, muda automaticamente para o seguinte.

Para manter o navegador rápido e evitar sobrecarregar a API a cada pesquisa ou mudança de país, o freeAudio mantém uma cache local do catálogo de estações em disco. Esta cache é atualizada automaticamente em segundo plano de forma periódica, pelo que a lista apresentada está normalmente já atualizada sem qualquer ação da sua parte. Também pode forçar uma nova sincronização imediata a qualquer momento com o botão **Atualizar Lista de Estações** — consulte Navegador de Estações abaixo.

## Adicionar uma Estação ao Radio Browser

Se a estação que procura não estiver no diretório Radio Browser, pode submetê-la em [https://www.radio-browser.info/add](https://www.radio-browser.info/add). Não é necessária conta nem registo.

Preencha o formulário da página:

- **URL da transmissão (Stream URL)** *(obrigatório)* — o endereço direto da transmissão de áudio, terminado em `.mp3`, `.aac`, `.ogg` ou semelhante. Não é o endereço do site da estação, mas sim o endereço bruto da transmissão que colaria num leitor multimédia. A maioria das estações publica o URL da transmissão no seu site ou na secção "Ouvir em direto".
- **Nome da estação** *(obrigatório)* — o nome da estação tal como deve aparecer no diretório.
- **Página inicial** — o endereço do site da estação.
- **País e idioma** — selecione o país de emissão e o idioma a partir das listas pendentes.
- **Etiquetas** — palavras-chave de género ou tema separadas por vírgulas, por exemplo `notícias`, `jazz`, `clássica`. São utilizadas para pesquisa e filtragem.
- **URL do logótipo** — uma ligação direta à imagem do logótipo da estação, se disponível.

Após a submissão, a estação é revista e adicionada ao diretório público. Uma vez aceite, aparecerá automaticamente nas pesquisas e nas listagens por país do freeAudio, uma vez que o diretório é atualizado a partir da API em tempo real.

## Requisitos

- NVDA 2025.1	 ou posterior
- Windows 10 ou posterior
- Ligação à Internet

## Instalação

Descarregue o ficheiro `.nvda-addon`, prima Enter sobre ele e reinicie o NVDA quando solicitado.

## Atalhos de Teclado

Todos os atalhos podem ser reatribuídos em Menu NVDA → Preferências → Definir comandos → freeAudio. Estes atalhos funcionam em qualquer lugar, independentemente da janela que estiver em foco.

Alguns destes atalhos sobrepõem-se a atalhos que o próprio Windows usa. Se preferir manter o atalho do próprio Windows sem reatribuir o do freeAudio, prima `NVDA+F2` (Passar a tecla seguinte) imediatamente antes da combinação de teclas — o NVDA enviará essa combinação de teclas diretamente para o Windows em vez de a intercetar para o freeAudio.

| Atalho | Função | Descrição |
|---|---|---|
| `Ctrl+Win+R` | Abrir navegador de estações | Abre a janela do navegador se estiver fechada, ou traz-a para primeiro plano se já estiver aberta. |
| `Ctrl+Win+O` | Abrir separador Podcasts | Abre o navegador de estações (se fechado) ou traz-o para primeiro plano, e muda diretamente para o separador **Podcasts**. |
| `Ctrl+Win+L` | Abrir separador Audiolivros | Abre o navegador de estações (se fechado) ou traz-o para primeiro plano, e muda diretamente para o separador **Audiolivros**. |
| `Ctrl+Win+U` | Abrir separador Jukebox | Abre o navegador de estações (se fechado) ou traz-o para primeiro plano, e muda diretamente para o separador **Jukebox**, focado na caixa de pesquisa de disco. |
| `Ctrl+Win+P` | Pausar / retomar | Pausa a estação atual se estiver a reproduzir; retoma se estiver em pausa. Se nada estiver a reproduzir, inicia a última estação ou abre a lista de favoritos conforme a definição. Premir duas vezes rapidamente salta diretamente para um separador à escolha. Premir três vezes pode desencadear uma ação separada conforme a definição. |
| `Ctrl+Win+S` | Parar | Para completamente a estação atual e reinicia o leitor. |
| `Ctrl+Win+→` | Próximo favorito | Avança para a próxima estação na lista de favoritos. Volta ao início no final da lista. |
| `Ctrl+Win+←` | Favorito anterior | Recua para a estação anterior na lista de favoritos. Salta para o fim quando está no início. |
| `Ctrl+Win+F3` | Item anterior | A tecla `F3` do Navegador de Estações, disponível com a janela fechada. O que faz depende do que está a ser reproduzido: **rádio** — estação anterior; **podcast** — episódio anterior; **audiolivro** — livro anterior; **jukebox** — faixa anterior na pasta. Anuncia «Já está no primeiro …» no início de uma lista. Se nada estiver a ser reproduzido, a tecla é passada sem alterações. Consulte [Saltar Itens com o Navegador de Estações Fechado](#saltar-itens-com-o-navegador-de-estações-fechado). |
| `Ctrl+Win+F4` | Item seguinte | A tecla `F4` do Navegador de Estações, disponível com a janela fechada: estação seguinte, episódio de podcast, audiolivro ou faixa do jukebox, consoante o que estiver a ser reproduzido. |
| `Ctrl+Win+Shift+F3` | Feed / parte / entrada anterior | A tecla `Shift+F3` do Navegador de Estações, disponível com a janela fechada: **rádio** — estação anterior (igual a `Ctrl+Win+F3`); **podcast** — podcast subscrito anterior; **audiolivro** — parte anterior do livro; **jukebox** — entrada anterior do jukebox (ficheiro ou pasta). |
| `Ctrl+Win+Shift+F4` | Feed / parte / entrada seguinte | A tecla `Shift+F4` do Navegador de Estações, disponível com a janela fechada: estação seguinte, podcast subscrito, parte de audiolivro ou entrada do jukebox, consoante o que estiver a ser reproduzido. |
| `Ctrl+Win+↑` | Aumentar volume | Aumenta o volume em 5; máximo 200. |
| `Ctrl+Win+↓` | Diminuir volume | Diminui o volume em 5; mínimo 0. |
| `Ctrl+Win+V` | Adicionar aos favoritos / Descarregar o Média | Adiciona a estação em reprodução à lista de favoritos ou descarrega o episódio de podcast ou audiolivro em reprodução. Anuncia se a estação já está na lista ou se o média já foi descarregado. Não aplicável quando uma faixa do jukebox está a tocar: o freeAudio informa que o atalho é apenas para estações, podcasts ou audiolivros. |
| `Ctrl+Win+Shift+K` | Aumentar velocidade de reprodução | Aumenta a velocidade de reprodução de um episódio de podcast, audiolivro ou faixa de jukebox em 0,1× (preservando o tom). Intervalo: 0,5× a 2,0×. |
| `Ctrl+Win+Shift+J` | Diminuir velocidade de reprodução | Diminui a velocidade de reprodução em 0,1×. |
| `Shift+Win+K` | Transpor para cima | Aumenta o tom de um episódio de podcast, audiolivro ou faixa de jukebox em passos de 1/8 de tom inteiro (0,25 semitons), sem alterar a velocidade. Intervalo: −12,00 a +12,00 semitons. Veja [Transposição (Alteração de Tom)](#transposição-alteração-de-tom). |
| `Shift+Win+J` | Transpor para baixo | Diminui o tom em passos de 1/8 de tom inteiro, sem alterar a velocidade. |
| `Ctrl+Win+F12` | Adicionar marcador | Adiciona um marcador na posição de reprodução atual de uma parte de audiolivro, episódio de podcast ou faixa do jukebox. Não está disponível para estações de rádio em direto. Veja [Marcadores](#marcadores). |
| `Ctrl+Win+I` | Informação da estação | Anuncia o nome da estação, episódio de podcast, audiolivro ou faixa de jukebox em reprodução. Premir duas vezes mostra detalhes como país, género e bitrate numa caixa de diálogo. Premir três vezes copia as informações da faixa atual (metadados ICY) para a área de transferência, se disponíveis; se não existirem metadados, inicia o reconhecimento musical Shazam. Premir quatro vezes força o reconhecimento musical em caso de metadados ICY incorretos. Enquanto uma gravação está em curso, o seu nome também é anunciado; durante a gravação de todas as músicas, é a música que está a ser gravada nesse momento. |
| `Ctrl+Win+M` | Espelho de áudio | Espelha o fluxo ou média atual para um dispositivo de saída de áudio adicional em simultâneo. Prima novamente para parar o espelhamento. |
| `Ctrl+Win+Shift+M` | Modo Obligato (música de fundo) | Reproduz em ciclo uma estação favorita escolhida discretamente em segundo plano, no seu próprio dispositivo de saída e volume, independentemente do que estiver a tocar no leitor principal. A primeira pressão abre uma caixa de diálogo para escolher a estação, o dispositivo de saída e o volume relativo. Prima novamente para o parar. |
| `Ctrl+Win+E` | Gravação (instantânea / música / todas as músicas) | Prima uma vez para começar a gravar a estação atual; prima novamente para parar. Prima **duas vezes** para gravar **a música atual**: o ficheiro recebe o nome da faixa e a gravação pára sozinha quando a faixa muda. Prima **três vezes** para gravar **todas as músicas** até parar: cada música é guardada no seu próprio ficheiro. Para parar uma gravação de música ou de todas as músicas, prima duas vezes. A reprodução continua sem interrupções em todos os modos de gravação. A gravação de música e de todas as músicas só funciona em estações que enviam os títulos das faixas (metadados ICY) dentro do fluxo; a gravação de todas as músicas não funciona em estações HLS (`.m3u8`). Veja [Gravação](#gravação). |
| `Ctrl+Win+W` | Abrir pasta de gravações | Abre a pasta com os ficheiros gravados no Explorador de Ficheiros. |
| `Ctrl+Win+J` | Time-shift recuar / avançar em podcast, audiolivro e jukebox | Para rádio em direto: recua 15 segundos. A primeira pressão entra no modo time-shift; cada pressão adicional retrocede mais 15 segundos, até ao limite do buffer definido nas definições do freeAudio. Requer que o buffer de time-shift esteja ativado nas Definições. Para um episódio de podcast, audiolivro ou faixa de jukebox, esta tecla procura dentro do ficheiro, e escala com a forma como a prime: **manter premida** avança ou recua 5 segundos por repetição; **um toque deliberado** recua 12 segundos; **dois toques** em rápida sucessão recuam 1 minuto; **três ou mais toques** recuam 5 minutos. Apenas ocorre uma procura por sequência de toques, dimensionada pelo número de toques — os toques não se somam. Funciona independentemente da definição de time-shift. |
| `Ctrl+Win+K` | Time-shift avançar / procurar à frente em podcast, audiolivro e jukebox | Para rádio em direto: avança 15 segundos enquanto em time-shift. Ao atingir a margem do direto, a reprodução regressa automaticamente ao direto e este comando não tem efeito até retroceder novamente. Para um episódio de podcast, audiolivro ou faixa de jukebox, esta tecla procura à frente dentro do ficheiro usando a mesma escala de toque/manter premido que `Ctrl+Win+J` acima (manter = 5 segundos por repetição; 1 toque = 12 segundos; 2 toques = 1 minuto; 3+ toques = 5 minutos). Funciona independentemente da definição de time-shift. |
| `Ctrl+Win+Alt+J` | Retrocesso fino (1 segundo) | Retrocede exatamente 1 segundo, para pequenas correções. Num podcast, audiolivro ou faixa do jukebox recua 1 segundo no ficheiro; na rádio em direto recua 1 segundo no buffer de time-shift (o buffer de time-shift tem de estar ativo e a primeira pressão entra no modo de time-shift, como `Ctrl+Win+J`). Veja [Busca Precisa (1 Segundo)](#busca-precisa-1-segundo). |
| `Ctrl+Win+Alt+K` | Avanço fino (1 segundo) | Avança exatamente 1 segundo. Num podcast, audiolivro ou faixa do jukebox avança 1 segundo no ficheiro; na rádio em direto avança 1 segundo enquanto está em time-shift. Veja [Busca Precisa (1 Segundo)](#busca-precisa-1-segundo). |
| `Ctrl+Win+T` | Alternar buffer de time-shift | Ativa ou desativa o buffer de time-shift instantaneamente, refletindo a caixa de verificação nas Definições. Ao desativar, regressa imediatamente ao direto se estiver em modo time-shift e interrompe a captura em segundo plano. Sem efeito na reprodução de podcasts, audiolivros ou jukebox. |
| *(não atribuído)* | Selecionar dispositivo de saída | Abre uma lista a pedido dos principais dispositivos de saída disponíveis. A lista só é apresentada quando o BASS deteta mais do que um dispositivo de saída físico. Atribua uma combinação de teclas em Menu NVDA → Preferências → Definir comandos → freeAudio. |
| *(não atribuído)* | Alternar silenciamento de notificações | Ativa ou desativa o silenciamento de notificações em tempo real. Atribua uma combinação de teclas em Menu NVDA → Preferências → Definir comandos → freeAudio. |
| *(não atribuído)* | Reproduzir estação favorita diretamente | Cada estação da lista de favoritos aparece como uma entrada separada em Menu NVDA → Preferências → Definir comandos → **freeAudio Stations**. Atribua um atalho de teclado a qualquer estação para a iniciar imediatamente a partir de qualquer lugar, sem abrir o navegador. |
| *(não atribuído)* | Reproduzir entrada do jukebox diretamente | Cada ficheiro ou pasta da sua lista do Jukebox aparece como uma entrada separada em Menu NVDA → Preferências → Definir comandos → **freeAudio Jukebox**. Consulte [Atalhos de Teclado Diretos para Entradas do Jukebox](#atalhos-de-teclado-diretos-para-entradas-do-jukebox). |
| *(não atribuído)* | Reproduzir audiolivro diretamente | Cada livro da sua biblioteca de Audiolivros — do GETEM, LibriVox ou Project Gutenberg — aparece como uma entrada separada em Menu NVDA → Preferências → Definir comandos → **freeAudio Audio Books**. Atribua um atalho de teclado a qualquer livro para o retomar imediatamente a partir de qualquer lugar, sem abrir o navegador. Consulte [Atalhos de Teclado Diretos para Audiolivros](#atalhos-de-teclado-diretos-para-audiolivros). |

`Ctrl+Win+→` / `Ctrl+Win+←` apenas navegam na lista de favoritos; não funcionam com a lista de todas as estações — use `Ctrl+Win+F4` / `Ctrl+Win+F3` (ver abaixo) para percorrer a lista a partir da qual a estação atual foi iniciada. Quando uma lista está em foco na janela do navegador, as teclas de seta esquerda e direita têm a mesma função — consulte Atalhos na Caixa de Diálogo.

### Saltar Itens com o Navegador de Estações Fechado

No Navegador de Estações, `F3`, `F4`, `Shift+F3` e `Shift+F4` fazem coisas diferentes consoante o separador ativo. As versões globais — `Ctrl+Win+F3`, `Ctrl+Win+F4`, `Ctrl+Win+Shift+F3` e `Ctrl+Win+Shift+F4` — funcionam a partir de qualquer parte do Windows, esteja a janela aberta ou não. Sem um separador para consultar, o freeAudio decide pelo **que está a ser reproduzido neste momento**:

| A reproduzir | `Ctrl+Win+F3` / `Ctrl+Win+F4` | `Ctrl+Win+Shift+F3` / `Ctrl+Win+Shift+F4` |
|---|---|---|
| Estação de rádio | Estação anterior / seguinte na lista a partir da qual foi iniciada pela última vez (resultados de Todas as Estações ou Favoritos), voltando ao início nas extremidades. Se a estação não estiver nessa lista, é usada a lista de favoritos. | Igual ao comando sem `Shift`. |
| Episódio de podcast | Episódio anterior / seguinte do mesmo feed. | Podcast subscrito anterior / seguinte. Como não há uma lista onde destacar um feed, é reproduzido o seu primeiro episódio listado. |
| Audiolivro | Livro anterior / seguinte na biblioteca, retomando na parte que ouviu por último. | Parte anterior / seguinte do livro atual. |
| Faixa do jukebox | Faixa anterior / seguinte da pasta em reprodução. | Entrada anterior / seguinte na lista do Jukebox; uma pasta retoma onde foi deixada da última vez. |

Algumas coisas a saber:

- Se nada estiver a ser reproduzido, a combinação de teclas é passada ao Windows sem alterações, tal como `Ctrl+Win+→` / `Ctrl+Win+←`.
- Em qualquer extremidade de uma lista (exceto no rádio, que volta ao início), o NVDA anuncia «Já está no primeiro …» ou «Já está no último …» e nada muda. Uma faixa do jukebox que não foi iniciada como parte de uma pasta não tem vizinhas, pelo que comunica o mesmo.
- **O avanço automático não é interrompido.** Depois de saltar dentro de uma pasta do jukebox ou de um audiolivro, a faixa ou parte seguinte continua a arrancar sozinha quando a atual termina, com o Navegador de Estações aberto ou fechado. Premir «seguinte» na última faixa de uma pasta não repõe a posição guardada da pasta.
- A lista de episódios de um podcast só é mantida em memória durante a sessão atual do NVDA. Se ainda não tiver sido carregada — por exemplo, logo após o arranque do NVDA —, o NVDA pede-lhe que abra o Navegador de Estações e selecione esse podcast uma vez; depois disso, as teclas funcionam com a janela fechada.
- Se o Navegador de Estações estiver aberto, saltar um audiolivro pelo teclado atualiza também o livro e a parte «em reprodução» da janela, para que o seu próprio avanço automático continue a partir do sítio certo.

Tal como todos os comandos do freeAudio, estes podem ser reatribuídos em Menu NVDA → Preferências → Definir comandos → freeAudio.

## Navegador de Estações

O freeAudio adiciona também um submenu **freeAudio** ao menu Ferramentas do NVDA, a partir do qual pode abrir diretamente o Navegador de Estações e as Definições do freeAudio.

A janela aberta com `Ctrl+Win+R` contém oito separadores: Todas as Estações, Favoritos, Gravação, Temporizador, Músicas Gostadas, Podcasts, Audiolivros e Jukebox. Pode navegar entre separadores com `Ctrl+Tab` ou usando `Alt+1` a `Alt+8`. Os separadores Podcasts, Audiolivros e Jukebox podem ser desativados com a definição **Módulos** (veja [Definições](#definições)); os separadores desativados não são apresentados.

Quando o separador Todas as Estações abre, as 1.000 estações mais votadas são carregadas automaticamente a partir do Radio Browser. Selecionar um país na lista pendente atualiza a lista para mostrar as estações desse país. Escrever no campo de pesquisa executa automaticamente uma pesquisa completa na base de dados Radio Browser em simultâneo por nome, país e género.

Ao pesquisar, os resultados do Radio Browser são complementados com estações do TuneIn e iHeartRadio (quando disponíveis). Estas fontes externas são pesquisadas em segundo plano e os seus resultados são fundidos automaticamente na lista, dando-lhe acesso a ainda mais estações sem qualquer ação extra.

A lista pendente **Dispositivo de saída** na parte inferior da janela do navegador — fora dos separadores — lista todos os dispositivos de saída de áudio reconhecidos pelo BASS. Selecionar um dispositivo redireciona imediatamente o áudio para ele e guarda a escolha permanentemente; o mesmo dispositivo é utilizado automaticamente na próxima sessão. Se o dispositivo selecionado não estiver ligado, o complemento reverte automaticamente para a predefinição do sistema. Prima `F11` para abrir um seletor de dispositivo mais simples a pedido, a partir de qualquer lugar no Navegador de Estações. O seletor não é mostrado automaticamente e abre apenas quando o BASS deteta mais do que um dispositivo de saída físico. Quando apenas um está disponível, nenhuma seleção é necessária e o freeAudio usa a saída predefinida do sistema.

Os controlos **Volume** (0–200) e **Efeitos** na mesma área podem ser ajustados em qualquer altura com a janela aberta. Na lista de Efeitos, é possível ativar simultaneamente Chorus, Compressor, Distortion, Echo, Flanger, Gargle, Reverb, EQ: Bass Boost, EQ: Treble Boost e EQ: Vocal Boost; as alterações são aplicadas à transmissão ativa instantaneamente. Cada efeito também pode ser ativado ou desativado instantaneamente com `Ctrl+1` a `Ctrl+0`, sem largar o teclado — consulte Atalhos de Efeitos abaixo.

Quando um ou mais efeitos EQ estão ativos, surge automaticamente um **controlo de ganho** para cada banda ativa. O ganho pode ser ajustado entre −15 dB e +15 dB; os valores predefinidos são Graves +9 dB, Agudos +9 dB e Vocal +6 dB. Os controlos só aparecem para as bandas EQ selecionadas e ocultam-se automaticamente quando o efeito é desmarcado. Os valores são guardados permanentemente e restaurados na sessão seguinte.

O botão **Reproduzir/Pausar** encontra-se também na parte inferior da janela. Se nenhuma estação estiver a reproduzir, inicia a estação selecionada; se uma estação já estiver em reprodução, pausa a reprodução.

O botão **Atualizar Lista de Estações** sincroniza imediatamente o catálogo local de estações com a API do Radio Browser, em vez de esperar pela atualização periódica em segundo plano. Enquanto a atualização decorre, o botão fica desativado e o NVDA anuncia que está a decorrer uma atualização; se voltar a premi-lo antes de a atualização atual terminar, o NVDA informa que já está uma em curso. Assim que a atualização termina, o NVDA anuncia que a lista de estações foi atualizada e os resultados de pesquisa ou a listagem de país atualmente apresentados são atualizados automaticamente para refletir os novos dados.

Quando uma estação está selecionada na lista, o botão **Detalhes da Estação** apresenta informações como país, idioma, género, formato, bitrate, website e URL da transmissão numa caixa de diálogo separada. Cada campo aparece na sua própria caixa de texto só de leitura; pode mover-se entre campos com Tab e copiar todas as informações para a área de transferência de uma só vez com o botão **Copiar tudo para a área de transferência**. Este botão está disponível nos separadores Todas as Estações e Favoritos.

### Menu de Contexto da Estação

Clique com o botão direito numa estação na lista Todas as Estações ou Favoritos, ou selecione-a e prima a tecla Aplicações ou `Shift+F10`, para abrir um menu de contexto com ações rápidas:

- **Detalhes da Estação** — igual ao botão Detalhes da Estação descrito acima.
- **Adicionar aos Favoritos** *(separador Todas as Estações)* / **Eliminar Estação** *(separador Favoritos)*.
- **Mudar Nome da Estação** *(separador Favoritos)* — igual a `F9`.
- **Guardar Perfil de Áudio para Esta Estação** / **Limpar Perfil de Áudio** *(separador Favoritos)* — ver Perfil de Áudio da Estação.
- **Testar URL** — verifica se a transmissão da estação selecionada está atualmente acessível, sem iniciar a reprodução, e anuncia o resultado (acessível, ou o motivo da falha, como um erro HTTP ou um tempo limite de rede).

Apenas os itens relevantes para o separador e seleção atuais são apresentados como disponíveis.

### Atalhos na Caixa de Diálogo

As teclas seguintes funcionam apenas quando a janela do Navegador de Estações está ativa.

#### Teclas F

| Atalho | Função | Descrição |
|---|---|---|
| `F1` | Guia de ajuda | Abre o ficheiro de ajuda do complemento no browser predefinido. É pesquisado primeiro o guia para o idioma do NVDA ativo; se não for encontrado, abre o guia predefinido. |
| `F2` | Informação da estação | Anuncia o nome da estação em reprodução. Premir duas vezes mostra detalhes como país, género e bitrate numa caixa de diálogo. Premir três vezes copia as informações da faixa atual (metadados ICY) para a área de transferência, se disponíveis; se não existirem metadados, inicia o reconhecimento musical Shazam. Premir quatro vezes força o reconhecimento musical em caso de metadados ICY incorretos. Enquanto uma gravação está em curso, o seu nome também é anunciado. |
| `F3` | Item anterior | No separador Todas as Estações ou Favoritos: recua para a estação anterior e inicia a reprodução imediatamente. No separador Podcasts: recua para o episódio anterior e reproduz-o. No separador Audiolivros: recua para o livro anterior e começa a reproduzi-lo. No separador Jukebox: recua para a faixa anterior no item de jukebox selecionado e reproduz-a. No separador Jukebox, numa pasta, as faixas seguintes continuam a arrancar automaticamente. O equivalente global é `Ctrl+Win+F3` — consulte [Saltar Itens com o Navegador de Estações Fechado](#saltar-itens-com-o-navegador-de-estações-fechado). |
| `F4` | Próximo item | No separador Todas as Estações ou Favoritos: avança para a próxima estação e inicia a reprodução imediatamente. No separador Podcasts: avança para o próximo episódio e reproduz-o. No separador Audiolivros: avança para o próximo livro e começa a reproduzi-lo. No separador Jukebox: avança para a próxima faixa no item de jukebox selecionado e reproduz-a. No separador Jukebox, numa pasta, as faixas seguintes continuam a arrancar automaticamente. O equivalente global é `Ctrl+Win+F4`. |
| `Shift+F3` | Feed / parte / item anterior | No separador Podcasts: sobe um feed na lista de subscrições. No separador Audiolivros: recua para a parte anterior do livro em reprodução. No separador Jukebox: sobe uma entrada de jukebox (ficheiro ou pasta) na lista principal. O equivalente global é `Ctrl+Win+Shift+F3`, que também reproduz a entrada. |
| `Shift+F4` | Próximo feed / parte / item | No separador Podcasts: desce um feed na lista de subscrições. No separador Audiolivros: avança para a próxima parte do livro em reprodução. No separador Jukebox: desce uma entrada de jukebox na lista principal. O equivalente global é `Ctrl+Win+Shift+F4`, que também reproduz a entrada. |
| `F5` | Diminuir volume | Diminui o volume em 5 (mínimo 0). |
| `F6` | Aumentar volume | Aumenta o volume em 5 (máximo 200). |
| `F7` | Pausar / retomar | Pausa se uma estação estiver a reproduzir; retoma se estiver em pausa e os média estiverem carregados. |
| `F8` | Parar | Para completamente a estação atual e reinicia o leitor. |
| `F9` | Renomear | Abre a caixa de diálogo de renomeação para a estação em foco no separador Favoritos. |
| `F11` | Selecionar dispositivo de saída | Abre o seletor principal de dispositivo de saída quando o BASS deteta mais do que um dispositivo de saída físico. O dispositivo atual é pré-selecionado; Enter aplica e guarda a escolha. |
| `F12` | Adicionar marcador | Adiciona um marcador na posição de reprodução atual de uma parte de audiolivro, episódio de podcast ou faixa do jukebox — o equivalente dentro da janela de `Ctrl+Win+F12`. Veja [Marcadores](#marcadores). |

#### Atalhos de Lista e Navegação

| Atalho | Função | Descrição |
|---|---|---|
| `→` | Próximo item / Avançar | Numa lista de estações (Todas as Estações / Favoritos), avança para a próxima estação e reproduz-a imediatamente, voltando ao início no final da lista. Nas listas de itens de Podcasts, Audiolivros ou Jukebox, enquanto algo está carregado e a reproduzir, avança na faixa em vez disso — o mesmo que o comando global `Ctrl+Win+K` (ver Navegação escalonada acima). Na lista de episódios de Podcasts em particular, se ainda não houver nada carregado, volta a avançar para o próximo episódio e a reproduzi-lo. O mesmo se aplica às listas de marcadores por baixo destas listas (veja [Marcadores](#marcadores)). |
| `←` | Item anterior / Retroceder | Numa lista de estações, recua para a estação anterior e reproduz-a, saltando para o fim quando está no início. Nas listas de itens de Podcasts, Audiolivros ou Jukebox, enquanto algo está carregado e a reproduzir, retrocede na faixa em vez disso — o mesmo que o comando global `Ctrl+Win+J`. Na lista de episódios de Podcasts, se ainda não houver nada carregado, volta a recuar para o episódio anterior e a reproduzi-lo. O mesmo se aplica às listas de marcadores por baixo destas listas (veja [Marcadores](#marcadores)). |
| `Shift+→` | Transpor para cima | Nas listas de itens de Podcasts, Audiolivros ou Jukebox: aumenta o tom da reprodução atual em um semitom, o mesmo que o comando global `Shift+Win+K`. O mesmo se aplica às listas de marcadores por baixo destas listas (veja [Marcadores](#marcadores)). |
| `Shift+←` | Transpor para baixo | Nas listas de itens de Podcasts, Audiolivros ou Jukebox: diminui o tom da reprodução atual em um semitom, o mesmo que o comando global `Shift+Win+J`. O mesmo se aplica às listas de marcadores por baixo destas listas (veja [Marcadores](#marcadores)). |
| `Page Up` | Aumentar velocidade de reprodução | Nas listas de itens de Podcasts, Audiolivros ou Jukebox: aumenta a velocidade de reprodução, o mesmo que o comando global `Ctrl+Win+Shift+K`. O mesmo se aplica às listas de marcadores por baixo destas listas (veja [Marcadores](#marcadores)). |
| `Page Down` | Diminuir velocidade de reprodução | Nas listas de itens de Podcasts, Audiolivros ou Jukebox: diminui a velocidade de reprodução, o mesmo que o comando global `Ctrl+Win+Shift+J`. O mesmo se aplica às listas de marcadores por baixo destas listas (veja [Marcadores](#marcadores)). |
| `Alt+→` | Avanço fino (1 segundo) | Em qualquer separador do Navegador de Estações, quando algo está carregado: avança exatamente 1 segundo, tal como o comando global `Ctrl+Win+Alt+K`. Veja [Busca Precisa (1 Segundo)](#busca-precisa-1-segundo). |
| `Alt+←` | Retrocesso fino (1 segundo) | Em qualquer separador do Navegador de Estações, quando algo está carregado: retrocede exatamente 1 segundo, tal como o comando global `Ctrl+Win+Alt+J`. |
| `Ctrl+→` | Próximo episódio / livro / faixa | No separador Podcasts: avança para o próximo episódio e reproduz-o. No separador Audiolivros (lista da biblioteca em foco): avança para o próximo livro. No separador Jukebox (lista de entradas ou de faixas em foco): avança para a próxima faixa no item de jukebox selecionado e reproduz-a. |
| `Ctrl+←` | Episódio / livro / faixa anterior | No separador Podcasts: recua para o episódio anterior e reproduz-o. No separador Audiolivros: recua para o livro anterior. No separador Jukebox: recua para a faixa anterior no item de jukebox selecionado e reproduz-a. |
| `Enter` | Reproduzir / Adicionar | Numa lista de estações ou episódios: inicia a reprodução do item selecionado imediatamente. Nos resultados de pesquisa do separador Jukebox: adiciona o ficheiro selecionado ao jukebox. Nas listas de entradas ou faixas do separador Jukebox: reproduz o item em foco diretamente. |
| `Espaço` | Reproduzir / Pausar / Pré-visualizar | Pausa se algo estiver a reproduzir; caso contrário, inicia a reprodução do item selecionado. Nos resultados de pesquisa do separador Jukebox: alterna a pré-visualização (reproduzir/parar) do ficheiro selecionado. Nas listas de entradas ou faixas do separador Jukebox: pausa se estiver a reproduzir, caso contrário reproduz o item em foco. |
| `Ctrl+Tab` | Próximo separador | Muda para o próximo separador (Todas as Estações → Favoritos → Gravação → Temporizador → Músicas Gostadas → Podcasts → Audiolivros → Jukebox). |
| `Ctrl+Shift+Tab` | Separador anterior | Volta ao separador anterior. |
| `Escape` | Ocultar | Oculta a janela; o complemento continua a reproduzir em segundo plano. |

#### Atalhos de Volume

| Atalho | Função | Descrição |
|---|---|---|
| `Ctrl+↑` | Aumentar volume | Aumenta o volume em 5. Só funciona com a janela do navegador aberta. |
| `Ctrl+↓` | Diminuir volume | Diminui o volume em 5. Só funciona com a janela do navegador aberta. |

#### Atalhos de Efeitos

| Atalho | Função | Descrição |
|---|---|---|
| `Ctrl+1` | Alternar Chorus | Ativa ou desativa o efeito Chorus e aplica-o instantaneamente à transmissão ativa. |
| `Ctrl+2` | Alternar Compressor | Ativa ou desativa o efeito Compressor e aplica-o instantaneamente à transmissão ativa. |
| `Ctrl+3` | Alternar Distortion | Ativa ou desativa o efeito Distortion e aplica-o instantaneamente à transmissão ativa. |
| `Ctrl+4` | Alternar Echo | Ativa ou desativa o efeito Echo e aplica-o instantaneamente à transmissão ativa. |
| `Ctrl+5` | Alternar Flanger | Ativa ou desativa o efeito Flanger e aplica-o instantaneamente à transmissão ativa. |
| `Ctrl+6` | Alternar Gargle | Ativa ou desativa o efeito Gargle e aplica-o instantaneamente à transmissão ativa. |
| `Ctrl+7` | Alternar Reverb | Ativa ou desativa o efeito Reverb e aplica-o instantaneamente à transmissão ativa. |
| `Ctrl+8` | Alternar EQ: Bass Boost | Ativa ou desativa a banda EQ: Bass Boost e aplica-a instantaneamente à transmissão ativa. |
| `Ctrl+9` | Alternar EQ: Treble Boost | Ativa ou desativa a banda EQ: Treble Boost e aplica-a instantaneamente à transmissão ativa. |
| `Ctrl+0` | Alternar EQ: Vocal Boost | Ativa ou desativa a banda EQ: Vocal Boost e aplica-a instantaneamente à transmissão ativa. |

Cada atalho reflete marcar ou desmarcar o item correspondente na lista **Efeitos**: o NVDA anuncia se o efeito foi ativado ou desativado, a alteração é guardada automaticamente e o controlo de ganho dessa banda (se aplicável) aparece ou desaparece em conformidade.

#### Atalhos da Tecla Alt

| Atalho | Função | Descrição |
|---|---|---|
| `Alt+R` | Ir para o campo de pesquisa | Move o foco para a caixa de texto de pesquisa. Pesquisa nome, país e género em simultâneo. |
| `Alt+V` | Adicionar / remover favorito | Adiciona a estação selecionada aos favoritos; remove-a se já estiver na lista. |
| `Alt+1` | Todas as Estações | Muda para o separador Todas as Estações. |
| `Alt+2` | Favoritos | Muda para o separador Favoritos. |
| `Alt+3` | Gravação | Muda para o separador Gravação. |
| `Alt+4` | Temporizador | Muda para o separador Temporizador. |
| `Alt+5` | Músicas Gostadas | Muda para o separador Músicas Gostadas. |
| `Alt+6` | Podcasts | Muda para o separador Podcasts. |
| `Alt+7` | Audiolivros | Muda para o separador Audiolivros. |
| `Alt+8` | Jukebox | Muda para o separador Jukebox, focado na caixa de pesquisa de disco. |
| `Alt+K` | Fechar | Fecha a janela; o complemento continua a reproduzir em segundo plano. |

## Favoritos

A lista de favoritos é uma coleção pessoal de estações guardada permanentemente. Para adicionar uma estação, selecione-a na lista e prima o botão Adicionar aos Favoritos ou use o atalho `Alt+V`. O mesmo atalho remove uma estação que já esteja na lista quando está selecionada.

Os favoritos podem ser reproduzidos com `Ctrl+Win+→` e `Ctrl+Win+←`; estes atalhos funcionam mesmo quando a janela do navegador não está aberta.

Para eliminar uma estação da lista de favoritos, selecione-a e prima o botão **Eliminar Estação** ou a tecla `Delete`. Após a eliminação, o foco e a seleção movem-se automaticamente para a estação seguinte. Se a estação eliminada era a última, o foco vai para a estação anterior. Se a lista ficar vazia, o foco vai para o botão Reproduzir.

### Marcar e Remover Vários Itens

Favoritos, Músicas Gostadas, a biblioteca de Audiolivros e a lista do Jukebox suportam marcar vários itens e removê-los juntos num único passo:

- Prima **`.`** (ponto) num item destacado para o marcar ou desmarcar. O NVDA anuncia a alteração, e a linha de um item marcado é rotulada como "(marcado)" para que o seu estado permaneça claro enquanto percorre a lista.
- Prima **`Shift+Home`** para marcar ou desmarcar todos os itens desde o atual até ao primeiro da lista, ou **`Shift+End`** para fazer o mesmo até ao último. Se o intervalo é marcado ou desmarcado é decidido pelo estado do próprio item atual, pelo que o intervalo inteiro se move sempre no mesmo sentido numa única ação. O foco passa depois para o extremo oposto do intervalo, e o NVDA anuncia quantos itens mudaram.
- Prima **`Delete`** para remover todos os itens marcados de uma só vez. Se nada estiver marcado, `Delete` continua a remover apenas o item atualmente selecionado, como antes.
- O menu de contexto do botão direito (tecla Aplicações / `Shift+F10`) de cada lista inclui um comando **Remover Selecionados**, ativo apenas quando pelo menos um item está marcado, que faz o mesmo.
- Antes de qualquer remoção, uma única caixa de diálogo de confirmação resume quantos itens estão prestes a ser removidos.

As marcas são por lista e são limpas assim que remove os itens (ou os desmarca individualmente); não são guardadas entre sessões.

As listas de marcadores dos separadores Podcasts, Audiolivros e Jukebox usam a mesma marcação com `.`, e os marcadores marcados são aqueles sobre os quais atuam os comandos **Eliminar selecionados** e **Repetir entre os marcadores marcados** — veja [Marcadores](#marcadores).

### Exportar e Importar Favoritos

O separador Favoritos inclui dois botões para fazer cópias de segurança e restaurar a sua lista de estações:

**Exportar Favoritos…** — guarda toda a sua lista de favoritos num ficheiro. Uma caixa de diálogo permite-lhe escolher entre dois formatos:

- **JSON** (`.json`) — uma cópia de segurança completa que preserva nomes de estações, URLs de transmissão e todos os metadados. Recomendado para restaurar a sua lista mais tarde ou movê-la para outro computador.
- **Lista de reprodução M3U** (`.m3u`) — um formato de lista de reprodução padrão compatível com a maioria dos leitores de multimédia e aplicações de rádio. Note que o M3U não armazena todos os metadados das estações, pelo que restaurar a partir de M3U pode resultar em menos detalhes do que uma cópia de segurança JSON.

**Importar Favoritos…** — carrega estações de um ficheiro JSON ou M3U previamente exportado. Após selecionar o ficheiro, é perguntado como adicionar as estações:

- **Sim (Intercalar)** — adiciona as estações importadas à sua lista existente sem remover os favoritos atuais. Estações duplicadas não são adicionadas duas vezes.
- **Não (Substituir)** — limpa completamente a sua lista de favoritos atual e substitui-a pelo conteúdo do ficheiro importado.
- **Cancelar** — regressa ao navegador sem efetuar quaisquer alterações.

Após uma importação bem-sucedida, a lista de favoritos, a lista de estações de gravação agendada e a lista de estações do temporizador são todas atualizadas automaticamente.

### Organizar Favoritos em Grupos

Os favoritos podem pertencer a uma pasta/grupo, apresentado como um sufixo "— Grupo" após o nome da estação na lista (por exemplo, "NPR Newscast — NPR").

- **Importar de M3U** — se o ficheiro usar a etiqueta `group-title` (a convenção usada pelo DVBViewer e pela maioria dos outros editores e leitores de M3U) para organizar estações em pastas, o freeAudio lê-a e mantém o grupo de cada estação na importação. Exportar os seus favoritos de volta para M3U escreve a mesma etiqueta, pelo que a estrutura de pastas sobrevive a uma ida e volta pelo freeAudio.
- **Atribuir ou remover um grupo manualmente** — marque um ou mais favoritos com `.` (ver [Marcar e Remover Vários Itens](#marcar-e-remover-vários-itens) acima), depois escolha **Atribuir ao Grupo…** no menu de contexto (tecla Aplicações / `Shift+F10`) e escreva um nome de grupo. Deixe o campo vazio para remover os favoritos marcados do seu grupo. Se nada estiver marcado, o comando aplica-se ao favorito atualmente selecionado.
- **Filtrar por grupo** — o campo Filtro acima da lista de favoritos também corresponde a nomes de grupos e aceita várias palavras, cada uma podendo corresponder a um campo diferente. Por exemplo, escrever `Houston Classical` encontra "Houston Public Media Classical" mesmo que essa frase exata nunca apareça em lado nenhum — "Houston" corresponde ao grupo e "Classical" corresponde ao nome da estação.

### Reordenar Favoritos

Com uma estação selecionada no separador Favoritos, prima `vírgula` para entrar no modo de mover — ouvirá um sinal sonoro. Navegue até à posição pretendida com as teclas de seta e prima `vírgula` novamente. A estação é colocada na posição escolhida e a nova ordem é guardada imediatamente. Premir `vírgula` novamente na mesma posição cancela a operação.

### Atalhos de Teclado Diretos para Estações Favoritas

Cada estação da lista de favoritos é registada como um script separado na caixa de diálogo Definir Comandos do NVDA, na categoria **freeAudio Stations**. Pode atribuir qualquer atalho de teclado a qualquer estação e premi-lo a partir de qualquer lugar — sem necessidade de abrir a janela do navegador.

Para atribuir um atalho:

1. Abra Menu NVDA → Preferências → Definir comandos.
2. Expanda a categoria **freeAudio Stations**.
3. Encontre a estação pelo nome, selecione-a e prima **Adicionar**.
4. Prima a combinação de teclas pretendida e confirme.

O atalho inicia a estação imediatamente. Se a estação for removida dos favoritos, a sua entrada desaparece da categoria e qualquer atalho atribuído é automaticamente removido pelo NVDA. Quando uma nova estação é adicionada aos favoritos, aparece na categoria de imediato — não é necessário reabrir a caixa de diálogo Definir Comandos.

### Adicionar Estação Personalizada

Para adicionar uma estação que não esteja no Radio Browser, utilize o botão Adicionar Estação Personalizada. Na caixa de diálogo que aparece, introduza o nome da estação e o URL da transmissão para a adicionar diretamente aos favoritos. As estações personalizadas podem ser reproduzidas e reordenadas tal como qualquer outro favorito.

Estão disponíveis dois botões adicionais nesta caixa de diálogo:

- **Testar URL** — verifica o URL da transmissão introduzido antes de adicionar a estação e anuncia se está acessível. Útil para detetar um erro de escrita ou uma ligação inválida antes de esta ficar na sua lista de favoritos.
- **Adicionar ao diretório Radio Browser…** — abre a [página de submissão do Radio Browser](https://www.radio-browser.info/add) no navegador predefinido, para que possa partilhar a estação com a comunidade Radio Browser assim que confirmar que funciona. Consulte Adicionar uma Estação ao Radio Browser acima para saber o que o formulário de submissão espera.

### Perfil de Áudio da Estação

O separador Favoritos inclui dois botões para gerir as definições de áudio por estação:

**Guardar Perfil de Áudio para Esta Estação** — guarda o nível de volume atual, os efeitos ativos e os valores de ganho EQ como um perfil associado a essa estação específica. Sempre que essa estação iniciar a reprodução, o volume, efeitos e ganho guardados são automaticamente aplicados, substituindo as predefinições globais.

**Limpar Perfil de Áudio** — remove o perfil de áudio guardado da estação selecionada. Após limpar, a estação reverte para as definições globais de volume, efeitos e ganho EQ. Este botão só está ativo quando a estação selecionada já tem um perfil guardado.

Ambos os botões estão localizados abaixo da lista de favoritos e só estão ativos quando uma estação da lista está selecionada.

## Reconhecimento Musical

Premir `Ctrl+Win+I` três vezes ativa o reconhecimento musical baseado em Shazam para a transmissão em reprodução. O reconhecimento só inicia quando não existem metadados ICY disponíveis; se existirem metadados, estes são copiados para a área de transferência.

O reconhecimento funciona assim: com o ffmpeg, é capturada do fluxo uma pequena amostra de áudio (o ffmpeg apresenta-se como um leitor de multimédia, pelo que as estações que recusam programas desconhecidos continuam a responder), é aplicado o algoritmo de impressões digitais do Shazam e o resultado é enviado para os servidores do Shazam. Se o reconhecimento tiver êxito, o título da música, o artista, o álbum e o ano de lançamento são anunciados pelo NVDA e copiados automaticamente para a área de transferência. Se a opção **Guardar músicas gostadas em ficheiro de texto** estiver ativa, o resultado do reconhecimento é também acrescentado ao ficheiro `likedSongs.txt`.

Se o ffmpeg não conseguir ler o fluxo diretamente — por exemplo, porque a estação recusa a sua ligação, ou porque o endereço do fluxo termina em `.nsv` (comum em servidores SHOUTcast), o que leva o ffmpeg a detetar mal o formato de áudio — o freeAudio grava ele próprio uma pequena amostra do fluxo e faz o ffmpeg descodificar esse ficheiro. Isto acontece automaticamente; não há nenhuma definição para o efeito.

**Feedback sonoro:** Dois sinais sonoros ascendentes indicam o início do reconhecimento e dois descendentes indicam o fim. Um sinal sonoro curto soa a cada 2 segundos enquanto o processo está em execução.

**Requisito:** É necessário `ffmpeg.exe`. Um `ffmpeg.exe` colocado na pasta do complemento é utilizado automaticamente; se estiver noutro local, o caminho pode ser definido nas Definições. Descarregue o ffmpeg em [ffmpeg.org](https://ffmpeg.org/download.html).

**Uma nota sobre estações que inserem anúncios:** algumas estações reproduzem um anúncio curto em cada nova ligação feita à sua transmissão, separado da emissão que já está a ouvir. O reconhecimento evita amostrar esse anúncio ao reutilizar a ligação de transmissão em segundo plano já existente do freeAudio (a mesma utilizada para o Time-Shift) em vez de abrir uma nova, identificando assim o que está realmente a tocar em vez de um anúncio. Isto funciona automaticamente e não requer configuração.

## Espelho de Áudio

O atalho `Ctrl+Win+M` duplica a transmissão atual para um segundo dispositivo de saída de áudio em simultâneo.

Na primeira pressão, aparece uma caixa de diálogo de seleção com os dispositivos de saída disponíveis. Depois de escolher um dispositivo, o espelhamento inicia e a reprodução principal continua sem interrupção. Prima o atalho novamente para parar o espelhamento.

**Casos de utilização:**

- **Colunas + auscultadores** — Permita que um convidado acompanhe a mesma transmissão nos auscultadores enquanto ouve pelas colunas do computador.
- **Configuração de gravação** — Direcione a saída principal para colunas e a segunda saída para um gravador externo ou interface de áudio para captura externa.
- **Multi-divisão** — Reproduza através de um altifalante Bluetooth e do altifalante integrado em simultâneo; não é necessário software adicional para levar o áudio para outra divisão.
- **Monitorização remota** — Numa sessão de partilha de ecrã ou ambiente de trabalho remoto, tanto o lado local como o remoto podem ouvir a mesma transmissão em simultâneo.

## Modo de Música de Fundo (Obligato)

O atalho `Ctrl+Win+Shift+M` reproduz uma estação favorita discretamente em segundo plano, num motor de áudio completamente separado do leitor principal — como um fundo musical suave a tocar por baixo do que estiver realmente a fazer.

Na primeira pressão, abre-se uma caixa de diálogo com três controlos:

- **Estação de fundo** — uma lista das suas estações favoritas para escolher qual reproduzir em ciclo em segundo plano. Requer pelo menos um favorito; se a sua lista de favoritos estiver vazia, o freeAudio pede-lhe para adicionar primeiro uma estação (`Ctrl+Win+V` enquanto uma estação está a tocar).
- **Saída de áudio** — o dispositivo através do qual a estação de fundo é reproduzida: **Igual à saída principal** (predefinição), **Predefinição do sistema**, ou qualquer dispositivo específico que o freeAudio consiga detetar.
- **Volume de fundo** — a que volume a estação de fundo toca, como percentagem do volume atual do leitor principal (25%, 50%, 75%, 100%, 125% ou 150%). As suas escolhas são memorizadas para a próxima vez.

Depois de iniciado, a estação de fundo continua a tocar independentemente do leitor principal — mudar de estação, podcast ou audiolivro no leitor principal, ou pará-lo completamente, nunca interrompe o modo Obligato. Duas coisas permanecem automaticamente ligadas ao leitor principal:

- **Volume** — o volume de fundo é mantido continuamente na percentagem escolhida do volume atual do leitor principal, pelo que aumentar ou diminuir o volume principal (`Ctrl+Win+↑`/`↓`) ajusta a música de fundo na mesma proporção.
- **Pausa** — pausar o leitor principal (`Ctrl+Win+P`) também pausa a estação de fundo, e retomar o leitor principal também a retoma. Uma paragem completa do leitor principal não é considerada uma pausa, pelo que a estação de fundo continua a tocar.

Prima `Ctrl+Win+Shift+M` novamente a qualquer momento para parar o modo Obligato.

## Gravação

As gravações são guardadas por predefinição em `Documents\freeAudio Recordings\`. O nome do ficheiro inclui o nome da estação (ou o título da canção, em modo de gravação de canção) e a hora de início da gravação. A pasta de gravações pode ser alterada em qualquer altura em Menu NVDA → Preferências → Definições → freeAudio → **Pasta de gravações**.

A definição **Formato de saída da gravação** controla como as gravações concluídas são guardadas:

- **Formato original do fluxo** escreve o fluxo exatamente como recebido. Uma emissão HLS pode, portanto, produzir um ficheiro `.ts`.
- **Apenas áudio, codec original** remove a camada de vídeo/contentor sem recodificar o áudio. Por exemplo, o áudio AAC de uma gravação HLS `.ts` é normalmente guardado como `.m4a`, preservando a qualidade da emissão.
- **MP3** converte o áudio após a gravação usando o débito binário selecionado. A conversão usa o `ffmpeg.exe` incluído no freeAudio e é executada em segundo plano para que o NVDA permaneça responsivo. Se a conversão falhar, a gravação original é mantida.

**Gravação instantânea:** Enquanto uma estação está a reproduzir, prima `Ctrl+Win+E` uma vez. Prima novamente para parar. A reprodução continua sem interrupção.

**Gravação de música (música atual):** Prima `Ctrl+Win+E` **duas vezes** rapidamente enquanto toca uma estação que emite metadados ICY. A gravação começa pouco depois da segunda pressão — o freeAudio espera um instante, caso vá premir uma terceira vez — e é nomeada com o título da música atual. Quando a estação anunciar a música seguinte, a gravação pára nesse ponto e o NVDA anuncia o nome do ficheiro guardado. Para terminar mais cedo, prima novamente `Ctrl+Win+E` duas vezes. Se a estação atual não emitir metadados ICY, a gravação de música não está disponível e o NVDA avisa-o.

**Gravação de todas as músicas:** Prima `Ctrl+Win+E` **três vezes** rapidamente para gravar todas as músicas que a estação tocar, até parar. O freeAudio mantém uma única ligação aberta e inicia um novo ficheiro em cada mudança de faixa, pelo que nada se perde entre as músicas. Cada música é guardada como um ficheiro separado, com o nome do título e da hora em que começou. Quando a gravação começa, o NVDA anuncia que está a gravar todas as músicas e diz o título atual. Para parar, prima `Ctrl+Win+E` duas vezes; o NVDA anuncia quantas músicas foram guardadas.

Alguns pormenores sobre a gravação de todas as músicas:

- A primeira música (gravada desde o momento em que premiu as teclas) e a última (cortada quando pára) estão incompletas, por isso os nomes dos seus ficheiros incluem **(partial)** — por exemplo, `Artist - Title (partial) - 2026-10-09 10-15.mp3`.
- Segmentos com menos de 15 segundos — jingles, separadores publicitários ou um título que alterna entre dois valores — são descartados em vez de guardados.
- É necessário que a estação envie os títulos das faixas dentro do próprio fluxo de áudio (metadados ICY). As estações HLS (`.m3u8`) e os servidores que não enviam títulos desta forma não podem ser divididos em músicas; o NVDA informa-o e nada é gravado.
- Durante a gravação, `Ctrl+Win+I` anuncia a música que está a ser gravada nesse momento, e não aquela com que a gravação começou.

**Gravação agendada:** Abra o separador Gravação no navegador. Selecione uma estação dos seus favoritos, introduza a hora de início no formato HH:MM e a duração em minutos, selecione um ou mais dias ativos e, em seguida, escolha o modo de repetição e o modo de gravação:

Um campo **Filtro** acima da lista de estações permite-lhe restringir a lista de favoritos em tempo real, para que possa encontrar rapidamente a estação que deseja agendar.

**Dias ativos:** Marque um ou mais dias da semana. No modo de gravação única, é criada uma entrada separada para cada dia selecionado, colocada na próxima ocorrência desse dia. No modo recorrente, a gravação repete-se apenas nos dias marcados. Se não forem selecionados dias, a gravação não está restrita a dias específicos.

**Recorrência:**

- **Gravar uma vez** — cria uma gravação única para cada dia selecionado. Cada entrada é colocada na próxima ocorrência desse dia; se a hora de hoje já tiver passado, a entrada é automaticamente transferida para a semana seguinte.
- **Repetir semanalmente** — repete-se todas as semanas nos dias ativos selecionados até ser removida da lista de agendamento.

**Guardar gravação em:** Para cada gravação agendada, pode escolher guardar na pasta de gravações predefinida ou numa pasta personalizada. Use o botão **Procurar...** para selecionar uma pasta interativamente. Se a pasta escolhida ficar indisponível, a gravação reverte para a pasta predefinida e é notificado.

**Modo de gravação:**

- **Gravar enquanto ouve** — reproduz e grava em simultâneo através do backend BASS.
- **Apenas gravar** — grava silenciosamente em segundo plano sem qualquer saída de áudio; o motor de gravação liga-se diretamente à transmissão.

Assim que um agendamento é adicionado, aparece na lista abaixo. Use o botão **Remover Selecionado** para eliminar um agendamento, ou **Editar Selecionado** para modificar a sua hora, duração, recorrência, dias ativos, modo de gravação ou pasta de saída.

O NVDA anuncia quando uma gravação inicia e quando termina. Se o NVDA for reiniciado enquanto uma gravação agendada estiver ativa, a gravação é retomada automaticamente no arranque.

**Como se ligam as gravações:** As gravações instantâneas, de música e de todas as músicas abrem a sua própria ligação à estação, em vez de copiarem o que está a ouvir; por isso, uma gravação instantânea ou de todas as músicas continua se colocar a reprodução em pausa ou mudar para outra estação — prossegue com a estação em que começou. Parar a reprodução com `Ctrl+Win+S` durante uma gravação pede primeiro confirmação, porque isso também termina a gravação. O preço da ligação separada é que uma estação que passa um breve anúncio a cada nova ligação pode colocar esse anúncio no início do ficheiro.

## Time-Shift (Recuar na Rádio em Direto)

O time-shift permite recuar na estação que está a ouvir, como um DVR ou uma cassete — pause o momento, volte uns minutos atrás e recupere o direto quando quiser. A reprodução nunca precisa de parar: recuar e avançar acontecem instantaneamente no mesmo fluxo de áudio.

Esta funcionalidade está **desativada por defeito**. Ative-a em Menu NVDA → Preferências → Definições → freeAudio → **Ativar buffer de time-shift (recuar na rádio em direto)**, ou ative-a instantaneamente a qualquer momento com `Ctrl+Win+T`.

> **Nota:** o freeAudio mantém sempre uma pequena captura em segundo plano da estação que está a tocar — não apenas quando esta definição está ativa — porque o [Reconhecimento Musical](#reconhecimento-musical) depende dela para evitar anúncios, como descrito nessa secção. Quando esta definição está **desativada**, a captura em segundo plano limita-se a cerca dos últimos 45 segundos e `Ctrl+Win+J`/`Ctrl+Win+K` continuam indisponíveis — o que muda é apenas o tamanho do buffer, não se está a funcionar. Ativar a definição alarga essa mesma captura até ao buffer de retrocesso completo descrito abaixo.

### Como funciona

Quando ativado, o freeAudio captura continuamente a estação que está a tocar para um buffer local circular em segundo plano, independentemente da reprodução normal. O buffer guarda o áudio mais recente até ao comprimento definido em **Duração do buffer de time-shift**; o áudio mais antigo é descartado automaticamente do início à medida que chega áudio novo, pelo que o buffer representa sempre o «passado recente» em relação ao limite da emissão em direto.

- **`Ctrl+Win+J`** — Recuar 15 segundos. A primeira pressão passa da reprodução em direto para a reprodução com time-shift, começando 15 segundos atrás da margem do direto. Cada pressão adicional recua mais 15 segundos, até ao limite do buffer.
- **`Ctrl+Win+K`** — Avançar 15 segundos em modo time-shift. Ao atingir a margem do direto, a reprodução regressa automaticamente ao stream em direto e o NVDA anuncia «Voltar ao direto».
- **`Ctrl+Win+Alt+J`** / **`Ctrl+Win+Alt+K`** — O mesmo retrocesso e avanço, mas em passos de 1 segundo em vez de 15, para ajustes finos. Veja [Busca Precisa (1 Segundo)](#busca-precisa-1-segundo).
- **`Ctrl+Win+T`** — Liga ou desliga toda a funcionalidade. Desligá-la em modo time-shift regressa imediatamente ao direto e interrompe a captura em segundo plano da estação atual.

A captura em segundo plano continua a funcionar todo o tempo que está em time-shift, pelo que a margem do direto continua a avançar mesmo enquanto ouve algo de alguns minutos atrás — exatamente como um DVR real.

### Ativação e aquecimento do buffer

O buffer começa a preencher-se assim que uma estação começa a reproduzir (após ativar a funcionalidade) ou no momento em que ativa a funcionalidade enquanto já ouve uma estação. Por isso, recuar só é possível depois de alguns segundos de áudio terem sido realmente capturados — se premir `Ctrl+Win+J` imediatamente após mudar de estação, o NVDA avisará que ainda não há áudio suficiente no buffer. Aguarde alguns segundos e tente novamente.

Mudar para uma estação diferente reinicia sempre o buffer para a nova estação; o áudio da estação anterior é descartado.

### Streams suportados

O time-shift funciona com a mesma gama de streams que o freeAudio já suporta:

- Streams HTTP/HTTPS simples (MP3, AAC, OGG, etc.), incluindo servidores de tipo Shoutcast/Icecast.
- **Streams HLS (`.m3u8`)** — O freeAudio resolve a playlist principal da estação, segue a playlist de multimédia e transfere segmentos em segundo plano para manter o buffer preenchido.

No caso raro de a playlist de uma estação não poder ser lida de todo (por exemplo, um manifesto `.m3u8` danificado ou inacessível), o NVDA indicará que recuar não está disponível para essa estação em particular.

### Requisitos e limitações

- **Requer o backend BASS**, que o freeAudio usa sempre para reprodução (ver [Reprodução](#reprodução)).
- O comprimento do buffer é determinado pela definição **Duração do buffer de time-shift** — veja [Definições](#definições).
- O buffer é por estação: mudar de estação, parar a reprodução ou reiniciar o NVDA limpa-o e começa de novo.
- A reprodução com time-shift usa o seu próprio ficheiro de buffer local e não produz uma gravação guardada — se quiser conservar o áudio permanentemente, use também a Gravação instantânea (`Ctrl+Win+E`).

## Temporizador

Abra o separador Temporizador no navegador de estações (`Alt+4`). É possível adicionar dois tipos de temporizador:

Ao escolher uma estação para um temporizador de alarme, um campo **Filtro** acima da lista de estações permite-lhe restringir a lista de favoritos em tempo real.

**Alarme — iniciar rádio:** Inicia automaticamente a reprodução de uma estação selecionada dos seus favoritos à hora especificada. Escolha uma estação e introduza a hora no formato HH:MM.

**Suspensão — parar rádio:** Para a reprodução à hora especificada. Quando o temporizador dispara, o volume é reduzido gradualmente durante 60 segundos antes de parar a reprodução. Não é necessário selecionar uma estação; basta introduzir a hora.

Para ambos os tipos, se a hora introduzida já tiver passado, a ação é agendada para o dia seguinte. Se já existir um temporizador à mesma hora (independentemente do tipo), a adição de um novo é bloqueada; o utilizador é informado do conflito e solicitado a remover primeiro a entrada existente. Os temporizadores pendentes estão listados no separador; selecione um e prima o botão Remover Temporizador Selecionado para o cancelar.

**Temporizadores recorrentes:** Em **Recorrência**, escolha **Repetir semanalmente** em vez da opção única predefinida para que o temporizador dispare todas as semanas em vez de uma só vez. Uma lista de verificação **Dias ativos** permite-lhe então escolher em que dias da semana se repete; deixar todos os dias desmarcados repete-o todos os dias. Um temporizador recorrente continua a disparar conforme agendado até o remover da lista de temporizadores pendentes — não é uma entrada única que desaparece após disparar.

## Podcasts

O freeAudio inclui um leitor de podcasts completo. Pode subscrever qualquer feed de podcast RSS ou Atom, navegar por episódios, reproduzi-los, descarregá-los e retomar a reprodução onde ficou — tudo totalmente acessível.

### Aceder ao Separador Podcasts

Abra o navegador de estações com `Ctrl+Win+R` e mude para o separador **Podcasts** com `Ctrl+Tab` ou `Alt+6`. O separador está organizado em três áreas principais:

1. **Pesquisar e adicionar** — secção superior para descobrir novos podcasts, incluindo uma lista de pré-visualização que mostra os episódios do resultado de pesquisa atualmente selecionado.
2. **Subscrições** — lista dos seus feeds subscritos.
3. **Episódios** — lista de episódios do feed selecionado, com controlos de reprodução. Uma lista **Marcadores** mesmo por baixo mostra os marcadores do episódio selecionado — veja [Marcadores](#marcadores).

### Adicionar um Feed de Podcast

Pode adicionar um feed de podcast de duas formas:

**Por URL:**

- No campo **Pesquisar**, cole o URL completo do feed RSS ou Atom (por exemplo, `https://example.com/feed.xml`).
- Prima Enter.
- O freeAudio obtém o feed, valida-o e adiciona-o às suas subscrições. Se o feed for válido, ouvirá uma confirmação com o título do feed. Se falhar, uma mensagem de erro explica o motivo.

**Por pesquisa:**

- No campo **Pesquisar**, escreva uma palavra-chave (título do podcast, tema ou nome do apresentador) e prima Enter.
- O freeAudio pesquisa no diretório de podcasts da iTunes e apresenta os podcasts correspondentes na lista **Resultados da pesquisa**.
- Selecionar um resultado obtém esse feed em segundo plano e lista os seus episódios na lista **Episódios do resultado selecionado** logo abaixo, para que possa pré-visualizar o que o programa realmente contém antes de decidir subscrever.
- Assim que estiver satisfeito com o que vê, selecione o resultado e prima `Enter`, ou abra o seu menu de contexto (tecla Aplicações / `Shift+F10`, ou clique com o botão direito) e escolha **Subscrever**, para o adicionar às suas subscrições. O feed é adicionado imediatamente e aparece na sua lista de subscrições. Não existe um botão separado "Adicionar Selecionado da Pesquisa" — `Enter` ou o menu de contexto é a única forma de subscrever a partir dos resultados de pesquisa.

> **Dica:** Também pode escrever um URL de feed diretamente no campo de pesquisa — se parecer um URL válido, o complemento tentará adicioná-lo como feed sem pesquisar.

**Menu de contexto para resultados de pesquisa:** Clique com o botão direito num resultado de pesquisa, ou selecione-o e prima a tecla Aplicações / `Shift+F10`, para abrir um menu com uma única ação **Subscrever**, idêntica a premir `Enter` no resultado.

### Pré-visualizar Episódios Antes de Subscrever

Antes de se comprometer com uma subscrição, pode ouvir os episódios de um podcast diretamente a partir dos resultados de pesquisa. Sempre que seleciona um podcast na lista **Resultados da pesquisa**, o freeAudio obtém esse feed e mostra os seus episódios — título e data de publicação — na lista **Episódios do resultado selecionado** por baixo.

- Selecione um episódio nessa lista de pré-visualização e prima `Enter`, ou abra o seu menu de contexto (tecla Aplicações / `Shift+F10`, ou clique com o botão direito) e escolha **Pré-visualizar**, para começar a reproduzi-lo através do leitor normal. Todos os controlos de reprodução habituais (pausa, volume, time-shift, etc.) funcionam nele exatamente como funcionariam em qualquer outra estação ou episódio.
- Enquanto um episódio está a ser pré-visualizado, o mesmo menu de contexto mostra **Parar Pré-visualização** no lugar de **Pré-visualizar** — escolha-o, ou prima `Enter` novamente nesse episódio, para parar.
- Pré-visualizar não o subscreve a nada; é puramente para ouvir antes de decidir. A própria lista de pré-visualização é temporária — é substituída assim que seleciona um resultado de pesquisa diferente, e não persiste em lado nenhum da forma como as suas subscrições reais persistem.

### Gerir Subscrições

Depois de adicionar alguns feeds, estes aparecem na lista **Subscrições**. Cada entrada mostra o título do feed e o número de episódios disponíveis.

- **Selecione um feed** para ver os seus episódios na lista inferior. A caixa de texto só de leitura **Detalhes do feed** por baixo da lista de subscrições mostra o título do feed, autor, descrição, número de episódios e URL.
- **Atualizar um feed** — selecione-o e prima o botão **Atualizar Feed** (disponível através do menu de contexto, veja abaixo) para obter os episódios mais recentes. Todos os feeds também são atualizados automaticamente em segundo plano quando abre o separador Podcasts, pelo que normalmente vê os episódios mais recentes sem intervenção manual.
- **Remover um feed** — selecione-o e prima `Delete` ou use o menu de contexto para o remover das suas subscrições. Ser-lhe-á pedida confirmação antes da remoção.

**Menu de contexto para feeds:** Clique com o botão direito num feed, ou selecione-o e prima a tecla Aplicações / `Shift+F10`, para abrir um menu com:

- **Atualizar Feed** — obtém novos episódios agora.
- **Guardar Perfil de Áudio para Este Podcast** / **Limpar Perfil de Áudio** — veja [Perfil de Áudio do Podcast](#perfil-de-áudio-do-podcast).
- **Remover Feed** — elimina a subscrição.
- **Copiar URL do Feed** — copia o URL do feed para a área de transferência.

### Navegar e Reproduzir Episódios

Selecione um feed na lista de subscrições; os seus episódios aparecem na lista **Episódios** abaixo. Cada episódio mostra:

- O seu número de episódio (1 = o episódio mais antigo no feed, contando até ao mais recente).
- A sua data de publicação (se disponível).
- O seu título.
- Um prefixo **"Ouvido"** se o episódio tiver sido reproduzido na totalidade.
- Um sufixo de duração, seja a duração total (se nunca reproduzido) ou o progresso decorrido/total (se reproduzido parcialmente).

**Reprodução:**

- Selecione um episódio e prima `Enter` ou `Espaço` para começar a reproduzi-lo. Se um episódio foi reproduzido parcialmente antes, retoma de onde ficou.
- A linha *não* é atualizada durante a reprodução do episódio — isto é intencional, para que o NVDA não reanuncie repetidamente a linha enquanto está nela. A sua marca "Ouvido" e duração são atualizadas imediatamente no momento em que pausa o episódio ou este termina de reproduzir, pelo que a apresentação é sempre exata precisamente quando importa; simplesmente não avança segundo a segundo durante a reprodução.
- Use `F3` / `F4` no separador Podcasts para se mover para o episódio anterior / seguinte e reproduzi-lo imediatamente. Também pode usar `←` / `→` enquanto a lista de episódios está em foco, ou `Ctrl+←` / `Ctrl+→` em qualquer parte do separador Podcasts — ambos funcionam de forma idêntica.
- Use `Shift+F3` / `Shift+F4` para se mover entre feeds sem reproduzir episódios.
- Prima `Espaço` enquanto um episódio está a tocar para pausar ou retomar a reprodução.

**Retomar a reprodução:** O freeAudio guarda a sua posição em cada episódio de podcast automaticamente — imediatamente sempre que pausa ou o episódio termina, e a cada 15 segundos em segundo plano enquanto continua a ouvir, para que uma falha ou reinício inesperado não perca muito progresso. Se parar ou pausar a reprodução e voltar mais tarde, o episódio retoma a partir da posição guardada. Se reproduzir o episódio até ao fim (dentro dos últimos 3 segundos), é marcado como "Ouvido" e não retomará — começa do início da próxima vez, e o prefixo "Ouvido" aparece na lista.

**Menu de contexto para episódios:** Clique com o botão direito num episódio, ou selecione-o e prima a tecla Aplicações / `Shift+F10`, para abrir um menu com:

- **Reproduzir Episódio** — inicia a reprodução.
- **Descarregar Episódio** — descarrega o ficheiro do episódio para a sua pasta de gravações.
- **Guardar Perfil de Áudio para Este Podcast** / **Limpar Perfil de Áudio** — os mesmos comandos do menu de contexto do próprio feed, incluídos aqui por conveniência para não ter de voltar à lista de Subscrições. Continuam a guardar um perfil para todo o podcast, não um separado para este episódio — veja [Perfil de Áudio do Podcast](#perfil-de-áudio-do-podcast).
- **Copiar URL do Episódio** — copia o URL de áudio direto para a área de transferência.

### Descarregar Episódios

Selecione um episódio e clique no botão **Descarregar Episódio** (ou use o menu de contexto). O episódio é descarregado para a sua pasta de gravações (`Documents\freeAudio Recordings\` por predefinição). O nome do ficheiro baseia-se no título do episódio e na extensão de ficheiro detetada (`.mp3`, `.m4a`, `.ogg`, etc.). O NVDA anuncia quando o descarregamento começa e termina. Se o ficheiro já existir, é informado e o descarregamento é ignorado.

### Filtrar Episódios

Acima da lista de episódios está um campo **Filtro**. À medida que escreve, a lista de episódios é filtrada em tempo real para mostrar episódios cujo título contém o texto escrito, ou cujo número de episódio corresponde exatamente — pelo que escrever `47` salta diretamente para o episódio 47 mesmo que "47" não apareça em lado nenhum do seu título. O NVDA anuncia o número de episódios correspondentes após cada alteração. Prima a seta `Para Baixo` a partir do campo de filtro para mover o foco diretamente para a lista filtrada.

### Detalhes de Reprodução de Podcasts

Os episódios de podcast são reproduzidos usando o **backend BASS** (o mesmo motor usado para fluxos de rádio e, a partir desta versão, o único backend de reprodução que o freeAudio usa). Como os episódios são descarregados progressivamente e são pesquisáveis, pode usar os atalhos de recuo/avanço de time-shift (`Ctrl+Win+J`/`Ctrl+Win+K`) enquanto reproduz um podcast para navegar dentro do episódio. A posição é guardada automaticamente para que possa retomar mais tarde.

**Navegação escalonada:** Ao contrário do recuo fixo de 15 segundos da rádio em direto, a navegação dentro de um podcast, audiolivro ou faixa de jukebox escala consoante a forma como prime a tecla, para que possa fazer uma pequena correção ou saltar uma longa distância sem premir repetidamente:

- **Manter a tecla premida** (repetição automática) avança ou recua **5 segundos** por repetição — a mesma pequena quantidade que este atalho sempre usou para ficheiros.
- **Um toque deliberado** navega **12 segundos**.
- **Dois toques** em sucessão rápida navegam **1 minuto**.
- **Três ou mais toques** navegam **5 minutos**; toques adicionais na mesma sequência não aumentam mais.

Um toque deliberado é retido por um breve momento antes de realmente navegar, para o caso de vir mais um toque — só ocorre uma navegação por sequência de toques, dimensionada consoante quantos toques foram finalmente feitos, não a soma da quantidade de cada toque. Após uma navegação, o NVDA anuncia a posição decorrida/restante resultante no episódio em vez de apenas "X segundos à frente/atrás".

### Busca Precisa (1 Segundo)

Para pequenas correções — como repetir uma palavra que acabou de lhe escapar — o freeAudio tem um par de comandos separado que se move sempre exatamente **1 segundo**, independentemente da forma como os prime:

- **`Ctrl+Win+Alt+J`** — 1 segundo para trás, a partir de qualquer ponto do Windows.
- **`Ctrl+Win+Alt+K`** — 1 segundo para a frente, a partir de qualquer ponto do Windows.
- **`Alt+←`** / **`Alt+→`** — os mesmos dois comandos dentro do Navegador de Estações, em qualquer separador.

Num episódio de podcast, parte de audiolivro ou faixa do jukebox funcionam exatamente como os comandos de busca normais, apenas com um passo de 1 segundo: o NVDA anuncia a posição resultante (decorrido/restante) e, num audiolivro ou pasta do jukebox, os limites das partes e das faixas comportam-se como descrito para `Ctrl+Win+J` / `Ctrl+Win+K` (um avanço para lá do fim passa à parte ou faixa seguinte; um retrocesso para lá do início pára primeiro em 0:00 e só um segundo retrocesso nos 10 segundos seguintes volta à parte ou faixa anterior).

Numa estação de rádio em direto movem-se 1 segundo no buffer de time-shift. Tal como com `Ctrl+Win+J`, o buffer tem de estar ativo nas definições e o primeiro retrocesso passa da reprodução em direto para a reprodução em time-shift. Um avanço que termine a cerca de 2 segundos do limite do direto regressa ao direto e anuncia «Voltar ao direto».

**Velocidade de reprodução:** Pode ajustar a velocidade de reprodução de episódios de podcast, audiolivros e faixas de jukebox usando `Ctrl+Win+Shift+K` (mais rápido) e `Ctrl+Win+Shift+J` (mais lento). A velocidade muda em incrementos de 0,1×, variando entre 0,5× e 2,0×, com o tom preservado.

**Transposição (alteração de tom):** Independentemente da velocidade de reprodução, pode deslocar o tom de um episódio de podcast, audiolivro ou faixa de jukebox para cima ou para baixo com `Shift+Win+K` / `Shift+Win+J` — veja [Transposição (Alteração de Tom)](#transposição-alteração-de-tom).

**Efeito sonoro ao retomar:** Sempre que um episódio retoma de uma posição guardada, o freeAudio reproduz brevemente um suave efeito sonoro de carregamento de cassete num canal separado enquanto navega de volta ao seu ponto guardado, em vez de deixar o áudio do próprio episódio tocar audivelmente a partir de 0:00 entretanto. Isto é independente da definição **Transição ao mudar de estação** — essa definição afeta apenas a mudança entre estações de rádio em direto, não a retoma de podcasts ou audiolivros.

### Perfil de Áudio do Podcast

Clique com o botão direito num podcast na lista Subscrições, ou clique com o botão direito em qualquer um dos seus episódios, e escolha **Guardar Perfil de Áudio para Este Podcast** para guardar o volume, efeitos, ganhos de equalizador e/ou velocidade de reprodução atuais como um perfil associado a esse podcast. Sempre que qualquer episódio desse podcast toca, as definições guardadas são aplicadas automaticamente, substituindo as predefinições globais. Como o comando está disponível tanto no menu de contexto do feed como no do episódio, pode aceder-lhe sem ter de voltar à lista de Subscrições — de qualquer forma, guarda sempre um perfil para todo o podcast, não um separado por episódio.

Uma caixa de diálogo com 15 opções permite-lhe escolher exatamente o que guardar:

- **Apenas volume**
- **Apenas efeitos**
- **Volume e efeitos**
- **Volume e velocidade de reprodução**
- **Efeitos e velocidade de reprodução**
- **Apenas velocidade de reprodução**
- **Volume, efeitos e velocidade de reprodução**
- **Apenas transposição de tom**
- **Volume e transposição de tom**
- **Efeitos e transposição de tom**
- **Velocidade de reprodução e transposição de tom**
- **Volume, efeitos e transposição de tom**
- **Volume, velocidade de reprodução e transposição de tom**
- **Efeitos, velocidade de reprodução e transposição de tom**
- **Volume, efeitos, velocidade de reprodução e transposição de tom**

Apenas as partes que escolher são escritas no perfil; o que for deixado de fora mantém o que já estava guardado. Por exemplo, escolher **Apenas velocidade de reprodução** num podcast que já tem um perfil de volume/efeitos guardado atualiza apenas a velocidade e deixa o resto intacto.

**Limpar Perfil de Áudio** remove o perfil guardado do podcast, a partir de qualquer um dos menus de contexto. Só está ativo quando o podcast tem atualmente um perfil guardado.

### Armazenamento de Dados de Podcasts

As suas subscrições são armazenadas em `freeAudio_podcasts.json` na pasta de configuração de utilizador do NVDA. As posições dos episódios são armazenadas separadamente em `podcast_positions.json` no mesmo local. Ambos os ficheiros são JSON simples e podem ser copiados para backup ou transferidos para outro computador.

## Audiolivros (GETEM, LibriVox e Project Gutenberg)

O freeAudio inclui um leitor de audiolivros que pesquisa, reproduz e descarrega livros de três fontes:

- **[GETEM](https://getem.boun.edu.tr/)** — a biblioteca digital gerida pelo Centro para Pessoas com Deficiência Visual da Universidade de Boğaziçi. Requer uma adesão gratuita para transmitir ou descarregar o áudio de um livro (a navegação não requer) — veja [Iniciar Sessão](#iniciar-sessão) abaixo.
- **[LibriVox](https://librivox.org/)** — o projeto de audiolivros de domínio público lidos por voluntários. Não é necessária conta ou início de sessão de qualquer tipo; todo o seu catálogo, incluindo os próprios ficheiros de áudio, é de domínio público e livremente acessível.
- **Coleção de Audiolivros Abertos do Project Gutenberg** — audiolivros de domínio público narrados por humanos e por computador, alojados em [archive.org](https://archive.org/), complemento da biblioteca de texto do Project Gutenberg. Tal como o LibriVox, não requer conta ou início de sessão.

Os resultados das três fontes aparecem juntos numa única lista fundida de **Resultados da pesquisa** e numa única lista fundida de **Biblioteca** — não existe um separador ou menu suspenso separado para alternar entre eles. A fonte de cada livro (GETEM, LibriVox ou Project Gutenberg) é apresentada como uma etiqueta junto ao seu título, e nos seus detalhes, para que possa sempre saber qual está a ver. Pode pesquisar, pré-visualizar, adicionar, reproduzir e descarregar livros de qualquer uma das fontes exatamente da mesma forma; reproduzir obras de várias partes com retoma automática entre partes; e descarregar livros para ouvir offline — tudo totalmente acessível.

Qualquer uma das fontes pode ser desativada individualmente em **NVDA Menu → Preferências → Definições → freeAudio** com a lista de verificação **Fontes de audiolivros**, se quiser pesquisar apenas algumas delas. As três estão ativadas por predefinição.

> **Nota:** Ouvir um livro do GETEM requer uma adesão gratuita ao GETEM. Navegar no catálogo do GETEM não requer conta, mas resolver e reproduzir o áudio de um livro do GETEM requer — veja [Iniciar Sessão](#iniciar-sessão) abaixo. Os livros do LibriVox e do Project Gutenberg nunca requerem conta.

### Aceder ao Separador Audiolivros

Abra o navegador de estações com `Ctrl+Win+R` e mude para o separador **Audiolivros** com `Ctrl+Tab` ou `Alt+7`. O separador tem três áreas principais:

1. **Pesquisar** — um campo de texto para pesquisar todos os catálogos ativados de uma vez, com uma lista de resultados que aparece assim que uma pesquisa é executada.
2. **Biblioteca** — a lista de livros que adicionou de qualquer uma das fontes, onde os reproduz, descarrega e gere. Uma lista **Marcadores** mesmo por baixo mostra os marcadores do livro selecionado — veja [Marcadores](#marcadores).
3. **Detalhes** — uma caixa só de leitura que mostra a fonte, título, autor, narrador, editora, formato, número de partes, descrição e URL do catálogo do livro selecionado, em qualquer uma das listas.

### Iniciar Sessão

O GETEM requer ser um membro registado para transmitir ou descarregar o áudio real de um livro, embora o próprio catálogo possa ser pesquisado livremente. Introduza o seu nome de utilizador e palavra-passe do GETEM uma vez em **NVDA Menu → Preferências → Definições → freeAudio**; são armazenados encriptados no disco (através da API Windows Data Protection, associada à sua conta de utilizador do Windows) e reutilizados automaticamente depois. Se tentar reproduzir ou descarregar um livro do GETEM antes de introduzir as credenciais, o freeAudio diz-lhe para as adicionar primeiro nas Definições.

O LibriVox e o Project Gutenberg não precisam de nenhum passo de início de sessão — os seus resultados e áudio podem ser pesquisados, pré-visualizados, reproduzidos e descarregados imediatamente, sem credenciais a introduzir.

### Pesquisar Audiolivros

Escreva um termo de pesquisa no campo de pesquisa e prima `Enter`. O freeAudio pesquisa nas fontes ativadas nas Definições e funde os resultados numa única lista:

- O **GETEM** é pesquisado por título, autor, narrador, assunto e editora ao mesmo tempo, uma vez que o próprio formulário de pesquisa do GETEM só suporta restringir por todos eles em conjunto, em vez de uma única pesquisa através de qualquer um deles. Só são mostradas obras realmente disponíveis em formato áudio (narração humana ou computorizada, audiodescrição, drama radiofónico, livros falados DAISY, etc.); braille, letra grande e outros formatos não sonoros são filtrados automaticamente.
- O **LibriVox** é pesquisado por título ou autor/leitor no seu catálogo de domínio público.
- O **Project Gutenberg** é pesquisado por título ou autor na Coleção de Audiolivros Abertos em archive.org.

Colar o URL da página de catálogo/detalhes de um livro diretamente no campo de pesquisa (uma página de catálogo GETEM, ou uma página "details" do archive.org para um título LibriVox ou Project Gutenberg) resolve esse único livro diretamente em vez de executar uma pesquisa por palavras-chave.

O NVDA anuncia quantos audiolivros foram encontrados no total.

Selecionar um resultado mostra os seus detalhes — autor, narrador, editora, formato e número de partes — na caixa de detalhes abaixo.

**Pré-visualização:** Selecione um resultado e prima `Espaço`, ou abra o seu menu de contexto (tecla Aplicações / `Shift+F10`, ou clique com o botão direito) e escolha **Pré-visualizar**, para começar a reproduzi-lo a partir da primeira parte sem o adicionar à sua biblioteca. Enquanto um livro está a ser pré-visualizado, o mesmo menu de contexto mostra **Parar Pré-visualização** no seu lugar — escolha-o, ou prima `Espaço` novamente, para parar. Pré-visualizar um livro não guarda a sua posição de escuta, uma vez que isso só é seguido para livros já na sua biblioteca.

**Adicionar à sua biblioteca:** Selecione um resultado e prima `Enter`, ou use o seu menu de contexto e escolha **Adicionar à Biblioteca**, para o adicionar. O freeAudio diz-lhe se o livro já lá está.

### A Sua Biblioteca

Os livros que adicionou aparecem na lista **Biblioteca**, mostrando título, autor e formato. Selecionar um mostra os seus detalhes abaixo.

- Prima `Enter` ou `Espaço` para reproduzir o livro selecionado. Se nada estiver carregado, `Espaço` inicia-o; se algo já estiver a tocar, `Espaço` pausa-o, correspondendo ao resto do leitor.
- Use `F3` / `F4` no separador Audiolivros para se mover para o **livro** anterior / seguinte na sua biblioteca e começar a reproduzi-lo. `Ctrl+←` / `Ctrl+→` fazem o mesmo enquanto a lista da biblioteca está em foco.
- Use `Shift+F3` / `Shift+F4` para se mover entre **partes** do livro atualmente a tocar — o inverso do separador Podcasts, onde F3/F4 se movem entre episódios e Shift+F3/F4 entre feeds. Isto porque um livro é uma única entrada da biblioteca mesmo quando tem várias partes, pelo que a navegação mais detalhada "por parte" fica aqui nas teclas modificadas com Shift.
- Com o Navegador de Estações fechado, `Ctrl+Win+F3` / `Ctrl+Win+F4` (livro anterior / seguinte) e `Ctrl+Win+Shift+F3` / `Ctrl+Win+Shift+F4` (parte anterior / seguinte) fazem o mesmo — consulte [Saltar Itens com o Navegador de Estações Fechado](#saltar-itens-com-o-navegador-de-estações-fechado).

**Menu de contexto para entradas da biblioteca:** Clique com o botão direito num livro, ou selecione-o e prima a tecla Aplicações / `Shift+F10`, para abrir um menu com:

- **Reproduzir Média** — inicia a reprodução, o mesmo que `Enter`.
- **Descarregar Livro** — descarrega todas as partes do livro; veja [Descarregar Audiolivros](#descarregar-audiolivros) abaixo.
- **Copiar o URL** — copia o URL da página do catálogo do livro para a área de transferência (a página do catálogo GETEM para um livro do GETEM, ou a página de detalhes do archive.org para um livro do LibriVox ou Project Gutenberg).
- **Guardar Perfil de Áudio para Este Livro** / **Limpar Perfil de Áudio** — veja [Perfil de Áudio do Audiolivro](#perfil-de-áudio-do-audiolivro) abaixo.
- **Remover da Biblioteca** — elimina o livro da sua biblioteca.

Também pode marcar vários livros de uma só vez e removê-los todos juntos — veja [Marcar e Remover Vários Itens](#marcar-e-remover-vários-itens) em Favoritos.

### Reprodução e Retoma

Uma obra de várias partes é tratada como um único item no leitor, não uma linha por parte — da mesma forma que um episódio de podcast é um único item independentemente de como é entregue. O freeAudio lembra-se de qual parte ouviu por último e retoma aí automaticamente da próxima vez que reproduzir esse livro, mesmo após um reinício do NVDA.

Quando uma parte termina, o freeAudio inicia automaticamente a parte seguinte do mesmo livro — não precisa de a selecionar manualmente. Isto acontece mesmo que a janela do Navegador de Estações esteja fechada nessa altura; a parte "a tocar agora" mostrada na lista Biblioteca é ressincronizada automaticamente da próxima vez que a janela é aberta.

A reprodução é transmitida através de um pequeno relé local em vez de descarregar toda a parte primeiro, pelo que a escuta começa assim que os primeiros bytes chegam — o mesmo comportamento de início imediato que os podcasts usam. Todos os controlos usuais do leitor (pausa, volume, time-shift, velocidade de reprodução, transposição, dispositivo de saída, etc.) funcionam num audiolivro exatamente como funcionariam numa estação ou episódio de podcast.

Tal como os podcasts, retomar um livro da sua posição guardada reproduz um breve efeito sonoro de carregamento de cassete enquanto o freeAudio navega até ao seu ponto guardado — veja a nota **Efeito sonoro ao retomar** em [Detalhes de Reprodução de Podcasts](#detalhes-de-reprodução-de-podcasts).

### Perfil de Áudio do Audiolivro

Clique com o botão direito num livro na sua lista Biblioteca e escolha **Guardar Perfil de Áudio para Este Livro** para guardar o volume, efeitos, ganhos de equalizador e/ou velocidade de reprodução atuais como um perfil associado a esse livro. Sempre que o livro (ou qualquer uma das suas partes) toca, as definições guardadas são aplicadas automaticamente, substituindo as predefinições globais. Isto funciona exatamente da mesma forma que o [Perfil de Áudio do Podcast](#perfil-de-áudio-do-podcast) acima, incluindo o mesmo conjunto de opções de guardar (volume, efeitos e/ou velocidade de reprodução, em qualquer combinação) e o mesmo comportamento de atualização parcial.

**Limpar Perfil de Áudio** remove o perfil guardado do livro; só está ativo quando o livro tem atualmente um perfil guardado.

### Descarregar Audiolivros

Selecione um livro na sua biblioteca e escolha **Descarregar Livro** no seu menu de contexto para guardar cada parte na sua própria pasta (com o nome do livro) dentro da sua pasta de gravações (`Documents\freeAudio Recordings\` por predefinição). Os ficheiros são numerados para que as partes fiquem sempre ordenadas pela ordem de escuta, independentemente de como o próprio GETEM as designa. O NVDA anuncia quantas partes foram guardadas assim que o descarregamento termina; se uma parte falhar, o último erro é reportado juntamente com a contagem.

### Atalhos de Teclado Diretos para Audiolivros

Cada livro da sua biblioteca de Audiolivros — quer venha do GETEM, do LibriVox ou do Project Gutenberg — é registado como um script separado na caixa de diálogo Definir Comandos do NVDA, na categoria **freeAudio Audio Books**, exatamente como em [Atalhos de Teclado Diretos para Estações Favoritas](#atalhos-de-teclado-diretos-para-estações-favoritas) e [Atalhos de Teclado Diretos para Entradas do Jukebox](#atalhos-de-teclado-diretos-para-entradas-do-jukebox). Pode atribuir qualquer atalho de teclado a qualquer livro e premi-lo a partir de qualquer lugar — sem necessidade de abrir primeiro a janela do navegador. Por predefinição, não há atalhos atribuídos.

Para atribuir um atalho:

1. Abra Menu NVDA → Preferências → Definir comandos.
2. Expanda a categoria **freeAudio Audio Books**.
3. Encontre o livro pelo título (cada entrada chama-se «*título* playback shortcut»), selecione-o e prima **Adicionar**.
4. Prima a combinação de teclas pretendida e confirme.

O atalho inicia o livro imediatamente, retomando na parte que ouviu por último; a posição dentro dessa parte é restaurada da mesma forma que ao reproduzir o livro a partir da lista da biblioteca. Se a lista de partes do livro ainda não tiver sido obtida, o NVDA diz «A carregar: *título*» e a reprodução começa assim que estiver pronta (um livro do GETEM precisa do seu início de sessão guardado — consulte [Iniciar Sessão](#iniciar-sessão)). Quando uma parte termina, a seguinte arranca automaticamente, com o Navegador de Estações aberto ou fechado.

Quando adiciona um livro à biblioteca ou remove um, a categoria **freeAudio Audio Books** é atualizada de imediato — não é necessário reabrir a caixa de diálogo Definir Comandos. Se um livro for removido, a sua entrada desaparece e qualquer atalho atribuído é automaticamente removido pelo NVDA; se um atalho obsoleto ainda assim disparar, o NVDA diz que o audiolivro já não está na biblioteca.

### Armazenamento de Dados de Audiolivros

Cada fonte mantém o seu próprio ficheiro de biblioteca, apesar de serem apresentadas fundidas no separador Audiolivros. A sua biblioteca GETEM (livros adicionados e o seu progresso de escuta) é armazenada em `freeAudio_getem_library.json`, a sua biblioteca LibriVox é armazenada separadamente em `freeAudio_librivox_library.json`, e a sua biblioteca Project Gutenberg é armazenada separadamente em `freeAudio_gutenberg_library.json` — as três na pasta de configuração de utilizador do NVDA. As suas credenciais GETEM encriptadas são armazenadas separadamente em `freeAudio_getem_credentials.bin` no mesmo local, e só podem ser desencriptadas pela mesma conta de utilizador do Windows que as guardou. O LibriVox e o Project Gutenberg não têm ficheiro de credenciais, uma vez que nenhum deles requer conta.

## Jukebox Local

O separador **Jukebox** do freeAudio dá-lhe duas formas de reproduzir ficheiros de áudio que já estão no seu computador: pesquisar em todas as unidades ligadas por nome de ficheiro, ou construir uma biblioteca pessoal persistente de ficheiros e pastas. Tudo o que reproduzir a partir daqui recebe o mesmo tratamento que um podcast ou audiolivro — retoma automática, recuo/avanço escalonado, velocidade de reprodução, transposição de tom e perfis de áudio por item funcionam exatamente da mesma forma.

### Aceder ao Separador Jukebox

Abra o navegador de estações com `Ctrl+Win+R` e mude para o separador **Jukebox** com `Ctrl+Tab` ou `Alt+8`, ou abra-o diretamente a partir de qualquer lugar com o atalho global `Ctrl+Win+U`. O separador está organizado em três áreas principais:

1. **Pesquisar no disco** — um campo de texto que pesquisa em todas as unidades locais ligadas e prontas por ficheiros de áudio cujo nome contenha o texto introduzido. Prima `Enter` para iniciar a pesquisa.
2. **Resultados da pesquisa** — uma lista que aparece assim que uma pesquisa é executada, mostrando os ficheiros correspondentes. Oculta até então, para que o separador permaneça arrumado quando não há nada a pesquisar.
3. **Jukebox e Faixas** — a lista persistente de itens que adicionou, seguida da lista de faixas na entrada selecionada (para uma entrada de ficheiro, apenas esse ficheiro; para uma entrada de pasta, todos os ficheiros de áudio encontrados dentro dela). Uma lista **Marcadores** vem a seguir à lista de Faixas e mostra os marcadores da faixa selecionada — veja [Marcadores](#marcadores).

Os botões **Adicionar Ficheiro…**, **Adicionar Pasta…**, **Remover**, **Exportar Jukebox…** e **Importar Jukebox…** encontram-se na parte inferior do separador.

### Pesquisar Ficheiros no Disco

Escreva qualquer parte de um nome de ficheiro no campo **Pesquisar no disco** e prima `Enter`. O freeAudio percorre todas as unidades locais ligadas — discos fixos, unidades USB, cartões de memória — à procura de ficheiros de áudio (`.mp3`, `.wav`, `.ogg`, `.flac`, `.m4a`, `.m4b`, `.aac`, `.wma`, `.opus`, e vários outros) cujo nome contenha o texto de pesquisa. A pesquisa é executada em segundo plano, para que o NVDA permaneça responsivo. As unidades de rede são ignoradas por predefinição, porque pesquisar uma partilha de rede pode transformar uma pesquisa de um segundo numa de vários minutos, ou bloqueá-la se a partilha estiver inacessível. Para as incluir, ative nas definições a opção **Incluir unidades de rede ao pesquisar no Jukebox**.

- **Espaço** num resultado de pesquisa pré-visualiza-o — inicia a reprodução através do leitor normal. Prima **Espaço** novamente no mesmo ficheiro para parar a pré-visualização.
- **Enter** num resultado de pesquisa adiciona-o ao seu jukebox.
- O menu de contexto (tecla Aplicações / `Shift+F10`, ou clique com o botão direito) oferece as mesmas duas ações: **Pré-visualizar** / **Parar Pré-visualização** e **Adicionar ao Jukebox**.
- Iniciar uma nova pesquisa cancela qualquer pesquisa ainda em execução, para que uma pesquisa lenta numa unidade grande nunca atrase uma nova.

### Construir o Seu Jukebox

A lista Jukebox é a sua biblioteca pessoal persistente. Podem ser adicionados dois tipos de item:

- **Adicionar Ficheiro…** — abre um seletor de ficheiros que lhe permite adicionar um ou mais ficheiros de áudio individuais. Todos os ficheiros escolhidos são adicionados de uma só vez.
- **Adicionar Pasta…** — abre um seletor de pastas que lhe permite selecionar várias pastas de uma só vez. Cada ficheiro de áudio encontrado dentro de cada pasta escolhida, incluindo nas suas subpastas, é tratado como uma das **faixas** dessa pasta. Cada pasta é adicionada como uma entrada própria na sua lista Jukebox; os ficheiros dentro dela são listados na lista Faixas quando a pasta é selecionada. O NVDA anuncia quantas pastas foram adicionadas assim que o seletor fecha.
- **Remover** — elimina a entrada atualmente selecionada do seu Jukebox. Remover uma entrada de pasta não elimina quaisquer ficheiros do disco; apenas esquece a pasta. Também pode marcar várias entradas de uma só vez e removê-las todas juntas — veja [Marcar e Remover Vários Itens](#marcar-e-remover-vários-itens) em Favoritos.

A sua lista Jukebox é guardada automaticamente, pelo que sobrevive a reinícios do NVDA. O conteúdo das pastas é analisado a pedido e armazenado em cache, pelo que adicionar uma pasta é instantâneo mesmo para coleções muito grandes — a análise completa ocorre na primeira vez que seleciona essa pasta. Se adicionar ficheiros a uma pasta fora do freeAudio, use o item **Reanalisar Pasta** no menu de contexto da pasta para os detetar.

### Adicionar Itens a partir do Windows Explorer

Mais dois comandos, disponíveis apenas enquanto um ficheiro ou pasta está em foco na lista de ficheiros do Windows Explorer (lista Detalhes/Ícones — não a barra de endereço, a árvore de pastas, o friso, ou a caixa de pesquisa), permitem-lhe ignorar completamente as caixas de diálogo Adicionar Ficheiro…/Adicionar Pasta… acima:

- **Reproduzir o ficheiro em foco com o freeAudio** — reproduz o ficheiro de áudio destacado diretamente, sem ser necessário já estar na sua lista Jukebox. Só funciona em ficheiros; usá-lo numa pasta diz-lhe para adicionar a pasta ao jukebox em vez disso.
- **Adicionar o item em foco ao jukebox do freeAudio** — adiciona o ficheiro ou pasta destacado à sua lista Jukebox, exatamente como se tivesse usado **Adicionar Ficheiro…** ou **Adicionar Pasta…** acima.

Nenhum dos comandos tem uma tecla predefinida atribuída. Atribua uma em Menu NVDA → Preferências → Definir comandos → freeAudio **enquanto estiver em foco dentro de uma janela do Explorador de Ficheiros**.

### Reproduzir a partir do Jukebox

- **Enter** numa entrada do Jukebox reproduz-la diretamente: para uma entrada de ficheiro, o próprio ficheiro; para uma entrada de pasta, a pasta por ordem — a partir da faixa realçada na lista de Faixas ou, se nenhuma estiver realçada, a partir de onde a pasta foi deixada da última vez (a primeira faixa, se nunca foi reproduzida). Quando uma faixa termina, a faixa seguinte da pasta arranca automaticamente.
- **Espaço** numa entrada do Jukebox pausa a reprodução se algo estiver a tocar; caso contrário reproduz a entrada em foco.
- **Enter** ou **Espaço** na lista de Faixas reproduz a faixa em foco. **Espaço** pausa primeiro se algo já estiver a tocar. Uma faixa iniciada desta forma toca sozinha e não passa para a seguinte quando termina; para reprodução contínua, use `F3` / `F4` ou reproduza a própria entrada da pasta.
- **F3 / F4** no separador Jukebox movem-se entre faixas dentro da entrada atualmente selecionada e reproduzem imediatamente. Numa entrada de pasta, a faixa é reproduzida como parte da pasta, pelo que as faixas seguintes continuam a arrancar automaticamente quando termina.
- **Shift+F3 / Shift+F4** movem-se entre entradas na lista Jukebox (ficheiros e pastas), espelhando como estas teclas se movem entre feeds no separador Podcasts.
- **Ctrl+← / Ctrl+→** enquanto a lista de entradas ou faixas está em foco fazem o mesmo que F3/F4 na lista de faixas — faixa anterior / seguinte, com continuação automática numa pasta.
- Com o Navegador de Estações fechado, `Ctrl+Win+F3` / `Ctrl+Win+F4` (faixa anterior / seguinte) e `Ctrl+Win+Shift+F3` / `Ctrl+Win+Shift+F4` (entrada anterior / seguinte) fazem o mesmo — consulte [Saltar Itens com o Navegador de Estações Fechado](#saltar-itens-com-o-navegador-de-estações-fechado).

### Detalhes de Reprodução do Jukebox

Cada faixa reproduzida a partir do Jukebox recebe o tratamento completo de média local:

- **Retoma:** O freeAudio lembra-se da sua posição em cada faixa, guarda-a ao pausar e periodicamente durante a reprodução, e retoma a partir desse ponto quando a reproduz novamente — mesmo após um reinício do NVDA.
- **Faixa seguinte automática:** quando uma faixa reproduzida como parte de uma pasta termina, a faixa seguinte dessa pasta arranca sozinha, com o Navegador de Estações aberto ou fechado, e continua a fazê-lo depois de saltar faixas com `F3` / `F4` ou `Ctrl+Win+F3` / `Ctrl+Win+F4`. Quando a última faixa termina, a posição guardada da pasta é limpa e, da próxima vez, recomeça na primeira faixa. Premir «seguinte» manualmente na última faixa não a limpa.
- **Navegação escalonada:** `Ctrl+Win+J` / `Ctrl+Win+K` navegam dentro da faixa usando a mesma escala de toque/manter premido que os podcasts e audiolivros — manter premido para 5 segundos por repetição, um toque para 12 segundos, dois toques para 1 minuto, três ou mais toques para 5 minutos. `Ctrl+Win+Alt+J` / `Ctrl+Win+Alt+K` procuram exatamente 1 segundo — veja [Busca Precisa (1 Segundo)](#busca-precisa-1-segundo).
- **Velocidade de reprodução:** `Ctrl+Win+Shift+J` / `Ctrl+Win+Shift+K` ajustam a velocidade em passos de 0,1× de 0,5× a 2,0×, com o tom preservado.
- **Transposição:** `Shift+Win+J` / `Shift+Win+K` alteram o tom sem mudar a velocidade — veja [Transposição (Alteração de Tom)](#transposição-alteração-de-tom).


> **Nota:** O buffer de time-shift (usado para recuar a rádio em direto) é deliberadamente **não** iniciado para faixas do Jukebox — já são ficheiros locais pesquisáveis, pelo que uma captura em segundo plano não tem propósito e apenas consumiria espaço em disco. O recuo e o avanço continuam a funcionar porque atuam diretamente no ficheiro em reprodução.

### Renomear Entradas do Jukebox

Escolha **Renomear…** no menu de contexto de uma entrada do Jukebox (tecla Aplicações / `Shift+F10`) para lhe dar um nome de apresentação personalizado. O nome personalizado substitui o nome do ficheiro ou da pasta na lista do Jukebox e é escrito na linha `#EXTINF` quando a entrada é exportada para M3U (consulte [Exportar e Importar a Biblioteca do Jukebox](#exportar-e-importar-a-biblioteca-do-jukebox) abaixo). Deixe o campo vazio para limpar o nome personalizado e voltar ao nome original do ficheiro ou da pasta.

### Organizar o Jukebox em Grupos

As entradas do Jukebox podem pertencer a um grupo, apresentado como um sufixo "— Grupo" após o nome da entrada na lista, exatamente como em [Organizar Favoritos em Grupos](#organizar-favoritos-em-grupos):

- Marque uma ou mais entradas com `.` (ver [Marcar e Remover Vários Itens](#marcar-e-remover-vários-itens) acima), depois escolha **Atribuir ao Grupo…** no menu de contexto e escreva um nome de grupo. Deixe o campo vazio para remover as entradas marcadas do seu grupo. Se nada estiver marcado, o comando aplica-se à entrada atualmente selecionada.
- O campo Filtro acima da lista do Jukebox também corresponde a nomes de grupos, da mesma forma que acontece nos Favoritos.

### Reordenar o Jukebox

Com uma entrada selecionada na lista do Jukebox, prima `vírgula` para entrar no modo de mover — ouvirá um sinal sonoro. Navegue até à posição pretendida com as teclas de seta e prima `vírgula` novamente. A entrada é colocada na posição escolhida e a nova ordem é guardada imediatamente. Premir `vírgula` novamente na mesma posição cancela a operação.

### Exportar e Importar a Biblioteca do Jukebox

O separador Jukebox inclui dois botões para fazer cópias de segurança e restaurar a sua biblioteca, na parte inferior do separador:

**Exportar Jukebox…** — guarda toda a sua lista do Jukebox num ficheiro. Uma caixa de diálogo permite-lhe escolher entre dois formatos:

- **JSON** (`.json`) — uma cópia de segurança completa que preserva o caminho, o nome personalizado, o grupo e o perfil de áudio guardado de cada entrada. Recomendado para restaurar a sua biblioteca mais tarde ou movê-la para outro computador.
- **Lista de reprodução M3U** (`.m3u`) — um formato mais leve compatível com a maioria dos leitores de multimédia, que lista o caminho de cada entrada com o respetivo nome personalizado (se existir) numa linha `#EXTINF` anterior. Os grupos e os perfis de áudio não são incluídos no M3U, pelo que restaurar a partir de M3U perde esse detalhe.

**Importar Jukebox…** — carrega entradas de um ficheiro JSON ou M3U previamente exportado. Após selecionar o ficheiro, é perguntado como adicionar as entradas:

- **Sim (Intercalar)** — adiciona as entradas importadas à sua biblioteca existente sem remover nenhuma entrada atual. As entradas cujo caminho coincide com uma já existente na sua biblioteca não são adicionadas duas vezes.
- **Não (Substituir)** — limpa completamente a sua lista atual do Jukebox e substitui-a pelo conteúdo do ficheiro importado.
- **Cancelar** — regressa ao navegador sem efetuar quaisquer alterações.

### Atalhos de Teclado Diretos para Entradas do Jukebox

Cada entrada da sua lista do Jukebox é registada como um script separado na caixa de diálogo Definir Comandos do NVDA, na categoria **freeAudio Jukebox**, exatamente como em [Atalhos de Teclado Diretos para Estações Favoritas](#atalhos-de-teclado-diretos-para-estações-favoritas). Pode atribuir qualquer atalho de teclado a qualquer entrada e premi-lo a partir de qualquer lugar — sem necessidade de abrir primeiro a janela do navegador.

Para atribuir um atalho:

1. Abra Menu NVDA → Preferências → Definir comandos.
2. Expanda a categoria **freeAudio Jukebox**.
3. Encontre a entrada pelo nome, selecione-a e prima **Adicionar**.
4. Prima a combinação de teclas pretendida e confirme.

O atalho reproduz a entrada imediatamente — no caso de uma entrada de ficheiro, o próprio ficheiro; no caso de uma entrada de pasta, a faixa onde a pasta foi deixada da última vez (a primeira faixa, se nunca foi reproduzida), após o que as faixas seguintes tocam automaticamente, mesmo com o Navegador de Estações fechado. Se a entrada for posteriormente removida do Jukebox, a sua entrada desaparece da categoria e qualquer atalho atribuído é automaticamente removido pelo NVDA. Quando uma nova entrada é adicionada, aparece na categoria de imediato — não é necessário reabrir a caixa de diálogo Definir Comandos.

## Marcadores

Os marcadores permitem assinalar um ponto numa **parte de audiolivro**, num **episódio de podcast** ou numa **faixa do jukebox** e voltar a ele mais tarde. Não estão disponíveis para estações de rádio em direto, que não têm posições fixas a que voltar.

### Adicionar um marcador

- Prima **`Ctrl+Win+F12`** em qualquer ponto do Windows, ou **`F12`** quando o Navegador de Estações está ativo, para adicionar um marcador na posição de reprodução atual.
- O NVDA anuncia o nome e a posição do marcador, por exemplo «Marcador adicionado: Marcador 2, 12:30».
- Se nada estiver a tocar, ou se estiver a tocar uma estação de rádio em direto, o freeAudio informa-o e nenhum marcador é adicionado.

O nome predefinido de um marcador é a sua **posição ordinal** entre os marcadores do item, do mais antigo para o mais recente: «Marcador 1», «Marcador 2» e assim por diante. Como o número acompanha a posição no item, adicionar um marcador mais cedo renumera os posteriores que ainda têm o nome predefinido. Os marcadores a que deu outro nome mantêm o seu nome.

### A lista de marcadores

Cada um dos separadores Podcasts, Audiolivros e Jukebox tem uma lista **Marcadores** mesmo junto ao item a que pertence:

- **Podcasts** — diretamente por baixo da lista de Episódios, com os marcadores do episódio selecionado.
- **Audiolivros** — diretamente por baixo da lista da Biblioteca, com os marcadores de todas as partes do livro selecionado. Quando um livro tem várias partes, cada linha começa com o título da parte.
- **Jukebox** — diretamente por baixo da lista de Faixas, com os marcadores da faixa selecionada.

Cada linha mostra o nome e a posição do marcador. É acrescentada a indicação **[texto]** ou **[nota de voz]** quando o marcador tem uma nota de texto ou de voz, e **(marcado)** quando o marcou com `.`. A lista acompanha a seleção acima e é também atualizada quando adiciona um marcador com `Ctrl+Win+F12` com a janela aberta.

Enquanto uma lista de marcadores tem o foco, as teclas de reprodução do separador que está por cima também funcionam nela: `←` / `→` retrocedem e avançam, `Shift+←` / `Shift+→` transpõem, `Page Up` / `Page Down` mudam a velocidade de reprodução, `Ctrl+←` / `Ctrl+→` passam para o episódio, livro ou faixa anterior ou seguinte, e `Alt+←` / `Alt+→` procuram 1 segundo.

| Tecla | Ação |
|---|---|
| `.` | Marca ou desmarca o marcador com o foco. Veja [Marcar e Remover Vários Itens](#marcar-e-remover-vários-itens). |
| `Enter` | Reproduz a partir do marcador com o foco. |
| `Space` | Põe em pausa se algo estiver a tocar; caso contrário, reproduz a partir do marcador com o foco. |
| `Delete` | Elimina todos os marcadores marcados, ou o que tem o foco se nenhum estiver marcado. Aparece primeiro uma caixa de diálogo de confirmação. |
| tecla Aplicações / `Shift+F10` | Abre o menu de contexto do marcador. |

### Menu de contexto do marcador

- **Reproduzir a partir do marcador** — se o item já estiver carregado, a reprodução salta para o marcador; caso contrário, o item começa a tocar a partir dessa posição.
- **Mudar o nome…** — dá ao marcador um nome próprio. Deixe o campo vazio para voltar ao nome predefinido.
- **Eliminar selecionados** — elimina os marcadores marcados, ou o que tem o foco se nenhum estiver marcado.
- **Adicionar ou editar texto…** — abre um campo de várias linhas para uma nota de texto. Deixe-o vazio para remover o texto.
- **Adicionar nota de voz…** — abre uma caixa de diálogo que começa a gravar a partir do microfone predefinido assim que aparece. Prima **Parar e guardar** para anexar a gravação ao marcador, ou **Cancelar** para a descartar. Adicionar uma nova nota de voz substitui a anterior.
- **Limpar notas** — remove a nota de texto e a nota de voz do marcador com o foco. Ativo apenas quando o marcador tem uma nota.
- **Repetir entre os marcadores marcados** — veja abaixo. Ativo quando pelo menos dois marcadores estão marcados.
- **Parar repetição** — desativa o modo de repetição. Ativo enquanto uma repetição estiver ativa.

### O que acontece quando a reprodução chega a um marcador

Durante a reprodução normal, quando a posição chega a um marcador, o freeAudio emite **dois sinais sonoros rápidos**. Se o marcador não tiver nota, a reprodução simplesmente continua.

Se o marcador tiver uma nota de texto e/ou de voz, a reprodução é **colocada em pausa**, o texto é lido pelo sintetizador atual do NVDA e a nota de voz é reproduzida, após o que a reprodução **retoma onde ficou**. Se parar a reprodução ou iniciar outra coisa enquanto a nota estiver a ser reproduzida, a reprodução não é retomada.

Os marcadores são detetados durante a reprodução normal. Avançar ou retroceder por cima de um marcador não o aciona.

### Repetir a secção entre marcadores

Marque com `.` dois ou mais marcadores **do mesmo item** e escolha **Repetir entre os marcadores marcados**. A reprodução salta para o marcador marcado mais antigo e repete em ciclo entre o mais antigo e o mais recente dos marcados, e o NVDA anuncia as duas posições. É útil para repassar uma passagem difícil de perceber, uma frase de aprendizagem de línguas ou uma peça musical que está a praticar. Escolha **Parar repetição** para voltar à reprodução normal. A repetição não é guardada entre sessões e, se outro item começar a tocar, o intervalo de repetição é ignorado e abandonado ao fim de cerca de 20 segundos.

### Armazenamento dos dados dos marcadores

Os marcadores são guardados em `freeAudio_bookmarks.json` na pasta de configuração do utilizador do NVDA, e as notas de voz como ficheiros `.wav` na pasta `freeAudio_bookmark_audio` junto a ela. Ambos podem ser copiados como cópia de segurança ou transferidos para outro computador. Eliminar um marcador elimina também o ficheiro da sua nota de voz. Todos os marcadores e notas de voz podem ser removidos de uma só vez com o item **Marcadores** da caixa de diálogo de limpeza — veja [Limpeza: repor definições e apagar dados guardados](#limpeza-repor-definições-e-apagar-dados-guardados).

Cada marcador pertence à chave de retoma do próprio item — o URL do episódio, o URL estável de catálogo da parte do audiolivro ou o caminho do ficheiro da faixa do jukebox. Um ficheiro do jukebox movido ou renomeado fora do freeAudio é, por isso, tratado como um item diferente e não mostra os seus marcadores antigos.

## Transposição (Alteração de Tom)

A transposição desloca o **tom** do que está a tocar para cima ou para baixo sem alterar a sua **velocidade** — o oposto do "efeito de esquilo" que obteria simplesmente acelerando uma faixa. É útil para corresponder ao alcance natural de um determinado narrador, transpor música para uma tonalidade mais agradável, ou apenas ajustar uma gravação para assentar mais confortavelmente nos seus ouvidos.

A transposição está disponível para **podcasts**, **audiolivros** e **faixas de jukebox** — o mesmo "média local, pesquisável e capaz de tempo" ao qual os atalhos de velocidade de reprodução já se aplicam. Não está disponível para estações de rádio em direto, que não têm um tom fixo para deslocar.

- **`Shift+Win+K`** — Aumenta o tom em um passo.
- **`Shift+Win+J`** — Diminui o tom em um passo.

Cada passo é **um oitavo de tom inteiro** — ou seja, **0,25 semitons** (um tom inteiro são 2 semitons, pelo que 8 passos fazem um tom inteiro e 48 passos fazem uma oitava). O intervalo é **−12,00 a +12,00 semitons**, ou seja, uma oitava completa para cima ou para baixo. O NVDA anuncia o novo valor após cada passo, por exemplo "**+1,25 semitons**"; voltar a 0,0 anuncia "**Tom normal**".

A transposição é memorizada entre faixas, da mesma forma que a velocidade de reprodução: defini-la uma vez enquanto uma faixa está a tocar significa que a próxima faixa capaz de tempo que reproduzir começa com o mesmo deslocamento, a menos que o seu próprio perfil de áudio guardado o substitua. Reproduzir uma faixa sem valor de transposição guardado repõe o deslocamento em 0,0 (Tom normal), tal como a mesma regra já se aplica à velocidade.

## Músicas Gostadas

Quando a opção **Guardar músicas gostadas em ficheiro de texto** está ativada, as informações de faixa copiadas para a área de transferência ao premir `Ctrl+Win+I` três vezes são também adicionadas linha a linha a `Documents\freeAudio Recordings\likedSongs.txt`.

Nas estações que difundem metadados ICY, o título e o artista da faixa são guardados diretamente. Nas estações sem metadados ICY, o resultado do reconhecimento Shazam é guardado no mesmo ficheiro — ambas as fontes partilham a mesma lista. O ficheiro é criado automaticamente se não existir; cada entrada é adicionada ao fim do ficheiro e as entradas anteriores nunca são eliminadas.

## Separador Músicas Gostadas

O separador **Músicas Gostadas** no navegador de estações exibe todas as faixas guardadas em `likedSongs.txt`. A lista é automaticamente recarregada a partir do ficheiro sempre que o separador é aberto. Clique com o botão direito numa música, ou selecione-a e prima a tecla Aplicações / `Shift+F10`, para abrir um menu de contexto com as mesmas ações descritas abaixo.

Um campo de **Filtro** acima da lista permite restringir as faixas apresentadas em tempo real. Escreva qualquer parte de um título de canção ou nome de artista e a lista atualiza-se instantaneamente a cada tecla pressionada. O NVDA anuncia o número de resultados correspondentes após cada alteração. Prima a seta `Para baixo` a partir do campo de filtro para mover o foco diretamente para a lista.

Selecionar uma faixa da lista ativa as seguintes ações:

- **Reproduzir no Spotify:** Tenta abrir diretamente a aplicação de ambiente de trabalho do Spotify. Se a aplicação não estiver instalada, recorre ao site do Spotify e reproduz automaticamente o primeiro resultado.
- **Reproduzir no YouTube (`Alt+O`):** Procura a faixa selecionada no YouTube e abre os resultados no navegador predefinido.
- **Mostrar letra:** Obtém e apresenta a letra da faixa selecionada. As letras são obtidas de [lrclib.net](https://lrclib.net) (gratuito, sem conta necessária). É anunciada uma breve mensagem "A obter letra…" enquanto a pesquisa decorre em segundo plano. Se forem encontradas letras, abrem-se numa caixa de diálogo só de leitura onde pode lê-las com o NVDA e copiá-las para a área de transferência. Se não forem encontradas letras, o NVDA anuncia-o. O botão é temporariamente desativado enquanto uma obtenção está em curso para evitar pedidos duplicados.
- **Remover (`Alt+M`):** Elimina a faixa selecionada de `likedSongs.txt` e atualiza a lista. A tecla `Delete` também aciona este botão quando a lista está em foco. Também pode marcar várias músicas de uma só vez e removê-las todas juntas — veja [Marcar e Remover Vários Itens](#marcar-e-remover-vários-itens) em Favoritos.
- **Atualizar (`Alt+E`):** Recarrega a lista a partir do ficheiro.

Os botões Spotify, YouTube, Mostrar letra e Remover só estão ativos quando uma faixa real é selecionada na lista.

### Serviço de letras

O freeAudio utiliza o [lrclib.net](https://lrclib.net) para obter letras — uma base de dados gratuita e aberta que não requer chave de API nem conta. O processo de pesquisa analisa a cadeia de faixas armazenada em `likedSongs.txt` e tenta consultas progressivamente mais amplas até encontrar letras:

1. Correspondência exata com o nome completo do artista e o título limpo (sufixos de ruído como "Remastered", "Live" ou etiquetas de ano são removidos antes da pesquisa).
2. Correspondência exata com o nome completo do artista e o título original (se a limpeza o alterou).
3. Correspondência exata com apenas o primeiro nome de artista e o título limpo (para cadeias com múltiplos artistas, como "Artista A & Artista B").
4. Pesquisa difusa com o primeiro nome de artista e o título limpo.
5. Pesquisa difusa com a cadeia de faixa bruta como último recurso.

Quando há letras em texto simples disponíveis, são apresentadas tal como estão. Quando apenas estão disponíveis letras LRC sincronizadas temporalmente, os carimbos de tempo são removidos e o texto simples é apresentado. As faixas instrumentais são reportadas como não encontradas.

## Definições

As seguintes opções podem ser configuradas em Menu NVDA → Preferências → Definições → freeAudio:

| Opção | Descrição |
|---|---|
| Voz de mudança de faixa | Escolha se as mudanças de faixa anunciadas automaticamente são faladas usando o sintetizador NVDA ou uma voz SAPI5 selecionada. |
| Voz SAPI5 | Quando **Voz de mudança de faixa** está definida para SAPI5, seleciona qual voz SAPI5 instalada é usada para anunciar mudanças de faixa. A lista é preenchida em segundo plano a partir das vozes instaladas no sistema. |
| Dispositivo de saída de áudio | Define o dispositivo de saída de áudio para reprodução de rádio. A lista inclui todos os dispositivos compatíveis com BASS no sistema, mais uma opção "Predefinição do sistema". As alterações são aplicadas imediatamente ao guardar; se o dispositivo selecionado for desligado, o complemento reverte automaticamente para a predefinição do sistema e anuncia a alteração. |
| Modo de atualização de dispositivos de áudio | Controla como o freeAudio atualiza os números dos dispositivos de saída BASS. O modo **Fiável** (predefinição) sonda dispositivos em tempo real e rastreia alterações Bluetooth/USB com mais precisão, mas pode tornar as alterações de dispositivo ligeiramente mais lentas. O modo **Rápido** usa a lista de dispositivos BASS atual e é mais rápido, mas os números dos dispositivos podem ficar desatualizados até o BASS ou o NVDA serem reiniciados. |
| Volume | Define o volume inicial do suplemento (0–100). Durante a reprodução, `Ctrl+Win+↑` pode aumentar o volume até 200, mas o volume inicial guardado aqui está limitado a 100. |
| Efeitos de áudio | Define quais efeitos (Chorus, Compressor, Distortion, Echo, Flanger, Gargle, Reverb e os três reforços de EQ) estão ativos quando o NVDA inicia ou uma estação começa a reproduzir. Vários efeitos podem ser selecionados ao mesmo tempo, correspondendo à lista de Efeitos no Navegador de Estações. |
| Ganho EQ (graves / agudos / vocal) | Define o nível de ganho em dB para cada banda EQ (−15 a +15). Estes valores aplicam-se quando o efeito EQ correspondente está ativo e são guardados globalmente. Substituições por estação podem ser armazenadas usando o botão **Guardar Perfil de Áudio** no separador Favoritos. |
| Transição entre estações | Controla o comportamento de transição ao mudar entre **estações de rádio em direto**. **Corte imediato** (predefinição) para a estação anterior imediatamente antes de a nova começar. **Transição curta (1 segundo)** e **Transição normal (2 segundos)** iniciam a nova estação sem pausa, desvanecendo gradualmente a anterior em segundo plano assim que o novo fluxo é confirmado. **Efeito sonoro de sintonização de estação** para a estação anterior imediatamente e reproduz um efeito sonoro de sintonização antes de a nova começar. Não tem efeito nem impacto no desempenho quando definido como Corte imediato. Não se aplica a podcasts, audiolivros ou faixas de jukebox — retomar esses reproduz sempre o seu próprio efeito sonoro breve de cassete, independentemente desta definição; veja [Detalhes de Reprodução de Podcasts](#detalhes-de-reprodução-de-podcasts). |
| Retomar última estação ao iniciar o NVDA | Quando ativado, a última estação reproduzida reinicia automaticamente sempre que o NVDA inicia. |
| Anunciar automaticamente mudanças de faixa (metadados ICY) | Quando ativado, o NVDA lê automaticamente o novo nome da faixa sempre que muda numa estação que difunde metadados ICY. A primeira faixa também é anunciada imediatamente ao mudar para uma nova estação. Desativado por predefinição. |
| Silenciar notificações | Quando ativado, o NVDA deixa de anunciar mudanças de estação, alterações do estado de reprodução (reproduzir, pausar, parar) e eventos de gravação (iniciada, parada, concluída). Mensagens de erro, feedback de favoritos, resultados do reconhecimento musical e notificações de atualização não são afetados. Pode também ser alternado em tempo real através de um gesto de entrada não atribuído. Desativado por predefinição. |
| Mostrar mensagens do freeAudio na linha braille | Quando ativado, o freeAudio também envia as suas notificações diretamente para o visor braille. Isto é útil para títulos de faixas, mudanças de estação, estado de reprodução e alterações de volume. Desativado por predefinição. |
| Ativar buffer de time-shift (recuar na rádio em direto) | Ativa ou desativa os controlos de retrocesso (`Ctrl+Win+J`/`Ctrl+Win+K`) e alarga a captura em segundo plano de cerca de 45 segundos até ao valor de **Duração do buffer de time-shift**. Uma pequena captura em segundo plano da estação que está a tocar corre sempre, mesmo com esta opção desativada — veja a nota na secção **Time-Shift (Recuar na Rádio em Direto)** acima. Também pode ser alternada instantaneamente com `Ctrl+Win+T`. Desativado por predefinição — veja a secção **Time-Shift (Recuar na Rádio em Direto)** acima para todos os pormenores. Não afeta podcasts nem audiolivros. |
| Duração do buffer de time-shift | Define o comprimento máximo do buffer de recuo. As opções variam de 10 minutos até 5 horas. Buffers mais longos consomem mais espaço temporário em disco. |
| Guardar músicas gostadas em ficheiro de texto | Quando ativado, as informações de faixa copiadas para a área de transferência ao premir `Ctrl+Win+I` três vezes são também adicionadas a `Documents\freeAudio Recordings\likedSongs.txt`. Se não existirem metadados ICY, o resultado do reconhecimento Shazam é guardado no mesmo ficheiro. Desativado por predefinição. |
| Quando Ctrl+Win+P é premido sem reprodução ativa | Determina o que acontece quando este atalho é premido e nada está a reproduzir: iniciar a última estação ou abrir a lista de favoritos. |
| Quando Ctrl+Win+P é premido duas vezes | Seleciona o que acontece quando o atalho é premido duas vezes rapidamente: não fazer nada, abrir a lista de favoritos, abrir o separador de gravação ou abrir o separador do temporizador. Quando "não fazer nada" está selecionado, a primeira pressão responde instantaneamente sem atraso. |
| Quando Ctrl+Win+P é premido três vezes | Seleciona o que acontece quando o atalho é premido três vezes rapidamente: não fazer nada, abrir a lista de favoritos, abrir o separador de pesquisa, abrir o separador de gravação ou abrir o separador do temporizador. |
| Verificar atualizações automaticamente ao iniciar | Quando ativado, é efetuada uma verificação de atualizações em segundo plano sempre que o NVDA inicia; é emitida uma notificação se for encontrada uma nova versão. Quando desativado, as verificações automáticas são interrompidas mas as verificações manuais continuam disponíveis. |
| Verificar atualizações agora | Um botão que verifica imediatamente se existe uma nova versão, mesmo que as verificações automáticas estejam desativadas. Enquanto a verificação decorre, o botão indica «A verificar...». |
| Caminho do ffmpeg.exe | Caminho para o ffmpeg.exe utilizado no reconhecimento musical. Se deixado em branco, é utilizado automaticamente um ffmpeg.exe na pasta do complemento. |
| Pasta de gravações | Define a pasta onde os ficheiros gravados são guardados. Se deixado em branco, é utilizada a localização predefinida `Documents\freeAudio Recordings\`. Um botão Procurar permite selecionar a pasta de forma interativa. As alterações têm efeito imediatamente após guardar. |
| Módulos | Uma lista de caixas de verificação com as partes opcionais do freeAudio: **Podcasts**, **Audiolivros** e **Jukebox**. As três estão ativas por predefinição. Desmarcar uma remove o seu separador do Navegador de Estações e os seus comandos da caixa de diálogo Definir comandos do NVDA, sem apagar nada do que lá guardou (subscrições, biblioteca, lista do Jukebox); voltar a marcá-la repõe tudo. As alterações aplicam-se na próxima vez que o Navegador de Estações for aberto. |
| Incluir unidades de rede ao pesquisar no Jukebox | Quando ativado, **Pesquisar no disco** do Jukebox também pesquisa unidades de rede. Desativado por predefinição, porque pesquisar uma partilha de rede pode demorar vários minutos ou bloquear se a partilha estiver inacessível. |
| Fontes de audiolivros | Uma lista de verificação que seleciona quais fontes de audiolivros (**GETEM**, **LibriVox**, **Project Gutenberg**) são pesquisadas e mostradas no separador Audiolivros. As três estão ativadas por predefinição. Desmarcar uma fonte oculta os seus livros dos resultados de pesquisa fundidos e da lista da biblioteca sem eliminar nada que já tenha adicionado dela — veja [Audiolivros (GETEM, LibriVox e Project Gutenberg)](#audiolivros-getem-librivox-e-project-gutenberg). |
| Nome de utilizador GETEM / Palavra-passe GETEM | As suas credenciais de adesão aos audiolivros [GETEM](https://getem.boun.edu.tr/), necessárias para transmitir ou descarregar o áudio de um livro — veja [Iniciar Sessão](#iniciar-sessão). Armazenadas encriptadas em disco através da Windows Data Protection API, associadas à sua conta de utilizador do Windows; nunca armazenadas como texto simples. Deixar ambos os campos vazios e guardar remove quaisquer credenciais armazenadas. O LibriVox e o Project Gutenberg não requerem conta e não têm campo equivalente. |
| Formato de saída da gravação | Mantém o fluxo original, extrai o áudio sem alterar o seu codec, ou converte gravações concluídas para MP3. A predefinição é o formato original do fluxo. |
| Débito binário de gravação MP3 | Define o débito binário usado quando o formato de saída da gravação é MP3. A predefinição é 128 kb/s. |
| Desativar verificação de conectividade à Internet antes de reproduzir | Recomendado para utilizadores que experimentam um atraso antes de uma estação começar a reproduzir. Também útil quando o DNS está bloqueado. |
| Limpeza: repor definições e apagar dados guardados... | Um botão que abre uma caixa de diálogo para repor as definições do freeAudio e apagar os dados que ele guardou — veja [Limpeza: repor definições e apagar dados guardados](#limpeza-repor-definições-e-apagar-dados-guardados). |

### Limpeza: repor definições e apagar dados guardados

O botão **Limpeza: repor definições e apagar dados guardados...** na parte inferior da página de definições do freeAudio abre a caixa de diálogo **Repor definições / apagar dados guardados**. Lista, como caixas de verificação, tudo o que o freeAudio guarda na pasta de configuração do NVDA. **Por predefinição, nenhuma está marcada.** Cada item mostra o espaço que ocupa, ou «nada guardado»:

- **Definições** — repostas para os valores predefinidos. A pasta de gravações e a opção **Guardar músicas gostadas em ficheiro de texto** são mantidas.
- **Estações favoritas**
- **Cache da lista de estações** — descarregada novamente quando necessário.
- **Subscrições de podcasts**
- **Bibliotecas de audiolivros** — GETEM, LibriVox e Project Gutenberg.
- **Início de sessão GETEM guardado** — o nome de utilizador e a palavra-passe guardados.
- **Lista do Jukebox** — os seus ficheiros de música não são apagados.
- **Posições de retoma guardadas** — podcasts, audiolivros e pastas do Jukebox.
- **Marcadores** — todos os marcadores, incluindo as notas de texto e de voz.
- **Temporizadores de adormecer e alarmes**
- **Planos de gravação agendados** — as gravações em si não são apagadas.

**Selecionar tudo** marca todos os itens. **Repor / apagar selecionados** executa a sua escolha; se nada estiver marcado, o freeAudio diz «Nada está selecionado.» **Cancelar** (ou `Escape`) fecha a caixa de diálogo sem fazer nada.

Antes de alterar seja o que for, o freeAudio lista os itens marcados, avisa que isto não pode ser desfeito e pede confirmação; a resposta predefinida é **Não**. Depois, uma mensagem diz «Concluído.» ou lista os itens que não puderam ser removidos — normalmente porque um ficheiro está em uso. Se o Navegador de Estações estiver aberto quando os dados guardados forem apagados, é fechado e reconstruído a partir dos dados restantes da próxima vez que o abrir.

As gravações, a pasta de gravações e o ficheiro de texto das músicas gostadas **nunca** são tocados, e repor as definições não faz o freeAudio voltar a importar dados do suplemento FreeRadio anterior.

Depois de repor as definições, os valores que ainda aparecem na página de definições não são guardados ao premir OK, pelo que não podem desfazer a reposição. Recomenda-se reiniciar o NVDA para que todas as definições tenham efeito.

## Silenciamento de Notificações

Quando a opção **Silenciar notificações** está ativada nas Definições, o NVDA suprime os seguintes anúncios automáticos:

- Nome da estação quando uma nova estação começa a reproduzir
- Alterações do estado de reprodução: reproduzir, pausar, parar
- Modo Obligato: iniciado / parado
- Eventos de gravação: iniciada, parada, concluída (gravações instantâneas, de música, de todas as músicas e agendadas)
- Anúncios de mudança de faixa, mesmo quando **Anunciar automaticamente mudanças de faixa** também está ativo
- O aviso de que uma estação está a ser reproduzida num modo de compatibilidade especial (veja [Reprodução](#reprodução))

Os seguintes anúncios **não** são afetados intencionalmente: mensagens de erro, feedback de favoritos (adicionado / já na lista), resultados do reconhecimento musical e notificações de atualização.

A definição pode ser alternada em Menu NVDA → Preferências → Definições → freeAudio, ou em tempo real através de um gesto de entrada não atribuído (atribua um em Menu NVDA → Preferências → Definir comandos → freeAudio). Quando alternada, o NVDA anuncia uma vez "Notificações silenciadas" ou "Notificações reativadas" para confirmar a alteração.

## Anúncio Automático de Mudanças de Faixa

Quando a opção **Anunciar automaticamente mudanças de faixa** está ativada nas Definições, o freeAudio verifica os metadados ICY da estação ativa em segundo plano aproximadamente a cada 5 segundos. Quando a faixa muda, o novo título é automaticamente lido pelo NVDA — sem necessidade de premir qualquer tecla.

Ao mudar para uma nova estação, as primeiras informações de faixa são anunciadas assim que a ligação é estabelecida. Se mudar para uma estação que não difunde metadados ICY, o sistema permanece silencioso e as informações da faixa anterior não são repetidas.

Esta funcionalidade está desativada por predefinição e pode ser ativada em Menu NVDA → Preferências → Definições → freeAudio.

## Reprodução

O freeAudio usa o **BASS** como o seu único backend de reprodução para tudo — rádio pela Internet, podcasts, audiolivros e faixas de jukebox. Não é necessária instalação separada; está incluído no complemento. O freeAudio não utiliza o VLC, o PotPlayer nem o Windows Media Player.

O BASS envia o áudio diretamente para a pilha de áudio do Windows e aparece no misturador de volume do Windows como uma fonte de áudio independente com o nome "pythonw.exe", separada do NVDA. Isto significa que o áudio do freeAudio circula num canal completamente separado do sintetizador de voz do NVDA: o rádio não é interrompido, não se mistura nem é afetado pelas definições de áudio do NVDA enquanto este fala. O utilizador pode ajustar o volume do rádio independentemente do NVDA no Misturador de Volume do Windows. Suporta HTTP, HTTPS e a maioria dos formatos de transmissão incorporados.

Episódios de podcast, capítulos de audiolivros e faixas de jukebox são reproduzidos através do BASS porque este pode abrir o fluxo como um ficheiro pesquisável (mesmo durante o descarregamento), permitindo um rastreio preciso da posição, recuo/avanço escalonado, velocidade de reprodução, transposição de tom e retoma. O espelho de áudio, o time-shift e a procura/retoma de podcasts/audiolivros/jukebox dependem todos do BASS e estão sempre disponíveis.

**Estações HLS que precisam do modo de compatibilidade:** algumas estações HLS (`.m3u8`) empacotam o áudio de uma forma que o BASS não consegue ler com fluidez — volta sempre a abrir o fluxo, o que soa a falhas constantes. Para estas (atualmente as transmissões de rádio da ABC Australia), o freeAudio reempacota automaticamente o mesmo áudio, sem o recodificar, num formato convencional, através de um pequeno servidor que corre apenas no seu computador, e reproduz esse em vez do original. Não é preciso configurar nada. Quando reproduz uma destas estações pela primeira vez depois de o NVDA arrancar, o NVDA diz «Esta estação usa um modo de reprodução especial para evitar falhas.» Este anúncio respeita a definição **Silenciar notificações**.

## Verificação de Atualizações

O freeAudio verifica automaticamente a existência de novas versões através do GitHub.

**Verificação automática:** É executada silenciosamente em segundo plano 15 segundos após o NVDA iniciar. Se for encontrada uma nova versão, é emitida uma notificação; se não for encontrada nenhuma, não é apresentada qualquer mensagem.

**Verificação manual:** Pode ser acionada em qualquer altura em Ferramentas NVDA → freeAudio → **Verificar Atualizações…**. Quando iniciada desta forma, o resultado é anunciado mesmo que a versão esteja atualizada.

**Quando é encontrada uma atualização:** Abre-se uma caixa de diálogo com o número da versão e a sua versão instalada.

- Se estiver disponível um ficheiro `.nvda-addon` diretamente descarregável na versão do GitHub, é apresentado o botão **Descarregar e Instalar**. Após confirmação, o ficheiro é descarregado em segundo plano, o NVDA anuncia quando o descarregamento inicia e o ecrã de instalação do NVDA abre automaticamente.
- Se não estiver disponível uma ligação de descarregamento direto, é apresentado o botão **Abrir Página** e a página da versão do GitHub abre no browser predefinido.

**Para desativar as verificações automáticas:** Desative a opção **Verificar atualizações automaticamente ao iniciar** em Menu NVDA → Preferências → Definições → freeAudio.

## Agradecimentos e Créditos

* **Base e Conceitos Originais:** Um sincero agradecimento a **Gary Mp** ([GaryMp/freeradio](https://github.com/GaryMp/freeradio)) pelos conceitos originais do complemento de rádio e pelas estruturas centrais de gestão de favoritos que serviram de base fundacional para este projeto.
* **Ferramentas de IA e LLM:** Reconhecimento grato às ferramentas modernas de Modelos de Linguagem de Grande Escala (LLM) (incluindo Claude, ChatGPT e Gemini) pela assistência durante as fases de desenvolvimento, refatoração de código e implementação de funcionalidades.
* **Serviço de Diretório:** O diretório de estações é fornecido pela [Radio Browser API](https://www.radio-browser.info/).
* **Comunidade:** Um sincero agradecimento a todos os membros da comunidade NVDA e tradutores pelo seu apoio contínuo, feedback e contribuições de localização.

## Licença

GPL v2