#!/usr/bin/env python3
"""Embute as imagens da pasta fichas/ dentro do index.html.

Como usar:
  1. Deixe este arquivo, o index.html e a pasta fichas/ na mesma pasta.
  2. Rode:  python3 embutir-imagens.py
  3. Suba o arquivo gerado, index-publicar.html, onde você publica.
     Ele não precisa da pasta fichas/.
"""
import base64, json, os, re, sys

aqui = os.path.dirname(os.path.abspath(__file__))
entrada = os.path.join(aqui, "index.html")
pasta = os.path.join(aqui, "fichas")
saida = os.path.join(aqui, "index-publicar.html")

if not os.path.isfile(entrada) or not os.path.isdir(pasta):
    sys.exit("Coloque index.html e a pasta fichas/ ao lado deste script.")

mime = {".webp": "image/webp", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}
dados, ignorados = {}, []
for nome in sorted(os.listdir(pasta)):
    base, ext = os.path.splitext(nome)
    if ext.lower() not in mime:
        continue
    with open(os.path.join(pasta, nome), "rb") as f:
        b64 = base64.b64encode(f.read()).decode("ascii")
    dados[base.lower().strip()] = "data:%s;base64,%s" % (mime[ext.lower()], b64)

html = open(entrada, encoding="utf-8").read()
if "var IMGDATA={};" not in html:
    sys.exit("Este index.html já foi processado ou não tem o marcador IMGDATA.")
ids = re.findall(r'\["([a-z0-9-]+)","', html.split("var FICHAS=[")[1].split("].map")[0])
faltam = [i for i in ids if i not in dados]
html = html.replace("var IMGDATA={};", "var IMGDATA=" + json.dumps(dados) + ";", 1)
open(saida, "w", encoding="utf-8").write(html)

mb = os.path.getsize(saida) / 1048576
print("Imagens embutidas: %d de %d" % (len(ids) - len(faltam), len(ids)))
if faltam:
    print("Faltaram (confira os nomes): " + ", ".join(faltam))
print("Arquivo gerado: index-publicar.html (%.1f MB)" % mb)
if mb > 15:
    print("Atenção: acima de 15 MB. Reduza o tamanho das imagens ou publique a pasta normalmente.")
