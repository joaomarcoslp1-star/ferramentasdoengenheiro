# -*- coding: utf-8 -*-
"""Gera o site estático Ferramentas do Engenheiro em /home/claude/site."""
import os, re, json, shutil, html
from datetime import date

ROOT = "/home/claude"
OUT = f"{ROOT}/site"
SRC = f"{ROOT}/site_src"
DOMAIN = "https://ferramentasdoengenheiro.com"
SITE = "Ferramentas do Engenheiro"
IG = "https://www.instagram.com/ferramentasdoengenheiro/"
TODAY = date.today().isoformat()

LINKS = {
    "/2026/11/blog-post_26.html": "/calculadoras/perda-de-carga/",
    "/2026/11/blog-post.html": "/calculadoras/peso-de-perfis/",
    "/2026/11/calculadora-queda-de-tensao-nbr-5410.html": "/calculadoras/queda-de-tensao/",
    "/2026/11/calculadora-area-pintura-tinta.html": "/calculadoras/area-de-pintura/",
    "/p/contato.html": "/contato/",
    "/p/sobre.html": "/sobre/",
    "/p/politica-de-privacidade.html": "/privacidade/",
}

FIGS = {  # figuras cotadas inseridas nas páginas: (âncora, figura em site_src/figs, antes|depois)
    "calculadoras/torque-de-aperto-de-parafusos": [("<h2>Como calcular o torque de aperto</h2>", "torque", "depois")],
    "calculadoras/categoria-vaso-de-pressao-nr-13": [("<h2>Passo 1: o vaso entra na NR-13?</h2>", "nr13", "antes")],
    "calculadoras/vigas-cortante-e-momento-fletor": [("<h2>Como resolver uma viga isostática</h2>", "vigas", "depois")],
    "calculadoras/perda-de-carga": [("<h2>Como calcular a perda de carga</h2>", "perda", "depois")],
    "calculadoras/queda-de-tensao": [("<h2>Fórmula da queda de tensão</h2>", "queda", "depois")],
    "calculadoras/area-de-pintura": [("<h2>Como calcular a área de pintura de perfis metálicos</h2>", "pintura", "depois")],
}

AREAS = [
    ("Resistência dos materiais", ["Resistência dos materiais"]),
    ("Elementos de máquinas", ["Elementos de máquinas"]),
    ("Estruturas, caldeiraria e pintura", ["Estruturas metálicas", "Pintura industrial"]),
    ("Hidráulica", ["Hidráulica"]),
    ("Elétrica", ["Elétrica"]),
    ("Segurança e NRs", ["Segurança · NR-13"]),
]

PAGES = [
    dict(slug="calculadoras/area-de-pintura", kind="calc", src="post-calculadora-tinta-blogger.html", img="area-de-pintura.jpg",
         title="Calculadora de Área de Pintura e Consumo de Tinta (Perfis, Tubos e Chapas)", short="Área de pintura e litros de tinta",
         desc="Calcule grátis a área de pintura de perfis, tubos e chapas e os litros de tinta pelos sólidos por volume, espessura seca, demãos e perdas.",
         card="Área em m² de perfis, tubos e chapas e litros de tinta por demão, com perdas.", tag="Pintura industrial", date="2026-11-18"),
    dict(slug="calculadoras/queda-de-tensao", kind="calc", src="post-queda-tensao-blogger.html", img="queda-de-tensao.jpg",
         title="Calculadora de Queda de Tensão e Bitola de Cabo (NBR 5410)", short="Queda de tensão e bitola de cabo",
         desc="Calcule grátis a queda de tensão em circuitos mono e trifásicos e a bitola mínima do cabo pelos limites da NBR 5410.",
         card="Queda de tensão em V e % e seção mínima do cabo pelos limites da NBR 5410.", tag="Elétrica", date="2026-11-18"),
    dict(slug="calculadoras/peso-de-perfis", kind="calc", src="post-peso-perfis-blogger.html", img="peso-de-perfis.jpg",
         title="Calculadora de Peso de Perfis, Tubos e Chapas de Aço", short="Peso de perfis, tubos e chapas",
         desc="Calcule grátis o peso de perfis W, U, L, tubos e chapas de aço, inox e alumínio: 2.300+ bitolas, lista de peças, perda de compra e custo do material.",
         card="Lista de peças com 2.300+ bitolas, aço, inox e alumínio, perda de compra e custo.", tag="Estruturas metálicas", date="2026-11-18"),
    dict(slug="calculadoras/perda-de-carga", kind="calc", src="post-perda-carga-blogger.html", img="perda-de-carga.jpg",
         title="Calculadora de Perda de Carga em Tubulações (Hazen-Williams)", short="Perda de carga em tubulações",
         desc="Calcule grátis a perda de carga em tubulações por Hazen-Williams ou Fair-Whipple-Hsiao, com conexões, válvulas, velocidade e altura manométrica.",
         card="Hazen-Williams e Fair-Whipple-Hsiao, conexões e válvulas, altura manométrica.", tag="Hidráulica", date="2026-11-26"),
    dict(slug="calculadoras/tabela-de-perfis-e-tubos", kind="calc", src="site_src/posts/post-tabelas.html", img="tabelas.jpg",
         title="Tabela de Perfis W, HP, VS, IPE, HEA, HEB e Tubos Schedule (ASME B36.10)", short="Tabelas de perfis e tubos",
         desc="Consulte grátis as tabelas de perfis W e HP (Gerdau), vigas soldadas VS, IPE, HEA e HEB e de tubos ASME B36.10 por schedule: peso, área, Ix, Wx e raio de giração. Ache o perfil mais leve para o seu Wx.",
         card="W, HP, VS, IPE, HEA, HEB e tubos schedule, com busca e o perfil mais leve para o seu Wx.", tag="Estruturas metálicas", date="2026-11-27"),
    dict(slug="calculadoras/momento-de-inercia", kind="calc", src="site_src/posts/post-inercia.html", img="inercia.jpg",
         title="Calculadora de Momento de Inércia e Centroide (Perfis I, T, L, U e Tubos)", short="Momento de inércia e centroide",
         desc="Calcule grátis o centroide, o momento de inércia, o módulo resistente e o raio de giração de retângulos, tubos e perfis I, T, L e U, com passo a passo pelo teorema de Steiner.",
         card="Centroide, Ix, Iy, W e raio de giração de perfis e seções compostas, passo a passo.", tag="Resistência dos materiais", date="2026-11-27"),
    dict(slug="calculadoras/vigas-cortante-e-momento-fletor", kind="calc", src="site_src/posts/post-vigas.html", img="vigas.jpg",
         title="Calculadora de Vigas: Reações, Diagrama de Cortante e Momento Fletor", short="Vigas: cortante e momento fletor",
         desc="Calcule grátis as reações de apoio e desenhe os diagramas de esforço cortante e momento fletor de vigas biapoiadas e em balanço, com cargas pontuais, distribuídas e momentos, passo a passo.",
         card="Reações, diagramas de cortante e momento fletor e resolução passo a passo.", tag="Resistência dos materiais", date="2026-11-27"),
    dict(slug="calculadoras/categoria-vaso-de-pressao-nr-13", kind="calc", src="site_src/posts/post-nr13-vasos.html", img="nr13-vasos.jpg",
         title="Categoria de Vaso de Pressão NR-13: Calculadora, Tabela e Prazos de Inspeção", short="Categoria de vaso de pressão (NR-13)",
         desc="Descubra grátis se o vaso entra na NR-13, a classe do fluido, o grupo de risco P·V, a categoria (I a V) e os prazos de inspeção externa e interna, com e sem SPIE.",
         card="Enquadramento, P·V, grupo, categoria I a V e prazos de inspeção pela NR-13.", tag="Segurança · NR-13", date="2026-11-27"),
    dict(slug="calculadoras/torque-de-aperto-de-parafusos", kind="calc", src="site_src/posts/post-torque-parafusos.html", img="torque-parafusos.jpg",
         title="Calculadora de Torque de Aperto de Parafusos (com Tabela 8.8, 10.9 e 12.9)", short="Torque de aperto de parafusos",
         desc="Calcule grátis o torque de aperto e a pré-carga de parafusos métricos M3 a M48, classes 4.6 a 12.9, pela condição da rosca. Com tabela pronta e exemplo resolvido.",
         card="Torque e pré-carga de parafusos M3 a M48, classes 4.6 a 12.9, com tabela pronta.", tag="Elementos de máquinas", date="2026-11-26"),
    dict(slug="simulados/engenharia-mecanica-petrobras", kind="sim", src="post-simulado-mecanica-70.html", img="simulado-mecanica.jpg",
         title="Simulado de Engenharia Mecânica Petrobras e Transpetro: 70 Questões Inéditas Comentadas (Estilo Cesgranrio)", short="Engenharia Mecânica · Petrobras e Transpetro",
         desc="Simulado grátis com 70 questões inéditas de Engenharia Mecânica no estilo Cesgranrio (Petrobras e Transpetro), com resoluções comentadas e desempenho por matéria.",
         card="70 questões inéditas no estilo Cesgranrio, com resolução comentada, cronômetro e desempenho por matéria.", tag="Concursos", date="2026-11-26"),
]

MATS = json.load(open(f"{SRC}/posts/materias.json", encoding="utf-8"))
for m in MATS:
    PAGES.append(dict(slug=f"simulados/{m['slug']}", kind="mat", src=f"site_src/posts/materia-{m['slug']}.html", img=f"{m['slug']}.jpg",
        title=f"Questões de {m['mat']} para Concurso Petrobras e Transpetro ({m['n']} Questões Comentadas)", short=f"Questões de {m['mat']}",
        desc=f"{m['n']} questões inéditas de {m['mat']} no estilo Cesgranrio, com resumo do que mais cai, fórmulas, pegadinhas e resolução comentada.",
        card=f"{m['n']} questões inéditas, resumo de fórmulas e pegadinhas da banca.", tag="Concursos", date="2026-11-26"))

CSS = r"""
:root{--az:#0f2742;--az2:#163d6b;--azl:#1f6feb;--la:#f28c28;--la2:#f9a24b;--tx:#1c2430;--su:#5a6575;--bo:#dde3ec;--bg:#f6f8fb}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;font-family:system-ui,-apple-system,"Segoe UI",Roboto,Ubuntu,sans-serif;color:var(--tx);background:#fff;line-height:1.65}
a{color:var(--azl)}
img{max-width:100%;height:auto}
.wrap{max-width:900px;margin:0 auto;padding:0 18px}
.top{background:var(--az);color:#fff;position:sticky;top:0;z-index:20;box-shadow:0 1px 0 rgba(255,255,255,.06)}
.top .wrap{display:flex;align-items:center;gap:14px;min-height:60px}
.brand{display:flex;align-items:center;gap:10px;color:#fff;text-decoration:none;font-weight:800;letter-spacing:.2px}
.brand img{width:36px;height:36px;border-radius:50%}
.nav{margin-left:auto;display:flex;gap:4px;flex-wrap:wrap}
.nav a{color:#dbe6f4;text-decoration:none;font-size:.92rem;padding:7px 10px;border-radius:8px}
.nav a:hover,.nav a.on{background:rgba(255,255,255,.1);color:#fff}
.crumb{font-size:.82rem;color:var(--su);margin:18px 0 4px}
.crumb a{color:var(--su);text-decoration:none}
h1{font-size:clamp(1.55rem,3.4vw,2.15rem);line-height:1.2;margin:6px 0 8px;color:var(--az)}
.meta{font-size:.85rem;color:var(--su);margin-bottom:14px}
.cover{border-radius:14px;display:block;margin:8px 0 22px;aspect-ratio:1200/630;width:100%;object-fit:cover;background:var(--bg)}
article h2{color:var(--az);margin-top:1.8em;line-height:1.25}
article h3{color:var(--az2)}
.hero{background:linear-gradient(90deg,#0f2742 0%,#0f2742 38%,rgba(15,39,66,.55) 62%,rgba(15,39,66,0) 85%),url(/img/hero-inicio.jpg) right center/auto 100% no-repeat,#0f2742;color:#fff;padding:70px 0 64px;min-height:400px}
@media(max-width:900px){.hero{background:linear-gradient(180deg,rgba(15,39,66,.92),rgba(15,39,66,.8)),url(/img/hero-inicio.jpg) center/cover no-repeat,#0f2742}}
.hero h1{color:#fff;font-size:clamp(1.8rem,4.2vw,2.6rem);margin:0 0 10px}
.hero h1 span{color:var(--la2)}
.hero p{color:#c9d6e6;font-size:1.08rem;max-width:520px;margin:0 0 18px}
.hero h1{max-width:560px}
.pill{display:inline-block;background:var(--la);color:var(--tx);font-weight:800;font-size:.78rem;padding:5px 12px;border-radius:99px;margin-bottom:14px;letter-spacing:.3px}
.btn{display:inline-block;background:var(--la);color:var(--tx);font-weight:700;text-decoration:none;padding:11px 18px;border-radius:10px;margin:4px 8px 4px 0}
.btn.sec{background:transparent;color:#fff;border:1px solid rgba(255,255,255,.35)}
.sec-t{margin:34px 0 12px;font-size:1.35rem;color:var(--az)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}
a.card{border:1px solid var(--bo);border-radius:14px;overflow:hidden;text-decoration:none;color:var(--tx);background:#fff;transition:transform .15s,box-shadow .15s;display:flex;flex-direction:column}
a.card:hover{transform:translateY(-2px);box-shadow:0 8px 24px rgba(15,39,66,.12)}
a.card img{aspect-ratio:1200/630;object-fit:cover;width:100%;display:block}
a.card div{padding:12px 14px 16px}
a.card small{color:var(--la);font-weight:800;font-size:.72rem;text-transform:uppercase;letter-spacing:.5px}
a.card b{display:block;font-size:1.02rem;line-height:1.3;margin:3px 0 6px;color:var(--az)}
a.card p{margin:0;font-size:.88rem;color:var(--su);line-height:1.45}
.note{background:var(--bg);border-left:4px solid var(--la);border-radius:8px;padding:12px 16px;font-size:.92rem}
.rel{margin:40px 0 10px}
footer{background:var(--az);color:#c9d6e6;margin-top:50px;padding:28px 0;font-size:.88rem}
footer a{color:#fff;text-decoration:none;margin-right:14px;display:inline-block}
footer p{margin:8px 0}
body #fde-q .bar-top{top:68px}
@media(max-width:640px){.top{position:static}body #fde-q .bar-top{top:0}.top .wrap{flex-wrap:wrap;padding-top:8px;padding-bottom:8px}.nav{margin-left:0;width:100%}.nav a{padding:6px 8px;font-size:.86rem}}
"""

import json as _json
for _e in _json.load(open(ROOT + "/site_src/exer/exercicios.json", encoding="utf-8")):
    _c = _e["publico"] == "concurso"
    PAGES.append(dict(slug=f"exercicios/{_e['slug']}", kind="ex", pub=_e["publico"], src=f"site_src/posts/ex-{_e['id']}.html", img=f"ex-{_e['id']}.jpg",
        title=(("Questão de concurso: " if _c else "Exercício resolvido: ") + _e["titulo"]), short=_e["titulo"],
        desc=(f"{_e['titulo']}. Questão de {_e['materia']} no estilo das bancas, com alternativas, resolução comentada e vídeo." if _c else
              f"{_e['titulo']}. Exercício de {_e['materia']} resolvido passo a passo, com figura, vídeo e calculadora para conferir."),
        card=("Questão estilo banca com resolução comentada e a pegadinha." if _c else "Resolvido passo a passo, com vídeo de 40 segundos."),
        tag=("Concursos · " if _c else "Faculdade · ") + _e["materia"], date="2026-11-27"))

def nav(active):
    items = [("/", "Início"), ("/calculadoras/", "Calculadoras"), ("/exercicios/", "Exercícios"), ("/simulados/", "Simulados"), ("/sobre/", "Sobre"), ("/contato/", "Contato")]
    return "".join(f'<a href="{u}"{" class=on" if active == u else ""}>{t}</a>' for u, t in items)

def layout(*, path, title, desc, body, img=None, active="", jsonld=None, page_title=None, noindex=False):
    url = DOMAIN + path
    og = DOMAIN + "/img/" + (img or "simulado-mecanica.jpg")
    ld = "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in (jsonld or []))
    t = page_title or f"{title} | {SITE}"
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(t)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
{'<meta name="robots" content="noindex">' if noindex else ''}
<meta property="og:type" content="{'article' if img else 'website'}">
<meta property="og:site_name" content="{SITE}">
<meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0f2742">
<link rel="icon" type="image/png" sizes="48x48" href="/img/favicon-48.png">
<link rel="icon" type="image/png" sizes="192x192" href="/img/logo-192.png">
<link rel="apple-touch-icon" href="/img/apple-touch-icon.png">
<link rel="stylesheet" href="/assets/site.css">
<meta name="google-adsense-account" content="ca-pub-9800534934394753">
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-9800534934394753" crossorigin="anonymous"></script>
{ld}
</head>
<body>
<header class="top"><div class="wrap"><a class="brand" href="/"><img src="/img/logo-192.png" alt="" width="36" height="36">{SITE}</a><nav class="nav" aria-label="Menu principal">{nav(active)}</nav></div></header>
<main>{body}</main>
<footer><div class="wrap">
<p><b style="color:#fff">{SITE}</b> · calculadoras e simulados gratuitos para engenheiros, técnicos e estudantes.</p>
<p><a href="/calculadoras/">Calculadoras</a><a href="/exercicios/">Exercícios</a><a href="/simulados/">Simulados</a><a href="/sobre/">Sobre</a><a href="/contato/">Contato</a><a href="/privacidade/">Privacidade</a><a href="{IG}" rel="noopener" target="_blank">Instagram</a></p>
<p style="font-size:.8rem;opacity:.8">As ferramentas apoiam estudos, orçamentos e pré-dimensionamentos e não substituem o projeto e a responsabilidade técnica de um profissional habilitado.</p>
</div></footer>
</body>
</html>
"""

def clean_post(raw):
    raw = re.sub(r"<!--.*?-->", "", raw, flags=re.S).strip()
    for a, b in LINKS.items():
        raw = raw.replace(f'href="{a}"', f'href="{b}"')
    raw = raw.replace("Use o formulário de contato do blog", "Use a página de <a href=\"/contato/\">Contato</a>")
    raw = raw.replace("neste blog", "neste site").replace("do blog", "do site")
    return raw

def fmt_date(d):
    y, m, dd = d.split("-")
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    return f"{int(dd)} de {meses[int(m)-1]} de {y}"

def card(p):
    return (f'<a class="card" href="/{p["slug"]}/"><img src="/img/{p["img"]}" alt="" width="1200" height="630" loading="lazy">'
            f'<div><small>{p["tag"]}</small><b>{p["short"]}</b><p>{p["card"]}</p></div></a>')

def write(path, content):
    fp = OUT + path + ("index.html" if path.endswith("/") else "")
    os.makedirs(os.path.dirname(fp), exist_ok=True)
    open(fp, "w", encoding="utf-8").write(content)

def build():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT + "/assets")
    shutil.copytree(SRC + "/img", OUT + "/img")
    open(OUT + "/assets/site.css", "w").write(CSS)
    urls = []
    calcs = [p for p in PAGES if p["kind"] == "calc"]
    sims = [p for p in PAGES if p["kind"] == "sim"]
    mats_all = [p for p in PAGES if p["kind"] == "mat"]
    exs = [p for p in PAGES if p["kind"] == "ex"]

    # Páginas de conteúdo
    for p in PAGES:
        path = f'/{p["slug"]}/'
        sec = ("/calculadoras/", "Calculadoras") if p["kind"] == "calc" else ("/exercicios/", "Exercícios") if p["kind"] == "ex" else ("/simulados/", "Simulados")
        mats = [x for x in PAGES if x["kind"] == "mat"]
        body_post = clean_post(open(f'{ROOT}/{p["src"]}', encoding="utf-8").read())
        for anchor, fig, where in FIGS.get(p["slug"], []):
            figh = open(f"{ROOT}/site_src/figs/{fig}.html", encoding="utf-8").read()
            if anchor in body_post:
                body_post = body_post.replace(anchor, (anchor + figh) if where == "depois" else (figh + anchor), 1)
            else:
                print("AVISO: âncora não encontrada", p["slug"], fig)
        if p["kind"] == "mat":
            i = mats.index(p); rel = [x for x in PAGES if x["kind"] == "sim"] + [mats[(i+1) % len(mats)], mats[(i+2) % len(mats)]]
        elif p["kind"] == "sim":
            rel = mats[:3]
        elif p["kind"] == "ex":
            tool = next((x for x in PAGES if x["kind"] == "calc" and f'/{x["slug"]}/' in body_post), None)
            rel = ([tool] if tool else []) + [x for x in PAGES if x["kind"] == "ex" and x is not p and x["pub"] == p["pub"]][:2]
        else:
            rel = [x for x in PAGES if x is not p and x["kind"] != "mat"][:3]
        extra = ""
        if p["kind"] == "sim":
            extra = '<section class="rel"><h2 class="sec-t">Estude por matéria</h2><p>' + " · ".join(f'<a href="/{x["slug"]}/">{x["short"].replace("Questões de ","")}</a>' for x in mats) + '</p></section>'
        body = (f'<div class="wrap"><nav class="crumb" aria-label="Você está em"><a href="/">Início</a> › <a href="{sec[0]}">{sec[1]}</a></nav>'
                f'<article><h1>{p["title"]}</h1><div class="meta">Publicado em {fmt_date(p["date"])} · {p["tag"]}</div>'
                f'<img class="cover" src="/img/{p["img"]}" alt="{html.escape(p["title"])}" width="1200" height="630" fetchpriority="high">'
                f'{body_post}</article>{extra}'
                f'<section class="rel"><h2 class="sec-t">Veja também</h2><div class="grid">{"".join(card(x) for x in rel)}</div></section></div>')
        ld = [
            {"@context": "https://schema.org", "@type": "Article", "headline": p["title"], "description": p["desc"],
             "image": f'{DOMAIN}/img/{p["img"]}', "datePublished": p["date"], "dateModified": TODAY, "inLanguage": "pt-BR",
             "author": {"@type": "Organization", "name": SITE, "url": DOMAIN},
             "publisher": {"@type": "Organization", "name": SITE, "logo": {"@type": "ImageObject", "url": f"{DOMAIN}/img/logo-512.png"}},
             "mainEntityOfPage": DOMAIN + path},
            {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Início", "item": DOMAIN + "/"},
                {"@type": "ListItem", "position": 2, "name": sec[1], "item": DOMAIN + sec[0]},
                {"@type": "ListItem", "position": 3, "name": p["short"], "item": DOMAIN + path}]},
        ]
        if p["kind"] == "calc":
            ld.append({"@context": "https://schema.org", "@type": "WebApplication", "name": p["short"], "url": DOMAIN + path,
                       "applicationCategory": "EngineeringApplication", "operatingSystem": "Any", "inLanguage": "pt-BR",
                       "offers": {"@type": "Offer", "price": "0", "priceCurrency": "BRL"}})
        write(path, layout(path=path, title=p["title"], desc=p["desc"], body=body, img=p["img"], active=sec[0], jsonld=ld))
        urls.append((path, p["date"]))

    # Listagens
    for path, h, intro, items in [
        ("/calculadoras/", "Calculadoras de engenharia", "Ferramentas gratuitas que funcionam direto no navegador, no computador ou no celular, sem cadastro. Cada uma traz a fórmula, a norma aplicável e um exemplo resolvido.", calcs),
        ("/simulados/", "Simulados para concursos de engenharia", "Questões inéditas no estilo das bancas, com resolução comentada, cronômetro e painel de desempenho por matéria. Seu progresso fica salvo no navegador, sem cadastro.", sims + mats_all)]:
        if path == "/calculadoras/":
            grupos = ""
            for area, tags in AREAS:
                its = [x for x in items if x["tag"] in tags]
                if its: grupos += f'<h2 class="sec-t">{area}</h2><div class="grid">{"".join(card(x) for x in its)}</div>'
            resto = [x for x in items if not any(x["tag"] in t for _, t in AREAS)]
            if resto: grupos += f'<h2 class="sec-t">Outras</h2><div class="grid">{"".join(card(x) for x in resto)}</div>'
            body = f'<div class="wrap"><nav class="crumb"><a href="/">Início</a></nav><h1>{h}</h1><p>{intro}</p>{grupos}</div>'
        else:
            body = f'<div class="wrap"><nav class="crumb"><a href="/">Início</a></nav><h1>{h}</h1><p>{intro}</p><div class="grid">{"".join(card(x) for x in items)}</div></div>'
        write(path, layout(path=path, title=h, desc=intro, body=body, active=path))
        urls.append((path, TODAY))

    intro = "Exercícios resolvidos passo a passo para quem está na faculdade e questões no estilo das bancas para quem estuda para concursos. Cada um tem figura, vídeo curto com a resolução narrada e a calculadora para conferir o resultado."
    body = (f'<div class="wrap"><nav class="crumb"><a href="/">Início</a></nav><h1>Exercícios resolvidos de engenharia</h1><p>{intro}</p>'
            f'<h2 class="sec-t">Para a faculdade</h2><div class="grid">{"".join(card(x) for x in exs if x["pub"] != "concurso")}</div>'
            f'<h2 class="sec-t">Cai na prova: concursos</h2><div class="grid">{"".join(card(x) for x in exs if x["pub"] == "concurso")}</div>'
            f'<p class="note">Novos exercícios toda semana. Siga o <a href="{IG}" target="_blank" rel="noopener">@ferramentasdoengenheiro</a> para receber os vídeos.</p></div>')
    write("/exercicios/", layout(path="/exercicios/", title="Exercícios resolvidos de engenharia", desc=intro, body=body, active="/exercicios/"))
    urls.append(("/exercicios/", TODAY))

    # Home
    body = f"""<section class="hero"><div class="wrap"><span class="pill">GRÁTIS · SEM CADASTRO</span>
<h1>Calculadoras e simulados para <span>engenheiros</span></h1>
<p>Contas do dia a dia de projeto, orçamento e obra resolvidas no navegador, e questões inéditas para treinar para os concursos de engenharia.</p>
<a class="btn" href="/calculadoras/">Ver calculadoras</a><a class="btn sec" href="/simulados/engenharia-mecanica-petrobras/">Fazer o simulado</a></div></section>
<div class="wrap"><h2 class="sec-t">Simulados</h2><div class="grid">{"".join(card(x) for x in sims)}</div>
<p style="margin-top:14px"><b>Por matéria:</b> {" · ".join(f'<a href="/{x["slug"]}/">{x["short"].replace("Questões de ","")}</a>' for x in mats_all)}</p>
<h2 class="sec-t">Exercícios resolvidos</h2><div class="grid">{"".join(card(x) for x in [exs[0], exs[5], exs[2]])}</div>
<p style="margin-top:14px"><a href="/exercicios/"><b>Ver todos os exercícios →</b></a></p>
<h2 class="sec-t">Calculadoras</h2><div class="grid">{"".join(card(x) for x in calcs)}</div>
<h2 class="sec-t">Por que usar</h2>
<p class="note"><b>Fórmula aberta e norma citada.</b> Toda ferramenta mostra o método, as unidades e um exemplo resolvido, para você conferir o resultado. Os valores digitados ficam só no seu navegador.</p></div>"""
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": DOMAIN + "/", "inLanguage": "pt-BR"},
          {"@context": "https://schema.org", "@type": "Organization", "name": SITE, "url": DOMAIN + "/", "logo": f"{DOMAIN}/img/logo-512.png", "sameAs": [IG]}]
    write("/", layout(path="/", title=SITE, page_title=f"{SITE}: calculadoras e simulados de engenharia grátis",
                      desc="Calculadoras gratuitas de engenharia (tinta, queda de tensão, peso de aço, perda de carga) e simulados com questões inéditas para concursos.",
                      body=body, active="/", jsonld=ld))
    urls.append(("/", TODAY))

    # Páginas institucionais
    sobre = clean_post(open(f"{ROOT}/pg-sobre.html", encoding="utf-8").read())
    priv = clean_post(open(f"{ROOT}/pg-privacidade.html", encoding="utf-8").read())
    priv = (priv.replace("o blog Ferramentas do Engenheiro (ferramentasdoengenheiro.blogspot.com)", "o site Ferramentas do Engenheiro (ferramentasdoengenheiro.com)")
                .replace("coletados de forma automática pela plataforma Blogger e por ferramentas de estatística do Google", "coletados de forma automática pela hospedagem do site e por ferramentas de estatística do Google")
                .replace("Este blog é hospedado no Blogger, do Google, e pode exibir", "Este site pode exibir")
                .replace("Formulário de contato e comentários", "Mensagens de contato")
                .replace("ou um comentário", "")
                .replace("blog", "site"))
    priv = priv.replace("são processados apenas no seu navegador", "são processados apenas no seu navegador") + \
        '<div style="max-width:860px;margin:0 auto"><h2>Histórico dos simulados</h2><p>O desempenho nos simulados (questões respondidas, acertos e tempo) fica salvo apenas no armazenamento local do seu navegador (localStorage). Ele não é enviado para nós. Você pode apagá-lo a qualquer momento pelo botão "Zerar histórico" no simulado ou limpando os dados do navegador.</p></div>'
    contato = f"""<div style="max-width:860px;margin:0 auto">
<p>Quer sugerir uma nova calculadora, avisar sobre um erro ou falar sobre parcerias? Fale com a gente pelo <a href="{IG}" target="_blank" rel="noopener"><b>Instagram @ferramentasdoengenheiro</b></a>, por mensagem direta.</p>
<h2>Ao relatar um erro, informe</h2>
<ul><li>o link da ferramenta ou o código da questão (por exemplo, MEC-T01);</li><li>os valores que você digitou;</li><li>o resultado que apareceu e o que você esperava, com a fonte (norma, catálogo ou tabela), se tiver.</li></ul>
<p>Respondemos assim que possível, normalmente em alguns dias úteis.</p></div>"""
    for path, h, d, b in [("/sobre/", "Sobre o Ferramentas do Engenheiro", "Quem somos e como as calculadoras e os simulados do Ferramentas do Engenheiro são feitos.", sobre),
                          ("/contato/", "Contato", "Fale com o Ferramentas do Engenheiro: sugestões de calculadoras, correções e parcerias.", contato),
                          ("/privacidade/", "Política de Privacidade", "Como o Ferramentas do Engenheiro trata dados, cookies e publicidade, de acordo com a LGPD.", priv)]:
        write(path, layout(path=path, title=h, desc=d, body=f'<div class="wrap"><nav class="crumb"><a href="/">Início</a></nav><h1>{h}</h1>{b}</div>', active=path))
        urls.append((path, TODAY))

    # 404, sitemap, robots, CNAME
    open(OUT + "/404.html", "w").write(layout(path="/404.html", title="Página não encontrada", desc="Página não encontrada.", noindex=True,
        body='<div class="wrap"><h1>Página não encontrada</h1><p>O endereço pode ter mudado. Veja as <a href="/calculadoras/">calculadoras</a> e os <a href="/simulados/">simulados</a>.</p></div>'))
    sm = "".join(f"<url><loc>{DOMAIN}{u}</loc><lastmod>{d}</lastmod></url>" for u, d in urls)
    open(OUT + "/sitemap.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>')
    open(OUT + "/robots.txt", "w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    open(OUT + "/ads.txt", "w").write("google.com, pub-9800534934394753, DIRECT, f08c47fec0942fa0\n")
    open(OUT + "/CNAME", "w").write("ferramentasdoengenheiro.com\n")
    open(OUT + "/.nojekyll", "w").write("")
    open(OUT + "/google8c5e0565b8eec656.html", "w").write("google-site-verification: google8c5e0565b8eec656.html")
    print(len(urls), "páginas")

if __name__ == "__main__":
    build()
