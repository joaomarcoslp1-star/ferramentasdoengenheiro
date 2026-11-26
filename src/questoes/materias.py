# -*- coding: utf-8 -*-
# Conteúdo próprio de cada página de matéria (resumo, fórmulas e pegadinhas).
F = lambda s: f'<p style="background:#f6f8fb;border-left:4px solid #1f6feb;padding:10px 14px;border-radius:6px;margin:6px 0">{s}</p>'

MATERIAS = {
"Termodinâmica": dict(slug="questoes-de-termodinamica", cover=("Termodinâmica", "10 questões comentadas"),
 resumo="""<p>Termodinâmica é uma das matérias com mais questões nas provas de Engenharia Mecânica da Cesgranrio. Os temas que mais aparecem são a primeira lei em sistemas fechados e volumes de controle, ciclos de potência (Carnot, Rankine, Otto e Brayton), refrigeração por compressão de vapor e variação de entropia.</p>
<h3>Fórmulas que você precisa saber de cor</h3>
""" + F("<b>Carnot:</b> η = 1 − T<sub>L</sub>/T<sub>H</sub> · COP<sub>ref</sub> = T<sub>L</sub>/(T<sub>H</sub> − T<sub>L</sub>) · COP<sub>BC</sub> = T<sub>H</sub>/(T<sub>H</sub> − T<sub>L</sub>), sempre em kelvin") + F("<b>Otto:</b> η = 1 − 1/r<sup>k−1</sup> · <b>Brayton:</b> η = 1 − 1/r<sub>p</sub><sup>(k−1)/k</sup>") + F("<b>Isentrópico (gás ideal):</b> T<sub>2</sub>/T<sub>1</sub> = (P<sub>2</sub>/P<sub>1</sub>)<sup>(k−1)/k</sup> · <b>Isotérmico:</b> W = mRT·ln(V<sub>2</sub>/V<sub>1</sub>)") + F("<b>Entropia de sólido/líquido:</b> ΔS = m·c·ln(T<sub>2</sub>/T<sub>1</sub>) · <b>Bocal:</b> V<sub>2</sub> = √(2·c<sub>p</sub>·ΔT)") + """
<h3>Pegadinhas da banca</h3>
<ul><li>Usar °C em vez de kelvin no rendimento de Carnot.</li><li>Confundir o COP do refrigerador com o da bomba de calor (a diferença é exatamente 1).</li><li>Esquecer que a válvula de expansão é isentálpica, e não isentrópica.</li><li>No Rankine, achar que o superaquecimento reduz o rendimento (ele aumenta) ou que baixar a pressão do condensador reduz a umidade (ela aumenta).</li></ul>"""),

"Mecânica dos Fluidos": dict(slug="questoes-de-mecanica-dos-fluidos", cover=("Mecânica dos Fluidos", "10 questões comentadas"),
 resumo="""<p>Em Mecânica dos Fluidos, a Cesgranrio cobra principalmente hidrostática (pressão, empuxo e forças em superfícies submersas), as equações da continuidade e de Bernoulli, quantidade de movimento, perda de carga e semelhança dinâmica. As contas costumam usar g = 10 m/s² para sair à mão.</p>
<h3>Fórmulas que você precisa saber de cor</h3>
""" + F("<b>Hidrostática:</b> p = ρgh · <b>Empuxo:</b> E = ρ<sub>fluido</sub>·g·V<sub>sub</sub> · <b>Força em placa plana:</b> F = ρg·h<sub>CG</sub>·A, centro de pressão y<sub>CP</sub> = y<sub>CG</sub> + I<sub>CG</sub>/(y<sub>CG</sub>·A)") + F("<b>Continuidade:</b> Q = A<sub>1</sub>v<sub>1</sub> = A<sub>2</sub>v<sub>2</sub> · <b>Bernoulli:</b> p/ρg + v²/2g + z = constante") + F("<b>Darcy-Weisbach:</b> h<sub>f</sub> = f·(L/D)·v²/2g · <b>Laminar:</b> f = 64/Re, Re = vD/ν · <b>Jato em placa:</b> F = ρQV") + F("<b>Froude:</b> escala de velocidades √λ e de vazões λ<sup>2,5</sup>") + """
<h3>Pegadinhas da banca</h3>
<ul><li>Fator de atrito de Fanning (16/Re) no lugar do de Darcy (64/Re).</li><li>Esquecer o 2 de 2g na perda de carga.</li><li>Responder o volume submerso quando a pergunta é o emerso.</li><li>No laminar, a perda cai com D<sup>4</sup> (Hagen-Poiseuille), e não com D².</li></ul>
<p>Para treinar com valores reais, use também a <a href="/calculadoras/perda-de-carga/">calculadora de perda de carga</a>.</p>"""),

"Resistência dos Materiais": dict(slug="questoes-de-resistencia-dos-materiais", cover=("Resistência dos Materiais", "10 questões comentadas"),
 resumo="""<p>Resistência dos Materiais aparece em toda prova de Engenharia Mecânica. Os assuntos mais frequentes são tração e compressão, torção de eixos, flexão de vigas, flambagem, estado plano de tensões (círculo de Mohr), vasos de pressão de parede fina, critérios de falha e fadiga.</p>
<h3>Fórmulas que você precisa saber de cor</h3>
""" + F("<b>Axial:</b> σ = F/A · δ = FL/(EA) · <b>Torção (eixo maciço):</b> τ<sub>máx</sub> = 16T/(πd³)") + F("<b>Flexão:</b> σ = M/W, retângulo W = bh²/6 e I = bh³/12 · <b>Biapoiada com carga central:</b> M<sub>máx</sub> = PL/4") + F("<b>Euler:</b> P<sub>cr</sub> = π²EI/L<sub>e</sub>², com L<sub>e</sub> = L (biarticulada), 2L (engaste-livre), 0,7L (engaste-articulação), 0,5L (biengastada)") + F("<b>Mohr:</b> centro (σ<sub>x</sub>+σ<sub>y</sub>)/2 e raio √[((σ<sub>x</sub>−σ<sub>y</sub>)/2)² + τ²] · <b>Vaso fino:</b> σ<sub>θ</sub> = pD/2t, σ<sub>L</sub> = pD/4t") + F("<b>Tresca:</b> √(σ² + 4τ²) · <b>von Mises:</b> √(σ² + 3τ²)") + """
<h3>Pegadinhas da banca</h3>
<ul><li>Trocar Tresca por von Mises (Tresca é sempre igual ou mais conservador).</li><li>Usar a viga "deitada" no cálculo do módulo resistente.</li><li>Esquecer que a flecha de balanço com carga distribuída cresce com L<sup>4</sup>.</li><li>Achar que tensão média de compressão prejudica a fadiga (em geral ajuda).</li></ul>"""),

"Transferência de Calor": dict(slug="questoes-de-transferencia-de-calor", cover=("Transferência de Calor", "8 questões comentadas"),
 resumo="""<p>Em Transferência de Calor, a banca cobra condução em paredes planas e cilíndricas com resistências térmicas, convecção, radiação de corpo negro, trocadores de calor (LMTD e ε-NTU), raio crítico de isolamento e o modelo de capacitância global.</p>
<h3>Fórmulas que você precisa saber de cor</h3>
""" + F("<b>Parede plana:</b> R = L/(kA) · <b>Cilindro:</b> R = ln(r<sub>2</sub>/r<sub>1</sub>)/(2πkL) · <b>Convecção:</b> R = 1/(hA)") + F("<b>Raio crítico:</b> cilindro r<sub>cr</sub> = k/h, esfera r<sub>cr</sub> = 2k/h") + F("<b>Radiação:</b> E = εσT<sup>4</sup> · <b>Wien:</b> λ<sub>máx</sub>·T ≈ 2.898 µm·K") + F("<b>LMTD:</b> (ΔT<sub>1</sub> − ΔT<sub>2</sub>)/ln(ΔT<sub>1</sub>/ΔT<sub>2</sub>) · <b>Mudança de fase:</b> ε = 1 − e<sup>−NTU</sup>") + F("<b>Capacitância global:</b> válida se Bi = hL<sub>c</sub>/k &lt; 0,1, com L<sub>c</sub> = V/A; τ = ρcL<sub>c</sub>/h") + """
<h3>Pegadinhas da banca</h3>
<ul><li>Usar 2k/h (esfera) para um cilindro.</li><li>Ignorar o isolante numa parede composta: é ele que domina a resistência.</li><li>Usar a média aritmética no lugar da LMTD.</li><li>Na esfera, L<sub>c</sub> é r/3, e não r.</li></ul>"""),

"Elementos de Máquinas": dict(slug="questoes-de-elementos-de-maquinas", cover=("Elementos de Máquinas", "8 questões comentadas"),
 resumo="""<p>Elementos de Máquinas cobra transmissões (engrenagens e correias), rolamentos, parafusos, chavetas, molas e embreagens. As questões costumam misturar relação de transmissão com potência e torque.</p>
<h3>Fórmulas que você precisa saber de cor</h3>
""" + F("<b>Potência:</b> P = T·ω, com ω = 2πn/60 · <b>Engrenagens:</b> n<sub>1</sub>/n<sub>2</sub> = z<sub>2</sub>/z<sub>1</sub>, e o torque se multiplica pela mesma relação") + F("<b>Correia:</b> n<sub>1</sub>d<sub>1</sub> = n<sub>2</sub>d<sub>2</sub> · v = πdn/60") + F("<b>Rolamentos:</b> L<sub>10</sub> = (C/P)<sup>a</sup> milhões de rotações, a = 3 (esferas) ou 10/3 (rolos)") + F("<b>Aperto de parafusos:</b> T = K·F·d · <b>Chaveta:</b> F = T/(d/2), τ = F/(bL)") + F("<b>Mola helicoidal:</b> k = Gd<sup>4</sup>/(8D³n) · <b>Embreagem (desgaste uniforme):</b> T = μ·F·r<sub>m</sub>·N") + """
<h3>Pegadinhas da banca</h3>
<ul><li>Dividir o torque pela relação de transmissão em vez de multiplicar.</li><li>Esquecer as duas faces de atrito da embreagem.</li><li>Usar o raio no lugar do diâmetro no aperto de parafusos.</li><li>Engrenagens helicoidais geram força axial: exigem mancais que a suportem.</li></ul>"""),

"Materiais e Tratamentos Térmicos": dict(slug="questoes-de-materiais-e-tratamentos-termicos", cover=("Materiais e Tratamentos", "8 questões comentadas"),
 resumo="""<p>Em Materiais, a Cesgranrio pergunta sobre o diagrama ferro-carbono, tratamentos térmicos, ensaios mecânicos (tração, dureza e impacto), estruturas cristalinas e corrosão. São questões mais conceituais, que premiam quem entende o porquê.</p>
<h3>O que você precisa saber</h3>
""" + F("<b>Fe-C:</b> eutetoide em 0,76% C e 727 °C; hipoeutetoide → ferrita + perlita; hipereutetoide → cementita + perlita") + F("<b>Regra da alavanca:</b> fração de perlita = (C − 0,02)/(0,76 − 0,02)") + F("<b>Têmpera:</b> martensita (adifusional, dura e frágil) · <b>Revenimento:</b> alivia tensões e dá tenacidade · <b>Normalização:</b> resfria ao ar") + F("<b>Estruturas:</b> ferrita CCC (FEA 0,68), austenita CFC (FEA 0,74) · <b>Dureza:</b> S<sub>ut</sub> ≈ 3,45·HB (MPa)") + """
<h3>Pegadinhas da banca</h3>
<ul><li>Dizer que a normalização resfria no forno (é ao ar).</li><li>Achar que a martensita se forma por difusão.</li><li>Inox austenítico (CFC) não tem transição dúctil-frágil; aço ferrítico (CCC) tem.</li><li>Na corrosão galvânica, ânodo pequeno e cátodo grande é a pior combinação.</li></ul>"""),

"Máquinas de Fluxo": dict(slug="questoes-de-maquinas-de-fluxo", cover=("Máquinas de Fluxo", "8 questões comentadas"),
 resumo="""<p>Bombas, compressores e turbinas são presença garantida nas provas da Petrobras e da Transpetro. Os temas mais frequentes são NPSH e cavitação, leis de semelhança, ponto de operação, associação de bombas, potência de bombeamento e ciclo Brayton.</p>
<h3>Fórmulas que você precisa saber de cor</h3>
""" + F("<b>NPSH disponível:</b> (p<sub>atm</sub> − p<sub>v</sub>)/ρg − z<sub>s</sub> − h<sub>f,s</sub> (z<sub>s</sub> positivo com a bomba acima do nível) · cavita se NPSH<sub>d</sub> &lt; NPSH<sub>r</sub>") + F("<b>Afinidade:</b> Q ∝ n, H ∝ n², P ∝ n³") + F("<b>Potência:</b> P<sub>hid</sub> = ρgQH · P<sub>eixo</sub> = P<sub>hid</sub>/η") + F("<b>Ponto de operação:</b> curva da bomba = curva do sistema · <b>Compressão em 2 estágios:</b> p<sub>int</sub> = √(p<sub>1</sub>p<sub>2</sub>)") + """
<h3>Pegadinhas da banca</h3>
<ul><li>Aumentar a rotação para "resolver" a cavitação (piora, porque o NPSH<sub>r</sub> sobe).</li><li>Achar que duas bombas em paralelo dobram a vazão no sistema.</li><li>Multiplicar pelo rendimento em vez de dividir.</li><li>Fechar a válvula na descarga muda a curva do sistema, não a da bomba.</li></ul>"""),

"Vibrações": dict(slug="questoes-de-vibracoes", cover=("Vibrações", "4 questões comentadas"),
 resumo="""<p>Vibrações costuma ter poucas questões, mas fáceis de pontuar para quem domina o sistema massa-mola-amortecedor: frequência natural, amortecimento, associação de molas e isolamento.</p>
<h3>Fórmulas que você precisa saber de cor</h3>
""" + F("<b>Frequência natural:</b> ω<sub>n</sub> = √(k/m) em rad/s · f<sub>n</sub> = ω<sub>n</sub>/2π em Hz") + F("<b>Molas:</b> série 1/k<sub>eq</sub> = Σ1/k<sub>i</sub> · paralelo k<sub>eq</sub> = Σk<sub>i</sub>") + F("<b>Amortecimento crítico:</b> c<sub>c</sub> = 2√(km) = 2mω<sub>n</sub> · ζ = c/c<sub>c</sub>") + F("<b>Isolamento:</b> transmissibilidade &lt; 1 só para ω/ω<sub>n</sub> &gt; √2") + """
<h3>Pegadinhas da banca</h3>
<ul><li>Responder em rad/s quando a pergunta pede hertz.</li><li>Molas em série deixam o sistema mais macio, e a frequência cai por √2.</li><li>Na região de isolamento, mais amortecimento piora o isolamento.</li></ul>"""),

"Fabricação e Soldagem": dict(slug="questoes-de-fabricacao-e-soldagem", cover=("Fabricação e Soldagem", "4 questões comentadas"),
 resumo="""<p>Na área de Fabricação, a prova cobra processos de soldagem, soldabilidade dos aços, usinagem e conformação mecânica. Para a Petrobras e a Transpetro, soldagem é especialmente importante pela relação com dutos e vasos de pressão.</p>
<h3>O que você precisa saber</h3>
""" + F("<b>Usinagem:</b> V<sub>c</sub> = πDn/1.000 (V<sub>c</sub> em m/min, D em mm)") + F("<b>Carbono equivalente (IIW):</b> CE = C + Mn/6 + (Cr+Mo+V)/5 + (Ni+Cu)/15; acima de ~0,40 a 0,45, cuidado com preaquecimento e hidrogênio") + F("<b>Processos:</b> TIG com eletrodo de tungstênio não consumível; MIG com gás inerte e MAG com gás ativo; eletrodo revestido gera escória; arco submerso nas posições plana e horizontal") + F("<b>Conformação:</b> trabalho a frio encrua (sobe escoamento, cai ductilidade); o recozimento de recristalização restaura a ductilidade") + """
<h3>Pegadinhas da banca</h3>
<ul><li>Dizer que o eletrodo de tungstênio do TIG é consumível.</li><li>Achar que o preaquecimento acelera o resfriamento (ele desacelera).</li><li>Usar o raio no lugar do diâmetro na velocidade de corte.</li></ul>"""),
}
