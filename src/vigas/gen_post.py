# -*- coding: utf-8 -*-
S='style="padding:7px 8px;border-bottom:1px solid #eef1f5;text-align:center"'
S0='style="padding:7px 8px;border-bottom:1px solid #eef1f5"'
H='style="padding:8px;border-bottom:2px solid #dde3ec;text-align:center;background:#f6f8fb"'
H0='style="padding:8px;border-bottom:2px solid #dde3ec;text-align:left;background:#f6f8fb"'
T=lambda head,rows:f'<table style="border-collapse:collapse;width:100%;font-size:.95rem;margin:8px 0 16px"><thead><tr><th {H0}>{head[0]}</th>'+"".join(f'<th {H}>{h}</th>' for h in head[1:])+'</tr></thead><tbody>'+"".join(f'<tr><td {S0}>{r[0]}</td>'+"".join(f'<td {S}>{c}</td>' for c in r[1:])+'</tr>' for r in rows)+'</tbody></table>'
F=lambda s:f'<p style="background:#f6f8fb;border-left:4px solid #1f6feb;padding:12px 16px;border-radius:6px">{s}</p>'
top='''<div style="font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;line-height:1.65;color:#1c2430;max-width:860px;margin:0 auto">
<p>Toda viga que recebe carga trabalha com dois esforços internos: o <b>esforço cortante</b> (V), que tenta "cortar" a viga na vertical, e o <b>momento fletor</b> (M), que tenta dobrá-la. Saber onde cada um é máximo é o primeiro passo para dimensionar um perfil, uma prateleira, uma ponte rolante ou uma laje, e é a matéria que mais reprova em Resistência dos Materiais.</p>
<p>Monte a sua viga abaixo: escolha os apoios, adicione cargas pontuais, distribuídas (uniformes, triangulares ou trapezoidais) e momentos. A calculadora mostra as reações, desenha os diagramas de cortante e de momento fletor e explica a resolução passo a passo.</p>
<h2>Calculadora de vigas: reações, cortante e momento fletor</h2>
'''
bottom=f'''
<h2>Como resolver uma viga isostática</h2>
<p>Vigas biapoiadas e em balanço são <b>isostáticas</b>: as três equações de equilíbrio da estática bastam para achar as reações. O roteiro é sempre o mesmo:</p>
{F("<b>1. Substitua as cargas distribuídas pela resultante.</b> Uniforme: F = w × comprimento, no meio do trecho. Triangular: F = w × comprimento / 2, a 1/3 do lado maior. Trapezoidal: F = (w<sub>1</sub> + w<sub>2</sub>)/2 × comprimento.")}
{F("<b>2. Some os momentos em um apoio e iguale a zero.</b> Isso dá a reação do outro apoio sem precisar da primeira.")}
{F("<b>3. Some as forças verticais e iguale a zero.</b> Isso dá a reação que falta.")}
{F("<b>4. Corte a viga em seções e calcule V e M.</b> Use sempre o pedaço à esquerda do corte: V é a soma das forças verticais, M é a soma dos momentos em relação ao ponto do corte.")}
<p>Duas relações ajudam a conferir o desenho dos diagramas:</p>
<ul>
<li><b>dV/dx = −w</b>: a inclinação do cortante é a carga distribuída. Sem carga distribuída, o cortante é constante; com carga uniforme, é uma reta inclinada.</li>
<li><b>dM/dx = V</b>: a inclinação do momento é o cortante. Por isso o <b>momento é máximo onde o cortante passa por zero</b> ou troca de sinal.</li>
</ul>
<p>Carga pontual causa um degrau no cortante; momento concentrado causa um degrau no momento fletor.</p>

<h2>Exemplo resolvido</h2>
<p>Viga biapoiada de 6 m, com uma carga distribuída de 5 kN/m em todo o vão e uma carga pontual de 20 kN a 2 m do apoio A (é o exemplo que já vem preenchido na calculadora).</p>
<p><b>Resultante da distribuída:</b> 5 × 6 = 30 kN, a 3 m de A.<br>
<b>Momentos em A:</b> R<sub>B</sub> × 6 = 20 × 2 + 30 × 3 = 130 → <b>R<sub>B</sub> = 21,67 kN</b>.<br>
<b>Forças verticais:</b> R<sub>A</sub> = 20 + 30 − 21,67 → <b>R<sub>A</sub> = 28,33 kN</b>.<br>
<b>Cortante:</b> logo antes da carga pontual, V = 28,33 − 5 × 2 = 18,33 kN; logo depois, V = 18,33 − 20 = −1,67 kN. O cortante troca de sinal em x = 2 m.<br>
<b>Momento máximo</b> (em x = 2 m): M = 28,33 × 2 − 5 × 2²/2 = <b>46,67 kN·m</b>.</p>

<h2>Fórmulas prontas dos casos clássicos</h2>
<p>Para conferir o resultado ou resolver rápido na prova (E = módulo de elasticidade, I = momento de inércia da seção):</p>
{T(["Caso","Reações","Momento máximo","Flecha máxima"],[
 ["Biapoiada, carga P no meio","P/2 e P/2","PL/4 (no meio)","PL³/(48EI)"],
 ["Biapoiada, carga uniforme w","wL/2 e wL/2","wL²/8 (no meio)","5wL⁴/(384EI)"],
 ["Balanço, carga P na ponta","R = P; M = PL","PL (no engaste)","PL³/(3EI)"],
 ["Balanço, carga uniforme w","R = wL; M = wL²/2","wL²/2 (no engaste)","wL⁴/(8EI)"]])}
<p>Com o momento máximo em mãos, a tensão de flexão é <b>σ = M / W</b>, onde W é o módulo resistente da seção. Para um perfil, compare σ com a tensão admissível do aço; o <a href="/calculadoras/peso-de-perfis/">peso do perfil</a> você calcula na outra ferramenta.</p>

<h2>Perguntas frequentes</h2>
<h3>Qual convenção de sinais a calculadora usa?</h3>
<p>Cortante positivo quando a resultante das forças à esquerda do corte aponta para cima. Momento positivo quando traciona a fibra de baixo (a viga "sorri"). O diagrama de momento é desenhado do lado tracionado, como é comum no Brasil: momento positivo aparece abaixo do eixo.</p>
<h3>Funciona para viga com balanço (apoio fora da ponta)?</h3>
<p>Sim. Na viga biapoiada, posicione os apoios A e B onde quiser dentro do comprimento. Os trechos além dos apoios viram balanços, e o momento negativo sobre o apoio aparece no diagrama.</p>
<h3>E viga contínua, com três ou mais apoios?</h3>
<p>Essas são hiperestáticas e exigem método das forças, dos deslocamentos ou de Cross. Por enquanto a calculadora resolve as isostáticas, que são a base de tudo.</p>
<h3>Por que meu professor desenha o momento para cima?</h3>
<p>É só convenção de desenho. Alguns livros desenham o momento positivo acima do eixo. O valor e o sinal são os mesmos.</p>

<p style="font-size:.85rem;color:#5a6575;border-top:1px solid #dde3ec;padding-top:12px;margin-top:28px">Ferramenta para estudo e pré-dimensionamento. Projetos de estruturas devem seguir as normas aplicáveis (como a NBR 8800 para aço) e ser verificados por profissional habilitado. Treine o assunto nas <a href="/simulados/questoes-de-resistencia-dos-materiais/">questões de Resistência dos Materiais</a>.</p>
</div>'''
open('/home/claude/site_src/posts/post-vigas.html','w').write(top+open('/home/claude/site_src/vigas/tool.html').read()+bottom)
print('ok')
