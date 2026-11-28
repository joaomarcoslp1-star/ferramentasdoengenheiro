# -*- coding: utf-8 -*-
# Lote 4 (28/11/2026): Elementos de Máquinas, Transferência de Calor, Materiais, Máquinas de Fluxo, Vibrações, Fabricação
import math
from nbase import num, con, br

E = "Elementos de Máquinas"
num("MEC-E41", E, "Número mínimo de dentes",
    "Para engrenagens cilíndricas de dentes retos com perfil evolvente normal (ângulo de pressão de 20° e altura de cabeça igual ao módulo), geradas por cremalheira, o número mínimo de dentes do pinhão que evita o corte de pé (interferência) é, aproximadamente,",
    17, [12, 14, 20, 32], d=0,
    res="z<sub>mín</sub> = 2/sen²α = 2/0,342² ≈ 17,1 → <b>17 dentes</b> (na prática, 14 com pequeno rebaixamento admitido). Com 14,5° de pressão, seriam 32. Abaixo do mínimo, usam-se dentes corrigidos (deslocamento de perfil).")

p = math.pi * 4
num("MEC-E42", E, "Passo circular",
    "Uma engrenagem tem módulo 4 mm. O passo circular, medido sobre a circunferência primitiva, em mm, é, aproximadamente,",
    p, [4, 2 * p, p / 2, 8], d=2,
    res=f"p = π·m = π × 4 = <b>{br(p,2)} mm</b>. Só engrenagens de mesmo módulo (logo, mesmo passo) e mesmo ângulo de pressão engrenam entre si.")

T2 = 50 * 4 * 0.95
num("MEC-E43", E, "Torque na saída de redutor",
    "Um redutor de engrenagens com relação de redução 4:1 e rendimento de 95% recebe 50 N·m no eixo de entrada. O torque no eixo de saída, em N·m, é",
    T2, [200, 12.5, 50 * 4 / 0.95, 47.5], d=1,
    res=f"Potência de saída = 0,95 × potência de entrada, e a rotação cai 4 vezes: T<sub>2</sub> = T<sub>1</sub>·i·η = 50 × 4 × 0,95 = <b>{br(T2,1)} N·m</b>. Dividir pelo rendimento (210,5) daria mais torque do que a potência permite.")

L = 2 * 500000 / 50 / (4.5 * 100)
num("MEC-E44", E, "Comprimento de chaveta pelo esmagamento",
    "Uma chaveta paralela com altura de 9 mm transmite 500 N·m num eixo de 50 mm. Considerando que metade da altura (4,5 mm) fica no cubo e pressão admissível de esmagamento de 100 MPa, o comprimento mínimo da chaveta, em mm, é, aproximadamente,",
    L, [L / 2, 2 * L, 500000 / 50 / (9 * 100), 100], d=1,
    res=f"Força no raio do eixo: F = T/(d/2) = 500.000/25 = 20.000 N. Área de esmagamento: (h/2)·L. L = 20.000/(4,5 × 100) = <b>{br(L,1)} mm</b>. Usar a altura inteira (9 mm) superestima a área de contato.")

con("MEC-E45", E, "Mancal fixo e mancal livre",
    "Num eixo apoiado em dois rolamentos e sujeito a dilatação térmica, a montagem recomendada é",
    "um rolamento fixo (localizado axialmente), que absorve as cargas axiais, e outro livre, que permite o deslocamento axial causado pela dilatação",
    ["os dois rolamentos fixos axialmente, para maior rigidez",
     "os dois rolamentos livres, para o eixo flutuar",
     "os dois rolamentos com interferência máxima nos anéis externos",
     "um único rolamento no meio do eixo"],
    res="Com dois mancais travados, a dilatação do eixo geraria cargas axiais enormes e anormais nos rolamentos. O arranjo <b>fixo-livre</b> resolve: o livre pode ser um rolamento de rolos cilíndricos (desliza internamente) ou um rígido de esferas com folga axial na caixa.")

T = 4 * 0.3 * 2000 * 0.08
num("MEC-E46", E, "Embreagem de múltiplos discos",
    "Uma embreagem de discos múltiplos tem 4 superfícies de atrito, força axial de 2 kN, coeficiente de atrito de 0,3 e raio médio de 80 mm. O torque transmissível, em N·m, é",
    T, [48, 96, 384, 240], d=0,
    res=f"T = n·μ·F·r<sub>m</sub> = 4 × 0,3 × 2.000 × 0,08 = <b>{br(T,0)} N·m</b>. A mesma força axial atua em todas as superfícies, por isso empilhar discos multiplica o torque sem aumentar o diâmetro.")

con("MEC-E47", E, "Engajamento de rosca em material macio",
    "Um parafuso de aço será roscado diretamente num furo de uma carcaça de alumínio. Para evitar o arrancamento da rosca da carcaça, recomenda-se",
    "aumentar o comprimento de engajamento (cerca de 2 vezes o diâmetro) ou usar insertos helicoidais de aço",
    ["reduzir o comprimento de engajamento para meio diâmetro",
     "usar rosca de passo maior com menos filetes engajados",
     "apertar o parafuso com o dobro do torque",
     "lubrificar com graxa grafitada para aumentar o atrito"],
    res="O alumínio tem resistência ao cisalhamento bem menor que a do parafuso de aço. Para que o parafuso rompa antes da rosca da carcaça, aumenta-se o <b>comprimento engajado</b> (≈ 1,5d a 2d) ou usam-se insertos helicoidais (Heli-Coil). Em aço com aço, ≈ 1d basta.")

con("MEC-E48", E, "Grau de viscosidade ISO",
    "Um óleo lubrificante industrial especificado como ISO VG 68 tem",
    "viscosidade cinemática média de 68 cSt (mm²/s) a 40 °C",
    ["viscosidade de 68 cSt a 100 °C",
     "viscosidade dinâmica de 68 Pa·s a 20 °C",
     "índice de viscosidade igual a 68",
     "ponto de fulgor de 68 °C"],
    res="Na classificação <b>ISO VG</b>, o número é a viscosidade cinemática média a <b>40 °C</b>, em cSt (com faixa de ±10%). ISO VG 68 é muito usado em sistemas hidráulicos e redutores. A viscosidade a 100 °C e o índice de viscosidade são outras propriedades.")

con("MEC-E49", E, "Concentração de tensão em ombro de eixo",
    "Para reduzir a concentração de tensão num ombro de eixo, onde o diâmetro muda bruscamente, a medida mais eficaz é",
    "aumentar o raio de concordância entre os dois diâmetros, usando, se necessário, rebaixo ou anel espaçador para o rolamento assentar",
    ["reduzir o raio de concordância a zero, deixando canto vivo",
     "aumentar a diferença entre os diâmetros",
     "fazer um rasgo de chaveta no ombro",
     "usar um material mais duro, que elimina o K<sub>t</sub>"],
    res="K<sub>t</sub> cresce quando o raio de concordância diminui e quando a razão D/d aumenta. Um <b>raio maior</b> espalha as linhas de força. Quando o rolamento exige canto vivo, usam-se rebaixos ou anéis. O material não muda K<sub>t</sub>; ele só afeta a sensibilidade ao entalhe na fadiga.")

con("MEC-E50", E, "Correia sincronizada",
    "A correia sincronizada (dentada) é preferida à correia em V quando",
    "é necessária relação de transmissão exata, sem deslizamento, como no comando de válvulas de motores",
    ["se deseja que a correia deslize em caso de sobrecarga",
     "a distância entre centros é variável durante a operação",
     "o ambiente é muito quente, acima de 300 °C",
     "se precisa de alto amortecimento de choques por deslizamento"],
    res="A correia <b>sincronizada</b> engrena nas polias dentadas e mantém a relação exata, como uma corrente, mas sem lubrificação e com pouco ruído. A correia em V transmite por atrito: tem algum deslizamento, que funciona como proteção contra sobrecarga.")

C = "Transferência de Calor"
U = 1 / (1 / 1000 + 0.0002)
num("MEC-C36", C, "Fator de incrustação",
    "Um trocador de calor limpo tem coeficiente global de 1.000 W/m²·K. Após um tempo de operação, a incrustação acrescenta uma resistência de 0,0002 m²·K/W. O novo coeficiente global, em W/m²·K, é, aproximadamente,",
    U, [800, 999.8, 1200, 5000], d=0,
    res=f"As resistências se somam: 1/U = 1/1.000 + 0,0002 = 0,0012 → U = <b>{br(U,0)} W/m²·K</b>. Uma camada fina de depósito reduz em 17% a capacidade do trocador; por isso o projeto prevê área extra e limpezas periódicas.")

q = 0.75 * 2 * (150 - 30); Tho = 150 - q / 2
num("MEC-C37", C, "Temperatura de saída pelo método da efetividade",
    "Num trocador de calor, o fluido quente (C = 2 kW/K, o menor dos dois) entra a 150 °C, e o frio entra a 30 °C. Com efetividade de 0,75, a temperatura de saída do fluido quente, em °C, é",
    Tho, [90, 120, 30, 112.5], d=0,
    res=f"q = ε·C<sub>mín</sub>·(T<sub>q,e</sub> − T<sub>f,e</sub>) = 0,75 × 2 × 120 = 180 kW. T<sub>q,s</sub> = 150 − 180/2 = <b>{br(Tho,0)} °C</b>. Como o quente é o C<sub>mín</sub>, ele sofre a maior variação de temperatura (90 K).")

dT = 1e6 * 0.01 ** 2 / (2 * 20)
num("MEC-C38", C, "Geração interna de calor em placa",
    "Uma placa de 20 mm de espessura (meia espessura L = 10 mm), com k = 20 W/m·K, gera calor uniformemente a 10⁶ W/m³ e tem as duas faces mantidas à mesma temperatura. A diferença entre a temperatura no plano central e nas faces, em °C, é",
    dT, [2 * dT, 4 * dT, dT / 2, 50], d=2,
    res=f"Com geração uniforme e faces à mesma temperatura, o perfil é parabólico: ΔT<sub>máx</sub> = q'''L²/(2k) = 10⁶ × 0,01²/(2 × 20) = <b>{br(dT,2)} °C</b>. Usar a espessura total (20 mm) no lugar da meia espessura quadruplica o resultado.")

con("MEC-C39", C, "Radiação em gases",
    "Na troca de calor por radiação em fornos e caldeiras, os gases que emitem e absorvem radiação de forma significativa são",
    "CO<sub>2</sub> e H<sub>2</sub>O (e outros gases de moléculas assimétricas), enquanto N<sub>2</sub> e O<sub>2</sub> são praticamente transparentes",
    ["N<sub>2</sub> e O<sub>2</sub>, por serem os mais abundantes no ar",
     "todos os gases igualmente, em qualquer comprimento de onda",
     "apenas os gases inertes, como argônio",
     "nenhum gás, pois gases não emitem radiação térmica"],
    res="Moléculas diatômicas simétricas (N<sub>2</sub>, O<sub>2</sub>, H<sub>2</sub>) quase não emitem nem absorvem no infravermelho. <b>CO<sub>2</sub>, H<sub>2</sub>O</b>, CO e SO<sub>2</sub> emitem em bandas específicas. Por isso os gases de combustão irradiam calor intensamente para os tubos da caldeira, e é também a base do efeito estufa.")

con("MEC-C40", C, "Barreira de vapor em isolamento frio",
    "Em tubulações de água gelada ou de fluido refrigerante, o isolamento térmico deve ter barreira de vapor contínua na face externa porque",
    "o vapor do ar ambiente que penetrasse no isolante condensaria (ou congelaria) perto do tubo frio, encharcando o material e destruindo sua capacidade isolante",
    ["a barreira aumenta a condutividade do isolante",
     "a barreira serve apenas para proteção contra raios ultravioleta",
     "o vapor de dentro da tubulação escapa pelo isolante",
     "a barreira dispensa a necessidade de espessura mínima"],
    res="O ar externo é mais quente e úmido; a pressão de vapor empurra a umidade para dentro do isolamento. Ao encontrar uma camada abaixo do ponto de orvalho, ela <b>condensa</b>, e a água conduz calor cerca de 25 vezes mais que o ar parado. Além disso, a espessura do isolamento deve evitar condensação na superfície externa.")

ref = (1 - 0.8) * 1000
num("MEC-C41", C, "Balanço de irradiação em superfície opaca",
    "Uma superfície opaca e cinzenta, com absortividade de 0,8, recebe irradiação de 1.000 W/m². A parcela refletida, em W/m², é",
    ref, [800, 0, 1000, 100], d=0,
    res=f"Para superfície opaca, α + ρ = 1 (sem transmissão): ρ = 0,2. Refletido = 0,2 × 1.000 = <b>{br(ref,0)} W/m²</b>; absorvido, 800 W/m². A emissão própria da superfície depende da sua temperatura e é outra parcela.")

Rc = 1 / (25 * 2)
num("MEC-C42", C, "Resistência térmica de convecção",
    "Uma superfície de 2 m² troca calor por convecção com h = 25 W/m²·K. A resistência térmica de convecção, em K/W, é",
    Rc, [50, 0.04, 12.5, 0.08], d=None,
    res=f"R<sub>conv</sub> = 1/(hA) = 1/(25 × 2) = <b>{br(Rc,3)} K/W</b>. Com a analogia elétrica, essa resistência entra em série com as de condução (L/kA) para calcular a taxa de calor q = ΔT/ΣR.")

con("MEC-C43", C, "Fator de correção F em trocadores casco e tubo",
    "No dimensionamento de trocadores casco e tubo com vários passes pelo método da média logarítmica, aplica-se um fator de correção F à ΔT<sub>ml</sub> calculada como contracorrente. Esse fator",
    "é menor ou igual a 1 e corrige o fato de o escoamento não ser contracorrente puro; valores muito baixos (abaixo de ~0,75) indicam arranjo inadequado",
    ["é sempre maior que 1, pois os passes aumentam a troca",
     "corrige a incrustação dos tubos",
     "depende apenas do material dos tubos",
     "é usado somente em trocadores de placas"],
    res="Com passes múltiplos, parte do trocador opera em correntes paralelas: a força motriz real é menor que a da contracorrente pura, e <b>F ≤ 1</b>. Se F fica baixo demais, o projeto pede mais cascos em série. A incrustação entra pelo fator R<sub>f</sub>, não por F.")

M = "Materiais e Tratamentos Térmicos"
con("MEC-M37", M, "Curvas TTT",
    "Num diagrama TTT (transformação-tempo-temperatura) de um aço eutetoide, para obter estrutura totalmente martensítica, o resfriamento a partir da austenita deve",
    "ser rápido o bastante para não cruzar o \"nariz\" da curva de início de transformação, até abaixo da temperatura M<sub>f</sub>",
    ["ser lento, para permitir a difusão do carbono",
     "manter o aço por longo tempo logo abaixo de 727 °C",
     "cruzar o nariz da curva para formar perlita fina",
     "parar acima de M<sub>s</sub> por tempo indefinido"],
    res="As curvas em <b>C</b> marcam o início e o fim da formação de perlita e bainita por difusão. Passando à esquerda do nariz (cerca de 550 °C no aço eutetoide, em poucos segundos), a austenita chega intacta a M<sub>s</sub> e se transforma em martensita, sem difusão. Aços ligados deslocam o nariz para a direita: são mais temperáveis.")

con("MEC-M38", M, "Austêmpera",
    "A austêmpera de aços consiste em resfriar a peça rapidamente a partir da austenita até um banho mantido acima de M<sub>s</sub> (por exemplo, 300 a 400 °C), conservando-a até o fim da transformação, para obter",
    "bainita, com boa tenacidade, menor distorção e sem necessidade de revenimento",
    ["martensita revenida, com alta fragilidade",
     "perlita grosseira e baixa dureza",
     "austenita estável à temperatura ambiente",
     "ferrita pura, por descarbonetação"],
    res="Na <b>austêmpera</b>, a transformação isotérmica gera <b>bainita</b>: dureza intermediária, tenacidade alta e pouca distorção, porque a peça não sofre o choque térmico da têmpera até a ambiente. É usada em molas, lâminas e no ferro fundido nodular austemperado (ADI).")

fc = (0.76 - 0.022) / (6.7 - 0.022)
num("MEC-M39", M, "Fração de cementita na perlita",
    "Pela regra da alavanca, aplicada logo abaixo de 727 °C entre a ferrita (0,022% C) e a cementita (6,7% C), a fração em massa de cementita na perlita (0,76% C) é, aproximadamente,",
    fc, [1 - fc, 0.76 / 6.7, 0.5, 0.022], fmt=lambda v: br(100 * v, 1) + "%",
    res=f"W<sub>Fe3C</sub> = (0,76 − 0,022)/(6,7 − 0,022) = 0,738/6,678 = <b>{br(100*fc,1)}%</b>. O resto (89%) é ferrita. Por isso as lamelas de cementita na perlita são bem mais finas que as de ferrita.")

ng = 2 ** (5 - 1)
num("MEC-M40", M, "Número de tamanho de grão ASTM",
    "Pela norma ASTM E112, o número de grãos por polegada quadrada numa micrografia com aumento de 100× é N = 2<sup>G−1</sup>, em que G é o número ASTM. Para G = 5, N é",
    ng, [32, 10, 25, 5], d=0,
    res=f"N = 2<sup>5−1</sup> = 2⁴ = <b>{br(ng,0)} grãos/pol²</b>. Quanto maior o número ASTM, mais fino o grão, maior a resistência e a tenacidade (Hall-Petch).")

con("MEC-M41", M, "Rigidez específica",
    "Comparando alumínio (E ≈ 70 GPa; ρ ≈ 2,7 g/cm³), titânio (E ≈ 110 GPa; ρ ≈ 4,5 g/cm³) e aço (E ≈ 200 GPa; ρ ≈ 7,85 g/cm³), a razão E/ρ (rigidez específica) é",
    "praticamente a mesma para os três, de cerca de 25 GPa/(g/cm³)",
    ["muito maior no aço, por ter o maior módulo",
     "muito maior no alumínio, por ser o mais leve",
     "nula no titânio",
     "o dobro no titânio em relação aos outros"],
    res="E/ρ: alumínio 26; titânio 24; aço 25. Para peças em tração, onde o que importa é o alongamento por unidade de peso, os três empatam: <b>trocar de metal não ganha rigidez por peso</b>. Ganha-se com geometria (perfis, sanduíches) ou com compósitos (fibra de carbono: E/ρ acima de 100).")

con("MEC-M42", M, "Galvanização",
    "O revestimento de zinco por imersão a quente (galvanização) protege o aço contra a corrosão porque",
    "atua como barreira e, se riscado, o zinco, menos nobre, corrói no lugar do aço exposto (proteção catódica)",
    ["o zinco é mais nobre que o ferro e por isso não corrói",
     "o zinco forma uma camada de cementita na superfície",
     "o zinco reage com o carbono do aço formando carbonetos protetores",
     "o zinco só protege enquanto a camada estiver totalmente intacta, como uma tinta"],
    res="Ao contrário de uma tinta, o zinco <b>protege mesmo onde o aço ficou exposto</b>, sacrificando-se. A taxa de corrosão do zinco na atmosfera é baixa e a camada dura décadas. Revestimentos mais nobres que o aço (estanho, cromo) fazem o contrário: num risco, aceleram a corrosão do aço.")

con("MEC-M43", M, "Aspecto da fratura dúctil e frágil",
    "Na análise de uma fratura por tração, a fratura dúctil diferencia-se da frágil por apresentar",
    "estricção e superfície fibrosa e opaca em forma de taça e cone, com microcavidades (dimples) vistas ao microscópio",
    ["superfície plana, brilhante e cristalina, sem deformação visível",
     "marcas de praia (beach marks) concêntricas",
     "facetas de clivagem planas em cada grão",
     "ausência total de deformação plástica"],
    res="<b>Dúctil</b>: muita deformação plástica, estricção, taça e cone, fundo fibroso; ao microscópio eletrônico, dimples (coalescência de microvazios). <b>Frágil</b>: pouca deformação, superfície plana e brilhante, clivagem. Marcas de praia são típicas de fadiga.")

B = "Máquinas de Fluxo"
con("MEC-B36", B, "Bombas em série",
    "Duas bombas centrífugas idênticas associadas em série, num sistema com altura estática elevada, resultam numa curva combinada em que",
    "as alturas se somam para a mesma vazão, sendo indicado quando o sistema exige mais altura do que uma bomba sozinha fornece",
    ["as vazões se somam para a mesma altura",
     "a vazão dobra e a altura cai à metade",
     "a potência total é a mesma de uma bomba",
     "a segunda bomba sempre opera em shutoff"],
    res="Em <b>série</b>, o fluido passa pelas duas bombas: mesma vazão, alturas somadas. É como uma bomba de dois estágios. Em <b>paralelo</b>, as vazões se somam para a mesma altura. A vazão real em cada caso sai do cruzamento com a curva do sistema.")

N2 = 3 * (3500 / 1750) ** 2
num("MEC-B37", B, "Semelhança do NPSH requerido",
    "Uma bomba tem NPSH requerido de 3 m a 1.750 rpm, num certo ponto de operação. Se a rotação for dobrada para 3.500 rpm, no ponto homólogo, o NPSH requerido será, aproximadamente, em m,",
    N2, [6, 24, 3, 1.5], d=0,
    res=f"O NPSH<sub>r</sub> segue a lei das alturas: ∝ n². NPSH<sub>r2</sub> = 3 × 2² = <b>{br(N2,0)} m</b>. Por isso bombas de 2 polos (3.500 rpm) cavitam com muito mais facilidade que as de 4 polos com a mesma instalação de sucção.")

Y = 9.81 * 100
num("MEC-B38", B, "Energia específica disponível numa turbina",
    "Uma turbina hidráulica dispõe de queda líquida de 100 m (g = 9,81 m/s²). A energia hidráulica específica disponível, por quilograma de água, em J/kg, é",
    Y, [100, 9.81, 98.1, 9810], d=0,
    res=f"Y = gH = 9,81 × 100 = <b>{br(Y,0)} J/kg</b>. Multiplicando pela vazão mássica, obtém-se a potência hidráulica (1 m³/s → 981 kW).")

con("MEC-B39", B, "Condensado em resfriadores intermediários",
    "Em compressores de ar de múltiplos estágios, os resfriadores intermediários e o pós-resfriador precisam de purgadores (drenos) porque",
    "ao resfriar o ar comprimido, a umidade aspirada condensa, e a água precisa ser removida para não atingir o estágio seguinte e a rede",
    ["o óleo lubrificante evapora nos resfriadores",
     "o ar se liquefaz no resfriador",
     "a pressão cai abaixo da atmosférica",
     "os resfriadores produzem gelo continuamente"],
    res="Comprimir o ar aumenta a pressão parcial do vapor; resfriá-lo em seguida faz cair abaixo do ponto de orvalho, e a água <b>condensa</b>. Gotas no estágio seguinte danificam válvulas e pistões; na rede, causam corrosão e golpes. Daí purgadores, separadores e secadores.")

con("MEC-B40", B, "Ventiladores de pás para trás",
    "Ventiladores centrífugos de pás curvadas para trás (backward), em comparação com os de pás para frente (sirocco), caracterizam-se por",
    "maior rendimento e curva de potência que atinge um máximo e depois cai (não sobrecarregável), evitando sobrecarga do motor",
    ["menor rendimento e potência crescente sem limite com a vazão",
     "maior vazão por tamanho de rotor, porém mais ruído e menor rendimento",
     "pressão nula em qualquer vazão",
     "funcionamento apenas como ventilador axial"],
    res="Pás <b>para trás</b>: rendimentos de 80% a 85% e potência com máximo próximo do ponto de projeto (o motor não sobrecarrega se a vazão aumentar). Pás <b>para frente</b> (sirocco) são compactas e silenciosas em baixa rotação, mas rendem menos e a potência cresce continuamente com a vazão.")

vj = 0.98 * math.sqrt(2 * 9.81 * 500)
num("MEC-B41", B, "Velocidade do jato na turbina Pelton",
    "Uma turbina Pelton opera com queda líquida de 500 m (g = 9,81 m/s²) e o injetor tem coeficiente de velocidade 0,98. A velocidade do jato, em m/s, é, aproximadamente,",
    vj, [math.sqrt(9.81 * 500), math.sqrt(2 * 9.81 * 500), 48.5, 194], d=1,
    res=f"V<sub>j</sub> = C<sub>v</sub>·√(2gH) = 0,98 × √9.810 = 0,98 × 99,0 = <b>{br(vj,1)} m/s</b>. Para máximo rendimento, as conchas devem andar a cerca de metade disso.")

con("MEC-B42", B, "Compressores alternativos e centrífugos",
    "Na escolha entre compressores alternativos e centrífugos, é correto afirmar que os alternativos são mais indicados para",
    "vazões pequenas a médias com razões de compressão elevadas, enquanto os centrífugos atendem grandes vazões com razões moderadas por estágio",
    ["grandes vazões contínuas com baixa razão de compressão",
     "aplicações sem necessidade de lubrificação nem válvulas",
     "operação sem pulsação de pressão",
     "rotações muito altas, acima de 20.000 rpm"],
    res="O <b>alternativo</b> é de deslocamento positivo: atinge razões altas em poucos estágios e vazões pequenas, mas tem pulsação e válvulas de manutenção frequente. O <b>centrífugo</b> é dinâmico: grandes vazões, fluxo contínuo e alta rotação, com razão por estágio limitada (cerca de 1,5 a 3,5).")

H = (300 + 20) / 10 + (2.25 ** 2 - 1 ** 2) / 20
num("MEC-B43", B, "Altura manométrica com diâmetros diferentes",
    "Numa bomba com água (g = 10 m/s²; ρ = 1.000 kg/m³), a descarga tem 300 kPa e a sucção −20 kPa (manômetros na mesma cota). As velocidades são 1,0 m/s na sucção e 2,25 m/s na descarga. A altura manométrica, em m, é, aproximadamente,",
    H, [32.0, 28.2, 34.0, 30.0], d=1,
    res=f"H = (p<sub>d</sub> − p<sub>s</sub>)/ρg + (V<sub>d</sub>² − V<sub>s</sub>²)/2g = 32,0 + (5,06 − 1,00)/20 = 32,0 + 0,20 = <b>{br(H,1)} m</b>. Com diâmetros diferentes, a parcela cinética entra, ainda que pequena.")

V = "Vibrações"
k = 48 * 200e9 * 4e-6 / 2 ** 3; f = math.sqrt(k / 120) / (2 * math.pi)
num("MEC-V26", V, "Frequência natural de massa no meio de viga",
    "Um motor de 120 kg está montado no meio de uma viga biapoiada de aço (E = 200 GPa; I = 4 × 10<sup>−6</sup> m⁴) com 2 m de vão. Desprezando a massa da viga, a frequência natural, em Hz, é, aproximadamente,",
    f, [math.sqrt(k / 120), f / 2, 2 * f, f / 4], d=1,
    res=f"Rigidez no meio do vão: k = 48EI/L³ = 48 × 200 × 10⁹ × 4 × 10<sup>−6</sup>/8 = 4,8 × 10⁶ N/m. ω<sub>n</sub> = √(4,8 × 10⁶/120) = 200 rad/s → f<sub>n</sub> = <b>{br(f,1)} Hz</b> (1.910 rpm). Um motor de 4 polos a 1.780 rpm ficaria perigosamente perto.")

X = 100 / (500 * 20) * 1000
num("MEC-V27", V, "Amplitude na ressonância limitada pelo amortecimento",
    "Um sistema com coeficiente de amortecimento de 500 N·s/m é excitado exatamente na frequência natural, de 20 rad/s, por uma força harmônica de amplitude 100 N. A amplitude do deslocamento, em mm, é",
    X, [X / 2, 2 * X, 0.2, 100], d=1,
    res=f"Na ressonância, a força da mola e a da inércia se cancelam e só o amortecimento limita: X = F<sub>0</sub>/(c·ω<sub>n</sub>) = 100/(500 × 20) = 0,01 m = <b>{br(X,1)} mm</b>.")

TR = 1 / (3 ** 2 - 1)
num("MEC-V28", V, "Transmissibilidade acima da ressonância",
    "Uma máquina montada sobre molas, com amortecimento desprezível, opera com frequência de excitação igual a 3 vezes a frequência natural do sistema. A fração da força de excitação transmitida à fundação é, aproximadamente,",
    TR, [1 / 3, 1 / 9, 0.5, 8], d=3,
    res=f"Sem amortecimento: TR = 1/|1 − r²| = 1/(9 − 1) = <b>{br(TR,3)}</b>, ou 12,5% da força. Isolamento só funciona com r &gt; √2; quanto maior r, melhor.")

w = math.sqrt(3 * 9.81 / (2 * 1)); Tp = 2 * math.pi / w
num("MEC-V29", V, "Pêndulo físico (barra articulada)",
    "Uma barra fina e uniforme de 1 m de comprimento oscila em torno de uma articulação numa das extremidades, com pequenas amplitudes (g = 9,81 m/s²). Sendo ω<sub>n</sub> = √(3g/2L), o período de oscilação, em s, é, aproximadamente,",
    Tp, [2 * math.pi * math.sqrt(1 / 9.81), w, Tp / 2, 2 * Tp], d=2,
    res=f"ω<sub>n</sub> = √(3 × 9,81/2) = 3,84 rad/s → T = 2π/ω<sub>n</sub> = <b>{br(Tp,2)} s</b>. Um pêndulo simples de 1 m teria 2,01 s: a barra oscila como um pêndulo simples de comprimento 2L/3.")

con("MEC-V30", V, "Princípio dos transdutores sísmicos",
    "Um transdutor sísmico (massa-mola-amortecedor dentro de uma caixa fixada à máquina) funciona como acelerômetro quando",
    "sua frequência natural é muito maior que as frequências medidas, e como sensor de deslocamento (vibrômetro) quando é muito menor",
    ["sua frequência natural é igual à frequência medida",
     "não tem amortecimento nenhum",
     "sua frequência natural é muito menor que as frequências medidas",
     "a massa interna é muito maior que a da máquina"],
    res="Com f<sub>n</sub> ≫ f, o deslocamento relativo da massa interna é proporcional à <b>aceleração</b>: é o acelerômetro piezelétrico, de f<sub>n</sub> alta (dezenas de kHz). Com f<sub>n</sub> ≪ f, a massa fica quase parada no espaço e mede o deslocamento (sismógrafo). Perto de f<sub>n</sub>, a ressonância distorce a medida.")

P = "Fabricação e Soldagem"
con("MEC-P28", P, "Dureza do rebolo na retificação",
    "Na retificação, para retificar materiais muito duros, como aços temperados, recomenda-se em geral um rebolo de liga (grau)",
    "mole, que libera com facilidade os grãos abrasivos desgastados, expondo grãos novos e afiados",
    ["duro, que segura os grãos gastos por mais tempo",
     "sem abrasivo, apenas de liga",
     "metálico, sem porosidade",
     "de qualquer grau, pois a dureza do rebolo não influencia"],
    res="O \"grau\" é a força com que a liga segura o abrasivo. Material duro desgasta o grão rápido: um rebolo <b>mole</b> se autoafia, soltando os grãos cegos. Material mole cega pouco o grão e pede rebolo duro, para não gastar o rebolo à toa. A regra prática é: material duro, rebolo mole.")

con("MEC-P29", P, "Ângulo de saída da ferramenta",
    "Na geometria de ferramentas de usinagem, ângulos de saída (γ) negativos, comuns em pastilhas de metal duro e cerâmica para desbaste de aço, têm como característica",
    "aumentar a resistência da aresta de corte contra choques, à custa de maior força e potência de corte",
    ["reduzir a força de corte e facilitar a saída do cavaco",
     "ser indicados para usinar alumínio e materiais macios",
     "eliminar a formação de cavaco",
     "dispensar ângulo de folga"],
    res="Com saída <b>negativa</b>, a aresta fica mais \"cheia\" e suporta impactos (corte interrompido), mas o cavaco é mais deformado e as forças sobem. Saída <b>positiva</b> corta mais leve, ideal para alumínio e aços macios, com aresta mais frágil.")

con("MEC-P30", P, "Fresamento concordante e discordante",
    "No fresamento concordante (climb milling), em comparação com o discordante (convencional),",
    "a espessura do cavaco começa máxima e termina nula, o que dá melhor acabamento e vida da ferramenta, mas exige máquina sem folga no fuso da mesa",
    ["a espessura do cavaco começa nula e cresce, causando atrito e encruamento na entrada do dente",
     "a força de corte tende a afastar a peça da fresa, por isso não há risco com folgas",
     "a vida da ferramenta é sempre menor",
     "só pode ser usado em máquinas manuais antigas"],
    res="No <b>concordante</b>, o dente entra no material com a espessura máxima de cavaco, sem \"esfregar\" a superfície; a força puxa a peça para a fresa, e qualquer folga no fuso da mesa causa avanços bruscos. Por isso ele é o padrão em CNC (fusos de esferas sem folga) e era evitado em máquinas convencionais antigas.")

BA = math.pi / 2 * (4 + 0.33 * 2)
num("MEC-P31", P, "Comprimento desenvolvido no dobramento",
    "Uma chapa de 2 mm de espessura é dobrada a 90° com raio interno de 4 mm. Considerando a linha neutra a 0,33 da espessura a partir da face interna (fator K = 0,33), o comprimento do arco da linha neutra (bend allowance), em mm, é, aproximadamente,",
    BA, [math.pi / 2 * 4, math.pi / 2 * 6, math.pi / 2 * 5, math.pi * (4 + 0.66)], d=2,
    res=f"BA = (π/2)·(R<sub>i</sub> + K·t) = 1,571 × (4 + 0,66) = <b>{br(BA,2)} mm</b>. O comprimento da chapa plana é a soma dos trechos retos com esse arco. Usar o raio interno (6,28 mm) ou o externo (9,42 mm) erra o blank.")

con("MEC-P32", P, "Transferência por curto-circuito no MIG/MAG",
    "Na soldagem MIG/MAG, o modo de transferência metálica por curto-circuito, com baixa corrente e tensão, é indicado para",
    "chapas finas e soldagem fora de posição, pela poça pequena e de baixo aporte térmico",
    ["chapas grossas na posição plana com máxima taxa de deposição",
     "soldagem sem gás de proteção",
     "eliminar totalmente os respingos em qualquer condição",
     "soldagem de alumínio com corrente alternada"],
    res="No <b>curto-circuito</b>, a ponta do arame toca a poça várias vezes por segundo: o aporte de calor é baixo e a poça, pequena e controlável. Serve para chapas finas, passes de raiz e todas as posições. Em correntes altas, com gás rico em argônio, a transferência passa a goticular (spray), de alta deposição, só na posição plana.")

con("MEC-P33", P, "Fundição sob pressão",
    "A fundição sob pressão (die casting) em matriz metálica é característica da produção de",
    "peças de ligas de baixo ponto de fusão (alumínio, zinco, magnésio) em grande série, com paredes finas e bom acabamento",
    ["peças grandes de aço em pequenas quantidades",
     "lingotes de ferro fundido em areia verde",
     "peças de aço inoxidável com moldes de cera perdida",
     "peças únicas de grande porte, como carcaças de turbinas"],
    res="A <b>fundição sob pressão</b> injeta o metal líquido em alta velocidade numa matriz de aço: ciclos de segundos, precisão e paredes finas (carcaças de câmbio, blocos de motor de alumínio). A matriz é cara e só se paga em grandes séries; metais de alto ponto de fusão, como o aço, destruiriam a matriz.")
