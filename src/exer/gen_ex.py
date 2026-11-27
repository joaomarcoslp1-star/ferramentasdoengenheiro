# -*- coding: utf-8 -*-
"""Gera posts/ex-<id>.html e img/ex-<id>.jpg para os exercícios resolvidos."""
import asyncio, json, os, sys, html as H
D = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, D)
from figs import FIGS
EX = json.load(open(f'{D}/exercicios.json'))
SS = '/home/claude/site_src'
TOOLN = {'/calculadoras/vigas-cortante-e-momento-fletor/': 'calculadora de vigas', '/calculadoras/momento-de-inercia/': 'calculadora de momento de inércia',
         '/calculadoras/tabela-de-perfis-e-tubos/': 'tabela de perfis e tubos', '/calculadoras/torque-de-aperto-de-parafusos/': 'calculadora de torque de aperto',
         '/calculadoras/categoria-vaso-de-pressao-nr-13/': 'calculadora de categoria NR-13', '/calculadoras/perda-de-carga/': 'calculadora de perda de carga',
         '/calculadoras/queda-de-tensao/': 'calculadora de queda de tensão'}
BOX = 'background:#f6f8fb;border:1px solid #dde3ec;border-radius:12px;padding:18px 20px;margin:14px 0'

def post(e):
    conc = e['publico'] == 'concurso'; k = e['id']
    intro = (f"<p>Questão no estilo das bancas de concursos de engenharia (Petrobras, Transpetro, Cesgranrio e similares), com resolução comentada e a pegadinha que mais derruba candidatos. Tente resolver antes de abrir a resolução.</p>" if conc else
             f"<p>Exercício de {e['materia']} no nível das provas da faculdade, resolvido passo a passo. Tente resolver antes de abrir a resolução e confira o resultado na <a href=\"{e['tool']}\">{TOOLN[e['tool']]}</a>.</p>")
    vid = (f'<figure style="margin:8px auto 24px;max-width:340px;text-align:center"><video controls playsinline preload="none" poster="/ig/ex-{k}/poster.jpg" '
           f'style="width:100%;border-radius:14px;background:#0f2742;aspect-ratio:9/16" aria-label="Vídeo: resolução do exercício"><source src="/ig/ex-{k}/reel.mp4" type="video/mp4"></video>'
           f'<figcaption style="font-size:.85rem;color:#5a6575;margin-top:6px">▶ Resolução narrada em menos de 1 minuto.</figcaption></figure>')
    enun = f'<h2>Enunciado</h2><div style="{BOX}"><p style="margin-top:0">{e["enunciado"]}</p><div class="exfig" style="max-width:520px;margin:0 auto;background:#0f2742;border-radius:10px;padding:10px">{FIGS[e["fig"]]().replace("<svg ", '<svg style="width:100%;height:auto;display:block" ', 1)}</div>'
    if conc:
        enun += '<div id="alts" style="margin-top:14px">' + ''.join(
            f'<button type="button" data-i="{i}" style="display:block;width:100%;text-align:left;margin:6px 0;padding:10px 14px;border:1px solid #c9d3e0;border-radius:8px;background:#fff;font-size:1rem;cursor:pointer"><b>({"ABCDE"[i]})</b> {a}</button>'
            for i, a in enumerate(e['alts'])) + '</div><p id="fb" style="font-weight:700;min-height:1.5em"></p>'
        enun += ('<script>(function(){var c=' + str(e['certa']) + ';document.querySelectorAll("#alts button").forEach(function(b){b.onclick=function(){var i=+b.dataset.i;'
                 'document.querySelectorAll("#alts button").forEach(function(x){x.style.background="#fff"});b.style.background=i===c?"#e8f5ec":"#fdecea";'
                 'document.getElementById("fb").textContent=i===c?"Correto! Confira a resolução abaixo.":"Não é essa. Tente de novo ou abra a resolução.";}})})();</script>')
    enun += '</div>'
    passos = ''.join(f'<li style="margin:8px 0">{p}</li>' for p in e['passos'])
    sol = (f'<details style="{BOX}"><summary style="cursor:pointer;font-weight:700;font-size:1.1rem">Ver a resolução</summary>'
           f'<ol style="padding-left:22px">{passos}</ol><p style="background:#e8f5ec;color:#123d24;border-radius:8px;padding:12px 16px;font-weight:700">Resposta: {e["resposta"]}</p>'
           f'<p style="border-left:4px solid #f28c28;padding:6px 14px;background:#fff7ee">{e["dica"]}</p></details>')
    cta = (f'<p style="{BOX};border-left:4px solid #1f6feb">Quer testar com outros valores? Use a <a href="{e["tool"]}"><b>{TOOLN[e["tool"]]}</b></a>, grátis e sem cadastro.'
           + (' Treine mais no <a href="/simulados/engenharia-mecanica-petrobras/">simulado de Engenharia Mecânica</a>.' if conc else '') + '</p>')
    outros = [x for x in EX if x['publico'] == e['publico'] and x is not e]
    lista = '<h2>Mais exercícios</h2><ul>' + ''.join(f'<li><a href="/exercicios/{x["slug"]}/">{x["titulo"]}</a></li>' for x in outros) + '</ul><p><a href="/exercicios/">Ver todos os exercícios</a></p>'
    return (f'<div style="font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.65;color:#1c2430;max-width:860px;margin:0 auto">'
            f'{intro}{enun}{vid}<h2>Resolução</h2><p>Pausou e tentou? Abra para conferir.</p>{sol}{cta}{lista}</div>')

COVER = """<html><head><meta charset=utf-8><style>body{{margin:0;width:1200px;height:630px;background:#0f2742;font-family:Arial,Helvetica,sans-serif;color:#fff;position:relative;overflow:hidden}}
.g{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:40px 40px}}
.l{{position:absolute;left:60px;top:60px;width:600px}}.bd{{display:inline-block;background:{cor};color:#1c2430;font-weight:700;font-size:24px;padding:10px 22px;border-radius:30px}}
h1{{font-size:54px;line-height:1.1;margin:30px 0 0}}.m{{font-size:26px;color:#c9d6e6;margin-top:24px}}.f{{position:absolute;right:40px;top:0;bottom:0;width:480px;display:flex;align-items:center}}.f svg{{width:100%;height:auto}}
.s{{position:absolute;left:60px;bottom:44px;font-size:22px;color:#c9d6e6}}</style></head><body><div class=g></div><div class=l><span class=bd>{serie}</span><h1>{titulo}</h1><div class=m>{materia} · resolução passo a passo</div></div>
<div class=f>{fig}</div><div class=s>ferramentasdoengenheiro.com</div></body></html>"""

async def capas():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg = await b.new_page(viewport={"width": 1200, "height": 630})
        for e in EX:
            await pg.set_content(COVER.format(cor='#f28c28' if e['publico'] == 'concurso' else '#5b9bff', serie=e['serie'], titulo=e['titulo'], materia=e['materia'], fig=FIGS[e['fig']]()))
            await pg.screenshot(path=f"{SS}/img/ex-{e['id']}.jpg", type='jpeg', quality=85)
        await b.close()

for e in EX:
    open(f"{SS}/posts/ex-{e['id']}.html", 'w').write(post(e))
if '--capas' in sys.argv: asyncio.run(capas())
print('ok')
