# -*- coding: utf-8 -*-
# Banco de questões inéditas – Engenharia Mecânica, estilo Cesgranrio
# Cada questão: (id, materia, assunto, enunciado, [A,B,C,D,E], gabarito 0-4, resolucao)
Q = []
def q(i, mat, ass, en, alts, gab, res): Q.append(dict(id=i, mat=mat, ass=ass, en=en, alts=alts, gab="ABCDE".index(gab), res=res))

T = "Termodinâmica"
q("MEC-T01", T, "Refrigerador de Carnot",
  "Um refrigerador opera segundo o ciclo de Carnot entre um ambiente refrigerado a −13 °C e o ar externo a 39 °C. Para remover 10 kW de calor do ambiente refrigerado, a potência mínima de acionamento, em kW, é",
  ["0,40", "1,67", "2,00", "5,00", "50,0"], "C",
  "Em kelvin: T<sub>L</sub> = 260 K e T<sub>H</sub> = 312 K. O COP de Carnot do refrigerador é T<sub>L</sub>/(T<sub>H</sub> − T<sub>L</sub>) = 260/52 = 5. Logo W = Q<sub>L</sub>/COP = 10/5 = <b>2,0 kW</b>. A alternativa 1,67 kW usa o COP de bomba de calor (T<sub>H</sub>/ΔT = 6), erro comum.")
q("MEC-T02", T, "Máquina térmica de Carnot",
  "Uma máquina térmica recebe 500 kJ de calor de uma fonte a 627 °C e rejeita calor para o ambiente a 27 °C. O máximo trabalho que essa máquina pode produzir, em kJ, é aproximadamente",
  ["333", "375", "417", "479", "500"], "A",
  "Rendimento de Carnot com temperaturas absolutas: η = 1 − 300/900 = 2/3. W<sub>máx</sub> = 2/3 × 500 = <b>333 kJ</b>. Quem usa °C encontra η = 1 − 27/627 ≈ 0,957 e chega a 479 kJ, pegadinha clássica.")
q("MEC-T03", T, "Processo isotérmico de gás ideal",
  "Um quilograma de ar, tratado como gás ideal (R = 0,287 kJ/kg·K), expande-se isotermicamente e de forma reversível a 300 K, até dobrar de volume. Considerando ln 2 ≈ 0,69, o trabalho realizado pelo gás, em kJ, é aproximadamente",
  ["43,1", "59,4", "86,1", "119", "172"], "B",
  "No processo isotérmico reversível de gás ideal, W = mRT·ln(V<sub>2</sub>/V<sub>1</sub>) = 1 × 0,287 × 300 × 0,69 ≈ <b>59,4 kJ</b>. Como a energia interna não varia, o calor recebido é igual ao trabalho.")
q("MEC-T04", T, "Primeira lei em ciclo",
  "Um sistema fechado executa um ciclo composto por dois processos. No processo 1→2, recebe 80 kJ de calor e realiza 30 kJ de trabalho. No processo 2→1, rejeita 60 kJ de calor. No processo 2→1, há",
  ["10 kJ de trabalho realizado pelo sistema", "10 kJ de trabalho realizado sobre o sistema", "20 kJ de trabalho realizado sobre o sistema", "30 kJ de trabalho realizado pelo sistema", "110 kJ de trabalho realizado sobre o sistema"], "B",
  "Processo 1→2: ΔU = Q − W = 80 − 30 = 50 kJ. No ciclo, ΔU<sub>2→1</sub> = −50 kJ. Então −50 = −60 − W<sub>21</sub> → W<sub>21</sub> = −10 kJ: <b>10 kJ realizados sobre o sistema</b>. Conferência: no ciclo, Q<sub>líq</sub> = 20 kJ = W<sub>líq</sub> = 30 − 10.")
q("MEC-T05", T, "Ciclo Rankine",
  "Em relação ao ciclo Rankine simples usado em centrais termelétricas a vapor, é correto afirmar que",
  ["o superaquecimento do vapor reduz o rendimento térmico do ciclo, embora diminua a umidade na saída da turbina.",
   "o reaquecimento tem como principal objetivo reduzir o trabalho consumido pela bomba.",
   "o trabalho consumido pela bomba é da mesma ordem de grandeza do trabalho produzido pela turbina.",
   "a redução da pressão no condensador aumenta o rendimento térmico, mas aumenta o teor de umidade na saída da turbina.",
   "o aumento da pressão na caldeira, mantida a temperatura máxima, reduz o teor de umidade na saída da turbina."], "D",
  "Baixar a pressão do condensador reduz a temperatura média de rejeição de calor e aumenta o rendimento, mas a expansão vai mais fundo na região bifásica e o título cai: <b>mais umidade</b>. O superaquecimento aumenta o rendimento; o reaquecimento serve para limitar a umidade; a bomba consome muito pouco (líquido quase incompressível); e subir a pressão da caldeira com a mesma T<sub>máx</sub> aumenta a umidade.")
q("MEC-T06", T, "Entropia de sólido",
  "Um bloco de cobre de 2 kg (calor específico 0,4 kJ/kg·K) é aquecido de 300 K a 600 K. Considerando ln 2 ≈ 0,69, a variação de entropia do bloco, em kJ/K, é aproximadamente",
  ["0,276", "0,552", "0,800", "1,104", "240"], "B",
  "Para sólido ou líquido incompressível: ΔS = m·c·ln(T<sub>2</sub>/T<sub>1</sub>) = 2 × 0,4 × ln 2 = 0,8 × 0,69 ≈ <b>0,552 kJ/K</b>. O valor 240 é o calor (m·c·ΔT), não a entropia.")
q("MEC-T07", T, "Compressão isentrópica",
  "Ar, considerado gás ideal com k = 1,4, entra em um compressor adiabático e reversível a 300 K e é comprimido com razão de pressões igual a 8. Considerando 8<sup>(0,4/1,4)</sup> ≈ 1,81, a temperatura de saída, em K, é aproximadamente",
  ["371", "450", "543", "600", "2.400"], "C",
  "Processo isentrópico de gás ideal: T<sub>2</sub> = T<sub>1</sub>·(P<sub>2</sub>/P<sub>1</sub>)<sup>(k−1)/k</sup> = 300 × 1,81 ≈ <b>543 K</b>. O valor 2.400 K vem de multiplicar pela razão de pressões, como se fosse T proporcional a P.")
q("MEC-T08", T, "Ciclo Otto",
  "Um motor de ignição por centelha é modelado pelo ciclo Otto padrão a ar, com razão de compressão 8 e k = 1,4. Considerando 8<sup>0,4</sup> ≈ 2,30, o rendimento térmico do ciclo é aproximadamente",
  ["35%", "44%", "50%", "57%", "88%"], "D",
  "η<sub>Otto</sub> = 1 − 1/r<sup>k−1</sup> = 1 − 1/2,30 ≈ 0,565, ou seja, <b>≈ 57%</b>. 88% corresponde a 1 − 1/r, sem o expoente.")
q("MEC-T09", T, "Bocal adiabático",
  "Ar entra em um bocal adiabático a 500 K, com velocidade desprezível, e sai a 450 K. Considerando c<sub>p</sub> = 1,0 kJ/kg·K e √10 ≈ 3,16, a velocidade de saída, em m/s, é aproximadamente",
  ["100", "158", "224", "250", "316"], "E",
  "Balanço de energia em regime permanente, sem calor e sem trabalho: h<sub>1</sub> = h<sub>2</sub> + V<sub>2</sub>²/2 → V<sub>2</sub> = √(2·c<sub>p</sub>·ΔT) = √(2 × 1.000 × 50) = √100.000 ≈ <b>316 m/s</b>. Atenção: c<sub>p</sub> deve estar em J/kg·K.")
q("MEC-T10", T, "Refrigeração por compressão de vapor",
  "No ciclo ideal de refrigeração por compressão de vapor, o processo que ocorre no dispositivo de expansão (válvula ou tubo capilar) é",
  ["isentálpico.", "isentrópico.", "isobárico.", "isotérmico.", "isocórico."], "A",
  "A válvula de expansão é um estrangulamento: sem trabalho, sem calor e com variação desprezível de energia cinética, logo h<sub>entrada</sub> = h<sub>saída</sub>: processo <b>isentálpico</b> e irreversível, portanto não isentrópico.")

F = "Mecânica dos Fluidos"
q("MEC-F01", F, "Bernoulli e continuidade",
  "Água (ρ = 1.000 kg/m³) escoa em regime permanente por uma tubulação horizontal que se reduz de 100 mm para 50 mm de diâmetro. A velocidade no trecho de 100 mm é 1 m/s. Desprezando as perdas, a queda de pressão entre os dois trechos, em kPa, é",
  ["1,5", "3,0", "7,5", "15,0", "30,0"], "C",
  "Continuidade: com o diâmetro pela metade, a área cai 4 vezes e v<sub>2</sub> = 4 m/s. Bernoulli: Δp = ρ(v<sub>2</sub>² − v<sub>1</sub>²)/2 = 1.000 × (16 − 1)/2 = 7.500 Pa = <b>7,5 kPa</b>.")
q("MEC-F02", F, "Darcy-Weisbach",
  "Uma tubulação de 200 m de comprimento e 100 mm de diâmetro interno transporta água a 2 m/s. Adotando fator de atrito de Darcy f = 0,02 e g = 10 m/s², a perda de carga distribuída, em metros de coluna de água, é",
  ["4,0", "8,0", "16,0", "40,0", "80,0"], "B",
  "h<sub>f</sub> = f·(L/D)·v²/(2g) = 0,02 × (200/0,1) × 4/20 = 0,02 × 2.000 × 0,2 = <b>8,0 m</b>. Esquecer o 2 de 2g leva a 16 m. <a href=\"/2026/11/blog-post_26.html\">Calcule outros casos na calculadora de perda de carga</a>.")
q("MEC-F03", F, "Escoamento laminar",
  "Água com viscosidade cinemática 1,0 × 10<sup>−6</sup> m²/s escoa a 0,04 m/s em um tubo de 50 mm de diâmetro. O fator de atrito de Darcy desse escoamento é",
  ["0,016", "0,020", "0,025", "0,032", "0,064"], "D",
  "Re = vD/ν = 0,04 × 0,05/10<sup>−6</sup> = 2.000: escoamento laminar. Nesse caso, f = 64/Re = <b>0,032</b>. O valor 0,016 é o fator de Fanning (16/Re), que é 4 vezes menor que o de Darcy.")
q("MEC-F04", F, "Hidrostática com dois líquidos",
  "Um tanque aberto contém uma camada de 3 m de água (ρ = 1.000 kg/m³) sob uma camada de 2 m de óleo (ρ = 800 kg/m³). Com g = 10 m/s², a pressão manométrica no fundo do tanque, em kPa, é",
  ["40", "46", "50", "60", "80"], "B",
  "Some as colunas: p = ρ<sub>óleo</sub>·g·h<sub>óleo</sub> + ρ<sub>água</sub>·g·h<sub>água</sub> = 800 × 10 × 2 + 1.000 × 10 × 3 = 16.000 + 30.000 = <b>46 kPa</b>. 50 kPa considera 5 m só de água e 40 kPa, 5 m só de óleo.")
q("MEC-F05", F, "Empuxo",
  "Um bloco maciço de 0,5 m³, feito de material com massa específica 600 kg/m³, flutua em água (1.000 kg/m³). O volume do bloco que fica acima da superfície, em m³, é",
  ["0,10", "0,20", "0,25", "0,30", "0,40"], "B",
  "Equilíbrio: peso = empuxo → 600 × 0,5 = 1.000 × V<sub>sub</sub> → V<sub>sub</sub> = 0,30 m³. O volume emerso é 0,5 − 0,3 = <b>0,20 m³</b>. Quem marca 0,30 respondeu o volume submerso.")
q("MEC-F06", F, "Força em superfície plana submersa",
  "Uma comporta retangular vertical, com 2 m de largura e 3 m de altura, tem a aresta superior na superfície livre da água (ρ = 1.000 kg/m³, g = 10 m/s²). A força resultante da água sobre a comporta e a profundidade do centro de pressão são, respectivamente,",
  ["90 kN e 1,5 m", "45 kN e 2,0 m", "180 kN e 2,0 m", "90 kN e 1,0 m", "90 kN e 2,0 m"], "E",
  "F = ρ·g·h<sub>CG</sub>·A = 1.000 × 10 × 1,5 × 6 = <b>90 kN</b>. Para retângulo com topo na superfície, o centro de pressão fica a 2/3 da altura: y<sub>CP</sub> = h<sub>CG</sub> + I/(h<sub>CG</sub>·A) = 1,5 + (2 × 3³/12)/(1,5 × 6) = 1,5 + 0,5 = <b>2,0 m</b>.")
q("MEC-F07", F, "Quantidade de movimento",
  "Um jato de água (ρ = 1.000 kg/m³) com vazão de 0,02 m³/s e velocidade de 20 m/s incide perpendicularmente sobre uma placa plana fixa e é defletido em 90°, espalhando-se paralelamente à placa. A força exercida pelo jato sobre a placa, em N, é",
  ["200", "400", "800", "4.000", "8.000"], "B",
  "Na direção do jato, toda a quantidade de movimento é anulada: F = ρ·Q·V = 1.000 × 0,02 × 20 = <b>400 N</b>. Se a placa fizesse o jato voltar (deflexão de 180°), a força dobraria para 800 N.")
q("MEC-F08", F, "Semelhança de Froude",
  "Um modelo de vertedouro é construído na escala geométrica 1:25 e ensaiado segundo a semelhança de Froude. Se a vazão medida no modelo é 0,02 m³/s, a vazão correspondente no protótipo, em m³/s, é",
  ["0,5", "12,5", "62,5", "312,5", "1.250"], "C",
  "Com Froude igual, a escala de velocidades é √25 = 5 e a de vazões é L<sup>2,5</sup> = 25² × 5 = 3.125. Q<sub>p</sub> = 0,02 × 3.125 = <b>62,5 m³/s</b>.")
q("MEC-F09", F, "Hagen-Poiseuille",
  "Em escoamento laminar plenamente desenvolvido em um tubo circular, mantidas a vazão, o comprimento e o fluido, se o diâmetro interno dobrar, a perda de carga",
  ["cairá à metade.", "cairá a 1/4.", "cairá a 1/8.", "cairá a 1/16.", "cairá a 1/32."], "D",
  "Pela equação de Hagen-Poiseuille, Δp = 128μLQ/(πD<sup>4</sup>). Com Q constante, Δp ∝ 1/D<sup>4</sup>: dobrar D divide a perda por 2<sup>4</sup> = <b>16</b>.")
q("MEC-F10", F, "Viscosidade",
  "A respeito da viscosidade dos fluidos, é correto afirmar que",
  ["a viscosidade de líquidos e de gases aumenta com a temperatura.",
   "a viscosidade cinemática é o produto da viscosidade dinâmica pela massa específica.",
   "um fluido de Bingham escoa sob qualquer tensão de cisalhamento aplicada, por menor que seja.",
   "no SI, a viscosidade dinâmica é expressa em m²/s.",
   "em um fluido newtoniano, a tensão de cisalhamento é proporcional à taxa de deformação, e a viscosidade dos líquidos diminui quando a temperatura aumenta."], "E",
  "Fluido newtoniano: τ = μ·du/dy. Nos líquidos, a viscosidade <b>cai</b> com a temperatura, porque as forças de coesão enfraquecem; nos gases, ela <b>aumenta</b>, porque a agitação molecular cresce. ν = μ/ρ (divisão, não produto); μ é dada em Pa·s; e o fluido de Bingham só escoa acima da tensão limite de escoamento.")
