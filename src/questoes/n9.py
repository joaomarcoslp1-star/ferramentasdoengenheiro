# -*- coding: utf-8 -*-
# Lote 5 (28/11/2026): Termodinâmica, Mecânica dos Fluidos, Resistência dos Materiais
import math
from nbase import num, con, br

T = "Termodinâmica"
ec = (1 - 3 / 12) * 100
num("MEC-T57", T, "Economia da bomba de calor",
    "Para aquecer um ambiente com 12 kW, compara-se uma resistência elétrica (que converte toda a energia elétrica em calor) com uma bomba de calor de COP = 4. A economia de energia elétrica da bomba de calor em relação à resistência é de",
    ec, [25, 80, 90, 85], fmt=lambda v: br(v, 0) + "%",
    res=f"Resistência: 12 kW elétricos. Bomba de calor: 12/4 = 3 kW. Economia = (12 − 3)/12 = <b>{br(ec,0)}%</b>. A bomba de calor não \"cria\" energia: ela retira 9 kW do ar externo e gasta 3 kW para bombeá-los até a temperatura mais alta.")

rho = 100 / (0.287 * 300)
num("MEC-T58", T, "Massa específica do ar",
    "A massa específica do ar (R = 0,287 kJ/kg·K), tratado como gás ideal, a 100 kPa e 27 °C, em kg/m³, é, aproximadamente,",
    rho, [100 / (0.287 * 27), 0.287 * 300 / 100, 100 / (8.314 * 300), 1.29], d=2,
    res=f"ρ = P/(RT) = 100/(0,287 × 300) = <b>{br(rho,2)} kg/m³</b>. A 0 °C e 101,3 kPa, seria 1,29 kg/m³. Com a temperatura em °C, a conta dá 12,9, sem sentido.")

W = 0.718 * (600 - 400)
num("MEC-T59", T, "Trabalho em expansão adiabática",
    "Um quilograma de ar (c<sub>v</sub> = 0,718 kJ/kg·K; c<sub>p</sub> = 1,005 kJ/kg·K) num cilindro se expande adiabaticamente, e sua temperatura cai de 600 K para 400 K. O trabalho realizado pelo ar, em kJ, é, aproximadamente,",
    W, [1.005 * 200, 0.287 * 200, 0, 0.718 * 600], d=0,
    res=f"Sistema fechado adiabático: Q = 0 → W = −ΔU = m·c<sub>v</sub>·(T<sub>1</sub> − T<sub>2</sub>) = 0,718 × 200 = <b>{br(W,0)} kJ</b>. O gás gasta a própria energia interna para empurrar o pistão. Com c<sub>p</sub> (201 kJ), seria o trabalho de eixo de uma turbina, em volume de controle.")

con("MEC-T60", T, "Ignição no motor Diesel",
    "No motor Diesel de quatro tempos, a combustão começa",
    "por autoignição do combustível injetado no ar, que foi aquecido acima da temperatura de ignição pela compressão a alta taxa",
    ["pela centelha da vela, como no motor Otto",
     "pela mistura ar-combustível admitida já pronta no carburador",
     "por uma chama piloto permanente na câmara",
     "pela detonação controlada da mistura no início da compressão"],
    res="O Diesel comprime <b>só ar</b> (taxas de 15 a 22), que chega a 500–700 °C; o combustível injetado no fim da compressão se inflama sozinho. Como não há mistura pronta durante a compressão, não existe o limite de detonação do Otto, e a taxa pode ser maior.")

Tf = 1.4 * 300
num("MEC-T61", T, "Enchimento de tanque evacuado",
    "Um tanque rígido e isolado, inicialmente evacuado, é enchido com ar de uma linha de alimentação a 300 K, até a pressão se igualar à da linha. Considerando o ar gás ideal com k = 1,4, a temperatura final do ar no tanque, em K, é",
    Tf, [300, 300 / 1.4, 600, 360], d=0,
    res=f"Balanço de energia do volume de controle em regime transiente: m<sub>2</sub>u<sub>2</sub> = m<sub>e</sub>h<sub>linha</sub> → c<sub>v</sub>T<sub>2</sub> = c<sub>p</sub>T<sub>linha</sub> → T<sub>2</sub> = k·T<sub>linha</sub> = <b>{br(Tf,0)} K</b>. O trabalho de \"empurrar\" o ar para dentro (Pv) vira energia interna, e o tanque esquenta. É por isso que cilindros de mergulho esquentam ao serem enchidos.")

dTw = 2 * 1.005 * 30 / (5 * 4.18)
num("MEC-T62", T, "Balanço de energia em trocador ar-água",
    "Num resfriador, 2 kg/s de ar (c<sub>p</sub> = 1,005 kJ/kg·K) são resfriados em 30 K por 5 kg/s de água (c = 4,18 kJ/kg·K). Sem perdas para o ambiente, o aquecimento da água, em K, é, aproximadamente,",
    dTw, [30, 12, 2 * 30 / 5, dTw * 4.18], d=1,
    res=f"Calor retirado do ar: 2 × 1,005 × 30 = 60,3 kW. Aquecimento da água: 60,3/(5 × 4,18) = <b>{br(dTw,1)} K</b>. A água tem calor específico quatro vezes maior e vazão maior, por isso varia pouco de temperatura.")

cop = (390 - 240) / (420 - 390)
num("MEC-T63", T, "COP pelo ciclo de refrigeração",
    "Num ciclo de refrigeração por compressão de vapor, as entalpias são: saída do evaporador 390 kJ/kg, saída do compressor 420 kJ/kg e saída do condensador 240 kJ/kg. O COP do ciclo é",
    cop, [cop + 1, 390 / 30, 180 / 150, 420 / 390], d=1,
    res=f"Efeito refrigerante: h<sub>1</sub> − h<sub>4</sub> = 390 − 240 = 150 kJ/kg (a válvula é isentálpica: h<sub>4</sub> = h<sub>3</sub>). Trabalho: 420 − 390 = 30 kJ/kg. COP = 150/30 = <b>{br(cop,1)}</b>. COP + 1 = 6 seria o da bomba de calor (calor no condensador: 180 kJ/kg).")

con("MEC-T64", T, "Temperatura de bulbo úmido",
    "A temperatura de bulbo úmido do ar, medida num psicrômetro com o bulbo envolto em gaze molhada e ventilada, é",
    "menor que a de bulbo seco quando o ar não está saturado, porque a evaporação da água da gaze retira calor do bulbo",
    ["sempre igual à de bulbo seco",
     "maior que a de bulbo seco em ar seco",
     "igual ao ponto de orvalho em qualquer condição",
     "independente da umidade do ar"],
    res="Quanto mais seco o ar, mais água evapora da gaze e <b>maior a diferença</b> entre bulbo seco e úmido. Com ar saturado, não há evaporação, e bulbo seco, bulbo úmido e orvalho coincidem. Torres de resfriamento só conseguem resfriar a água até perto do bulbo úmido.")

eta = 17 / (0.5 * 40) * 100
num("MEC-T65", T, "Rendimento de caldeira",
    "Uma caldeira queima 0,5 kg/s de combustível com poder calorífico inferior de 40 MJ/kg e entrega 17 MW à água e ao vapor. O rendimento da caldeira (base PCI) é",
    eta, [42.5, 80, 88, 90, 94, 100], fmt=lambda v: br(v, 0) + "%",
    res=f"Energia do combustível: 0,5 × 40 = 20 MW. η = 17/20 = <b>{br(eta,0)}%</b>. As perdas são principalmente o calor sensível dos gases na chaminé, combustão incompleta e radiação pelas paredes.")

HR = 3600 / 0.40
num("MEC-T66", T, "Consumo específico de calor (heat rate)",
    "Uma usina térmica tem rendimento global de 40%. Seu consumo específico de calor (heat rate), em kJ por kWh gerado, é",
    HR, [3600 * 0.4, 3600, 2500, 1440 * 2], d=0,
    res=f"1 kWh = 3.600 kJ. Com 40% de rendimento: HR = 3.600/0,40 = <b>{br(HR,0)} kJ/kWh</b>. Quanto menor o heat rate, mais eficiente a usina; ciclos combinados chegam a cerca de 6.000 kJ/kWh.")

mf = 100 / (0.35 * 42000) * 3600
num("MEC-T67", T, "Consumo de combustível de motor",
    "Um motor entrega 100 kW no eixo com rendimento térmico efetivo de 35%, queimando combustível com poder calorífico de 42 MJ/kg. O consumo de combustível, em kg/h, é, aproximadamente,",
    mf, [100 * 0.35 / 42000 * 3600, 100 / 42000 * 3600, mf * 2, 0.0068], d=1,
    res=f"Potência do combustível: 100/0,35 = 285,7 kW. ṁ = 285,7/42.000 = 0,0068 kg/s × 3.600 = <b>{br(mf,1)} kg/h</b>. O consumo específico correspondente é 245 g/kWh, típico de motores diesel.")

con("MEC-T68", T, "Terceira lei da termodinâmica",
    "A terceira lei da termodinâmica estabelece que",
    "a entropia de uma substância cristalina pura e perfeita tende a zero quando a temperatura tende ao zero absoluto",
    ["a energia de um sistema isolado é constante",
     "o rendimento de qualquer máquina térmica é menor que 1",
     "a entropia de um sistema isolado nunca diminui",
     "dois corpos em equilíbrio térmico com um terceiro estão em equilíbrio entre si"],
    res="A <b>terceira lei</b> fornece uma referência absoluta para a entropia (S = 0 a 0 K para o cristal perfeito), usada em reações químicas e tabelas de entropia absoluta. As outras alternativas são a primeira lei, consequências da segunda e a lei zero.")

pO2 = 300 * 1 / 3
num("MEC-T69", T, "Pressão parcial (lei de Dalton)",
    "Um tanque contém uma mistura de 2 kmol de N<sub>2</sub> e 1 kmol de O<sub>2</sub>, tratados como gases ideais, à pressão total de 300 kPa. A pressão parcial do O<sub>2</sub>, em kPa, é",
    pO2, [200, 150, 300, 32 / 60 * 300], d=0,
    res=f"Dalton: p<sub>i</sub> = y<sub>i</sub>·P, com y<sub>O2</sub> = 1/3. p<sub>O2</sub> = 300/3 = <b>{br(pO2,0)} kPa</b>. A fração é molar, não mássica: usar massas (32 kg de O<sub>2</sub> contra 56 kg de N<sub>2</sub>) dá outro valor.")

con("MEC-T70", T, "Trabalho de bombear líquido e comprimir gás",
    "No escoamento reversível em regime permanente, o trabalho de eixo por unidade de massa é w = −∫v dP. Por isso, para o mesmo aumento de pressão,",
    "bombear um líquido consome muito menos trabalho do que comprimir um gás, porque o volume específico do líquido é muito menor",
    ["comprimir um gás consome menos trabalho, pois o gás é mais leve",
     "o trabalho é o mesmo, pois depende apenas da diferença de pressão",
     "bombear um líquido consome mais trabalho, pois o líquido é incompressível",
     "o trabalho independe do volume específico"],
    res="Com v do líquido cerca de mil vezes menor que o do vapor, a integral ∫v dP também é cerca de mil vezes menor. É por isso que o ciclo Rankine (que bombeia líquido) gasta tão pouco na bomba, enquanto o Brayton gasta perto de metade do trabalho da turbina no compressor. Também explica por que o resfriamento intermediário reduz o trabalho de compressão: diminui v.")

F = "Mecânica dos Fluidos"
num("MEC-F57", F, "Vácuo e pressão absoluta",
    "Um vacuômetro conectado a um condensador indica −70 kPa (pressão manométrica) num local onde a pressão atmosférica é 100 kPa. A pressão absoluta no condensador, em kPa, é",
    30, [70, 170, -70, 0], d=0,
    res="p<sub>abs</sub> = p<sub>atm</sub> + p<sub>man</sub> = 100 + (−70) = <b>30 kPa</b>. Pressões absolutas nunca são negativas; valores negativos só aparecem em escala manométrica (vácuo).")

A = math.pi * 0.5 ** 2 / 4; F_ = 1000 * 10 * 2 * A / 1000
num("MEC-F58", F, "Força em visor circular vertical",
    "Um visor circular de 0,5 m de diâmetro está na parede vertical de um tanque de água, com o centro a 2 m de profundidade (g = 10 m/s²). A força resultante da água sobre o visor, em kN, é, aproximadamente,",
    F_, [F_ * 4, F_ / 2, F_ * 1.25, 20], d=2,
    res=f"Em superfícies planas, F = ρg·h<sub>CG</sub>·A = 1.000 × 10 × 2 × (π × 0,5²/4) = 20.000 × 0,196 = <b>{br(F_,2)} kN</b>. O ponto de aplicação (centro de pressão) fica um pouco abaixo do centro do visor.")

p = -(1000 * 10 * 1 + 0.5 * 1000 * 36) / 1000
num("MEC-F59", F, "Pressão no ponto alto de um sifão",
    "Num sifão, a água passa a 6 m/s por um ponto situado 1 m acima da superfície livre do reservatório de origem. Desprezando perdas e com g = 10 m/s², a pressão manométrica nesse ponto, em kPa, é",
    p, [-10, -18, 28, -46], fmt=lambda v: br(v, 0),
    res=f"Bernoulli da superfície (p = 0, V = 0, z = 0) ao ponto alto: 0 = p/ρ + V²/2 + gz → p = −1.000 × (18 + 10) = −28.000 Pa = <b>{br(p,0)} kPa</b>. Se a pressão absoluta ali cair até a pressão de vapor, a coluna se rompe e o sifão para.")

Fc = 1000 * 0.02 * 5 * math.sqrt(2)
num("MEC-F60", F, "Força em curva de 90°",
    "Uma curva de 90°, num plano horizontal, conduz 20 L/s de água (ρ = 1.000 kg/m³) a 5 m/s, com diâmetro constante. Desprezando a pressão e o peso, a força resultante que a água exerce na curva, em N, é, aproximadamente,",
    Fc, [100, 200, Fc / 2, 2 * Fc], d=0,
    res=f"A quantidade de movimento muda de direção: ṁV = 1.000 × 0,02 × 5 = 100 N em cada eixo. A resultante é √(100² + 100²) = <b>{br(Fc,0)} N</b>, a 45°. Em linhas pressurizadas, soma-se a parcela p·A, que costuma ser bem maior: daí os blocos de ancoragem nas curvas.")

num("MEC-F61", F, "Perfil de velocidade laminar",
    "No escoamento laminar plenamente desenvolvido num tubo circular, a velocidade média é de 0,5 m/s. A velocidade máxima, no centro do tubo, em m/s, é",
    1.0, [0.5, 0.25, 0.6, 2.0], d=2,
    res="O perfil laminar é parabólico (Hagen-Poiseuille): V<sub>máx</sub> = 2·V<sub>média</sub> = <b>1,0 m/s</b>. No turbulento, o perfil é achatado e V<sub>máx</sub> ≈ 1,2·V<sub>média</sub>.")

con("MEC-F62", F, "Perfil de velocidade turbulento",
    "Comparado ao perfil laminar num tubo, o perfil de velocidade do escoamento turbulento é",
    "mais achatado no centro, com gradiente de velocidade muito forte junto à parede, o que aumenta a tensão de cisalhamento na parede",
    ["parabólico, com velocidade máxima igual a duas vezes a média",
     "uniforme, com velocidade nula em toda a seção",
     "mais pontiagudo, com velocidade máxima maior que no laminar",
     "linear, como no escoamento de Couette"],
    res="A mistura turbulenta uniformiza a velocidade no núcleo (lei de potência ≈ 1/7), e quase toda a variação fica concentrada numa camada fina junto à parede. O gradiente forte aumenta o <b>atrito na parede</b> e também a troca de calor.")

hf2 = 32 / 2 ** 5
num("MEC-F63", F, "Efeito do diâmetro na perda de carga",
    "Numa tubulação longa, em escoamento turbulento com fator de atrito constante, a perda de carga é de 32 m para certa vazão. Se o diâmetro for dobrado, mantida a vazão, a nova perda de carga, em m, será",
    hf2, [16, 8, 4, 2, 0.5], d=1,
    res=f"Com Q constante, V ∝ 1/D², e h<sub>f</sub> = f(L/D)V²/2g ∝ 1/D⁵. Dobrar o diâmetro divide a perda por 2⁵ = 32: <b>{br(hf2,0)} m</b>. É por isso que um pequeno aumento de diâmetro reduz muito o custo de bombeamento.")

p0 = 100 + 0.5 * 1.2 * 50 ** 2 / 1000
num("MEC-F64", F, "Pressão de estagnação",
    "Ar (ρ = 1,2 kg/m³) escoa a 50 m/s com pressão estática absoluta de 100 kPa. A pressão de estagnação (total), em kPa, é",
    p0, [100, 103, 101.2, 250], d=1,
    res=f"p<sub>0</sub> = p + ½ρV² = 100 + 0,5 × 1,2 × 2.500/1.000 = 100 + 1,5 = <b>{br(p0,1)} kPa</b>. Abaixo de Mach 0,3 (cerca de 100 m/s), a forma incompressível é precisa o bastante.")

CD = 24 / 0.5
num("MEC-F65", F, "Arrasto no regime de Stokes",
    "Para uma esfera em escoamento com número de Reynolds muito baixo (regime de Stokes), o coeficiente de arrasto é C<sub>D</sub> = 24/Re. Para Re = 0,5, C<sub>D</sub> vale",
    CD, [12, 4.8, 96, 24], d=1,
    res=f"C<sub>D</sub> = 24/0,5 = <b>{br(CD,0)}</b>. Em Re baixo, o arrasto é dominado pela viscosidade, e C<sub>D</sub> é alto. Em Re de 10³ a 10⁵, o C<sub>D</sub> da esfera fica em torno de 0,47.")

Lft = 1.2 * 0.5 * 1.2 * 50 ** 2 * 20 / 1000
num("MEC-F66", F, "Força de sustentação",
    "Uma asa com área de 20 m² e coeficiente de sustentação 1,2 voa a 50 m/s no ar (ρ = 1,2 kg/m³). A força de sustentação, em kN, é",
    Lft, [2 * Lft, Lft / 1.2, 1.44, 3.6], d=0,
    res=f"L = C<sub>L</sub>·½ρV²·A = 1,2 × 0,5 × 1,2 × 2.500 × 20 = 36.000 N = <b>{br(Lft,0)} kN</b>, o suficiente para sustentar cerca de 3,7 toneladas. Esquecer o ½ dobra a força.")

num("MEC-F67", F, "Diâmetro hidráulico de seção anular",
    "Um fluido escoa no espaço anular entre um tubo externo de 100 mm de diâmetro interno e um tubo interno de 60 mm de diâmetro externo (como num trocador bitubular). O diâmetro hidráulico, em mm, é",
    40, [80, 20, 100, 160], d=0,
    res="D<sub>h</sub> = 4A/P = 4·(π/4)(D² − d²)/[π(D + d)] = D − d = 100 − 60 = <b>40 mm</b>. O perímetro molhado inclui as duas paredes, externa e interna.")

con("MEC-F68", F, "Rotâmetro",
    "O rotâmetro, medidor de vazão formado por um flutuador dentro de um tubo vertical cônico, funciona porque",
    "o flutuador sobe até a posição em que a área anular livre gera a queda de pressão que equilibra seu peso aparente, e a altura indica a vazão",
    ["o flutuador gira com velocidade proporcional à vazão",
     "a queda de pressão no flutuador aumenta com a vazão, e o flutuador desce",
     "o tubo cônico funciona como um Venturi de área fixa",
     "o flutuador mede a temperatura do fluido"],
    res="No <b>rotâmetro</b> (medidor de área variável), a queda de pressão através do flutuador é praticamente constante; o que muda é a área de passagem, que cresce com a altura no tubo cônico. Ele precisa ser instalado na vertical e calibrado para a densidade do fluido.")

M_ = 272 / 340
num("MEC-F69", F, "Número de Mach",
    "Um avião voa a 272 m/s numa altitude em que a velocidade do som é 340 m/s. O número de Mach do voo é",
    M_, [1.25, 0.64, 0.92, 0.8 * 340 / 272], d=2,
    res=f"Ma = V/c = 272/340 = <b>{br(M_,2)}</b>: subsônico alto. Acima de Ma ≈ 0,3, os efeitos de compressibilidade já são importantes; perto de 0,8, surgem regiões locais supersônicas sobre a asa.")

con("MEC-F70", F, "Condição de não deslizamento",
    "A condição de não deslizamento, usada na análise de escoamentos viscosos, estabelece que",
    "o fluido em contato com uma superfície sólida tem a mesma velocidade da superfície",
    ["o fluido desliza livremente sobre a parede, sem atrito",
     "a velocidade do fluido é máxima junto à parede",
     "a pressão é nula junto à parede",
     "só vale para gases, não para líquidos"],
    res="Junto à parede, a velocidade relativa é nula (parede parada → fluido parado). Isso gera o gradiente de velocidade, a <b>camada limite</b> e o atrito viscoso. Bernoulli e o escoamento potencial ignoram essa condição; por isso não preveem o arrasto de atrito.")

R = "Resistência dos Materiais"
M = 10 * 1
num("MEC-R60", R, "Flexão em quatro pontos",
    "Uma viga biapoiada de 3 m recebe duas cargas concentradas de 10 kN, aplicadas a 1 m de cada apoio. O momento fletor no trecho central, entre as cargas, em kN·m, é",
    M, [15, 20, 7.5, 30], d=0,
    res=f"Reações de 10 kN em cada apoio. Sob a carga, M = 10 × 1 = 10 kN·m; entre as cargas, o cortante é nulo e o momento fica <b>constante em {br(M,0)} kN·m</b> (flexão pura). É a montagem usada para ensaiar vigas sem cortante no trecho central.")

Mt = 10 * 6 ** 2 / (9 * math.sqrt(3))
num("MEC-R61", R, "Momento máximo com carga triangular",
    "Uma viga biapoiada de 6 m recebe carga distribuída triangular, de zero num apoio até 10 kN/m no outro. Sabendo que o momento máximo é w<sub>0</sub>L²/(9√3) e √3 ≈ 1,732, ele vale, em kN·m, aproximadamente,",
    Mt, [10 * 36 / 8, 10 * 36 / 16, 10 * 36 / 12, 10 * 36 / 6, 10 * 36 / 9], d=1,
    res=f"M<sub>máx</sub> = 10 × 36/(9 × 1,732) = 360/15,59 = <b>{br(Mt,1)} kN·m</b>, a L/√3 ≈ 3,46 m do apoio onde a carga é nula. wL²/8 = 45 kN·m seria para a carga uniforme de 10 kN/m, com o dobro da resultante.")

tau = 4 / 3 * 10000 / (math.pi * 40 ** 2 / 4)
num("MEC-R62", R, "Cisalhamento máximo em seção circular",
    "Uma viga de seção circular maciça com 40 mm de diâmetro está submetida a esforço cortante de 10 kN. A tensão de cisalhamento máxima na seção, em MPa, é, aproximadamente,",
    tau, [10000 / (math.pi * 40 ** 2 / 4), 1.5 * 10000 / (math.pi * 40 ** 2 / 4), 2 * 10000 / (math.pi * 40 ** 2 / 4), 4.0], d=1,
    res=f"Em seção circular maciça, τ<sub>máx</sub> = (4/3)·V/A = 1,333 × 10.000/1.256,6 = <b>{br(tau,1)} MPa</b>, na linha neutra. O fator 1,5 é da seção retangular; 2 é do tubo de parede fina.")

num("MEC-R63", R, "Efeito do diâmetro no ângulo de torção",
    "Dois eixos maciços do mesmo material e comprimento recebem o mesmo torque. O diâmetro do segundo é metade do diâmetro do primeiro. O ângulo de torção do segundo, comparado ao do primeiro, é multiplicado por",
    16, [2, 4, 8, 32], d=0,
    res="φ = TL/(GJ), com J = πd⁴/32. Metade do diâmetro → J dividido por 2⁴ = 16 → ângulo <b>16 vezes</b> maior. A tensão cresceria 8 vezes (d³).")

Pc = math.pi ** 2 * 200000 / 150 ** 2 * 2000 / 1000
num("MEC-R64", R, "Carga crítica pela tensão de Euler",
    "Uma coluna de aço (E = 200 GPa) tem área de seção de 2.000 mm² e índice de esbeltez 150. A carga crítica de Euler, em kN, é, aproximadamente,",
    Pc, [Pc * 1.5, Pc / 1.5, Pc * 2.25, 400], d=0,
    res=f"σ<sub>cr</sub> = π²E/λ² = 9,87 × 200.000/22.500 = 87,7 MPa. P<sub>cr</sub> = σ<sub>cr</sub>·A = 87,7 × 2.000 = <b>{br(Pc,0)} kN</b>. Muito abaixo da carga de escoamento (500 kN com 250 MPa): coluna esbelta, governada pela flambagem.")

ex = (100 - 0.3 * 50) / 200000
num("MEC-R65", R, "Lei de Hooke generalizada",
    "Num estado plano de tensões, σ<sub>x</sub> = 100 MPa e σ<sub>y</sub> = 50 MPa, sem cisalhamento. Com E = 200 GPa e ν = 0,3, a deformação ε<sub>x</sub> é",
    ex, [100 / 200000, (100 + 0.3 * 50) / 200000, (100 - 0.3 * 100) / 200000, 50 / 200000], fmt=lambda v: br(v * 1e4, 2) + " × 10<sup>−4</sup>",
    res=f"ε<sub>x</sub> = [σ<sub>x</sub> − ν·σ<sub>y</sub>]/E = (100 − 0,3 × 50)/200.000 = 85/200.000 = <b>4,25 × 10<sup>−4</sup></b>. A tração em y encurta x pelo efeito Poisson; ignorá-la dá 5,0 × 10<sup>−4</sup>.")

con("MEC-R66", R, "Vasos sob pressão externa (vácuo)",
    "Um vaso cilíndrico de parede fina projetado para pressão interna pode falhar ao operar sob vácuo (pressão externa) mesmo com tensões baixas, porque",
    "sob pressão externa o modo de falha é a instabilidade elástica (flambagem do casco), e por isso se usam anéis de reforço ou maior espessura",
    ["a pressão externa gera tensões de tração maiores que a interna",
     "o vácuo reduz o módulo de elasticidade do aço",
     "a tensão de membrana dobra sob pressão externa",
     "a solda perde resistência sob compressão"],
    res="Sob pressão externa, as tensões de membrana são de compressão, e o casco fino pode <b>flambar</b> (colapsar) muito antes de escoar. A pressão crítica depende de E, de (t/D)³ e do comprimento entre reforços. Caminhões-tanque implodidos por vácuo são o exemplo clássico.")

tau_a = 5000 / (25 * 50)
num("MEC-R67", R, "Cisalhamento em junta colada",
    "Duas chapas são coladas numa junta sobreposta com área de colagem de 25 mm × 50 mm e tracionadas com 5 kN. A tensão de cisalhamento média no adesivo, em MPa, é",
    tau_a, [2, 8, 20, 0.4], d=1,
    res=f"τ = F/A = 5.000/(25 × 50) = 5.000/1.250 = <b>{br(tau_a,1)} MPa</b>. Na realidade, a tensão se concentra nas extremidades da sobreposição, onde a junta começa a descolar.")

con("MEC-R68", R, "Centro de cisalhamento",
    "Uma viga de perfil U (canal) recebe uma carga vertical que passa pelo centroide da seção. Nessa situação, a viga",
    "sofre flexão acompanhada de torção, pois o centro de cisalhamento do perfil U fica fora da alma, do lado oposto às abas",
    ["sofre apenas flexão, pois a carga passa pelo centroide",
     "não sofre flexão, apenas torção",
     "sofre apenas esforço normal",
     "tem tensões de cisalhamento nulas"],
    res="O fluxo de cisalhamento nas abas e na alma do U gera um momento em torno do centroide. Só não há torção se a carga passar pelo <b>centro de cisalhamento</b>, que no U fica fora da seção, atrás da alma. Em perfis simétricos (I, tubos), centro de cisalhamento e centroide coincidem.")

num("MEC-R69", R, "Fator de forma da seção retangular",
    "Para uma seção retangular, a razão entre o módulo plástico (Z = bh²/4) e o módulo elástico (W = bh²/6), chamada fator de forma, vale",
    1.5, [1.0, 1.27, 1.7, 2.0], d=2,
    res="Z/W = (bh²/4)/(bh²/6) = <b>1,5</b>. O momento de plastificação total é 50% maior que o do início do escoamento. Para perfis I, o fator é cerca de 1,12 a 1,15; para seção circular maciça, 1,70.")

Mp = 250 * 100 * 200 ** 2 / 4 / 1e6
num("MEC-R70", R, "Momento de plastificação",
    "Uma viga de aço (σ<sub>e</sub> = 250 MPa) tem seção retangular de 100 mm × 200 mm (largura × altura). O momento de plastificação total da seção, em kN·m, é",
    Mp, [Mp / 1.5, Mp * 2, Mp / 3, 50], d=0,
    res=f"Z = bh²/4 = 100 × 200²/4 = 10⁶ mm³. M<sub>p</sub> = σ<sub>e</sub>·Z = 250 × 10⁶ N·mm = <b>{br(Mp,0)} kN·m</b>. O momento de início do escoamento é σ<sub>e</sub>·W = 167 kN·m.")

s = 200000 * 500e-6
num("MEC-R71", R, "Tensão a partir de extensômetro",
    "Um extensômetro colado na superfície de uma barra de aço (E = 200 GPa), sob tração uniaxial, indica 500 µε (microdeformações). A tensão na barra, em MPa, é",
    s, [10, 1000, 400, 50], d=0,
    res=f"σ = E·ε = 200.000 MPa × 500 × 10<sup>−6</sup> = <b>{br(s,0)} MPa</b>. 1 µε = 10<sup>−6</sup> m/m. Em estados biaxiais, é preciso uma roseta e a lei de Hooke generalizada.")

con("MEC-R72", R, "Tensões de contato de Hertz",
    "No contato entre um rolo e uma pista (rolamentos, engrenagens, rodas em trilhos), a teoria de Hertz mostra que a tensão de cisalhamento máxima ocorre",
    "um pouco abaixo da superfície, o que explica o início das trincas de fadiga de contato e o descascamento (pitting e spalling)",
    ["exatamente na superfície de contato",
     "no centro do rolo",
     "na face oposta ao contato",
     "em nenhum ponto, pois o contato é de compressão pura"],
    res="A pressão de contato é máxima na superfície, mas a combinação das tensões principais dá o <b>cisalhamento máximo abaixo da superfície</b> (a cerca de 0,8 vez a meia largura de contato). A fadiga de contato começa ali, e as pistas precisam de camada endurecida profunda o bastante.")

con("MEC-R73", R, "Coluna com carga excêntrica",
    "Numa coluna esbelta comprimida com carga levemente excêntrica (fórmula da secante), em comparação com a coluna ideal de Euler,",
    "a deflexão lateral aparece desde o início do carregamento, e o escoamento pode ocorrer com carga menor que a carga crítica de Euler",
    ["a capacidade é sempre maior que a carga de Euler",
     "a excentricidade não altera o comportamento",
     "a coluna só flete depois de atingir a carga crítica",
     "a tensão máxima independe da excentricidade"],
    res="Com excentricidade, o momento P·(e + y) cresce junto com a deflexão: a coluna flete <b>desde o início</b>, e a tensão máxima σ = (P/A)[1 + (ec/r²)·sec(…)] pode atingir o escoamento antes de P<sub>cr</sub>. As normas de projeto consideram essas imperfeições inevitáveis.")

f = 2000 * 2 ** 2 / (2 * 2e6) * 1000
num("MEC-R74", R, "Flecha de balanço com momento na ponta",
    "Uma viga em balanço de 2 m, com rigidez à flexão EI = 2 × 10⁶ N·m², recebe um momento de 2 kN·m na extremidade livre. A flecha na extremidade, em mm, é",
    f, [2 * f, f / 2, 4 * f / 3, 8], d=1,
    res=f"Com momento puro, a curvatura é constante e a elástica é um arco: f = ML²/(2EI) = 2.000 × 4/(2 × 2 × 10⁶) = 0,002 m = <b>{br(f,1)} mm</b>. Uma força na ponta daria PL³/(3EI).")

w = 50 * 9.81 / 1000; Mpp = w * 8 ** 2 / 8
num("MEC-R75", R, "Momento devido ao peso próprio",
    "Uma viga de aço biapoiada de 8 m de vão tem massa de 50 kg/m. Com g = 9,81 m/s², o momento fletor máximo devido apenas ao peso próprio, em kN·m, é, aproximadamente,",
    Mpp, [Mpp * 2, Mpp / 2, 50 * 64 / 8 / 1000, 15.7], d=2,
    res=f"w = 50 × 9,81 = 490,5 N/m = 0,49 kN/m. M = wL²/8 = 0,49 × 64/8 = <b>{br(Mpp,2)} kN·m</b>. Esquecer o g (0,40) trata massa como força. Em vãos grandes, o peso próprio pesa bastante no dimensionamento.")
