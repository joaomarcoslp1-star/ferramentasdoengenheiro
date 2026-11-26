"""Carrossel Instagram 1080x1350: tabela de torque de parafusos."""
import asyncio, base64, os
from playwright.async_api import async_playwright

OUT = "/home/claude/site_src/ig/torque"
os.makedirs(OUT, exist_ok=True)
CAPA = "/home/claude/ferramentasdoengenheiro/src/img-ia/capa-torque-parafusos.png"
LOGO = "/home/claude/site_src/img/logo-192.png"

B = {'M6': (6, 20.1), 'M8': (8, 36.6), 'M10': (10, 58.0), 'M12': (12, 84.3), 'M14': (14, 115),
     'M16': (16, 157), 'M18': (18, 192), 'M20': (20, 245), 'M22': (22, 303), 'M24': (24, 353),
     'M27': (27, 459), 'M30': (30, 561)}
SP = {'8.8': (580, 600), '10.9': (830, 830), '12.9': (970, 970)}


def torque(b, c, k=0.20, pct=0.75):
    d, at = B[b]
    sp = SP[c][0] if d <= 16 else SP[c][1]
    f = pct * at * sp  # N
    return k * f * d / 1000  # N·m


def br(x):
    s = f"{x:,.0f}" if x >= 100 else f"{x:.1f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def b64(p):
    return base64.b64encode(open(p, "rb").read()).decode()


CSS = """
*{box-sizing:border-box}
body{margin:0;width:1080px;height:1350px;overflow:hidden;font-family:Arial,Helvetica,sans-serif;color:#fff;
 background:#0f2742;position:relative}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),
 linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:54px 54px}
.wrap{position:absolute;inset:0;padding:90px 80px 0}
.bd{display:inline-block;background:#f28c28;color:#1c2430;font-weight:700;font-size:26px;padding:12px 28px;border-radius:30px}
h1{font-size:78px;line-height:1.08;margin:34px 0 0;font-weight:800}
h2{font-size:72px;line-height:1.1;margin:30px 0 0;font-weight:800}
em{font-style:normal;color:#f9a24b}
.sub{font-size:36px;color:#c9d6e6;margin-top:22px;line-height:1.35}
table{width:100%;border-collapse:collapse;margin-top:50px;font-size:50px}
th{font-size:32px;color:#f9a24b;text-align:right;padding:0 18px 18px;font-weight:700}
th:first-child{text-align:left}
td{padding:30px 18px;text-align:right;border-top:2px solid rgba(255,255,255,.1);font-variant-numeric:tabular-nums}
td:first-child{text-align:left;font-weight:800}
tr:nth-child(even) td{background:rgba(255,255,255,.04)}
.foot{position:absolute;left:80px;right:80px;bottom:60px;display:flex;align-items:center;justify-content:space-between;
 font-size:26px;color:#c9d6e6}
.foot img{width:54px;height:54px;border-radius:12px;margin-right:16px;vertical-align:middle}
.pg{color:#f9a24b;font-weight:700}
.note{font-size:30px;color:#c9d6e6;margin-top:30px;line-height:1.4}
.card{background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.1);border-radius:24px;padding:30px 36px;margin-top:26px}
.row{display:flex;justify-content:space-between;align-items:center;font-size:40px;padding:34px 0;border-top:2px solid rgba(255,255,255,.08)}
.row:first-child{border-top:0}
.row b{font-size:52px}
.bad{color:#ff8a7a}.ok{color:#7fd6a0}
.formula{font-size:80px;font-weight:800;margin-top:70px;color:#f9a24b;letter-spacing:1px}
"""


def foot(n):
    return (f"<div class=foot><div><img src='data:image/png;base64,{b64(LOGO)}'>@ferramentasdoengenheiro</div>"
            f"<div class=pg>{n}/5 →</div></div>")


def page(body, bg=""):
    return f"<html><head><meta charset=utf-8><style>{CSS}</style></head><body>{bg}<div class=grid></div><div class=wrap>{body}</div></body></html>"


def tabela(bitolas):
    rows = "".join(f"<tr><td>{b}</td>" + "".join(f"<td>{br(torque(b, c))}</td>" for c in SP) + "</tr>" for b in bitolas)
    return f"<table><tr><th>Bitola</th><th>Classe 8.8</th><th>10.9</th><th>12.9</th></tr>{rows}</table>"


s1_bg = (f"<div style=\"position:absolute;inset:0;background:url(data:image/png;base64,{b64(CAPA)}) 100% 96%/auto 56% no-repeat\"></div>"
         "<div style='position:absolute;inset:0;background:linear-gradient(180deg,#0f2742 0%,#0f2742 42%,rgba(15,39,66,.55) 62%,rgba(15,39,66,.15) 100%)'></div>")
s1 = page("<div class=bd>SALVE PARA CONSULTAR</div>"
          "<h1>Tabela de torque<br>de aperto de<br><em>parafusos</em></h1>"
          "<div class=sub>Classes 8.8 · 10.9 · 12.9<br>Bitolas M6 a M30, em N·m</div>" + foot(1), s1_bg)

cond = "<div class=note>Rosca métrica grossa, zincada (K = 0,20), pré-carga de 75% da carga de prova (ISO 898-1). Valores em N·m.</div>"
s2 = page("<div class=bd>TABELA · PARTE 1</div><h2>M6 a M16</h2>" + tabela(['M6', 'M8', 'M10', 'M12', 'M14', 'M16']) + cond + foot(2))
s3 = page("<div class=bd>TABELA · PARTE 2</div><h2>M18 a M30</h2>" + tabela(['M18', 'M20', 'M22', 'M24', 'M27', 'M30']) + cond + foot(3))

ks = [("Seco, sem acabamento", 0.30), ("Zincado", 0.20), ("Com óleo", 0.18), ("Pasta MoS₂", 0.12)]
rows = "".join(f"<div class=row><span>{n} <span style='color:#8fa3bb'>(K = {str(k).replace('.', ',')})</span></span><b>{br(torque('M12', '8.8', k))} N·m</b></div>" for n, k in ks)
s4 = page("<div class=bd>ATENÇÃO</div><h2>A lubrificação<br><em>muda tudo</em></h2>"
          "<div class=sub>Mesmo parafuso M12 classe 8.8, mesma pré-carga (36,7&nbsp;kN):</div>"
          f"<div class=card>{rows}</div>"
          "<div class=note><span class=bad>✕</span> Usar o torque “a seco” num parafuso lubrificado pode passar do limite e escoar o parafuso.<br>"
          "<span class=ok>✓</span> Sempre confira a condição da rosca antes de apertar.</div>" + foot(4))

s5 = page("<div class=bd>CALCULADORA GRÁTIS</div><h2>Sua bitola, classe<br>ou lubrificação<br>não está aqui?</h2>"
          "<div class=formula>T = K × F × d</div>"
          "<div class=sub>Calcule torque e pré-carga de M3 a M48, classes 4.6 a 12.9, roscas finas e 5 condições de rosca.</div>"
          "<div class=card style='margin-top:80px;padding:50px;font-size:52px;font-weight:800;text-align:center;line-height:1.5'>🔗 Link na bio<br>"
          "<span style='font-size:40px;color:#f9a24b;font-weight:700'>ferramentasdoengenheiro.com</span></div>"
          + foot(5).replace("5/5 →", "5/5"))


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width": 1080, "height": 1350})
        for i, h in enumerate([s1, s2, s3, s4, s5], 1):
            await pg.set_content(h)
            await pg.wait_for_timeout(300)
            await pg.screenshot(path=f"{OUT}/{i}.jpg", type="jpeg", quality=92)
        await b.close()

asyncio.run(main())
for b_ in B:
    print(b_, [br(torque(b_, c)) for c in SP])
