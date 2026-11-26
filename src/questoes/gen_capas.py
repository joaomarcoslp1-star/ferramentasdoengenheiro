import json, asyncio
from playwright.async_api import async_playwright
from PIL import Image
meta = json.load(open('/home/claude/site_src/posts/materias.json'))
card = open('/home/claude/capa-simulado.svg').read()
g0 = card.index('<g transform="translate(790,95) rotate(4)">'); g1 = card.index('<g font-family="Arial, Helvetica, sans-serif" fill="#ffffff">')
cartao = card[g0:g1]
def svg(m):
    t1, t2 = m["cover"]
    words = t1.split(); lines=[t1]
    if len(t1) > 15:
        best=None
        for i in range(1,len(words)):
            a,b=" ".join(words[:i])," ".join(words[i:]); w=max(len(a),len(b))
            if best is None or w<best[0]: best=(w,[a,b])
        lines=best[1]
    fs = min(64, int(660/(max(len(l) for l in lines)*0.72)))
    y = 228
    tl = ""
    for l in lines:
        y += fs + 10
        tl += f'<text x="80" y="{y}" font-size="{fs}" font-weight="800" fill="#f9a24b">{l}</text>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0f2742"/><stop offset="1" stop-color="#163d6b"/></linearGradient>
<pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#ffffff" stroke-opacity=".05"/></pattern></defs>
<rect width="1200" height="630" fill="url(#bg)"/><rect width="1200" height="630" fill="url(#grid)"/>
{cartao}
<g font-family="Arial, Helvetica, sans-serif" fill="#ffffff">
<rect x="80" y="100" width="300" height="44" rx="22" fill="#f28c28"/>
<text x="230" y="130" text-anchor="middle" font-size="20" font-weight="700" fill="#1c2430">QUESTÕES COMENTADAS</text>
<text x="80" y="228" font-size="58" font-weight="800">Questões de</text>
{tl}
<text x="80" y="{y+60}" font-size="28" fill="#c9d6e6">{t2} · estilo Cesgranrio</text>
<text x="80" y="{y+100}" font-size="28" fill="#c9d6e6">Petrobras e Transpetro</text>
<text x="80" y="560" font-size="22" fill="#c9d6e6" fill-opacity=".85">ferramentasdoengenheiro.com</text>
</g></svg>'''
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg = await b.new_page(viewport={'width':1200,'height':630})
        for m in meta:
            await pg.set_content('<html><body style="margin:0">'+svg(m)+'</body></html>')
            await pg.screenshot(path='/tmp/c.png')
            Image.open('/tmp/c.png').convert('RGB').save(f'/home/claude/site_src/img/{m["slug"]}.jpg', quality=84, optimize=True, progressive=True)
        await b.close()
asyncio.run(main()); print('ok')
