# -*- coding: utf-8 -*-
NRURL="https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-partitaria-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-13-nr-13"
S='style="padding:7px 8px;border-bottom:1px solid #eef1f5;text-align:center"'
S0='style="padding:7px 8px;border-bottom:1px solid #eef1f5"'
H='style="padding:8px;border-bottom:2px solid #dde3ec;text-align:center;background:#f6f8fb"'
H0='style="padding:8px;border-bottom:2px solid #dde3ec;text-align:left;background:#f6f8fb"'
T=lambda head,rows:f'<table style="border-collapse:collapse;width:100%;font-size:.95rem;margin:8px 0 16px"><thead><tr><th {H0}>{head[0]}</th>'+"".join(f'<th {H}>{h}</th>' for h in head[1:])+'</tr></thead><tbody>'+"".join(f'<tr><td {S0}>{r[0]}</td>'+"".join(f'<td {S}>{c}</td>' for c in r[1:])+'</tr>' for r in rows)+'</tbody></table>'
F=lambda s:f'<p style="background:#f6f8fb;border-left:4px solid #1f6feb;padding:12px 16px;border-radius:6px">{s}</p>'
top='''<div style="font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.65;color:#1c2430;max-width:860px;margin:0 auto">
<p>Todo vaso de pressão enquadrado na <b>NR-13</b> precisa de uma <b>categoria</b>, de I a V. É ela que define os prazos máximos das inspeções de segurança, os requisitos de instalação e o rigor da documentação. A categoria sai de duas informações: a <b>classe do fluido</b> e o <b>grupo de potencial de risco</b>, calculado pelo produto da pressão pelo volume (P·V).</p>
<p>A calculadora abaixo verifica se o vaso entra na NR-13, calcula o P·V, o grupo e a categoria, e mostra os prazos de exame externo e interno, com e sem SPIE. Ela segue a redação atual da norma, dada pela Portaria MTP nº 1.846/2022.</p>
<h2>Calculadora de categoria de vaso de pressão</h2>
'''
bottom=f'''
<h2>Passo 1: o vaso entra na NR-13?</h2>
<p>Pelo item 13.2.1, a NR-13 se aplica, entre outros, a:</p>
<ul>
<li>vasos de pressão cujo produto <b>P·V seja superior a 8</b>, com P em <b>kPa</b> (pressão máxima de operação, em módulo) e V em m³;</li>
<li>vasos que contenham <b>fluido classe A</b>, independentemente das dimensões e do P·V;</li>
<li>recipientes móveis com P·V acima de 8 ou com fluido classe A;</li>
<li>tubulações com fluido classe A ou B ligadas a caldeiras ou vasos enquadrados;</li>
<li>tanques metálicos de superfície com diâmetro externo acima de 3 m, capacidade acima de 20.000 L e fluido classe A ou B.</li>
</ul>
<p>O item 13.2.2 traz a lista de exclusões. Entre as mais comuns na indústria: vasos com diâmetro interno abaixo de 150 mm para fluidos das classes B, C e D, vasos sujeitos apenas a vácuo abaixo de 5 kPa, extintores e cilindros de gás transportáveis, trocadores de calor a placas gaxetadas e vasos que fazem parte de sistemas auxiliares de pacotes de máquinas. Mesmo excluído, o equipamento continua precisando de inspeção e manutenção (item 13.2.3).</p>
{F("<b>Atenção às unidades:</b> no enquadramento (P·V &gt; 8) a pressão entra em <b>kPa</b>. No grupo de potencial de risco, entra em <b>MPa</b>. É o erro mais comum ao aplicar a norma.")}

<h2>Passo 2: classe do fluido</h2>
<p>Item 13.5.1.1.1 da NR-13:</p>
{T(["Classe","Fluidos"],[
 ["<b>A</b>","inflamáveis; combustíveis a 200 °C ou mais; tóxicos com limite de tolerância até 20 ppm; hidrogênio; acetileno"],
 ["<b>B</b>","combustíveis abaixo de 200 °C; tóxicos com limite de tolerância acima de 20 ppm"],
 ["<b>C</b>","vapor de água; gases asfixiantes simples; ar comprimido"],
 ["<b>D</b>","outro fluido não enquadrado nas classes anteriores"]]).replace('text-align:center"','text-align:left"')}
<p>Em <b>misturas</b>, classifica-se pelo componente de maior risco aos trabalhadores e às instalações, considerando toxicidade, inflamabilidade e concentração (item 13.5.1.1.2). Pelo glossário da norma, fluido inflamável tem ponto de fulgor até 60 °C, e combustível tem ponto de fulgor acima de 60 °C e até 93 °C.</p>

<h2>Passo 3: grupo de potencial de risco</h2>
<p>Multiplique a pressão máxima de operação (em <b>MPa</b>) pelo volume interno (em <b>m³</b>):</p>
{T(["Grupo","Produto P·V (MPa·m³)"],[["1","100 ou mais"],["2","de 30 a menos de 100"],["3","de 2,5 a menos de 30"],["4","de 1 a menos de 2,5"],["5","menos de 1"]])}
<p>A pressão a usar é a pressão máxima de operação manométrica prevista no prontuário. Se o prontuário não informar, use a PMTA (pressão máxima de trabalho admissível).</p>

<h2>Passo 4: categoria do vaso</h2>
{T(["Classe do fluido","Grupo 1","Grupo 2","Grupo 3","Grupo 4","Grupo 5"],[
 ["<b>A</b>","I","I","II","III","III"],["<b>B</b>","I","II","III","IV","IV"],["<b>C</b>","I","II","III","IV","V"],["<b>D</b>","II","III","IV","V","V"]])}
<p>A Categoria I é a de maior risco e a V, a de menor.</p>

<h2>Prazos de inspeção por categoria</h2>
<p>Prazos máximos da inspeção de segurança periódica (item 13.5.4.5). SPIE é o Serviço Próprio de Inspeção de Equipamentos, certificado pelo Inmetro.</p>
{T(["Categoria","Externo sem SPIE","Interno sem SPIE","Externo com SPIE","Interno com SPIE"],[
 ["I","1 ano","3 anos","3 anos","6 anos"],["II","2 anos","4 anos","4 anos","8 anos"],["III","3 anos","6 anos","5 anos","10 anos"],["IV","4 anos","8 anos","6 anos","12 anos"],["V","5 anos","10 anos","7 anos","a critério do PH"]])}

<h2>Exemplos resolvidos</h2>
<h3>1. Reservatório de ar comprimido de 500 L a 12 bar</h3>
<p>Enquadramento: P = 1.200 kPa, V = 0,5 m³ → P·V = 600 &gt; 8 → <b>entra na NR-13</b>.<br>
Grupo: P = 1,2 MPa → P·V = 1,2 × 0,5 = 0,6 MPa·m³ → <b>grupo 5</b>.<br>
Ar comprimido é <b>classe C</b> → <b>Categoria V</b>. Sem SPIE: exame externo a cada 5 anos e interno a cada 10 anos.</p>
<h3>2. Vaso de GLP de 4 m³ a 1,5 MPa</h3>
<p>GLP é inflamável → <b>classe A</b>, enquadrado independentemente do P·V.<br>
P·V = 1,5 × 4 = 6 MPa·m³ → <b>grupo 3</b> → <b>Categoria II</b>. Sem SPIE: exame externo a cada 2 anos e interno a cada 4 anos.</p>
<h3>3. Compressor de oficina com tanque de 50 L a 8 bar</h3>
<p>P·V = 800 kPa × 0,05 m³ = 40, bem acima de 8. Com diâmetro interno acima de 150 mm, <b>o tanque entra na NR-13</b>, ainda que seja pequeno: grupo 5, classe C, Categoria V. É um dos casos mais esquecidos em oficinas e pequenas indústrias.</p>

<h2>Perguntas frequentes</h2>
<h3>Quem pode classificar o vaso e definir os prazos?</h3>
<p>O Profissional Habilitado (PH), engenheiro com atribuição legal para projeto, construção, operação ou inspeção de vasos de pressão. A classificação e os prazos devem constar no prontuário e no registro de segurança do vaso.</p>
<h3>A categoria muda se eu baixar a pressão de operação?</h3>
<p>Pode mudar, porque o grupo depende do P·V. Mas a alteração precisa ser formalizada pelo PH, com ajuste dos dispositivos de segurança e atualização da documentação.</p>
<h3>Vaso de água quente entra em qual classe?</h3>
<p>Água líquida, sem ser vapor, cai em geral na classe D (outro fluido). Já um vaso que contém vapor de água é classe C.</p>
<h3>A tabela de categorias cai em concurso?</h3>
<p>Muito. A NR-13 aparece com frequência em provas de engenharia mecânica e de segurança do trabalho, inclusive da Petrobras e da Transpetro. Treine nas <a href="/simulados/engenharia-mecanica-petrobras/">questões do simulado de Engenharia Mecânica</a>.</p>

<p style="font-size:.85rem;color:#5a6575;border-top:1px solid #dde3ec;padding-top:12px;margin-top:28px">Conteúdo baseado no texto oficial da NR-13, com a redação da Portaria MTP nº 1.846/2022. Consulte a norma completa no <a href="{NRURL}" rel="noopener">site do Ministério do Trabalho e Emprego</a>. Esta página é material de apoio e não substitui a avaliação do Profissional Habilitado. Calcule também a <a href="/calculadoras/perda-de-carga/">perda de carga na tubulação</a> e o <a href="/calculadoras/torque-de-aperto-de-parafusos/">torque dos parafusos de flanges</a>.</p>
</div>'''
open('/home/claude/site_src/posts/post-nr13-vasos.html','w').write(top+open('/home/claude/site_src/nr13/tool.html').read()+bottom)
print('ok')
