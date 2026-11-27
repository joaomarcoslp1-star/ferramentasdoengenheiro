# -*- coding: utf-8 -*-
"""Carrosséis 1080x1350 dos exercícios: capa, enunciado+figura, resolução, resposta+CTA."""
import asyncio, base64, json, os, sys
from playwright.async_api import async_playwright
sys.path.insert(0, os.path.dirname(__file__))
from figs import FIGS

EX = json.load(open('/home/claude/exer/exercicios.json'))
LOGO = base64.b64encode(open('/home/claude/site_src/img/logo-192.png', 'rb').read()).decode()
OUT = '/home/claude/exer/out'
CSS = """*{box-sizing:border-box}body{margin:0;width:1080px;height:1350px;overflow:hidden;background:#0f2742;font-family:Arial,Helvetica,sans-serif;color:#fff;position:relative}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:54px 54px}
.wrap{position:absolute;inset:0;padding:90px 80px 0}
.bd{display:inline-block;background:#f28c28;color:#1c2430;font-weight:700;font-size:28px;padding:12px 28px;border-radius:30px}
.bd.az{background:#5b9bff}.tag{display:inline-block;margin-left:12px;font-size:26px;color:#c9d6e6;border:2px solid rgba(255,255,255,.2);padding:9px 20px;border-radius:30px}
h1{font-size:74px;line-height:1.1;margin:40px 0 0;font-weight:800}h2{font-size:52px;line-height:1.15;margin:30px 0 0;font-weight:800}
em{font-style:normal;color:#f9a24b}.en{font-size:40px;line-height:1.38;margin-top:28px}
.fig{margin-top:26px;text-align:center}.fig svg{max-width:100%;height:auto}
.alts{margin-top:22px;font-size:38px;line-height:1.55}.alts b{color:#f9a24b;margin-right:12px}
.step{display:flex;gap:22px;align-items:flex-start;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.1);border-radius:22px;padding:26px 30px;margin-top:22px;font-size:37px;line-height:1.38}
.step .n{flex:none;width:58px;height:58px;border-radius:50%;background:#f28c28;color:#1c2430;font-weight:800;display:flex;align-items:center;justify-content:center;font-size:32px}
.ans{margin-top:34px;background:#e8f5ec;color:#123d24;border-radius:24px;padding:34px 38px;font-size:46px;font-weight:800;line-height:1.3}
.tip{margin-top:30px;font-size:36px;line-height:1.4;color:#ffd166}
.cta{margin-top:44px;background:rgba(255,255,255,.07);border:3px solid rgba(255,255,255,.12);border-radius:26px;padding:34px;text-align:center}
.foot{position:absolute;left:80px;right:80px;bottom:56px;display:flex;align-items:center;justify-content:space-between;font-size:26px;color:#c9d6e6}
.foot img{width:54px;height:54px;border-radius:12px;margin-right:16px;vertical-align:middle}.pg{color:#f9a24b;font-weight:700}
.big{font-size:44px;color:#c9d6e6;margin-top:36px;line-height:1.4}
"""

def foot(n, tot=4):
    return (f"<div class=foot><div><img src='data:image/png;base64,{LOGO}'>@ferramentasdoengenheiro</div>"
            f"<div class=pg>{n}/{tot}{' →' if n < tot else ''}</div></div>")

def page(body):
    return f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=grid></div><div class=wrap>{body}</div></body></html>"

def slides(e):
    conc = e['publico'] == 'concurso'
    bd = f"<span class='bd{'' if conc else ' az'}'>{e['serie']}</span><span class=tag>{e['materia']}</span>"
    fig = FIGS[e['fig']]()
    s1 = page(bd + f"<h1>{e['titulo']}</h1><div class=fig style='margin-top:60px'>{fig}</div>"
              f"<div class=big>{'Questão inédita no estilo Cesgranrio.' if conc else 'Exercício de faculdade, resolvido passo a passo.'}<br><b style='color:#fff'>Tente antes de arrastar →</b></div>" + foot(1))
    alts = ''
    if conc:
        alts = "<div class=alts>" + ''.join(f"<div><b>({'ABCDE'[i]})</b>{a}</div>" for i, a in enumerate(e['alts'])) + "</div>"
    s2 = page(bd + f"<div class=en>{e['enunciado']}</div>" + (f"<div class=fig>{fig}</div>" if not conc else '') + alts
              + "<div class=tip style='margin-top:26px'>✍ Resolva no papel e confira no próximo slide.</div>" + foot(2))
    steps = ''.join(f"<div class=step><div class=n>{i+1}</div><div>{p}</div></div>" for i, p in enumerate(e['passos']))
    s3 = page(bd + "<h2>Resolução</h2>" + steps + foot(3))
    s4 = page(bd + "<h2>Resposta</h2>" + f"<div class=ans>{e['resposta']}</div>" + f"<div class=tip>{'⚠ ' if conc else '💡 '}{e['dica']}</div>"
              + "<div class=cta><div style='font-size:42px;font-weight:800'>Mais exercícios e calculadoras grátis</div>"
              "<div style='font-size:36px;color:#f9a24b;font-weight:700;margin-top:10px'>link na bio · ferramentasdoengenheiro.com</div></div>" + foot(4))
    return [s1, s2, s3, s4]

async def main(ids):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for e in EX:
            if ids and e['id'] not in ids: continue
            d = f"{OUT}/{e['id']}"; os.makedirs(d, exist_ok=True)
            for i, h in enumerate(slides(e), 1):
                await pg.set_content(h); await pg.wait_for_timeout(150)
                over = await pg.evaluate("()=>{const f=document.querySelector('.foot').getBoundingClientRect().top;return Math.max(...[...document.querySelectorAll('.wrap > *:not(.foot)')].map(x=>x.getBoundingClientRect().bottom))-f}")
                if over > -10: print('OVERFLOW', e['id'], i, round(over))
                await pg.screenshot(path=f"{d}/{i}.jpg", type="jpeg", quality=90)
        await b.close()

asyncio.run(main(sys.argv[1:]))
