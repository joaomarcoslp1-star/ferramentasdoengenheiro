# -*- coding: utf-8 -*-
"""Gera as versões em inglês das ferramentas (vigas, inércia, torque) a partir das versões em português."""
import re
S = '/home/claude/site_src'

def rep(s, pairs):
    for a, b in pairs:
        if a not in s:
            raise SystemExit('NÃO ACHEI: ' + a[:80])
        s = s.replace(a, b)
    return s

UNITSEL = '''<div><label>Units<select id="{p}-u"><option value="us">US customary ({us})</option><option value="si">SI ({si})</option></select></label></div>'''

# ---------------- BEAM ----------------
v = open(f'{S}/vigas/tool.html').read()
v = rep(v, [
 ('<h3>Viga</h3>\n  <p class="sub">Forças em kN, distâncias em m (a partir da extremidade esquerda), momentos em kN·m. Cargas para baixo são positivas.</p>\n  <div class="g">',
  '<h3>Beam</h3>\n  <p class="sub">Positions are measured from the left end. Downward loads are positive. Switching units converts the values you typed.</p>\n  <div class="g">\n    ' + UNITSEL.format(p='vg', us='kip, ft', si='kN, m')),
 ('Comprimento da viga L (m)', 'Beam length L (<span class="uL">ft</span>)'),
 ('value="6"></label></div>\n    <div><label>Tipo de apoio', 'value="20"></label></div>\n    <div><label>Supports'),
 ('Biapoiada (pino + rolete)', 'Simply supported (pin + roller)'),
 ('Engastada à esquerda (balanço)', 'Fixed at left end (cantilever)'),
 ('Engastada à direita (balanço)', 'Fixed at right end (cantilever)'),
 ('Posição do apoio A (m)', 'Support A position (<span class="uL">ft</span>)'),
 ('Posição do apoio B (m)<input id="vg-b" type="number" step="any" min="0" value="6">', 'Support B position (<span class="uL">ft</span>)<input id="vg-b" type="number" step="any" min="0" value="20">'),
 ('<h3>Cargas</h3>', '<h3>Loads</h3>'),
 ('Distribuída: informe a intensidade no início e no fim (iguais = uniforme; diferentes = triangular ou trapezoidal). Momento: positivo no sentido anti-horário.',
  'Distributed load: enter the intensity at the start and at the end (equal = uniform; different = triangular or trapezoidal). Applied moment: counterclockwise is positive.'),
 ('+ Carga pontual', '+ Point load'), ('+ Carga distribuída', '+ Distributed load'), ('+ Momento concentrado', '+ Applied moment'),
 ('<span>Reação</span><b>–</b></div>\n    <div class="kpi" id="vg-k2"><span>Reação</span>', '<span>Reaction</span><b>–</b></div>\n    <div class="kpi" id="vg-k2"><span>Reaction</span>'),
 ('Cortante máximo |V|', 'Maximum shear |V|'), ('Momento fletor máximo |M|', 'Maximum bending moment |M|'),
 ('Esquema da viga e diagramas de esforço cortante e momento fletor', 'Beam sketch with shear force and bending moment diagrams'),
 ('Convenção: cortante positivo quando a resultante à esquerda da seção aponta para cima; momento positivo quando traciona a fibra de baixo (viga "sorrindo"). Ferramenta para estudo e pré-dimensionamento.',
  'Sign convention: shear is positive when the resultant to the left of the section points up; moment is positive when it puts the bottom fiber in tension (sagging). For study and preliminary design only.'),
 ("toLocaleString('pt-BR'", "toLocaleString('en-US'"),
 ("var LBL={P:'Carga pontual',W:'Carga distribuída',M:'Momento concentrado'};",
  "var LBL={P:'Point load',W:'Distributed load',M:'Applied moment'};\nvar UN={us:{F:'kip',L:'ft',M:'kip·ft',w:'kip/ft'},si:{F:'kN',L:'m',M:'kN·m',w:'kN/m'}},FX={F:4.44822,L:0.3048,M:1.35582,w:14.5939},U=UN.us,usys='us';"),
 ("'<div><label>Tipo<input value=\"'", "'<div><label>Type<input value=\"'"),
 ("'<div><label>P (kN)<input class=\"v1\"", "'<div><label>P ('+U.F+')<input class=\"v1\" data-q=\"F\""),
 ("'\"></label></div><div><label>Posição x (m)<input class=\"x1\" type=\"number\" step=\"any\" value=\"'+(v.x1!=null?v.x1:1)+'\"></label></div><div></div><div></div>';\n  if(t==='W')",
  "'\"></label></div><div><label>Position x ('+U.L+')<input class=\"x1\" data-q=\"L\" type=\"number\" step=\"any\" value=\"'+(v.x1!=null?v.x1:1)+'\"></label></div><div></div><div></div>';\n  if(t==='W')"),
 ("'<div><label>w início (kN/m)<input class=\"v1\"", "'<div><label>w start ('+U.w+')<input class=\"v1\" data-q=\"w\""),
 ("<div><label>w fim (kN/m)<input class=\"v2\"", "<div><label>w end ('+U.w+')<input class=\"v2\" data-q=\"w\""),
 ("<div><label>de x (m)<input class=\"x1\"", "<div><label>from x ('+U.L+')<input class=\"x1\" data-q=\"L\""),
 ("<div><label>até x (m)<input class=\"x2\"", "<div><label>to x ('+U.L+')<input class=\"x2\" data-q=\"L\""),
 ("'<div><label>M (kN·m)<input class=\"v1\"", "'<div><label>M ('+U.M+')<input class=\"v1\" data-q=\"M\""),
 ("'\"></label></div><div><label>Posição x (m)<input class=\"x1\" type=\"number\" step=\"any\" value=\"'+(v.x1!=null?v.x1:1)+'\"></label></div><div></div><div></div>';\n  h+=",
  "'\"></label></div><div><label>Position x ('+U.L+')<input class=\"x1\" data-q=\"L\" type=\"number\" step=\"any\" value=\"'+(v.x1!=null?v.x1:1)+'\"></label></div><div></div><div></div>';\n  h+="),
 ('title="Remover"', 'title="Remove"'),
 ("addLoad('P',{v1:20,x1:2}); addLoad('W',{v1:5,v2:5,x1:0,x2:6});", "addLoad('P',{v1:5,x1:6}); addLoad('W',{v1:0.4,v2:0.4,x1:0,x2:20});"),
 ("err='Informe um comprimento positivo.'", "err='Enter a positive length.'"),
 ("err='Os apoios precisam estar dentro da viga, com B à direita de A.'", "err='Supports must be on the beam, with B to the right of A.'"),
 ("err='Há carga fora da viga (posição entre 0 e L).'", "err='A load is outside the beam (position must be between 0 and L).'"),
 ("err='Preencha todos os valores das cargas.'", "err='Fill in all load values.'"),
 ("var L=num($('vg-L'))", "setUnits(); var L=num($('vg-L'))"),
 ("'<span>Reação no apoio A</span><b>'+nf(sup[0].F,2)+' kN</b>'", "'<span>Reaction at A</span><b>'+nf(sup[0].F,2)+' '+U.F+'</b>'"),
 ("'<span>Reação no apoio B</span><b>'+nf(sup[1].F,2)+' kN</b>'", "'<span>Reaction at B</span><b>'+nf(sup[1].F,2)+' '+U.F+'</b>'"),
 ("'<span>Reação vertical no engaste</span><b>'+nf(sup[0].F,2)+' kN</b>'", "'<span>Vertical reaction at the fixed end</span><b>'+nf(sup[0].F,2)+' '+U.F+'</b>'"),
 ("'<span>Momento no engaste</span><b>'+nf(Math.abs(sup[0].M),2)+' kN·m</b>'", "'<span>Fixed-end moment</span><b>'+nf(Math.abs(sup[0].M),2)+' '+U.M+'</b>'"),
 ("$('vg-vm').textContent=nf(vmax,2)+' kN'; $('vg-mm').textContent=nf(mmax,2)+' kN·m';", "$('vg-vm').textContent=nf(vmax,2)+' '+U.F; $('vg-mm').textContent=nf(mmax,2)+' '+U.M;"),
 ("if(l.t==='P') return nf(l.P,2)+' kN em x = '+nf(l.x,2)+' m'; if(l.t==='M') return 'momento de '+nf(l.M,2)+' kN·m em x = '+nf(l.x,2)+' m'; return 'distribuída de '+nf(l.w1,2)+(l.w1!==l.w2?' a '+nf(l.w2,2):'')+' kN/m entre '+nf(l.a,2)+' e '+nf(l.b,2)+' m → resultante '+nf(l.F,2)+' kN em x = '+nf(l.xc,3)+' m';",
  "if(l.t==='P') return nf(l.P,2)+' '+U.F+' at x = '+nf(l.x,2)+' '+U.L; if(l.t==='M') return 'moment of '+nf(l.M,2)+' '+U.M+' at x = '+nf(l.x,2)+' '+U.L; return 'distributed load of '+nf(l.w1,2)+(l.w1!==l.w2?' to '+nf(l.w2,2):'')+' '+U.w+' from '+nf(l.a,2)+' to '+nf(l.b,2)+' '+U.L+' → resultant '+nf(l.F,2)+' '+U.F+' at x = '+nf(l.xc,3)+' '+U.L;"),
 ("'<b>1. Cargas e resultantes:</b> '+(desc.join('; ')||'nenhuma carga')", "'<b>1. Loads and resultants:</b> '+(desc.join('; ')||'no loads')"),
 ("'<b>2. Soma dos momentos em A = 0:</b> R<sub>B</sub> × ('", "'<b>2. Sum of moments about A = 0:</b> R<sub>B</sub> × ('"),
 ("' → <b>R<sub>B</sub> = '+nf(sup[1].F,3)+' kN</b>'", "' → <b>R<sub>B</sub> = '+nf(sup[1].F,3)+' '+U.F+'</b>'"),
 ("'<b>3. Soma das forças verticais = 0:</b> R<sub>A</sub> = '", "'<b>3. Sum of vertical forces = 0:</b> R<sub>A</sub> = '"),
 ("' → <b>R<sub>A</sub> = '+nf(sup[0].F,3)+' kN</b>'", "' → <b>R<sub>A</sub> = '+nf(sup[0].F,3)+' '+U.F+'</b>'"),
 ("'<b>2. Soma das forças verticais = 0:</b> <b>R = '+nf(sP,3)+' kN</b> (para cima)'", "'<b>2. Sum of vertical forces = 0:</b> <b>R = '+nf(sP,3)+' '+U.F+'</b> (upward)'"),
 ("'<b>3. Soma dos momentos no engaste = 0:</b> M<sub>engaste</sub> = '", "'<b>3. Sum of moments about the fixed end = 0:</b> M<sub>fixed</sub> = '"),
 ("' = <b>'+nf(sup[0].M,3)+' kN·m</b> ('+(sup[0].M>=0?'anti-horário':'horário')+')'", "' = <b>'+nf(sup[0].M,3)+' '+U.M+'</b> ('+(sup[0].M>=0?'counterclockwise':'clockwise')+')'"),
 ("'<b>4. Momento fletor máximo:</b> '+(mpos>1e-9?'positivo de '+nf(mpos,2)+' kN·m em x = '+nf(xmp,2)+' m':'')", "'<b>4. Maximum bending moment:</b> '+(mpos>1e-9?'positive '+nf(mpos,2)+' '+U.M+' at x = '+nf(xmp,2)+' '+U.L:'')"),
 ("(mneg<-1e-9?'negativo de '+nf(mneg,2)+' kN·m em x = '+nf(xmn,2)+' m':'')+'. O momento é máximo onde o cortante passa por zero ou muda de sinal.'", "(mneg<-1e-9?'negative '+nf(mneg,2)+' '+U.M+' at x = '+nf(xmn,2)+' '+U.L:'')+'. The moment peaks where the shear crosses zero or changes sign.'"),
 ("\">Esquema</text>'", "\">Sketch</text>'"),
 ("(i?'B':'A')+' · '+nf(s.F,2)+' kN</text>'", "(i?'B':'A')+' · '+nf(s.F,2)+' '+U.F+'</text>'"),
 ("\">R = '+nf(s.F,2)+' kN · M = '+nf(Math.abs(s.M),2)+' kN·m</text>'", "\">R = '+nf(s.F,2)+' '+U.F+' · M = '+nf(Math.abs(s.M),2)+' '+U.M+'</text>'"),
 ("nf(Math.abs(l.P),1)+' kN</text>'", "nf(Math.abs(l.P),1)+' '+U.F+'</text>'"),
 ("(l.w1!==l.w2?'→'+nf(l.w2,1):'')+' kN/m</text>'", "(l.w1!==l.w2?'→'+nf(l.w2,1):'')+' '+U.w+'</text>'"),
 ("nf(Math.abs(l.M),1)+' kN·m</text>'", "nf(Math.abs(l.M),1)+' '+U.M+'</text>'"),
 ("\">L = '+nf(L,2)+' m</text>'", "\">L = '+nf(L,2)+' '+U.L+'</text>'"),
 ("diag(250,170,1,'Esforço cortante V (kN)','kN'", "diag(250,170,1,'Shear force V ('+U.F+')',U.F"),
 ("diag(455,170,2,'Momento fletor M (kN·m) — desenhado do lado tracionado','kN·m'", "diag(455,170,2,'Bending moment M ('+U.M+'), drawn on the tension side',U.M"),
 ("function draw(L,", """function setUnits(){ var s=$('vg-u').value; if(s===usys) return; var to=s==='si';
  R.querySelectorAll('input[data-q]').forEach(function(e){var x=num(e); if(isFinite(x)) e.value=+(to? x*FX[e.dataset.q] : x/FX[e.dataset.q]).toPrecision(4);});
  ['vg-L','vg-a','vg-b'].forEach(function(i){var e=$(i),x=num(e); if(isFinite(x)) e.value=+(to? x*FX.L : x/FX.L).toPrecision(4);});
  usys=s; U=UN[s];
  R.querySelectorAll('.uL').forEach(function(e){e.textContent=U.L;});
  R.querySelectorAll('.ld').forEach(function(d){ d.querySelectorAll('label').forEach(function(l){ var q=l.querySelector('input[data-q]'); if(q) l.firstChild.textContent=l.firstChild.textContent.replace(/\\(.*\\)/,'('+U[q.dataset.q]+')'); }); });
}
function draw(L,"""),
])
left=[m for m in re.findall(r".{25}kN.{8}", v.split('<script>')[1]) if 'si:{F' not in m]
assert not left, left
v = v.replace('id="vg-L" type="number" step="any" min="0.1" value="6"', 'id="vg-L" type="number" step="any" min="0.1" value="20"')
open(f'{S}/en/beam_tool.html', 'w').write(v)
print('beam ok')

# ---------------- INERTIA ----------------
v = open(f'{S}/inercia/tool.html').read()
v = rep(v, [
 ('<h3>Seção transversal</h3>\n  <p class="sub">Medidas em milímetros. Resultados em cm (área em cm², inércia em cm⁴, módulo resistente em cm³), como nas tabelas de perfis.</p>\n  <div class="g">',
  '<h3>Cross section</h3>\n  <p class="sub">US customary: dimensions and results in inches (in², in⁴, in³), as in the AISC tables. SI: dimensions in mm, results in cm (cm², cm⁴, cm³), as in European tables.</p>\n  <div class="g">\n    ' + UNITSEL.format(p='in', us='in', si='mm, cm')),
 ('<label>Tipo de seção<select id="in-t">', '<label>Section type<select id="in-t">'),
 ('<option value="ret">Retângulo</option><option value="cir">Circular cheia</option><option value="tub">Tubo circular</option><option value="tre">Tubo retangular</option>',
  '<option value="ret">Rectangle</option><option value="cir">Solid circle</option><option value="tub">Round tube (pipe)</option><option value="tre">Rectangular tube (HSS)</option>'),
 ('<option value="I">Perfil I (simétrico)</option><option value="T" selected>Perfil T</option><option value="L">Cantoneira L</option><option value="U">Perfil U</option><option value="comp">Composta por retângulos</option>',
  '<option value="I">I-beam / W shape (symmetric)</option><option value="T" selected>T section</option><option value="L">Angle (L)</option><option value="U">Channel (C)</option><option value="comp">Built-up from rectangles</option>'),
 ('Cada retângulo: largura b, altura h e a posição do canto inferior esquerdo (x, y). Retângulos não devem se sobrepor.', 'Each rectangle: width b, height h and the position of its lower-left corner (x, y). Rectangles must not overlap.'),
 ('+ Retângulo</button>', '+ Rectangle</button>'),
 ('Desenho da seção com o centroide e os eixos', 'Section drawing with the centroid and axes'),
 ('<span>Área A</span>', '<span>Area A</span>'),
 ('Centroide (x̄ ; ȳ) a partir do canto inferior esquerdo', 'Centroid (x̄ ; ȳ) from the lower-left corner'),
 ('Momento de inércia I<sub>x</sub> (eixo horizontal)', 'Moment of inertia I<sub>x</sub> (horizontal axis)'),
 ('Momento de inércia I<sub>y</sub> (eixo vertical)', 'Moment of inertia I<sub>y</sub> (vertical axis)'),
 ('Módulo resistente W<sub>x</sub> (topo ; base)', 'Section modulus S<sub>x</sub> (top ; bottom)'),
 ('Módulo resistente W<sub>y</sub> (direita ; esquerda)', 'Section modulus S<sub>y</sub> (right ; left)'),
 ('Raio de giração r<sub>x</sub> ; r<sub>y</sub>', 'Radius of gyration r<sub>x</sub> ; r<sub>y</sub>'),
 ('Produto de inércia I<sub>xy</sub> e eixos principais', 'Product of inertia I<sub>xy</sub> and principal axes'),
 ('<th>Parte</th><th>A (mm²)</th><th>x<sub>i</sub> (mm)</th><th>y<sub>i</sub> (mm)</th><th>I<sub>x,próprio</sub> (mm⁴)</th><th>d<sub>y</sub> = y<sub>i</sub> − ȳ</th><th>A·d<sub>y</sub>² (mm⁴)</th><th>I<sub>y,próprio</sub> (mm⁴)</th><th>A·d<sub>x</sub>² (mm⁴)</th>',
  '<th>Part</th><th>A (<span class="uL">in</span>²)</th><th>x<sub>i</sub> (<span class="uL">in</span>)</th><th>y<sub>i</sub> (<span class="uL">in</span>)</th><th>I<sub>x,own</sub> (<span class="uL">in</span>⁴)</th><th>d<sub>y</sub> = y<sub>i</sub> − ȳ</th><th>A·d<sub>y</sub>² (<span class="uL">in</span>⁴)</th><th>I<sub>y,own</sub> (<span class="uL">in</span>⁴)</th><th>A·d<sub>x</sub>² (<span class="uL">in</span>⁴)</th>'),
 ('Passo a passo pelo teorema dos eixos paralelos (Steiner): I<sub>x</sub> = Σ (I<sub>próprio</sub> + A·d²). Partes vazadas entram com sinal negativo. Valores de perfis comerciais variam com os raios de concordância; para projeto, use a tabela do fabricante.',
  'Step by step with the parallel axis theorem: I<sub>x</sub> = Σ (I<sub>own</sub> + A·d²). Holes enter with a negative sign. Rolled shapes have fillets between web and flange, so their tabulated values differ slightly; for design, use the AISC or manufacturer tables.'),
 ("toLocaleString('pt-BR'", "toLocaleString('en-US'"),
 ("var DIMS={", "var USYS='us',UL={us:'in',si:'mm'};\nvar DIMS_US={ret:[4,8],cir:[4],tub:[4.5,0.237],tre:[4,6,0.25],I:[8,4,0.4,0.25],T:[8,6,0.75,0.5],L:[3,3,0.25],U:[6,2,0.35,0.25]};\nvar DIMS={"),
 ("ret:[['b','Largura b',100],['h','Altura h',200]]", "ret:[['b','Width b',100],['h','Height h',200]]"),
 ("cir:[['D','Diâmetro D',100]]", "cir:[['D','Diameter D',100]]"),
 ("tub:[['D','Diâmetro externo D',114.3],['t','Espessura t',6]]", "tub:[['D','Outside diameter D',114.3],['t','Wall thickness t',6]]"),
 ("tre:[['B','Largura B',100],['H','Altura H',150],['t','Espessura t',5]]", "tre:[['B','Width B',100],['H','Height H',150],['t','Wall thickness t',5]]"),
 ("I:[['h','Altura total h',200],['bf','Largura da mesa b<sub>f</sub>',100],['tf','Espessura da mesa t<sub>f</sub>',10],['tw','Espessura da alma t<sub>w</sub>',6]]",
  "I:[['h','Overall depth d',200],['bf','Flange width b<sub>f</sub>',100],['tf','Flange thickness t<sub>f</sub>',10],['tw','Web thickness t<sub>w</sub>',6]]"),
 ("T:[['h','Altura total h',200],['bf','Largura da mesa b<sub>f</sub>',150],['tf','Espessura da mesa t<sub>f</sub>',20],['tw','Espessura da alma t<sub>w</sub>',15]]",
  "T:[['h','Overall depth d',200],['bf','Flange width b<sub>f</sub>',150],['tf','Flange thickness t<sub>f</sub>',20],['tw','Stem thickness t<sub>w</sub>',15]]"),
 ("L:[['b','Aba horizontal b',50],['h','Aba vertical h',50],['t','Espessura t',5]]", "L:[['b','Horizontal leg b',50],['h','Vertical leg h',50],['t','Thickness t',5]]"),
 ("U:[['h','Altura h',150],['bf','Largura da aba b<sub>f</sub>',50],['tf','Espessura da aba t<sub>f</sub>',8],['tw','Espessura da alma t<sub>w</sub>',6]]",
  "U:[['h','Depth d',150],['bf','Flange width b<sub>f</sub>',50],['tf','Flange thickness t<sub>f</sub>',8],['tw','Web thickness t<sub>w</sub>',6]]"),
 ("function buildDims(){var t=$('in-t').value; if(t===cur) return; cur=t;\n $('in-dims').innerHTML=DIMS[t].map(function(d){return '<div><label>'+d[1]+' (mm)<input data-k=\"'+d[0]+'\" type=\"number\" step=\"any\" min=\"0\" value=\"'+d[2]+'\"></label></div>';}).join('');",
  "function buildDims(){var t=$('in-t').value,u=$('in-u').value;\n if(u!==USYS){var f=u==='si'?25.4:1/25.4; R.querySelectorAll('#in-dims input,#in-rects input').forEach(function(e){var x=num(e); if(isFinite(x)) e.value=+(x*f).toPrecision(4);}); USYS=u; R.querySelectorAll('.uL').forEach(function(e){e.textContent=UL[u];}); R.querySelectorAll('#in-rects label,#in-dims label').forEach(function(l){l.firstChild.textContent=l.firstChild.textContent.replace(/\\((mm|in)\\)/,'('+UL[u]+')');});}\n if(t===cur) return; cur=t;\n $('in-dims').innerHTML=DIMS[t].map(function(d,i){var val=USYS==='us'?DIMS_US[t][i]:d[2];return '<div><label>'+d[1]+' ('+UL[USYS]+')<input data-k=\"'+d[0]+'\" type=\"number\" step=\"any\" min=\"0\" value=\"'+val+'\"></label></div>';}).join('');"),
 ("d.innerHTML='<div><label>b (mm)<input class=\"b\" type=\"number\" step=\"any\" value=\"'+b+'\"></label></div><div><label>h (mm)<input class=\"h\" type=\"number\" step=\"any\" value=\"'+h+'\"></label></div><div><label>x (mm)<input class=\"xx\" type=\"number\" step=\"any\" value=\"'+x+'\"></label></div><div><label>y (mm)<input class=\"yy\" type=\"number\" step=\"any\" value=\"'+y+'\"></label></div><button type=\"button\" class=\"x\" title=\"Remover\">×</button>';",
  "var u=UL[USYS]; d.innerHTML='<div><label>b ('+u+')<input class=\"b\" type=\"number\" step=\"any\" value=\"'+b+'\"></label></div><div><label>h ('+u+')<input class=\"h\" type=\"number\" step=\"any\" value=\"'+h+'\"></label></div><div><label>x ('+u+')<input class=\"xx\" type=\"number\" step=\"any\" value=\"'+x+'\"></label></div><div><label>y ('+u+')<input class=\"yy\" type=\"number\" step=\"any\" value=\"'+y+'\"></label></div><button type=\"button\" class=\"x\" title=\"Remove\">×</button>';"),
 ("addRect(150,20,0,180); addRect(15,180,67.5,0);\n$('in-add').onclick=function(){addRect(50,10,0,0);calc();};",
  "addRect(6,0.75,0,7.25); addRect(0.5,7.25,2.75,0);\n$('in-add').onclick=function(){if(USYS==='us')addRect(2,0.5,0,0);else addRect(50,10,0,0);calc();};"),
 ("return [rect('Retângulo',0,0,v.b,v.h)]", "return [rect('Rectangle',0,0,v.b,v.h)]"),
 ("return [circ('Círculo',", "return [circ('Circle',"),
 ("throw 'A espessura precisa ser menor que o raio.'; return [circ('Círculo externo',v.D/2,v.D/2,v.D/2),circ('Furo (vazio)',", "throw 'The wall thickness must be less than the radius.'; return [circ('Outer circle',v.D/2,v.D/2,v.D/2),circ('Hole (void)',"),
 ("throw 'A espessura precisa ser menor que metade dos lados.'; return [rect('Retângulo externo',0,0,v.B,v.H),rect('Vazio interno',", "throw 'The wall thickness must be less than half of each side.'; return [rect('Outer rectangle',0,0,v.B,v.H),rect('Inner void',"),
 ("throw 'Confira: 2·t<sub>f</sub> < h e t<sub>w</sub> ≤ b<sub>f</sub>.'; return [rect('Mesa inferior',0,0,v.bf,v.tf),rect('Alma',(v.bf-v.tw)/2,v.tf,v.tw,v.h-2*v.tf),rect('Mesa superior',",
  "throw 'Check: 2·t<sub>f</sub> < d and t<sub>w</sub> ≤ b<sub>f</sub>.'; return [rect('Bottom flange',0,0,v.bf,v.tf),rect('Web',(v.bf-v.tw)/2,v.tf,v.tw,v.h-2*v.tf),rect('Top flange',"),
 ("throw 'Confira: t<sub>f</sub> < h e t<sub>w</sub> ≤ b<sub>f</sub>.'; return [rect('Alma',(v.bf-v.tw)/2,0,v.tw,v.h-v.tf),rect('Mesa',", "throw 'Check: t<sub>f</sub> < d and t<sub>w</sub> ≤ b<sub>f</sub>.'; return [rect('Stem',(v.bf-v.tw)/2,0,v.tw,v.h-v.tf),rect('Flange',"),
 ("throw 'A espessura precisa ser menor que as abas.'; return [rect('Aba vertical',0,0,v.t,v.h),rect('Aba horizontal (sem o canto)',", "throw 'The thickness must be less than the legs.'; return [rect('Vertical leg',0,0,v.t,v.h),rect('Horizontal leg (without the corner)',"),
 ("throw 'Confira: 2·t<sub>f</sub> < h e t<sub>w</sub> < b<sub>f</sub>.'; return [rect('Alma',0,0,v.tw,v.h),rect('Aba inferior',v.tw,0,v.bf-v.tw,v.tf),rect('Aba superior',",
  "throw 'Check: 2·t<sub>f</sub> < d and t<sub>w</sub> < b<sub>f</sub>.'; return [rect('Web',0,0,v.tw,v.h),rect('Bottom flange',v.tw,0,v.bf-v.tw,v.tf),rect('Top flange',"),
 ("out.push(rect('Retângulo '+i,", "out.push(rect('Rectangle '+i,"),
 ("throw 'Adicione ao menos um retângulo.'", "throw 'Add at least one rectangle.'"),
 ("err='Preencha todas as medidas com valores positivos.'", "err='Fill in all dimensions with positive values.'"),
 ("err='Medidas inválidas.'", "err='Invalid dimensions.'"),
 ("textContent='A área resultante precisa ser positiva.'", "textContent='The net area must be positive.'"),
 (" var c4=1e4,c3=1e3,c2=100;\n $('k-A').textContent=nf(A/c2,2)+' cm²';\n $('k-c').textContent=nf((xb-xmin)/10,2)+' ; '+nf((yb-ymin)/10,2)+' cm';\n $('k-Ix').textContent=nfs(Ix/c4)+' cm⁴'; $('k-Iy').textContent=nfs(Iy/c4)+' cm⁴';\n $('k-Wx').textContent=nfs(Ix/(ymax-yb)/c3)+' ; '+nfs(Ix/(yb-ymin)/c3)+' cm³';\n $('k-Wy').textContent=nfs(Iy/(xmax-xb)/c3)+' ; '+nfs(Iy/(xb-xmin)/c3)+' cm³';\n $('k-r').textContent=nf(Math.sqrt(Ix/A)/10,2)+' ; '+nf(Math.sqrt(Iy/A)/10,2)+' cm';",
  " var k1=USYS==='us'?1:10,c4=Math.pow(k1,4),c3=Math.pow(k1,3),c2=k1*k1,uo=USYS==='us'?'in':'cm';\n $('k-A').textContent=nf(A/c2,2)+' '+uo+'²';\n $('k-c').textContent=nf((xb-xmin)/k1,2)+' ; '+nf((yb-ymin)/k1,2)+' '+uo;\n $('k-Ix').textContent=nfs(Ix/c4)+' '+uo+'⁴'; $('k-Iy').textContent=nfs(Iy/c4)+' '+uo+'⁴';\n $('k-Wx').textContent=nfs(Ix/(ymax-yb)/c3)+' ; '+nfs(Ix/(yb-ymin)/c3)+' '+uo+'³';\n $('k-Wy').textContent=nfs(Iy/(xmax-xb)/c3)+' ; '+nfs(Iy/(xb-xmin)/c3)+' '+uo+'³';\n $('k-r').textContent=nf(Math.sqrt(Ix/A)/k1,2)+' ; '+nf(Math.sqrt(Iy/A)/k1,2)+' '+uo;"),
 ("var pr='I<sub>xy</sub> = 0 (seção simétrica): x e y já são os eixos principais';", "var pr='I<sub>xy</sub> = 0 (symmetric section): x and y are already the principal axes';"),
 ("' cm⁴ · I<sub>1</sub> = '+nfs((m+rr)/c4)+' · I<sub>2</sub> = '+nfs((m-rr)/c4)+' cm⁴ · θ = '", "' '+uo+'⁴ · I<sub>1</sub> = '+nfs((m+rr)/c4)+' · I<sub>2</sub> = '+nfs((m-rr)/c4)+' '+uo+'⁴ · θ = '"),
 ("'<tr style=\"font-weight:700\"><td>Total</td>", "'<tr style=\"font-weight:700\"><td>Total</td>"),
 ("I<sub>x</sub> = '+nfs(Ix)+' mm⁴</td><td colspan=\"2\">I<sub>y</sub> = '+nfs(Iy)+' mm⁴</td></tr>'", "I<sub>x</sub> = '+nfs(Ix)+' '+UL[USYS]+'⁴</td><td colspan=\"2\">I<sub>y</sub> = '+nfs(Iy)+' '+UL[USYS]+'⁴</td></tr>'"),
])
left = re.findall(r".{20}(?:cm|mm)[²³⁴]?['\" ].{5}", v.split('<script>')[1])
print('inercia restos:', [x for x in left if 'UL=' not in x and 'uo=' not in x][:8])
open(f'{S}/en/inertia_tool.html', 'w').write(v)
print('inertia ok')
