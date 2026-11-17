# Zezé Di Camargo & Luciano — 1999 (player)

Player estático (HTML/CSS/JS, sem build) para GitHub Pages. Dados em `data/album.js`.

## Dia e Noite = duas capas
- **Dia** usa a capa branca do álbum (`assets/cover.jpg`, p&b): papel branco, preto da blusa e cinzas da camisa.
- **Noite** usa a foto colorida (`assets/foto.jpg`): preto da blusa, camisa vinho listrada e pele como destaque.
O botão Dia/Noite troca a capa (com transição), o fundo desfocado e toda a paleta. A escolha fica salva.

## Paletas (medidas nos pixels)
Dia: white `#FFFFFF`, mist `#F1F7F4`, silver `#95A29A`, slate `#56665C`, deep `#0F1B18`, ink `#000201`.
Noite: black `#030609`, hair `#231F1B`, maroon `#471F1B`, wine `#572A26`, stripe `#90443E`, skin `#DE9D7B`, shadow `#744E35`, snow `#FAFBFB`.

## Identidade
- **Progresso = o logo da capa**: por onde a faixa já passou, as letras prateadas "ZEZE DI CAMARGO & LUCIANO" se preenchem (preto no Dia, vermelho-vinho da camisa na Noite), com máscara real das letras de cada imagem. Clique/arraste no logo para buscar na faixa.
- A divisória são as listras reais da camisa (cinza no Dia, vinho na Noite).
- Fontes: Marcellus (títulos) e Jost (texto), ambas OFL em `assets/fonts/`.
- Central de mídia (Media Session) com capa, anterior/próxima e seek.

## Arquivos
`index.html`, `css/style.css`, `js/{app,player,ui}.js`, `data/album.js` (ganhou `coverNight` e o bloco `palette`), `assets/{cover.jpg, foto.jpg, cover-256.jpg, cover-512.jpg, foto-256.jpg, logo-dia.webp, logo-noite.webp, listras.jpg, fonts/}`, `tools/`.
`assets/zcl.png` e `assets/zclogo.png` não são mais usados.
