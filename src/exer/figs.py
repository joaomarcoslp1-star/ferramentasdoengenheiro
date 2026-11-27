# -*- coding: utf-8 -*-
"""Figuras SVG (fundo escuro) para os exercícios. Cada função devolve um <svg> 900 x 420."""
O = '#f28c28'; B = '#5b9bff'; W = '#ffffff'; G = '#9fb3c8'; S = '#c9d6e6'; Y = '#ffd166'

def _svg(body, h=420):
    return (f'<svg viewBox="0 0 900 {h}" width="900" height="{h}" xmlns="http://www.w3.org/2000/svg" '
            f'font-family="Arial,Helvetica,sans-serif"><defs><marker id="a" viewBox="0 0 10 10" refX="5" refY="5" '
            f'markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 1L9 5L0 9z" fill="{B}"/></marker>'
            f'<marker id="o" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
            f'<path d="M0 1L9 5L0 9z" fill="{O}"/></marker></defs>{body}</svg>')

def viga():
    x0, x1, y = 120, 780, 220; xp = x0 + (x1 - x0) * 2 / 6
    return _svg(f'''<rect x="{x0}" y="{y-12}" width="{x1-x0}" height="24" rx="4" fill="{G}"/>
<path d="M{x0} {y+12} l-26 44 h52 z" fill="none" stroke="{W}" stroke-width="4"/>
<path d="M{x1} {y+12} l-26 40 h52 z" fill="none" stroke="{W}" stroke-width="4"/><circle cx="{x1-14}" cy="{y+62}" r="8" fill="none" stroke="{W}" stroke-width="3"/><circle cx="{x1+14}" cy="{y+62}" r="8" fill="none" stroke="{W}" stroke-width="3"/>
<line x1="{xp}" y1="{y-130}" x2="{xp}" y2="{y-22}" stroke="{O}" stroke-width="7" marker-end="url(#o)"/>
<text x="{xp+16}" y="{y-110}" font-size="40" font-weight="700" fill="{O}">12 kN</text>
<text x="{x0}" y="{y+110}" text-anchor="middle" font-size="34" fill="{W}">A</text><text x="{x1}" y="{y+110}" text-anchor="middle" font-size="34" fill="{W}">B</text>
<line x1="{x0}" y1="{y+150}" x2="{xp}" y2="{y+150}" stroke="{B}" stroke-width="3" marker-start="url(#a)" marker-end="url(#a)"/><text x="{(x0+xp)/2}" y="{y+190}" text-anchor="middle" font-size="34" fill="{B}">2 m</text>
<line x1="{xp}" y1="{y+150}" x2="{x1}" y2="{y+150}" stroke="{B}" stroke-width="3" marker-start="url(#a)" marker-end="url(#a)"/><text x="{(xp+x1)/2}" y="{y+190}" text-anchor="middle" font-size="34" fill="{B}">4 m</text>''')

def secaoT():
    k = 2.6; cx = 450; yb = 380
    mesa = (cx - 60 * k, yb - 120 * k, 120 * k, 20 * k); alma = (cx - 10 * k, yb - 100 * k, 20 * k, 100 * k)
    return _svg(f'''<rect x="{mesa[0]}" y="{mesa[1]}" width="{mesa[2]}" height="{mesa[3]}" fill="{S}" stroke="{W}" stroke-width="2"/>
<rect x="{alma[0]}" y="{alma[1]}" width="{alma[2]}" height="{alma[3]}" fill="{S}" stroke="{W}" stroke-width="2"/>
<line x1="{mesa[0]}" y1="{mesa[1]-18}" x2="{mesa[0]+mesa[2]}" y2="{mesa[1]-18}" stroke="{B}" stroke-width="3" marker-start="url(#a)" marker-end="url(#a)"/>
<text x="{cx}" y="{mesa[1]-30}" text-anchor="middle" font-size="30" fill="{B}">120 mm</text>
<text x="{mesa[0]+mesa[2]+16}" y="{mesa[1]+40}" font-size="30" fill="{B}">20 mm</text>
<line x1="{cx+60*k+60}" y1="{yb}" x2="{cx+60*k+60}" y2="{yb-100*k}" stroke="{B}" stroke-width="3" marker-start="url(#a)" marker-end="url(#a)"/><text x="{cx+60*k+76}" y="{yb-130}" font-size="30" fill="{B}">100</text>
<text x="{cx}" y="{yb+34}" text-anchor="middle" font-size="30" fill="{B}">20 mm</text>
<line x1="{cx-60*k-40}" y1="{yb-82.7*k}" x2="{cx+60*k+40}" y2="{yb-82.7*k}" stroke="{O}" stroke-width="3" stroke-dasharray="10 8"/><text x="{cx-60*k-48}" y="{yb-82.7*k+10}" text-anchor="end" font-size="34" font-weight="700" fill="{O}">ȳ = ?</text>''', 440)

def perfil():
    def I(cx, d, bf, lab, sub):
        k = 1.25; h = d * k; b = bf * k; tf = 9; tw = 6; y0 = 360 - h
        return (f'<path d="M{cx-b/2} {y0} h{b} v{tf} h{-(b-tw)/2} v{h-2*tf} h{(b-tw)/2} v{tf} h{-b} v{-tf} h{(b-tw)/2} v{-(h-2*tf)} h{-(b-tw)/2} z" fill="{S}" stroke="{W}" stroke-width="2"/>'
                f'<text x="{cx}" y="400" text-anchor="middle" font-size="34" font-weight="700" fill="{W}">{lab}</text><text x="{cx}" y="{y0-16}" text-anchor="middle" font-size="28" fill="{B}">{sub}</text>')
    return _svg(I(280, 148, 100, 'W 150 × 13', 'Wx = 85,8 cm³') + I(620, 200, 100, 'W 200 × 15', 'Wx = 130,5 cm³'), 420)

def pilar():
    return _svg(f'''<rect x="420" y="40" width="60" height="320" fill="{G}" stroke="{W}" stroke-width="2"/>
<line x1="450" y1="-10" x2="450" y2="34" stroke="{O}" stroke-width="7" marker-end="url(#o)"/><text x="480" y="30" font-size="36" font-weight="700" fill="{O}">P</text>
<circle cx="450" cy="40" r="9" fill="{W}"/><circle cx="450" cy="360" r="9" fill="{W}"/><path d="M450 360 l-26 40 h52 z" fill="none" stroke="{W}" stroke-width="4"/>
<line x1="560" y1="40" x2="560" y2="360" stroke="{B}" stroke-width="3" marker-start="url(#a)" marker-end="url(#a)"/><text x="580" y="210" font-size="36" fill="{B}">L = 4 m</text>
<circle cx="250" cy="200" r="80" fill="{S}" stroke="{W}" stroke-width="2"/><circle cx="250" cy="200" r="70" fill="#0f2742" stroke="{W}" stroke-width="2"/><text x="250" y="320" text-anchor="middle" font-size="30" fill="{W}">tubo 4" Sch 40</text>
<path d="M360 200 L410 200" stroke="{W}" stroke-width="2" stroke-dasharray="6 6"/>''')

def parafuso():
    return _svg(f'''<rect x="250" y="150" width="400" height="60" fill="{G}" stroke="{W}" stroke-width="2"/><rect x="250" y="212" width="400" height="60" fill="{G}" stroke="{W}" stroke-width="2"/>
<rect x="420" y="100" width="60" height="220" fill="{S}" stroke="{W}" stroke-width="2"/><rect x="385" y="80" width="130" height="36" rx="4" fill="{S}" stroke="{W}" stroke-width="2"/><rect x="385" y="290" width="130" height="36" rx="4" fill="{S}" stroke="{W}" stroke-width="2"/>
<line x1="450" y1="74" x2="450" y2="22" stroke="{O}" stroke-width="6" marker-end="url(#o)"/><line x1="450" y1="332" x2="450" y2="384" stroke="{O}" stroke-width="6" marker-end="url(#o)"/>
<text x="470" y="44" font-size="34" font-weight="700" fill="{O}">Fᵢ</text>
<path d="M545 300 A100 26 0 1 1 556 292" fill="none" stroke="{Y}" stroke-width="5"/><text x="680" y="330" font-size="36" font-weight="700" fill="{Y}">T</text>
<text x="450" y="415" text-anchor="middle" font-size="30" fill="{B}">M16 · classe 8.8</text>''', 430)

def vaso():
    return _svg(f'''<path d="M230 130 H640 A70 80 0 0 1 640 290 H230 A70 80 0 0 1 230 130 Z" fill="{S}" stroke="{W}" stroke-width="3"/>
<text x="435" y="222" text-anchor="middle" font-size="40" font-weight="700" fill="#0f2742">AR COMPRIMIDO</text>
<line x1="330" y1="130" x2="330" y2="100" stroke="{W}" stroke-width="5"/><circle cx="330" cy="76" r="26" fill="#0f2742" stroke="{W}" stroke-width="4"/><line x1="330" y1="76" x2="346" y2="62" stroke="{O}" stroke-width="4"/>
<text x="370" y="72" font-size="36" font-weight="700" fill="{O}">P = 1,2 MPa</text>
<text x="435" y="360" text-anchor="middle" font-size="36" font-weight="700" fill="{B}">V = 0,5 m³</text>''')

def retangulos():
    return _svg(f'''<rect x="120" y="230" width="280" height="140" fill="{S}" stroke="{W}" stroke-width="2"/><text x="260" y="410" text-anchor="middle" font-size="32" fill="{W}">deitada</text>
<text x="260" y="220" text-anchor="middle" font-size="30" fill="{B}">2b</text><text x="410" y="310" font-size="30" fill="{B}">b</text>
<rect x="590" y="90" width="140" height="280" fill="{S}" stroke="{W}" stroke-width="2"/><text x="660" y="410" text-anchor="middle" font-size="32" fill="{W}">em pé</text>
<text x="660" y="80" text-anchor="middle" font-size="30" fill="{B}">b</text><text x="740" y="240" font-size="30" fill="{B}">2b</text>
<path d="M440 300 Q500 220 560 260" fill="none" stroke="{O}" stroke-width="5" marker-end="url(#o)"/><text x="500" y="200" text-anchor="middle" font-size="40" font-weight="800" fill="{O}">× ?</text>''', 430)

def tubo():
    return _svg(f'''<rect x="80" y="170" width="740" height="80" rx="6" fill="{G}"/><rect x="80" y="182" width="740" height="56" fill="#7fb2e5" opacity=".7"/>
<line x1="140" y1="210" x2="300" y2="210" stroke="#0f2742" stroke-width="6" marker-end="url(#a)"/><text x="220" y="150" text-anchor="middle" font-size="38" font-weight="700" fill="{W}">Q → 2Q</text>
<text x="620" y="150" text-anchor="middle" font-size="38" font-weight="700" fill="{O}">h<tspan baseline-shift="sub" font-size="26">f</tspan> → ?</text>
<text x="450" y="320" text-anchor="middle" font-size="32" fill="{B}">mesmo D, mesmo L, mesmo material</text>''')

def cabo():
    return _svg(f'''<circle cx="270" cy="200" r="70" fill="#b87333" stroke="#7a4a1e" stroke-width="4"/><circle cx="270" cy="200" r="44" fill="#d9925a"/>
<text x="270" y="320" text-anchor="middle" font-size="36" font-weight="700" fill="{W}">2,5 mm²</text><text x="270" y="364" text-anchor="middle" font-size="32" fill="#ff8a7a">ΔV = 5%</text>
<path d="M380 200 L500 200" stroke="{O}" stroke-width="6" marker-end="url(#o)"/>
<circle cx="640" cy="200" r="90" fill="#b87333" stroke="#7a4a1e" stroke-width="4"/><circle cx="640" cy="200" r="58" fill="#d9925a"/>
<text x="640" y="330" text-anchor="middle" font-size="36" font-weight="700" fill="{W}">4 mm²</text><text x="640" y="374" text-anchor="middle" font-size="32" fill="{Y}">ΔV = ?</text>''')

FIGS = dict(viga=viga, secaoT=secaoT, perfil=perfil, pilar=pilar, parafuso=parafuso, vaso=vaso, retangulos=retangulos, tubo=tubo, cabo=cabo)
