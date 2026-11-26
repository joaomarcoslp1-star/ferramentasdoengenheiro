# -*- coding: utf-8 -*-
from q1 import q, Q

B = "Máquinas de Fluxo"
q("MEC-B01", B, "NPSH e cavitação",
  "Uma bomba centrífuga, instalada 4 m acima do nível de um reservatório aberto, succiona água a 20 °C (pressão de vapor 2,3 kPa, ρg = 9.810 N/m³), com pressão atmosférica de 101,3 kPa e perda de carga de 1,5 m na sucção. O NPSH requerido pela bomba é 5 m. É correto afirmar que",
  ["o NPSH disponível é cerca de 4,6 m, e a bomba cavitará.",
   "o NPSH disponível é cerca de 14,6 m, e a bomba não cavitará.",
   "o NPSH disponível é cerca de 6,1 m, e a bomba não cavitará, pois a perda de carga não afeta o NPSH.",
   "aumentar a rotação da bomba reduz o NPSH requerido e resolve a cavitação.",
   "o NPSH disponível independe da temperatura da água."], "A",
  "NPSH<sub>d</sub> = (p<sub>atm</sub> − p<sub>v</sub>)/(ρg) − z<sub>s</sub> − h<sub>f,s</sub> = 99.000/9.810 − 4 − 1,5 ≈ 10,1 − 5,5 = <b>4,6 m &lt; 5 m</b>: a bomba <b>cavita</b>. Para resolver: baixar a bomba, reduzir as perdas na sucção (diâmetro maior, menos acessórios) ou reduzir a temperatura. Aumentar a rotação piora, porque o NPSH<sub>r</sub> cresce com n².")
q("MEC-B02", B, "Leis de semelhança",
  "Uma bomba centrífuga a 1.750 rpm fornece 100 m³/h com altura manométrica de 40 m, consumindo 15 kW. Se a rotação passar a 3.500 rpm, mantido o rotor, os novos valores de vazão, altura e potência serão, aproximadamente,",
  ["200 m³/h, 80 m e 30 kW", "200 m³/h, 160 m e 60 kW", "200 m³/h, 160 m e 120 kW", "400 m³/h, 160 m e 120 kW", "200 m³/h, 80 m e 60 kW"], "C",
  "Leis de afinidade: Q ∝ n, H ∝ n², P ∝ n³. Com n dobrada: Q = <b>200 m³/h</b>, H = 40 × 4 = <b>160 m</b> e P = 15 × 8 = <b>120 kW</b>.")
q("MEC-B03", B, "Potência de bombeamento",
  "Uma bomba recalca 0,05 m³/s de água (ρ = 1.000 kg/m³) com altura manométrica de 30 m. Com rendimento global de 75% e g = 10 m/s², a potência no eixo, em kW, é",
  ["11,25", "15,0", "20,0", "22,5", "40,0"], "C",
  "Potência hidráulica: ρgQH = 1.000 × 10 × 0,05 × 30 = 15 kW. Potência no eixo = 15/0,75 = <b>20 kW</b>. Multiplicar pelo rendimento em vez de dividir dá 11,25 kW.")
q("MEC-B04", B, "Associação de bombas",
  "Duas bombas centrífugas idênticas são associadas em paralelo para alimentar um sistema com perdas de carga significativas. É correto afirmar que",
  ["a vazão no sistema será exatamente o dobro da vazão de uma bomba operando isolada.",
   "a altura manométrica de operação será a mesma de uma bomba isolada.",
   "a associação em paralelo é indicada quando se precisa dobrar a altura manométrica.",
   "cada bomba passará a fornecer maior vazão do que quando operava isolada.",
   "a vazão total será menor que o dobro da vazão de uma bomba isolada no mesmo sistema."], "E",
  "Em paralelo, as vazões se somam <b>para a mesma altura</b>. Como a curva do sistema sobe com Q², o novo ponto de operação tem altura maior e cada bomba fornece menos que antes, então a vazão total fica <b>menor que o dobro</b>. A associação em série é que soma alturas.")
q("MEC-B05", B, "Ponto de operação",
  "A curva de uma bomba é H = 70 − 0,003·Q² e a curva do sistema é H = 20 + 0,002·Q², com H em metros e Q em m³/h. O ponto de operação é",
  ["50 m³/h e 25 m", "70,7 m³/h e 30 m", "100 m³/h e 30 m", "100 m³/h e 40 m", "141 m³/h e 60 m"], "D",
  "Igualando as curvas: 70 − 0,003Q² = 20 + 0,002Q² → 0,005Q² = 50 → Q² = 10.000 → Q = <b>100 m³/h</b>. H = 20 + 0,002 × 10.000 = <b>40 m</b>. Confira na curva da bomba: 70 − 30 = 40 m.")
q("MEC-B06", B, "Compressão em estágios",
  "Um compressor alternativo de dois estágios, com resfriamento intermediário perfeito, comprime ar de 1 bar para 16 bar. Para minimizar o trabalho total, a pressão intermediária, em bar, deve ser",
  ["4,0", "5,0", "8,0", "8,5", "15,0"], "A",
  "Trabalho mínimo com razões iguais em cada estágio: p<sub>int</sub> = √(p<sub>1</sub>·p<sub>2</sub>) = √16 = <b>4 bar</b>, com razão 4 em cada estágio. A média aritmética (8,5 bar) é a pegadinha.")
q("MEC-B07", B, "Ciclo Brayton",
  "Uma turbina a gás opera segundo o ciclo Brayton ideal, com razão de pressões 10 e k = 1,4. Considerando 10<sup>(0,4/1,4)</sup> ≈ 1,93, o rendimento térmico do ciclo é aproximadamente",
  ["37%", "48%", "52%", "60%", "90%"], "B",
  "η<sub>Brayton</sub> = 1 − 1/r<sub>p</sub><sup>(k−1)/k</sup> = 1 − 1/1,93 ≈ 1 − 0,518 = <b>48%</b>. 52% é o complemento (1/1,93) e 90% é 1 − 1/r<sub>p</sub>.")
q("MEC-B08", B, "Controle de vazão",
  "Ao se fechar parcialmente uma válvula globo instalada na descarga de uma bomba centrífuga, mantida a rotação,",
  ["a curva da bomba se desloca para baixo e a vazão aumenta.",
   "a curva do sistema fica mais íngreme e a vazão aumenta.",
   "a curva da bomba se desloca para cima e a altura manométrica diminui.",
   "a curva do sistema fica mais íngreme, e o ponto de operação se desloca sobre a mesma curva da bomba para menor vazão e maior altura.",
   "o rendimento da bomba aumenta necessariamente."], "D",
  "Estrangular a descarga acrescenta perda de carga: a <b>curva do sistema fica mais íngreme</b>, enquanto a curva da bomba não muda (ela só depende da rotação e do rotor). O ponto de operação desliza para <b>menor Q e maior H</b>. É um controle simples, mas desperdiça energia; o inversor de frequência é mais eficiente.")

V = "Vibrações"
q("MEC-V01", V, "Frequência natural",
  "Um sistema massa-mola tem massa de 10 kg e rigidez de 40 kN/m. Considerando π ≈ 3,14 e √10 ≈ 3,16, a frequência natural não amortecida, em Hz, é aproximadamente",
  ["1,6", "2,0", "6,3", "10,1", "63,2"], "D",
  "ω<sub>n</sub> = √(k/m) = √4.000 = 20√10 ≈ 63,2 rad/s. f<sub>n</sub> = ω<sub>n</sub>/(2π) = 63,2/6,28 ≈ <b>10,1 Hz</b>. Responder 63,2 é confundir rad/s com Hz.")
q("MEC-V02", V, "Molas em série",
  "Uma massa está apoiada sobre uma mola de rigidez k. Se essa mola for substituída por duas molas iguais, de rigidez k cada uma, associadas em série, a nova frequência natural, em relação à original, será multiplicada por aproximadamente",
  ["0,25", "0,50", "0,71", "1,41", "2,00"], "C",
  "Molas em série: k<sub>eq</sub> = k/2. Como f<sub>n</sub> ∝ √k, a frequência fica multiplicada por 1/√2 ≈ <b>0,71</b>. Em paralelo, k<sub>eq</sub> = 2k e o fator seria 1,41.")
q("MEC-V03", V, "Amortecimento crítico",
  "Para o sistema com massa de 10 kg e rigidez de 40 kN/m, considerando √10 ≈ 3,16, o coeficiente de amortecimento crítico, em N·s/m, é aproximadamente",
  ["632", "1.265", "2.530", "20.000", "400.000"], "B",
  "c<sub>c</sub> = 2√(k·m) = 2√(40.000 × 10) = 2√400.000 = 2 × 632,5 ≈ <b>1.265 N·s/m</b>. Ou, de outra forma, c<sub>c</sub> = 2mω<sub>n</sub> = 2 × 10 × 63,2.")
q("MEC-V04", V, "Isolamento de vibrações",
  "Uma máquina rotativa será montada sobre isoladores elásticos para reduzir a força transmitida à fundação. Para que a transmissibilidade seja menor que 1, a razão entre a frequência de excitação e a frequência natural do sistema deve ser",
  ["menor que 1.", "igual a 1.", "menor que √2.", "entre 1 e √2.", "maior que √2."], "E",
  "A transmissibilidade só fica abaixo de 1 para r = ω/ω<sub>n</sub> <b>&gt; √2</b>. Por isso os isoladores são macios: baixam ω<sub>n</sub>. Para r = 1 há ressonância, e abaixo de √2 a força transmitida é amplificada. Nessa região, aumentar o amortecimento piora o isolamento.")

P = "Fabricação e Soldagem"
q("MEC-P01", P, "Processos de soldagem",
  "A respeito dos processos de soldagem a arco elétrico, é correto afirmar que",
  ["no processo TIG (GTAW), o eletrodo de tungstênio é consumível e incorporado à poça de fusão.",
   "o eletrodo revestido (SMAW) não gera escória, dispensando limpeza entre passes.",
   "o arco submerso (SAW) é especialmente indicado para soldagem na posição sobre-cabeça.",
   "o preaquecimento aumenta a velocidade de resfriamento da junta.",
   "a diferença entre MIG e MAG está no gás de proteção: inerte (Ar, He) no MIG e ativo (CO<sub>2</sub> ou misturas com O<sub>2</sub>/CO<sub>2</sub>) no MAG."], "E",
  "<b>MIG</b> usa gás inerte (comum em alumínio e inox) e <b>MAG</b> usa gás ativo (comum no aço carbono). No TIG, o tungstênio <b>não</b> é consumível; o eletrodo revestido gera escória; o arco submerso exige posição plana ou horizontal; e o preaquecimento <b>reduz</b> a velocidade de resfriamento, o que evita martensita e trincas por hidrogênio.")
q("MEC-P02", P, "Usinagem: velocidade de corte",
  "Uma peça de 60 mm de diâmetro será torneada com velocidade de corte de 150 m/min. Considerando π ≈ 3,14, a rotação do eixo-árvore, em rpm, é aproximadamente",
  ["796", "1.250", "1.592", "2.500", "7.958"], "A",
  "V<sub>c</sub> = π·D·n/1.000, com D em mm e V<sub>c</sub> em m/min. n = 1.000 × 150/(3,14 × 60) ≈ <b>796 rpm</b>. Usar o raio no lugar do diâmetro dá 1.592 rpm.")
q("MEC-P03", P, "Carbono equivalente",
  "Um aço estrutural tem 0,20% C e 1,20% Mn, com teores desprezíveis dos demais elementos. Pela fórmula do IIW, CE = C + Mn/6 + (Cr + Mo + V)/5 + (Ni + Cu)/15, o carbono equivalente é",
  ["0,20", "0,30", "0,40", "0,50", "1,40"], "C",
  "CE = 0,20 + 1,20/6 = 0,20 + 0,20 = <b>0,40</b>. Na faixa de 0,40 a 0,45, a soldabilidade começa a exigir cuidados, como preaquecimento e eletrodos de baixo hidrogênio, conforme a espessura e a restrição da junta.")
q("MEC-P04", P, "Trabalho a frio e recristalização",
  "Sobre a conformação mecânica de metais, é correto afirmar que",
  ["o trabalho a frio reduz o limite de escoamento e aumenta a ductilidade.",
   "a temperatura de recristalização é a mesma para todos os metais.",
   "o trabalho a quente provoca encruamento acentuado e dispensa o tratamento térmico posterior.",
   "o trabalho a frio aumenta o limite de escoamento e reduz a ductilidade, e o recozimento de recristalização pode restaurar a ductilidade.",
   "o encruamento é causado pela redução da densidade de discordâncias."], "D",
  "O trabalho a frio <b>encrua</b> o metal: a densidade de discordâncias aumenta, o escoamento e a dureza sobem e a ductilidade cai. O <b>recozimento de recristalização</b> forma grãos novos e restaura a ductilidade. A temperatura de recristalização fica, em geral, entre 0,3 e 0,5 T<sub>fusão</sub> (em K) e depende do metal e do grau de deformação.")
