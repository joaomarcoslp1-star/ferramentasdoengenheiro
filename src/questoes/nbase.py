# -*- coding: utf-8 -*-
"""Base das questões novas (lote 2 em diante).

Cada questão numérica é definida pelo valor CERTO (calculado em Python) e por
distratores (erros típicos). A função montar() escolhe a letra do gabarito
(rodízio A-E por matéria), completa os distratores se faltar valor de um lado
e põe as alternativas em ordem crescente. Questões conceituais: certa + 4 erradas.
"""
import math

RAW = []  # questões ainda sem posição de gabarito

def br(v, d=None):
    """Formata número no padrão brasileiro: 2.400 · 0,552 · 1.234,5"""
    if d is None:
        a = abs(v)
        d = 0 if a >= 100 else 1 if a >= 10 else 2 if a >= 1 else 3
    s = f"{abs(v):,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if abs(v) < 10000 and d == 0 and abs(v) >= 1000:
        pass
    return ("−" if v < 0 else "") + s

def num(i, mat, ass, en, certo, distr, res, d=None, fmt=None):
    RAW.append(dict(tipo="num", id=i, mat=mat, ass=ass, en=en, certo=certo, distr=list(distr), res=res, d=d, fmt=fmt))

def con(i, mat, ass, en, certo, erradas, res):
    assert len(erradas) == 4, i
    RAW.append(dict(tipo="con", id=i, mat=mat, ass=ass, en=en, certo=certo, erradas=list(erradas), res=res))

FILL_DOWN = [0.5, 0.8, 0.25, 0.4, 0.1]
FILL_UP = [2, 1.25, 4, 1.5, 10]

def _pos_num(x, alvo):
    f = x["fmt"] or (lambda v: br(v, x["d"]))
    c = x["certo"]; cs = f(c)
    seen = {cs}
    baixo, alto = [], []
    for v in x["distr"]:
        s = f(v)
        if s in seen: continue
        seen.add(s)
        (baixo if v < c else alto).append(v)
    # completa com valores de preenchimento se faltar de algum lado
    for fac in FILL_DOWN:
        if len(baixo) >= 4: break
        v = c * fac; s = f(v)
        if s not in seen and v > 0: seen.add(s); baixo.append(v)
    for fac in FILL_UP:
        if len(alto) >= 4: break
        v = c * fac; s = f(v)
        if s not in seen: seen.add(s); alto.append(v)
    # a letra alvo exige 'alvo' valores abaixo e 4-alvo acima; se não houver, usa a mais próxima possível
    nb = min(alvo, len(baixo)); na = 4 - nb
    if na > len(alto): na = len(alto); nb = 4 - na
    escolhidos = baixo[:nb] + alto[:na]   # os primeiros da lista são os distratores mais importantes
    vals = sorted(escolhidos + [c])
    alts = [f(v) for v in vals]
    assert len(set(alts)) == 5, (x["id"], alts)
    return alts, vals.index(c)

def montar():
    out = []
    cont = {}
    for x in RAW:
        k = cont.get(x["mat"], 0); cont[x["mat"]] = k + 1
        alvo = (k * 3 + len(x["mat"])) % 5   # rodízio: distribui as letras dentro de cada matéria
        if x["tipo"] == "num":
            alts, g = _pos_num(x, alvo)
        else:
            alts = list(x["erradas"]); alts.insert(alvo, x["certo"]); g = alvo
        out.append(dict(id=x["id"], mat=x["mat"], ass=x["ass"], en=x["en"], alts=alts, gab=g, res=x["res"]))
    return out
