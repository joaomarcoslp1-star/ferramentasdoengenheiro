# -*- coding: utf-8 -*-
# Lote 2 (28/11/2026): Termodinâmica, Mecânica dos Fluidos, Resistência dos Materiais
import math
from nbase import num, con, br

T = "Termodinâmica"
Q = 20 * (3200 - 200) / 1000
num("MEC-T21", T, "Calor na caldeira (volume de controle)",
    "Uma caldeira recebe 20 kg/s de água de alimentação com entalpia de 200 kJ/kg e entrega vapor superaquecido com 3.200 kJ/kg. A taxa de calor fornecida à água, em MW, é",
    Q, [64, 3.0, 4.0, 600], d=1,
    res=f"Regime permanente, sem trabalho: Q̇ = ṁ(h<sub>s</sub> − h<sub>e</sub>) = 20 × (3.200 − 200) = 60.000 kW = <b>{br(Q,1)} MW</b>. Somar as entalpias ou usar só a de saída (64 MW) ignora a energia que a água já traz.")

dT = (200 ** 2 - 20 ** 2) / (2 * 1000)
num("MEC-T22", T, "Difusor adiabático",
    "Ar (c<sub>p</sub> = 1,0 kJ/kg·K) entra num difusor adiabático a 200 m/s e sai a 20 m/s. Desprezando variações de energia potencial, o aumento de temperatura do ar, em K, é, aproximadamente,",
    dT, [2 * dT, 180, 18, 0.0198], d=1,
    res=f"Sem calor nem trabalho: c<sub>p</sub>ΔT = (V<sub>1</sub>² − V<sub>2</sub>²)/2 → ΔT = (40.000 − 400)/(2 × 1.000) = <b>{br(dT,1)} K</b>. Atenção: V² em m²/s² dá J/kg, por isso c<sub>p</sub> entra como 1.000 J/kg·K. O difusor converte energia cinética em entalpia (pressão e temperatura sobem).")

con("MEC-T23", T, "Ciclos Stirling e Ericsson",
    "Os ciclos ideais de Stirling e de Ericsson, com regeneração perfeita, operando entre as temperaturas T<sub>H</sub> e T<sub>L</sub>, têm rendimento térmico",
    "igual ao do ciclo de Carnot entre as mesmas temperaturas, pois todo o calor externo é trocado de forma isotérmica",
    ["igual ao do ciclo Otto de mesma taxa de compressão",
     "sempre menor que o do ciclo Brayton",
     "nulo, pois o calor regenerado não produz trabalho",
     "maior que o do ciclo de Carnot, graças ao regenerador"],
    res="No Stirling (duas isotérmicas e duas isocóricas) e no Ericsson (duas isotérmicas e duas isobáricas), o regenerador devolve internamente o calor dos processos intermediários. O calor externo entra só a T<sub>H</sub> e sai só a T<sub>L</sub>: rendimento <b>igual ao de Carnot</b>, nunca maior.")

q = 2 * 4.18 * 80 + 2 * 2257
num("MEC-T24", T, "Calor sensível e latente",
    "Deseja-se transformar 2 kg de água líquida a 20 °C em vapor saturado a 100 °C, à pressão atmosférica. Com c = 4,18 kJ/kg·K e calor latente de vaporização de 2.257 kJ/kg, a energia necessária, em kJ, é, aproximadamente,",
    q, [2 * 2257, 2 * 4.18 * 80, 2257 + 4.18 * 80, 2 * 4.18 * 100 + 2 * 2257], d=0,
    res=f"Aquecer o líquido: 2 × 4,18 × 80 = 669 kJ. Vaporizar: 2 × 2.257 = 4.514 kJ. Total: <b>{br(q,0)} kJ</b>. A vaporização consome quase sete vezes mais energia que o aquecimento de 20 a 100 °C.")

Mm = 0.6 * 28 + 0.4 * 44
num("MEC-T25", T, "Massa molar de mistura de gases",
    "Uma mistura de gases ideais tem 60% de N<sub>2</sub> (M = 28 kg/kmol) e 40% de CO<sub>2</sub> (M = 44 kg/kmol), em base molar. A massa molar aparente da mistura, em kg/kmol, é",
    Mm, [36.0, 0.4 * 28 + 0.6 * 44, 72, 30.4], d=1,
    res=f"M = Σy<sub>i</sub>M<sub>i</sub> = 0,6 × 28 + 0,4 × 44 = 16,8 + 17,6 = <b>{br(Mm,1)} kg/kmol</b>. A média simples (36) ignora a composição; trocar as frações dá 37,6. A constante da mistura é R = 8,314/34,4 = 0,242 kJ/kg·K.")

con("MEC-T26", T, "Diagrama T-s",
    "Num diagrama temperatura-entropia (T-s), a área sob a curva de um processo internamente reversível representa",
    "o calor trocado por unidade de massa",
    ["o trabalho de fronteira por unidade de massa",
     "a variação de entalpia",
     "a variação de energia interna",
     "a entropia gerada"],
    res="Para processo reversível, δq = T·ds, logo q = ∫T·ds: <b>área sob a curva no T-s</b>. Num ciclo, a área interna é o calor líquido, igual ao trabalho líquido. O trabalho de fronteira é a área sob a curva no diagrama P-v.")

v = 0.001043 + 0.3 * (1.694 - 0.001043); V = 4 * v
num("MEC-T27", T, "Volume de mistura líquido-vapor",
    "Um tanque contém 4 kg de água a 100 kPa, como mistura saturada com título 0,3. A 100 kPa: v<sub>l</sub> = 0,001043 m³/kg e v<sub>v</sub> = 1,694 m³/kg. O volume do tanque, em m³, é, aproximadamente,",
    V, [4 * 0.7 * 1.694, 4 * 1.694, 0.3 * 1.694, 4 * 0.001043], d=2,
    res=f"v = v<sub>l</sub> + x(v<sub>v</sub> − v<sub>l</sub>) = 0,001043 + 0,3 × 1,693 = 0,509 m³/kg. V = m·v = 4 × 0,509 = <b>{br(V,2)} m³</b>. Usar (1 − x) no lugar de x (4,74 m³) troca vapor por líquido: o título é a fração de vapor.")

eta = 1 - 200 / 800
num("MEC-T28", T, "Efeito das temperaturas no rendimento de Carnot",
    "Uma máquina de Carnot opera entre 800 K e 300 K. Se a temperatura do reservatório frio for reduzida em 100 K, mantida a do quente, o novo rendimento será",
    eta, [1 - 300 / 900, 1 - 300 / 800, 1 - 200 / 900, 0.5], fmt=lambda v: br(100 * v, 1) + "%",
    res=f"Original: 1 − 300/800 = 62,5%. Novo: 1 − 200/800 = <b>{br(100*eta,1)}%</b>. Elevar T<sub>H</sub> em 100 K daria só 66,7%: reduzir T<sub>L</sub> rende mais, porque T<sub>L</sub> está no numerador da razão T<sub>L</sub>/T<sub>H</sub>.")

Pb = 0.001 * (10000 - 10) * 50
num("MEC-T29", T, "Trabalho da bomba (líquido incompressível)",
    "Uma bomba eleva a pressão de 50 kg/s de água (v = 0,001 m³/kg) de 10 kPa para 10 MPa, de forma isentrópica. A potência teórica da bomba, em kW, é, aproximadamente,",
    Pb, [Pb / 50, Pb * 2, Pb / 10, 50000], d=0,
    res=f"Líquido incompressível: w = v·ΔP = 0,001 × (10.000 − 10) = 9,99 kJ/kg. Ẇ = 50 × 9,99 = <b>{br(Pb,0)} kW</b>. É pouco perto da turbina de uma termelétrica (dezenas de MW): bombear líquido custa muito menos que comprimir gás.")

con("MEC-T30", T, "Temperatura de ponto de orvalho",
    "A temperatura de ponto de orvalho do ar úmido é",
    "a temperatura de saturação da água correspondente à pressão parcial do vapor no ar, abaixo da qual começa a condensação no resfriamento a pressão constante",
    ["a temperatura lida num termômetro com bulbo envolto em gaze molhada",
     "sempre igual à temperatura de bulbo seco",
     "a temperatura em que a umidade relativa é zero",
     "a temperatura de ebulição da água à pressão atmosférica"],
    res="Resfriando o ar sem mudar sua umidade absoluta, a pressão parcial do vapor fica constante; quando T chega à <b>saturação correspondente a p<sub>v</sub></b>, a umidade relativa vale 100% e começa a condensação. A gaze molhada mede o bulbo úmido; ponto de orvalho ≤ bulbo úmido ≤ bulbo seco.")

F = "Mecânica dos Fluidos"
con("MEC-F21", F, "Paradoxo hidrostático",
    "Três recipientes de formatos diferentes (um cilíndrico, um que se alarga para cima e outro que se estreita para cima) têm fundos de mesma área e estão cheios de água até a mesma altura. A força exercida pela água sobre o fundo",
    "é a mesma nos três, pois depende apenas da altura da coluna, da massa específica e da área do fundo",
    ["é maior no recipiente que se alarga para cima, pois ele contém mais água",
     "é maior no recipiente que se estreita para cima, pois a pressão se concentra",
     "é igual ao peso da água contida em cada recipiente",
     "depende da forma das paredes laterais, mas não da altura"],
    res="A pressão no fundo é ρgh, igual nos três; logo F = ρgh·A também. Nos recipientes não cilíndricos, as paredes inclinadas sustentam (ou empurram) parte do peso: a força no fundo <b>não é</b> o peso do líquido. É o paradoxo hidrostático de Stevin e Pascal.")

dp = 1000 * 10 * 0.2 * 0.5
num("MEC-F22", F, "Manômetro de tubo inclinado",
    "Um manômetro de tubo inclinado a 30° com a horizontal, com água (ρ = 1.000 kg/m³), indica um deslocamento de 200 mm ao longo do tubo. Com g = 10 m/s², a diferença de pressão medida, em Pa, é",
    dp, [2000, 1732, 500, 20], d=0,
    res=f"A altura vertical é L·senθ = 200 × 0,5 = 100 mm. Δp = ρg·L·senθ = 1.000 × 10 × 0,1 = <b>{br(dp,0)} Pa</b>. A inclinação amplia a leitura (200 mm para 100 mm de coluna), melhorando a precisão em pressões pequenas.")

rho = 30 / (30 - 20) * 1000
num("MEC-F23", F, "Massa específica pelo peso aparente",
    "Uma pedra pesa 30 N no ar e 20 N quando totalmente submersa em água (ρ = 1.000 kg/m³). A massa específica da pedra, em kg/m³, é",
    rho, [1500, 2000, 1000, 667], d=0,
    res=f"Empuxo = 30 − 20 = 10 N = ρ<sub>água</sub>·g·V. Logo ρ<sub>pedra</sub>/ρ<sub>água</sub> = P/E = 30/10 = 3 → <b>{br(rho,0)} kg/m³</b>. É o método de Arquimedes para a coroa do rei Hierão. 1.500 kg/m³ seria dividir pelo peso aparente.")

v2 = 2 * 10 / 1
num("MEC-F24", F, "Continuidade em escoamento compressível",
    "Um gás escoa em regime permanente num duto de seção constante. Na entrada, a massa específica é 2,0 kg/m³ e a velocidade, 10 m/s. Na saída, a massa específica caiu para 1,0 kg/m³. A velocidade na saída, em m/s, é",
    v2, [10, 5, 14.1, 40], d=1,
    res=f"Vazão mássica constante: ρ<sub>1</sub>V<sub>1</sub>A = ρ<sub>2</sub>V<sub>2</sub>A → V<sub>2</sub> = 2 × 10/1 = <b>{br(v2,1)} m/s</b>. A continuidade Q = AV (vazão volumétrica constante) só vale para escoamento incompressível.")

Re = 1 * 0.05 / 1e-4; f = 64 / Re
num("MEC-F25", F, "Fator de atrito laminar",
    "Óleo (ν = 1 × 10<sup>−4</sup> m²/s) escoa a 1 m/s num tubo de 50 mm. O fator de atrito de Darcy é",
    f, [16 / Re, 0.0128, 0.064, 1.28], d=3,
    res=f"Re = VD/ν = 1 × 0,05/10<sup>−4</sup> = 500: laminar. f = 64/Re = <b>{br(f,3)}</b>. O valor 16/Re (0,032) é o fator de Fanning, quatro vezes menor; misturar os dois é a pegadinha mais comum em perda de carga.")

p = 0.5 * 1000 * 20 ** 2 / 1000
num("MEC-F26", F, "Pressão para formar um jato",
    "Água (ρ = 1.000 kg/m³) sai por um bocal para a atmosfera com velocidade de 20 m/s. A velocidade a montante do bocal é desprezível e não há perdas. A pressão manométrica a montante do bocal, em kPa, é",
    p, [2 * p, p / 10, p / 2, 2.0], d=0,
    res=f"Bernoulli: p<sub>1</sub>/ρ = V<sub>2</sub>²/2 → p<sub>1</sub> = ½ × 1.000 × 400 = 200.000 Pa = <b>{br(p,0)} kPa</b> (≈ 2 bar ou 20 m de coluna d'água). Esquecer o ½ dobra o resultado.")

h = 12 ** 2 / (2 * 10)
num("MEC-F27", F, "Altura de jato vertical",
    "Um esguicho lança um jato de água verticalmente para cima com velocidade de 12 m/s na saída. Desprezando o atrito com o ar e com g = 10 m/s², a altura máxima atingida pelo jato, em m, é",
    h, [14.4, 1.2, 3.6, 0.6], d=1,
    res=f"Toda a energia cinética vira potencial: h = V²/(2g) = 144/20 = <b>{br(h,1)} m</b>. Sem o 2 do denominador, o resultado dobraria (14,4 m).")

con("MEC-F28", F, "Número de Froude em canais",
    "Num canal aberto, a água escoa com velocidade média de 6 m/s e profundidade de 0,9 m (g = 10 m/s²). Sobre esse escoamento, é correto afirmar que",
    "o número de Froude vale 2, o regime é supercrítico, e uma perturbação na superfície não consegue se propagar para montante",
    ["o número de Froude vale 2 e o regime é subcrítico",
     "o número de Froude vale 0,5 e o regime é supercrítico",
     "o número de Froude vale 1, o regime é crítico, com energia específica máxima",
     "o número de Froude vale 6,7 e o escoamento é laminar"],
    res="Fr = V/√(gy) = 6/√9 = <b>2 &gt; 1: supercrítico</b> (rápido). A velocidade da onda (√(gy) = 3 m/s) é menor que a do escoamento, então perturbações só descem o canal. Ao passar para subcrítico, forma-se um ressalto hidráulico. No regime crítico (Fr = 1), a energia específica é mínima, não máxima.")

con("MEC-F29", F, "Fluidos não newtonianos",
    "Um fluido que só começa a escoar depois que a tensão de cisalhamento aplicada supera um valor limite e, a partir daí, se comporta de forma aproximadamente linear (como pasta de dente ou lama de perfuração) é classificado como",
    "plástico de Bingham",
    ["pseudoplástico, cuja viscosidade aparente aumenta com a taxa de deformação",
     "dilatante, cuja viscosidade aparente diminui com a taxa de deformação",
     "newtoniano de alta viscosidade",
     "fluido ideal (invíscido)"],
    res="O <b>plástico de Bingham</b> tem tensão limite de escoamento: τ = τ<sub>0</sub> + μ<sub>p</sub>·(du/dy). Pseudoplásticos (tintas, polímeros) ficam <i>menos</i> viscosos com a agitação; dilatantes (amido em água) ficam <i>mais</i>. As alternativas trocam essas definições.")

Fr = 1000 * 0.001 * 10 ** 2
num("MEC-F30", F, "Força de reação de um jato",
    "Água (ρ = 1.000 kg/m³) sai horizontalmente por um orifício de 10 cm² na lateral de um tanque apoiado sobre rodas, com velocidade de 10 m/s. A força de reação sobre o tanque, em N, é",
    Fr, [10, 50, 200, 1000], d=0,
    res=f"F = ṁV = ρAV² = 1.000 × 0,001 × 100 = <b>{br(Fr,0)} N</b>, no sentido oposto ao jato. É o mesmo princípio da propulsão a jato e dos foguetes. ρAV (10 kg/s) é a vazão mássica, não a força.")

R = "Resistência dos Materiais"
num("MEC-R21", R, "Efeito do diâmetro na torção",
    "Um eixo maciço apresenta tensão de cisalhamento máxima de 80 MPa sob certo torque. Se o eixo for substituído por outro, do mesmo material, com o dobro do diâmetro, a tensão máxima para o mesmo torque, em MPa, será",
    10, [40, 20, 5, 160], d=0,
    res="τ = 16T/(πd³): a tensão cai com o cubo do diâmetro. Dobrar d divide τ por 2³ = 8: 80/8 = <b>10 MPa</b>. O ângulo de torção cairia ainda mais, com d⁴ (16 vezes).")

f = 10000 * 4 ** 3 / (48 * 200e9 * 2e-5) * 1000
num("MEC-R22", R, "Flecha com carga concentrada no meio do vão",
    "Uma viga biapoiada de aço (E = 200 GPa) com 4 m de vão e I = 2.000 cm⁴ recebe uma carga concentrada de 10 kN no meio do vão. A flecha máxima, em mm, é, aproximadamente,",
    f, [4 * f, f / 2, 16 * f, 10 * f], d=2,
    res=f"f = PL³/(48EI) = 10.000 × 64/(48 × 200 × 10⁹ × 2 × 10<sup>−5</sup>) = 640.000/192 × 10⁶ = 0,00333 m = <b>{br(f,2)} mm</b>. Conversão: 2.000 cm⁴ = 2 × 10<sup>−5</sup> m⁴. Para o balanço com carga na ponta, PL³/(3EI) daria 16 vezes mais.")

s = 20000 / (20 * 10)
num("MEC-R23", R, "Tensão de esmagamento (contato)",
    "Um pino de 20 mm de diâmetro atravessa uma chapa de 10 mm de espessura e transmite uma força de 20 kN. A tensão de esmagamento (contato) na chapa, em MPa, é",
    s, [20000 / (math.pi * 20 * 10), 20000 / (math.pi * 10 ** 2), 2 * s, s / 2], d=1,
    res=f"A tensão de esmagamento usa a área projetada do furo: σ<sub>e</sub> = F/(d·t) = 20.000/(20 × 10) = <b>{br(s,1)} MPa</b>. A área do semicilindro (π·d·t/2) ou a área do círculo não são as usadas nas normas.")

con("MEC-R24", R, "Cisalhamento puro",
    "Num ponto de um eixo sob torção pura, o estado de tensões é de cisalhamento puro, com τ = 50 MPa nos planos transversal e longitudinal. As tensões principais nesse ponto são",
    "+50 MPa e −50 MPa, em planos a 45° do eixo",
    ["50 MPa e 0, nos mesmos planos do cisalhamento",
     "+100 MPa e −100 MPa, em planos a 45°",
     "+25 MPa e −25 MPa, em planos a 30°",
     "nulas, pois não há tensão normal aplicada"],
    res="No círculo de Mohr do cisalhamento puro, o centro está na origem e o raio é τ: <b>σ<sub>1</sub> = +τ e σ<sub>2</sub> = −τ</b>, a 45°. Por isso um giz torcido (frágil, fraco à tração) rompe numa hélice a 45°, enquanto um eixo dúctil rompe na seção transversal, por cisalhamento.")

U = 20000 ** 2 * 2000 / (2 * 200000 * 100) / 1000
num("MEC-R25", R, "Energia de deformação axial",
    "Uma barra de aço (E = 200 GPa) com 2 m de comprimento e 100 mm² de seção é tracionada elasticamente por 20 kN. A energia de deformação armazenada, em J, é",
    U, [2 * U, U / 2, 2.0, 200], d=0,
    res=f"U = F²L/(2EA) = 20.000² × 2.000/(2 × 200.000 × 100) = 20.000 N·mm = <b>{br(U,0)} J</b>. É a área do triângulo sob a reta força × alongamento (½·F·δ, com δ = 2 mm).")

con("MEC-R26", R, "Eficiência de seções vazadas",
    "Comparando uma barra maciça e um tubo de mesma área de seção transversal (mesmo peso por metro) e mesmo material, é correto afirmar que o tubo",
    "tem maior momento de inércia e maior módulo resistente, sendo mais eficiente à flexão, à torção e à flambagem",
    ["tem o mesmo momento de inércia, pois a área é igual",
     "resiste mais à tração, pois a tensão normal depende do diâmetro externo",
     "é menos eficiente à flexão, pois tem menos material no centro",
     "só é vantajoso à torção, nunca à flexão"],
    res="I e J dependem da distância da área ao eixo (∫y²dA). O tubo afasta o material do centro, onde a tensão é pequena. Com a mesma área, I, W e J crescem: <b>tubos e perfis I são mais eficientes</b>. À tração pura, só a área importa, e as duas peças são iguais.")

st = 200000 * (12e-6 * 50 * 1000 - 0.3) / 1000
num("MEC-R27", R, "Tensão térmica com folga",
    "Uma barra de aço (E = 200 GPa; α = 12 × 10<sup>−6</sup> °C<sup>−1</sup>) de 1 m está entre dois apoios rígidos, com folga de 0,3 mm a 20 °C. A temperatura sobe para 70 °C. A tensão de compressão na barra, em MPa, é",
    st, [120, 0, 30, 90], d=0,
    res=f"Dilatação livre: αLΔT = 12 × 10<sup>−6</sup> × 1.000 × 50 = 0,6 mm. A folga absorve 0,3 mm; os outros 0,3 mm são impedidos: σ = E·δ/L = 200.000 × 0,3/1.000 = <b>{br(st,0)} MPa</b>. Sem folga, seriam 120 MPa.")

scr = math.pi ** 2 * 200000 / 100 ** 2
num("MEC-R28", R, "Tensão crítica de Euler",
    "Uma coluna de aço (E = 200 GPa) tem índice de esbeltez igual a 100. Pela fórmula de Euler, a tensão crítica de flambagem, em MPa, é, aproximadamente,",
    scr, [2 * scr, scr / 4, 20, 2000], d=0,
    res=f"σ<sub>cr</sub> = π²E/λ² = 9,87 × 200.000/10.000 = <b>{br(scr,0)} MPa</b>. Se esse valor superasse o limite de proporcionalidade (colunas curtas, λ pequeno), a fórmula de Euler deixaria de valer e seria preciso usar fórmulas inelásticas (Johnson, normas).")

Am = math.pi * 50 ** 2; tau = 2e6 / (2 * Am * 4)
num("MEC-R29", R, "Torção em tubo de parede fina (Bredt)",
    "Um tubo de parede fina com raio médio de 50 mm e espessura de 4 mm é submetido a um torque de 2 kN·m. Pela fórmula de Bredt, a tensão de cisalhamento média na parede, em MPa, é, aproximadamente,",
    tau, [2 * tau, tau / 2, 2e6 / (2 * math.pi * 50 * 4), 4 * tau], d=1,
    res=f"Área limitada pela linha média: A<sub>m</sub> = π × 50² = 7.854 mm². τ = T/(2A<sub>m</sub>t) = 2 × 10⁶/(2 × 7.854 × 4) = <b>{br(tau,1)} MPa</b>. A fórmula vale para qualquer seção fechada de parede fina.")

M = 6 * 4 ** 2 / 12
num("MEC-R30", R, "Momento no engaste de viga biengastada",
    "Uma viga biengastada de 4 m de vão recebe carga uniformemente distribuída de 6 kN/m. O momento fletor nos engastes, em kN·m, é",
    M, [12, 4, 48, 24], d=0,
    res=f"Na viga biengastada com carga uniforme, M<sub>engaste</sub> = wL²/12 = 6 × 16/12 = <b>{br(M,0)} kN·m</b> e, no meio do vão, wL²/24 = 4 kN·m. Na biapoiada, o momento máximo seria wL²/8 = 12 kN·m: o engaste reduz o pico e o distribui.")
