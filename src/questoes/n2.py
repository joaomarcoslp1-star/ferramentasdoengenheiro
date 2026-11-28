# -*- coding: utf-8 -*-
# Lote 1 (28/11/2026): Elementos de Máquinas, Transferência de Calor, Materiais, Máquinas de Fluxo, Vibrações, Fabricação
import math
from nbase import num, con, br

E = "Elementos de Máquinas"
s = 25000 / 84.3
num("MEC-E09", E, "Tensão no parafuso pela área resistente",
    "Um parafuso M12 (área resistente à tração de 84,3 mm²) recebe uma pré-carga de 25 kN. A tensão de tração no núcleo do parafuso, em MPa, é, aproximadamente,",
    s, [25000 / (math.pi * 12 ** 2 / 4), 2 * s, s / 2, 25000 / 144], d=0,
    res=f"σ = F/A<sub>t</sub> = 25.000/84,3 = <b>{br(s,0)} MPa</b>. Usar a área do diâmetro nominal (113 mm²) subestima a tensão em cerca de 25%: a rosca retira material, e o que resiste é a área de tensão tabelada.")

v = math.pi * 0.2 * 1200 / 60
num("MEC-E10", E, "Velocidade tangencial de engrenagem",
    "Uma engrenagem com diâmetro primitivo de 200 mm gira a 1.200 rpm. A velocidade tangencial no diâmetro primitivo, em m/s, é, aproximadamente,",
    v, [v / 2, 2 * v, math.pi * 0.2 * 1200, 1.26], d=2,
    res=f"v = π·d·n/60 = π × 0,2 × 1.200/60 = <b>{br(v,2)} m/s</b>. Essa velocidade define a classe de qualidade da engrenagem e o tipo de lubrificação. Usar o raio dá a metade; esquecer o /60 dá m/min.")

Ft = 2 * 300 / 0.150; Fr = Ft * 0.364
num("MEC-E11", E, "Força radial em engrenagem de dentes retos",
    "Um pinhão de dentes retos com diâmetro primitivo de 150 mm e ângulo de pressão de 20° transmite 300 N·m. Com tg 20° ≈ 0,364, sen 20° ≈ 0,342 e cos 20° ≈ 0,940, a força radial no dente, em N, é, aproximadamente,",
    Fr, [Ft, Ft * 0.342, Ft * 0.940, Ft / 2 * 0.364], d=0,
    res=f"Força tangencial: F<sub>t</sub> = T/(d/2) = 300/0,075 = 4.000 N. Força radial: F<sub>r</sub> = F<sub>t</sub>·tg α = 4.000 × 0,364 = <b>{br(Fr,0)} N</b>. É ela que empurra o pinhão para longe da coroa e carrega os mancais. Usar T/d no lugar de T/(d/2) dá a metade.")

p = 12000 / (60 * 50)
num("MEC-E12", E, "Pressão média em mancal de deslizamento",
    "Um mancal de deslizamento com 60 mm de diâmetro e 50 mm de comprimento suporta carga radial de 12 kN. A pressão média projetada no mancal, em MPa, é",
    p, [12000 / (math.pi * 60 * 50), 2 * p, p / 2, 0.4], d=2,
    res=f"A pressão média usa a área projetada (L × d): p = F/(L·d) = 12.000/(50 × 60) = <b>{br(p,2)} MPa</b>. A área lateral (π·d·L) não é a área que suporta a carga radial.")

num("MEC-E13", E, "Ajuste com interferência",
    "Num ajuste 40 H7/p6, o furo tem afastamentos 0 e +0,025 mm, e o eixo, +0,026 e +0,042 mm. A interferência máxima do ajuste, em mm, é",
    0.042, [0.001, 0.017, 0.026, 0.067], d=3,
    res="Interferência máxima = maior eixo − menor furo = 40,042 − 40,000 = <b>0,042 mm</b>. A mínima é menor eixo − maior furo = 40,026 − 40,025 = 0,001 mm. Como o eixo é sempre maior que o furo, é um ajuste prensado.")

con("MEC-E14", E, "Acoplamentos para desalinhamento angular",
    "Para transmitir torque entre dois eixos com desalinhamento angular grande e variável durante a operação, como no eixo de transmissão de um caminhão, o elemento mais indicado é",
    "a junta universal (cardã), de preferência em par para anular a flutuação de velocidade",
    ["o acoplamento rígido de flanges",
     "a chaveta paralela",
     "o acoplamento de garras com elemento elástico, projetado para desalinhamentos de poucos décimos de grau",
     "a luva de compressão (acoplamento de luva bipartida)"],
    res="A <b>junta universal</b> admite ângulos de dezenas de graus. Uma única cruzeta faz a velocidade de saída oscilar duas vezes por volta; com duas juntas em fase e ângulos iguais, a oscilação se cancela. Acoplamentos rígidos não toleram desalinhamento, e os elásticos comuns aceitam só valores pequenos.")

Tf = 0.35 * 2000 * 0.2
num("MEC-E15", E, "Torque de freio de sapata",
    "Uma sapata pressiona um tambor de freio de 400 mm de diâmetro com força normal de 2 kN. Com coeficiente de atrito 0,35, o torque de frenagem, em N·m, é",
    Tf, [2 * Tf, 2000 * 0.2, Tf / 2, 1400], d=0,
    res=f"F<sub>atrito</sub> = μN = 0,35 × 2.000 = 700 N. T = F<sub>atrito</sub> × r = 700 × 0,2 = <b>{br(Tf,0)} N·m</b>. Usar o diâmetro (0,4 m) no lugar do raio dobra o torque.")

A1 = math.pi * 16 ** 2 / 4; tau = 60000 / (4 * A1)
num("MEC-E16", E, "Junta rebitada em cisalhamento",
    "Duas chapas sobrepostas são unidas por 4 rebites de 16 mm de diâmetro, em cisalhamento simples, e transmitem 60 kN. Admitindo divisão igual da carga, a tensão de cisalhamento nos rebites, em MPa, é, aproximadamente,",
    tau, [4 * tau, tau / 2, 60000 / (4 * 16 ** 2), 2 * tau], d=1,
    res=f"Área de um rebite: π × 16²/4 = {br(A1,0)} mm². τ = F/(n·A) = 60.000/(4 × 201) = <b>{br(tau,1)} MPa</b>. Em cisalhamento duplo, a tensão cairia à metade.")

w = 2 * math.pi * 600 / 60; Ec = 0.5 * 10 * w ** 2 / 1000
num("MEC-E17", E, "Energia cinética de volante",
    "Um volante com momento de inércia de 10 kg·m² gira a 600 rpm. Sua energia cinética, em kJ, é, aproximadamente,",
    Ec, [2 * Ec, 0.5 * 10 * 600 ** 2 / 1000, 0.5, 3.14], d=None,
    res=f"ω = 2π × 600/60 = 62,8 rad/s. E = ½Iω² = 0,5 × 10 × 62,8² = 19.739 J ≈ <b>{br(Ec,1)} kJ</b>. Usar rpm direto na fórmula dá 1.800 kJ. Como a energia cresce com ω², volantes rápidos guardam muito mais energia.")

con("MEC-E18", E, "Designação de rolamentos",
    "Na designação usual de rolamentos (ISO), um rolamento rígido de esferas 6205 tem diâmetro do furo de",
    "25 mm, pois, a partir do código 04, o diâmetro do furo é o número formado pelos dois últimos algarismos multiplicado por 5",
    ["5 mm, igual ao último algarismo",
     "205 mm, igual ao número de série",
     "52 mm, que corresponde ao diâmetro externo",
     "62 mm, indicado pelos dois primeiros algarismos"],
    res="No 6205: <b>6</b> = rígido de esferas; <b>2</b> = série de dimensões; <b>05</b> × 5 = <b>25 mm</b> de furo. As exceções são 00 = 10 mm, 01 = 12 mm, 02 = 15 mm e 03 = 17 mm. O diâmetro externo do 6205 (52 mm) vem do catálogo.")

C = "Transferência de Calor"
L = 0.04 * 100 / 50 * 1000
num("MEC-C09", C, "Espessura de isolamento",
    "Uma parede de câmara frigorífica terá isolamento de poliuretano (k = 0,04 W/m·K) com diferença de 100 °C entre as faces. Para limitar o fluxo de calor a 50 W/m², a espessura mínima de isolamento, em mm, é",
    L, [L / 4, L * 1.5625, L / 10, L * 10], d=0,
    res=f"q'' = kΔT/L → L = kΔT/q'' = 0,04 × 100/50 = 0,08 m = <b>{br(L,0)} mm</b>. Isolantes têm k cerca de 20 a 1.000 vezes menor que alvenaria e metais, por isso poucos centímetros bastam.")

Lc = 0.010 / 3; Bi = 50 * Lc / 40
num("MEC-C10", C, "Número de Biot",
    "Uma esfera de aço (k = 40 W/m·K) com raio de 10 mm é resfriada por convecção com h = 50 W/m²·K. Usando o comprimento característico L<sub>c</sub> = V/A, o número de Biot é, aproximadamente,",
    Bi, [50 * 0.010 / 40, 50 * 0.020 / 40, 50 * 0.010 / 6 / 40, 40 / (50 * Lc)], fmt=lambda v: br(v, 4) if v < 1 else br(v, 0),
    res=f"Para esfera, L<sub>c</sub> = V/A = (4πr³/3)/(4πr²) = r/3 = 3,33 mm. Bi = hL<sub>c</sub>/k = 50 × 0,00333/40 = <b>{br(Bi,4)}</b>. Como Bi &lt; 0,1, a temperatura dentro da esfera é praticamente uniforme e vale o modelo de capacitância global.")

lam = 2898 / 5800
num("MEC-C11", C, "Lei do deslocamento de Wien",
    "Considerando o Sol como corpo negro a 5.800 K e a constante de Wien igual a 2.898 µm·K, o comprimento de onda de máxima emissão, em µm, é, aproximadamente,",
    lam, [1.0, 0.25, 2.0, 5.0], d=2,
    res=f"λ<sub>máx</sub>·T = 2.898 µm·K → λ<sub>máx</sub> = 2.898/5.800 = <b>{br(lam,2)} µm</b>, no meio do espectro visível. Um corpo a 300 K emite em torno de 10 µm (infravermelho): por isso o vidro deixa o sol entrar e segura o calor da estufa.")

A1 = math.pi * 0.5 ** 2; F21 = A1 / 6
num("MEC-C12", C, "Fator de forma e reciprocidade",
    "Uma esfera de 0,5 m de diâmetro (superfície 1) está no interior de uma caixa cúbica de 1 m de aresta (superfície 2). Usando a reciprocidade, o fator de forma F<sub>21</sub> (da caixa para a esfera) é, aproximadamente,",
    F21, [1.0, 1 - F21, 0.5, 1 / 6], d=3,
    res=f"Toda a radiação que sai da esfera atinge a caixa: F<sub>12</sub> = 1. Reciprocidade: A<sub>1</sub>F<sub>12</sub> = A<sub>2</sub>F<sub>21</sub> → F<sub>21</sub> = A<sub>1</sub>/A<sub>2</sub> = (π × 0,5²)/6 = 0,785/6 = <b>{br(F21,3)}</b>. O restante (0,869) é F<sub>22</sub>: a caixa enxerga a si mesma.")

q = 0.05 * 4.2 * 20
num("MEC-C13", C, "Potência para aquecer água",
    "Um aquecedor de passagem deve aquecer 3 L/min de água (c = 4,2 kJ/kg·K) de 20 °C para 40 °C. Desprezando perdas, a potência necessária, em kW, é",
    q, [2 * q, 60 * q, q / 2, 3 * q], d=1,
    res=f"ṁ = 3 L/min = 0,05 kg/s. q = ṁcΔT = 0,05 × 4,2 × 20 = <b>{br(q,1)} kW</b>. Esquecer de converter minutos em segundos dá um valor 60 vezes maior; usar a temperatura final no lugar da diferença dobra a potência.")

eps = 1 - 0.223
num("MEC-C14", C, "Efetividade de condensador",
    "Num condensador, o vapor condensa a temperatura constante enquanto a água de resfriamento se aquece. O trocador tem NTU = 1,5. Dado e<sup>−1,5</sup> ≈ 0,223, a efetividade do trocador é, aproximadamente,",
    eps, [0.223, (1 - math.exp(-3)) / 2, 1.0, 1.5 / 2.5], d=2,
    res=f"Quando um fluido muda de fase, sua capacidade térmica é praticamente infinita e C<sub>r</sub> = C<sub>mín</sub>/C<sub>máx</sub> = 0. Para qualquer arranjo de escoamento, ε = 1 − e<sup>−NTU</sup> = 1 − 0,223 = <b>{br(eps,2)}</b>. A fórmula com C<sub>r</sub> = 1 (0,48) não se aplica.")

con("MEC-C15", C, "Lei de Kirchhoff da radiação",
    "Para uma superfície cinza e difusa em equilíbrio radiativo com sua vizinhança, a lei de Kirchhoff estabelece que",
    "a emissividade é igual à absortividade",
    ["a emissividade é igual à refletividade",
     "a absortividade é sempre igual a 1",
     "a soma da emissividade com a absortividade é igual a 1",
     "a emissividade é igual à transmissividade"],
    res="Kirchhoff: <b>ε = α</b> (para superfície cinza, em todo o espectro). Bons emissores são bons absorvedores. Para corpo opaco, α + ρ = 1; somar ε com α não tem significado. Só o corpo negro tem α = ε = 1.")

Ts = 30 + 600 / 20
num("MEC-C16", C, "Temperatura de superfície em balanço de energia",
    "Uma placa isolada no verso absorve 600 W/m² de radiação solar e perde calor apenas por convecção para o ar a 30 °C, com h = 20 W/m²·K. Em regime permanente, a temperatura da placa, em °C, é",
    Ts, [30, 90, 50, 333], d=0,
    res=f"Balanço: energia absorvida = energia perdida → 600 = 20 × (T<sub>s</sub> − 30) → T<sub>s</sub> = 30 + 30 = <b>{br(Ts,0)} °C</b>. Na prática, a placa também perderia calor por radiação e ficaria um pouco mais fria.")

con("MEC-C17", C, "Fluxo crítico na ebulição",
    "Num gerador de vapor com fluxo de calor imposto (aquecimento elétrico ou por chama), ultrapassar o fluxo crítico de calor da ebulição nucleada provoca",
    "a formação de um filme de vapor sobre a superfície, com queda brusca do coeficiente de troca e salto da temperatura da parede, que pode romper o tubo",
    ["o aumento do coeficiente de troca, pois a geração de bolhas se intensifica",
     "o início da ebulição nucleada, com bolhas isoladas",
     "a redução da temperatura da parede, pela maior evaporação",
     "o retorno à convecção natural, sem mudança de fase"],
    res="Acima do <b>fluxo crítico</b>, as bolhas coalescem num filme de vapor isolante. Com o fluxo de calor imposto, a parede precisa ficar centenas de graus mais quente para manter a troca: é o burnout, causa clássica de ruptura de tubos de caldeira.")

M = "Materiais e Tratamentos Térmicos"
Emod = 200 / 0.001 / 1000
num("MEC-M09", M, "Módulo de elasticidade no ensaio de tração",
    "Um corpo de prova com 50 mm² de seção e 50 mm de comprimento útil recebe 10 kN de tração e se alonga elasticamente 0,05 mm. O módulo de elasticidade do material, em GPa, é",
    Emod, [20, 2000, 100, 0.2], d=0,
    res=f"σ = 10.000/50 = 200 MPa; ε = 0,05/50 = 0,001. E = σ/ε = 200/0,001 = 200.000 MPa = <b>{br(Emod,0)} GPa</b>, típico dos aços.")

rho = 2 * 55.85 / (2.354e-23 * 6.022e23)
num("MEC-M10", M, "Densidade teórica de metal cúbico",
    "O ferro α tem estrutura cúbica de corpo centrado, massa atômica de 55,85 g/mol e parâmetro de rede tal que o volume da célula unitária é 2,354 × 10<sup>−23</sup> cm³. Com N<sub>A</sub> = 6,022 × 10²³ átomos/mol, a densidade teórica, em g/cm³, é, aproximadamente,",
    rho, [rho / 2, 2 * rho, rho * 0.68, 2.63], d=2,
    res=f"A célula CCC contém 2 átomos (1 no centro + 8 × 1/8 nos vértices). ρ = n·A/(V<sub>c</sub>·N<sub>A</sub>) = 2 × 55,85/(2,354 × 10<sup>−23</sup> × 6,022 × 10²³) = 111,7/14,18 = <b>{br(rho,2)} g/cm³</b>. Com 4 átomos (CFC), o valor dobraria.")

con("MEC-M11", M, "Revenimento",
    "O revenimento, realizado após a têmpera dos aços, tem como principal efeito",
    "reduzir a fragilidade e as tensões da martensita, aumentando a tenacidade à custa de alguma perda de dureza",
    ["aumentar a dureza obtida na têmpera",
     "transformar a martensita em austenita retida",
     "aumentar o teor de carbono na superfície",
     "dissolver os carbonetos para homogeneizar a austenita antes da têmpera"],
    res="No <b>revenimento</b>, o aço temperado é aquecido abaixo da zona crítica (tipicamente 150 a 650 °C). A martensita libera carbono em carbonetos finos e as tensões se aliviam: a tenacidade sobe e a dureza cai, mais quanto maior a temperatura.")

con("MEC-M12", M, "Ensaio de dureza Vickers",
    "O ensaio de dureza Vickers caracteriza-se por usar",
    "um penetrador de diamante em forma de pirâmide de base quadrada, com ângulo de 136° entre faces opostas, medindo-se as diagonais da impressão",
    ["uma esfera de aço temperado ou de metal duro, medindo-se o diâmetro da impressão",
     "um cone de diamante com 120°, medindo-se a profundidade de penetração",
     "um pêndulo que mede a energia absorvida",
     "um martelo que mede a altura de ressalto"],
    res="<b>Vickers</b>: pirâmide de diamante de 136°, dureza = carga/área da impressão, calculada pelas diagonais. Serve para qualquer material, inclusive camadas finas (microdureza). Esfera é o Brinell; cone de diamante com leitura de profundidade é o Rockwell C; ressalto é o Shore.")

con("MEC-M13", M, "Alívio de tensões",
    "Após a soldagem de um vaso de pressão de aço-carbono, aplica-se um tratamento térmico de alívio de tensões, que consiste em",
    "aquecer a peça abaixo da temperatura crítica (tipicamente 550 a 650 °C), manter e resfriar lentamente, sem mudança de fase",
    ["austenitizar a peça e resfriar em água",
     "aquecer acima da zona crítica e resfriar ao ar",
     "enriquecer a superfície com nitrogênio",
     "resfriar a peça abaixo de 0 °C para transformar a austenita retida"],
    res="No <b>alívio de tensões</b>, o aquecimento subcrítico reduz o limite de escoamento a quente, e as tensões residuais da soldagem se relaxam por deformação plástica localizada e fluência. Não há transformação de fase: a microestrutura se mantém. As normas de vasos exigem esse tratamento acima de certas espessuras.")

con("MEC-M14", M, "Proteção catódica por ânodo de sacrifício",
    "Para proteger o casco de aço de uma embarcação contra a corrosão na água do mar por meio de ânodos de sacrifício, o material dos ânodos deve ser",
    "zinco, alumínio ou magnésio, mais ativos (menos nobres) que o aço na série galvânica",
    ["cobre, por ser mais nobre que o aço",
     "aço inoxidável, por ser resistente à corrosão",
     "grafite, por ser bom condutor",
     "o mesmo aço do casco, para evitar a corrosão galvânica"],
    res="O ânodo de sacrifício precisa ser <b>menos nobre</b> que o aço: ele se oxida no lugar do casco, que vira cátodo. Zinco e alumínio são os mais usados no mar; magnésio, em água doce e solo. Cobre ou inox acoplados ao aço acelerariam a corrosão do casco.")

con("MEC-M15", M, "Termoplásticos e termofixos",
    "Sobre os polímeros termoplásticos e termofixos, é correto afirmar que",
    "os termoplásticos amolecem ao serem aquecidos e podem ser remoldados, enquanto os termofixos formam ligações cruzadas irreversíveis e não podem ser refundidos",
    ["os termofixos podem ser reciclados por refusão, pois suas cadeias são lineares",
     "os termoplásticos têm estrutura em rede tridimensional com muitas ligações cruzadas",
     "o polietileno e o PVC são exemplos de termofixos",
     "a resina epóxi curada e a baquelite são exemplos de termoplásticos"],
    res="<b>Termoplásticos</b> (PE, PP, PVC, náilon) têm cadeias lineares ou ramificadas unidas por forças secundárias: amolecem com calor e podem ser remoldados. <b>Termofixos</b> (epóxi curada, fenólicas como a baquelite, poliéster insaturado) curam em rede tridimensional e se degradam antes de fundir.")

Tm = 660 + 273; Tcr = 0.4 * Tm - 273
num("MEC-M16", M, "Temperatura homóloga e fluência",
    "A fluência dos metais passa a ser relevante, em geral, acima de cerca de 0,4 da temperatura absoluta de fusão. Para o alumínio, que funde a 660 °C, essa temperatura, em °C, é, aproximadamente,",
    Tcr, [0.4 * 660, 0.4 * Tm, 0.5 * Tm - 273, 300], d=0,
    res=f"T<sub>f</sub> = 660 + 273 = 933 K. 0,4 × 933 = 373 K = <b>{br(Tcr,0)} °C</b>. A temperatura homóloga usa kelvin: aplicar 0,4 sobre 660 °C (264 °C) superestima muito o limite. Ligas de alumínio já perdem resistência com o tempo acima de ~100 °C, enquanto aços só a partir de ~400 °C.")

con("MEC-M17", M, "Endurecimento por precipitação",
    "O endurecimento por precipitação (envelhecimento) de ligas de alumínio como as das séries 2xxx, 6xxx e 7xxx é obtido pela sequência de",
    "solubilização, resfriamento rápido para obter solução supersaturada e envelhecimento, natural ou artificial, que forma precipitados finos",
    ["austenitização, têmpera e revenimento, formando martensita",
     "cementação seguida de têmpera superficial",
     "laminação a frio seguida de recozimento pleno",
     "fusão, vazamento e resfriamento lento no molde"],
    res="O <b>envelhecimento</b>: (1) solubilização dissolve os elementos de liga; (2) a têmpera em água congela a solução supersaturada; (3) o envelhecimento forma precipitados finos e coerentes que bloqueiam as discordâncias. É a origem do tratamento T6 (ex.: 6061-T6). Alumínio não tem martensita como os aços.")

B = "Máquinas de Fluxo"
H = (420 + 30) / 10
num("MEC-B09", B, "Altura manométrica por manômetros",
    "Num teste de bomba com água (ρ = 1.000 kg/m³; g = 10 m/s²), o vacuômetro na sucção indica −30 kPa e o manômetro na descarga indica 420 kPa. Os instrumentos estão na mesma cota e os diâmetros de sucção e descarga são iguais. A altura manométrica da bomba, em m, é",
    H, [(420 - 30) / 10, 42, 450, 4.5], d=1,
    res=f"H = (p<sub>d</sub> − p<sub>s</sub>)/(ρg) = [420 − (−30)] × 1.000/(1.000 × 10) = <b>{br(H,1)} m</b>. Com diâmetros iguais, as velocidades se cancelam. A pressão de sucção negativa soma à altura: subtrair 30 kPa (39 m) é o erro típico.")

Wiso = 100 * 1 * 2.08
num("MEC-B10", B, "Potência de compressão isotérmica",
    "Um compressor ideal aspira 1 m³/s de ar a 100 kPa e o comprime isotermicamente até 800 kPa. Dado ln 8 ≈ 2,08, a potência teórica de compressão, em kW, é, aproximadamente,",
    Wiso, [700, 3.5 * 100 * 0.81, Wiso / 2, 80], d=0,
    res=f"Compressão isotérmica reversível: Ẇ = p<sub>1</sub>V̇<sub>1</sub>·ln(p<sub>2</sub>/p<sub>1</sub>) = 100 × 1 × 2,08 = <b>{br(Wiso,0)} kW</b>. A compressão isentrópica exigiria mais (≈ 284 kW). Por isso se usam estágios com resfriamento intermediário: o processo se aproxima do isotérmico.")

Pt = 10 * (3200 - 2500) / 1000
num("MEC-B11", B, "Potência de turbina a vapor",
    "Uma turbina a vapor adiabática recebe 10 kg/s de vapor com entalpia de 3.200 kJ/kg e o descarrega com 2.500 kJ/kg. Desprezando variações de energia cinética e potencial, a potência produzida, em MW, é",
    Pt, [0.7, 25, 32, 70], d=1,
    res=f"Ẇ = ṁ(h<sub>e</sub> − h<sub>s</sub>) = 10 × (3.200 − 2.500) = 7.000 kW = <b>{br(Pt,1)} MW</b>.")

con("MEC-B12", B, "Bombas de deslocamento positivo",
    "Bombas de deslocamento positivo, como as de engrenagens e as de pistão, devem ter válvula de alívio na descarga porque",
    "a vazão praticamente independe da pressão, e com a descarga bloqueada a pressão subiria até romper a tubulação ou travar o acionamento",
    ["precisam de vazão mínima para não cavitar, como as centrífugas",
     "sua altura manométrica cai a zero quando a descarga é fechada",
     "são autoescorvantes e acumulam ar na descarga",
     "a potência absorvida é mínima com a descarga fechada"],
    res="Nas bombas de <b>deslocamento positivo</b>, cada volta desloca um volume fixo. Se a descarga fecha, o líquido (quase incompressível) não tem para onde ir: a pressão sobe sem limite. A centrífuga, ao contrário, opera na altura de shutoff, que é finita.")

u2 = 3.14 * 0.3 * 1800 / 60; He = u2 * 20 / 9.81
num("MEC-B13", B, "Equação de Euler para turbomáquinas",
    "O rotor de uma bomba centrífuga tem 300 mm de diâmetro externo e gira a 1.800 rpm. Na saída, a componente tangencial da velocidade absoluta é 20 m/s, e a entrada não tem pré-rotação. Com π ≈ 3,14 e g = 9,81 m/s², a altura teórica de Euler, em m, é, aproximadamente,",
    He, [u2 ** 2 / 9.81, u2 ** 2 / (2 * 9.81), He / 2, 2 * He], d=1,
    res=f"u<sub>2</sub> = πDn/60 = 3,14 × 0,3 × 1.800/60 = {br(u2,2)} m/s. Sem pré-rotação na entrada: H = u<sub>2</sub>·c<sub>u2</sub>/g = 28,26 × 20/9,81 = <b>{br(He,1)} m</b>. A altura real é menor, por causa do escorregamento e das perdas hidráulicas.")

eg = 0.85 * 0.95 * 0.95 * 100
num("MEC-B14", B, "Rendimento global de bomba",
    "Uma bomba tem rendimento hidráulico de 85%, volumétrico de 95% e mecânico de 95%. Seu rendimento global é, aproximadamente,",
    eg, [85, 91.7, 95, 0.85 ** 3 * 100], fmt=lambda v: br(v, 1) + "%",
    res=f"Os rendimentos parciais se multiplicam: η = η<sub>h</sub>·η<sub>v</sub>·η<sub>m</sub> = 0,85 × 0,95 × 0,95 = <b>{br(eg,1)}%</b>. A média aritmética (91,7%) não tem significado físico.")

con("MEC-B15", B, "Surge em compressor centrífugo",
    "Um compressor centrífugo operando com vazão muito baixa, à esquerda do ponto de máxima pressão da curva, pode entrar em surge (bombeamento), fenômeno caracterizado por",
    "oscilações violentas de vazão e pressão, com reversão periódica do fluxo, que exigem sistema antissurge de recirculação ou alívio",
    ["aumento contínuo da vazão até o limite de engasgamento (choke)",
     "cavitação nas pás do rotor por vaporização do gás",
     "queda de rotação causada pelo excesso de vazão",
     "aquecimento uniforme do gás sem efeito mecânico"],
    res="No <b>surge</b>, o compressor não sustenta a pressão do sistema: o fluxo reverte, a pressão cai, o fluxo volta, e o ciclo se repete em segundos, com fortes cargas nos mancais e selos. O controle antissurge recircula gás para manter a vazão acima da linha de surge. Choke é o limite oposto, de vazão máxima.")

con("MEC-B16", B, "Gaxeta e selo mecânico",
    "Na vedação do eixo de bombas centrífugas, a gaxeta difere do selo mecânico porque",
    "a gaxeta precisa de um pequeno vazamento controlado para lubrificar e refrigerar o contato, enquanto o selo mecânico veda entre faces planas lapidadas com vazamento praticamente nulo",
    ["a gaxeta veda por faces radiais de carbeto e carvão, sem vazamento",
     "o selo mecânico precisa de aperto periódico do preme-gaxeta",
     "a gaxeta é indicada para fluidos tóxicos, por não vazar",
     "o selo mecânico só pode ser usado em bombas de deslocamento positivo"],
    res="A <b>gaxeta</b> (anéis trançados comprimidos pelo preme-gaxeta) trabalha com gotejamento: apertar demais queima a gaxeta e desgasta a luva do eixo. O <b>selo mecânico</b> usa uma face rotativa e outra estacionária com filme fluido de micrômetros: é o exigido para fluidos inflamáveis ou tóxicos.")

Vd = math.pi * 0.1 ** 2 / 4 * 0.1 * 1200
num("MEC-B17", B, "Deslocamento volumétrico de compressor alternativo",
    "Um compressor alternativo de um cilindro e simples efeito tem diâmetro de 100 mm, curso de 100 mm e gira a 1.200 rpm. O volume deslocado pelo pistão, em m³/min, é, aproximadamente,",
    Vd, [2 * Vd, 4 * Vd, Vd / 60, Vd * 60], d=None,
    res=f"Volume por curso: (π × 0,1²/4) × 0,1 = 7,85 × 10<sup>−4</sup> m³. V̇ = 7,85 × 10<sup>−4</sup> × 1.200 = <b>{br(Vd,3)} m³/min</b>. Em duplo efeito, o valor quase dobraria. A vazão real aspirada é menor, pela eficiência volumétrica.")

V = "Vibrações"
vmax = 2 * 2 * math.pi * 50
num("MEC-V05", V, "Velocidade em movimento harmônico",
    "Um mancal vibra em movimento harmônico simples com amplitude de deslocamento de 2 mm e frequência de 50 Hz. A velocidade máxima de vibração, em mm/s, é, aproximadamente,",
    vmax, [2 * 50, vmax / 2, 2 * vmax, vmax * 2 * math.pi * 50 / 1000], d=0,
    res=f"x = X·sen(ωt) → v<sub>máx</sub> = Xω = 2 × (2π × 50) = <b>{br(vmax,0)} mm/s</b>. Usar f no lugar de ω (100 mm/s) esquece o 2π; 1.257 mm/s seria o valor pico a pico.")

k = 3 * 200e9 * 8e-8 / 0.5 ** 3; fn = math.sqrt(k / 96) / (2 * math.pi)
num("MEC-V06", V, "Frequência natural de viga em balanço",
    "Uma massa de 96 kg está presa na extremidade livre de uma viga em balanço de aço (E = 200 GPa) com 0,5 m de comprimento e momento de inércia de 8 cm⁴. Desprezando a massa da viga, a frequência natural, em Hz, é, aproximadamente,",
    fn, [math.sqrt(k / 96), 2 * fn, fn / math.sqrt(3), 1.6], d=1,
    res=f"Rigidez da ponta: k = 3EI/L³ = 3 × 200 × 10⁹ × 8 × 10<sup>−8</sup>/0,125 = 384.000 N/m. ω<sub>n</sub> = √(k/m) = √4.000 = 63,2 rad/s → f<sub>n</sub> = 63,2/(2π) = <b>{br(fn,1)} Hz</b>. Sem dividir por 2π, a resposta fica em rad/s.")

fnt = math.sqrt(800 / 0.5) / (2 * math.pi)
num("MEC-V07", V, "Vibração torcional",
    "Um disco com momento de inércia de massa de 0,5 kg·m² está montado na ponta de um eixo engastado com rigidez torcional de 800 N·m/rad. A frequência natural torcional, em Hz, é, aproximadamente,",
    fnt, [40, 2 * fnt, fnt / 2, 1.0], d=2,
    res=f"ω<sub>n</sub> = √(k<sub>t</sub>/J) = √(800/0,5) = 40 rad/s → f<sub>n</sub> = 40/(2π) = <b>{br(fnt,2)} Hz</b>. É a mesma forma do sistema massa-mola, trocando massa por inércia de rotação e rigidez linear por torcional.")

zeta = 200 / (2 * math.sqrt(40000 * 10))
num("MEC-V08", V, "Razão de amortecimento",
    "Um sistema tem massa de 10 kg, rigidez de 40.000 N/m e coeficiente de amortecimento viscoso de 200 N·s/m. A razão de amortecimento é, aproximadamente,",
    zeta, [2 * zeta, zeta / 2, 200 / 40000, 0.5], d=3,
    res=f"Amortecimento crítico: c<sub>c</sub> = 2√(km) = 2√(400.000) = 1.265 N·s/m. ζ = c/c<sub>c</sub> = 200/1.265 = <b>{br(zeta,3)}</b>: sistema subamortecido. Esquecer o 2 de c<sub>c</sub> dobra o valor.")

fd = 20 * math.sqrt(1 - 0.36)
num("MEC-V09", V, "Frequência natural amortecida",
    "Um sistema tem frequência natural não amortecida de 20 Hz e razão de amortecimento de 0,6. A frequência da vibração livre amortecida, em Hz, é",
    fd, [12, 20, 8, 25], d=1,
    res=f"f<sub>d</sub> = f<sub>n</sub>·√(1 − ζ²) = 20 × √(1 − 0,36) = 20 × 0,8 = <b>{br(fd,1)} Hz</b>. Com amortecimentos usuais (ζ &lt; 0,1), a diferença entre f<sub>d</sub> e f<sub>n</sub> é desprezível; aqui, com ζ = 0,6, é grande.")

con("MEC-V10", V, "Parâmetros de medição de vibração",
    "Na manutenção preditiva, para detectar precocemente defeitos em rolamentos, que geram impactos de alta frequência (vários kHz), a grandeza mais indicada para medir é",
    "a aceleração, inclusive com técnicas de envelope (demodulação)",
    ["o deslocamento, por ser mais sensível em altas frequências",
     "a temperatura do óleo, que acusa o defeito antes da vibração",
     "a velocidade de rotação do eixo",
     "a corrente elétrica do motor, que é a primeira a se alterar"],
    res="Para a mesma amplitude de deslocamento, a aceleração cresce com ω²: ela realça as altas frequências. Por isso defeitos de rolamento são vistos na <b>aceleração</b> e no espectro de envelope. Deslocamento serve para baixas frequências (eixos em mancais de deslizamento); a velocidade RMS (mm/s) é o critério geral de severidade das normas ISO.")

nres = 25 * 60
num("MEC-V11", V, "Rotação de ressonância",
    "A base de um equipamento tem frequência natural de 25 Hz. A rotação do motor que levaria o conjunto à ressonância por desbalanceamento, em rpm, é",
    nres, [25, 2 * math.pi * 25, 750, 3000], d=0,
    res=f"O desbalanceamento excita a frequência de 1× a rotação. Ressonância quando n/60 = 25 Hz → n = 25 × 60 = <b>{br(nres,0)} rpm</b>. Um motor de 4 polos em 50 Hz (≈ 1.480 rpm) ficaria perigosamente perto; em 60 Hz (≈ 1.780 rpm), mais afastado.")

P = "Fabricação e Soldagem"
vf = 0.1 * 4 * 1500
num("MEC-P05", P, "Velocidade de avanço no fresamento",
    "Uma fresa de 4 dentes gira a 1.500 rpm com avanço por dente de 0,1 mm. A velocidade de avanço da mesa, em mm/min, é",
    vf, [0.1 * 1500, vf * 4, 10, 6000], d=0,
    res=f"v<sub>f</sub> = f<sub>z</sub>·z·n = 0,1 × 4 × 1.500 = <b>{br(vf,0)} mm/min</b>. Esquecer o número de dentes dá 150 mm/min: cada dente corta 0,1 mm por volta.")

Tv = (400 / 200) ** (1 / 0.25)
num("MEC-P06", P, "Vida de ferramenta pela equação de Taylor",
    "Para uma ferramenta de metal duro, a equação de Taylor é v·T<sup>0,25</sup> = 400, com v em m/min e T em min. Para v = 200 m/min, a vida da ferramenta, em min, é",
    Tv, [Tv / 2, Tv / 4, 2 * Tv, 2.0], d=0,
    res=f"T<sup>0,25</sup> = 400/200 = 2 → T = 2<sup>4</sup> = <b>{br(Tv,0)} min</b>. Reduzir a velocidade à metade multiplica a vida por 16: por isso a velocidade de corte é o parâmetro que mais afeta o custo de ferramenta.")

ra = (1 - 0.8 ** 2) * 100
num("MEC-P07", P, "Redução de área na trefilação",
    "Um arame de 10 mm de diâmetro é trefilado para 8 mm. A redução de área percentual é",
    ra, [20, 64, 25, 56.25], fmt=lambda v: br(v, 0) + "%",
    res=f"RA = (A<sub>0</sub> − A<sub>f</sub>)/A<sub>0</sub> = 1 − (8/10)² = 1 − 0,64 = <b>{br(ra,0)}%</b>. A redução de diâmetro (20%) não é a redução de área, que depende do quadrado.")

Lm = 500 * 1.02
num("MEC-P08", P, "Sobremetal de contração no modelo de fundição",
    "Uma peça de ferro fundido deve ter 500 mm de comprimento final. Considerando contração linear de solidificação e resfriamento de 2%, o comprimento do modelo, em mm, deve ser, aproximadamente,",
    Lm, [490, 500, 520, 550], d=0,
    res=f"O modelo precisa ser maior para compensar a contração: L<sub>modelo</sub> = L·(1 + c) = 500 × 1,02 = <b>{br(Lm,0)} mm</b> (pelo cálculo exato, 500/0,98 = 510,2 mm). Daí as \"réguas de contração\" dos modeladores.")

con("MEC-P09", P, "Soldagem por arco submerso",
    "O processo de soldagem por arco submerso (SAW) é caracterizado por",
    "arco totalmente coberto por fluxo granulado, alta taxa de deposição e uso principal em posição plana, em juntas longas e chapas grossas",
    ["eletrodo de tungstênio não consumível e gás inerte",
     "arco visível protegido por CO₂, indicado para todas as posições",
     "eletrodo revestido trocado manualmente a cada consumo",
     "ausência de arco elétrico, com aquecimento por atrito"],
    res="No <b>arco submerso</b>, o arame é alimentado continuamente sob uma camada de fluxo granulado que protege o arco (invisível, sem respingos nem radiação). Tem altíssima produtividade em vasos, tubos de grande diâmetro e estruturas, mas o fluxo solto limita o processo à posição plana ou horizontal.")

Rt = 0.2 ** 2 / (8 * 0.8) * 1000
num("MEC-P10", P, "Rugosidade teórica no torneamento",
    "No torneamento com ferramenta de raio de ponta 0,8 mm e avanço de 0,2 mm/rot, a rugosidade máxima teórica R<sub>t</sub> ≈ f²/(8r), em µm, é",
    Rt, [Rt / 4, 4 * Rt, 2 * Rt, 50], d=2,
    res=f"R<sub>t</sub> = f²/(8r) = 0,2²/(8 × 0,8) = 0,04/6,4 = 0,00625 mm = <b>{br(Rt,2)} µm</b>. A rugosidade cresce com o quadrado do avanço: reduzir o avanço à metade divide R<sub>t</sub> por 4. R<sub>a</sub> é cerca de R<sub>t</sub>/4 (≈ 1,6 µm).")

con("MEC-P11", P, "Brasagem e soldagem",
    "A brasagem difere da soldagem por fusão porque, na brasagem,",
    "o metal de base não funde: um metal de adição com temperatura de fusão acima de 450 °C, mas abaixo da do metal de base, preenche a junta por capilaridade",
    ["o metal de base e o metal de adição fundem juntos, formando uma poça de fusão",
     "não há metal de adição, apenas pressão",
     "o metal de adição funde abaixo de 450 °C, como nas soldas de estanho",
     "a união é feita exclusivamente por adesivos poliméricos"],
    res="Na <b>brasagem</b>, só o metal de adição (ligas de prata, cobre ou latão) funde, acima de 450 °C, e molha a junta por capilaridade. Abaixo de 450 °C é a solda branda (estanho). Permite unir metais diferentes, como cobre e aço, sem fundir as peças.")
