# -*- coding: utf-8 -*-
# Lote 5 (28/11/2026): Elementos de Máquinas, Transferência de Calor, Materiais, Máquinas de Fluxo, Vibrações, Fabricação
import math
from nbase import num, con, br

E = "Elementos de Máquinas"
con("MEC-E51", E, "Razão de contato",
    "Em engrenagens cilíndricas, a razão de contato (número médio de pares de dentes em contato) deve ser",
    "maior que 1, e recomenda-se pelo menos 1,2 a 1,4, para que um novo par de dentes engrene antes de o anterior sair do contato",
    ["menor que 1, para reduzir o atrito",
     "exatamente igual a 1, para evitar ruído",
     "igual ao número de dentes do pinhão",
     "nula em engrenagens helicoidais"],
    res="Com razão de contato <b>&gt; 1</b>, sempre há pelo menos um par engrenado e a transmissão é contínua. Valores maiores dividem a carga entre pares e reduzem o ruído. Engrenagens helicoidais somam a razão de contato frontal com a de recobrimento e passam facilmente de 2.")

i = 1 + 80 / 20
num("MEC-E52", E, "Trem epicicloidal",
    "Num trem planetário simples, a engrenagem anelar (80 dentes) está fixa, o sol (20 dentes) é a entrada e o braço porta-satélites é a saída. A relação de redução entre sol e braço é",
    i, [4, 80 / 20 - 1, 1 + 20 / 80, 20], d=2,
    res=f"Com o anel fixo, i = 1 + Z<sub>anel</sub>/Z<sub>sol</sub> = 1 + 80/20 = <b>{br(i,2)}</b>. Esquecer o \"1 +\" (resposta 4) ignora que o braço também gira. É o arranjo mais comum de redutores planetários, compactos e de alta capacidade.")

Ft = 0.3 * 4 * 50
num("MEC-E53", E, "Junta parafusada por atrito",
    "Uma junta de atrito tem 4 parafusos, cada um com pré-carga de 50 kN, unindo duas chapas com coeficiente de atrito 0,3 (uma superfície de deslizamento). A força máxima transmitida sem deslizamento, em kN, é",
    Ft, [Ft / 4, 200, 2 * Ft, 30], d=0,
    res=f"F = μ·n·F<sub>i</sub> = 0,3 × 4 × 50 = <b>{br(Ft,0)} kN</b>. Na junta de atrito, a carga passa pelo atrito entre as chapas, e os parafusos trabalham só à tração. Isso elimina o escorregamento e a fadiga por cisalhamento, por isso é usada em estruturas sob vibração e cargas alternadas.")

num("MEC-E54", E, "Carga equivalente com pouca carga axial",
    "Um rolamento rígido de esferas suporta 5 kN radiais e 0,5 kN axiais. O catálogo indica e = 0,3 e, para F<sub>a</sub>/F<sub>r</sub> ≤ e, X = 1 e Y = 0. A carga dinâmica equivalente, em kN, é",
    5.0, [5.5, 4.5, 5.02, 2.8], d=2,
    res="F<sub>a</sub>/F<sub>r</sub> = 0,5/5 = 0,1 ≤ 0,3. Logo X = 1 e Y = 0: P = F<sub>r</sub> = <b>5,00 kN</b>. Somar a carga axial (5,5) ou fazer a soma vetorial (5,02) não segue o método do catálogo.")

Pf = 0.01 * 10000 * math.pi * 0.1 * 1200 / 60
num("MEC-E55", E, "Potência perdida por atrito em mancal",
    "Um mancal de deslizamento com 100 mm de diâmetro suporta 10 kN e gira a 1.200 rpm, com coeficiente de atrito de 0,01. A potência dissipada por atrito, em W, é, aproximadamente,",
    Pf, [Pf / 2, 2 * Pf, 0.01 * 10000 * 1200, 63], d=0,
    res=f"Força de atrito: 0,01 × 10.000 = 100 N. Velocidade periférica: π × 0,1 × 1.200/60 = 6,28 m/s. P = 100 × 6,28 = <b>{br(Pf,0)} W</b>. Esse calor precisa ser levado pelo óleo, e o aquecimento limita a carga e a rotação do mancal.")

L10 = 2 ** (10 / 3)
num("MEC-E56", E, "Vida nominal de rolamento de rolos",
    "Um rolamento de rolos tem capacidade dinâmica C igual ao dobro da carga equivalente P. Com L<sub>10</sub> = (C/P)<sup>10/3</sup> milhões de revoluções e 2<sup>10/3</sup> ≈ 10,1, a vida nominal é, em milhões de revoluções,",
    L10, [8, 2, 6.67, 20.2], d=1,
    res=f"L<sub>10</sub> = 2<sup>10/3</sup> ≈ <b>{br(L10,1)} milhões de rev</b>. Para esferas, o expoente é 3 (2³ = 8). Dividindo pela rotação, a vida sai em horas.")

con("MEC-E57", E, "Retentor de lábio",
    "O retentor de lábio (anel de vedação radial) usado em eixos rotativos de redutores veda porque",
    "um lábio de elastômero, pressionado por uma mola, toca o eixo com um filme lubrificante muito fino, retendo o óleo e barrando a contaminação",
    ["preenche completamente a folga por interferência metálica",
     "funciona sem contato, por labirinto, com vazamento controlado",
     "é colado ao eixo e gira com ele",
     "dispensa acabamento superficial do eixo"],
    res="No <b>retentor</b>, a mola mantém o lábio apoiado no eixo; o filme de óleo de micrômetros lubrifica o contato. O eixo precisa de dureza e rugosidade adequadas, sem riscos helicoidais, que bombeiam óleo para fora. Labirintos são vedações sem contato.")

mt = 3 / 0.94
num("MEC-E58", E, "Módulo transversal de engrenagem helicoidal",
    "Uma engrenagem helicoidal tem módulo normal de 3 mm e ângulo de hélice de 20° (cos 20° ≈ 0,94). O módulo transversal (no plano de rotação), em mm, é, aproximadamente,",
    mt, [3 * 0.94, 3, 3 / 0.342, 3 * 1.5], d=2,
    res=f"m<sub>t</sub> = m<sub>n</sub>/cos β = 3/0,94 = <b>{br(mt,2)} mm</b>. O diâmetro primitivo é d = m<sub>t</sub>·z. A ferramenta de corte é especificada pelo módulo normal.")

con("MEC-E59", E, "Acoplamento hidráulico",
    "O acoplamento hidráulico (fluido), usado entre motores elétricos e transportadores de correia, tem como principais vantagens",
    "partida suave da carga, proteção contra sobrecarga e amortecimento de choques, com um pequeno escorregamento permanente (2% a 4%)",
    ["transmissão sem nenhum escorregamento",
     "multiplicação do torque, como um conversor de torque",
     "não ter perdas de energia",
     "permitir grandes desalinhamentos angulares"],
    res="O rotor bomba lança o óleo contra o rotor turbina, e o torque passa pelo fluido: o motor parte quase sem carga e o torque cresce aos poucos. O <b>escorregamento</b> gera perda e calor. O conversor de torque, que tem estator, é que multiplica o torque.")

d = math.sqrt(4 * 40000 / (2 * 80) / math.pi)
num("MEC-E60", E, "Diâmetro de pino em cisalhamento duplo",
    "Um pino em cisalhamento duplo deve transmitir 40 kN com tensão de cisalhamento admissível de 80 MPa. O diâmetro mínimo, em mm, é, aproximadamente,",
    d, [d * math.sqrt(2), d / math.sqrt(2), 250 / 10, 15.8], d=1,
    res=f"Área necessária: A = F/(2τ) = 40.000/(2 × 80) = 250 mm² por seção. d = √(4A/π) = √318 = <b>{br(d,1)} mm</b>; adota-se o diâmetro comercial acima (por exemplo, 20 mm). Esquecer o cisalhamento duplo dá 25,2 mm.")

C = "Transferência de Calor"
Tt = 20 + 180 * math.exp(-1)
num("MEC-C44", C, "Resfriamento exponencial (capacitância global)",
    "Uma peça metálica a 200 °C é resfriada num ambiente a 20 °C, valendo o modelo de capacitância global com constante de tempo de 100 s. Com e<sup>−1</sup> ≈ 0,368, a temperatura da peça após 100 s, em °C, é, aproximadamente,",
    Tt, [200 * math.exp(-1), 20 + 180 * (1 - math.exp(-1)), 110, 20], d=0,
    res=f"θ/θ<sub>i</sub> = e<sup>−t/τ</sup> → T = 20 + (200 − 20) × 0,368 = 20 + 66,2 = <b>{br(Tt,0)} °C</b>. Após uma constante de tempo, resta 36,8% da diferença inicial; após 5τ, menos de 1%.")

Pe = 0.9 * 5.67e-8 * 0.5 * 500 ** 4
num("MEC-C45", C, "Potência emitida por radiação",
    "Uma superfície de 0,5 m² a 500 K, com emissividade 0,9, emite radiação térmica. Com σ = 5,67 × 10<sup>−8</sup> W/m²·K⁴ e 500⁴ = 6,25 × 10¹⁰ K⁴, a potência emitida, em W, é, aproximadamente,",
    Pe, [Pe / 0.9, 2 * Pe, Pe / 2, 1.5 * Pe], d=0,
    res=f"E = εσAT⁴ = 0,9 × 5,67 × 10<sup>−8</sup> × 0,5 × 6,25 × 10¹⁰ = <b>{br(Pe,0)} W</b>. É a emissão bruta; a perda líquida desconta a radiação que a superfície recebe da vizinhança.")

con("MEC-C46", C, "Significado do número de Nusselt",
    "Numa camada de fluido entre duas superfícies a temperaturas diferentes, um número de Nusselt igual a 1 indica que",
    "o calor atravessa a camada apenas por condução, sem contribuição de movimento do fluido",
    ["a convecção é infinitamente mais intensa que a condução",
     "o escoamento é turbulento",
     "a radiação domina a troca",
     "o fluido está em ebulição"],
    res="Nu = hL/k compara a troca convectiva com a condução pura na mesma camada. <b>Nu = 1</b>: só condução (fluido parado, como ar entre vidros de janela dupla estreita). Valores grandes indicam que o movimento do fluido intensifica a troca.")

num("MEC-C47", C, "MLDT com diferenças de temperatura iguais",
    "Num trocador contracorrente, o fluido quente entra a 120 °C e sai a 80 °C, e o frio entra a 20 °C e sai a 60 °C. A média logarítmica das diferenças de temperatura, em °C, é",
    60, [40, 50, 30, 100], d=0,
    res="ΔT<sub>1</sub> = 120 − 60 = 60 °C e ΔT<sub>2</sub> = 80 − 20 = 60 °C. Com ΔT<sub>1</sub> = ΔT<sub>2</sub>, a fórmula vira 0/0, e o limite é a própria diferença: <b>ΔT<sub>ml</sub> = 60 °C</b>. Isso acontece em contracorrente quando as capacidades térmicas são iguais.")

con("MEC-C48", C, "Resistência térmica de contato",
    "Ao montar um componente eletrônico num dissipador de alumínio, aplica-se pasta térmica entre as superfícies porque",
    "as superfícies se tocam só em pequenos pontos, e a pasta preenche os vazios de ar (mau condutor), reduzindo a resistência térmica de contato",
    ["a pasta aumenta a emissividade do dissipador",
     "a pasta funciona como isolante elétrico e térmico",
     "a pasta aumenta a área de aletas do dissipador",
     "a pasta reduz o coeficiente de convecção"],
    res="Mesmo superfícies polidas têm rugosidades: o contato real é uma fração pequena da área, e o resto é ar, com k ≈ 0,026 W/m·K. A pasta (k ≈ 1 a 10 W/m·K) troca o ar por um meio condutor e reduz a <b>resistência de contato</b>, às vezes a maior do caminho do calor.")

Qs = 0.6 * 800 * 100 / 1000
num("MEC-C49", C, "Radiação solar absorvida",
    "Um telhado de 100 m² recebe irradiação solar de 800 W/m², e sua absortividade solar é 0,6. A potência solar absorvida, em kW, é",
    Qs, [80, 32, 60, 133], d=0,
    res=f"Q = α·G·A = 0,6 × 800 × 100 = 48.000 W = <b>{br(Qs,0)} kW</b>. Uma tinta branca (α ≈ 0,2 a 0,3) reduziria esse ganho à metade ou menos: é o princípio dos telhados frios.")

con("MEC-C50", C, "Biot e Nusselt",
    "Os números de Biot (Bi = hL/k) e de Nusselt (Nu = hL/k) têm a mesma forma, mas diferem porque",
    "no Biot, k é a condutividade do sólido (compara resistência interna com externa); no Nusselt, k é a do fluido (compara convecção com condução no fluido)",
    ["no Biot, k é a do fluido; no Nusselt, a do sólido",
     "o Biot só se aplica a gases",
     "o Nusselt só se aplica à radiação",
     "não há diferença; são o mesmo número"],
    res="<b>Biot</b>: k do sólido. Decide se a temperatura dentro do corpo é uniforme (Bi &lt; 0,1). <b>Nusselt</b>: k do fluido. É o h adimensional, obtido de correlações (Nu = f(Re, Pr) ou f(Ra)). Confundir os dois é pegadinha clássica.")

M = "Materiais e Tratamentos Térmicos"
con("MEC-M44", M, "Fragilização da martensita revenida",
    "Ao revenir certos aços temperados na faixa de cerca de 250 a 400 °C, pode ocorrer queda de tenacidade, fenômeno conhecido como",
    "fragilização da martensita revenida (fragilidade a 350 °C), por isso essa faixa de revenimento costuma ser evitada",
    ["endurecimento por precipitação",
     "recristalização dinâmica",
     "sensitização dos aços inoxidáveis",
     "transição dúctil-frágil por refino de grão"],
    res="Na <b>fragilização da martensita revenida</b>, carbonetos precipitam como filmes nos contornos das ripas de martensita, e a energia de impacto cai. Também existe a fragilidade de revenido (450 a 600 °C, por segregação de impurezas como P e Sb), reversível e agravada por resfriamento lento.")

con("MEC-M45", M, "Aços inoxidáveis duplex",
    "Os aços inoxidáveis duplex (como o 2205) têm microestrutura de",
    "ferrita e austenita em proporções aproximadamente iguais, combinando resistência mecânica cerca do dobro dos austeníticos com boa resistência à corrosão sob tensão",
    ["martensita revenida, com alta dureza",
     "apenas austenita, com níquel acima de 20%",
     "apenas ferrita, sem níquel",
     "perlita e cementita, como os aços-carbono"],
    res="O <b>duplex</b> (≈ 22% Cr, 5% Ni, 3% Mo, N) tem cerca de 50% de ferrita e 50% de austenita. O limite de escoamento passa de 450 MPa (contra ≈ 210 MPa do 316L), e ele resiste muito melhor à corrosão sob tensão por cloretos. É muito usado em offshore, dessalinização e celulose.")

con("MEC-M46", M, "Estágios da fluência",
    "Na curva de fluência (deformação × tempo, sob carga e temperatura constantes), o estágio secundário caracteriza-se por",
    "taxa de deformação aproximadamente constante e mínima, resultado do equilíbrio entre encruamento e recuperação, sendo o parâmetro usado em projeto",
    ["taxa de deformação crescente até a ruptura",
     "deformação elástica instantânea",
     "taxa de deformação decrescente desde o início",
     "ausência total de deformação"],
    res="<b>Primário</b>: taxa decrescente (domina o encruamento). <b>Secundário</b>: taxa constante e mínima (encruamento e recuperação em equilíbrio), a mais longa e usada em projeto. <b>Terciário</b>: taxa crescente (vazios, estricção) até a ruptura.")

num("MEC-M47", M, "Átomos por célula unitária CFC",
    "O número de átomos por célula unitária na estrutura cúbica de face centrada (CFC) é",
    4, [1, 2, 6, 14], d=0,
    res="Vértices: 8 × 1/8 = 1. Faces: 6 × 1/2 = 3. Total: <b>4 átomos</b>. CCC tem 2 (8 × 1/8 + 1 no centro) e cúbica simples, 1. Contar 14 é somar os átomos sem dividir os compartilhados.")

HV = 1.854 * 10 / 0.2 ** 2
num("MEC-M48", M, "Cálculo da dureza Vickers",
    "Num ensaio Vickers com carga de 10 kgf, a média das diagonais da impressão é 0,2 mm. Com HV = 1,854·F/d² (F em kgf e d em mm), a dureza é, aproximadamente,",
    HV, [1.854 * 10 / 0.2, HV / 2, 2 * HV, 10 / 0.04], d=0,
    res=f"HV = 1,854 × 10/0,2² = 18,54/0,04 = <b>{br(HV,0)} HV</b>, típico de aço temperado e revenido. Esquecer de elevar a diagonal ao quadrado dá 93.")

con("MEC-M49", M, "Temperatura de transição vítrea",
    "Para polímeros amorfos, a temperatura de transição vítrea (T<sub>g</sub>) é aquela em que o material",
    "passa de um estado rígido e frágil (vítreo) para um estado borrachoso, mais flexível, sem fusão",
    ["funde completamente e vira líquido",
     "cristaliza totalmente",
     "se decompõe quimicamente",
     "atinge a máxima resistência à tração"],
    res="Abaixo de <b>T<sub>g</sub></b>, as cadeias ficam congeladas (vítreo); acima, os segmentos ganham mobilidade (borrachoso). Borrachas são usadas acima da T<sub>g</sub> (≈ −70 °C), e plásticos rígidos como o PS e o PMMA, abaixo (≈ 100 °C). A fusão (T<sub>m</sub>) é dos domínios cristalinos.")

tx = 10 / (7.87 * 100) * 10
num("MEC-M50", M, "Taxa de corrosão uniforme",
    "Uma placa de aço (ρ = 7,87 g/cm³) com 100 cm² de área exposta perde 10 g por corrosão uniforme em um ano. A taxa de corrosão, em mm/ano, é, aproximadamente,",
    tx, [tx / 10, tx * 10, tx * 2, 7.87], d=3,
    res=f"Volume perdido: 10/7,87 = 1,27 cm³. Espessura: 1,27/100 = 0,0127 cm = <b>{br(tx,3)} mm/ano</b>. Em 20 anos, cerca de 2,5 mm: por isso se especifica sobre-espessura de corrosão em vasos e tubulações.")

B = "Máquinas de Fluxo"
Q = 50 / 3600; P = 850 * 9.81 * Q * 40 / 0.7 / 1000
num("MEC-B44", B, "Potência de bomba para óleo",
    "Uma bomba transfere 50 m³/h de óleo (ρ = 850 kg/m³) com altura manométrica de 40 m e rendimento de 70% (g = 9,81 m/s²). A potência no eixo, em kW, é, aproximadamente,",
    P, [P * 0.7 * 0.7, P * 1000 / 850, P * 0.7, 23.8], d=2,
    res=f"P = ρgQH/η = 850 × 9,81 × (50/3.600) × 40/0,7 = <b>{br(P,2)} kW</b>. Usar a densidade da água (7,79 kW) superdimensiona o motor; multiplicar pelo rendimento em vez de dividir dá a potência hidráulica reduzida, que não tem sentido.")

sc = 3600 / 900
num("MEC-B45", B, "Consumo específico de vapor",
    "Uma turbina a vapor tem queda real de entalpia de 900 kJ/kg. Desprezando perdas mecânicas e do gerador, o consumo específico de vapor, em kg por kWh, é",
    sc, [900 / 3600, 3600, 900, 2], d=None,
    res=f"1 kWh = 3.600 kJ. ṁ/Ẇ = 3.600/900 = <b>{br(sc,1)} kg/kWh</b>. Quanto maior a queda de entalpia aproveitada, menos vapor por kWh.")

num("MEC-B46", B, "Vazão real de compressor alternativo",
    "Um compressor alternativo tem deslocamento volumétrico de 2,0 m³/min e eficiência volumétrica de 85%. A vazão real aspirada, nas condições de sucção, em m³/min, é",
    1.7, [2.0, 2.35, 0.3, 1.0], d=2,
    res="Q<sub>real</sub> = η<sub>v</sub> × deslocamento = 0,85 × 2,0 = <b>1,70 m³/min</b>. A eficiência volumétrica cai com a razão de pressões (reexpansão do espaço morto), com vazamentos nas válvulas e com o aquecimento do ar na sucção.")

con("MEC-B47", B, "Parada brusca de bombas",
    "Numa adutora longa com bomba centrífuga, a falta de energia elétrica (parada brusca da bomba) é crítica porque",
    "a vazão cai rapidamente, gerando golpe de aríete com depressão e sobrepressão, e o fluxo pode inverter; por isso se usam válvula de retenção de fechamento rápido, volante de inércia ou tanques de alívio",
    ["a bomba passa a funcionar como compressor",
     "a pressão na adutora fica constante",
     "a bomba entra em cavitação apenas na partida",
     "o motor elétrico sobrecarrega por excesso de vazão"],
    res="Sem o motor, a bomba desacelera em segundos: a queda brusca de vazão gera uma onda de <b>depressão</b> (que pode separar a coluna d'água) seguida de sobrepressão quando a coluna volta. Proteções: retenção rápida, volante, tanques hidropneumáticos (TAU) e válvulas antecipadoras.")

Ean = 10 * 8760 * 0.5
num("MEC-B48", B, "Energia anual de uma hidrelétrica",
    "Uma pequena central hidrelétrica de 10 MW de potência instalada opera com fator de capacidade de 50%. A energia gerada num ano (8.760 h), em MWh, é",
    Ean, [87600, 4380, 8760, 5000], d=0,
    res=f"E = P × horas × FC = 10 × 8.760 × 0,5 = <b>{br(Ean,0)} MWh</b>. O fator de capacidade é a razão entre a energia gerada e a que seria gerada à potência nominal o ano todo.")

con("MEC-B49", B, "Ventiladores, sopradores e compressores",
    "A classificação usual entre ventiladores, sopradores e compressores se baseia principalmente",
    "na razão de compressão (ou elevação de pressão): ventiladores até cerca de 1,1, sopradores até cerca de 1,1 a 2, e compressores acima disso",
    ["no tipo de motor de acionamento",
     "no material das pás",
     "na temperatura do gás aspirado",
     "na vazão, independentemente da pressão"],
    res="Valores aproximados: <b>ventiladores</b>, razão de pressões de até ≈ 1,1 (ar tratado quase como incompressível); <b>sopradores</b>, ≈ 1,1 a 2; <b>compressores</b>, acima disso. A compressibilidade passa a pesar no projeto conforme a razão cresce.")

con("MEC-B50", B, "Critério de definição do NPSH requerido",
    "O NPSH requerido informado na curva do fabricante de uma bomba centrífuga corresponde, normalmente,",
    "ao NPSH disponível em que a altura manométrica cai 3% por causa da cavitação, e por isso se recomenda uma margem acima desse valor",
    ["ao NPSH em que não há nenhuma bolha de vapor no rotor",
     "à pressão atmosférica local em metros",
     "à altura de sucção máxima com a bomba desligada",
     "à pressão de descarga em metros de coluna"],
    res="Pelas normas de ensaio (Hydraulic Institute, ISO 9906), NPSH<sub>r</sub> = NPSH<sub>3</sub>: quando a altura cai <b>3%</b>. Nesse ponto, já existe cavitação desenvolvida; a cavitação incipiente começa bem antes. Por isso se exigem margens (por exemplo, NPSH<sub>d</sub> ≥ 1,1 a 1,5 × NPSH<sub>r</sub>, ou + 0,6 a 1 m).")

V = "Vibrações"
num("MEC-V31", V, "Massa da mola (método de Rayleigh)",
    "Uma massa de 10 kg está presa a uma mola helicoidal com massa de 3 kg. Pelo método de Rayleigh, a massa efetiva do sistema para o cálculo da frequência natural, em kg, é",
    11.0, [13, 10, 11.5, 12], d=1,
    res="A mola não se move por inteiro: sua velocidade varia de zero (no apoio) à da massa (na ponta). A energia cinética equivale a um terço da massa da mola na ponta: m<sub>ef</sub> = 10 + 3/3 = <b>11,0 kg</b>.")

con("MEC-V32", V, "Rotor acima da velocidade crítica",
    "Um rotor flexível, com pequena excentricidade de massa, opera numa rotação bem acima da sua primeira velocidade crítica. Nessa condição, é correto afirmar que",
    "o rotor tende a girar em torno do seu centro de massa (autocentragem), e a deflexão do eixo se aproxima da excentricidade",
    ["a deflexão do eixo cresce indefinidamente com a rotação",
     "o rotor sempre opera em ressonância",
     "a força nos mancais é máxima",
     "o centro de massa se afasta cada vez mais do eixo de rotação"],
    res="No modelo de Jeffcott, abaixo da crítica o centro de massa fica \"para fora\" (em fase); na crítica, a deflexão é limitada só pelo amortecimento; <b>acima</b>, a fase passa de 90° e o rotor gira em torno do centro de massa. Turbinas e compressores rápidos operam assim, atravessando a crítica rapidamente na partida.")

num("MEC-V33", V, "Frequência natural e rigidez",
    "Um sistema massa-mola tem frequência natural de 10 Hz. Se a rigidez da mola for quadruplicada, mantida a massa, a nova frequência natural, em Hz, será",
    20, [40, 10, 14.1, 5], d=1,
    res="f<sub>n</sub> ∝ √(k/m): quadruplicar k multiplica f por √4 = 2 → <b>20 Hz</b>. Enrijecer suportes é a medida típica para afastar uma ressonância para cima da rotação de operação.")

a = 2 * math.pi * 100 * 5 / 1000
num("MEC-V34", V, "Conversão de velocidade em aceleração",
    "Uma vibração senoidal de 100 Hz tem velocidade RMS de 5 mm/s. A aceleração RMS correspondente, em m/s², é, aproximadamente,",
    a, [0.5, 2 * a, a / (2 * math.pi), 31.4], d=2,
    res=f"Para senoide, a = ω·v = 2π × 100 × 0,005 = <b>{br(a,2)} m/s²</b> (≈ 0,32 g). A mesma velocidade em 1.000 Hz daria 31,4 m/s²: em altas frequências, a aceleração cresce muito.")

mc = 2000 / 100
num("MEC-V35", V, "Massa de correção no balanceamento",
    "O desbalanceamento de um rotor foi medido em 2.000 g·mm. A massa de correção a ser colocada num raio de 100 mm, na posição oposta, em gramas, é",
    mc, [200, 2, 10, 40], d=0,
    res=f"U = m·r → m = 2.000/100 = <b>{br(mc,0)} g</b>, a 180° do ponto pesado. Em balanceamento de dois planos, calcula-se uma correção em cada plano.")

P = "Fabricação e Soldagem"
Pm = 6 / 0.8
num("MEC-P34", P, "Potência do motor da máquina-ferramenta",
    "Uma operação de torneamento exige potência de corte de 6 kW. Com rendimento mecânico da transmissão do torno de 80%, a potência mínima do motor, em kW, é",
    Pm, [4.8, 6.0, 9.6, 12.0], d=1,
    res=f"P<sub>motor</sub> = P<sub>corte</sub>/η = 6/0,8 = <b>{br(Pm,1)} kW</b>. Multiplicar pelo rendimento (4,8 kW) inverte o sentido: as perdas na transmissão são somadas, não descontadas.")

num("MEC-P35", P, "Broca para abrir rosca",
    "Para abrir com macho uma rosca métrica grossa M10 × 1,5, o diâmetro de broca usualmente indicado para o furo prévio, em mm, é",
    8.5, [10, 9, 7.5, 8.0], d=1,
    res="Regra prática para roscas métricas: d<sub>broca</sub> ≈ d<sub>nominal</sub> − passo = 10 − 1,5 = <b>8,5 mm</b>. Isso deixa cerca de 75% de altura de filete, bom compromisso entre resistência e esforço no macho.")

con("MEC-P36", P, "Sistema furo-base",
    "No sistema de ajustes ISO furo-base, adotado na maioria das aplicações mecânicas,",
    "o furo tem posição de tolerância H (afastamento inferior nulo), e os diferentes ajustes são obtidos variando a tolerância do eixo",
    ["o eixo tem posição h, e os ajustes são obtidos variando o furo",
     "furo e eixo têm sempre a mesma tolerância",
     "não há folga nem interferência",
     "a tolerância do furo é sempre maior que 1 mm"],
    res="No <b>furo-base</b>, o furo é sempre H (H7, H8…) e se escolhe o eixo (f, g, h, k, n, p…) para obter folga, transição ou interferência. É mais econômico, porque eixos são mais fáceis de usinar e medir com precisão do que furos e exigem menos alargadores e calibradores diferentes.")

con("MEC-P37", P, "Razão limite de estampagem",
    "No embutimento profundo de copos cilíndricos, a razão limite de estampagem (LDR = diâmetro máximo do disco/diâmetro do punção), para aços de estampagem, fica em torno de",
    "2, e copos mais profundos exigem várias etapas de reestampagem com recozimentos intermediários, se necessário",
    ["10, permitindo copos muito profundos numa única operação",
     "1, ou seja, não é possível estampar copos",
     "0,5, pois o disco é menor que o punção",
     "100, independente do material"],
    res="Se o disco for grande demais, a força para \"puxar\" a aba ultrapassa a resistência da parede do copo, que rompe perto do fundo. <b>LDR ≈ 1,8 a 2,2</b> para aços de estampagem; materiais com alta anisotropia normal (r) estampam mais.")

con("MEC-P38", P, "Posições de soldagem",
    "Na qualificação de soldadores para chapas com solda de topo (ASME IX / AWS), a posição 4G corresponde à soldagem",
    "sobrecabeça",
    ["plana",
     "horizontal",
     "vertical",
     "em tubo girando"],
    res="Chapas com junta de topo: <b>1G</b> plana, <b>2G</b> horizontal, <b>3G</b> vertical, <b>4G</b> sobrecabeça. Em tubos, 5G (tubo fixo horizontal) e 6G (tubo fixo a 45°), esta última qualificando para todas as posições. Para soldas de filete, usa-se F no lugar de G.")

con("MEC-P39", P, "Fundição de precisão (cera perdida)",
    "A fundição por cera perdida (microfusão) é indicada para",
    "peças pequenas e complexas, com excelente acabamento e tolerâncias apertadas, inclusive em ligas de alto ponto de fusão, como aços inoxidáveis e superligas",
    ["grandes lingotes de aço em altíssima produção",
     "peças simples em que o acabamento não importa",
     "apenas ligas de baixo ponto de fusão, como estanho",
     "peças ocas de grande porte sem machos"],
    res="Na <b>microfusão</b>, um modelo de cera é revestido com cerâmica, a cera é derretida e o metal é vazado no molde cerâmico (que é quebrado depois). Permite detalhes finos e quase não exige usinagem: palhetas de turbina, próteses, peças de armas e de válvulas.")

vc = math.pi * 0.3 * 1910 / 60
num("MEC-P40", P, "Velocidade periférica de rebolo",
    "Um rebolo de 300 mm de diâmetro gira a 1.910 rpm. Sua velocidade periférica, em m/s, é, aproximadamente,",
    vc, [vc * 60, vc / 2, 2 * vc, 573], d=0,
    res=f"v = πDn/60 = π × 0,3 × 1.910/60 = <b>{br(vc,0)} m/s</b>. Na retificação, a velocidade é dada em m/s (não em m/min, como na usinagem). Cada rebolo tem velocidade máxima marcada, que não pode ser excedida sob risco de estouro.")
