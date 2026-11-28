# -*- coding: utf-8 -*-
# Lote 2 (28/11/2026): Elementos de Máquinas, Transferência de Calor, Materiais, Máquinas de Fluxo, Vibrações, Fabricação
import math
from nbase import num, con, br

E = "Elementos de Máquinas"
v = 19.05 * 17 * 600 / 60000
num("MEC-E19", E, "Velocidade de corrente de rolos",
    "Uma corrente de rolos de passo 19,05 mm passa por uma roda dentada de 17 dentes que gira a 600 rpm. A velocidade média da corrente, em m/s, é, aproximadamente,",
    v, [v / 17, 2 * v, 60 * v, v * math.pi], d=2,
    res=f"A cada volta, a corrente avança z passos: v = p·z·n/60.000 = 19,05 × 17 × 600/60.000 = <b>{br(v,2)} m/s</b>. Como a corrente se apoia num polígono, a velocidade oscila em torno da média (efeito poligonal), mais quanto menos dentes.")

eta = 10000 * 0.005 / (2 * math.pi * 20)
num("MEC-E20", E, "Rendimento de fuso de potência",
    "Um fuso de rosca trapezoidal com avanço de 5 mm eleva uma carga de 10 kN quando se aplica um torque de 20 N·m. O rendimento do fuso é, aproximadamente,",
    eta, [10000 * 0.005 / 20, 10000 * 0.005 / (math.pi * 20), eta / 2, 0.9], fmt=lambda v: br(100 * v, 0) + "%",
    res=f"Trabalho útil por volta: F·l = 10.000 × 0,005 = 50 J. Trabalho fornecido por volta: 2π·T = 125,7 J. η = 50/125,7 = <b>{br(100*eta,0)}%</b>. Fusos de rosca trapezoidal costumam ficar entre 30% e 50%; fusos de esferas passam de 90%.")

con("MEC-E21", E, "Autotravamento de roscas",
    "Um fuso de potência é autotravante, isto é, a carga não faz o fuso girar sozinho para baixo, quando",
    "o ângulo de atrito é maior que o ângulo de hélice da rosca, o que implica rendimento menor que 50% na elevação",
    ["o ângulo de hélice é maior que o ângulo de atrito",
     "o rendimento do fuso é maior que 90%",
     "o fuso é de esferas recirculantes",
     "a rosca tem várias entradas e grande avanço"],
    res="Na descida, o torque necessário é proporcional a tg(φ − λ). Se o <b>ângulo de atrito φ supera o de hélice λ</b>, é preciso torque para baixar: a rosca trava sozinha. A consequência é rendimento &lt; 50% na subida. Fusos de esferas e roscas de muitas entradas não travam e precisam de freio.")

da = 2 * (30 + 2)
num("MEC-E22", E, "Diâmetro externo de engrenagem",
    "Uma engrenagem cilíndrica de dentes retos, com dentes normais, tem módulo 2 mm e 30 dentes. O diâmetro externo (de cabeça), em mm, é",
    da, [60, 2 * (30 - 2.5), 30 * 2 * math.pi, 68], d=0,
    res=f"Diâmetro primitivo: d = m·z = 60 mm. Altura da cabeça: 1 módulo. d<sub>a</sub> = d + 2m = m(z + 2) = <b>{br(da,0)} mm</b>. O diâmetro de pé é d − 2,5m = 55 mm.")

con("MEC-E23", E, "Engrenagem intermediária (louca)",
    "Num trem de engrenagens simples, uma engrenagem intermediária (louca) é colocada entre a motora e a movida. Esse elemento",
    "inverte o sentido de rotação da movida sem alterar a relação de transmissão entre motora e movida",
    ["multiplica a relação de transmissão pelo seu número de dentes",
     "reduz a rotação da movida à metade",
     "mantém o sentido de rotação e dobra o torque",
     "só funciona se tiver o mesmo número de dentes da motora"],
    res="Relação: (z<sub>i</sub>/z<sub>1</sub>)·(z<sub>2</sub>/z<sub>i</sub>) = z<sub>2</sub>/z<sub>1</sub>. O número de dentes da intermediária se cancela. Ela serve para <b>inverter o sentido</b> ou cobrir uma distância maior entre centros, sem mudar a relação.")

con("MEC-E24", E, "Lubrificação de rolamentos com graxa ou óleo",
    "Na escolha entre graxa e óleo para lubrificar rolamentos, é correto afirmar que",
    "a graxa é preferida em rotações moderadas pela simplicidade de vedação, enquanto o óleo é usado em altas rotações ou quando é preciso remover calor",
    ["a graxa é sempre superior, pois dissipa mais calor que o óleo",
     "o óleo não pode ser usado em rolamentos, apenas em mancais de deslizamento",
     "a graxa é indicada para rotações muito altas, acima do limite do óleo",
     "a escolha não afeta a temperatura de operação nem a vida do rolamento"],
    res="Cerca de 90% dos rolamentos usam <b>graxa</b>: fica no lugar, veda contra contaminação e dispensa sistema de circulação. O <b>óleo</b> é escolhido quando a rotação passa do limite para graxa, quando o mancal precisa ser refrigerado (circulação) ou quando outro componente já é lubrificado a óleo, como as engrenagens de um redutor.")

U = 0.5 * 50000 * 0.02 ** 2
num("MEC-E25", E, "Energia armazenada em mola",
    "Uma mola helicoidal de compressão, com rigidez de 50 N/mm, é comprimida 20 mm. A energia elástica armazenada, em J, é",
    U, [2 * U, 1000, 1.0, 0.5], d=1,
    res=f"U = ½kx² = 0,5 × 50.000 N/m × 0,02² m² = <b>{br(U,1)} J</b>. Atenção às unidades: 50 N/mm = 50.000 N/m. Esquecer o ½ (área do triângulo força × deflexão) dobra o valor.")

Fb = 8 * 1 / (1 + 3)
num("MEC-E26", E, "Parcela da carga externa no parafuso",
    "Numa junta parafusada pré-tensionada, a rigidez do parafuso é k<sub>b</sub> e a das peças unidas é k<sub>m</sub> = 3k<sub>b</sub>. Uma carga externa de tração de 8 kN é aplicada à junta, sem separá-la. O acréscimo de força no parafuso, em kN, é",
    Fb, [8, 4, 6, 2.67], d=1,
    res=f"Fator de rigidez da junta: C = k<sub>b</sub>/(k<sub>b</sub> + k<sub>m</sub>) = 1/4. O parafuso recebe ΔF<sub>b</sub> = C·P = 0,25 × 8 = <b>{br(Fb,1)} kN</b>; os outros 6 kN aliviam a compressão das peças. Por isso a pré-carga protege o parafuso da fadiga.")

Fp = 3000 / (6 * 0.075)
num("MEC-E27", E, "Acoplamento de flanges parafusado",
    "Um acoplamento de flanges transmite 3 kN·m por meio de 6 parafusos dispostos numa circunferência de 150 mm de diâmetro, trabalhando ao cisalhamento. A força cortante em cada parafuso, em N, é, aproximadamente,",
    Fp, [Fp / 2, 3000 / 0.075, 3000 / 6, 2 * Fp], d=0,
    res=f"T = n·F·r → F = T/(n·r) = 3.000/(6 × 0,075) = <b>{br(Fp,0)} N</b>. Usar o diâmetro do círculo de furação (0,15 m) no lugar do raio dá a metade.")

Tb = 2 * 0.4 * 5000 * 0.1
num("MEC-E28", E, "Torque de freio a disco",
    "Num freio a disco, cada uma das duas pastilhas aperta o disco com força de 5 kN, com coeficiente de atrito 0,4 e raio efetivo de 100 mm. O torque de frenagem total, em N·m, é",
    Tb, [Tb / 2, 2 * Tb, 2000, 100], d=0,
    res=f"Cada face gera F<sub>at</sub> = μN = 0,4 × 5.000 = 2.000 N. Com duas faces: T = 2 × 2.000 × 0,1 = <b>{br(Tb,0)} N·m</b>. Contar só uma face dá metade; é o mesmo raciocínio das embreagens de disco com várias superfícies de atrito.")

C = "Transferência de Calor"
num("MEC-C18", C, "Emissão de corpo negro e temperatura",
    "Se a temperatura absoluta de um corpo negro dobra, o poder emissivo total (energia emitida por unidade de área) fica multiplicado por",
    16, [2, 4, 8, 32], d=0,
    res="Stefan-Boltzmann: E = σT⁴. Dobrar T multiplica E por 2⁴ = <b>16</b>. É por isso que a radiação domina a troca de calor em fornos e chamas e é desprezível perto da temperatura ambiente.")

con("MEC-C19", C, "Ordens de grandeza do coeficiente de convecção",
    "Dentre as situações abaixo, aquela em que se espera o MAIOR coeficiente de transferência de calor por convecção é",
    "condensação de vapor de água sobre tubos",
    ["convecção natural do ar ao redor de uma parede",
     "convecção forçada de ar num duto de ventilação",
     "convecção natural de óleo num tanque",
     "convecção forçada de gases de combustão numa chaminé"],
    res="Ordens de grandeza (W/m²·K): ar em convecção natural, 5 a 25; ar forçado, 25 a 250; líquidos em convecção forçada, 100 a 20.000; <b>ebulição e condensação, 2.500 a 100.000</b>. A mudança de fase transporta muita energia pelo calor latente.")

hr = 4 * 5.67e-8 * 300 ** 3
num("MEC-C20", C, "Coeficiente de radiação linearizado",
    "Para pequenas diferenças de temperatura, a troca de calor por radiação entre uma superfície negra e uma vizinhança grande, ambas perto de 300 K, pode ser escrita como q'' = h<sub>r</sub>·ΔT, com h<sub>r</sub> ≈ 4σT³. Com σ = 5,67 × 10<sup>−8</sup> W/m²·K⁴, h<sub>r</sub> vale, em W/m²·K, aproximadamente,",
    hr, [hr / 4, 5.67e-8 * 300 ** 4 / 100, 2 * hr, 0.6], d=1,
    res=f"h<sub>r</sub> = 4 × 5,67 × 10<sup>−8</sup> × 300³ = 4 × 5,67 × 10<sup>−8</sup> × 2,7 × 10⁷ = <b>{br(hr,1)} W/m²·K</b>. É da mesma ordem da convecção natural do ar: numa parede de casa, radiação e convecção pesam quase igual.")

con("MEC-C21", C, "Trocador em contracorrente",
    "Comparando trocadores de calor de correntes paralelas e de contracorrente com a mesma área e os mesmos fluidos, é correto afirmar que, no de contracorrente,",
    "a temperatura de saída do fluido frio pode superar a de saída do fluido quente, e a média logarítmica das diferenças de temperatura é maior",
    ["a temperatura de saída do fluido frio nunca supera a de saída do fluido quente",
     "a média logarítmica das diferenças de temperatura é sempre menor",
     "a efetividade é sempre menor",
     "não se aplica o método da média logarítmica"],
    res="Em correntes paralelas, as saídas se aproximam de uma temperatura comum, e a saída fria fica sempre abaixo da saída quente. Na <b>contracorrente</b>, a saída fria encontra a entrada quente e pode ultrapassar a saída quente. A ΔT<sub>ml</sub> é maior, e o trocador precisa de menos área para o mesmo calor.")

con("MEC-C22", C, "Quando usar aletas",
    "Num trocador de calor que troca calor entre água (h ≈ 5.000 W/m²·K) e ar (h ≈ 50 W/m²·K) através de tubos metálicos, as aletas devem ser colocadas",
    "do lado do ar, onde o coeficiente de convecção é baixo e domina a resistência térmica",
    ["do lado da água, onde o coeficiente de convecção é maior",
     "dos dois lados igualmente, pois a resistência se divide meio a meio",
     "em nenhum dos lados, pois o metal já conduz bem",
     "do lado da água, para reduzir a perda de carga"],
    res="A maior resistência (1/hA) está no lado do <b>ar</b>. Aumentar a área desse lado é o que reduz a resistência total. É por isso que radiadores de carro, condensadores de ar-condicionado e serpentinas têm aletas do lado do ar.")

num("MEC-C23", C, "Escudo de radiação",
    "Entre duas placas paralelas muito grandes, de mesma emissividade, o fluxo de calor por radiação é 1.000 W/m². Introduz-se entre elas uma placa fina (escudo) com a mesma emissividade nas duas faces. O novo fluxo, em W/m², é",
    500, [1000, 250, 333, 750], d=0,
    res="Cada par de superfícies adiciona a mesma resistência radiativa. Com um escudo de mesma emissividade, passam a ser duas resistências iguais em série: o fluxo cai para <b>metade</b>, 500 W/m². Com N escudos, o fluxo fica 1/(N + 1) do original. Escudos de baixa emissividade reduzem ainda mais.")

con("MEC-C24", C, "Número de Prandtl",
    "O número de Prandtl (Pr = ν/α) compara a difusão de quantidade de movimento com a difusão de calor num fluido. É correto afirmar que",
    "os óleos têm Pr muito maior que 1, com camada limite térmica muito mais fina que a de velocidade",
    ["os metais líquidos têm Pr muito maior que 1",
     "o ar tem Pr muito maior que 100",
     "Pr depende da velocidade do escoamento",
     "a água tem Pr igual a zero"],
    res="Pr é propriedade do fluido, não do escoamento. Gases: Pr ≈ 0,7; água: ≈ 7; <b>óleos: de 100 a 10.000</b> (o calor difunde pouco: a camada térmica é fina); metais líquidos: Pr ≪ 1 (o calor difunde muito mais que o momento).")

q = 10 * math.pi * 0.1 * 10 * 100
num("MEC-C25", C, "Perda de calor em tubo nu",
    "Uma tubulação de vapor não isolada, com 100 mm de diâmetro externo e 10 m de comprimento, tem superfície a 120 °C e está em ar a 20 °C. Com h = 10 W/m²·K (convecção e radiação combinadas), a perda de calor, em W, é, aproximadamente,",
    q, [q / 2, q / 4, 2 * q, 1000], d=0,
    res=f"Área lateral: A = πDL = π × 0,1 × 10 = 3,14 m². q = hAΔT = 10 × 3,14 × 100 = <b>{br(q,0)} W</b>. Em 8.000 h por ano, isso é cerca de 25 MWh de energia perdida: isolar compensa rápido.")

q = 200 * 1e-4 * 100 / 0.5
num("MEC-C26", C, "Condução em barra",
    "Uma barra de alumínio (k = 200 W/m·K) com seção de 1 cm² e 0,5 m de comprimento tem as extremidades mantidas a 120 °C e 20 °C, com a superfície lateral isolada. A taxa de calor conduzida, em W, é",
    q, [400, 2 * q, q / 2, 0.4], d=None,
    res=f"q = kAΔT/L = 200 × 10<sup>−4</sup> × 100/0,5 = <b>{br(q,1)} W</b>. A conversão de área é a armadilha: 1 cm² = 10<sup>−4</sup> m².")

M = "Materiais e Tratamentos Térmicos"
con("MEC-M18", M, "Tratamento subzero",
    "Após a têmpera de aços ferramenta de alto carbono, aplica-se às vezes um tratamento subzero (resfriamento a temperaturas como −80 °C) com o objetivo de",
    "transformar a austenita retida em martensita, aumentando a dureza e a estabilidade dimensional",
    ["aliviar as tensões residuais sem alterar a microestrutura",
     "recristalizar a ferrita encruada",
     "dissolver os carbonetos na austenita",
     "transformar a martensita em perlita fina"],
    res="Em aços com muito carbono e liga, a temperatura de fim da transformação martensítica (M<sub>f</sub>) fica abaixo da ambiente: sobra <b>austenita retida</b>, que pode se transformar depois e mudar as dimensões da peça. O subzero completa a transformação. Em seguida, sempre se faz o revenimento.")

con("MEC-M19", M, "Encruamento",
    "O encruamento (trabalho a frio) de um metal dúctil provoca",
    "aumento do limite de escoamento e da dureza, com redução da ductilidade, por multiplicação e interação das discordâncias",
    ["redução do limite de escoamento e aumento da ductilidade",
     "aumento simultâneo da resistência e da ductilidade",
     "recristalização imediata dos grãos",
     "nenhuma alteração nas propriedades, apenas na forma"],
    res="A deformação plástica a frio <b>multiplica as discordâncias</b>, que se emaranham e dificultam novos deslizamentos: o metal fica mais duro e mais resistente, mas menos dúctil. O recozimento (recristalização) desfaz o encruamento. É o caso dos arames trefilados e chapas laminadas a frio.")

Se = 0.5 * 800
num("MEC-M20", M, "Estimativa do limite de fadiga",
    "Para aços com limite de resistência de até cerca de 1.400 MPa, o limite de fadiga de um corpo de prova polido, em flexão rotativa, pode ser estimado como metade do limite de resistência. Para um aço com σ<sub>r</sub> = 800 MPa, esse limite, em MPa, é",
    Se, [800, 600, 200, 700], d=0,
    res=f"S'<sub>e</sub> ≈ 0,5·σ<sub>r</sub> = 0,5 × 800 = <b>{br(Se,0)} MPa</b>. Na peça real, esse valor é reduzido por fatores de acabamento superficial, tamanho, confiabilidade, temperatura e concentração de tensão (equação de Marin).")

K = 200 * math.sqrt(math.pi * 0.002)
num("MEC-M21", M, "Fator de intensidade de tensão",
    "Uma placa larga com uma trinca de borda de 2 mm está sob tensão de 200 MPa. Com fator geométrico Y = 1 e K = Y·σ·√(πa), o fator de intensidade de tensão, em MPa·√m, é, aproximadamente,",
    K, [200 * math.sqrt(0.002), 200 * math.sqrt(math.pi * 2), 2 * K, K / 2], d=1,
    res=f"K = 1 × 200 × √(π × 0,002) = 200 × 0,0793 = <b>{br(K,1)} MPa·√m</b>. Se K atingir a tenacidade à fratura K<sub>IC</sub> do material, a trinca se propaga de forma instável. O tamanho da trinca entra em metros.")

con("MEC-M22", M, "Molibdênio no aço inoxidável",
    "O aço inoxidável AISI 316 é preferido ao 304 em ambientes com cloretos (água do mar, por exemplo) porque",
    "contém molibdênio, que aumenta a resistência à corrosão por pites e por frestas",
    ["tem mais carbono, que forma carbonetos protetores",
     "é martensítico, e por isso mais duro",
     "não contém cromo, eliminando a sensitização",
     "é ferrítico e magnético, o que repele os cloretos"],
    res="O 316 tem cerca de 2% a 3% de <b>molibdênio</b>, que estabiliza o filme passivo contra o ataque localizado dos cloretos (pites e frestas). Os dois aços são austeníticos (não magnéticos quando recozidos). Para ambientes mais agressivos, usam-se duplex ou superausteníticos, com ainda mais Mo e N.")

con("MEC-M23", M, "Discordâncias e deformação plástica",
    "A deformação plástica dos metais cristalinos, em temperaturas usuais, ocorre principalmente por",
    "movimento de discordâncias em planos e direções de deslizamento, exigindo tensões muito menores que a ruptura simultânea de todas as ligações",
    ["difusão de vacâncias, mesmo à temperatura ambiente",
     "ruptura simultânea de todas as ligações atômicas de um plano",
     "transformação de fase da ferrita em austenita",
     "deslizamento dos contornos de grão sem deformação dos grãos"],
    res="As <b>discordâncias</b> permitem o deslizamento rompendo uma linha de ligações de cada vez. Por isso a resistência real ao cisalhamento é cem a mil vezes menor que a teórica. Todos os mecanismos de endurecimento (solução sólida, encruamento, refino de grão, precipitação) funcionam dificultando o movimento delas.")

con("MEC-M24", M, "Nitretação",
    "Em comparação com a cementação, a nitretação gasosa de aços ligados (com Cr, Mo, Al) tem como característica",
    "ser realizada a temperatura mais baixa (cerca de 500 a 550 °C), sem necessidade de têmpera posterior, com mínima distorção das peças",
    ["exigir têmpera em água logo após o tratamento",
     "ser realizada acima de 900 °C, na região austenítica",
     "produzir camadas mais espessas que a cementação, com núcleo mais duro",
     "ser aplicável apenas a aços de baixo carbono sem elementos de liga"],
    res="Na <b>nitretação</b>, o nitrogênio difunde na ferrita e forma nitretos duros com Cr, Mo, Al e V. Como não há austenitização nem têmpera, a distorção é mínima, ideal para peças acabadas (virabrequins, matrizes). As camadas são finas (décimos de mm) e o processo é longo (dezenas de horas).")

con("MEC-M25", M, "Latões e bronzes",
    "As ligas de cobre conhecidas como latão e bronze são, respectivamente, ligas de cobre com",
    "zinco e estanho",
    ["estanho e zinco",
     "níquel e alumínio",
     "chumbo e ferro",
     "zinco e níquel"],
    res="<b>Latão = Cu + Zn</b> (ex.: latão 70/30, de cartuchos e tubos de trocadores). <b>Bronze = Cu + Sn</b> (bronze fosforoso de molas e mancais); por extensão, chamam-se bronzes outras ligas de cobre, como o bronze-alumínio. Cu + Ni forma os cuproníqueis, usados em água do mar.")

dL = 23e-6 * 2000 * 50
num("MEC-M26", M, "Dilatação térmica linear",
    "Uma barra de alumínio (α = 23 × 10<sup>−6</sup> °C<sup>−1</sup>) de 2 m é aquecida de 20 °C para 70 °C, livre para dilatar. O alongamento, em mm, é",
    dL, [dL / 2, 2 * dL, 23, 0.115], d=2,
    res=f"ΔL = α·L·ΔT = 23 × 10<sup>−6</sup> × 2.000 × 50 = <b>{br(dL,2)} mm</b>. O alumínio dilata cerca do dobro do aço (12 × 10<sup>−6</sup>), o que exige cuidado em montagens mistas.")

con("MEC-M27", M, "Ensaio Jominy",
    "O ensaio Jominy, em que um corpo de prova austenitizado é resfriado por um jato de água em apenas uma das extremidades, é usado para avaliar",
    "a temperabilidade do aço, pela queda de dureza com a distância da extremidade resfriada",
    ["a tenacidade ao impacto em baixa temperatura",
     "a resistência à fadiga",
     "a resistência à corrosão sob tensão",
     "a dureza máxima possível, que depende só do teor de liga"],
    res="Ao longo da barra, a taxa de resfriamento cai com a distância da ponta molhada. A curva dureza × distância mostra a <b>temperabilidade</b>: até que profundidade o aço forma martensita. Elementos de liga (Cr, Mo, Ni, Mn) aumentam a temperabilidade; a dureza máxima depende principalmente do carbono.")

B = "Máquinas de Fluxo"
P2 = 10 * 1.2 ** 3
num("MEC-B18", B, "Lei de afinidade para potência de ventilador",
    "Um ventilador consome 10 kW. Se a rotação aumentar 20%, mantidos o rotor e o sistema, a nova potência, pelas leis de semelhança, em kW, será, aproximadamente,",
    P2, [12, 14.4, 20.7, 10], d=1,
    res=f"P ∝ n³: P<sub>2</sub> = 10 × 1,2³ = 10 × 1,728 = <b>{br(P2,1)} kW</b>. Vazão cresce 20% (∝ n) e pressão 44% (∝ n²). Pela mesma lei, reduzir a rotação 20% com inversor de frequência corta a potência quase pela metade.")

H2 = 20 + 10 * (100 / 50) ** 2
num("MEC-B19", B, "Curva do sistema",
    "Um sistema de bombeamento tem altura estática de 20 m e perdas de carga de 10 m quando a vazão é 50 m³/h. Considerando as perdas proporcionais ao quadrado da vazão, a altura manométrica exigida pelo sistema para 100 m³/h, em m, é",
    H2, [40, 80, 30, 50], d=0,
    res=f"H = H<sub>est</sub> + kQ². Dobrar a vazão multiplica as perdas por 4: 10 × 4 = 40 m. H = 20 + 40 = <b>{br(H2,0)} m</b>. A parcela estática não muda com a vazão: dobrar tudo (60 → 80) ou só as perdas linearmente (40) são os erros.")

ns = 1750 * math.sqrt(0.1) / 11.18
num("MEC-B20", B, "Rotação específica",
    "Uma bomba opera a 1.750 rpm com vazão de 0,1 m³/s e altura de 25 m. Com n<sub>s</sub> = n·√Q/H<sup>3/4</sup> e 25<sup>0,75</sup> ≈ 11,18, a rotação específica (em unidades de rpm, m³/s e m) é, aproximadamente,",
    ns, [1750 * 0.1 / 11.18, 1750 * math.sqrt(0.1) / 25, ns * 2, 156], d=1,
    res=f"n<sub>s</sub> = 1.750 × √0,1/25<sup>0,75</sup> = 1.750 × 0,316/11,18 = <b>{br(ns,1)}</b>. Nessa escala, valores baixos (até ~30) indicam rotores radiais estreitos; médios, rotores radiais largos e mistos; altos (acima de ~150), axiais.")

eta = 850 / (1000 * 9.81 * 1 * 100 / 1000)
num("MEC-B21", B, "Rendimento de turbina hidráulica",
    "Uma turbina hidráulica entrega 850 kW no eixo com vazão de 1 m³/s e queda líquida de 100 m (g = 9,81 m/s²). Seu rendimento é, aproximadamente,",
    eta, [0.85, 0.95, 0.765, 0.981], fmt=lambda v: br(100 * v, 1) + "%",
    res=f"Potência hidráulica disponível: ρgQH = 1.000 × 9,81 × 1 × 100 = 981 kW. η = 850/981 = <b>{br(100*eta,1)}%</b>. Na turbina, a potência do eixo é menor que a hidráulica; na bomba, maior.")

num("MEC-B22", B, "Compressão em estágios com resfriamento intermediário",
    "Um compressor de dois estágios, com resfriamento intermediário perfeito (ar volta à temperatura de aspiração), comprime ar de 100 kPa para 1.600 kPa. Para mínimo trabalho total, a razão de pressões de cada estágio deve ser",
    4, [8, 2, 16, 5.33], d=0,
    res="Trabalho mínimo com estágios iguais: r<sub>estágio</sub> = (r<sub>total</sub>)<sup>1/N</sup> = √16 = <b>4</b>. A pressão intermediária é √(100 × 1.600) = 400 kPa. Dividir a razão total por 2 (8) é o erro: as razões se multiplicam, não se somam.")

pt = 800 + 0.5 * 1.2 * 10 ** 2
num("MEC-B23", B, "Pressão total de ventilador",
    "Na descarga de um ventilador, a pressão estática é 800 Pa e o ar (ρ = 1,2 kg/m³) sai a 10 m/s. A pressão total, em Pa, é",
    pt, [800, 920, 740, 1400], d=0,
    res=f"p<sub>total</sub> = p<sub>estática</sub> + ½ρV² = 800 + 0,5 × 1,2 × 100 = 800 + 60 = <b>{br(pt,0)} Pa</b>. Esquecer o ½ dá 920 Pa. A potência útil do ventilador usa a pressão total.")

con("MEC-B24", B, "Regenerador em turbina a gás",
    "Num ciclo Brayton com regenerador, que pré-aquece o ar comprimido com os gases de exaustão, o ganho de rendimento é",
    "maior com razões de pressão baixas, quando a exaustão da turbina sai bem mais quente que o ar comprimido",
    ["maior com razões de pressão altas, quando a saída do compressor é mais quente que a exaustão",
     "nulo, pois o calor dos gases de escape não pode ser reaproveitado",
     "independente da razão de pressões",
     "obtido à custa de maior trabalho do compressor"],
    res="O regenerador só funciona se T<sub>exaustão</sub> &gt; T<sub>saída do compressor</sub>. Com razão de pressões alta, o ar sai do compressor quente e a turbina descarrega mais fria: o ganho some ou fica negativo. Por isso microturbinas (r ≈ 3 a 5) usam regenerador; turbinas de grande razão usam ciclo combinado.")

P2 = 50 * 1200 / 1000
num("MEC-B25", B, "Efeito da massa específica na potência de bomba",
    "Uma bomba centrífuga que consome 50 kW bombeando água (1.000 kg/m³) passa a bombear salmoura com 1.200 kg/m³, na mesma rotação e no mesmo ponto de vazão, com viscosidade semelhante. A nova potência, em kW, é",
    P2, [50, 72, 41.7, 55], d=0,
    res=f"A altura (em metros de coluna do fluido bombeado) e a vazão dependem só da geometria e da rotação. A pressão gerada (ρgH) e a potência (ρgQH/η) crescem com ρ: P = 50 × 1,2 = <b>{br(P2,0)} kW</b>. O motor precisa ser verificado para a nova carga.")

con("MEC-B26", B, "Tubo de sucção em turbinas de reação",
    "Em turbinas de reação (Francis e Kaplan), o tubo de sucção instalado na saída do rotor tem a função de",
    "recuperar parte da energia cinética da água na saída do rotor, convertendo-a em pressão e permitindo instalar a turbina acima do nível de jusante",
    ["aumentar a velocidade da água antes do rotor",
     "funcionar como injetor, como na turbina Pelton",
     "eliminar totalmente o risco de cavitação",
     "regular a vazão, no lugar do distribuidor"],
    res="O <b>tubo de sucção</b> é um difusor: ao desacelerar a água, ele cria uma depressão na saída do rotor e recupera energia que seria perdida. Ele aumenta a queda aproveitada, mas a depressão aumenta o risco de cavitação, que limita a altura de instalação (coeficiente de Thoma).")

V = "Vibrações"
r = 2; fa = abs(1 / (1 - r ** 2))
num("MEC-V12", V, "Amplificação em vibração forçada sem amortecimento",
    "Um sistema massa-mola sem amortecimento é excitado por uma força harmônica com frequência igual ao dobro da frequência natural. A razão entre a amplitude dinâmica e a deflexão estática produzida pela mesma força é",
    fa, [1.0, 0.5, 3.0, 0.25], d=3,
    res=f"Fator de amplificação: 1/|1 − r²| com r = 2: 1/|1 − 4| = <b>{br(fa,3)}</b>. Acima da ressonância, a massa vibra menos do que se a força fosse estática, e em oposição de fase à força.")

vm = 0.010 * 100
num("MEC-V13", V, "Velocidade máxima em vibração livre",
    "Uma massa presa a uma mola, com frequência natural de 100 rad/s, é deslocada 10 mm da posição de equilíbrio e solta do repouso. Sem amortecimento, a velocidade máxima da massa, em m/s, é",
    vm, [0.1, 10, 100, 0.159], d=2,
    res=f"Na vibração livre, v<sub>máx</sub> = X·ω<sub>n</sub> = 0,010 × 100 = <b>{br(vm,2)} m/s</b>, ao passar pela posição de equilíbrio. Pela energia: ½kX² = ½mv² → v = X√(k/m) = Xω<sub>n</sub>.")

con("MEC-V14", V, "Diagnóstico de desalinhamento",
    "Na análise de vibração de um conjunto motor-bomba, os sinais típicos de desalinhamento entre os eixos são",
    "picos em 1× e 2× a rotação, com componente axial elevada e defasagem de cerca de 180° entre os mancais dos lados do acoplamento",
    ["pico apenas em 1× na direção radial, com fase estável, amplitude crescendo com n²",
     "frequências não síncronas de 3,5× a 5× a rotação",
     "ruído de banda larga em altas frequências",
     "pico na frequência da rede elétrica (60 Hz) que some ao desligar o motor"],
    res="<b>Desalinhamento</b>: 2× marcante, vibração axial alta e fase oposta através do acoplamento. Pico só em 1× radial é desbalanceamento; frequências não síncronas são de rolamentos; banda larga indica cavitação ou atrito; 2× a frequência da rede é de origem elétrica.")

e = 6.3 / (2 * math.pi * 3000 / 60) * 1000
num("MEC-V15", V, "Grau de qualidade de balanceamento",
    "Um rotor deve atender ao grau de balanceamento G 6,3 (e·ω = 6,3 mm/s) e opera a 3.000 rpm. A excentricidade residual admissível do centro de massa, em µm, é, aproximadamente,",
    e, [6.3 / 3000 * 1000, 6.3 / 50 * 1000, 2 * e, e / 2], d=0,
    res=f"ω = 2π × 3.000/60 = 314 rad/s. e = 6,3/314 = 0,020 mm = <b>{br(e,0)} µm</b>. Para um rotor de 100 kg, o desbalanceamento residual admissível é m·e = 100 kg × 20 µm = 2.000 g·mm.")

N = math.log(10) / (2 * math.pi * 0.05)
num("MEC-V16", V, "Decaimento da vibração livre amortecida",
    "Um sistema com razão de amortecimento de 0,05 vibra livremente. Usando δ ≈ 2πζ e ln 10 ≈ 2,30, o número aproximado de ciclos para a amplitude cair a 10% do valor inicial é",
    N, [N / 2, 2 * N, 46, 23], d=1,
    res=f"Em N ciclos, x<sub>0</sub>/x<sub>N</sub> = e<sup>Nδ</sup>. Com δ = 2π × 0,05 = 0,314: N = ln 10/0,314 = <b>{br(N,1)}</b> ciclos. Com ζ = 1%, seriam cerca de 37 ciclos.")

con("MEC-V17", V, "Absorvedor dinâmico de vibrações",
    "Uma máquina que opera em rotação constante vibra muito por estar perto da ressonância. Acopla-se a ela um sistema massa-mola auxiliar (absorvedor dinâmico) sem amortecimento. Para anular a vibração da máquina, o absorvedor deve",
    "ter frequência natural própria igual à frequência de excitação",
    ["ter frequência natural muito maior que a de excitação",
     "ter massa igual à da máquina",
     "ter rigidez nula",
     "ter frequência natural igual à metade da de excitação"],
    res="Sintonizado em <b>√(k<sub>a</sub>/m<sub>a</sub>) = ω<sub>excitação</sub></b>, o absorvedor vibra em oposição e aplica na máquina uma força que cancela a excitação. O efeito colateral: surgem duas novas ressonâncias, uma abaixo e outra acima da frequência de operação, o que exige cuidado na partida e na parada.")

con("MEC-V18", V, "Graus de liberdade e modos",
    "Um sistema formado por duas massas ligadas por molas, que se movem apenas na direção vertical, tem",
    "dois graus de liberdade e, portanto, duas frequências naturais, cada uma com um modo de vibração",
    ["um grau de liberdade e uma frequência natural",
     "dois graus de liberdade e uma única frequência natural",
     "quatro graus de liberdade, pois cada mola acrescenta um",
     "infinitas frequências naturais, como uma viga contínua"],
    res="Cada coordenada independente é um grau de liberdade: <b>2 g.d.l. → 2 frequências naturais</b>. No primeiro modo, as massas se movem em fase; no segundo, em oposição. Sistemas contínuos (vigas, eixos) têm infinitos modos.")

P = "Fabricação e Soldagem"
Fc = 2000 * 0.2 * 2; Pc = Fc * 150 / 60 / 1000
num("MEC-P12", P, "Potência de corte no torneamento",
    "Num torneamento com avanço de 0,2 mm/rot e profundidade de corte de 2 mm, a pressão específica de corte do material é 2.000 N/mm². Com velocidade de corte de 150 m/min, a potência de corte, em kW, é",
    Pc, [Fc * 150 / 1000, Pc * 2, Pc / 2, 0.8], d=1,
    res=f"Força de corte: F<sub>c</sub> = k<sub>c</sub>·f·a<sub>p</sub> = 2.000 × 0,2 × 2 = 800 N. P = F<sub>c</sub>·v<sub>c</sub> = 800 × (150/60) = 2.000 W = <b>{br(Pc,1)} kW</b>. Esquecer de converter m/min em m/s multiplica por 60.")

t = 30 / (0.15 * 800)
num("MEC-P13", P, "Tempo de furação",
    "Um furo de 30 mm de profundidade é feito com broca girando a 800 rpm e avanço de 0,15 mm/rot. Desprezando aproximação e saída da broca, o tempo de corte, em min, é",
    t, [t * 2, t / 2, 4.0, 0.0375], d=2,
    res=f"v<sub>f</sub> = f·n = 0,15 × 800 = 120 mm/min. t = L/v<sub>f</sub> = 30/120 = <b>{br(t,2)} min</b> (15 s). Na prática, soma-se a ponta da broca (cerca de 0,3·D) ao comprimento.")

L2 = 1.0 * 20 / 15
num("MEC-P14", P, "Conservação de volume na laminação",
    "Uma chapa de 20 mm de espessura e 1,0 m de comprimento é laminada a frio para 15 mm, sem alteração apreciável de largura. O comprimento final, em m, é, aproximadamente,",
    L2, [0.75, 1.25, 1.78, 1.5], d=2,
    res=f"Na deformação plástica, o volume se conserva: h<sub>0</sub>·L<sub>0</sub> = h<sub>1</sub>·L<sub>1</sub> → L<sub>1</sub> = 1,0 × 20/15 = <b>{br(L2,2)} m</b>. A redução de espessura é de 25%, mas o alongamento é de 33%.")

con("MEC-P15", P, "Retorno elástico no dobramento",
    "No dobramento de chapas, o retorno elástico (springback) faz o ângulo final ser menor do que o imposto pela ferramenta. Ele é maior em materiais",
    "com maior limite de escoamento e menor módulo de elasticidade, sendo compensado com sobredobra ou calibração",
    ["com menor limite de escoamento e maior módulo de elasticidade",
     "frágeis, que não deformam plasticamente",
     "aquecidos acima da temperatura de recristalização",
     "de qualquer tipo, pois o retorno depende apenas da espessura"],
    res="O retorno vem da parcela elástica da deformação, proporcional a <b>σ<sub>e</sub>/E</b>. Aços de alta resistência e alumínio (E baixo) voltam mais que aço doce. Compensa-se dobrando além do ângulo final, calibrando o raio ou estirando a chapa durante o dobramento.")

con("MEC-P16", P, "Classificação de eletrodos revestidos (AWS)",
    "Na especificação AWS A5.1, o eletrodo revestido E7018 tem",
    "resistência mínima à tração de 70 ksi, uso em todas as posições e revestimento básico de baixo hidrogênio com pó de ferro",
    ["resistência mínima de 7.018 MPa",
     "uso apenas na posição plana e revestimento celulósico",
     "resistência de 70 MPa e revestimento rutílico",
     "diâmetro de 7 mm e comprimento de 18 polegadas"],
    res="E <b>70</b>18: 70 ksi (≈ 480 MPa) de resistência mínima do metal depositado; <b>1</b> = todas as posições; <b>8</b> = revestimento básico, baixo hidrogênio, com pó de ferro. Exige estufa para manter os eletrodos secos e é o padrão para aços estruturais e de vasos.")

con("MEC-P17", P, "Porosidade em soldas",
    "A porosidade em cordões de solda é causada principalmente por",
    "gases aprisionados na solidificação, vindos de umidade, contaminação (óleo, tinta, ferrugem) ou proteção gasosa deficiente",
    ["excesso de penetração da raiz",
     "corrente de soldagem baixa demais para fundir o metal de base",
     "velocidade de soldagem alta demais, que deixa a borda sem preencher",
     "resfriamento lento da junta"],
    res="Os <b>poros</b> são bolhas de gás (hidrogênio, nitrogênio, CO) presas quando o metal solidifica. As causas típicas são eletrodo úmido, superfície suja, vento retirando o gás de proteção e vazão de gás errada. Velocidade alta com corrente alta causa mordedura; corrente baixa causa falta de fusão.")

Fc = 2 * (100 + 50) * 2 * 350 / 1000
num("MEC-P18", P, "Força de corte em estampagem",
    "Deseja-se recortar uma peça retangular de 100 mm × 50 mm numa chapa de 2 mm de espessura, com resistência ao cisalhamento de 350 MPa. A força de corte, em kN, é",
    Fc, [Fc / 2, 100 * 50 * 350 / 1000, 2 * Fc, 70], d=0,
    res=f"A área cortada é o perímetro vezes a espessura: 2 × (100 + 50) × 2 = 600 mm². F = 600 × 350 = 210.000 N = <b>{br(Fc,0)} kN</b>. Usar a área da peça (100 × 50) não tem sentido físico: o corte acontece ao longo do contorno.")

con("MEC-P19", P, "Metalurgia do pó",
    "Na metalurgia do pó, a etapa de sinterização consiste em",
    "aquecer a peça compactada abaixo da temperatura de fusão do constituinte principal, unindo as partículas por difusão",
    ["fundir completamente o pó num molde de areia",
     "compactar o pó a frio, sem aquecimento",
     "pulverizar o metal líquido com jato de gás",
     "usinar a peça para remover a porosidade"],
    res="Sequência: obtenção do pó → mistura → compactação na matriz (peça \"verde\") → <b>sinterização</b> em atmosfera controlada, abaixo da fusão, quando as partículas se soldam por difusão. A porosidade residual permite fazer mancais autolubrificantes impregnados de óleo.")
