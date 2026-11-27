# -*- coding: utf-8 -*-
S='style="padding:7px 8px;border-bottom:1px solid #eef1f5;text-align:center"'
S0='style="padding:7px 8px;border-bottom:1px solid #eef1f5"'
H='style="padding:8px;border-bottom:2px solid #dde3ec;text-align:center;background:#f6f8fb"'
H0='style="padding:8px;border-bottom:2px solid #dde3ec;text-align:left;background:#f6f8fb"'
T=lambda head,rows:f'<table style="border-collapse:collapse;width:100%;font-size:.95rem;margin:8px 0 16px"><thead><tr><th {H0}>{head[0]}</th>'+"".join(f'<th {H}>{h}</th>' for h in head[1:])+'</tr></thead><tbody>'+"".join(f'<tr><td {S0}>{r[0]}</td>'+"".join(f'<td {S}>{c}</td>' for c in r[1:])+'</tr>' for r in rows)+'</tbody></table>'
F=lambda s:f'<p style="background:#f6f8fb;border-left:4px solid #1f6feb;padding:12px 16px;border-radius:6px">{s}</p>'
VID='''<figure style="margin:8px auto 24px;max-width:340px;text-align:center"><video controls playsinline preload="none" poster="/ig/inercia/poster.jpg" style="width:100%;border-radius:14px;background:#0f2742;aspect-ratio:9/16" aria-label="Vídeo: por que a régua em pé quase não dobra"><source src="/ig/inercia/reel.mp4" type="video/mp4"></video><figcaption style="font-size:.85rem;color:#5a6575;margin-top:6px">▶ Em 30 segundos: por que a mesma régua dobra deitada e quase não dobra em pé.</figcaption></figure>
'''
top='''<div style="font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.65;color:#1c2430;max-width:860px;margin:0 auto">
<p>Pegue uma régua e tente dobrá-la deitada: é fácil. Agora tente dobrá-la em pé: quase impossível. É o mesmo material e a mesma área. O que muda é o <b>momento de inércia</b>, a propriedade da seção que mede como a área está distribuída em relação ao eixo de flexão. Quanto mais material longe do centro, maior a inércia e mais rígida a peça. É por isso que vigas têm formato de I.</p>
<p>A calculadora abaixo encontra o <b>centroide</b>, os <b>momentos de inércia</b> I<sub>x</sub> e I<sub>y</sub>, os <b>módulos resistentes</b> e os <b>raios de giração</b> de seções retangulares, circulares, tubos, perfis I, T, L e U, ou de qualquer seção montada com retângulos, mostrando o cálculo parte por parte.</p>
'''+VID+'''<h2>Calculadora de momento de inércia e centroide</h2>
'''
bottom=f'''
<h2>Passo a passo: centroide e teorema dos eixos paralelos</h2>
<p>Para seções compostas (T, I, L, U ou qualquer combinação de retângulos), o cálculo segue três passos:</p>
{F("<b>1. Divida a seção em partes simples</b> (retângulos, círculos) e anote a área A<sub>i</sub> e a posição do centroide (x<sub>i</sub>, y<sub>i</sub>) de cada uma. Furos e vazios entram com área negativa.")}
{F("<b>2. Ache o centroide da seção:</b> ȳ = Σ(A<sub>i</sub> · y<sub>i</sub>) / ΣA<sub>i</sub> e x̄ = Σ(A<sub>i</sub> · x<sub>i</sub>) / ΣA<sub>i</sub>")}
{F("<b>3. Transporte a inércia de cada parte para o eixo do centroide (Steiner):</b> I<sub>x</sub> = Σ (I<sub>x,próprio</sub> + A<sub>i</sub> · d<sub>i</sub>²), onde d<sub>i</sub> = y<sub>i</sub> − ȳ")}
<p>O termo A·d² é sempre positivo e costuma ser a maior parcela: é ele que mostra por que afastar material do centro aumenta tanto a inércia.</p>

<h2>Exemplo resolvido: perfil T</h2>
<p>Seção T com mesa de 150 × 20 mm e alma de 15 mm, altura total de 200 mm (o exemplo que vem preenchido na calculadora).</p>
<p><b>Partes:</b> alma 15 × 180 mm → A = 2.700 mm², y = 90 mm; mesa 150 × 20 mm → A = 3.000 mm², y = 190 mm.<br>
<b>Centroide:</b> ȳ = (2.700 × 90 + 3.000 × 190) / 5.700 = <b>142,6 mm</b> a partir da base.<br>
<b>Alma:</b> I = 15 × 180³/12 = 7.290.000 mm⁴; d = 90 − 142,6 = −52,6 mm; A·d² ≈ 7.479.000 mm⁴.<br>
<b>Mesa:</b> I = 150 × 20³/12 = 100.000 mm⁴; d = 47,4 mm; A·d² ≈ 6.732.000 mm⁴.<br>
<b>I<sub>x</sub></b> ≈ 7.290.000 + 7.479.000 + 100.000 + 6.732.000 ≈ <b>21.600.000 mm⁴ = 2.160 cm⁴</b>.</p>

<h2>Fórmulas das seções básicas</h2>
<p>Momento de inércia em relação ao eixo que passa pelo centroide:</p>
{T(["Seção","I<sub>x</sub> (eixo horizontal)","I<sub>y</sub> (eixo vertical)","Centroide"],[
 ["Retângulo b × h","b·h³/12","h·b³/12","no centro"],
 ["Círculo de diâmetro D","π·D⁴/64","π·D⁴/64","no centro"],
 ["Tubo D (externo) e d (interno)","π·(D⁴ − d⁴)/64","π·(D⁴ − d⁴)/64","no centro"],
 ["Triângulo de base b e altura h","b·h³/36","h·b³/48 (isósceles)","a h/3 da base"],
 ["Semicírculo de raio r","0,1098·r⁴","π·r⁴/8","a 4r/(3π) da base"]])}

<h2>Módulo resistente e raio de giração: para que servem</h2>
<ul>
<li><b>Módulo resistente W = I / c</b>, onde c é a distância do centroide à fibra mais afastada. Ele dá a tensão de flexão: <b>σ = M / W</b>. Com o momento fletor da <a href="/calculadoras/vigas-cortante-e-momento-fletor/">calculadora de vigas</a> e o W desta página, você verifica se o perfil aguenta.</li>
<li><b>Raio de giração r = √(I / A)</b> entra na flambagem de pilares: o índice de esbeltez é λ = L<sub>fl</sub> / r. A flambagem acontece em torno do eixo de menor r.</li>
</ul>

<h2>Perguntas frequentes</h2>
<h3>Por que a régua em pé é tão mais rígida?</h3>
<p>Numa régua de 30 × 3 mm, a inércia deitada é 30 × 3³/12 = 67,5 mm⁴. Em pé, é 3 × 30³/12 = 6.750 mm⁴: <b>100 vezes maior</b>, com a mesma área. A altura entra ao cubo na fórmula.</p>
<h3>Qual a diferença entre momento de inércia e módulo resistente?</h3>
<p>A inércia (cm⁴) governa a <b>rigidez</b> (quanto a viga deforma, a flecha). O módulo resistente (cm³) governa a <b>resistência</b> (a tensão máxima). Uma viga pode passar na tensão e falhar na flecha.</p>
<h3>O que é o produto de inércia e os eixos principais?</h3>
<p>Em seções sem eixo de simetria, como a cantoneira L, o produto de inércia I<sub>xy</sub> não é zero, e os eixos de inércia máxima e mínima ficam inclinados. A calculadora mostra os momentos principais I<sub>1</sub> e I<sub>2</sub> e o ângulo θ. Na cantoneira, a flambagem acontece em torno do eixo de I<sub>2</sub>.</p>
<h3>Por que o valor é diferente da tabela do fabricante?</h3>
<p>Perfis laminados têm raios de concordância entre alma e mesa que a calculadora não considera. A diferença costuma ser pequena; para projeto, use a tabela do fabricante.</p>

<p style="font-size:.85rem;color:#5a6575;border-top:1px solid #dde3ec;padding-top:12px;margin-top:28px">Ferramenta para estudo e pré-dimensionamento. Treine o assunto nas <a href="/simulados/questoes-de-resistencia-dos-materiais/">questões de Resistência dos Materiais</a> e calcule o peso do perfil na <a href="/calculadoras/peso-de-perfis/">calculadora de peso de perfis</a>.</p>
</div>'''
open('/home/claude/site_src/posts/post-inercia.html','w').write(top+open('/home/claude/site_src/inercia/tool.html').read()+bottom)
print('ok')
