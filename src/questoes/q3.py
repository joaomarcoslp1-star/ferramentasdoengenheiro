# -*- coding: utf-8 -*-
from q1 import q, Q

E = "Elementos de Máquinas"
q("MEC-E01", E, "Redutor por engrenagens",
  "Um motor de 10 kW a 1.750 rpm aciona um pinhão de 20 dentes, que engrena com uma coroa de 60 dentes. Desprezando as perdas e considerando π ≈ 3,14, o torque no eixo da coroa, em N·m, é aproximadamente",
  ["18,2", "54,6", "109", "136", "164"], "E",
  "Rotação da coroa: 1.750 × 20/60 ≈ 583 rpm. Torque de entrada: T = P/ω = 10.000/(1.750 × 2π/60) ≈ 54,6 N·m. Sem perdas, o torque se multiplica pela relação 3: <b>≈ 164 N·m</b>. 18,2 N·m é o erro de dividir em vez de multiplicar.")
q("MEC-E02", E, "Transmissão por correia",
  "Uma polia motora de 100 mm de diâmetro gira a 1.750 rpm e aciona, por correia, uma polia movida de 350 mm. Desprezando o deslizamento e considerando π ≈ 3,14, a rotação da polia movida e a velocidade da correia são, respectivamente,",
  ["500 rpm e 9,2 m/s", "500 rpm e 32,1 m/s", "6.125 rpm e 9,2 m/s", "583 rpm e 9,2 m/s", "500 rpm e 2,6 m/s"], "A",
  "n<sub>2</sub> = n<sub>1</sub>·d<sub>1</sub>/d<sub>2</sub> = 1.750 × 100/350 = <b>500 rpm</b>. A velocidade da correia é a mesma nas duas polias: v = π·d·n/60 = 3,14 × 0,1 × 1.750/60 ≈ <b>9,2 m/s</b>.")
q("MEC-E03", E, "Vida de rolamentos",
  "Um rolamento rígido de esferas tem capacidade de carga dinâmica C = 20 kN e opera com carga equivalente P = 4 kN, a 1.000 rpm. A vida nominal L<sub>10</sub>, em horas, é aproximadamente",
  ["347", "833", "2.083", "4.167", "125.000"], "C",
  "Para rolamentos de esferas, L<sub>10</sub> = (C/P)³ = 5³ = 125 milhões de rotações. Em horas: 125 × 10<sup>6</sup>/(60 × 1.000) ≈ <b>2.083 h</b>. Para rolamentos de rolos, o expoente seria 10/3.")
q("MEC-E04", E, "Torque de aperto de parafusos",
  "Um parafuso M12 deve ser apertado para gerar uma força de pré-carga de 20 kN. Adotando coeficiente de torque K = 0,2, o torque de aperto, em N·m, é",
  ["24", "48", "96", "240", "480"], "B",
  "T = K·F·d = 0,2 × 20.000 × 0,012 = <b>48 N·m</b>. Erros comuns: usar d em mm sem converter (×1.000) ou o raio no lugar do diâmetro (24 N·m).")
q("MEC-E05", E, "Chavetas",
  "Uma chaveta paralela de 14 mm de largura e 40 mm de comprimento transmite torque de 500 N·m em um eixo de 50 mm de diâmetro. A tensão de cisalhamento média na chaveta, em MPa, é aproximadamente",
  ["8,9", "17,9", "25,0", "35,7", "71,4"], "D",
  "Força tangencial na interface: F = T/(d/2) = 500/0,025 = 20 kN. Área cisalhada: b·L = 14 × 40 = 560 mm². τ = 20.000/560 ≈ <b>35,7 MPa</b>. Usar d em vez de d/2 dá 17,9 MPa.")
q("MEC-E06", E, "Molas helicoidais",
  "A rigidez de uma mola helicoidal de compressão é dada por k = G·d<sup>4</sup>/(8·D³·n). Mantidos o material e o número de espiras ativas, se o diâmetro do arame (d) e o diâmetro médio da espiral (D) forem ambos dobrados, a rigidez",
  ["cairá à metade.", "não se alterará.", "dobrará.", "ficará 4 vezes maior.", "ficará 16 vezes maior."], "C",
  "k ∝ d<sup>4</sup>/D³ = 2<sup>4</sup>/2³ = 16/8 = <b>2</b>: a rigidez dobra. O índice de mola C = D/d não muda, então a forma relativa da mola é a mesma.")
q("MEC-E07", E, "Embreagem de disco",
  "Uma embreagem de disco com duas superfícies de atrito tem raio externo de 100 mm e raio interno de 60 mm, coeficiente de atrito 0,3 e força axial de 5 kN. Pela hipótese de desgaste uniforme, o torque transmissível, em N·m, é",
  ["60", "96", "120", "150", "240"], "E",
  "Desgaste uniforme: raio médio r<sub>m</sub> = (r<sub>e</sub> + r<sub>i</sub>)/2 = 80 mm. T = μ·F·r<sub>m</sub>·N = 0,3 × 5.000 × 0,08 × 2 = <b>240 N·m</b>. Esquecer as duas faces leva a 120 N·m.")
q("MEC-E08", E, "Engrenagens helicoidais",
  "Comparadas às engrenagens cilíndricas de dentes retos de mesmas dimensões, as engrenagens helicoidais",
  ["operam com menos ruído e maior capacidade de carga, mas geram força axial nos mancais.",
   "não geram força axial, por isso dispensam rolamentos de escora.",
   "só podem ser usadas entre eixos que se cruzam a 90°.",
   "têm menor razão de contato, por isso são mais ruidosas.",
   "transmitem potência com relação de transmissão variável."], "A",
  "Nos dentes inclinados, o engrenamento é gradual e há mais dentes em contato (maior razão de contato), então a operação é <b>mais silenciosa</b> e a capacidade de carga é maior. O preço é a <b>força axial</b>, que exige mancais que a suportem, ou o uso de engrenagens espinha-de-peixe (helicoidal dupla).")

M = "Materiais e Tratamentos Térmicos"
q("MEC-M01", M, "Têmpera e revenimento",
  "Sobre os tratamentos térmicos de aços, é correto afirmar que",
  ["o recozimento pleno tem como objetivo principal aumentar a dureza do aço.",
   "na normalização, o resfriamento é feito lentamente dentro do forno desligado.",
   "a têmpera forma martensita, fase dura e frágil, e o revenimento posterior reduz a fragilidade com alguma perda de dureza.",
   "a martensita se forma por difusão do carbono durante o resfriamento lento.",
   "aços com teor de carbono muito baixo (menos de 0,1%) atingem dureza elevada na têmpera."], "C",
  "A têmpera resfria rápido a partir da austenita e forma <b>martensita</b>, por transformação adifusional (por cisalhamento), dura e frágil. O <b>revenimento</b> alivia tensões e aumenta a tenacidade. O recozimento amacia; a normalização resfria <b>ao ar</b>; e sem carbono suficiente a martensita é pouco dura.")
q("MEC-M02", M, "Diagrama ferro-carbono",
  "Um aço com 0,4% de carbono, resfriado lentamente a partir do campo austenítico até a temperatura ambiente, apresentará microestrutura composta por",
  ["apenas perlita.", "cementita proeutetoide e perlita.", "martensita e austenita retida.", "ferrita proeutetoide e perlita.", "austenita e ferrita."], "D",
  "O aço é <b>hipoeutetoide</b> (C &lt; 0,76%). No resfriamento lento, forma-se primeiro a ferrita proeutetoide entre as linhas A<sub>3</sub> e A<sub>1</sub>, e a austenita restante vira perlita a 727 °C. Resultado: <b>ferrita + perlita</b>. A cementita proeutetoide aparece nos hipereutetoides.")
q("MEC-M03", M, "Regra da alavanca",
  "Usando a regra da alavanca no diagrama Fe-Fe<sub>3</sub>C, com ponto eutetoide em 0,76% C e solubilidade de C na ferrita de 0,02%, a fração aproximada de perlita em um aço com 0,40% C, resfriado lentamente, é",
  ["40%", "51%", "53%", "60%", "76%"], "B",
  "Logo acima de 727 °C: fração de austenita (futura perlita) = (0,40 − 0,02)/(0,76 − 0,02) = 0,38/0,74 ≈ <b>51%</b>. Estimar 0,40/0,76 ignora a solubilidade na ferrita e dá 53%.")
q("MEC-M04", M, "Ensaio de tração",
  "A respeito do ensaio de tração de metais, é correto afirmar que",
  ["o limite de resistência é a tensão no instante da fratura.",
   "o módulo de elasticidade de um aço aumenta significativamente com o tratamento térmico de têmpera.",
   "o alongamento percentual mede a dureza do material.",
   "o limite de escoamento convencional é definido pela deformação de 2% (n = 0,02).",
   "a tenacidade pode ser estimada pela área total sob a curva tensão-deformação."], "E",
  "A área sob a curva é a energia absorvida por volume até a fratura: a <b>tenacidade</b>. O limite de resistência é a tensão máxima, não a de fratura; o E dos aços quase não muda com tratamento térmico; o alongamento mede ductilidade; e o escoamento convencional usa 0,2% de deformação.")
q("MEC-M05", M, "Dureza Brinell",
  "Para aços carbono e de baixa liga, uma correlação empírica usual estima o limite de resistência à tração (em MPa) como aproximadamente 3,45 vezes a dureza Brinell. Um aço com 200 HB terá limite de resistência de aproximadamente",
  ["200 MPa", "345 MPa", "500 MPa", "690 MPa", "1.000 MPa"], "D",
  "S<sub>ut</sub> ≈ 3,45 × HB = 3,45 × 200 = <b>690 MPa</b>. Essa correlação é muito usada em inspeção de campo para estimar a resistência sem retirar corpo de prova.")
q("MEC-M06", M, "Corrosão galvânica",
  "Uma tubulação de aço carbono é conectada diretamente a um equipamento de aço inoxidável, em meio aquoso eletrolítico. É correto afirmar que",
  ["o aço carbono atua como ânodo e sua corrosão se agrava quando a área dele é pequena em relação à do inox.",
   "o aço inoxidável atua como ânodo e sofre corrosão acelerada.",
   "não há corrosão galvânica, pois ambos são ligas de ferro.",
   "a corrosão do aço carbono diminui quando sua área é muito menor que a do inox.",
   "a corrosão galvânica independe da presença de eletrólito."], "A",
  "Na série galvânica, o inox passivado é mais nobre, então o <b>aço carbono é o ânodo</b>. A relação ânodo pequeno e cátodo grande concentra a corrente no ânodo e acelera muito a corrosão. Soluções: juntas isolantes, revestir o cátodo ou proteção catódica.")
q("MEC-M07", M, "Estruturas cristalinas",
  "Sobre as estruturas cristalinas dos metais, é correto afirmar que",
  ["o ferro α (ferrita) tem estrutura cúbica de faces centradas (CFC).",
   "o ferro γ (austenita) tem estrutura cúbica de corpo centrado (CCC).",
   "o fator de empacotamento atômico da estrutura CFC (0,74) é maior que o da CCC (0,68).",
   "metais CCC são, em geral, mais dúcteis que os CFC a baixas temperaturas.",
   "a estrutura hexagonal compacta tem mais sistemas de deslizamento que a CFC."], "C",
  "Os fatores de empacotamento são <b>CFC = 0,74</b> (o máximo, junto com a HC) e <b>CCC = 0,68</b>. A ferrita é CCC e a austenita é CFC. Os CFC (Al, Cu, Ni, inox austenítico) são mais dúcteis e não têm transição dúctil-frágil; a HC tem poucos sistemas de deslizamento.")
q("MEC-M08", M, "Transição dúctil-frágil",
  "Em ensaios de impacto Charpy realizados em diferentes temperaturas, observa-se que",
  ["aços inoxidáveis austeníticos apresentam transição dúctil-frágil bem definida.",
   "aços carbono ferríticos apresentam queda acentuada da energia absorvida abaixo da temperatura de transição, o que não ocorre em metais CFC.",
   "a energia absorvida aumenta à medida que a temperatura diminui, em qualquer metal.",
   "o refino de grão eleva a temperatura de transição dúctil-frágil.",
   "a temperatura de transição não tem relevância para vasos de pressão."], "B",
  "Metais <b>CCC</b>, como os aços ferríticos, têm transição dúctil-frágil; os <b>CFC</b>, como o inox austenítico e o alumínio, não. O refino de grão <b>reduz</b> a temperatura de transição. Esse é o critério para escolher material em serviço de baixa temperatura (o naufrágio do Titanic e os navios Liberty são os exemplos clássicos).")
