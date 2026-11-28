# -*- coding: utf-8 -*-
import json, html, sys
import q2, q3, q4
from q1 import Q
from collections import Counter

# Rebalanceia o gabarito (troca alternativas em questões conceituais)
MOVES = {"MEC-C02": "A", "MEC-M01": "A", "MEC-M07": "A", "MEC-T04": "A", "MEC-M08": "A", "MEC-R06": "E", "MEC-T05": "E"}
for x in Q:
    if x["id"] in MOVES:
        t = "ABCDE".index(MOVES[x["id"]]); g = x["gab"]
        x["alts"][g], x["alts"][t] = x["alts"][t], x["alts"][g]; x["gab"] = t
from novas import NOVAS
Q.extend(NOVAS)
print(Counter("ABCDE"[x["gab"]] for x in Q), file=sys.stderr)

MATS = list(dict.fromkeys(x["mat"] for x in Q))

CSS = r"""
#fde-q{--az:#1f6feb;--la:#f28c28;--bo:#dde3ec;--su:#5a6575;--ok:#1a7f37;--er:#cf222e;font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:#1c2430;line-height:1.55;max-width:860px;margin:0 auto}
#fde-q *{box-sizing:border-box}
#fde-q button{font-family:inherit;cursor:pointer}
#fde-q .card{background:#f6f8fb;border:1px solid var(--bo);border-radius:12px;padding:16px;margin:0 0 14px}
#fde-q .card h3{margin:0 0 8px;font-size:1.1rem}
#fde-q .kp{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:10px}
#fde-q .kp div{background:#fff;border:1px solid var(--bo);border-radius:8px;padding:8px 10px}
#fde-q .kp span{display:block;font-size:.72rem;color:var(--su);font-weight:600}
#fde-q .kp b{font-size:1.2rem}
#fde-q .bars{display:grid;gap:5px;margin:6px 0 10px}
#fde-q .bar{display:grid;grid-template-columns:190px 1fr 92px;gap:8px;align-items:center;font-size:.82rem}
#fde-q .bar i{display:block;height:10px;border-radius:5px;background:#e3e8ef;overflow:hidden}
#fde-q .bar i em{display:block;height:100%;background:var(--az)}
#fde-q .bar small{color:var(--su);text-align:right}
#fde-q .btns{display:flex;flex-wrap:wrap;gap:6px}
#fde-q .b{border:1px solid #c4ccd8;background:#fff;border-radius:8px;padding:7px 11px;font-size:.85rem;color:#1c2430}
#fde-q .b:hover{border-color:var(--az);color:var(--az)}
#fde-q .b.pri{background:var(--az);border-color:var(--az);color:#fff}
#fde-q .b.lar{background:var(--la);border-color:var(--la);color:#1c2430;font-weight:700}
#fde-q .ctl{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:8px;margin-bottom:10px}
#fde-q label{font-size:.75rem;font-weight:600;color:#3a4452}
#fde-q select{width:100%;padding:7px 8px;border:1px solid #c4ccd8;border-radius:8px;font-size:.9rem;background:#fff;margin-top:2px;font-family:inherit}
#fde-q .bar-top{position:sticky;top:0;z-index:5;background:#0f2742;color:#fff;border-radius:10px;padding:8px 12px;margin:0 0 12px;display:flex;justify-content:space-between;align-items:center;gap:10px;font-size:.88rem}
#fde-q .bar-top b{color:#f9a24b}
#fde-q .bar-top .b{padding:5px 10px}
#fde-q .fq{background:#fff;border:1px solid var(--bo);border-radius:12px;padding:16px;margin:0 0 14px}
#fde-q .fq.hide{display:none}
#fde-q .fq header{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:.78rem;color:var(--su);margin-bottom:8px}
#fde-q .fq header .n{background:#0f2742;color:#fff;border-radius:6px;padding:2px 8px;font-weight:700}
#fde-q .fq header .tg{border:1px solid var(--bo);border-radius:6px;padding:1px 7px}
#fde-q .fq header .st{margin-left:auto;font-weight:600}
#fde-q .en{margin:0 0 10px;font-size:1rem}
#fde-q .alts{list-style:none;margin:0;padding:0;display:grid;gap:6px}
#fde-q .alts li{display:grid;grid-template-columns:1fr 34px;gap:6px}
#fde-q .alt{display:grid;grid-template-columns:30px 1fr;gap:8px;align-items:start;text-align:left;background:#f6f8fb;border:1px solid var(--bo);border-radius:8px;padding:8px 10px;font-size:.95rem;color:#1c2430;line-height:1.45}
#fde-q .alt b{display:inline-flex;width:26px;height:26px;border-radius:50%;border:1px solid #c4ccd8;align-items:center;justify-content:center;background:#fff;font-size:.85rem}
#fde-q .alt:hover{border-color:var(--az)}
#fde-q .alt.sel{border-color:var(--az);background:#eef4ff}
#fde-q .alt.sel b{background:var(--az);color:#fff;border-color:var(--az)}
#fde-q .alt.cut span{text-decoration:line-through;color:#9aa5b1}
#fde-q .alt.ok{border-color:var(--ok);background:#e9f7ee}
#fde-q .alt.ok b{background:var(--ok);color:#fff;border-color:var(--ok)}
#fde-q .alt.er{border-color:var(--er);background:#ffebe9}
#fde-q .alt.er b{background:var(--er);color:#fff;border-color:var(--er)}
#fde-q .cut-b{border:1px solid var(--bo);background:#fff;border-radius:8px;color:var(--su);font-size:.9rem}
#fde-q .cut-b:hover{color:var(--er);border-color:var(--er)}
#fde-q .act{display:flex;gap:8px;align-items:center;margin-top:10px}
#fde-q .res{margin-top:12px;border-top:1px dashed var(--bo);padding-top:10px;font-size:.93rem}
#fde-q .fb{font-weight:700;margin:0 0 6px}
#fde-q .fb.ok{color:var(--ok)}
#fde-q .fb.er{color:var(--er)}
#fde-q .muted{color:var(--su);font-size:.8rem}
#fde-q .resumo{border-left:5px solid var(--la)}
@media(max-width:640px){#fde-q .kp{grid-template-columns:1fr 1fr}#fde-q .ctl{grid-template-columns:1fr}#fde-q .bar{grid-template-columns:1fr 70px;}#fde-q .bar i{grid-column:1/-1;order:3}}
"""

def esc_attr(s): return html.escape(s, quote=True)

def render_q(x):
    alts = "".join(
        f'<li><button type="button" class="alt" data-i="{i}"><b>{"ABCDE"[i]}</b><span>{a}</span></button>'
        f'<button type="button" class="cut-b" title="Riscar alternativa" aria-label="Riscar alternativa {"ABCDE"[i]}">✂</button></li>'
        for i, a in enumerate(x["alts"]))
    return (f'<article class="fq" id="{x["id"]}" data-mat="{esc_attr(x["mat"])}" data-g="{x["gab"]}">'
            f'<header><span class="n">Questão</span><span class="tg">{x["mat"]}</span><span class="tg">{x["ass"]}</span>'
            f'<span class="tg">Inédita · estilo Cesgranrio</span><span class="st"></span></header>'
            f'<p class="en">{x["en"]}</p><ol class="alts">{alts}</ol>'
            f'<div class="act"><button type="button" class="b pri resp">Responder</button><span class="muted qst"></span></div>'
            f'<div class="res" hidden><p class="fb"></p><div><b>Resolução:</b> {x["res"]}</div>'
            f'<p class="muted">Gabarito: {"ABCDE"[x["gab"]]} · Código {x["id"]}</p></div></article>')

JS = r"""
(function(){
var R=document.getElementById('fde-q'); if(!R) return;
var KEY='fde_quest_v1', META=206; // segundos por questão (70 em 4 h)
function $(s,c){return (c||R).querySelector(s);} function $$(s,c){return [].slice.call((c||R).querySelectorAll(s));}
function load(){try{var d=JSON.parse(localStorage.getItem(KEY)||'{}');d.h=d.h||[];return d;}catch(e){return {h:[]};}}
function save(d){try{localStorage.setItem(KEY,JSON.stringify(d));}catch(e){}}
var DB=load(), QS=$$('.fq'), MATS=[], mode='estudo', prova=null;
QS.forEach(function(q){if(MATS.indexOf(q.dataset.mat)<0)MATS.push(q.dataset.mat);});
var MATALL={}; QS.forEach(function(q){MATALL[q.id]=q.dataset.mat;});
function pct(a,b){return b?Math.round(100*a/b)+'%':'–';}
function fmt(s){s=Math.max(0,Math.round(s));var h=Math.floor(s/3600),m=Math.floor(s%3600/60),x=s%60;return (h?h+'h':'')+(h&&m<10?'0':'')+m+'min'+(x<10?'0':'')+x+'s';}
function last(id){for(var i=DB.h.length-1;i>=0;i--)if(DB.h[i][0]===id)return DB.h[i];return null;}
function record(id,ok,ch,secs,md){DB.h.push([id,ok?1:0,ch,Math.round(secs),Date.now(),md]); if(DB.h.length>5000)DB.h=DB.h.slice(-5000); save(DB);}
/* ---------- painel ---------- */
function painel(){
 var h=DB.h.filter(function(r){return MATALL[r[0]];}), tot=h.length, ac=0, dist={}, secs=0, dias={}, pm={};
 MATS.forEach(function(m){pm[m]={n:0,a:0,q:{}};});
 h.forEach(function(r){ac+=r[1];secs+=r[3];dist[r[0]]=1;dias[new Date(r[4]).toDateString()]=1;var m=MATALL[r[0]];if(m){pm[m].n++;pm[m].a+=r[1];pm[m].q[r[0]]=1;}});
 // sequência de dias
 var seq=0,d=new Date(); for(;;){if(dias[d.toDateString()]){seq++;d.setDate(d.getDate()-1);}else{if(seq===0&&d.toDateString()===new Date().toDateString()){d.setDate(d.getDate()-1);if(dias[d.toDateString()])continue;}break;}}
 $('#k-res').textContent=Object.keys(dist).length+' / '+QS.length;
 $('#k-ac').textContent=pct(ac,tot);
 $('#k-tm').textContent=tot?fmt(secs/tot):'–';
 $('#k-sq').textContent=seq+(seq===1?' dia':' dias');
 $('#k-bars').innerHTML=MATS.map(function(m){var p=pm[m],v=p.n?Math.round(100*p.a/p.n):0,qt=QS.filter(function(q){return q.dataset.mat===m;}).length;
  return '<div class="bar"><span>'+m+'</span><i><em style="width:'+v+'%;background:'+(p.n?(v>=70?'#1a7f37':v>=50?'#f28c28':'#cf222e'):'#e3e8ef')+'"></em></i><small>'+(p.n?v+'% · '+Object.keys(p.q).length+'/'+qt:'0/'+qt)+'</small></div>';}).join('');
 var fracas=MATS.filter(function(m){return pm[m].n>=3;}).sort(function(a,b){return pm[a].a/pm[a].n-pm[b].a/pm[b].n;});
 $('#k-dica').textContent=fracas.length?'Seu ponto mais fraco agora: '+fracas[0]+' ('+pct(pm[fracas[0]].a,pm[fracas[0]].n)+' de acerto). Use o filtro para treinar essa matéria.':'Responda algumas questões para ver suas estatísticas por matéria.';
 QS.forEach(function(q){var l=last(q.id),st=$('.st',q);var n=0,a=0;h.forEach(function(r){if(r[0]===q.id){n++;a+=r[1];}});
  st.textContent=l?(l[1]?'✔ acertou':'✘ errou')+' da última vez · '+a+'/'+n:''; st.style.color=l?(l[1]?'#1a7f37':'#cf222e'):'';});
 topo();
}
/* ---------- filtros ---------- */
var sm=$('#f-mat'); MATS.forEach(function(m){var o=document.createElement('option');o.value=m;o.textContent=m+' ('+QS.filter(function(q){return q.dataset.mat===m;}).length+')';sm.appendChild(o);});
function visiveis(){return QS.filter(function(q){return !q.classList.contains('hide');});}
function filtrar(){
 var m=sm.value, s=$('#f-sit').value;
 QS.forEach(function(q){var l=last(q.id),show=(!m||q.dataset.mat===m);
  if(s==='nao')show=show&&!l; if(s==='err')show=show&&l&&!l[1];
  q.classList.toggle('hide',!show);});
 numerar(); topo();
}
function numerar(){var i=0;QS.forEach(function(q){if(!q.classList.contains('hide'))$('.n',q).textContent='Questão '+(++i);});}
function embaralhar(){var box=$('#qbox'),a=QS.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;}a.forEach(function(q){box.appendChild(q);});QS=a;numerar();}
sm.onchange=filtrar; $('#f-sit').onchange=filtrar;
$('#b-emb').onclick=embaralhar;
$('#b-err').onclick=function(){$('#f-sit').value='err';filtrar();$('#qbox').scrollIntoView({behavior:'smooth'});};
/* ---------- tempo por questão ---------- */
var t0={}; if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&!t0[e.target.id])t0[e.target.id]=Date.now();});},{threshold:.5});QS.forEach(function(q){io.observe(q);});}
function gasto(id){return t0[id]?(Date.now()-t0[id])/1000:0;}
/* ---------- responder ---------- */
QS.forEach(function(q){
 $$('.alt',q).forEach(function(b){b.onclick=function(){if(q.dataset.done)return;$$('.alt',q).forEach(function(x){x.classList.remove('sel');});b.classList.add('sel');b.classList.remove('cut');if(!t0[q.id])t0[q.id]=Date.now();if(prova)q.dataset.ch=b.dataset.i;topo();};});
 $$('.cut-b',q).forEach(function(c,i){c.onclick=function(){if(q.dataset.done)return;var a=$$('.alt',q)[i];a.classList.toggle('cut');if(a.classList.contains('cut'))a.classList.remove('sel');};});
 $('.resp',q).onclick=function(){
  var s=$('.alt.sel',q); if(!s){$('.qst',q).textContent='Escolha uma alternativa.';return;}
  corrigir(q,+s.dataset.i,true);
 };
});
function corrigir(q,ch,grava){
 var g=+q.dataset.g, ok=ch===g, secs=gasto(q.id);
 q.dataset.done=1; q.dataset.ok=ok?1:0; $$('.alt',q).forEach(function(a,i){a.classList.remove('sel');if(i===g)a.classList.add('ok');else if(i===ch)a.classList.add('er');});
 var fb=$('.fb',q); fb.className='fb '+(ok?'ok':'er');
 fb.textContent=ch<0?'Em branco. A resposta certa é '+'ABCDE'[g]+'.':ok?'Você acertou!':'Você marcou '+'ABCDE'[ch]+'. A resposta certa é '+'ABCDE'[g]+'.';
 $('.res',q).hidden=false; $('.resp',q).hidden=true;
 if(secs>=1)$('.qst',q).textContent='Tempo: '+fmt(secs)+(secs>META?' (acima da média de prova, '+fmt(META)+')':'');
 if(grava&&ch>=0)record(q.id,ok,ch,secs,prova?'p':'e');
 if(!prova)painel();
 return ok;
}
function reabrir(q){delete q.dataset.done;delete q.dataset.ch;delete q.dataset.ok;$$('.alt',q).forEach(function(a){a.classList.remove('ok','er','sel','cut');});$('.res',q).hidden=true;$('.resp',q).hidden=(mode==='prova');$('.qst',q).textContent='';t0[q.id]=0;}
$('#b-reset-q').onclick=function(){QS.forEach(reabrir);filtrar();};
/* ---------- modo prova ---------- */
var tick=null;
$('#f-modo').onchange=function(){mode=this.value;$('#prova-cfg').hidden=mode!=='prova';QS.forEach(function(q){$('.resp',q).hidden=mode==='prova'||!!q.dataset.done;});};
$('#b-ini').onclick=function(){
 var n=$('#f-n').value, vis=visiveis(); QS.forEach(reabrir);
 if(n!=='todas'){embaralhar();vis=visiveis();var k=+n;vis.forEach(function(q,i){if(i>=k)q.classList.add('hide');});vis=visiveis();}
 numerar(); QS.forEach(function(q){$('.resp',q).hidden=true;});
 prova={ini:Date.now(),lim:vis.length*META,qs:vis.map(function(q){return q.id;})};
 $('#b-fim').hidden=false; $('#resumo').hidden=true; clearInterval(tick); tick=setInterval(topo,1000); topo();
 $('#qbox').scrollIntoView({behavior:'smooth'});
};
$('#b-fim').onclick=function(){
 if(!prova)return; clearInterval(tick);
 var tot=prova.qs.length, ac=0, br=0, pm={}, dur=(Date.now()-prova.ini)/1000;
 prova.qs.forEach(function(id){var q=document.getElementById(id),ch=q.dataset.ch===undefined?-1:+q.dataset.ch,m=q.dataset.mat;pm[m]=pm[m]||[0,0];pm[m][1]++;
  if(ch<0)br++; var ok=corrigir(q,ch,true); if(ok){ac++;pm[m][0]++;}});
 var p=prova; prova=null; $('#b-fim').hidden=true; painel();
 var txt='Fiz '+ac+'/'+tot+' ('+pct(ac,tot)+') no simulado de Engenharia Mecânica estilo Cesgranrio (Petrobras/Transpetro) do Ferramentas do Engenheiro. Duvido você bater: '+location.href.split('#')[0];
 $('#resumo').innerHTML='<h3>Resultado do simulado</h3><div class="kp"><div><span>Acertos</span><b>'+ac+' / '+tot+'</b></div><div><span>Aproveitamento</span><b>'+pct(ac,tot)+'</b></div><div><span>Em branco</span><b>'+br+'</b></div><div><span>Tempo</span><b>'+fmt(dur)+'</b></div></div>'+
  '<div class="bars">'+Object.keys(pm).map(function(m){var v=Math.round(100*pm[m][0]/pm[m][1]);return '<div class="bar"><span>'+m+'</span><i><em style="width:'+v+'%"></em></i><small>'+pm[m][0]+'/'+pm[m][1]+'</small></div>';}).join('')+'</div>'+
  '<p class="muted">As resoluções de todas as questões já estão abertas abaixo. Meta de treino: passar de 70% de acerto com o tempo de prova.</p>'+
  '<div class="btns"><a class="b lar" target="_blank" rel="noopener" href="https://wa.me/?text='+encodeURIComponent(txt)+'">Compartilhar no WhatsApp</a><button type="button" class="b" id="b-err2">Refazer as que errei</button></div>';
 $('#resumo').hidden=false; $('#resumo').scrollIntoView({behavior:'smooth'});
 $('#b-err2').onclick=function(){QS.forEach(reabrir);$('#f-modo').value='estudo';mode='estudo';$('#prova-cfg').hidden=true;$('#f-sit').value='err';filtrar();QS.forEach(function(q){$('.resp',q).hidden=false;});$('#qbox').scrollIntoView({behavior:'smooth'});};
};
function topo(){
 var vis=visiveis(), resp=vis.filter(function(q){return q.dataset.done||q.dataset.ch!==undefined;}).length;
 var t=$('#topo-txt');
 if(prova){var rest=prova.lim-(Date.now()-prova.ini)/1000;t.innerHTML='Simulado · marcadas <b>'+vis.filter(function(q){return q.dataset.ch!==undefined;}).length+'/'+vis.length+'</b> · tempo restante <b>'+fmt(rest)+'</b>';if(rest<=0)$('#b-fim').click();}
 else{var ac=vis.filter(function(q){return q.dataset.ok==='1';}).length;t.innerHTML='Respondidas <b>'+resp+'/'+vis.length+'</b> · acertos nesta sessão <b>'+ac+'</b>';}
}
/* ---------- exportar / importar / zerar ---------- */
$('#b-exp').onclick=function(){var a=document.createElement('a');a.href=URL.createObjectURL(new Blob([JSON.stringify(DB)],{type:'application/json'}));a.download='meu-desempenho-ferramentas-do-engenheiro.json';document.body.appendChild(a);a.click();a.remove();};
$('#b-imp').onclick=function(){$('#f-imp').click();};
$('#f-imp').onchange=function(){var f=this.files[0];if(!f)return;var r=new FileReader();r.onload=function(){try{var d=JSON.parse(r.result),seen={};DB.h.concat(d.h||[]).forEach(function(x){seen[x[0]+'|'+x[4]]=x;});DB.h=Object.keys(seen).map(function(k){return seen[k];}).sort(function(a,b){return a[4]-b[4];});save(DB);painel();$('#k-dica').textContent='Progresso importado com sucesso.';}catch(e){$('#k-dica').textContent='Arquivo inválido.';}};r.readAsText(f);};
$('#b-zer').onclick=function(){if(confirm('Apagar todo o seu histórico de questões neste navegador?')){DB={h:[]};save(DB);QS.forEach(reabrir);painel();}};
numerar(); painel();
})();
"""

def page(sub=None):
    sub = sub or Q
    qs = "".join(render_q(x) for x in sub)
    return f"""<div id="fde-q"><style>{CSS}</style>
<div class="card" id="painel"><h3>📊 Meu desempenho</h3>
<div class="kp"><div><span>Questões respondidas</span><b id="k-res">–</b></div><div><span>Acerto geral</span><b id="k-ac">–</b></div><div><span>Tempo médio/questão</span><b id="k-tm">–</b></div><div><span>Sequência de estudo</span><b id="k-sq">–</b></div></div>
<div class="bars" id="k-bars"></div>
<p class="muted" id="k-dica"></p>
<div class="btns"><button type="button" class="b" id="b-err">Refazer as que errei</button><button type="button" class="b" id="b-exp">Exportar progresso</button><button type="button" class="b" id="b-imp">Importar progresso</button><button type="button" class="b" id="b-zer">Zerar histórico</button><input type="file" id="f-imp" accept=".json,application/json" hidden></div>
<p class="muted">Seu histórico fica salvo só neste navegador, sem cadastro. Para continuar em outro aparelho, use Exportar e Importar.</p></div>
<div class="card"><h3>⚙️ Como você quer estudar?</h3>
<div class="ctl"><label>Matéria<select id="f-mat"><option value="">Todas as matérias ({len(sub)})</option></select></label>
<label>Questões<select id="f-sit"><option value="">Todas</option><option value="nao">Não respondidas</option><option value="err">Que errei por último</option></select></label>
<label>Modo<select id="f-modo"><option value="estudo">Estudo (corrige na hora)</option><option value="prova">Simulado cronometrado</option></select></label></div>
<div id="prova-cfg" hidden><div class="ctl"><label>Nº de questões<select id="f-n"><option value="10">10 sorteadas (34 min)</option><option value="20">20 sorteadas (1h09)</option><option value="35">35 sorteadas (2h)</option><option value="todas">Todas as filtradas</option></select></label></div>
<p class="muted">Tempo de prova da Cesgranrio: cerca de 3min26s por questão (70 questões em 4 horas). A correção sai só no final, como na prova.</p></div>
<div class="btns"><button type="button" class="b" id="b-emb">🔀 Embaralhar</button><button type="button" class="b" id="b-reset-q">Limpar respostas da tela</button><button type="button" class="b lar" id="b-ini" style="display:none"></button></div></div>
<div class="bar-top"><span id="topo-txt"></span><span><button type="button" class="b lar" id="b-fim" hidden>Finalizar e corrigir</button></span></div>
<div class="card resumo" id="resumo" hidden></div>
<div id="qbox">{qs}</div>
<script>{JS}</script>
<script>(function(){{var m=document.getElementById('f-modo'),b=document.getElementById('b-ini');function u(){{b.style.display=m.value==='prova'?'':'none';b.textContent='▶ Iniciar simulado';}}m.addEventListener('change',u);u();}})();</script>
</div>"""

if __name__ == "__main__":
    open("simulado_tool.html", "w").write(page())
    json.dump(Q, open("questoes.json", "w"), ensure_ascii=False, indent=1)
    print("ok", file=sys.stderr)
