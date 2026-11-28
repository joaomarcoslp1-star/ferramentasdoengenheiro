# -*- coding: utf-8 -*-
# Lote 3 (28/11/2026): Elementos de Máquinas, Transferência de Calor, Materiais, Máquinas de Fluxo, Vibrações, Fabricação
import math
from nbase import num, con, br

E = "Elementos de Máquinas"
s = 120000 / (10 * 100)
num("MEC-E29", E, "Solda de topo à tração",
    "Duas chapas de 10 mm de espessura e 100 mm de largura são unidas por solda de topo com penetração total e tracionadas por 120 kN. A tensão normal na solda, em MPa, é",
    s, [s / 0.707, s / 2, 2 * s, 12], d=0,
    res=f"Na solda de topo com penetração total, a garganta é a própria espessura da chapa: σ = F/(t·L) = 120.000/(10 × 100) = <b>{br(s,0)} MPa</b>. O fator 0,707 é da solda de filete, não da de topo.")

Fi = 0.75 * 84.3 * 600 / 1000
num("MEC-E30", E, "Pré-carga recomendada em parafuso",
    "Para uma junta reutilizável, recomenda-se pré-carga igual a 75% da carga de prova do parafuso. Um parafuso M12 (A<sub>t</sub> = 84,3 mm²) da classe 8.8 tem resistência de prova de 600 MPa. A pré-carga recomendada, em kN, é, aproximadamente,",
    Fi, [84.3 * 600 / 1000, 0.75 * 113 * 600 / 1000, 0.75 * 84.3 * 800 / 1000, Fi / 2], d=1,
    res=f"F<sub>i</sub> = 0,75·A<sub>t</sub>·S<sub>p</sub> = 0,75 × 84,3 × 600 = 37.935 N ≈ <b>{br(Fi,1)} kN</b>. Para juntas permanentes, usa-se até 90% da carga de prova. A carga de prova (600 MPa) é menor que o limite de resistência (800 MPa).")

con("MEC-E31", E, "Engrenagens cônicas",
    "Para transmitir movimento entre dois eixos concorrentes (que se cruzam), em geral a 90°, o tipo de engrenagem indicado é",
    "a cônica",
    ["a cilíndrica de dentes retos",
     "a cilíndrica helicoidal de eixos paralelos",
     "a cremalheira",
     "a interna (anelar)"],
    res="Engrenagens <b>cônicas</b> trabalham com eixos concorrentes, como no diferencial de veículos. Cilíndricas (retas e helicoidais) ligam eixos paralelos; eixos reversos (que não se cruzam) usam coroa e sem-fim, helicoidais cruzadas ou hipoides.")

n2 = 1750 / (50 / 2)
num("MEC-E32", E, "Rotação de saída com sem-fim de várias entradas",
    "Um parafuso sem-fim de duas entradas, girando a 1.750 rpm, aciona uma coroa de 50 dentes. A rotação da coroa, em rpm, é",
    n2, [35, 140, 1750 / 2, 17.5], d=0,
    res=f"Cada volta do sem-fim avança tantos dentes quantas forem as entradas: i = z<sub>coroa</sub>/entradas = 50/2 = 25. n = 1.750/25 = <b>{br(n2,0)} rpm</b>. Tratar o sem-fim como de uma entrada dá 35 rpm.")

C, D, d = 500, 300, 100
L = 2 * C + math.pi * (D + d) / 2 + (D - d) ** 2 / (4 * C)
num("MEC-E33", E, "Comprimento de correia aberta",
    "Duas polias de 300 mm e 100 mm de diâmetro têm entre centros de 500 mm e são ligadas por correia aberta. Com L ≈ 2C + π(D + d)/2 + (D − d)²/(4C), o comprimento da correia, em mm, é, aproximadamente,",
    L, [2 * C + math.pi * (D + d), 2 * C + math.pi * (D + d) / 2, 2 * C + math.pi * (D + d) / 2 + (D - d) ** 2 / C, 1257], d=0,
    res=f"L = 2 × 500 + π × 400/2 + 200²/(4 × 500) = 1.000 + 628 + 20 = <b>{br(L,0)} mm</b>. O último termo corrige a diferença de diâmetros. Usar π(D + d) sem dividir por 2 conta a circunferência inteira de cada polia.")

Fu = 5000 / 10
num("MEC-E34", E, "Força útil em correia",
    "Uma transmissão por correia transmite 5 kW com velocidade da correia de 10 m/s. A força útil (diferença entre as forças nos ramos tenso e frouxo), em N, é",
    Fu, [50, 5000, 250, 1000], d=0,
    res=f"P = (T<sub>1</sub> − T<sub>2</sub>)·v → F<sub>u</sub> = 5.000/10 = <b>{br(Fu,0)} N</b>. Com a relação de Euler (T<sub>1</sub>/T<sub>2</sub> = e<sup>μθ</sup>), obtêm-se depois as forças em cada ramo e a força nos mancais.")

con("MEC-E35", E, "Mancal de deslizamento hidrodinâmico",
    "Num mancal de deslizamento hidrodinâmico (radial, lubrificado a óleo), a película que separa o eixo da bucha se forma",
    "pela rotação do eixo, que arrasta o óleo para a região convergente (cunha de óleo) e gera a pressão que sustenta a carga",
    ["por uma bomba externa de alta pressão, mesmo com o eixo parado",
     "apenas quando o eixo está parado",
     "pela dilatação térmica da bucha",
     "por esferas de aço entre o eixo e a bucha"],
    res="O eixo gira excêntrico e arrasta o óleo para uma folga que se estreita: a <b>cunha de óleo</b> gera pressão. Na partida e na parada, com baixa rotação, há contato metálico, e por isso grandes máquinas usam injeção de óleo na partida (mancal híbrido). Com bomba externa permanente, o mancal seria hidrostático.")

num("MEC-E36", E, "Fator de segurança estático de rolamento",
    "Um rolamento com capacidade de carga estática C<sub>0</sub> = 20 kN suporta carga estática equivalente P<sub>0</sub> = 10 kN, quase sem rotação. O fator de segurança estático s<sub>0</sub> = C<sub>0</sub>/P<sub>0</sub> é",
    2.0, [0.5, 10, 1.0, 4.0], d=1,
    res="s<sub>0</sub> = 20/10 = <b>2,0</b>. Para rolamentos parados, oscilantes ou de giro muito lento, a seleção é pela capacidade estática (deformação permanente das pistas), e não pela vida em fadiga. Valores de s<sub>0</sub> de 1 a 2 são comuns; com cargas de choque, exige-se mais.")

Cm = 40 / 5; tau = 8 * 200 * 40 / (math.pi * 5 ** 3) * 1.18
num("MEC-E37", E, "Tensão em mola helicoidal com fator de Wahl",
    "Uma mola helicoidal de compressão tem diâmetro médio de 40 mm e arame de 5 mm, e recebe força de 200 N. Com τ = K<sub>w</sub>·8FD/(πd³) e fator de Wahl K<sub>w</sub> ≈ 1,18 (índice 8), a tensão máxima de cisalhamento no arame, em MPa, é, aproximadamente,",
    tau, [tau / 1.18, tau * 2, tau / 2, 8 * 200 * 40 / (math.pi * 5 ** 3) * 1.18 / 8], d=0,
    res=f"8FD/(πd³) = 8 × 200 × 40/(π × 125) = 163 MPa. Com o fator de Wahl (curvatura e cisalhamento direto): τ = 1,18 × 163 = <b>{br(tau,0)} MPa</b>. Esquecer o K<sub>w</sub> subestima a tensão na face interna da espira.")

Tt = 0.15 * 30 * math.pi * 50 ** 2 * 60 / 2 / 1e6
num("MEC-E38", E, "Torque transmitido por ajuste prensado",
    "Um cubo é montado com interferência num eixo de 50 mm, com comprimento de contato de 60 mm, gerando pressão de contato de 30 MPa. Com coeficiente de atrito 0,15 e T = μ·p·π·d²·L/2, o torque transmissível, em kN·m, é, aproximadamente,",
    Tt, [2 * Tt, Tt / 2, Tt / 0.15, 0.106], d=2,
    res=f"Força de atrito: μ·p·(πdL) = 0,15 × 30 × π × 50 × 60 = 42.412 N. Torque: × d/2 = 42.412 × 25 = 1,06 × 10⁶ N·mm = <b>{br(Tt,2)} kN·m</b>. O ajuste prensado dispensa chaveta e não enfraquece o eixo com rasgos.")

con("MEC-E39", E, "Classe de resistência de parafusos",
    "Um parafuso métrico da classe de resistência 8.8 tem, aproximadamente,",
    "limite de resistência de 800 MPa e limite de escoamento de 640 MPa (80% de 800)",
    ["limite de resistência de 88 MPa",
     "limite de escoamento de 800 MPa e limite de resistência de 880 MPa",
     "diâmetro nominal de 8 mm e passo de 0,8 mm",
     "dureza de 88 HRC"],
    res="Na classe X.Y: X × 100 = limite de resistência (8 × 100 = <b>800 MPa</b>); Y/10 é a razão escoamento/resistência (0,8 × 800 = <b>640 MPa</b>). Assim, 10.9 tem 1.000 e 900 MPa, e 12.9, 1.200 e 1.080 MPa.")

Me = math.sqrt(3 ** 2 + 4 ** 2)
num("MEC-E40", E, "Momento equivalente em eixo (flexo-torção)",
    "Uma seção de eixo está submetida a momento fletor de 3 kN·m e torque de 4 kN·m. Pelo critério de Tresca, o momento equivalente M<sub>eq</sub> = √(M² + T²), em kN·m, é",
    Me, [7, 1, 3.5, 25], d=1,
    res=f"M<sub>eq</sub> = √(3² + 4²) = √25 = <b>{br(Me,1)} kN·m</b>. Com ele, o diâmetro sai de d³ = 32·n·M<sub>eq</sub>/(π·σ<sub>e</sub>). Somar M + T (7) não tem fundamento; pelo critério de von Mises, usa-se √(M² + 0,75T²).")

C = "Transferência de Calor"
Tq = 100 - (100 - 20) / 4
num("MEC-C27", C, "Perfil de temperatura em parede plana",
    "Uma parede plana homogênea, sem geração interna de calor e em regime permanente, tem uma face a 100 °C e a outra a 20 °C. A temperatura num plano situado a 1/4 da espessura, medido a partir da face quente, em °C, é",
    Tq, [60, 40, 25, 75], d=0,
    res=f"Sem geração e com k constante, o perfil é <b>linear</b>: T = 100 − (100 − 20) × 1/4 = <b>{br(Tq,0)} °C</b>. Numa parede cilíndrica, o perfil seria logarítmico.")

Nu = 0.023 * 1e4 * 2; h = Nu * 0.6 / 0.05
num("MEC-C28", C, "Correlação de Dittus-Boelter",
    "Água (k = 0,6 W/m·K) escoa em regime turbulento num tubo de 50 mm. Pela correlação Nu = 0,023·Re<sup>0,8</sup>·Pr<sup>0,4</sup>, com Re<sup>0,8</sup> = 10⁴ e Pr<sup>0,4</sup> = 2, o coeficiente de convecção, em W/m²·K, é",
    h, [Nu, h / 2, 2 * h, Nu * 0.6], d=0,
    res=f"Nu = 0,023 × 10⁴ × 2 = 460. h = Nu·k/D = 460 × 0,6/0,05 = <b>{br(h,0)} W/m²·K</b>. Água em convecção forçada costuma ficar na faixa de milhares de W/m²·K.")

con("MEC-C29", C, "Superfície seletiva de coletor solar",
    "Para a placa absorvedora de um coletor solar térmico, a superfície ideal (seletiva) deve ter",
    "alta absortividade na faixa solar (ondas curtas) e baixa emissividade no infravermelho (ondas longas)",
    ["baixa absortividade solar e alta emissividade no infravermelho",
     "absortividade e emissividade iguais a 1 em todos os comprimentos de onda",
     "alta refletividade em todos os comprimentos de onda",
     "emissividade alta e absortividade nula"],
    res="O Sol emite em torno de 0,5 µm; a placa a 80 °C emite em torno de 8 µm. Uma superfície <b>seletiva</b> (α<sub>solar</sub> ≈ 0,95; ε<sub>IV</sub> ≈ 0,1) absorve quase toda a radiação solar e perde pouco por radiação. Kirchhoff (α = ε) vale para cada comprimento de onda, não para faixas diferentes.")

NTU = 500 * 10 / 2500
num("MEC-C30", C, "Número de unidades de transferência",
    "Um trocador de calor tem coeficiente global de 500 W/m²·K e 10 m² de área. A menor taxa de capacidade térmica dos fluidos é 2.500 W/K. O NTU do trocador é",
    NTU, [0.5, 4, 20, 1.0], d=1,
    res=f"NTU = UA/C<sub>mín</sub> = 500 × 10/2.500 = <b>{br(NTU,1)}</b>. Com o NTU e a razão C<sub>mín</sub>/C<sub>máx</sub>, tira-se a efetividade das curvas ou fórmulas do arranjo de escoamento.")

con("MEC-C31", C, "Condutividade térmica dos materiais",
    "A sequência que ordena corretamente os materiais em ordem DECRESCENTE de condutividade térmica, à temperatura ambiente, é",
    "cobre, aço-carbono, vidro, água, ar",
    ["aço-carbono, cobre, água, vidro, ar",
     "cobre, vidro, aço-carbono, ar, água",
     "ar, água, vidro, aço-carbono, cobre",
     "vidro, cobre, aço-carbono, água, ar"],
    res="Valores típicos (W/m·K): <b>cobre ≈ 400; aço-carbono ≈ 50; vidro ≈ 1; água ≈ 0,6; ar ≈ 0,026</b>. Os isolantes funcionam prendendo ar parado em poros pequenos.")

t = 50 * 4.18 * 40 / 2 / 60
num("MEC-C32", C, "Tempo de aquecimento",
    "Um aquecedor elétrico de 2 kW aquece 50 L de água (c = 4,18 kJ/kg·K) de 20 °C para 60 °C. Desprezando perdas, o tempo necessário, em minutos, é, aproximadamente,",
    t, [t * 60, t / 2, 2 * t, t * 1.5], d=0,
    res=f"Energia: Q = mcΔT = 50 × 4,18 × 40 = 8.360 kJ. Tempo: 8.360/2 = 4.180 s = <b>{br(t,0)} min</b>. Não esquecer de converter segundos em minutos.")

qn = 5.67e-8 * (600 ** 4 - 300 ** 4); q = qn / (1 / 0.5 + 1 / 0.5 - 1)
num("MEC-C33", C, "Radiação entre placas cinzentas",
    "Duas placas paralelas, muito grandes e cinzentas, com emissividade 0,5 cada, estão a 600 K e 300 K. Com σ = 5,67 × 10<sup>−8</sup> W/m²·K⁴ e 600⁴ − 300⁴ = 1,215 × 10¹¹ K⁴, o fluxo líquido de calor por radiação, em W/m², é, aproximadamente,",
    q, [qn, qn * 0.25, qn * 0.5, qn * 0.5 * 0.5 * 2], d=0,
    res=f"q = σ(T<sub>1</sub>⁴ − T<sub>2</sub>⁴)/(1/ε<sub>1</sub> + 1/ε<sub>2</sub> − 1) = 6.889/(2 + 2 − 1) = 6.889/3 = <b>{br(q,0)} W/m²</b>. Multiplicar pelas emissividades (0,5 × 0,5) erra: o fator certo vem das reflexões múltiplas entre as placas.")

con("MEC-C34", C, "Condensação em gotas e em película",
    "Na condensação de vapor sobre uma superfície fria, a condensação em gotas, em comparação com a condensação em película,",
    "apresenta coeficientes de transferência de calor muito maiores, pois grande parte da superfície fica exposta diretamente ao vapor",
    ["apresenta coeficientes menores, pois as gotas isolam a superfície",
     "ocorre em superfícies que o condensado molha bem",
     "é a forma mais comum e estável na indústria",
     "não envolve liberação de calor latente"],
    res="Na condensação em <b>gotas</b>, que ocorre em superfícies que o condensado não molha, o h pode ser 10 vezes maior, porque não há um filme líquido contínuo atrapalhando. Ela é difícil de manter por muito tempo; por isso os projetos industriais consideram condensação em película (Nusselt).")

qt = 0.5 * 20 * 20 + 5 * 4 * 20
num("MEC-C35", C, "Resistências térmicas em paralelo",
    "Uma fachada tem 20 m² de parede (U = 0,5 W/m²·K) e 4 m² de janela de vidro simples (U = 5 W/m²·K), com 20 °C de diferença entre dentro e fora. A perda total de calor, em W, é",
    qt, [0.5 * 24 * 20, 5 * 24 * 20, 200, 400], d=0,
    res=f"Parede e janela são caminhos em paralelo: q = Σ U·A·ΔT = 0,5 × 20 × 20 + 5 × 4 × 20 = 200 + 400 = <b>{br(qt,0)} W</b>. A janela, com só 1/6 da área, perde o dobro da parede.")

M = "Materiais e Tratamentos Térmicos"
sv = 400 * 1.25
num("MEC-M28", M, "Tensão verdadeira",
    "Num ensaio de tração, antes da estricção, a tensão de engenharia é 400 MPa e a deformação de engenharia é 0,25. Considerando volume constante, a tensão verdadeira, em MPa, é",
    sv, [400, 320, 400 * math.log(1.25) + 400, 600], d=0,
    res=f"Com volume constante, a área real é A<sub>0</sub>/(1 + ε). Logo σ<sub>v</sub> = σ(1 + ε) = 400 × 1,25 = <b>{br(sv,0)} MPa</b>. A curva verdadeira fica sempre acima da de engenharia.")

al = (62 - 50) / 50 * 100
num("MEC-M29", M, "Alongamento após ruptura",
    "Um corpo de prova com comprimento útil inicial de 50 mm mede 62 mm após a ruptura, juntando-se as partes. O alongamento percentual é",
    al, [12, 19.4, 80.6, 62], fmt=lambda v: br(v, 1) + "%",
    res=f"A = (L<sub>f</sub> − L<sub>0</sub>)/L<sub>0</sub> = 12/50 = <b>{br(al,1)}%</b>. Dividir pelo comprimento final (19,4%) está errado. O alongamento é uma medida de ductilidade e depende do comprimento de referência usado (por isso a norma o fixa).")

ra = (1 - (7 / 10) ** 2) * 100
num("MEC-M30", M, "Redução de área (estricção)",
    "Um corpo de prova cilíndrico de 10 mm de diâmetro rompe com diâmetro de 7 mm na seção de fratura. A redução de área percentual é",
    ra, [30, 49, 70, 42.9, 65.7, 75], fmt=lambda v: br(v, 0) + "%",
    res=f"Z = 1 − (d<sub>f</sub>/d<sub>0</sub>)² = 1 − 0,49 = <b>{br(ra,0)}%</b>. Usar a redução de diâmetro (30%) esquece que a área varia com o quadrado. Reduções de área altas indicam fratura dúctil.")

con("MEC-M31", M, "Ponto eutético do diagrama Fe-C",
    "No diagrama ferro-carbono (Fe-Fe<sub>3</sub>C), o ponto eutético ocorre a cerca de",
    "4,3% C e 1.148 °C, onde o líquido se transforma em ledeburita (austenita + cementita)",
    ["0,76% C e 727 °C, onde a austenita se transforma em perlita",
     "2,1% C e 1.148 °C, limite entre aço e ferro fundido no líquido",
     "0,022% C e 727 °C, máxima solubilidade do carbono na ferrita",
     "6,7% C, composição da cementita pura"],
    res="<b>Eutético</b>: líquido → sólido + sólido, a 4,3% C e 1.148 °C (ledeburita). O <b>eutetoide</b> é sólido → sólido, a 0,76% C e 727 °C (perlita). 2,1% C é a máxima solubilidade do carbono na austenita (a fronteira aço/ferro fundido); 0,022%, na ferrita.")

con("MEC-M32", M, "Corrosão sob tensão",
    "A corrosão sob tensão (CST) de aços inoxidáveis austeníticos, como o 304, é favorecida pela combinação de",
    "tensões de tração (aplicadas ou residuais), meio com cloretos e temperatura elevada (acima de cerca de 60 °C)",
    ["tensões de compressão e meio seco",
     "baixa temperatura e meio alcalino isento de cloretos",
     "ausência de tensões, apenas meio ácido",
     "contato com zinco em atmosfera rural"],
    res="A <b>CST</b> exige três fatores simultâneos: material suscetível, meio específico (cloretos para inox austenítico) e tensão de tração. As trincas são finas e ramificadas e podem romper equipamentos sem corrosão generalizada visível. Combate-se com alívio de tensões, inox duplex ou controle do meio.")

con("MEC-M33", M, "Curva S-N e limite de fadiga",
    "Sobre a curva S-N (tensão × número de ciclos) obtida em ensaios de fadiga, é correto afirmar que",
    "aços costumam apresentar limite de fadiga (patamar abaixo do qual a vida é muito longa), enquanto ligas de alumínio não apresentam patamar definido",
    ["ligas de alumínio têm limite de fadiga bem definido, e os aços não",
     "a vida em fadiga aumenta com a tensão alternada",
     "a fadiga só ocorre com tensões acima do limite de escoamento",
     "a curva S-N independe do acabamento superficial"],
    res="Aços: a curva achata a partir de 10⁶ a 10⁷ ciclos (<b>limite de fadiga</b>). Alumínio: a curva continua caindo, e por isso se especifica a resistência à fadiga para um número de ciclos (por exemplo, 5 × 10⁸). A fadiga acontece abaixo do escoamento, e o acabamento superficial pesa muito.")

Ec = 0.6 * 230 + 0.4 * 3
num("MEC-M34", M, "Regra das misturas em compósitos",
    "Um compósito unidirecional tem 60% em volume de fibras de carbono (E = 230 GPa) numa matriz epóxi (E = 3 GPa). Pela regra das misturas, o módulo na direção das fibras, em GPa, é, aproximadamente,",
    Ec, [116.5, 230, 0.6 * 230, 7.4], d=1,
    res=f"E<sub>c</sub> = V<sub>f</sub>E<sub>f</sub> + V<sub>m</sub>E<sub>m</sub> = 0,6 × 230 + 0,4 × 3 = 138 + 1,2 = <b>{br(Ec,1)} GPa</b>. Na direção transversal, as fases ficam em série, e o módulo cai para cerca de 7 GPa: o compósito é muito anisotrópico.")

con("MEC-M35", M, "Comportamento mecânico dos cerâmicos",
    "Os materiais cerâmicos de engenharia (alumina, carbeto de silício, nitreto de silício) caracterizam-se por",
    "alta dureza e resistência ao desgaste, fratura frágil e resistência à compressão muito maior que à tração",
    ["alta ductilidade e boa tenacidade à fratura",
     "resistência à tração muito maior que à compressão",
     "baixa temperatura de fusão",
     "boa condutividade elétrica, semelhante à dos metais"],
    res="As ligações iônicas e covalentes dão aos cerâmicos <b>dureza e refratariedade</b>, mas impedem o movimento de discordâncias: a fratura é frágil e muito sensível a defeitos. Na compressão, os defeitos se fecham, e a resistência pode ser de 5 a 10 vezes maior que na tração.")

con("MEC-M36", M, "Aços microligados (ARBL)",
    "Os aços de alta resistência e baixa liga (ARBL) microligados, com pequenas adições de nióbio, vanádio ou titânio, obtêm alta resistência principalmente por",
    "refino de grão e precipitação de carbonitretos finos, mantendo baixo carbono e boa soldabilidade",
    ["alto teor de carbono e têmpera em água",
     "formação de martensita na laminação",
     "grandes adições de cromo e níquel, como os inoxidáveis",
     "encruamento severo a frio após a laminação"],
    res="Com 0,01% a 0,1% de Nb, V ou Ti e laminação controlada, os <b>carbonitretos</b> impedem o crescimento do grão e endurecem por precipitação. Como o carbono é baixo, a soldabilidade é boa. São os aços de tubos API, pontes e chassis.")

B = "Máquinas de Fluxo"
z = 10.33 - 0.24 - 1.0 - 3.0
num("MEC-B27", B, "Altura máxima de sucção",
    "Uma bomba aspira água fria de um reservatório aberto. Dados: pressão atmosférica de 10,33 m de coluna d'água, pressão de vapor de 0,24 m, perda de carga na sucção de 1,0 m e NPSH requerido de 3,0 m. A altura máxima de instalação da bomba acima do nível da água, em m, é, aproximadamente,",
    z, [10.33, 10.33 - 3, 10.33 - 0.24 - 1.0, 10.33 - 0.24 + 1 - 3], d=2,
    res=f"NPSH<sub>d</sub> = p<sub>atm</sub>/γ − z − h<sub>f</sub> − p<sub>v</sub>/γ ≥ NPSH<sub>r</sub>. z<sub>máx</sub> = 10,33 − 1,0 − 0,24 − 3,0 = <b>{br(z,2)} m</b>. Na prática, soma-se uma margem de segurança ao NPSH<sub>r</sub>, e a altura fica ainda menor.")

w = 1.005 * 300 * (1.486 - 1)
num("MEC-B28", B, "Trabalho de compressão isentrópica",
    "Ar (c<sub>p</sub> = 1,005 kJ/kg·K; k = 1,4) entra num compressor ideal a 300 K e é comprimido com razão de pressões 4. Dado 4<sup>0,286</sup> ≈ 1,486, o trabalho específico de compressão, em kJ/kg, é, aproximadamente,",
    w, [1.005 * 300 * 1.486, 0.718 * 300 * 0.486, 0.287 * 300 * math.log(4), 1.005 * 300 * 3], d=0,
    res=f"T<sub>2s</sub> = 300 × 1,486 = 445,8 K. w = c<sub>p</sub>(T<sub>2s</sub> − T<sub>1</sub>) = 1,005 × 145,8 = <b>{br(w,0)} kJ/kg</b>. A compressão isotérmica gastaria menos: RT·ln 4 = 119 kJ/kg.")

Pe = 0.5 * 1.2 * 1000 * 10 ** 3 * 0.4 / 1000
num("MEC-B29", B, "Potência de turbina eólica",
    "Uma turbina eólica tem área varrida de 1.000 m² e opera com vento de 10 m/s (ρ = 1,2 kg/m³) e coeficiente de potência de 0,4. A potência extraída, em kW, é",
    Pe, [Pe / 0.4, Pe / 10, 2 * Pe, Pe * 0.593 / 0.4], d=0,
    res=f"P = ½ρAV³·C<sub>p</sub> = 0,5 × 1,2 × 1.000 × 1.000 × 0,4 = 240.000 W = <b>{br(Pe,0)} kW</b>. A potência cresce com o cubo do vento, e o limite teórico de C<sub>p</sub> é o de Betz, 16/27 ≈ 0,593.")

con("MEC-B30", B, "Turbina Kaplan",
    "A principal vantagem da turbina Kaplan sobre a turbina hélice de pás fixas é",
    "manter rendimento elevado numa larga faixa de vazões, graças ao ajuste do ângulo das pás do rotor em conjunto com o distribuidor",
    ["operar com quedas muito altas, acima de 500 m",
     "dispensar o tubo de sucção",
     "ser uma turbina de ação, como a Pelton",
     "não estar sujeita à cavitação"],
    res="A <b>Kaplan</b> é axial, de reação, para quedas baixas e grandes vazões. Com pás móveis (dupla regulação), a curva de rendimento fica achatada; a hélice fixa só rende bem perto da vazão de projeto. Ambas estão sujeitas à cavitação e usam tubo de sucção.")

con("MEC-B31", B, "Controle de vazão por inversor de frequência",
    "Para reduzir a vazão de uma bomba centrífuga num sistema com perdas predominantemente dinâmicas (pouca altura estática), o método mais eficiente em energia é",
    "reduzir a rotação com inversor de frequência, pois a potência cai aproximadamente com o cubo da rotação",
    ["estrangular a válvula de descarga, que reduz a potência na mesma proporção da vazão",
     "estrangular a válvula de sucção",
     "abrir um desvio (bypass) da descarga para a sucção",
     "aumentar o diâmetro do rotor"],
    res="O estrangulamento desloca o ponto de operação na curva da bomba e dissipa energia na válvula. O <b>inversor</b> move a própria curva da bomba: com sistema dinâmico, 80% da vazão exige cerca de 51% da potência (0,8³). Estrangular a sucção ainda provoca cavitação, e o bypass desperdiça energia.")

dp = 1000 * 9.81 * 50 / 1000
num("MEC-B32", B, "Conversão de altura manométrica em pressão",
    "Uma bomba fornece altura manométrica de 50 m ao bombear água (ρ = 1.000 kg/m³; g = 9,81 m/s²). O aumento de pressão correspondente, em kPa, é, aproximadamente,",
    dp, [50, 5.1, 4905, dp / 2], d=0,
    res=f"Δp = ρgH = 1.000 × 9,81 × 50 = <b>{br(dp,0)} kPa</b>, cerca de 4,9 bar. Regra prática: 10 m de coluna d'água ≈ 1 bar ≈ 100 kPa.")

con("MEC-B33", B, "Turbinas a vapor de ação e de reação",
    "Numa turbina a vapor de ação (impulso), como a de Laval ou o estágio Curtis, a expansão do vapor ocorre",
    "inteiramente nos bocais fixos, e o rotor recebe o vapor a pressão praticamente constante, aproveitando só a energia cinética",
    ["inteiramente nas palhetas móveis, como num bocal rotativo",
     "metade nos bocais fixos e metade nas palhetas móveis, por definição",
     "apenas no condensador",
     "sem queda de pressão em nenhuma parte"],
    res="Na <b>ação</b>, toda a queda de pressão acontece nos bocais e as palhetas só desviam o jato (grau de reação zero). Na <b>reação</b> (Parsons, com grau de reação 50%), metade da expansão ocorre também nas palhetas móveis, que funcionam como bocais.")

con("MEC-B34", B, "Operação abaixo da vazão mínima",
    "Operar uma bomba centrífuga por longos períodos com vazão muito abaixo do ponto de melhor eficiência (BEP) pode causar",
    "recirculação interna, aquecimento do líquido, vibração e esforços radiais elevados, reduzindo a vida de selos e mancais",
    ["aumento do rendimento, pois a potência absorvida é menor",
     "redução do NPSH requerido, eliminando qualquer risco",
     "sobrecarga do motor por excesso de vazão",
     "aumento da vazão por efeito de sifão"],
    res="Longe do <b>BEP</b>, o fluxo descola das pás e recircula na entrada e na saída do rotor, com cavitação por recirculação, aquecimento (a energia vira calor no pouco líquido que passa) e forças radiais desequilibradas. Os fabricantes definem uma vazão mínima contínua, garantida às vezes por linha de recirculação.")

num("MEC-B35", B, "Semelhança geométrica de bombas",
    "Uma bomba é construída em escala, com todas as dimensões dobradas (inclusive o rotor), e opera na mesma rotação, em ponto homólogo. Pelas leis de semelhança, a vazão fica multiplicada por",
    8, [2, 4, 16, 32], d=0,
    res="Para máquinas semelhantes: Q ∝ nD³, H ∝ n²D² e P ∝ ρn³D⁵. Com n constante e D dobrado: Q × 2³ = <b>8</b>, H × 4 e P × 32. A regra de corte de rotor (Q ∝ D) vale só para pequenas usinagens no mesmo corpo de bomba.")

V = "Vibrações"
k = 200 * 200 / 400 + 100
num("MEC-V19", V, "Associação mista de molas",
    "Duas molas de 200 N/mm, ligadas em série, trabalham em paralelo com uma terceira mola de 100 N/mm. A rigidez equivalente do conjunto, em N/mm, é",
    k, [500, 300, 66.7, 150], d=0,
    res=f"Série: 200 × 200/(200 + 200) = 100 N/mm. Paralelo com a terceira: 100 + 100 = <b>{br(k,0)} N/mm</b>. Em série, somam-se as flexibilidades (1/k); em paralelo, as rigidezes.")

con("MEC-V20", V, "Fase na ressonância",
    "Num sistema massa-mola com amortecimento viscoso, excitado por força harmônica, o ângulo de fase entre a força e o deslocamento quando a frequência de excitação é igual à frequência natural é",
    "90°, independentemente do valor do amortecimento",
    ["0°, pois a força e o deslocamento ficam em fase",
     "180°, pois a massa vibra em oposição à força",
     "45°, para qualquer amortecimento",
     "dependente apenas da massa"],
    res="Abaixo da ressonância, a fase tende a 0°; acima, a 180°; <b>na ressonância, é 90°</b> para qualquer ζ. Essa virada de fase é usada em campo para identificar ressonâncias, por exemplo durante a partida de uma máquina.")

k = 200e9 * 100e-6 / 1.0; fa = math.sqrt(k / 50) / (2 * math.pi)
num("MEC-V21", V, "Vibração axial de barra com massa",
    "Uma massa de 50 kg está presa na ponta de uma barra de aço (E = 200 GPa) com 100 mm² de seção e 1 m de comprimento, que vibra axialmente. Desprezando a massa da barra, a frequência natural, em Hz, é, aproximadamente,",
    fa, [math.sqrt(k / 50), fa / math.sqrt(1000), 2 * fa, fa / 2], d=0,
    res=f"Rigidez axial: k = EA/L = 200 × 10⁹ × 100 × 10<sup>−6</sup>/1 = 2 × 10⁷ N/m. ω<sub>n</sub> = √(k/m) = √(4 × 10⁵) = 632 rad/s → f<sub>n</sub> = <b>{br(fa,0)} Hz</b>. Barras são muito mais rígidas axialmente que à flexão.")

rms = 10 / math.sqrt(2)
num("MEC-V22", V, "Valor RMS de sinal senoidal",
    "Um sinal de velocidade de vibração senoidal tem valor de pico de 10 mm/s. Seu valor RMS (eficaz), em mm/s, é, aproximadamente,",
    rms, [10, 5, 6.37, 20], d=2,
    res=f"Para senoide pura, RMS = pico/√2 = 10/1,414 = <b>{br(rms,2)} mm/s</b>. 6,37 é o valor médio retificado (2/π × pico); 14,1 seria pico × √2. As normas de severidade (ISO 10816/20816) usam a velocidade RMS.")

d = 9.81 / (2 * math.pi * 5) ** 2 * 1000
num("MEC-V23", V, "Deflexão estática de isolador",
    "Deseja-se que uma máquina montada sobre isoladores elásticos tenha frequência natural vertical de 5 Hz. Com g = 9,81 m/s², a deflexão estática dos isoladores sob o peso da máquina, em mm, deve ser, aproximadamente,",
    d, [d / 4, 4 * d, 1.0, 50], d=1,
    res=f"ω<sub>n</sub> = √(g/δ) → δ = g/ω<sub>n</sub>² = 9,81/(2π × 5)² = 9,81/987 = 0,00994 m ≈ <b>{br(d,1)} mm</b>. Para isolar bem uma máquina de 1.800 rpm (30 Hz), 5 Hz dá relação de frequências 6, bem acima de √2.")

num("MEC-V24", V, "Batimento",
    "Duas máquinas próximas vibram em 50 Hz e 52 Hz, com amplitudes semelhantes. O sinal medido entre elas apresenta batimento, com a amplitude oscilando a uma frequência, em Hz, de",
    2, [51, 102, 1, 4], d=0,
    res="A soma de duas senoides próximas oscila na média (51 Hz), com envoltória que pulsa na <b>diferença</b>: 52 − 50 = 2 Hz (o \"ronco\" periódico). Na partida de máquinas iguais, as rotações próximas produzem esse efeito.")

bpf = 6 * 1200 / 60
num("MEC-V25", V, "Frequência de passagem de pás",
    "Um ventilador com 6 pás gira a 1.200 rpm. A frequência de passagem de pás, típica no espectro de vibração e ruído, em Hz, é",
    bpf, [20, 1200, 7200, 60], d=0,
    res=f"BPF = número de pás × rotação em Hz = 6 × (1.200/60) = 6 × 20 = <b>{br(bpf,0)} Hz</b>. Amplitudes altas na BPF indicam folga pequena entre rotor e carcaça, obstrução ou problemas de fluxo.")

P = "Fabricação e Soldagem"
con("MEC-P20", P, "Funções do fluido de corte",
    "Na usinagem com altas velocidades de corte, a função predominante do fluido de corte é",
    "a refrigeração da ferramenta e da peça, pois há pouco tempo para o lubrificante penetrar na interface cavaco-ferramenta",
    ["a lubrificação, que é mais eficaz quanto maior a velocidade",
     "aumentar o atrito para quebrar o cavaco",
     "proteger a máquina contra pintura",
     "aumentar a temperatura de corte para amolecer o material"],
    res="Em velocidades baixas (rosqueamento, brochamento), a <b>lubrificação</b> domina e se usam óleos integrais. Em velocidades altas, o fluido não chega à zona de contato, e a função principal passa a ser a <b>refrigeração</b>, com emulsões e soluções aquosas. O fluido também ajuda a retirar cavacos e protege contra corrosão.")

Ff = 100 * math.pi * 100 ** 2 / 4 / 1000
num("MEC-P21", P, "Força de forjamento",
    "Um tarugo será recalcado a quente até um diâmetro final de 100 mm. Considerando tensão de escoamento a quente de 100 MPa e desprezando o atrito, a força final de forjamento, em kN, é, aproximadamente,",
    Ff, [Ff * 4, Ff / 4, 1000, 314], d=0,
    res=f"F = σ<sub>f</sub>·A<sub>final</sub> = 100 × (π × 100²/4) = 785.398 N ≈ <b>{br(Ff,0)} kN</b>. O atrito com as matrizes aumenta bastante esse valor em peças achatadas. Por isso se usa a área final, quando a força é máxima.")

Rx = (100 / 25) ** 2
num("MEC-P22", P, "Razão de extrusão",
    "Um tarugo de 100 mm de diâmetro é extrudado para uma barra de 25 mm de diâmetro. A razão de extrusão (A<sub>0</sub>/A<sub>f</sub>) é",
    Rx, [4, 8, 32, 64], d=0,
    res=f"R = A<sub>0</sub>/A<sub>f</sub> = (100/25)² = <b>{br(Rx,0)}</b>. A deformação verdadeira é ln R = ln 16 ≈ 2,77, muito acima do que se consegue numa única passagem de trefilação.")

con("MEC-P23", P, "Zona termicamente afetada",
    "Numa junta soldada, a zona termicamente afetada (ZTA) é",
    "a região do metal de base que não se fundiu, mas teve a microestrutura e as propriedades alteradas pelo calor da soldagem",
    ["a região do metal de adição depositado e solidificado",
     "a região do metal de base que se fundiu durante a soldagem",
     "a escória que cobre o cordão",
     "a região da chapa sem nenhuma influência do calor"],
    res="A junta tem três regiões: <b>zona fundida</b> (metal de solda), <b>ZTA</b> (metal de base aquecido abaixo da fusão, com crescimento de grão, têmpera ou revenimento locais) e metal de base inalterado. Nos aços temperáveis, é na ZTA que aparecem dureza alta e trincas a frio.")

con("MEC-P24", P, "Oxicorte",
    "O processo de oxicorte é amplamente usado em aços-carbono, mas não é adequado para aço inoxidável e alumínio porque, nesses materiais,",
    "os óxidos formados são refratários (fundem acima do metal) e a reação de oxidação não se sustenta, e por isso se usa o corte a plasma",
    ["a temperatura de fusão é alta demais para a chama",
     "o oxigênio não reage com o cromo nem com o alumínio",
     "a condutividade elétrica impede o corte",
     "o metal é magnético e desvia o jato de oxigênio"],
    res="O <b>oxicorte</b> queima o ferro num jato de oxigênio, e o óxido, que funde abaixo do aço, é soprado para fora. No inox (Cr<sub>2</sub>O<sub>3</sub>) e no alumínio (Al<sub>2</sub>O<sub>3</sub>), os óxidos fundem bem acima do metal e bloqueiam a reação. Para esses materiais, usam-se plasma, laser ou jato d'água.")

con("MEC-P25", P, "Radiografia e ultrassom em soldas",
    "Para detectar trincas planas e finas numa solda de topo de chapa grossa, o ultrassom costuma ser mais eficaz que a radiografia porque",
    "a radiografia só detecta bem trincas alinhadas com o feixe de radiação, enquanto o ultrassom reflete fortemente em descontinuidades planas",
    ["a radiografia não atravessa aço",
     "o ultrassom detecta apenas defeitos superficiais",
     "a radiografia é sensível apenas a trincas transversais ao feixe",
     "o ultrassom dispensa calibração e acoplante"],
    res="Na <b>radiografia</b>, o contraste depende da diferença de espessura atravessada: poros e escória aparecem bem, mas uma trinca fina perpendicular ao feixe quase não muda essa espessura. No <b>ultrassom</b>, a trinca plana é um ótimo refletor. Por isso as normas aceitam ou exigem ultrassom em chapas grossas.")

HI = 24 * 150 / (300 / 60)
num("MEC-P26", P, "Energia de soldagem com velocidade em mm/min",
    "Uma soldagem é feita com 24 V, 150 A e velocidade de 300 mm/min. Desprezando o rendimento térmico do arco, a energia de soldagem, em J/mm, é",
    HI, [24 * 150 / 300, 24 * 150 * 300 / 60, HI / 2, 2 * HI], d=0,
    res=f"Converta a velocidade: 300 mm/min = 5 mm/s. E = V·I/v = 24 × 150/5 = <b>{br(HI,0)} J/mm</b>. Dividir por 300 sem converter dá 12 J/mm, um valor 60 vezes menor.")

num("MEC-P27", P, "Regra de Chvorinov",
    "Pela regra de Chvorinov, o tempo de solidificação de uma peça fundida é proporcional a (V/A)², em que V é o volume e A a área da superfície. Se todas as dimensões de um cubo fundido forem dobradas, o tempo de solidificação fica multiplicado por",
    4, [2, 8, 16, 1], d=0,
    res="Para o cubo de aresta a: V/A = a³/(6a²) = a/6. Dobrar a dobra o módulo V/A, e o tempo, proporcional ao quadrado, fica multiplicado por <b>4</b>. Por isso o massalote precisa de módulo maior que a peça: só assim ele solidifica por último.")
