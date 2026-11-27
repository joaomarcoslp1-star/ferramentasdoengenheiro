# -*- coding: utf-8 -*-
S='style="padding:7px 8px;border-bottom:1px solid #eef1f5;text-align:center"'
S0='style="padding:7px 8px;border-bottom:1px solid #eef1f5"'
H='style="padding:8px;border-bottom:2px solid #dde3ec;text-align:center;background:#f6f8fb"'
H0='style="padding:8px;border-bottom:2px solid #dde3ec;text-align:left;background:#f6f8fb"'
T=lambda head,rows:f'<table style="border-collapse:collapse;width:100%;font-size:.95rem;margin:8px 0 16px"><thead><tr><th {H0}>{head[0]}</th>'+"".join(f'<th {H}>{h}</th>' for h in head[1:])+'</tr></thead><tbody>'+"".join(f'<tr><td {S0}>{r[0]}</td>'+"".join(f'<td {S}>{c}</td>' for c in r[1:])+'</tr>' for r in rows)+'</tbody></table>'
F=lambda s:f'<p style="background:#f6f8fb;border-left:4px solid #1f6feb;padding:12px 16px;border-radius:6px">{s}</p>'
top='''<div style="font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.65;color:#1c2430;max-width:960px;margin:0 auto">
<p>Toda vez que você dimensiona uma viga, um pilar ou uma linha de tubulação, precisa da tabela do perfil: altura, espessuras, peso por metro, área, momento de inércia, módulo resistente. Aqui estão as tabelas dos perfis mais usados no Brasil, num só lugar, com busca, filtros e um recurso que as tabelas em PDF não têm: <b>achar o perfil mais leve que atende ao seu cálculo</b>.</p>
<ul>
<li><b>Perfis I e H laminados W e HP</b> (série Gerdau, padrão americano ASTM A6, em milímetros), 88 bitolas;</li>
<li><b>Vigas soldadas VS</b> (NBR 5884), 174 bitolas;</li>
<li><b>Perfis europeus IPE, HEA e HEB</b> (EN 10365), 56 bitolas;</li>
<li><b>Tubos de aço ASME B36.10M</b> de ⅛" a 36", em todos os schedules (10, 20, 30, STD, 40, 60, XS, 80, 100, 120, 140, 160 e XXS).</li>
</ul>
<h2>Tabelas de perfis e tubos de aço</h2>
'''
bottom=f'''
<h2>Como achar o perfil mais leve para a sua viga</h2>
<p>O dimensionamento à flexão começa pelo módulo resistente necessário: <b>W<sub>x,nec</sub> = M / σ<sub>adm</sub></b>. Com o momento fletor máximo (que você tira da <a href="/calculadoras/vigas-cortante-e-momento-fletor/">calculadora de vigas</a>) e a tensão admissível do aço, digite o W<sub>x</sub> no filtro: a tabela mostra só os perfis que atendem, e o mais leve fica em verde.</p>
{F("<b>Exemplo:</b> uma viga pede W<sub>x</sub> ≥ 500 cm³. Entre todas as famílias, a mais leve é a viga soldada <b>VS 400 × 30</b> (30,2 kg/m, W<sub>x</sub> = 505,7 cm³). Entre os laminados, o mais leve é o <b>W 310 × 38,7</b> (38,7 kg/m). Se a altura estiver limitada a 300 mm, a melhor opção laminada passa a ser o <b>IPE 300</b> (42,2 kg/m). Um HEA 220 também atende, mas pesa 50,5 kg/m: 67% a mais de aço que a VS pelo mesmo serviço.")}
<p>Perfis altos e de mesa estreita (W de mesa estreita, IPE) rendem mais em vigas, porque colocam o material longe do centro. Perfis de mesa larga (H, HP, HEA, HEB) têm inércia mais equilibrada nos dois eixos e são os preferidos para pilares. O <a href="/calculadoras/momento-de-inercia/">calculador de momento de inércia</a> mostra por quê.</p>
<p>Nas vigas soldadas VS, a relação altura/mesa é escolhida para flexão, e elas cobrem alturas que os laminados não têm. Compare sempre o peso: às vezes uma VS mais alta sai mais leve que um laminado.</p>
<p>Esta escolha é um pré-dimensionamento. A verificação completa de vigas e pilares de aço (flambagem local, flambagem lateral com torção, cortante, flecha) segue a NBR 8800.</p>

<h2>Notação das tabelas</h2>
{T(["Símbolo","Significado"],[
 ["d","altura total do perfil (no tubo, D = diâmetro externo)"],["b<sub>f</sub>","largura da mesa"],["t<sub>w</sub> / t<sub>f</sub>","espessura da alma / da mesa"],["A","área da seção transversal"],
 ["I<sub>x</sub>, I<sub>y</sub>","momentos de inércia nos eixos de maior e de menor inércia"],["W<sub>x</sub>, W<sub>y</sub>","módulos resistentes elásticos (I dividido pela distância à fibra extrema)"],
 ["r<sub>x</sub>, r<sub>y</sub>","raios de giração (√(I/A)), usados na esbeltez de pilares"],["Pintura","área lateral externa por metro, para orçar pintura e jateamento"]]).replace('text-align:center"','text-align:left"')}

<h2>Designação dos perfis: W, HP, IPE, HEA e HEB</h2>
<ul>
<li><b>W 310 × 38,7</b>: perfil de abas paralelas com cerca de 310 mm de altura e 38,7 kg/m. O "(H)" no nome indica mesa larga, quase igual à altura.</li>
<li><b>VS 400 × 49</b>: viga soldada da NBR 5884 com 400 mm de altura e cerca de 49 kg/m, montada com três chapas (duas mesas e uma alma).</li>
<li><b>HP</b>: perfil H com alma e mesa de mesma espessura, feito para estacas e pilares.</li>
<li><b>IPE 300</b>: perfil europeu de mesa estreita com 300 mm de altura.</li>
<li><b>HEA / HEB 300</b>: perfis europeus de mesa larga. Para a mesma designação, o HEB tem mesas e alma mais grossas que o HEA (série leve).</li>
</ul>

<h2>Schedule de tubos: o que significa</h2>
<p>O schedule é a série de espessura de parede da ASME B36.10M. Para um mesmo diâmetro nominal (NPS), o diâmetro externo é fixo e o schedule muda a espessura e, portanto, o diâmetro interno. Do NPS 14" em diante, o NPS é igual ao diâmetro externo em polegadas; abaixo disso, não é: um tubo de 4" tem 114,3 mm de diâmetro externo.</p>
<p>Não existe "schedule bom ou ruim": a espessura é escolhida pela pressão de projeto, pela temperatura, pela sobre-espessura de corrosão e pelo código de tubulação aplicável (como a ASME B31.3). A perda de carga, que depende do diâmetro interno, você calcula na <a href="/calculadoras/perda-de-carga/">calculadora de perda de carga</a>.</p>

<h2>Perguntas frequentes</h2>
<h3>De onde vêm os dados?</h3>
<p>Perfis W e HP: dimensões e propriedades publicadas no catálogo de perfis estruturais da Gerdau. Vigas VS: dimensões das chapas da série VS (NBR 5884), com propriedades calculadas a partir delas. Perfis IPE, HEA e HEB: dimensões da EN 10365, com propriedades calculadas incluindo os raios de concordância (a massa calculada confere com a nominal em todas as bitolas). Tubos: dimensões da ASME B36.10M, com massa pela fórmula da própria norma.</p>
<h3>E as séries CS e CVS?</h3>
<p>Estão sendo incluídas na próxima atualização, junto com cantoneiras, perfis U e tubos estruturais.</p>
<h3>O peso da tabela inclui tolerâncias?</h3>
<p>Não. É o peso nominal. A massa real de um lote pode variar dentro das tolerâncias de laminação (em geral −2,5% a +2,5% para perfis). Para listas de material com perda de corte, use a <a href="/calculadoras/peso-de-perfis/">calculadora de peso de perfis</a>.</p>

<p style="font-size:.85rem;color:#5a6575;border-top:1px solid #dde3ec;padding-top:12px;margin-top:28px">Tabelas de referência para estudo, orçamento e pré-dimensionamento. Confirme as dimensões com o catálogo do fornecedor antes de comprar ou fabricar. Treine o assunto nas <a href="/simulados/questoes-de-resistencia-dos-materiais/">questões de Resistência dos Materiais</a>.</p>
</div>'''
open('/home/claude/site_src/posts/post-tabelas.html','w').write(top+open('/home/claude/site_src/tabelas/tool.html').read()+bottom)
print('ok')
