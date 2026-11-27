# -*- coding: utf-8 -*-
"""English section (/en/) of the site. Called from build_site.build()."""
import json, html, os

D = os.path.dirname(os.path.abspath(__file__))
WRAP = '<div style="font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.65;color:#1c2430;max-width:860px;margin:0 auto">'
BOX = 'style="background:#f6f8fb;border-left:4px solid #1f6feb;padding:12px 16px;border-radius:6px"'
TH = 'style="padding:8px;border-bottom:2px solid #dde3ec;text-align:left;background:#f6f8fb"'
TD = 'style="padding:7px 8px;border-bottom:1px solid #eef1f5"'


def table(head, rows):
    return ('<div style="overflow-x:auto"><table style="border-collapse:collapse;width:100%;font-size:.92rem;margin:8px 0 16px"><thead><tr>'
            + ''.join(f'<th {TH}>{h}</th>' for h in head) + '</tr></thead><tbody>'
            + ''.join('<tr>' + ''.join(f'<td {TD}>{c}</td>' for c in r) + '</tr>' for r in rows) + '</tbody></table></div>')


def F(s):
    return f'<p {BOX}>{s}</p>'


TOOLS = open(f'{D}/beam_tool.html').read(), open(f'{D}/inertia_tool.html').read(), open(f'{D}/torque_tool.html').read()

PAGES = [
 dict(slug="en/calculators/beam-calculator", img="en-beam.jpg", tool=0, tag="Structural analysis",
      title="Beam Calculator: Reactions, Shear and Bending Moment Diagrams",
      short="Beam calculator", card="Reactions, shear and moment diagrams for simply supported and cantilever beams, step by step.",
      desc="Free beam calculator: support reactions, shear force and bending moment diagrams for simply supported and cantilever beams with point, distributed and moment loads. US (kip, ft) and SI units.",
      top="""<p>Draw the shear force and bending moment diagrams of any statically determinate beam in seconds. Pick the supports, add point loads, uniform or triangular distributed loads and applied moments, and the calculator returns the <b>support reactions</b>, the <b>maximum shear</b>, the <b>maximum bending moment</b> and where it happens, with every equilibrium step written out so you can check it.</p>
<p>It works in <b>US customary units</b> (kip, ft, kip·ft) or <b>SI units</b> (kN, m, kN·m). Switching units converts the numbers you already typed.</p>
<h2>Beam calculator</h2>
""",
      bottom=lambda: f"""
<h2>How to solve a statically determinate beam</h2>
<p>A simply supported beam (pin + roller) or a cantilever (one fixed end) has exactly three unknown support reactions, so the three equilibrium equations are enough to find them:</p>
{F("<b>1. Replace distributed loads by their resultants.</b> A uniform load w over a length a becomes a force w·a at the middle of that length. A triangular load becomes w·a/2 at one third of the length from the larger end.")}
{F("<b>2. Sum of moments about one support = 0.</b> This gives the reaction at the other support directly, with no simultaneous equations.")}
{F("<b>3. Sum of vertical forces = 0.</b> This gives the remaining reaction. For a cantilever, use ΣF = 0 for the vertical reaction and ΣM = 0 at the wall for the fixed-end moment.")}
{F("<b>4. Walk along the beam.</b> Shear V(x) is the sum of forces to the left of the section; bending moment M(x) is the sum of their moments about the section. The moment peaks where the shear crosses zero.")}

<h2>Worked example</h2>
<p>The default example: a 20 ft simply supported beam with a 5 kip point load at 6 ft and a uniform load of 0.4 kip/ft over the full span.</p>
<p><b>Resultant of the distributed load:</b> 0.4 × 20 = 8 kip at x = 10 ft.<br>
<b>Moments about A:</b> R<sub>B</sub> × 20 = 5 × 6 + 8 × 10 = 110 → <b>R<sub>B</sub> = 5.5 kip</b>.<br>
<b>Vertical forces:</b> R<sub>A</sub> = 5 + 8 − 5.5 → <b>R<sub>A</sub> = 7.5 kip</b>.<br>
<b>Maximum moment:</b> the shear drops from 7.5 kip to 7.5 − 0.4 × 6 = 5.1 kip just left of the point load and to 0.1 kip just right of it, then reaches zero 0.25 ft further, at x = 6.25 ft. M<sub>max</sub> = 7.5 × 6.25 − 0.4 × 6.25²/2 − 5 × 0.25 ≈ <b>37.8 kip·ft</b>.</p>

<h2>Common beam formulas</h2>
{table(["Case (span L)", "Reactions", "Maximum moment", "Maximum deflection"], [
 ["Simply supported, uniform load w", "wL/2 each", "wL²/8 at midspan", "5wL⁴/(384EI)"],
 ["Simply supported, point load P at midspan", "P/2 each", "PL/4 at midspan", "PL³/(48EI)"],
 ["Simply supported, point load P at a from A (b = L − a)", "R<sub>A</sub> = Pb/L, R<sub>B</sub> = Pa/L", "Pab/L under the load", "depends on a"],
 ["Cantilever, uniform load w", "R = wL, M = wL²/2", "wL²/2 at the wall", "wL⁴/(8EI)"],
 ["Cantilever, point load P at the free end", "R = P, M = PL", "PL at the wall", "PL³/(3EI)"]])}
<p>These are the same cases tabulated in the AISC Steel Construction Manual (Part 3, beam diagrams and formulas). The calculator handles any combination of them by superposition.</p>

<h2>From bending moment to beam size</h2>
<p>Once you know M<sub>max</sub>, the required section modulus is S = M / F<sub>b</sub>. Find S for any shape with the <a href="/en/calculators/moment-of-inertia-calculator/">moment of inertia calculator</a>, then check the bending stress: f<sub>b</sub> = M / S. Remember that serviceability (deflection, often limited to L/360 under live load) frequently controls before strength does.</p>

<h2>FAQ</h2>
<h3>Why does the moment diagram look upside down?</h3>
<p>The diagram is drawn on the tension side, the usual convention in structural engineering: positive (sagging) moment is plotted below the axis, where the bottom fiber is in tension.</p>
<h3>Can it solve continuous beams or fixed–fixed beams?</h3>
<p>Not yet. Those are statically indeterminate and need compatibility equations (or a matrix method). This tool covers simply supported beams, beams with overhangs and cantilevers.</p>
<h3>Does it include the beam self-weight?</h3>
<p>Only if you add it. Enter the weight per foot of the member as a uniform load over the full span.</p>
"""),
 dict(slug="en/calculators/moment-of-inertia-calculator", img="en-inertia.jpg", tool=1, tag="Section properties",
      title="Moment of Inertia Calculator: Centroid, Section Modulus and Radius of Gyration",
      short="Moment of inertia calculator", card="Centroid, Ix, Iy, S and r for I, T, L, C, tubes and built-up sections.",
      desc="Free moment of inertia calculator for rectangles, circles, pipes, HSS, I-beams, T sections, angles, channels and built-up sections. Centroid, Ix, Iy, section modulus and radius of gyration, step by step.",
      top="""<p>Try to bend a ruler lying flat: easy. Now try to bend it standing on its edge: almost impossible. Same material, same area. What changes is the <b>moment of inertia</b>, the property that measures how far the area sits from the bending axis. The farther the material from the center, the stiffer the member. That is why beams are shaped like an I.</p>
<p>This calculator finds the <b>centroid</b>, the <b>moments of inertia</b> I<sub>x</sub> and I<sub>y</sub>, the <b>section moduli</b> and the <b>radii of gyration</b> of rectangles, solid circles, pipes, rectangular tubes, I shapes, T sections, angles, channels, or any section built from rectangles, showing the calculation part by part.</p>
<h2>Moment of inertia and centroid calculator</h2>
""",
      bottom=lambda: f"""
<h2>Step by step: centroid and the parallel axis theorem</h2>
<p>For built-up sections (T, I, L, C or any combination of rectangles), the calculation takes three steps:</p>
{F("<b>1. Split the section into simple parts</b> (rectangles, circles) and write down each area A<sub>i</sub> and the position of its centroid (x<sub>i</sub>, y<sub>i</sub>). Holes enter with a negative area.")}
{F("<b>2. Locate the centroid:</b> ȳ = Σ(A<sub>i</sub> · y<sub>i</sub>) / ΣA<sub>i</sub> and x̄ = Σ(A<sub>i</sub> · x<sub>i</sub>) / ΣA<sub>i</sub>")}
{F("<b>3. Move each part's inertia to the centroidal axis (parallel axis theorem):</b> I<sub>x</sub> = Σ (I<sub>x,own</sub> + A<sub>i</sub> · d<sub>i</sub>²), where d<sub>i</sub> = y<sub>i</sub> − ȳ")}
<p>The A·d² term is always positive and is usually the largest one: it is the reason why moving material away from the center increases the inertia so much.</p>

<h2>Worked example: T section</h2>
<p>A T section with a 6 × 0.75 in flange and a 0.5 in stem, 8 in overall depth (the example loaded in the calculator).</p>
<p><b>Parts:</b> stem 0.5 × 7.25 in → A = 3.625 in², y = 3.625 in; flange 6 × 0.75 in → A = 4.5 in², y = 7.625 in.<br>
<b>Centroid:</b> ȳ = (3.625 × 3.625 + 4.5 × 7.625) / 8.125 = <b>5.84 in</b> from the bottom.<br>
<b>Stem:</b> I = 0.5 × 7.25³/12 = 15.88 in⁴; d = 3.625 − 5.84 = −2.215 in; A·d² = 17.79 in⁴.<br>
<b>Flange:</b> I = 6 × 0.75³/12 = 0.21 in⁴; d = 1.785 in; A·d² = 14.34 in⁴.<br>
<b>I<sub>x</sub></b> = 15.88 + 17.79 + 0.21 + 14.34 ≈ <b>48.2 in⁴</b>.</p>

<h2>Formulas for basic shapes</h2>
<p>Moment of inertia about the centroidal axis:</p>
{table(["Shape", "I<sub>x</sub> (horizontal axis)", "I<sub>y</sub> (vertical axis)", "Centroid"], [
 ["Rectangle b × h", "b·h³/12", "h·b³/12", "at the center"],
 ["Solid circle, diameter D", "π·D⁴/64", "π·D⁴/64", "at the center"],
 ["Pipe, outside D and inside d", "π·(D⁴ − d⁴)/64", "π·(D⁴ − d⁴)/64", "at the center"],
 ["Triangle, base b and height h", "b·h³/36", "h·b³/48 (isosceles)", "h/3 from the base"],
 ["Semicircle, radius r", "0.1098·r⁴", "π·r⁴/8", "4r/(3π) from the base"]])}

<h2>Section modulus and radius of gyration</h2>
<ul>
<li><b>Elastic section modulus S = I / c</b>, where c is the distance from the centroid to the extreme fiber. It gives the bending stress: <b>f<sub>b</sub> = M / S</b>. Get M from the <a href="/en/calculators/beam-calculator/">beam calculator</a> and S from this page to check a member.</li>
<li><b>Radius of gyration r = √(I / A)</b> governs column buckling through the slenderness ratio KL/r. A column buckles about the axis with the smaller r.</li>
</ul>
<p>Note: AISC uses <b>S</b> for the elastic section modulus and <b>Z</b> for the plastic modulus. European tables call the elastic modulus W (W<sub>el</sub>).</p>

<h2>FAQ</h2>
<h3>Why is a ruler on edge so much stiffer?</h3>
<p>For a 1.2 × 0.12 in ruler, I flat = 1.2 × 0.12³/12 ≈ 0.00017 in⁴. On edge, I = 0.12 × 1.2³/12 ≈ 0.0173 in⁴: <b>100 times larger</b> with the same area, because the height enters cubed.</p>
<h3>What is the difference between moment of inertia and section modulus?</h3>
<p>The moment of inertia (in⁴) controls <b>stiffness</b>, that is, deflection. The section modulus (in³) controls <b>strength</b>, the maximum bending stress. A beam can pass on stress and still fail on deflection.</p>
<h3>What are the product of inertia and the principal axes?</h3>
<p>For sections without an axis of symmetry, such as an angle, the product of inertia I<sub>xy</sub> is not zero and the axes of maximum and minimum inertia are rotated. The calculator shows the principal moments I<sub>1</sub>, I<sub>2</sub> and the angle θ. Single angles buckle about the minor principal axis.</p>
<h3>Why don't my results match the AISC table exactly?</h3>
<p>Rolled shapes have fillets between the web and the flanges that this calculator ignores, and AISC tabulates design dimensions. Differences are small; for design, use the published values.</p>
"""),
 dict(slug="en/calculators/bolt-torque-calculator", img="en-torque.jpg", tool=2, tag="Machine design",
      title="Bolt Torque Calculator: Tightening Torque and Preload (SAE and Metric)",
      short="Bolt torque calculator", card="Tightening torque and clamp force for SAE Grade 2, 5, 8 and metric bolts.",
      desc="Free bolt torque calculator: tightening torque and preload for UNC/UNF bolts in SAE J429 Grade 2, 5 and 8 and metric bolts in ISO 898-1 classes, with nut factor K for dry, plated and lubricated threads.",
      top="""<p>How tight should that bolt be? This calculator gives the <b>tightening torque</b> and the <b>preload</b> (clamp force) for inch bolts (UNC and UNF threads, <b>SAE J429 Grade 2, 5 and 8</b>) and metric bolts (<b>ISO 898-1</b> classes 4.6 to 12.9), taking into account the thread condition through the nut factor K.</p>
<p>It also builds a full torque table for every size, using the grade and lubrication you picked.</p>
<h2>Bolt torque calculator</h2>
""",
      bottom=lambda: f"""
<h2>How tightening torque is calculated</h2>
<p>The short-form torque equation used across industry is:</p>
{F("<b>T = K × F × D</b> &nbsp;where T is the torque, K the nut factor (dimensionless), F the target preload and D the nominal diameter. With F in lbf and D in inches, divide by 12 to get lbf·ft.")}
<p>The target preload is a percentage of the bolt's <b>proof load</b>, the largest load it can carry without permanent stretch:</p>
{F("<b>Proof load = A<sub>s</sub> × S<sub>p</sub></b> &nbsp;where A<sub>s</sub> is the tensile stress area and S<sub>p</sub> the proof strength of the grade. For inch threads, A<sub>s</sub> = 0.7854 × (D − 0.9743/n)², with n threads per inch.")}
<p>A common practice is 75% of proof load for joints that will be taken apart and 90% for permanent joints.</p>

<h2>Worked example: 1/2"-13 UNC, Grade 5, zinc plated</h2>
<p><b>Stress area:</b> A<sub>s</sub> = 0.7854 × (0.5 − 0.9743/13)² = 0.1419 in².<br>
<b>Proof load:</b> 0.1419 × 85,000 psi = 12,060 lbf.<br>
<b>Preload (75%):</b> 0.75 × 12,060 ≈ 9,050 lbf.<br>
<b>Torque:</b> T = 0.20 × 9,050 × 0.5 / 12 ≈ <b>75 lbf·ft</b>.</p>

<h2>SAE J429 proof strength</h2>
{table(["Grade", "Diameter", "Proof strength", "Min. tensile strength", "Head marking"], [
 ["Grade 2", "1/4\" to 3/4\"", "55 ksi", "74 ksi", "none"],
 ["Grade 2", "over 3/4\" to 1-1/2\"", "33 ksi", "60 ksi", "none"],
 ["Grade 5", "1/4\" to 1\"", "85 ksi", "120 ksi", "3 radial lines"],
 ["Grade 5", "over 1\" to 1-1/2\"", "74 ksi", "105 ksi", "3 radial lines"],
 ["Grade 8", "1/4\" to 1-1/2\"", "120 ksi", "150 ksi", "6 radial lines"]])}

<h2>Nut factor K by thread condition</h2>
{table(["Condition", "Typical K"], [
 ["Plain steel (black oxide), dry", "0.30"], ["Zinc plated", "0.20"], ["Oil lubricated", "0.18"],
 ["Cadmium plated", "0.16"], ["Anti-seize paste (MoS₂)", "0.12"]])}
<p>K lumps together thread and under-head friction. It is the biggest source of uncertainty: the same torque on a lubricated bolt produces much more preload than on a dry one. Using a dry-thread torque on a lubricated bolt is a classic way to stretch or snap it.</p>

<h2>FAQ</h2>
<h3>Why is the expected preload a range?</h3>
<p>Friction varies from bolt to bolt, so torque control alone gives about ±25% scatter in preload. When preload really matters, use direct tension indicators, turn-of-nut, or measure bolt stretch.</p>
<h3>Should I torque structural bolts (A325 / F3125) with this?</h3>
<p>Structural steel connections follow the RCSC Specification, which prefers turn-of-nut or calibrated wrench methods and does not accept a generic torque table. Use this calculator for machinery and general bolting.</p>
<h3>How do I convert lbf·ft to N·m?</h3>
<p>Multiply by 1.3558. The calculator shows both, plus lbf·in for small fasteners.</p>
"""),
]


COVER = """<html><head><meta charset=utf-8><style>body{{margin:0;width:1200px;height:630px;background:#0f2742;font-family:Arial,Helvetica,sans-serif;color:#fff;position:relative;overflow:hidden}}
.g{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:40px 40px}}
.l{{position:absolute;left:60px;top:70px;width:600px}}.bd{{display:inline-block;background:#f28c28;color:#1c2430;font-weight:700;font-size:24px;padding:10px 22px;border-radius:30px}}
h1{{font-size:58px;line-height:1.08;margin:30px 0 0}}.m{{font-size:26px;color:#c9d6e6;margin-top:24px}}.f{{position:absolute;right:40px;top:0;bottom:0;width:480px;display:flex;align-items:center}}.f svg{{width:100%;height:auto}}
.s{{position:absolute;left:60px;bottom:44px;font-size:22px;color:#c9d6e6}}</style></head><body><div class=g></div><div class=l><span class=bd>FREE CALCULATOR</span><h1>{t}</h1><div class=m>{m}</div></div>
<div class=f>{fig}</div><div class=s>ferramentasdoengenheiro.com/en</div></body></html>"""


def covers(SRC):
    import asyncio, sys
    sys.path.insert(0, f'{SRC}/exer')
    from figs import FIGS
    def sub(svg, pairs):
        for a, b in pairs: svg = svg.replace('>' + a + '<', '>' + b + '<', 1)
        return svg
    items = [("en-beam.jpg", "Beam calculator", "Reactions · shear · bending moment", sub(FIGS['viga'](), [("12 kN", "5 kip"), ("2 m", "6 ft"), ("4 m", "14 ft")])),
             ("en-inertia.jpg", "Moment of inertia", "Centroid · I · S · r for any section", sub(FIGS['secaoT'](), [("120 mm", "6 in"), ("20 mm", "0.75 in"), ("100", "7.25"), ("20 mm", "0.5 in")])),
             ("en-torque.jpg", "Bolt torque", "SAE Grade 2, 5, 8 and metric", sub(FIGS['parafuso'](), [("M16 · classe 8.8", '1/2"-13 · Grade 5')]))]
    async def go():
        from playwright.async_api import async_playwright
        async with async_playwright() as p:
            b = await p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg = await b.new_page(viewport={"width": 1200, "height": 630})
            for f, t, m, fig in items:
                await pg.set_content(COVER.format(t=t, m=m, fig=fig)); await pg.screenshot(path=f"{SRC}/img/{f}", type='jpeg', quality=85)
            await b.close()
    asyncio.run(go())


def build_en(B):
    """B: the build_site module (layout, write, DOMAIN, SITE_EN...). Returns [(path, date)]."""
    urls = []
    if not all(os.path.exists(f"{B.SRC}/img/{p['img']}") for p in PAGES):
        covers(B.SRC)
        import shutil
        for p in PAGES: shutil.copy(f"{B.SRC}/img/{p['img']}", f"{B.OUT}/img/{p['img']}")
    date = "2026-11-27"

    def card(p):
        return (f'<a class="card" href="/{p["slug"]}/"><img src="/img/{p["img"]}" alt="" width="1200" height="630" loading="lazy">'
                f'<div><small>{p["tag"]}</small><b>{p["short"]}</b><p>{p["card"]}</p></div></a>')

    for p in PAGES:
        path = f'/{p["slug"]}/'
        rel = [x for x in PAGES if x is not p]
        body_post = WRAP + p["top"] + TOOLS[p["tool"]] + p["bottom"]() + \
            '<p style="font-size:.85rem;color:#5a6575;border-top:1px solid #dde3ec;padding-top:12px;margin-top:28px">For study and preliminary design. Results should be checked by a licensed engineer before use in construction or manufacturing.</p></div>'
        body = (f'<div class="wrap"><nav class="crumb" aria-label="Breadcrumb"><a href="/en/">Home</a> › <a href="/en/calculators/">Calculators</a></nav>'
                f'<article><h1>{p["title"]}</h1><div class="meta">Updated {date} · {p["tag"]}</div>'
                f'<img class="cover" src="/img/{p["img"]}" alt="{html.escape(p["title"])}" width="1200" height="630" fetchpriority="high">'
                f'{body_post}</article>'
                f'<section class="rel"><h2 class="sec-t">More calculators</h2><div class="grid">{"".join(card(x) for x in rel)}</div></section></div>')
        ld = [{"@context": "https://schema.org", "@type": "WebApplication", "name": p["short"], "url": B.DOMAIN + path, "description": p["desc"],
               "applicationCategory": "EngineeringApplication", "operatingSystem": "Any", "inLanguage": "en",
               "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}},
              {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                  {"@type": "ListItem", "position": 1, "name": "Home", "item": B.DOMAIN + "/en/"},
                  {"@type": "ListItem", "position": 2, "name": "Calculators", "item": B.DOMAIN + "/en/calculators/"},
                  {"@type": "ListItem", "position": 3, "name": p["short"], "item": B.DOMAIN + path}]}]
        B.write(path, B.layout(path=path, title=p["title"], desc=p["desc"], body=body, img=p["img"], active="/en/calculators/", jsonld=ld, lang="en",
                               page_title=f'{p["title"].split(":")[0]} (Free, Step by Step) | {B.SITE_EN}'))
        urls.append((path, date))

    intro = "Free engineering calculators that run in your browser, on desktop or phone, with no sign-up. Each one shows the formula, the reference standard and a worked example, in US customary or SI units."
    body = (f'<div class="wrap"><nav class="crumb"><a href="/en/">Home</a></nav><h1>Engineering calculators</h1><p>{intro}</p>'
            f'<div class="grid">{"".join(card(x) for x in PAGES)}</div>'
            '<p class="note">More calculators are on the way. The Portuguese version of the site has more tools, including pipe friction loss, voltage drop and steel shape tables.</p></div>')
    B.write("/en/calculators/", B.layout(path="/en/calculators/", title="Engineering calculators", desc=intro, body=body, active="/en/calculators/", lang="en"))
    urls.append(("/en/calculators/", B.TODAY))

    home = f"""<section class="hero"><div class="wrap"><span class="pill">FREE · NO SIGN-UP</span>
<h1>Engineering calculators that <span>show their work</span></h1>
<p>Beam diagrams, section properties and bolt torque, solved in your browser with every step written out, in US customary or SI units.</p>
<a class="btn" href="/en/calculators/">See the calculators</a></div></section>
<div class="wrap"><h2 class="sec-t">Calculators</h2><div class="grid">{"".join(card(x) for x in PAGES)}</div>
<h2 class="sec-t">Why use them</h2>
<p class="note"><b>Open formulas, cited standards.</b> Every tool shows the method, the units and a worked example so you can check the result by hand. What you type stays in your browser.</p></div>"""
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": B.SITE_EN, "url": B.DOMAIN + "/en/", "inLanguage": "en"}]
    B.write("/en/", B.layout(path="/en/", title=B.SITE_EN, page_title=f"{B.SITE_EN}: free engineering calculators with step-by-step solutions",
                             desc="Free engineering calculators: beam shear and bending moment diagrams, moment of inertia and section properties, bolt tightening torque. Step by step, US and SI units.",
                             body=home, active="/en/", jsonld=ld, lang="en"))
    urls.append(("/en/", B.TODAY))

    about = f"""<div style="max-width:860px;margin:0 auto"><p>{B.SITE_EN} is the English edition of <a href="/">Ferramentas do Engenheiro</a>, a Brazilian site of free engineering calculators and exam practice for engineers, technicians and students.</p>
<p>Every calculator is written to be checked: it shows the formula, the units, the reference standard and the intermediate steps. Results are tested against hand calculations and published tables before going live.</p>
<h2>Corrections and suggestions</h2><p>Found an error or want a new calculator? Send a direct message to <a href="{B.IG}" target="_blank" rel="noopener">@ferramentasdoengenheiro</a> on Instagram with the page link, the values you entered and the result you expected.</p>
<p style="font-size:.9rem;color:#5a6575">The tools support study, estimating and preliminary design. They do not replace the work and responsibility of a licensed professional engineer.</p></div>"""
    priv = """<div style="max-width:860px;margin:0 auto"><p>This page explains how this site handles data. The Portuguese version of this policy (<a href="/privacidade/">Política de Privacidade</a>) has the same content and also covers Brazil's LGPD.</p>
<h2>Calculator inputs</h2><p>The values you type into the calculators are processed only in your browser. They are not sent to us.</p>
<h2>Analytics</h2><p>We use Google Analytics to count visits and understand which pages are useful. It collects technical data such as pages viewed, approximate location, device and browser, through cookies.</p>
<h2>Advertising</h2><p>This site may show ads served by Google AdSense. Google and its partners use cookies to serve ads based on your visits to this and other websites. You can opt out of personalized advertising in <a href="https://adssettings.google.com" target="_blank" rel="noopener">Google Ads Settings</a>. Learn more about how Google uses data at <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener">policies.google.com/technologies/partner-sites</a>.</p>
<h2>Contact</h2><p>Questions about this policy: send a direct message to @ferramentasdoengenheiro on Instagram.</p></div>"""
    for path, h, d, b in [("/en/about/", "About Engineer's Tools", "Who we are and how the calculators are built and checked.", about),
                          ("/en/privacy/", "Privacy Policy", "How Engineer's Tools handles data, cookies and advertising.", priv)]:
        B.write(path, B.layout(path=path, title=h, desc=d, body=f'<div class="wrap"><nav class="crumb"><a href="/en/">Home</a></nav><h1>{h}</h1>{b}</div>', active=path, lang="en"))
        urls.append((path, B.TODAY))
    return urls
