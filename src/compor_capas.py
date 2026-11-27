# Compõe capas 1200x630: ilustração IA ao fundo + título/subtítulo nítidos por cima
import asyncio, base64, sys
from playwright.async_api import async_playwright
from PIL import Image
IA = "/home/claude/ferramentasdoengenheiro/src/img-ia"
OUT = "/home/claude/site_src/img"
CAPAS = {
 "area-de-pintura": ("CALCULADORA GRÁTIS", ["Área de pintura", "e <em>litros de tinta</em>"], "Perfis, tubos e chapas · por m² ou por kg"),
 "queda-de-tensao": ("CALCULADORA GRÁTIS", ["Queda de tensão", "e <em>bitola</em> de cabo"], "Limites da NBR 5410 · mono e trifásico"),
 "peso-de-perfis": ("CALCULADORA GRÁTIS", ["Peso de perfis", "e <em>chapas</em> de aço"], "2.300+ bitolas · aço, inox e alumínio"),
 "perda-de-carga": ("CALCULADORA GRÁTIS", ["Perda de carga", "em <em>tubulações</em>"], "Hazen-Williams · conexões · bombas"),
 "torque-parafusos": ("CALCULADORA GRÁTIS", ["Torque de aperto", "de <em>parafusos</em>"], "Classes 4.6 a 12.9 · pré-carga · tabela"),
 "nr13-vasos": ("CALCULADORA NR-13", ["Categoria de", "<em>vaso de pressão</em>"], "Classe do fluido · P·V · prazos de inspeção"),
 "vigas": ("CALCULADORA GRÁTIS", ["Vigas: cortante e", "<em>momento fletor</em>"], "Reações · diagramas · passo a passo"),
 "inercia": ("CALCULADORA GRÁTIS", ["Momento de inércia", "e <em>centroide</em>"], "Perfis I, T, L, U · tubos · passo a passo"),
 "simulado-mecanica": ("SIMULADO GRÁTIS", ["70 questões de", "<em>Eng. Mecânica</em>"], "Estilo Cesgranrio · Petrobras e Transpetro"),
}
import json as _j
for _m in _j.load(open("/home/claude/site_src/posts/materias.json", encoding="utf-8")):
    CAPAS[_m["slug"]] = ("QUESTÕES COMENTADAS", ["Questões de", "<em>" + _m["mat"].replace("Materiais e Tratamentos Térmicos", "Materiais e Tratamentos") + "</em>"], f'{_m["n"]} questões · estilo Cesgranrio · Petrobras')
def html(src, badge, lines, sub):
    b64 = base64.b64encode(open(src, "rb").read()).decode()
    fs = "54px" if "QUESTÕES" in badge else "64px"
    t = "".join(f"<div class=t style='font-size:{fs}'>{l}</div>" for l in lines)
    return f"""<html><head><style>
body{{margin:0;width:1200px;height:630px;overflow:hidden;font-family:Arial,Helvetica,sans-serif}}
.bg{{position:absolute;inset:0;background:url(data:image/png;base64,{b64}) right center/cover no-repeat}}
.sh{{position:absolute;inset:0;background:linear-gradient(90deg,rgba(15,39,66,.97) 0%,rgba(15,39,66,.9) 38%,rgba(15,39,66,.35) 62%,rgba(15,39,66,0) 78%)}}
.tx{{position:absolute;left:80px;top:96px;width:620px;color:#fff}}
.bd{{display:inline-block;background:#f28c28;color:#1c2430;font-weight:700;font-size:20px;padding:11px 24px;border-radius:22px;margin-bottom:34px}}
.t{{font-size:64px;font-weight:800;line-height:1.12;text-shadow:0 2px 12px rgba(0,0,0,.35)}}
.t em{{font-style:normal;color:#f9a24b}}
.s{{font-size:27px;color:#c9d6e6;margin-top:26px}}
.u{{position:absolute;left:80px;bottom:56px;font-size:22px;color:#c9d6e6;opacity:.85}}
</style></head><body><div class=bg></div><div class=sh></div>
<div class=tx{" style='width:540px'" if "QUESTÕES" in badge else ""}><div class=bd>{badge}</div>{t}<div class=s>{sub}</div></div><div class=u>ferramentasdoengenheiro.com</div></body></html>"""
async def main(items):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width": 1200, "height": 630})
        for slug, (badge, lines, sub) in items:
            await pg.set_content(html(f"{IA}/capa-{slug}.png", badge, lines, sub)); await pg.wait_for_timeout(200)
            await pg.screenshot(path="/tmp/cap.png")
            Image.open("/tmp/cap.png").convert("RGB").save(f"{OUT}/{slug}.jpg", quality=84, optimize=True, progressive=True)
            print("ok", slug)
        await b.close()
if __name__ == "__main__":
    import os
    items = [(k, v) for k, v in CAPAS.items() if os.path.exists(f"{IA}/capa-{k}.png")]
    asyncio.run(main(items))
