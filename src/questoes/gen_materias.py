# -*- coding: utf-8 -*-
import sys, io, contextlib
with contextlib.redirect_stderr(io.StringIO()):
    import build
from build import Q, page
from materias import MATERIAS
OUT = "/home/claude/site_src/posts"
import os; os.makedirs(OUT, exist_ok=True)
FULL = "/simulados/engenharia-mecanica-petrobras/"
meta = []
for mat, m in MATERIAS.items():
    sub = [x for x in Q if x["mat"] == mat]
    n = len(sub)
    outros = " · ".join(f'<a href="/simulados/{o["slug"]}/">{k}</a>' for k, o in MATERIAS.items() if k != mat)
    top = f"""<div style="font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.65;color:#1c2430;max-width:860px;margin:0 auto">
<p>Treine <b>{mat}</b> com <b>{n} questões inéditas</b> no estilo da Cesgranrio, a banca dos concursos de Engenharia Mecânica da <b>Petrobras</b> e da <b>Transpetro</b>. Antes das questões, veja o resumo do que mais cai, as fórmulas essenciais e as pegadinhas mais comuns. Depois, responda no modo estudo ou cronometrado e acompanhe seu desempenho.</p>
<p style="font-size:.85rem;color:#5a6575;background:#f6f8fb;border-left:4px solid #f28c28;padding:10px 14px;border-radius:6px">Questões inéditas, elaboradas pelo Ferramentas do Engenheiro para treino. Não são questões oficiais e não têm vínculo com a Cesgranrio, a Petrobras ou a Transpetro.</p>
<h2>O que mais cai de {mat}</h2>
{m["resumo"]}
<h2>{n} questões de {mat} com resolução</h2>
"""
    bottom = f"""
<h2>Continue treinando</h2>
<p>Quer o simulado completo, com as 70 questões de todas as matérias e o tempo de prova? Faça o <a href="{FULL}"><b>simulado de Engenharia Mecânica Petrobras e Transpetro</b></a>. Seu desempenho é somado entre todas as páginas de questões do site.</p>
<p><b>Outras matérias:</b> {outros}.</p>
</div>"""
    open(f"{OUT}/materia-{m['slug']}.html", "w").write(top + page(sub) + bottom)
    meta.append(dict(mat=mat, slug=m["slug"], n=n, cover=(m["cover"][0], f"{n} questões comentadas")))
import json; json.dump(meta, open(f"{OUT}/materias.json", "w"), ensure_ascii=False, indent=1)
print(len(meta), sum(x["n"] for x in meta))
