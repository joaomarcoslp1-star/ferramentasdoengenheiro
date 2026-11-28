# -*- coding: utf-8 -*-
# Lote 4 (28/11/2026): Termodinâmica, Mecânica dos Fluidos, Resistência dos Materiais
import math
from nbase import num, con, br

T = "Termodinâmica"
con("MEC-T43", T, "Lei zero da termodinâmica",
    "A lei zero da termodinâmica, que fundamenta o uso de termômetros, afirma que",
    "se dois corpos estão em equilíbrio térmico com um terceiro, estão em equilíbrio térmico entre si",
    ["a entropia de um cristal perfeito é nula no zero absoluto",
     "a energia de um sistema isolado se conserva",
     "o calor flui espontaneamente do corpo quente para o frio",
     "é impossível atingir o zero absoluto num número finito de etapas"],
    res="A <b>lei zero</b> garante que a temperatura é uma propriedade comparável: o termômetro (terceiro corpo) entra em equilíbrio com cada sistema. A entropia nula a 0 K e a inatingibilidade do zero absoluto são a terceira lei; a conservação de energia é a primeira; o sentido do calor é a segunda.")

TK = (68 - 32) * 5 / 9 + 273.15
num("MEC-T44", T, "Conversão de escalas de temperatura",
    "Uma temperatura de 68 °F corresponde, em kelvin, a aproximadamente",
    TK, [68 + 273, (68 - 32) * 9 / 5 + 273, 20, 341], d=0,
    res=f"°C = (°F − 32) × 5/9 = 36 × 5/9 = 20 °C. K = 20 + 273,15 = <b>{br(TK,0)} K</b>. Somar 273 direto ao valor em °F (341 K) mistura as escalas.")

W = 2 * 10 * 60
num("MEC-T45", T, "Trabalho elétrico num sistema fechado",
    "Um resistor elétrico de 2 kW funciona durante 10 minutos dentro de um tanque rígido e bem isolado que contém ar. A variação de energia interna do ar, em kJ, é",
    W, [20, 2 * 10, 2 * 60, 12000], d=0,
    res=f"O trabalho elétrico entra no sistema: W = 2 kW × 600 s = 1.200 kJ. Sem calor (isolado) e sem trabalho de fronteira (rígido): ΔU = <b>{br(W,0)} kJ</b>. Não esquecer de converter minutos em segundos.")

Qc = 300 / 0.4 - 300
num("MEC-T46", T, "Calor rejeitado por uma usina",
    "Uma usina termelétrica produz 300 MW de potência líquida com rendimento térmico de 40%. A taxa de calor rejeitada no condensador, em MW, é",
    Qc, [750, 120, 300, 180], d=0,
    res=f"Calor fornecido: 300/0,4 = 750 MW. Rejeitado: 750 − 300 = <b>{br(Qc,0)} MW</b>. Para cada MW elétrico, 1,5 MW vai para a água de resfriamento ou para a atmosfera. 750 MW é o calor fornecido, não o rejeitado.")

m = 450000 / (4.18 * 10)
num("MEC-T47", T, "Vazão de água de resfriamento do condensador",
    "O condensador de uma usina rejeita 450 MW para a água de resfriamento, que se aquece 10 °C (c = 4,18 kJ/kg·K). A vazão mássica de água necessária, em kg/s, é, aproximadamente,",
    m, [450000 / 4.18, 450 / (4.18 * 10), m / 2, 2 * m], d=0,
    res=f"ṁ = Q̇/(cΔT) = 450.000 kW/(4,18 × 10) = <b>{br(m,0)} kg/s</b>, ou cerca de 10,8 m³/s. Por isso as termelétricas ficam perto de rios, do mar ou usam torres de resfriamento.")

UR = 1.5 / 3.17 * 100
num("MEC-T48", T, "Umidade relativa",
    "O ar a 25 °C tem pressão parcial de vapor de 1,5 kPa. A pressão de saturação da água a 25 °C é 3,17 kPa. A umidade relativa do ar é, aproximadamente,",
    UR, [3.17 / 1.5 * 100, 1.5, 0.622 * 1.5 / (100 - 1.5) * 100, 31.7], fmt=lambda v: br(v, 0) + "%",
    res=f"φ = p<sub>v</sub>/p<sub>sat</sub> = 1,5/3,17 = <b>{br(UR,0)}%</b>. A umidade relativa compara a quantidade de vapor com o máximo possível naquela temperatura; a umidade absoluta (razão de umidade) é outra grandeza.")

con("MEC-T49", T, "Aquecimento sensível do ar",
    "Quando o ar úmido é aquecido sem adição ou remoção de água (aquecimento sensível), como numa resistência de aquecimento de duto,",
    "a umidade absoluta permanece constante e a umidade relativa diminui",
    ["a umidade absoluta e a relativa aumentam",
     "a umidade relativa permanece constante",
     "a temperatura de ponto de orvalho aumenta",
     "a umidade absoluta diminui por condensação"],
    res="Sem água entrando ou saindo, ω e o ponto de orvalho ficam <b>constantes</b>. Como a pressão de saturação cresce com a temperatura, a <b>umidade relativa cai</b>: é por isso que o ar aquecido no inverno fica seco.")

con("MEC-T50", T, "Fator de compressibilidade",
    "O fator de compressibilidade Z = Pv/(RT) de um gás real",
    "mede o desvio em relação ao gás ideal: Z = 1 para gás ideal, e se aproxima de 1 em baixas pressões e altas temperaturas (em relação ao ponto crítico)",
    ["é sempre igual a 1 para qualquer gás",
     "é sempre maior que 1 em altas pressões",
     "depende apenas da massa molar do gás",
     "vale 1 exatamente no ponto crítico"],
    res="<b>Z = 1</b> indica comportamento ideal. Pelo princípio dos estados correspondentes, Z depende das pressão e temperatura reduzidas (P/P<sub>cr</sub>, T/T<sub>cr</sub>): perto do ponto crítico, Z fica bem abaixo de 1 (cerca de 0,3 no ponto crítico de muitos gases).")

con("MEC-T51", T, "Ponto crítico",
    "Sobre o ponto crítico de uma substância pura, como a água (22,06 MPa e 374 °C), é correto afirmar que",
    "nele as fases líquida e vapor tornam-se indistinguíveis e o calor latente de vaporização se anula",
    ["nele coexistem as fases sólida, líquida e vapor",
     "acima dele a água só pode existir como sólido",
     "nele o calor latente de vaporização é máximo",
     "corresponde à temperatura de ebulição à pressão atmosférica"],
    res="No <b>ponto crítico</b>, os volumes específicos do líquido e do vapor se igualam e h<sub>lv</sub> = 0. Acima dele, não há mudança de fase nítida (fluido supercrítico), como nas caldeiras supercríticas. A coexistência das três fases é o ponto triplo.")

con("MEC-T52", T, "Aquecedor de água de alimentação",
    "Nos ciclos Rankine regenerativos, parte do vapor é extraída da turbina para aquecer a água de alimentação da caldeira. O principal efeito disso é",
    "aumentar a temperatura média de adição de calor na caldeira, elevando o rendimento térmico do ciclo",
    ["aumentar o trabalho específico da turbina, pois todo o vapor se expande até o condensador",
     "reduzir o rendimento, pois o vapor extraído deixa de produzir trabalho",
     "eliminar a necessidade de condensador",
     "reduzir a pressão da caldeira"],
    res="O vapor extraído deixa de produzir parte do trabalho, mas a água chega mais quente à caldeira: a <b>temperatura média de adição de calor sobe</b> e o ciclo se aproxima do de Carnot. O saldo é positivo, e usinas grandes têm de 5 a 8 aquecedores.")

wn = 1.005 * ((1400 - 700) - (600 - 300))
num("MEC-T53", T, "Trabalho líquido do ciclo Brayton",
    "Num ciclo Brayton ideal, as temperaturas são: entrada do compressor 300 K, saída do compressor 600 K, entrada da turbina 1.400 K e saída da turbina 700 K. Com c<sub>p</sub> = 1,005 kJ/kg·K, o trabalho líquido específico, em kJ/kg, é, aproximadamente,",
    wn, [1.005 * 700, 1.005 * 1000, 1.005 * 300, 201], d=0,
    res=f"w<sub>turbina</sub> = 1,005 × 700 = 703,5 kJ/kg; w<sub>compressor</sub> = 1,005 × 300 = 301,5 kJ/kg. w<sub>líq</sub> = <b>{br(wn,0)} kJ/kg</b>. O rendimento é 1 − 300/600 = 50%. O trabalho da turbina sozinho (704) ignora o compressor; somar os dois (1.005) inverte o sinal do compressor.")

Xd = 300 * 2
num("MEC-T54", T, "Exergia destruída (Gouy-Stodola)",
    "Num processo, a entropia gerada é de 2 kJ/K. Com o ambiente a 300 K, a exergia destruída (trabalho útil perdido), em kJ, é",
    Xd, [150, 2, 302, 1200], d=0,
    res=f"Teorema de Gouy-Stodola: X<sub>destruída</sub> = T<sub>0</sub>·S<sub>ger</sub> = 300 × 2 = <b>{br(Xd,0)} kJ</b>. Cada irreversibilidade custa trabalho que poderia ter sido aproveitado.")

x = (6.8 - 0.65) / 7.5
num("MEC-T55", T, "Título na saída de turbina isentrópica",
    "Vapor com entropia de 6,8 kJ/kg·K expande-se isentropicamente numa turbina até a pressão do condensador, onde s<sub>l</sub> = 0,65 kJ/kg·K e s<sub>lv</sub> = 7,5 kJ/kg·K. O título na saída é, aproximadamente,",
    x, [6.8 / 7.5, (6.8 - 0.65) / (7.5 + 0.65), 0.88, 0.95, 0.98, 1 - x], d=2,
    res=f"Isentrópico: s<sub>2</sub> = s<sub>1</sub> = 6,8. x = (s − s<sub>l</sub>)/s<sub>lv</sub> = 6,15/7,5 = <b>{br(x,2)}</b>. Umidade de 18% já é alta para os últimos estágios; o recomendado é título acima de 0,88.")

con("MEC-T56", T, "Entalpia de gás ideal",
    "Para um gás ideal, a entalpia específica",
    "depende apenas da temperatura, por isso Δh = c<sub>p</sub>ΔT vale para qualquer processo, mesmo que a pressão varie",
    ["depende apenas da pressão",
     "depende da pressão e da temperatura, e Δh = c<sub>p</sub>ΔT só vale a pressão constante",
     "é constante em qualquer processo adiabático",
     "é sempre igual à energia interna"],
    res="Gás ideal: u = u(T) e h = u + Pv = u + RT, logo <b>h = h(T)</b>. Por isso Δh = c<sub>p</sub>ΔT vale em compressores e turbinas, onde a pressão muda. É também por isso que a temperatura não muda numa válvula de estrangulamento de gás ideal.")

F = "Mecânica dos Fluidos"
h = 100000 / (13600 * 9.81) * 1000
num("MEC-F43", F, "Coluna de mercúrio equivalente",
    "A altura de uma coluna de mercúrio (ρ = 13.600 kg/m³) que corresponde a uma pressão de 100 kPa, com g = 9,81 m/s², em mm, é, aproximadamente,",
    h, [h * 13.6, h / 9.81 * 10, 100, 1360], d=0,
    res=f"h = p/(ρg) = 100.000/(13.600 × 9,81) = 0,750 m = <b>{br(h,0)} mm</b>. A mesma pressão equivale a 10,2 m de água: 13,6 vezes mais.")

dp = 1.2 * 10 * 100 / 1000
num("MEC-F44", F, "Variação de pressão no ar com a altura",
    "Considerando o ar com massa específica constante de 1,2 kg/m³ e g = 10 m/s², a pressão atmosférica no topo de um prédio de 100 m é menor que a da base, em kPa, aproximadamente,",
    dp, [12, 0.12, 1000, 0.6], d=1,
    res=f"Δp = ρgh = 1,2 × 10 × 100 = 1.200 Pa = <b>{br(dp,1)} kPa</b>, cerca de 1,2% da atmosfera. Em gases, a variação é pequena em alturas modestas; para grandes altitudes, ρ varia e é preciso integrar.")

hp = 10 ** 2 * 0.3 ** 2 / (2 * 10)
num("MEC-F45", F, "Rotação de corpo rígido",
    "Um tanque cilíndrico aberto, com 0,3 m de raio, contém água e gira em torno do seu eixo vertical a 10 rad/s, como corpo rígido. Com g = 10 m/s², a diferença de altura entre a superfície na parede e no centro, em m, é",
    hp, [2 * hp, hp / 2, 0.09, 3.0], d=2,
    res=f"A superfície forma um paraboloide: Δh = ω²R²/(2g) = 100 × 0,09/20 = <b>{br(hp,2)} m</b>. É o princípio das centrífugas e da fundição centrífuga de tubos.")

dh = 2 * 5 / 10
num("MEC-F46", F, "Tanque em aceleração linear",
    "Um caminhão-tanque com 2 m de comprimento, parcialmente cheio de água, acelera horizontalmente a 5 m/s². Com g = 10 m/s², a diferença de nível da superfície livre entre a traseira e a dianteira do tanque, em m, é",
    dh, [0.5, 2.0, 4.0, 0.25], d=2,
    res=f"A superfície inclina com tg θ = a/g = 0,5. Δh = L·a/g = 2 × 0,5 = <b>{br(dh,2)} m</b>, com o nível mais alto na traseira. Por isso tanques de transporte têm chicanas internas.")

L = (1.2 - 0.17) * 10 * 100
num("MEC-F47", F, "Força de sustentação de balão",
    "Um balão contém 100 m³ de hélio (ρ = 0,17 kg/m³) no ar (ρ = 1,2 kg/m³). Com g = 10 m/s² e desprezando o peso do envelope, a força ascensional líquida, em N, é",
    L, [1200, 170, 1370, 515], d=0,
    res=f"Empuxo − peso do gás = (ρ<sub>ar</sub> − ρ<sub>He</sub>)·g·V = 1,03 × 10 × 100 = <b>{br(L,0)} N</b>, cerca de 103 kgf. O empuxo sozinho (1.200 N) esquece que o hélio também pesa.")

con("MEC-F48", F, "Estabilidade de corpos flutuantes",
    "Um corpo flutuante, como um navio, é estável quanto à inclinação lateral (adernamento) quando",
    "o metacentro está acima do centro de gravidade, isto é, a altura metacêntrica é positiva",
    ["o centro de gravidade está acima do metacentro",
     "o centro de empuxo coincide com o centro de gravidade",
     "o volume submerso é maior que o volume emerso",
     "o centro de gravidade está acima da linha d'água"],
    res="Quando o navio inclina, o centro de empuxo se desloca e a vertical que passa por ele corta o eixo de simetria no <b>metacentro M</b>. Se M está acima de G (GM &gt; 0), surge um momento restaurador. Diferente dos corpos totalmente submersos, um flutuante pode ser estável com G acima do centro de empuxo.")

con("MEC-F49", F, "Hipóteses da equação de Bernoulli",
    "A equação de Bernoulli na forma p/ρ + V²/2 + gz = constante só pode ser aplicada, rigorosamente, para escoamento",
    "permanente, incompressível, sem atrito, ao longo de uma linha de corrente e sem máquinas ou trocas de calor entre os pontos",
    ["transiente, compressível e com atrito",
     "com bomba entre os pontos, desde que se some a potência",
     "de gases em alta velocidade, com Mach acima de 0,3",
     "entre dois pontos quaisquer, mesmo em linhas de corrente diferentes de escoamento rotacional"],
    res="Bernoulli vem da integração de Euler ao longo de uma linha de corrente, com as hipóteses: <b>regime permanente, ρ constante, sem viscosidade, sem máquinas</b>. Com perdas e bombas, usa-se a equação da energia (com h<sub>f</sub> e H<sub>bomba</sub>). Entre linhas de corrente diferentes, só vale se o escoamento for irrotacional.")

v = math.sqrt(2 * 10 * 0.2)
num("MEC-F50", F, "Tubo de Pitot em líquido",
    "Um tubo de Pitot simples e um piezômetro, instalados num canal com água, mostram uma diferença de nível de 0,2 m entre as colunas. Com g = 10 m/s², a velocidade da água, em m/s, é",
    v, [4, 1.41, 0.2, 20], d=2,
    res=f"A diferença de colunas é a carga cinética: V²/2g = 0,2 → V = √(2 × 10 × 0,2) = <b>{br(v,2)} m/s</b>. Aqui o fluido da coluna é o próprio fluido que escoa, por isso não há razão de densidades como no Pitot com ar.")

Le = 0.9 * 0.1 / 0.02
num("MEC-F51", F, "Comprimento equivalente de acessório",
    "Um cotovelo de 90° tem coeficiente de perda K = 0,9 e está numa tubulação de 100 mm de diâmetro, com fator de atrito de Darcy igual a 0,02. O comprimento equivalente do cotovelo, em m, é",
    Le, [0.9 * 0.02 / 0.1, 0.9 / 0.02, 0.9 * 0.1, 9.0], d=2,
    res=f"Iguala-se K·V²/2g a f·(L<sub>e</sub>/D)·V²/2g → L<sub>e</sub> = K·D/f = 0,9 × 0,1/0,02 = <b>{br(Le,2)} m</b>. Somando os L<sub>e</sub> ao comprimento real, a perda total sai numa única conta de Darcy-Weisbach.")

con("MEC-F52", F, "Tubulações em paralelo",
    "Duas tubulações de diâmetros diferentes ligam os mesmos dois pontos de uma rede (estão em paralelo). Em regime permanente, é correto afirmar que",
    "a perda de carga é a mesma nos dois ramos, e a vazão total é a soma das vazões",
    ["a vazão é a mesma nos dois ramos, e as perdas se somam",
     "a velocidade é a mesma nos dois ramos",
     "o ramo de maior diâmetro tem maior perda de carga",
     "a perda de carga total é a soma das perdas dos ramos"],
    res="Em <b>paralelo</b>, os dois ramos começam e terminam nos mesmos nós: mesma diferença de carga, logo <b>mesma h<sub>f</sub></b>, e as vazões se somam. Em série, é o contrário: mesma vazão, e as perdas se somam. É a mesma lógica dos circuitos elétricos.")

Tc = 2 * 1200 / 1200
num("MEC-F53", F, "Tempo crítico de fechamento (golpe de aríete)",
    "Numa adutora de 1.200 m de comprimento, a onda de pressão se propaga a 1.200 m/s. O fechamento de uma válvula na extremidade é considerado brusco (sobrepressão máxima de Joukowsky) se o tempo de manobra for menor que, em segundos,",
    Tc, [1.0, 4.0, 0.5, 3.0], d=1,
    res=f"A onda vai até o reservatório e volta: T<sub>c</sub> = 2L/c = 2 × 1.200/1.200 = <b>{br(Tc,1)} s</b>. Fechando mais devagar que isso, a onda de alívio refletida chega antes de a válvula terminar de fechar, e a sobrepressão diminui.")

xt = 5e5 * 1.5e-5 / 10
num("MEC-F54", F, "Posição da transição na camada limite",
    "Ar (ν = 1,5 × 10<sup>−5</sup> m²/s) escoa a 10 m/s sobre uma placa plana lisa. Adotando Re<sub>crítico</sub> = 5 × 10⁵, a transição da camada limite de laminar para turbulenta ocorre a que distância do bordo de ataque, em m?",
    xt, [xt / 10, xt * 2, 7.5, 0.035], d=2,
    res=f"Re<sub>x</sub> = Ux/ν → x = 5 × 10⁵ × 1,5 × 10<sup>−5</sup>/10 = <b>{br(xt,2)} m</b>. Antes disso, a camada limite é laminar; depois, turbulenta, mais espessa e com atrito maior.")

con("MEC-F55", F, "Bocal convergente bloqueado",
    "Um gás escoa de um reservatório por um bocal convergente para um ambiente cuja pressão é reduzida aos poucos. Quando a garganta atinge Mach 1 (escoamento bloqueado ou choked), reduzir ainda mais a pressão do ambiente",
    "não aumenta a vazão mássica, que só cresce se aumentarem a pressão ou a densidade no reservatório",
    ["aumenta a vazão indefinidamente",
     "faz a velocidade na garganta passar de Mach 1",
     "reduz a vazão, pois surge uma onda de choque na garganta",
     "transforma o bocal em difusor"],
    res="Com M = 1 na garganta, as informações de pressão (que viajam à velocidade do som) não sobem mais o escoamento: a <b>vazão fica bloqueada</b>. Para ir além de Mach 1, é preciso um bocal convergente-divergente (de Laval). É o princípio das placas de orifício críticas e das válvulas de segurança.")

pr = 0.528
num("MEC-F56", F, "Razão de pressão crítica",
    "Para o ar (k = 1,4), a razão entre a pressão na garganta, quando o escoamento é sônico, e a pressão de estagnação é p*/p<sub>0</sub> = [2/(k + 1)]<sup>k/(k−1)</sup>. Dado 0,8333<sup>3,5</sup> ≈ 0,528, essa razão vale",
    pr, [0.833, 0.634, 0.577, 0.707, 0.5, 0.264], d=3,
    res=f"p*/p<sub>0</sub> = (2/2,4)<sup>3,5</sup> = 0,8333<sup>3,5</sup> ≈ <b>{br(pr,3)}</b>. Se a pressão a jusante for menor que cerca de 53% da pressão no reservatório, o bocal convergente fica bloqueado. A razão de temperaturas é 0,833 e a de densidades, 0,634.")

R = "Resistência dos Materiais"
phi = 500 * 1 / (80e9 * 2.5e-7) + 500 * 0.5 / (80e9 * 1.25e-7)
num("MEC-R44", R, "Torção em eixo escalonado",
    "Um eixo de aço (G = 80 GPa) tem dois trechos em série: o primeiro com 1 m e J = 2,5 × 10<sup>−7</sup> m⁴; o segundo com 0,5 m e J = 1,25 × 10<sup>−7</sup> m⁴. Um torque de 500 N·m atravessa os dois trechos. O ângulo de torção total, em radianos, é",
    phi, [0.025, 0.0375, 0.075, 0.1], d=3,
    res=f"Os ângulos se somam: φ = Σ TL/(GJ) = 500 × 1/(80 × 10⁹ × 2,5 × 10<sup>−7</sup>) + 500 × 0,5/(80 × 10⁹ × 1,25 × 10<sup>−7</sup>) = 0,025 + 0,025 = <b>{br(phi,3)} rad</b> (≈ 2,9°).")

T_ = 40 * math.pi * 50 ** 3 / 16 / 1000; P = T_ * 2 * math.pi * 1000 / 60 / 1000
num("MEC-R45", R, "Potência máxima transmitida por eixo",
    "Um eixo maciço de 50 mm, com tensão de cisalhamento admissível de 40 MPa, gira a 1.000 rpm. A potência máxima que ele pode transmitir, em kW, é, aproximadamente,",
    P, [P / 2, 2 * P, T_ * 1000 / 1000 / 1000 * 1000 / 60, 9.8], d=0,
    res=f"T<sub>adm</sub> = τπd³/16 = 40 × π × 50³/16 = 981.748 N·mm ≈ 982 N·m. ω = 2π × 1.000/60 = 104,7 rad/s. P = Tω = <b>{br(P,0)} kW</b>. Com o fator 32 (flexão) no lugar de 16, a potência cairia à metade.")

I = math.pi * (100 ** 4 - 80 ** 4) / 64 / 1e4
num("MEC-R46", R, "Momento de inércia de seção tubular",
    "O momento de inércia de área de um tubo com diâmetro externo de 100 mm e interno de 80 mm, em relação a um eixo diametral, em cm⁴, é, aproximadamente,",
    I, [2 * I, math.pi * (100 - 80) ** 4 / 64 / 1e4, math.pi * 100 ** 4 / 64 / 1e4, I / 2], d=0,
    res=f"I = π(D⁴ − d⁴)/64 = π × (10⁸ − 4,096 × 10⁷)/64 = 2,90 × 10⁶ mm⁴ = <b>{br(I,0)} cm⁴</b>. O tubo tem 59% do I da barra maciça (491 cm⁴) com só 36% da área. O momento polar seria o dobro (πD⁴/32).")

rg = 120 / math.sqrt(12)
num("MEC-R47", R, "Raio de giração de seção retangular",
    "O raio de giração de uma seção retangular de 60 mm × 120 mm em relação ao eixo centroidal paralelo ao lado de 60 mm (flexão em torno do eixo de maior inércia), em mm, é, aproximadamente,",
    rg, [60 / math.sqrt(12), 120 / 4, 120 / 12, 60], d=1,
    res=f"r = √(I/A) = √[(bh³/12)/(bh)] = h/√12 = 120/3,464 = <b>{br(rg,1)} mm</b>. Para o eixo de menor inércia, r = 60/√12 = 17,3 mm, e é ele que governa a flambagem se a coluna não tiver travamento lateral.")

V = 10 * 6 / 2
num("MEC-R48", R, "Esforço cortante máximo",
    "Uma viga biapoiada de 6 m de vão recebe carga uniformemente distribuída de 10 kN/m. O esforço cortante máximo, em kN, é",
    V, [60, 15, 45, 0], d=0,
    res=f"Reações iguais: R = wL/2 = 10 × 6/2 = 30 kN. O cortante é máximo junto aos apoios, <b>{br(V,0)} kN</b>, e se anula no meio do vão, onde o momento é máximo (wL²/8 = 45 kN·m).")

M = 5 * 3 + 2 * 3 ** 2 / 2
num("MEC-R49", R, "Superposição de cargas em balanço",
    "Uma viga em balanço de 3 m recebe uma carga concentrada de 5 kN na extremidade livre e uma carga distribuída de 2 kN/m em todo o comprimento. O momento fletor no engaste, em kN·m, é",
    M, [21, 15, 9, 33], d=0,
    res=f"Superposição: carga na ponta, PL = 5 × 3 = 15 kN·m; carga distribuída, wL²/2 = 2 × 9/2 = 9 kN·m. Total: <b>{br(M,0)} kN·m</b>. 21 seria somar P a wL e multiplicar por L, colocando a resultante distribuída na ponta.")

s = 100000 / 5000 + 10e6 / 250e3
num("MEC-R50", R, "Tração combinada com flexão",
    "Uma barra com área de 5.000 mm² e módulo resistente de 250 × 10³ mm³ recebe força de tração de 100 kN e momento fletor de 10 kN·m. A tensão normal máxima, em MPa, é",
    s, [20, 40, 20, 80], d=0,
    res=f"σ<sub>máx</sub> = N/A + M/W = 100.000/5.000 + 10 × 10⁶/250 × 10³ = 20 + 40 = <b>{br(s,0)} MPa</b> (tração), na face tracionada pela flexão. Na face oposta: 20 − 40 = −20 MPa (compressão).")

n = 300 / (150 - (-50))
num("MEC-R51", R, "Coeficiente de segurança pelo critério de Tresca",
    "Num ponto de uma peça de aço dúctil (σ<sub>e</sub> = 300 MPa), as tensões principais são σ<sub>1</sub> = 150 MPa, σ<sub>2</sub> = −50 MPa e σ<sub>3</sub> = 0. O coeficiente de segurança ao escoamento pelo critério de Tresca é",
    n, [2.0, 3.0, 300 / math.sqrt(150 ** 2 + 50 ** 2 + 150 * 50), 6.0], d=2,
    res=f"Tresca: σ<sub>eq</sub> = σ<sub>máx</sub> − σ<sub>mín</sub> = 150 − (−50) = 200 MPa. n = 300/200 = <b>{br(n,2)}</b>. Usar só σ<sub>1</sub> (n = 2) ignora que tensões de sinais opostos aumentam o cisalhamento. Von Mises daria n ≈ 1,65.")

ng = 1 / (100 / 250 + 150 / 600)
num("MEC-R52", R, "Fadiga pelo critério de Goodman",
    "Um componente de aço (S<sub>e</sub> = 250 MPa corrigido; σ<sub>r</sub> = 600 MPa) está sob tensão alternada de 100 MPa e tensão média de 150 MPa. Pelo critério de Goodman modificado, σ<sub>a</sub>/S<sub>e</sub> + σ<sub>m</sub>/σ<sub>r</sub> = 1/n, o coeficiente de segurança é, aproximadamente,",
    ng, [2.5, 4.0, 1 / (100 / 250 + 150 / 300), 0.65], d=2,
    res=f"1/n = 100/250 + 150/600 = 0,40 + 0,25 = 0,65 → n = <b>{br(ng,2)}</b>. Considerar só a tensão alternada (n = 2,5) ignora que a tensão média de tração reduz a resistência à fadiga.")

con("MEC-R53", R, "Kt e Kf",
    "Sobre o fator teórico de concentração de tensão K<sub>t</sub> e o fator de concentração na fadiga K<sub>f</sub>, é correto afirmar que",
    "K<sub>t</sub> depende só da geometria, e K<sub>f</sub> = 1 + q(K<sub>t</sub> − 1), em que a sensibilidade ao entalhe q depende do material e do raio do entalhe",
    ["K<sub>t</sub> depende do material e K<sub>f</sub> só da geometria",
     "K<sub>f</sub> é sempre maior que K<sub>t</sub>",
     "materiais frágeis nunca são sensíveis ao entalhe",
     "K<sub>t</sub> é sempre igual a 3 para qualquer furo"],
    res="<b>K<sub>t</sub></b> vem da teoria da elasticidade e só depende da forma (3 para furo pequeno em placa infinita sob tração). Na fadiga, o efeito real é <b>K<sub>f</sub> ≤ K<sub>t</sub></b>, com q de 0 (insensível) a 1 (totalmente sensível). Aços de alta resistência têm q próximo de 1.")

con("MEC-R54", R, "Tenacidade e resiliência",
    "No diagrama tensão-deformação de engenharia, a área total sob a curva, até a fratura, representa",
    "a tenacidade (energia absorvida por unidade de volume até romper)",
    ["a resiliência, que é a energia até o limite de escoamento",
     "o módulo de elasticidade",
     "a dureza do material",
     "a ductilidade, medida em porcentagem"],
    res="<b>Tenacidade</b> = área total sob a curva, até a fratura. <b>Resiliência</b> = área só do trecho elástico. Um material tenaz combina resistência e ductilidade: aço doce é mais tenaz que aço de molas ou ferro fundido.")

con("MEC-R55", R, "Linha neutra na flexão pura",
    "Numa viga de material homogêneo e elástico sob flexão pura, a linha neutra",
    "passa pelo centroide da seção, onde a tensão normal é nula",
    ["passa sempre pela face superior",
     "coincide com a face mais tracionada",
     "fica a 1/3 da altura, a partir da base",
     "é onde a tensão normal é máxima"],
    res="Do equilíbrio (∫σ dA = 0, sem força normal) resulta que a <b>linha neutra passa pelo centroide</b>. Em seções assimétricas, como o T, o centroide fica fora do meio da altura, e as tensões máximas de tração e compressão diferem.")

s = 20000 / (4 * 50)
num("MEC-R56", R, "Tensão em cabos de elevação",
    "Uma carga de 20 kN é suspensa por 4 cabos de aço que trabalham igualmente, cada um com 50 mm² de área metálica. A tensão normal em cada cabo, em MPa, é",
    s, [400, 200, 25, 1000], d=0,
    res=f"Cada cabo leva 5 kN: σ = 5.000/50 = <b>{br(s,0)} MPa</b>. Em equipamentos de elevação, normas exigem fatores de segurança de 5 ou mais sobre a carga de ruptura do cabo.")

nu = 0.00028 / 0.001
num("MEC-R57", R, "Coeficiente de Poisson a partir de extensômetros",
    "Num ensaio de tração, extensômetros medem deformação longitudinal de 1,0 × 10<sup>−3</sup> e deformação transversal de −2,8 × 10<sup>−4</sup>. O coeficiente de Poisson do material é",
    nu, [3.57, 0.028, 0.5, 0.72], d=2,
    res=f"ν = −ε<sub>trans</sub>/ε<sub>long</sub> = 2,8 × 10<sup>−4</sup>/1,0 × 10<sup>−3</sup> = <b>{br(nu,2)}</b>. Valores típicos: aço ≈ 0,3; alumínio ≈ 0,33; borracha ≈ 0,5. Inverter a razão dá 3,57, um valor impossível (ν ≤ 0,5).")

t = 2 * 500 / (138 * 0.85 - 0.6 * 2)
num("MEC-R58", R, "Espessura de casco cilíndrico (ASME VIII)",
    "Pelo código ASME VIII, a espessura de um casco cilíndrico sob pressão interna é t = PR/(SE − 0,6P). Para P = 2 MPa, raio interno de 500 mm, tensão admissível S = 138 MPa e eficiência de junta E = 0,85, a espessura mínima, sem corrosão, em mm, é, aproximadamente,",
    t, [2 * 500 / 138, 2 * t, 2 * 1000 / 138, 2 * 500 / (138 * 0.85)], d=2,
    res=f"t = 2 × 500/(138 × 0,85 − 0,6 × 2) = 1.000/(117,3 − 1,2) = 1.000/116,1 = <b>{br(t,2)} mm</b>. A eficiência de junta (radiografia parcial, 0,85) penaliza a solda longitudinal. Ainda se soma a sobre-espessura de corrosão.")

lam = math.pi * math.sqrt(200000 / 200)
num("MEC-R59", R, "Esbeltez limite para a fórmula de Euler",
    "Para um aço com E = 200 GPa e limite de proporcionalidade de 200 MPa, a esbeltez mínima a partir da qual a fórmula de Euler é válida é, aproximadamente, igual a",
    lam, [math.sqrt(200000 / 200), lam * 2, lam / 2, 1000], d=0,
    res=f"Euler vale enquanto σ<sub>cr</sub> = π²E/λ² ≤ σ<sub>p</sub> → λ ≥ π√(E/σ<sub>p</sub>) = π × √1.000 = <b>{br(lam,0)}</b>. Abaixo disso, a coluna é intermediária ou curta, e a flambagem é inelástica.")
