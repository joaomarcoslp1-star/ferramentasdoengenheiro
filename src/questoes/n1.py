# -*- coding: utf-8 -*-
# Lote 1 (28/11/2026): Termodinâmica, Mecânica dos Fluidos, Resistência dos Materiais
import math
from nbase import num, con, br

T = "Termodinâmica"
# T11 trabalho de fronteira isobárico
P, V1, V2 = 200, 0.05, 0.20
W = P * (V2 - V1)
num("MEC-T11", T, "Trabalho de fronteira a pressão constante",
    "Um gás contido num cilindro com pistão livre expande-se a pressão constante de 200 kPa, passando de 0,05 m³ para 0,20 m³. O trabalho realizado pelo gás, em kJ, é",
    W, [P * V2, P * V1, 3, 300], d=0,
    res=f"A pressão constante, W = P·(V<sub>2</sub> − V<sub>1</sub>) = 200 × (0,20 − 0,05) = <b>{br(W,0)} kJ</b> (kPa·m³ = kJ). Usar só o volume final (40 kJ) ignora que o gás já ocupava 0,05 m³.")

# T12 massa de gás ideal
P, V, T_ = 574, 0.5, 127 + 273
m = P * V / (0.287 * T_)
num("MEC-T12", T, "Equação de estado do gás ideal",
    "Um tanque rígido de 0,5 m³ contém ar (R = 0,287 kJ/kg·K) a 574 kPa e 127 °C. A massa de ar no tanque, em kg, é, aproximadamente,",
    m, [P * V / (0.287 * 127), P * V / (8.314 * T_), 5.0, 1.25], d=2,
    res=f"m = PV/(RT) = 574 × 0,5/(0,287 × 400) = 287/114,8 = <b>{br(m,2)} kg</b>. Com a temperatura em °C, o resultado (7,87 kg) não tem sentido físico; e 8,314 kJ/kmol·K é a constante universal, que exigiria massa em kmol.")

# T13 turbina com eficiência isentrópica
T1, T2s, eta = 1000, 600, 0.85
T2 = T1 - eta * (T1 - T2s)
num("MEC-T13", T, "Eficiência isentrópica da turbina",
    "Gases quentes entram numa turbina adiabática a 1.000 K. Se a expansão fosse isentrópica, a temperatura de saída seria 600 K. Com eficiência isentrópica de 85% e calor específico constante, a temperatura real de saída, em K, é",
    T2, [T1 - (T1 - T2s) / eta, T2s, 700, 340], d=0,
    res=f"Na turbina, η<sub>t</sub> = (T<sub>1</sub> − T<sub>2</sub>)/(T<sub>1</sub> − T<sub>2s</sub>), porque o trabalho real é menor que o ideal. T<sub>2</sub> = 1.000 − 0,85 × 400 = <b>{br(T2,0)} K</b>. Dividir por 0,85 (529 K) é a fórmula do compressor; a saída real é sempre mais quente que a isentrópica.")

# T14 eficiência de segunda lei de refrigerador
QL, Wr, TL, TH = 6, 2, 250, 300
cop = QL / Wr; copc = TL / (TH - TL); r = cop / copc
num("MEC-T14", T, "Rendimento de segunda lei do refrigerador",
    "Um refrigerador remove 6 kW de uma câmara a −23 °C, rejeita calor para o ambiente a 27 °C e consome 2 kW. A razão entre o COP real e o COP de um refrigerador de Carnot entre as mesmas temperaturas é",
    r, [cop / (TH / (TH - TL)), 1 / r, 0.4, 0.75], d=2,
    res=f"COP real = 6/2 = 3. COP de Carnot = T<sub>L</sub>/(T<sub>H</sub> − T<sub>L</sub>) = 250/50 = 5. Razão = 3/5 = <b>{br(r,2)}</b>: o refrigerador alcança 60% do desempenho ideal. Usar T<sub>H</sub>/ΔT = 6 (bomba de calor) dá 0,50.")

# T15 geração de entropia
Q, TH, TL = 1000, 500, 250
Sg = Q / TL - Q / TH
num("MEC-T15", T, "Geração de entropia na transferência de calor",
    "Uma quantidade de 1.000 kJ de calor é transferida diretamente de um reservatório a 500 K para outro a 250 K. A entropia gerada nesse processo, em kJ/K, é",
    Sg, [Q / TL + Q / TH, Q / TL, 0, 1], d=1,
    res=f"ΔS<sub>quente</sub> = −1.000/500 = −2 kJ/K; ΔS<sub>frio</sub> = +1.000/250 = +4 kJ/K. S<sub>ger</sub> = 4 − 2 = <b>{br(Sg,1)} kJ/K</b>, positiva porque transferir calor com diferença finita de temperatura é irreversível. Zero só se as temperaturas fossem iguais.")

# T16 trabalho politrópico
P1, V1, V2, n = 100, 0.8, 0.1, 1.25
P2 = P1 * 13.45
Wp = (P2 * V2 - P1 * V1) / (n - 1)
num("MEC-T16", T, "Trabalho em processo politrópico",
    "Ar a 100 kPa ocupa 0,8 m³ e é comprimido até 0,1 m³ segundo um processo politrópico com n = 1,25. Dado 8<sup>1,25</sup> ≈ 13,45, o trabalho recebido pelo ar, em kJ, é, aproximadamente,",
    Wp, [P2 * V2 - P1 * V1, P1 * V1 * math.log(8), 436, 1090], d=0,
    res=f"P<sub>2</sub> = P<sub>1</sub>·(V<sub>1</sub>/V<sub>2</sub>)<sup>n</sup> = 100 × 13,45 = 1.345 kPa. W = (P<sub>2</sub>V<sub>2</sub> − P<sub>1</sub>V<sub>1</sub>)/(n − 1) = (134,5 − 80)/0,25 = <b>{br(Wp,0)} kJ</b> recebidos. Se o processo fosse isotérmico, o trabalho seria P<sub>1</sub>V<sub>1</sub>·ln 8 ≈ 166 kJ.")

con("MEC-T17", T, "Enunciado de Kelvin-Planck",
    "O enunciado de Kelvin-Planck da segunda lei da termodinâmica estabelece que",
    "é impossível construir um dispositivo que, operando em ciclo, produza trabalho trocando calor com um único reservatório térmico",
    ["é impossível transferir calor de um corpo frio para um corpo quente, mesmo com consumo de trabalho",
     "todo processo adiabático é isentrópico",
     "a energia interna de um gás ideal depende da pressão e da temperatura",
     "o rendimento de qualquer máquina térmica reversível depende do fluido de trabalho"],
    res="Kelvin-Planck: nenhuma máquina cíclica converte <b>integralmente</b> em trabalho o calor recebido de uma única fonte; sempre há rejeição para um reservatório mais frio. O enunciado de Clausius proíbe o fluxo de calor do frio para o quente <b>sem</b> trabalho externo (com trabalho, é o que faz a geladeira). O rendimento de Carnot independe do fluido.")

# T18 rendimento de segunda lei de usina
eta, TH, TL = 0.30, 900, 300
ec = 1 - TL / TH; e2 = eta / ec
num("MEC-T18", T, "Rendimento de segunda lei de uma usina",
    "Uma usina térmica tem rendimento de 30% e opera entre uma fonte a 900 K e o ambiente a 300 K. Seu rendimento de segunda lei (razão entre o rendimento real e o máximo possível) é, aproximadamente,",
    e2, [eta * ec, 1 / e2, 0.30, 0.67], d=2,
    res=f"η<sub>Carnot</sub> = 1 − 300/900 = 0,667. η<sub>II</sub> = 0,30/0,667 = <b>{br(e2,2)}</b>: a usina aproveita 45% do trabalho que seria possível entre essas temperaturas. Multiplicar os rendimentos (0,20) não tem significado físico.")

# T19 Rankine com entalpias
h1, h2, h3, h4 = 192, 200, 3400, 2300
wt, wb, qe = h3 - h4, h2 - h1, h3 - h2
eta = 100 * (wt - wb) / qe
num("MEC-T19", T, "Rendimento do ciclo Rankine por entalpias",
    "Num ciclo Rankine ideal, as entalpias são: entrada da bomba 192 kJ/kg, saída da bomba 200 kJ/kg, saída da caldeira 3.400 kJ/kg e saída da turbina 2.300 kJ/kg. O rendimento térmico do ciclo é, aproximadamente,",
    eta, [100 * wt / qe, 100 * wt / h3, 100 * (wt - wb) / h3, 100 * h4 / h3, 100 * (wt + wb) / qe], fmt=lambda v: br(v, 1) + "%",
    res=f"w<sub>turbina</sub> = 3.400 − 2.300 = 1.100 kJ/kg; w<sub>bomba</sub> = 200 − 192 = 8 kJ/kg; q<sub>caldeira</sub> = 3.400 − 200 = 3.200 kJ/kg. η = (1.100 − 8)/3.200 = <b>{br(eta,1)}%</b>. O calor da caldeira começa na saída da bomba (200 kJ/kg), não em zero; e o trabalho da bomba é pequeno, mas desconta do trabalho líquido.")

con("MEC-T20", T, "Propriedades intensivas e extensivas",
    "Dentre os conjuntos de propriedades abaixo, aquele formado apenas por propriedades intensivas é",
    "temperatura, pressão e volume específico",
    ["massa, volume e energia interna",
     "temperatura, volume e entalpia",
     "pressão, massa e entropia",
     "energia interna específica, volume e massa"],
    res="Intensivas não dependem do tamanho do sistema: <b>temperatura, pressão e qualquer propriedade específica</b> (por unidade de massa, como v, u, h, s). Massa, volume, energia interna, entalpia e entropia totais são extensivas. Dividir uma extensiva pela massa a torna intensiva.")

F = "Mecânica dos Fluidos"
# F11 pressão absoluta com barômetro
pb = 13600 * 9.81 * 0.700 / 1000
pa = 250 + pb
num("MEC-F11", F, "Pressão absoluta e manométrica",
    "Um manômetro instalado num vaso indica 250 kPa num local onde o barômetro marca 700 mmHg (ρ<sub>Hg</sub> = 13.600 kg/m³; g = 9,81 m/s²). A pressão absoluta no vaso, em kPa, é, aproximadamente,",
    pa, [250, 250 - pb, 250 + 101.3, 950], d=0,
    res=f"p<sub>atm</sub> = ρgh = 13.600 × 9,81 × 0,700 = {br(pb,1)} kPa. p<sub>abs</sub> = p<sub>man</sub> + p<sub>atm</sub> = 250 + 93,4 = <b>{br(pa,0)} kPa</b>. Usar 101,3 kPa (nível do mar) dá 351 kPa: se o barômetro local foi informado, ele é que vale.")

# F12 prensa hidráulica
F2 = 100 * (20 / 2) ** 2 / 1000
num("MEC-F12", F, "Princípio de Pascal (prensa hidráulica)",
    "Numa prensa hidráulica, o pistão menor tem 2 cm de diâmetro e o maior, 20 cm. Aplicando-se 100 N no pistão menor, a força no pistão maior, em kN, é, desprezando atritos,",
    F2, [1.0, 100, 0.1, 3.14], d=1,
    res=f"A pressão é a mesma nos dois pistões: F<sub>2</sub> = F<sub>1</sub>·(D<sub>2</sub>/D<sub>1</sub>)² = 100 × 10² = 10.000 N = <b>{br(F2,1)} kN</b>. Usar a razão dos diâmetros sem elevar ao quadrado dá 1 kN; a força escala com a área.")

# F13 pressão com óleo
p = 0.85 * 1000 * 10 * 4 / 1000
num("MEC-F13", F, "Pressão em líquido com densidade relativa",
    "Um tanque aberto contém 4 m de óleo de densidade relativa 0,85. Com g = 10 m/s², a pressão manométrica no fundo, em kPa, é",
    p, [40, 4 / 0.85 * 10, 101.3 + p, 3.4], d=1,
    res=f"p = ρgh = (0,85 × 1.000) × 10 × 4 = 34.000 Pa = <b>{br(p,1)} kPa</b>. Somar a atmosfera (135,3 kPa) daria a pressão absoluta; usar a densidade da água (40 kPa) esquece o óleo.")

# F14 sifão
v = math.sqrt(2 * 10 * 2)
num("MEC-F14", F, "Velocidade de saída de um sifão",
    "Um sifão retira água de um reservatório de nível constante e descarrega na atmosfera num ponto 2 m abaixo da superfície livre. Desprezando perdas e com g = 10 m/s², a velocidade de saída, em m/s, é, aproximadamente,",
    v, [math.sqrt(10 * 2), 2 * 10 * 2, 20, 2.0], d=2,
    res=f"Bernoulli entre a superfície (v ≈ 0, p = p<sub>atm</sub>) e a saída (p = p<sub>atm</sub>): v = √(2gh) = √40 = <b>{br(v,2)} m/s</b>. A altura que conta é o desnível entre a superfície livre e a saída, não a altura do ponto mais alto do sifão (que só limita a operação, pela pressão de vapor).")

# F15 ramificação
vb = 2 * (100 / 50) ** 2 / 2
num("MEC-F15", F, "Continuidade em ramificação",
    "Um tubo de 100 mm de diâmetro, com água a 2 m/s, divide-se em dois ramais iguais de 50 mm, que recebem vazões iguais. A velocidade em cada ramal, em m/s, é",
    vb, [8.0, 2.0, 1.0, 16.0], d=1,
    res=f"Cada ramal tem 1/4 da área do tubo principal e recebe metade da vazão: v = 2 × 4 × ½ = <b>{br(vb,1)} m/s</b>. Esquecer a divisão da vazão dá 8 m/s.")

# F16 camada limite laminar
U, nu, x = 4, 1.6e-5, 0.4
Re = U * x / nu; d_ = 5 * x / math.sqrt(Re) * 1000
num("MEC-F16", F, "Espessura da camada limite laminar",
    "Ar (ν = 1,6 × 10<sup>−5</sup> m²/s) escoa a 4 m/s sobre uma placa plana lisa. Usando δ = 5x/√Re<sub>x</sub>, a espessura da camada limite a 0,4 m do bordo de ataque, em mm, é, aproximadamente,",
    d_, [5 * x / Re * 1000 * 1e3, 5 * x / math.sqrt(Re) * 1000 * 2, 5 * x / math.sqrt(Re) * 1000 / 2, 20], d=2,
    res=f"Re<sub>x</sub> = Ux/ν = 4 × 0,4/(1,6 × 10<sup>−5</sup>) = 10⁵ (laminar, abaixo de 5 × 10⁵). δ = 5 × 0,4/√10⁵ = 2/316,2 = 0,00632 m = <b>{br(d_,2)} mm</b>. A camada limite laminar cresce com √x.")

# F17 velocidade do som
c = math.sqrt(1.4 * 287 * 300)
num("MEC-F17", F, "Velocidade do som num gás",
    "A velocidade do som no ar (k = 1,4; R = 287 J/kg·K) a 27 °C é, aproximadamente, em m/s,",
    c, [math.sqrt(287 * 300), math.sqrt(1.4 * 287 * 27), math.sqrt(1.4 * 0.287 * 300), 410], d=0,
    res=f"c = √(kRT) = √(1,4 × 287 × 300) = √120.540 = <b>{br(c,0)} m/s</b>. Sem o k, a conta dá 293 m/s (seria um processo isotérmico, a hipótese errada de Newton); com °C, 104 m/s; e R precisa estar em J/kg·K.")

# F18 viscosidade cinemática
nu_cst = 0.08 / 800 * 1e6
num("MEC-F18", F, "Viscosidade dinâmica e cinemática",
    "Um óleo lubrificante tem viscosidade dinâmica de 0,08 Pa·s e massa específica de 800 kg/m³. Sua viscosidade cinemática, em centistokes (mm²/s), é",
    nu_cst, [64, 10, 1000, 0.1], d=0,
    res=f"ν = μ/ρ = 0,08/800 = 1,0 × 10<sup>−4</sup> m²/s = <b>{br(nu_cst,0)} mm²/s</b> = 100 cSt (1 cSt = 1 mm²/s). Multiplicar μ por ρ (64) inverte a definição. A água a 20 °C tem cerca de 1 cSt.")

con("MEC-F19", F, "Linha de energia e linha piezométrica",
    "Numa tubulação de diâmetro constante, com escoamento permanente de água, a linha de energia e a linha piezométrica",
    "são paralelas, separadas pela carga cinética v²/2g, e ambas descem no sentido do escoamento por causa da perda de carga",
    ["coincidem, pois a velocidade é constante",
     "são horizontais, pois a vazão não varia",
     "convergem no sentido do escoamento, pois a energia cinética é convertida em pressão",
     "a linha piezométrica fica acima da linha de energia sempre que a pressão é positiva"],
    res="A linha piezométrica marca p/ρg + z; a linha de energia soma v²/2g a ela. Com diâmetro constante, v²/2g é constante: as linhas são <b>paralelas</b> e caem juntas com a perda de carga. A linha piezométrica nunca fica acima da linha de energia.")

# F20 potência de jato
Pj = 0.5 * 1000 * 0.02 * 30 ** 2 / 1000
num("MEC-F20", F, "Potência de um jato",
    "Um bocal descarrega um jato de água (ρ = 1.000 kg/m³) com vazão de 20 L/s e velocidade de 30 m/s. A potência cinética do jato, em kW, é",
    Pj, [2 * Pj, 0.6, 0.3, 27], d=1,
    res=f"P = ṁ·v²/2 = ρQ·v²/2 = 1.000 × 0,02 × 900/2 = 9.000 W = <b>{br(Pj,1)} kW</b>. Esquecer o ½ da energia cinética dá 18 kW; e ρQv = 600 N é a força do jato numa placa, não uma potência.")

R = "Resistência dos Materiais"
# R11 coeficiente de segurança
A = 50000 / (250 / 2.5)
num("MEC-R11", R, "Tensão admissível e coeficiente de segurança",
    "Uma barra de aço com limite de escoamento de 250 MPa deve suportar 50 kN de tração com coeficiente de segurança 2,5 em relação ao escoamento. A área mínima da seção transversal, em mm², é",
    A, [50000 / 250, 50000 / (250 * 2.5), 1250, 625], d=0,
    res=f"σ<sub>adm</sub> = σ<sub>e</sub>/n = 250/2,5 = 100 MPa. A = F/σ<sub>adm</sub> = 50.000/100 = <b>{br(A,0)} mm²</b>. Sem o coeficiente, a área (200 mm²) deixaria a barra no limite do escoamento.")

# R12 barras em série
d1 = 20000 * 1000 / (200000 * 200); d2 = 20000 * 500 / (200000 * 100)
num("MEC-R12", R, "Alongamento de barra com dois trechos",
    "Uma barra de aço (E = 200 GPa) tem dois trechos: o primeiro com 1,0 m e 200 mm² de seção, e o segundo com 0,5 m e 100 mm². A barra é tracionada por 20 kN nas extremidades. O alongamento total, em mm, é",
    d1 + d2, [d1, 20000 * 1500 / (200000 * 100), 20000 * 1500 / (200000 * 200), 2.0], d=2,
    res=f"Os trechos estão em série e recebem a mesma força: δ = Σ FL/(EA) = 20.000 × 1.000/(200.000 × 200) + 20.000 × 500/(200.000 × 100) = 0,50 + 0,50 = <b>{br(d1+d2,2)} mm</b>.")

# R13 biapoiada com carga distribuída
w, L, b, h = 4, 6, 100, 300
M = w * L ** 2 / 8; W_ = b * h ** 2 / 6; s = M * 1e6 / W_
num("MEC-R13", R, "Tensão de flexão em viga biapoiada",
    "Uma viga biapoiada de 6 m de vão, com seção retangular de 100 mm de largura e 300 mm de altura, recebe carga uniformemente distribuída de 4 kN/m. A tensão normal máxima de flexão, em MPa, é",
    s, [2 * s, 3 * s, 4 * s, s / 2], d=0,
    res=f"M<sub>máx</sub> = wL²/8 = 4 × 36/8 = 18 kN·m. W = bh²/6 = 100 × 300²/6 = 1,5 × 10⁶ mm³. σ = M/W = 18 × 10⁶/1,5 × 10⁶ = <b>{br(s,0)} MPa</b>. Com a viga deitada (W = 300 × 100²/6), a tensão triplicaria (36 MPa); wL²/4 é o erro do momento.")

con("MEC-R14", R, "Tensões num plano inclinado",
    "Uma barra prismática está submetida a tração axial com tensão normal σ na seção transversal. Sobre as tensões em planos inclinados dessa barra, é correto afirmar que",
    "a tensão de cisalhamento máxima vale σ/2 e ocorre nos planos a 45° do eixo da barra",
    ["não há tensão de cisalhamento em nenhum plano, pois a carga é axial",
     "a tensão de cisalhamento máxima vale σ e ocorre na seção transversal",
     "a tensão normal é máxima nos planos a 45° do eixo",
     "a tensão de cisalhamento máxima vale σ/√2 e ocorre nos planos a 30°"],
    res="No plano a θ da seção transversal: σ<sub>θ</sub> = σcos²θ e τ<sub>θ</sub> = σ·senθ·cosθ. O cisalhamento é máximo em θ = 45°, com <b>τ<sub>máx</sub> = σ/2</b>. É por isso que materiais dúcteis, fracos ao cisalhamento, escoam com bandas a 45° no ensaio de tração.")

# R15 balanço com carga distribuída
w, L = 2, 3
M = w * L ** 2 / 2
num("MEC-R15", R, "Momento no engaste de viga em balanço",
    "Uma viga em balanço de 3 m de comprimento recebe carga uniformemente distribuída de 2 kN/m em todo o vão. O momento fletor no engaste, em kN·m, é",
    M, [w * L ** 2 / 8, w * L ** 2 / 4, w * L, w * L ** 2], d=2,
    res=f"A resultante (wL = 6 kN) atua no meio do vão, a L/2 do engaste: M = wL·L/2 = wL²/2 = <b>{br(M,2)} kN·m</b>. wL²/8 = 2,25 kN·m é o momento da viga biapoiada.")

# R16 esbeltez
d, L = 40, 2000
r = d / 4; lam = L / r
num("MEC-R16", R, "Índice de esbeltez",
    "Uma barra de seção circular maciça com 40 mm de diâmetro e 2 m de comprimento é biarticulada. Seu índice de esbeltez é",
    lam, [L / (d / 2), L / d, 2 * L / r, 141], d=0,
    res=f"Raio de giração: r = √(I/A) = √[(πd⁴/64)/(πd²/4)] = d/4 = 10 mm. λ = L<sub>e</sub>/r = 2.000/10 = <b>{br(lam,0)}</b>. Usar o raio geométrico (20 mm) no lugar do raio de giração dá 100.")

# R17 espessura de vaso cilíndrico
t = 1.5 * 1200 / (2 * 120)
num("MEC-R17", R, "Espessura de vaso de pressão cilíndrico",
    "Um vaso cilíndrico de parede fina com 1.200 mm de diâmetro vai operar a 1,5 MPa. Com tensão admissível de 120 MPa, a espessura mínima de parede, desprezando sobre-espessura de corrosão e eficiência de junta, em mm, é",
    t, [t / 2, 2 * t, 10, 4 * t], d=2,
    res=f"A tensão circunferencial é a que governa: σ<sub>θ</sub> = pD/(2t) → t = pD/(2σ) = 1,5 × 1.200/(2 × 120) = <b>{br(t,2)} mm</b>. Usar pD/(4σ) (3,75 mm) dimensiona pela tensão longitudinal, que é a metade.")

# R18 barras em paralelo
EA_a, EA_c = 200 * 150, 100 * 200
Fa = 100 * EA_a / (EA_a + EA_c)
num("MEC-R18", R, "Barras em paralelo (estaticamente indeterminado)",
    "Uma carga de 100 kN é sustentada por duas barras verticais de mesmo comprimento, ligadas a um bloco rígido que desce sem girar: uma de aço (E = 200 GPa; A = 150 mm²) e outra de cobre (E = 100 GPa; A = 200 mm²). A força na barra de aço, em kN, é",
    Fa, [50, 100 - Fa, 100 * 150 / 350, 100 * 200 / 300], d=1,
    res=f"Mesmo alongamento: F<sub>a</sub>/(EA)<sub>a</sub> = F<sub>c</sub>/(EA)<sub>c</sub>. Rigidezes: (EA)<sub>a</sub> = 30.000 kN e (EA)<sub>c</sub> = 20.000 kN. F<sub>a</sub> = 100 × 30/50 = <b>{br(Fa,1)} kN</b>. A carga se divide pela rigidez EA, não pela área nem meio a meio.")

# R19 eixos paralelos
b, h = 60, 120
Ib = b * h ** 3 / 3 / 1e4
num("MEC-R19", R, "Teorema dos eixos paralelos",
    "O momento de inércia de um retângulo de 60 mm de base e 120 mm de altura, em relação a um eixo que coincide com a sua base, em cm⁴, é",
    Ib, [Ib / 4, Ib / 2, 2 * Ib, 3 * Ib / 4], d=0,
    res=f"I<sub>CG</sub> = bh³/12 = 6 × 12³/12 = 864 cm⁴. Pelo teorema dos eixos paralelos: I<sub>base</sub> = I<sub>CG</sub> + A·d² = 864 + 72 × 6² = <b>{br(Ib,0)} cm⁴</b> = bh³/3, quatro vezes o valor centroidal.")

con("MEC-R20", R, "Curva tensão-deformação",
    "Na curva tensão-deformação de engenharia de um aço dúctil, obtida no ensaio de tração, o limite de resistência à tração corresponde",
    "à máxima tensão de engenharia da curva, a partir da qual começa a estricção do corpo de prova",
    ["à tensão em que o material começa a se deformar plasticamente",
     "à tensão no momento da ruptura, sempre a maior da curva",
     "ao fim do trecho linear, onde deixa de valer a lei de Hooke",
     "à tensão necessária para produzir 0,2% de deformação permanente"],
    res="O <b>limite de resistência</b> é o ponto mais alto da curva de engenharia: dali em diante a deformação se concentra num pescoço (estricção) e a força cai. Escoamento e limite de proporcionalidade vêm antes; 0,2% de deformação permanente define o escoamento convencional; e, na curva de engenharia, a tensão de ruptura de um aço dúctil é menor que o limite de resistência.")
