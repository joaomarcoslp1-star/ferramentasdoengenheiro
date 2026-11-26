# -*- coding: utf-8 -*-
B=[('M5',5,14.2),('M6',6,20.1),('M8',8,36.6),('M10',10,58.0),('M12',12,84.3),('M14',14,115),('M16',16,157),('M18',18,192),('M20',20,245),('M22',22,303),('M24',24,353),('M27',27,459),('M30',30,561)]
SP={'8.8':(580,600),'10.9':(830,830),'12.9':(970,970)}
def T(d,At,cl,K=0.20,p=0.75):
    sp=SP[cl][0] if d<=16 else SP[cl][1]; fi=p*At*sp; return fi/1000, K*fi*d/1000
nf=lambda x,dd=0: f"{x:,.{dd}f}".replace(",","X").replace(".",",").replace("X",".")
S='style="padding:7px 8px;border-bottom:1px solid #eef1f5;text-align:right"'
S0='style="padding:7px 8px;border-bottom:1px solid #eef1f5"'
H='style="padding:8px;border-bottom:2px solid #dde3ec;text-align:right;background:#f6f8fb"'
rows="".join(f'<tr><td {S0}><b>{b}</b></td>'+"".join(f'<td {S}>{nf(T(d,a,c)[1],0 if T(d,a,c)[1]>=20 else 1)}</td>' for c in ['8.8','10.9','12.9'])+'</tr>' for b,d,a in B)
tabela=f'<table style="border-collapse:collapse;width:100%;font-size:.95rem;margin:8px 0 6px"><thead><tr><th style="padding:8px;border-bottom:2px solid #dde3ec;text-align:left;background:#f6f8fb">Bitola</th><th {H}>Classe 8.8 (N·m)</th><th {H}>Classe 10.9 (N·m)</th><th {H}>Classe 12.9 (N·m)</th></tr></thead><tbody>{rows}</tbody></table><p style="font-size:.82rem;color:#5a6575;margin:0 0 16px">Rosca métrica grossa, K = 0,20 (parafuso zincado, sem lubrificação adicional), pré-carga de 75% da carga de prova. Para outras condições, use a calculadora acima.</p>'
F=lambda s:f'<p style="background:#f6f8fb;border-left:4px solid #1f6feb;padding:12px 16px;border-radius:6px">{s}</p>'
fi12,t12=T(12,84.3,'8.8')
top=f'''<div style="font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.65;color:#1c2430;max-width:860px;margin:0 auto">
<p>Apertar um parafuso "no braço" é a receita para dois problemas: o parafuso que afrouxa com a vibração e o parafuso que escoa ou rompe no aperto. O que segura uma junta aparafusada é a <b>pré-carga</b>, a força de tração que o parafuso exerce depois de apertado. O <b>torque</b> é só o jeito prático de chegar nela com um torquímetro.</p>
<p>A calculadora abaixo calcula o <b>torque de aperto</b> e a <b>pré-carga</b> de parafusos métricos pela classe de resistência (4.6 a 12.9) e pela condição da rosca (seca, zincada, lubrificada ou com pasta), e ainda monta a tabela completa para todas as bitolas.</p>
<h2>Calculadora de torque de aperto</h2>
'''
bottom=f'''
<h2>Tabela de torque de aperto de parafusos</h2>
<p>Valores de referência para as classes mais usadas em estruturas e máquinas:</p>
{tabela}

<h2>Como calcular o torque de aperto</h2>
<p>O cálculo tem três passos: a carga de prova do parafuso, a pré-carga desejada e o torque que produz essa pré-carga.</p>
{F("<b>1. Carga de prova:</b> F<sub>p</sub> = A<sub>t</sub> × S<sub>p</sub><br>A<sub>t</sub> = área resistente à tração da rosca (mm²) · S<sub>p</sub> = tensão de prova da classe (MPa)")}
{F("<b>2. Pré-carga:</b> F<sub>i</sub> = 0,75 × F<sub>p</sub> (ligações desmontáveis) ou 0,90 × F<sub>p</sub> (ligações permanentes)")}
{F("<b>3. Torque:</b> T = K × F<sub>i</sub> × d<br>K = fator de torque (atrito na rosca e sob a cabeça) · d = diâmetro nominal")}
<p>A área resistente não é a área do diâmetro nominal: ela considera o fundo da rosca. Um M12 tem diâmetro de 12 mm, mas área resistente de 84,3 mm², e não 113 mm².</p>

<h3>Classes de resistência (ISO 898-1)</h3>
<table style="border-collapse:collapse;width:100%;font-size:.95rem;margin:8px 0 16px"><thead><tr><th style="padding:8px;border-bottom:2px solid #dde3ec;text-align:left;background:#f6f8fb">Classe</th><th {H}>Tensão de prova (MPa)</th><th {H}>Escoamento (MPa)</th><th {H}>Resistência à tração (MPa)</th></tr></thead><tbody>
<tr><td {S0}>4.6</td><td {S}>225</td><td {S}>240</td><td {S}>400</td></tr>
<tr><td {S0}>5.8</td><td {S}>380</td><td {S}>420</td><td {S}>520</td></tr>
<tr><td {S0}>8.8 (até M16)</td><td {S}>580</td><td {S}>640</td><td {S}>800</td></tr>
<tr><td {S0}>8.8 (acima de M16)</td><td {S}>600</td><td {S}>660</td><td {S}>830</td></tr>
<tr><td {S0}>10.9</td><td {S}>830</td><td {S}>940</td><td {S}>1.040</td></tr>
<tr><td {S0}>12.9</td><td {S}>970</td><td {S}>1.100</td><td {S}>1.220</td></tr></tbody></table>
<p>A classe vem gravada na cabeça do parafuso. O primeiro número vezes 100 dá a resistência à tração em MPa, e o produto dos dois números vezes 10 dá o escoamento. Exemplo: 8.8 → 800 MPa de resistência e 8 × 8 × 10 = 640 MPa de escoamento.</p>

<h3>Fator de torque K</h3>
<table style="border-collapse:collapse;width:100%;font-size:.95rem;margin:8px 0 16px"><thead><tr><th style="padding:8px;border-bottom:2px solid #dde3ec;text-align:left;background:#f6f8fb">Condição do parafuso</th><th {H}>K</th></tr></thead><tbody>
<tr><td {S0}>Aço sem acabamento (oxidado), seco</td><td {S}>0,30</td></tr>
<tr><td {S0}>Zincado</td><td {S}>0,20</td></tr>
<tr><td {S0}>Lubrificado com óleo</td><td {S}>0,18</td></tr>
<tr><td {S0}>Cadmiado</td><td {S}>0,16</td></tr>
<tr><td {S0}>Com pasta antigripante (MoS₂)</td><td {S}>0,12</td></tr></tbody></table>
<p>O fator K é a maior fonte de incerteza do aperto por torque. O mesmo torque, num parafuso lubrificado em vez de seco, gera uma pré-carga muito maior e pode escoar o parafuso. Por isso, use sempre o K da condição real de montagem.</p>

<h2>Exemplo resolvido</h2>
<p>Parafuso <b>M12, classe 8.8, zincado (K = 0,20)</b>, em uma ligação desmontável (75% da carga de prova). É o exemplo que já vem preenchido na calculadora.</p>
<ol>
<li><b>Carga de prova:</b> F<sub>p</sub> = 84,3 mm² × 580 MPa = 48.894 N ≈ 48,9 kN</li>
<li><b>Pré-carga:</b> F<sub>i</sub> = 0,75 × 48,9 = <b>{nf(fi12,1)} kN</b></li>
<li><b>Torque:</b> T = 0,20 × {nf(fi12*1000,0)} N × 0,012 m = <b>{nf(t12,1)} N·m</b> (≈ {nf(t12/9.80665,1)} kgf·m)</li>
</ol>
<p>Se o mesmo parafuso estivesse seco e oxidado (K = 0,30), o torque para a mesma pré-carga subiria para {nf(t12*1.5,0)} N·m. Se estivesse com pasta de MoS₂ (K = 0,12), cairia para {nf(t12*0.6,0)} N·m.</p>

<h2>Boas práticas de aperto</h2>
<ul>
<li><b>Use torquímetro calibrado</b> e aperte em etapas (por exemplo, 30%, 70% e 100% do torque final).</li>
<li><b>Em flanges e tampas,</b> siga o aperto em cruz (estrela), para comprimir a junta por igual. Em flanges de tubulação e vasos, a referência é a ASME PCC-1.</li>
<li><b>Parafusos de classe 10.9 e 12.9</b> apertados até perto do escoamento não devem ser reaproveitados.</li>
<li><b>Não lubrifique</b> um parafuso cuja tabela de torque foi feita para a condição seca: o torque passa a gerar pré-carga demais.</li>
<li><b>Em juntas críticas,</b> o controle por ângulo (torque + ângulo) ou por alongamento é mais preciso que o torque puro.</li>
</ul>

<h2>Perguntas frequentes</h2>
<h3>Por que a pré-carga é de 75% da carga de prova?</h3>
<p>É a recomendação clássica para ligações que serão desmontadas: deixa margem para a dispersão do aperto (±25%) sem escoar o parafuso. Em ligações permanentes, usa-se até 90%.</p>
<h3>Qual a diferença entre carga de prova e resistência à tração?</h3>
<p>A carga de prova é a maior força que o parafuso suporta sem deformação permanente mensurável, um pouco abaixo do escoamento. A resistência à tração é a força de ruptura.</p>
<h3>Posso usar esta tabela para parafusos de inox?</h3>
<p>Não diretamente. Parafusos de inox (A2-70, A4-80) têm outras resistências e atrito maior, com risco de engripamento. Use os valores do fabricante.</p>
<h3>Como converter N·m em kgf·m?</h3>
<p>Divida por 9,81. Por exemplo, 88 N·m ≈ 9,0 kgf·m. Para lbf·ft, multiplique por 0,738.</p>

<p style="font-size:.85rem;color:#5a6575;border-top:1px solid #dde3ec;padding-top:12px;margin-top:28px">Os valores são de referência para estudo e pré-dimensionamento. Em montagens de equipamentos, siga o torque especificado pelo fabricante ou pelo projeto. Treine o assunto nas <a href="/simulados/questoes-de-elementos-de-maquinas/">questões de Elementos de Máquinas</a> e calcule o peso da estrutura na <a href="/calculadoras/peso-de-perfis/">calculadora de peso de perfis</a>.</p>
</div>'''
open('/home/claude/site_src/posts/post-torque-parafusos.html','w').write(top+open('tool.html').read()+bottom)
print('ok', nf(fi12,1), nf(t12,1))
