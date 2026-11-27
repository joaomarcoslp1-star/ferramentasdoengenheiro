# -*- coding: utf-8 -*-
"""Vídeos 1080x1920 dos exercícios, sincronizados com a narração.
Uso: python3 video.py e1 [e2 ...]   (ou 'all')"""
import asyncio, base64, json, os, re, subprocess, sys
from playwright.async_api import async_playwright
sys.path.insert(0, os.path.dirname(__file__))
from figs import FIGS

AUD = '/home/claude/ferramentasdoengenheiro/src/audio'
OUT = '/home/claude/exer/video'; os.makedirs(OUT, exist_ok=True)
EX = {e['id']: e for e in json.load(open('/home/claude/exer/exercicios.json'))}
RO = json.load(open('/home/claude/exer/roteiros.json'))
LOGO = base64.b64encode(open('/home/claude/site_src/img/logo-192.png', 'rb').read()).decode()
PAUSA = 2.2  # segundos de silêncio extra depois de "pause e tente"
FPS = 30

def tipos(k):
    n = len(RO[k])
    return ['hook', 'enun', 'pause', 's', 's', 's', 's', 'end'] if k == 'e2' else ['hook', 'enun', 'pause', 's', 's', 's', 'tip', 'cta']

def silencios(wav):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', wav, '-af', 'silencedetect=n=-38dB:d=0.14', '-f', 'null', '-'], capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', r)]; en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', r)]
    return list(zip(st, en))

def dur(wav):
    return float(subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', wav], capture_output=True, text=True).stdout)

def fronteiras(k, wav):
    """Início de cada frase: programação dinâmica sobre os silêncios (mesclados), casando a duração de cada trecho com o nº de caracteres."""
    partes = RO[k]; D = dur(wav)
    sil = []
    for a, b in silencios(wav):
        if b > D - 0.2: continue
        if sil and a - sil[-1][1] < 0.15: sil[-1] = (sil[-1][0], b)
        else: sil.append((a, b))
    L = [len(p) + 12 for p in partes]; tot = sum(L); n = len(partes)
    pts = [(0.0, 0.0, 0.0)] + [(a, b, b - a) for a, b in sil] + [(D, D, 0.0)]
    import functools
    @functools.lru_cache(None)
    def best(j, i):  # j: índice do ponto onde começa a frase i; retorna (custo, caminho)
        if i == n - 1:
            d = pts[-1][0] - pts[j][1]; e = D * L[i] / tot
            return (d - e) ** 2 / (e + 3), ()
        res = (1e9, ())
        for m in range(j + 1, len(pts) - 1):
            d = pts[m][0] - pts[j][1]; e = D * L[i] / tot
            c = (d - e) ** 2 / (e + 3) - 0.6 * min(pts[m][2], 0.8)
            if c > 6: 
                if d > e: break
                continue
            sub = best(m, i + 1); 
            if c + sub[0] < res[0]: res = (c + sub[0], (m,) + sub[1])
        return res
    path = best(0, 0)[1]
    return [0.0] + [pts[m][1] for m in path], D

CSS = """*{box-sizing:border-box}body{margin:0;width:1080px;height:1920px;overflow:hidden;background:#0f2742;font-family:Arial,Helvetica,sans-serif;color:#fff;position:relative}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:54px 54px}
.L{position:absolute;left:70px;right:70px}.C{top:240px!important;bottom:360px;display:flex;flex-direction:column;justify-content:center}
.bd{display:inline-block;background:#f28c28;color:#1c2430;font-weight:700;font-size:34px;padding:14px 32px;border-radius:40px}.bd.az{background:#5b9bff}
.tag{display:inline-block;margin-left:12px;font-size:30px;color:#c9d6e6;border:2px solid rgba(255,255,255,.2);padding:11px 22px;border-radius:40px}
h1{font-size:84px;line-height:1.08;margin:34px 0 0;font-weight:800}
.en{font-size:52px;line-height:1.36}.fig svg{width:100%;height:auto}
.alts{font-size:54px;line-height:1.55}.alts b{color:#f9a24b;margin-right:14px}.alts .ok{background:#e8f5ec;color:#123d24;border-radius:14px;padding:0 14px}
.step{display:flex;gap:24px;align-items:flex-start;background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.1);border-radius:24px;padding:30px 34px;margin-top:24px;font-size:46px;line-height:1.36}
.step .n{flex:none;width:64px;height:64px;border-radius:50%;background:#f28c28;color:#1c2430;font-weight:800;display:flex;align-items:center;justify-content:center;font-size:36px}
.ans{background:#e8f5ec;color:#123d24;border-radius:26px;padding:40px 44px;font-size:62px;font-weight:800;line-height:1.3}
.tip{font-size:48px;line-height:1.4;color:#ffd166;margin-top:30px}
.cta{background:rgba(255,255,255,.08);border:3px solid rgba(255,255,255,.14);border-radius:30px;padding:44px;text-align:center}
.foot{position:absolute;left:70px;right:70px;bottom:80px;display:flex;align-items:center;font-size:32px;color:#c9d6e6}.foot img{width:64px;height:64px;border-radius:14px;margin-right:18px}
.cd{position:absolute;left:0;right:0;top:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:center;background:rgba(15,39,66,.86)}
.cd .num{font-size:300px;font-weight:800;color:#f28c28;line-height:1}.cd .tx{font-size:64px;font-weight:800;margin-top:20px}
"""

def html(k, ini, D, ext):
    e = EX[k]; T = tipos(k); conc = e['publico'] == 'concurso'
    fig = FIGS[e['fig']]()
    alts = ''
    if conc:
        alts = "<div class=alts id=alts>" + ''.join(f"<div><span id=alt{i}><b>({'ABCDE'[i]})</b>{a}</span></div>" for i, a in enumerate(e['alts'])) + "</div>"
    steps = ''.join(f"<div class=step id=st{i}><div class=n>{i+1}</div><div>{p}</div></div>" for i, p in enumerate(e['passos']))
    sidx = [i for i, t in enumerate(T) if t == 's']
    tl = dict(ini=ini, D=D, T=T, sidx=sidx, ext=ext, certa=e.get('certa', -1), conc=conc)
    return f"""<html><head><meta charset=utf-8><style>{CSS}</style></head><body><div class=grid></div>
<div class=L style="top:120px"><span class="bd{'' if conc else ' az'}">{e['serie']}</span><span class=tag>{e['materia']}</span></div>
<div class="L C" id=hook><h1>{e['titulo']}</h1><div class=fig style="margin-top:70px">{fig}</div></div>
<div class="L C" id=enun><div class=en>{e['enunciado']}</div><div class=fig id=efig style="margin-top:30px{';max-height:560px' if conc else ''}">{fig}</div>{('<div style=margin-top:30px>'+alts+'</div>') if conc else ''}</div>
<div class="L C" id=sol><div style="font-size:60px;font-weight:800;margin-bottom:10px">Resolução</div>{steps}</div>
<div class="L C" id=fim><div style="font-size:60px;font-weight:800;margin-bottom:24px">Resposta</div><div class=ans>{e['resposta']}</div><div class=tip>{'⚠ ' if conc else '💡 '}{e['dica']}</div>
<div class=cta id=cta style="margin-top:60px"><div style="font-size:54px;font-weight:800">Calculadora e mais exercícios grátis</div><div style="font-size:44px;color:#f9a24b;font-weight:700;margin-top:12px">🔗 link na bio</div></div></div>
<div class=cd id=cd><div class=num id=cdn>3</div><div class=tx>Pause e tente!</div></div>
<div class=foot><img src='data:image/png;base64,{LOGO}'>@ferramentasdoengenheiro</div>
<script>
var TL={json.dumps(tl)};
function cl(v,a,b){{return Math.max(a,Math.min(b,v));}}
function at(i){{var t=TL.ini[i]; if(i>2) t+=TL.ext; return t;}}
function op(t,a,b){{return cl((t-a)/0.35,0,1)*cl((b-t)/0.35,0,1);}}
var $=function(i){{return document.getElementById(i)}};
window.render=function(t){{
  var n=TL.T.length, END=TL.D+TL.ext+0.6;
  var tEnun=at(1), tPause=at(2), tSol=at(3), lastS=TL.sidx[TL.sidx.length-1], tFim=(lastS+1<n)?at(lastS+1):END;
  $('hook').style.opacity=op(t,-1,tEnun);
  var solStart=tSol; $('enun').style.opacity=op(t,tEnun-0.2,solStart);
  // contagem regressiva no trecho da pausa + silêncio extra
  var pEnd=at(3); var cdOn=(t>=tPause+0.4&&t<pEnd-0.1); $('cd').style.opacity=cdOn?cl((t-tPause-0.4)/0.25,0,1)*cl((pEnd-0.1-t)/0.25,0,1):0;
  $('cdn').textContent=Math.max(1,Math.ceil((pEnd-0.1-t)/((pEnd-tPause-0.5)/3)));
  $('sol').style.opacity=op(t,tSol-0.2,tFim);
  TL.sidx.forEach(function(si,j){{var s=$('st'+j); if(!s)return; var a=cl((t-at(si))/0.35,0,1); s.style.opacity=a; s.style.transform='translateY('+(1-a)*30+'px)';}});
  // passos extras (sem parte de narração própria) aparecem com o último
  for(var j=TL.sidx.length;$('st'+j);j++){{var a=cl((t-at(lastS))/0.35,0,1);$('st'+j).style.opacity=a;}}
  $('fim').style.opacity=op(t,tFim-0.2,99);
  var tCta=(TL.T[n-1]==='cta')?at(n-1):tFim+0.8; $('cta').style.opacity=cl((t-tCta)/0.4,0,1);
  if(TL.conc){{ for(var i=0;i<5;i++){{var el=$('alt'+i); if(el) el.className=(t>=at(lastS)&&i===TL.certa)?'ok':'';}} }}
}};
render(0);
</script></body></html>"""

async def render(k):
    wav = f"{AUD}/narracao-ex-{k}.wav"; ini, D = fronteiras(k, wav); ext = PAUSA
    open(f"{OUT}/{k}.html", 'w').write(html(k, ini, D, ext))
    TOT = D + ext + 1.2
    tmp = f"{OUT}/tmp_{k}.mp4"
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                           "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", tmp], stdin=subprocess.PIPE)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg = await b.new_page(viewport={"width": 1080, "height": 1920})
        await pg.goto(f"file://{OUT}/{k}.html")
        for i in range(int(TOT * FPS)):
            await pg.evaluate(f"render({i/FPS})"); ff.stdin.write(await pg.screenshot(type="jpeg", quality=90))
        await b.close()
    ff.stdin.close(); assert ff.wait() == 0
    # áudio: narração com silêncio extra após a pausa + trilha com ducking
    cut = ini[3]
    mus = f"{OUT}/mus_{k}.wav"
    subprocess.run(["python3", "/home/claude/reel/musica.py", str(TOT)], check=True, capture_output=True); os.replace("/home/claude/reel/musica.wav", mus)
    fc = (f"[2:a]aresample=44100,aformat=channel_layouts=stereo,volume=1.5,asplit=2[a0][a1];"
          f"[a0]atrim=0:{cut},asetpts=PTS-STARTPTS[p1];[a1]atrim={cut},asetpts=PTS-STARTPTS[p2];"
          f"aevalsrc=0:d={ext}:s=44100:c=stereo[z];[p1][z][p2]concat=n=3:v=0:a=1,apad=whole_dur={TOT},asplit=2[v1][v2];"
          f"[1:a]volume=0.30[m];[m][v1]sidechaincompress=threshold=0.02:ratio=8:attack=15:release=350[md];"
          f"[md][v2]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]")
    fin = f"{OUT}/tmp2_{k}.mp4"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", tmp, "-i", mus, "-i", wav, "-filter_complex", fc, "-map", "0:v", "-map", "[a]",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", fin], check=True)
    os.replace(fin, f"{OUT}/{k}.mp4"); os.remove(tmp)
    print(k, 'ok', round(TOT, 1), 's', [round(x, 1) for x in ini])

ids = sys.argv[1:]
if ids == ['all']: ids = list(EX)
for k in ids: asyncio.run(render(k))
