# Área de Estudo PRF

Site estático (HTML, CSS e JavaScript). Não precisa de build.

## Jeito mais seguro: imagens dentro do HTML (recomendado para a Vercel)

Se as imagens aparecem no seu computador mas somem na Vercel, use este caminho.

1. Abra o arquivo `embutir-imagens.html` com um duplo clique (abre no navegador).
2. Escolha o `index.html` deste pacote e selecione todas as imagens da sua pasta `fichas` (Ctrl+A).
3. Clique em "Gerar o arquivo". O navegador baixa um `index.html` novo, já com as imagens dentro.
4. No GitHub, substitua o `index.html` por esse novo. Não precisa enviar a pasta `fichas/`.
5. A Vercel publica sozinha. Em *Framework Preset* use **Other**, sem comando de build.

A página mostra quantas das 28 imagens foram encontradas e lista as que faltaram.
O casamento é pelo nome do arquivo, sem diferenciar maiúsculas de minúsculas e ignorando a extensão.

## Jeito alternativo: pasta fichas/ no repositório

Envie `index.html` e a pasta `fichas/` com os `.webp`. Os nomes precisam ser idênticos aos de
`fichas/LEIA-ME.txt`, em minúsculas, porque a Vercel diferencia maiúsculas de minúsculas
(o Windows não, e por isso pode funcionar no seu computador e falhar na Vercel).
Para testar uma imagem, abra `seusite.vercel.app/fichas/tema-do-texto.webp`.

## Links dos PDFs

Ficam no começo do script do `index.html`, na linha `var LINKS={...}`.
