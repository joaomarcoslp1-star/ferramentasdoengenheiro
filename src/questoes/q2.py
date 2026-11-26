# -*- coding: utf-8 -*-
from q1 import q, Q

C = "Transferência de Calor"
q("MEC-C01", C, "Parede composta",
  "Uma parede de 10 m² é formada por 200 mm de tijolo (k = 0,8 W/m·K) e 50 mm de isolante (k = 0,04 W/m·K), em série. As temperaturas das faces externas são 40 °C e 10 °C. Desprezando a convecção, a taxa de calor através da parede, em W, é",
  ["40", "200", "1.000", "1.200", "1.500"], "B",
  "Resistências por unidade de área: tijolo 0,2/0,8 = 0,25 m²·K/W; isolante 0,05/0,04 = 1,25 m²·K/W; total 1,5 m²·K/W. q = A·ΔT/R″ = 10 × 30/1,5 = <b>200 W</b>. Ignorar o isolante dá 1.200 W: é ele que domina a resistência.")
q("MEC-C02", C, "Raio crítico de isolamento",
  "Um fio elétrico de raio 3 mm será isolado com material de k = 0,05 W/m·K, exposto a ar com coeficiente de convecção h = 10 W/m²·K. É correto afirmar que",
  ["o raio crítico é h/k = 200 m, e qualquer isolamento reduz a perda de calor.",
   "o raio crítico é 2k/h = 10 mm, valor válido para cilindros.",
   "o raio crítico é k/h = 5 mm, e uma camada fina de isolamento aumentará a perda de calor do fio.",
   "o raio crítico é k/h = 5 mm, e qualquer espessura de isolamento reduzirá a perda de calor.",
   "o raio crítico independe da condutividade do isolante."], "C",
  "Para cilindros, r<sub>cr</sub> = k/h = 0,05/10 = 5 mm (2k/h vale para esferas). Como o fio tem 3 mm &lt; r<sub>cr</sub>, isolar até 5 mm <b>aumenta</b> a perda de calor: a área de convecção cresce mais rápido que a resistência de condução. Isso é útil para resfriar cabos elétricos.")
q("MEC-C03", C, "Convecção e radiação combinadas",
  "Uma placa de 0,5 m² a 80 °C troca calor com o ar ambiente a 20 °C. O coeficiente de convecção é 25 W/m²·K, e a radiação pode ser representada por um coeficiente linearizado de 5 W/m²·K. A taxa total de calor perdida pela placa, em W, é",
  ["150", "750", "900", "1.500", "1.800"], "C",
  "Os dois mecanismos atuam em paralelo: q = (h<sub>conv</sub> + h<sub>rad</sub>)·A·ΔT = (25 + 5) × 0,5 × 60 = <b>900 W</b>, sendo 750 W por convecção e 150 W por radiação.")
q("MEC-C04", C, "Radiação de corpo negro",
  "Se a temperatura absoluta de um corpo negro dobrar, o poder emissivo total e o comprimento de onda de máxima emissão passarão, respectivamente, a ser",
  ["2 vezes maior e 2 vezes maior.", "4 vezes maior e a metade.", "8 vezes maior e 1/4.", "16 vezes maior e a metade.", "16 vezes maior e 2 vezes maior."], "D",
  "Stefan-Boltzmann: E = σT<sup>4</sup>, então dobrar T multiplica E por <b>16</b>. Wien: λ<sub>máx</sub>·T = constante, então λ<sub>máx</sub> cai à <b>metade</b>, deslocando a emissão para comprimentos de onda menores.")
q("MEC-C05", C, "Média logarítmica de temperaturas",
  "Em um trocador de calor em contracorrente, o fluido quente entra a 150 °C e sai a 90 °C, e o fluido frio entra a 30 °C e sai a 70 °C. Considerando ln(4/3) ≈ 0,288, a diferença média logarítmica de temperaturas, em °C, é aproximadamente",
  ["60,0", "69,4", "70,0", "75,0", "80,0"], "B",
  "Contracorrente: ΔT<sub>1</sub> = 150 − 70 = 80 °C e ΔT<sub>2</sub> = 90 − 30 = 60 °C. LMTD = (80 − 60)/ln(80/60) = 20/0,288 ≈ <b>69,4 °C</b>. A média aritmética (70 °C) sempre superestima a LMTD.")
q("MEC-C06", C, "Método ε-NTU",
  "Sobre o método da efetividade (ε-NTU) aplicado a trocadores de calor, é correto afirmar que",
  ["a efetividade pode ser maior que 1 em trocadores contracorrente muito longos.",
   "o NTU é a razão entre a capacidade calorífica mínima e o produto UA.",
   "para mesma área e mesmas vazões, o arranjo em paralelo (equicorrente) sempre tem maior efetividade que o contracorrente.",
   "a razão de capacidades C<sub>mín</sub>/C<sub>máx</sub> é igual a 1 quando um dos fluidos muda de fase.",
   "quando um dos fluidos muda de fase, C<sub>mín</sub>/C<sub>máx</sub> = 0 e ε = 1 − exp(−NTU), qualquer que seja a configuração do trocador."], "E",
  "Na mudança de fase, a temperatura do fluido não varia, o que equivale a C → ∞, então C<sub>r</sub> = 0 e todas as configurações caem em <b>ε = 1 − e<sup>−NTU</sup></b>. A efetividade é no máximo 1; NTU = UA/C<sub>mín</sub>; e o contracorrente é o arranjo mais efetivo.")
q("MEC-C07", C, "Capacitância global",
  "Uma pequena esfera metálica de raio 6 mm (ρc = 3,6 × 10<sup>6</sup> J/m³·K, k = 40 W/m·K) é resfriada em um fluido com h = 60 W/m²·K. Validando o modelo de capacitância global, a constante de tempo térmica da esfera, em segundos, é",
  ["30", "60", "120", "360", "1.200"], "C",
  "Comprimento característico L<sub>c</sub> = V/A = r/3 = 2 mm. Bi = h·L<sub>c</sub>/k = 60 × 0,002/40 = 0,003 &lt; 0,1, então o modelo vale. τ = ρc·L<sub>c</sub>/h = 3,6 × 10<sup>6</sup> × 0,002/60 = <b>120 s</b>. Usar L<sub>c</sub> = r leva a 360 s.")
q("MEC-C08", C, "Condução em cilindro",
  "Um tubo com raio interno de 50 mm e raio externo de 100 mm, feito de material com k = 1 W/m·K, tem as superfícies interna e externa a 160 °C e 50 °C. Considerando π ≈ 3,14 e ln 2 ≈ 0,69, a taxa de calor por metro de comprimento, em kW/m, é aproximadamente",
  ["0,50", "1,00", "1,57", "2,00", "6,91"], "B",
  "Resistência de parede cilíndrica: R = ln(r<sub>2</sub>/r<sub>1</sub>)/(2πkL). q = 2π·k·L·ΔT/ln 2 = 6,28 × 1 × 1 × 110/0,69 ≈ 1.001 W ≈ <b>1,0 kW/m</b>.")

R = "Resistência dos Materiais"
q("MEC-R01", R, "Torção em eixo maciço",
  "Um eixo maciço de 40 mm de diâmetro transmite um torque de 500 N·m. Considerando π ≈ 3,14, a máxima tensão de cisalhamento no eixo, em MPa, é aproximadamente",
  ["5", "10", "20", "40", "80"], "D",
  "τ<sub>máx</sub> = T·c/J = 16T/(πd³) = 16 × 500/(3,14 × 0,04³) = 8.000/(2,01 × 10<sup>−4</sup>) ≈ <b>40 MPa</b>. Usar 32 no lugar de 16 (confundir J com d<sup>4</sup>/32 sem dividir pelo raio) dá 80 MPa.")
q("MEC-R02", R, "Flexão simples",
  "Uma viga biapoiada de 4 m de vão, com seção retangular de 100 mm de base e 200 mm de altura, recebe uma carga concentrada de 10 kN no meio do vão. Desprezando o peso próprio, a máxima tensão normal de flexão, em MPa, é",
  ["7,5", "15", "30", "60", "150"], "B",
  "M<sub>máx</sub> = PL/4 = 10 × 4/4 = 10 kN·m. Módulo resistente W = bh²/6 = 0,1 × 0,2²/6 = 6,67 × 10<sup>−4</sup> m³. σ = M/W = <b>15 MPa</b>. Com a viga deitada (b e h trocados), W cai à metade e σ = 30 MPa.")
q("MEC-R03", R, "Tração e alongamento",
  "Uma barra de aço (E = 200 GPa) de 2 m de comprimento e seção de 100 mm² é tracionada por uma força axial de 10 kN. O alongamento da barra, em mm, é",
  ["0,1", "0,5", "1,0", "2,0", "10"], "C",
  "σ = F/A = 10.000/100 = 100 MPa, dentro do regime elástico. δ = FL/(EA) = 10.000 × 2.000 mm/(200.000 MPa × 100 mm²) = <b>1,0 mm</b>.")
q("MEC-R04", R, "Flambagem de Euler",
  "Uma coluna esbelta biarticulada tem carga crítica de flambagem de 100 kN. Se a mesma coluna for engastada na base e livre no topo, a nova carga crítica, em kN, será",
  ["25", "50", "100", "200", "400"], "A",
  "P<sub>cr</sub> = π²EI/(L<sub>e</sub>)². Na coluna engastada-livre, L<sub>e</sub> = 2L, então P<sub>cr</sub> cai 4 vezes: <b>25 kN</b>. Com engaste nas duas extremidades (L<sub>e</sub> = 0,5L), a carga seria 400 kN.")
q("MEC-R05", R, "Círculo de Mohr",
  "Em um ponto de uma peça, o estado plano de tensões é σ<sub>x</sub> = 80 MPa, σ<sub>y</sub> = 20 MPa e τ<sub>xy</sub> = 40 MPa. As tensões principais σ<sub>1</sub> e σ<sub>2</sub> e a máxima tensão de cisalhamento no plano valem, respectivamente, em MPa,",
  ["80, 20 e 40", "90, 10 e 40", "100, 0 e 40", "100, −20 e 60", "100, 0 e 50"], "E",
  "Centro do círculo: (80 + 20)/2 = 50 MPa. Raio: √(30² + 40²) = 50 MPa. Assim, σ<sub>1</sub> = 50 + 50 = <b>100</b>, σ<sub>2</sub> = 50 − 50 = <b>0</b> e τ<sub>máx,plano</sub> = R = <b>50 MPa</b>.")
q("MEC-R06", R, "Vaso de pressão de parede fina",
  "Um vaso cilíndrico de parede fina, com diâmetro de 1 m e espessura de 10 mm, está submetido à pressão interna de 2 MPa. As tensões circunferencial e longitudinal na parede valem, respectivamente, em MPa,",
  ["50 e 100", "100 e 50", "100 e 100", "200 e 100", "25 e 50"], "B",
  "σ<sub>θ</sub> = pD/(2t) = 2 × 1.000/20 = <b>100 MPa</b> e σ<sub>L</sub> = pD/(4t) = <b>50 MPa</b>. Por isso os vasos rompem longitudinalmente e a solda longitudinal é a mais crítica.")
q("MEC-R07", R, "Flecha em viga em balanço",
  "Uma viga em balanço, de seção constante, suporta uma carga uniformemente distribuída. Mantidos o material, a seção e a carga por unidade de comprimento, se o comprimento da viga dobrar, a flecha máxima ficará multiplicada por",
  ["2", "4", "8", "16", "32"], "D",
  "Para balanço com carga distribuída, δ<sub>máx</sub> = wL<sup>4</sup>/(8EI). Com w constante, δ ∝ L<sup>4</sup>: 2<sup>4</sup> = <b>16</b>. Se a carga fosse concentrada na ponta (δ = PL³/3EI), o fator seria 8.")
q("MEC-R08", R, "Momento de inércia",
  "Uma viga de seção retangular de 100 mm × 200 mm pode ser montada com a maior dimensão na vertical (em pé) ou na horizontal (deitada). A razão entre os momentos de inércia em relação ao eixo de flexão horizontal, I<sub>em pé</sub>/I<sub>deitada</sub>, é",
  ["1", "2", "4", "8", "16"], "C",
  "I = bh³/12. Em pé: 100 × 200³/12. Deitada: 200 × 100³/12. A razão é (200/100)² = <b>4</b>. Na rigidez, a viga em pé é 4 vezes melhor; na resistência (W = bh²/6), 2 vezes.")
q("MEC-R09", R, "Critérios de falha",
  "Um ponto de um eixo está submetido a uma tensão normal de 60 MPa e a uma tensão de cisalhamento de 40 MPa. A tensão equivalente segundo o critério de Tresca (máxima tensão de cisalhamento), em MPa, é",
  ["50,0", "72,1", "91,7", "100,0", "140,0"], "D",
  "Tresca: σ<sub>eq</sub> = √(σ² + 4τ²) = √(3.600 + 6.400) = <b>100 MPa</b>, ou seja, 2τ<sub>máx</sub> com τ<sub>máx</sub> = 50 MPa. Von Mises daria √(σ² + 3τ²) ≈ 91,7 MPa: Tresca é sempre igual ou mais conservador.")
q("MEC-R10", R, "Fadiga",
  "Sobre o dimensionamento de componentes mecânicos à fadiga, é correto afirmar que",
  ["tensões médias de compressão reduzem a vida em fadiga tanto quanto as de tração.",
   "aços não apresentam limite de resistência à fadiga, ao contrário das ligas de alumínio.",
   "um acabamento superficial mais rugoso aumenta o limite de resistência à fadiga corrigido.",
   "concentradores de tensão, como entalhes e furos, só são relevantes para carregamento estático.",
   "pelo critério de Goodman modificado, a presença de tensão média de tração reduz a amplitude de tensão admissível."], "E",
  "Goodman: σ<sub>a</sub>/S<sub>e</sub> + σ<sub>m</sub>/S<sub>ut</sub> = 1/n, então quanto maior σ<sub>m</sub> (de tração), <b>menor a amplitude admissível</b>. Tensão média de compressão costuma ser benéfica (é a base do jateamento com granalha, o shot peening). Aços têm limite de fadiga e o alumínio não; rugosidade reduz S<sub>e</sub>; e entalhes são críticos justamente em fadiga.")
