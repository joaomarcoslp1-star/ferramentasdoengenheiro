# -*- coding: utf-8 -*-
# Lote 3 (28/11/2026): Termodinâmica, Mecânica dos Fluidos, Resistência dos Materiais
import math
from nbase import num, con, br

T = "Termodinâmica"
W = 2 * 1.005 * (500 - 300)
num("MEC-T31", T, "Potência de compressor de ar",
    "Um compressor adiabático recebe 2 kg/s de ar (c<sub>p</sub> = 1,005 kJ/kg·K) a 300 K e o descarrega a 500 K. Desprezando variações de energia cinética e potencial, a potência consumida, em kW, é, aproximadamente,",
    W, [2 * 0.718 * 200, 1.005 * 200, 2 * 1.005 * 500, 4 * W], d=0,
    res=f"Ẇ = ṁc<sub>p</sub>(T<sub>2</sub> − T<sub>1</sub>) = 2 × 1,005 × 200 = <b>{br(W,0)} kW</b>. Em volume de controle, o fluxo de energia é de entalpia (c<sub>p</sub>); com c<sub>v</sub>, o valor (287 kW) fica subestimado.")

Q = 3 * 0.718 * 100
num("MEC-T32", T, "Aquecimento a volume constante",
    "Três quilogramas de ar (c<sub>v</sub> = 0,718 kJ/kg·K; c<sub>p</sub> = 1,005 kJ/kg·K) num tanque rígido são aquecidos de 300 K para 400 K. O calor fornecido, em kJ, é, aproximadamente,",
    Q, [3 * 1.005 * 100, 0.718 * 100, 3 * 0.287 * 100, 3 * 0.718 * 400], d=0,
    res=f"Volume constante: W = 0 e Q = ΔU = m·c<sub>v</sub>·ΔT = 3 × 0,718 × 100 = <b>{br(Q,0)} kJ</b>. Com c<sub>p</sub> (302 kJ), seria o calor a pressão constante, quando parte da energia sai como trabalho de expansão.")

r = 11.31
num("MEC-T33", T, "Razão de pressões em processo isentrópico",
    "Ar (k = 1,4) é comprimido de forma isentrópica de 300 K para 600 K. Dado 2<sup>3,5</sup> ≈ 11,31, a razão entre as pressões final e inicial é, aproximadamente,",
    r, [2, 2 ** 1.4, 4, 2 ** (1 / 0.4)], d=2,
    res=f"P<sub>2</sub>/P<sub>1</sub> = (T<sub>2</sub>/T<sub>1</sub>)<sup>k/(k−1)</sup> = 2<sup>1,4/0,4</sup> = 2<sup>3,5</sup> ≈ <b>{br(r,2)}</b>. Dobrar a temperatura absoluta exige mais que dobrar a pressão: o expoente é 3,5.")

ds = -0.287 * 0.693
num("MEC-T34", T, "Entropia de gás ideal em compressão isotérmica",
    "Ar (R = 0,287 kJ/kg·K) é comprimido isotermicamente até o dobro da pressão inicial. Com ln 2 ≈ 0,693, a variação de entropia específica do ar, em kJ/kg·K, é, aproximadamente,",
    ds, [-ds, 0, -0.287, 0.287 * 2], d=3,
    res=f"Gás ideal: Δs = c<sub>p</sub>ln(T<sub>2</sub>/T<sub>1</sub>) − R·ln(P<sub>2</sub>/P<sub>1</sub>). Com T constante: Δs = −0,287 × 0,693 = <b>{br(ds,3)} kJ/kg·K</b>. A entropia do ar diminui porque ele cedeu calor ao ambiente; a do ambiente aumenta mais, e a total não diminui.")

rc = 2 ** 2.5
num("MEC-T35", T, "Taxa de compressão do ciclo Otto",
    "Num ciclo Otto padrão a ar (k = 1,4), deseja-se rendimento térmico de 50%. Dado 2<sup>2,5</sup> ≈ 5,66, a taxa de compressão necessária é, aproximadamente,",
    rc, [2, 4, 8, 2 ** 1.4], d=2,
    res=f"η = 1 − 1/r<sup>k−1</sup> = 0,5 → r<sup>0,4</sup> = 2 → r = 2<sup>1/0,4</sup> = 2<sup>2,5</sup> ≈ <b>{br(rc,2)}</b>. Motores a gasolina usam r ≈ 9 a 12; o ciclo real rende bem menos que o padrão a ar.")

num("MEC-T36", T, "Relação entre COP de refrigerador e de bomba de calor",
    "Um equipamento reversível de ar-condicionado tem COP de 3,0 quando opera como refrigerador. Operando entre as mesmas temperaturas e com o mesmo trabalho, como bomba de calor, seu COP é",
    4.0, [2.0, 3.0, 1.33, 0.33], d=1,
    res="Pela primeira lei, Q<sub>H</sub> = Q<sub>L</sub> + W. Logo COP<sub>BC</sub> = Q<sub>H</sub>/W = (Q<sub>L</sub> + W)/W = COP<sub>R</sub> + 1 = <b>4,0</b>. Por isso a bomba de calor sempre entrega mais calor do que a energia elétrica que consome.")

dU = 50 - 20
num("MEC-T37", T, "Primeira lei em tanque agitado",
    "Um tanque rígido contém um fluido que é agitado por uma hélice, que lhe fornece 50 kJ de trabalho. Durante o processo, o tanque perde 20 kJ de calor para o ambiente. A variação de energia interna do fluido, em kJ, é",
    dU, [70, -30, -70, 0], fmt=lambda v: ("+" if v > 0 else "") + br(v, 0),
    res=f"ΔU = Q − W, com Q = −20 kJ (perdido) e W = −50 kJ (recebido pelo sistema): ΔU = −20 − (−50) = <b>+{br(dU,0)} kJ</b>. Sinais: calor que entra e trabalho que sai são positivos. O tanque rígido não troca trabalho de fronteira, mas o eixo da hélice sim.")

x = (763 - 417) / 2258
num("MEC-T38", T, "Título após estrangulamento",
    "Água como líquido saturado a 1 MPa (h = 763 kJ/kg) passa por uma válvula de estrangulamento até 100 kPa, onde h<sub>l</sub> = 417 kJ/kg e h<sub>lv</sub> = 2.258 kJ/kg. O título na saída da válvula é, aproximadamente,",
    x, [763 / 2258, 1 - x, 417 / 2258, 0], d=3,
    res=f"Estrangulamento: h<sub>s</sub> = h<sub>e</sub> = 763 kJ/kg. x = (h − h<sub>l</sub>)/h<sub>lv</sub> = (763 − 417)/2.258 = <b>{br(x,3)}</b>. Cerca de 15% do líquido \"flasheia\" em vapor: é o que acontece em purgadores e na válvula de expansão das geladeiras.")

TR = 35.17 / 3.517
num("MEC-T39", T, "Tonelada de refrigeração",
    "Um sistema de refrigeração remove 35,17 kW de calor do ambiente refrigerado. Sabendo que 1 TR (tonelada de refrigeração) equivale a 3,517 kW (12.000 BTU/h), a capacidade do sistema, em TR, é",
    TR, [3.517, 35.17, 100, 1.0], d=1,
    res=f"35,17/3,517 = <b>{br(TR,1)} TR</b> = 120.000 BTU/h. A TR vem do calor para congelar uma tonelada (curta) de gelo em 24 horas.")

con("MEC-T40", T, "Desigualdade de Clausius",
    "Para qualquer ciclo termodinâmico, a desigualdade de Clausius estabelece que a integral cíclica de δQ/T",
    "é menor ou igual a zero, valendo a igualdade apenas para ciclos internamente reversíveis",
    ["é sempre maior que zero",
     "é sempre igual a zero, por ser uma propriedade",
     "é igual ao trabalho líquido do ciclo",
     "é maior que zero para ciclos reversíveis e menor que zero para irreversíveis"],
    res="<b>∮δQ/T ≤ 0</b>. Para ciclos reversíveis, a integral é nula, e é isso que permite definir a entropia como propriedade. Um ciclo com ∮δQ/T &gt; 0 é impossível; é o teste que reprova o \"motor milagroso\" do inventor.")

cp = 1.4 * 0.287 / 0.4
num("MEC-T41", T, "Relação entre calores específicos",
    "Para o ar como gás ideal, com R = 0,287 kJ/kg·K e k = c<sub>p</sub>/c<sub>v</sub> = 1,4, o calor específico a pressão constante, em kJ/kg·K, é, aproximadamente,",
    cp, [0.287 / 0.4, 1.4 * 0.287, 0.287 / 1.4, 1.4], d=3,
    res=f"c<sub>p</sub> − c<sub>v</sub> = R e c<sub>p</sub> = k·c<sub>v</sub>. Resolvendo: c<sub>p</sub> = kR/(k − 1) = 1,4 × 0,287/0,4 = <b>{br(cp,3)} kJ/kg·K</b>, e c<sub>v</sub> = R/(k − 1) = 0,718 kJ/kg·K.")

con("MEC-T42", T, "Ciclo combinado",
    "Uma usina termelétrica de ciclo combinado alcança rendimentos próximos de 60% porque",
    "os gases de exaustão da turbina a gás, ainda muito quentes, geram vapor numa caldeira de recuperação que aciona um ciclo Rankine",
    ["a turbina a vapor opera com temperatura de entrada maior que a da turbina a gás",
     "o compressor da turbina a gás é acionado por um motor elétrico externo",
     "o condensador é eliminado, reduzindo a rejeição de calor",
     "a combustão ocorre duas vezes no mesmo combustível, dobrando a energia liberada"],
    res="O Brayton recebe calor a alta temperatura, mas rejeita gases a 500–600 °C. O Rankine aproveita esse calor na <b>caldeira de recuperação (HRSG)</b>. Juntos, um aproveita a faixa alta de temperatura e o outro, a baixa: rendimento global de 55% a 62%, contra 35% a 40% de cada ciclo isolado.")

F = "Mecânica dos Fluidos"
p = 50 + 1000 * 10 * 3 / 1000
num("MEC-F31", F, "Pressão em tanque pressurizado",
    "Um tanque fechado contém água até 3 m de altura, com ar comprimido acima dela a 50 kPa (manométrica). Com g = 10 m/s², a pressão manométrica no fundo, em kPa, é",
    p, [30, 50, 101.3 + p, 20], d=0,
    res=f"p<sub>fundo</sub> = p<sub>ar</sub> + ρgh = 50 + 1.000 × 10 × 3/1.000 = <b>{br(p,0)} kPa</b>. A pressão do gás se transmite integralmente a todo o líquido (Pascal) e se soma à da coluna.")

A = math.pi * 0.4 ** 2 / 4; Fz = 1000 * 10 * 5 * A / 1000
num("MEC-F32", F, "Força em tampa horizontal submersa",
    "Uma tampa circular de 0,4 m de diâmetro fecha um furo no fundo horizontal de um tanque aberto, sob 5 m de água (g = 10 m/s²). A força da água sobre a tampa, em kN, é, aproximadamente,",
    Fz, [4 * Fz, Fz / 2, 2 * Fz, 50], d=2,
    res=f"No fundo horizontal, a pressão é uniforme: p = ρgh = 50 kPa. F = p·A = 50 × (π × 0,4²/4) = 50 × 0,1257 = <b>{br(Fz,2)} kN</b>. Usar πD² sem o /4 dá 4 vezes mais.")

dp = 0.5 * 1000 * (6 ** 2 - 2 ** 2) / 1000
num("MEC-F33", F, "Queda de pressão numa contração",
    "Água (ρ = 1.000 kg/m³) escoa num tubo horizontal que se estreita: a velocidade passa de 2 m/s para 6 m/s. Desprezando perdas, a queda de pressão entre as duas seções, em kPa, é",
    dp, [0.5 * (6 - 2) ** 2, 2 * dp, 18, 4], d=0,
    res=f"Bernoulli: p<sub>1</sub> − p<sub>2</sub> = ½ρ(V<sub>2</sub>² − V<sub>1</sub>²) = 0,5 × 1.000 × (36 − 4) = 16.000 Pa = <b>{br(dp,0)} kPa</b>. Elevar ao quadrado a diferença das velocidades (8 kPa) é erro: o certo é a diferença dos quadrados.")

Pp = 1000 * 10 * 0.05 * 20 / 1000
num("MEC-F34", F, "Potência dissipada por perda de carga",
    "Água (ρ = 1.000 kg/m³) escoa com vazão de 50 L/s numa tubulação onde a perda de carga total é de 20 m. Com g = 10 m/s², a potência dissipada pelo atrito, em kW, é",
    Pp, [100, 1.0, 20, 5.0], d=1,
    res=f"P = ρ·g·Q·h<sub>f</sub> = 1.000 × 10 × 0,05 × 20 = 10.000 W = <b>{br(Pp,1)} kW</b>. Essa é a potência que a bomba precisa repor, antes de dividir pelo rendimento.")

con("MEC-F35", F, "Escoamento hidraulicamente rugoso",
    "No diagrama de Moody, para escoamento turbulento plenamente rugoso (números de Reynolds muito altos), o fator de atrito",
    "depende apenas da rugosidade relativa ε/D, sendo independente do número de Reynolds",
    ["depende apenas do número de Reynolds, como no regime laminar",
     "tende a zero, pois a turbulência elimina o atrito",
     "é igual a 64/Re",
     "aumenta linearmente com o número de Reynolds"],
    res="Com Re muito alto, a subcamada viscosa fica mais fina que as rugosidades, que passam a dominar o atrito: as curvas de Moody ficam <b>horizontais</b>, com f = f(ε/D). Nessa faixa, a perda de carga é exatamente proporcional a V² (ou Q²).")

v = (36 / 3600) / (math.pi * 0.1 ** 2 / 4)
num("MEC-F36", F, "Velocidade média a partir da vazão",
    "Uma tubulação com 100 mm de diâmetro interno conduz 36 m³/h de água. A velocidade média do escoamento, em m/s, é, aproximadamente,",
    v, [v / 4, 4 * v, v / 3.6, 2 * v], d=2,
    res=f"Q = 36/3.600 = 0,01 m³/s; A = π × 0,1²/4 = 0,00785 m². V = Q/A = <b>{br(v,2)} m/s</b>, dentro da faixa usual de 1 a 3 m/s para água em linhas de recalque.")

vt = (2600 - 1000) * 10 * (1e-4) ** 2 / (18 * 1e-3) * 1000
num("MEC-F37", F, "Lei de Stokes (velocidade terminal)",
    "Uma partícula esférica de areia (ρ = 2.600 kg/m³) com 0,1 mm de diâmetro sedimenta em água parada (ρ = 1.000 kg/m³; μ = 10<sup>−3</sup> Pa·s; g = 10 m/s²). Pela lei de Stokes, v = (ρ<sub>p</sub> − ρ)gd²/(18μ), sua velocidade terminal, em mm/s, é, aproximadamente,",
    vt, [2600 * 10 * 1e-8 / 0.018 * 1000, vt * 4, vt / 4, vt * 1000], d=1,
    res=f"v = 1.600 × 10 × (10<sup>−4</sup>)²/(18 × 10<sup>−3</sup>) = 1,6 × 10<sup>−4</sup>/0,018 = 0,0089 m/s ≈ <b>{br(vt,1)} mm/s</b>. Conferindo Re = ρvd/μ ≈ 0,9: dentro do regime de Stokes (Re &lt; 1). Usar o raio no lugar do diâmetro dá 4 vezes menos.")

num("MEC-F38", F, "Teorema dos Pi de Buckingham",
    "A força de arrasto F numa esfera depende da velocidade V, do diâmetro D, da massa específica ρ e da viscosidade μ do fluido. Pelo teorema dos Pi de Buckingham, o número de grupos adimensionais independentes que descrevem o fenômeno é",
    2, [1, 3, 4, 5], d=0,
    res="São 5 variáveis (F, V, D, ρ, μ) e 3 dimensões fundamentais (M, L, T): 5 − 3 = <b>2 grupos</b>. Por exemplo, o coeficiente de arrasto C<sub>D</sub> = F/(½ρV²A) e o número de Reynolds: C<sub>D</sub> = f(Re).")

Cc = 0.62 / 0.98
num("MEC-F39", F, "Coeficientes de orifício",
    "Num orifício de parede fina, o coeficiente de descarga é 0,62 e o coeficiente de velocidade é 0,98. O coeficiente de contração do jato é, aproximadamente,",
    Cc, [0.62 * 0.98, 0.98, 0.62, 0.36], d=3,
    res=f"C<sub>d</sub> = C<sub>c</sub>·C<sub>v</sub> → C<sub>c</sub> = 0,62/0,98 = <b>{br(Cc,3)}</b>. A perda pelo atrito é pequena (C<sub>v</sub> ≈ 0,98); a redução de vazão vem quase toda da contração do jato (vena contracta).")

con("MEC-F40", F, "Escoamento por gravidade entre reservatórios",
    "Dois reservatórios abertos, com desnível de 15 m entre as superfícies livres, são ligados por uma tubulação longa, e a água escoa por gravidade em regime permanente. Desprezando as cargas cinéticas nas superfícies, é correto afirmar que",
    "a perda de carga total na tubulação é igual a 15 m, qualquer que seja a vazão estabelecida",
    ["a perda de carga é nula, pois não há bomba",
     "a perda de carga é igual a 7,5 m, metade do desnível",
     "a velocidade na tubulação vale √(2g × 15), sem influência do atrito",
     "a vazão não depende do diâmetro da tubulação"],
    res="Equação da energia entre as superfícies: z<sub>1</sub> = z<sub>2</sub> + h<sub>f</sub> → <b>h<sub>f</sub> = 15 m</b>. A vazão se ajusta até que as perdas consumam exatamente o desnível. Um diâmetro maior perde menos por metro, então a vazão sobe até a perda voltar a 15 m.")

dp = 2 * 0.073 / 1e-4
num("MEC-F41", F, "Pressão no interior de uma gota",
    "Uma gota de água esférica tem raio de 0,1 mm, e a tensão superficial é 0,073 N/m. A diferença entre a pressão interna e a externa, em Pa, é, aproximadamente,",
    dp, [dp / 2, 2 * dp, 0.073 / 1e-4, 14.6], d=0,
    res=f"Equilíbrio de meia gota: Δp·πr² = σ·2πr → Δp = 2σ/r = 2 × 0,073/10<sup>−4</sup> = <b>{br(dp,0)} Pa</b>. Numa bolha de sabão (duas superfícies), seria 4σ/r.")

con("MEC-F42", F, "Medidores de vazão por obstrução",
    "Comparando a placa de orifício com o tubo Venturi como medidores de vazão, é correto afirmar que a placa de orifício",
    "é mais barata e fácil de instalar, mas causa perda de carga permanente bem maior",
    ["causa perda de carga permanente menor que o Venturi",
     "dispensa trechos retos de tubulação a montante",
     "tem coeficiente de descarga próximo de 0,98, como o Venturi",
     "mede a vazão pela velocidade do som no fluido"],
    res="O Venturi desacelera o fluido aos poucos no difusor e recupera quase toda a pressão; a placa de orifício gera um jato livre e turbulência, com <b>perda permanente</b> de 40% a 90% da pressão diferencial. Em compensação, a placa é simples, barata e normalizada. C<sub>d</sub> ≈ 0,6 na placa e ≈ 0,98 no Venturi.")

R = "Resistência dos Materiais"
ev = 100 / 200000 * (1 - 2 * 0.3)
num("MEC-R31", R, "Deformação volumétrica",
    "Uma barra de aço (E = 200 GPa; ν = 0,3) é tracionada uniaxialmente com tensão de 100 MPa, no regime elástico. A deformação volumétrica (variação relativa de volume) é",
    ev, [100 / 200000, 100 / 200000 * (1 + 2 * 0.3), 100 / 200000 * 0.6, 100 / 200000 * 0.3], fmt=lambda v: br(v * 1e4, 1) + " × 10<sup>−4</sup>",
    res=f"ε<sub>long</sub> = 5 × 10<sup>−4</sup>; ε<sub>lat</sub> = −0,3 × 5 × 10<sup>−4</sup> (nas duas direções). ε<sub>v</sub> = ε(1 − 2ν) = 5 × 10<sup>−4</sup> × 0,4 = <b>2,0 × 10<sup>−4</sup></b>. O volume aumenta na tração; com ν = 0,5 (borracha), ficaria constante.")

RA = 30 * 4 / 6
num("MEC-R32", R, "Reações de apoio com carga excêntrica",
    "Uma viga biapoiada de 6 m de vão (apoios A e B) recebe uma carga concentrada de 30 kN a 2 m do apoio A. A reação no apoio A, em kN, é",
    RA, [10, 15, 30, 25], d=0,
    res=f"Momentos em B: R<sub>A</sub> × 6 = 30 × 4 → R<sub>A</sub> = <b>{br(RA,0)} kN</b> e R<sub>B</sub> = 10 kN. O apoio mais próximo da carga recebe a maior parcela; inverter as distâncias dá 10 kN.")

M = 30 * 2 * 4 / 6
num("MEC-R33", R, "Momento máximo com carga fora do centro",
    "Na mesma viga biapoiada de 6 m, com carga de 30 kN a 2 m do apoio A, o momento fletor máximo, em kN·m, é",
    M, [45, 60, 20, 30], d=0,
    res=f"O momento máximo ocorre sob a carga: M = P·a·b/L = 30 × 2 × 4/6 = <b>{br(M,0)} kN·m</b> (ou R<sub>A</sub> × 2 = 20 × 2). Com a carga no meio, seria PL/4 = 45 kN·m, o maior possível.")

con("MEC-R34", R, "Relações entre carga, cortante e momento",
    "Numa viga carregada, a relação diferencial entre o esforço cortante V e o momento fletor M ao longo do eixo x permite concluir que",
    "o momento fletor é máximo (ou mínimo) onde o esforço cortante se anula ou muda de sinal",
    ["o cortante é máximo onde o momento é máximo",
     "o momento é constante em trechos com carga distribuída",
     "o cortante é sempre nulo nos apoios",
     "o diagrama de momento é retilíneo em trechos com carga uniforme"],
    res="dM/dx = V e dV/dx = −w. Onde <b>V = 0</b>, M tem um extremo. Em trechos com carga uniforme, V é linear e M é parabólico; em trechos sem carga, V é constante e M é linear.")

s = 10e6 * 32 / (math.pi * 100 ** 3)
num("MEC-R35", R, "Flexão em eixo maciço",
    "Um eixo maciço de 100 mm de diâmetro está submetido a um momento fletor de 10 kN·m. A tensão normal máxima de flexão, em MPa, é, aproximadamente,",
    s, [s / 2, 2 * s, s * 32 / 64 * 4, 12.7], d=1,
    res=f"W = πd³/32 = π × 100³/32 = 98.175 mm³. σ = M/W = 10 × 10⁶/98.175 = <b>{br(s,1)} MPa</b>. O fator 16 (πd³/16) é o módulo polar, da torção; usá-lo na flexão dá metade da tensão.")

sp = 78.5 * 100 / 1000
num("MEC-R36", R, "Tensão por peso próprio",
    "Uma barra de aço (peso específico 78,5 kN/m³) com 100 m de comprimento está pendurada verticalmente pela extremidade superior. A tensão normal máxima devida ao peso próprio, em MPa, é",
    sp, [sp / 2, 78.5, 0.785, 2 * sp], d=2,
    res=f"No topo, a seção sustenta o peso de toda a barra: σ = γAL/A = γL = 78,5 × 100 = 7.850 kPa = <b>{br(sp,2)} MPa</b>. Independe da área. Por isso cabos muito longos (elevadores de minas) limitam o comprimento útil.")

N = 10 / (2 * 0.5)
num("MEC-R37", R, "Esforço em barras de treliça",
    "Duas barras iguais, simétricas, formam um \"V\" invertido e sustentam no nó superior uma carga vertical de 10 kN. Cada barra faz 30° com a horizontal. O esforço de compressão em cada barra, em kN, é",
    N, [5, 5.77, 8.66, 20], d=2,
    res=f"Equilíbrio vertical do nó: 2·N·sen 30° = 10 → N = 10/(2 × 0,5) = <b>{br(N,2)} kN</b>. Quanto mais \"deitadas\" as barras, maior o esforço: com 10° de inclinação, cada uma levaria 28,8 kN.")

I = 1e-6; Pcr = math.pi ** 2 * 200e9 * I / (0.7 * 3) ** 2 / 1000
num("MEC-R38", R, "Flambagem de coluna engastada-articulada",
    "Uma coluna de aço (E = 200 GPa; I = 1 × 10<sup>−6</sup> m⁴) com 3 m de comprimento é engastada na base e articulada no topo (L<sub>e</sub> = 0,7L). A carga crítica de Euler, em kN, é, aproximadamente,",
    Pcr, [Pcr * 0.49, Pcr * 0.49 / 4, Pcr * 0.49 * 4, Pcr * 0.7], d=0,
    res=f"P<sub>cr</sub> = π²EI/(0,7L)² = 9,87 × 200 × 10⁹ × 10<sup>−6</sup>/(2,1)² = 1,974 × 10⁶/4,41 = <b>{br(Pcr,0)} kN</b>. Biarticulada, seria 219 kN; biengastada, 877 kN.")

sr = 7850 * 100 ** 2 / 1e6
num("MEC-R39", R, "Tensão em anel girante",
    "Um anel fino de aço (ρ = 7.850 kg/m³) gira em torno do seu eixo, com velocidade periférica de 100 m/s. A tensão circunferencial no anel, σ = ρv², em MPa, é, aproximadamente,",
    sr, [sr / 2, 2 * sr, 0.785, 785], d=1,
    res=f"σ = ρv² = 7.850 × 100² = 78,5 × 10⁶ Pa = <b>{br(sr,1)} MPa</b>. A tensão não depende da seção nem do raio, só da velocidade periférica: é o que limita a rotação de volantes e rebolos.")

num("MEC-R40", R, "Carga aplicada subitamente",
    "Uma carga é aplicada de forma súbita (sem velocidade inicial, mas instantaneamente) sobre uma barra elástica. A tensão máxima produzida, comparada à que a mesma carga produziria se aplicada lentamente, fica multiplicada por",
    2, [1, 1.5, 4, 3], d=0,
    res="Fator de impacto: 1 + √(1 + 2h/δ<sub>est</sub>). Com altura de queda h = 0 (carga súbita): 1 + 1 = <b>2</b>. A energia potencial Pδ vira energia elástica ½kδ², então a deflexão máxima é o dobro da estática.")

g = 40 / 80000
num("MEC-R41", R, "Deformação angular por cisalhamento",
    "Uma peça de aço (G = 80 GPa) está submetida a tensão de cisalhamento de 40 MPa, no regime elástico. A distorção angular, em radianos, é",
    g, [40 / 200000, 2 * g, g / 2, 40 / 100000], fmt=lambda v: br(v * 1e4, 1) + " × 10<sup>−4</sup>",
    res=f"Lei de Hooke no cisalhamento: γ = τ/G = 40/80.000 = <b>5,0 × 10<sup>−4</sup> rad</b>. Usar E no lugar de G (2,0 × 10<sup>−4</sup>) é o erro comum.")

con("MEC-R42", R, "Distribuição de esforços em perfil I",
    "Numa viga de perfil I sob flexão simples, é correto afirmar que",
    "as mesas resistem à maior parte do momento fletor, e a alma resiste à maior parte do esforço cortante",
    ["a alma resiste à maior parte do momento fletor",
     "as mesas resistem à maior parte do esforço cortante",
     "a tensão de cisalhamento é máxima nas faces externas das mesas",
     "a tensão normal é máxima na linha neutra"],
    res="As <b>mesas</b> ficam longe da linha neutra, onde a tensão de flexão é máxima: carregam o momento. A <b>alma</b> carrega o cortante (τ ≈ V/(h·t<sub>w</sub>)). Na linha neutra, a tensão normal é nula e o cisalhamento é máximo.")

con("MEC-R43", R, "Cilindros de parede grossa",
    "Num cilindro de parede grossa sob pressão interna (equações de Lamé), a tensão circunferencial",
    "é máxima na face interna e diminui em direção à face externa",
    ["é uniforme ao longo da espessura, como no cilindro de parede fina",
     "é máxima na face externa",
     "é nula na face interna",
     "é sempre de compressão"],
    res="Lamé: σ<sub>θ</sub> = A + B/r² decresce com o raio, sendo <b>máxima na face interna</b>. Aumentar a espessura ajuda cada vez menos. Por isso se usam cilindros compostos (fretados) ou autofretagem, que induzem compressão residual na parede interna.")
