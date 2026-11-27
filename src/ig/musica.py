"""Trilha de fundo original (sem direitos autorais): batida leve e acordes, 100 BPM."""
import numpy as np, wave, sys

SR = 44100
DUR = float(sys.argv[1]) if len(sys.argv) > 1 else 33.0
BPM = 100
beat = 60 / BPM
n = int(SR * DUR)
t = np.arange(n) / SR
mix = np.zeros(n)
rng = np.random.default_rng(7)


def add(sig, start):
    i = int(start * SR)
    if i >= n:
        return
    j = min(n, i + len(sig))
    mix[i:j] += sig[: j - i]


def env(length, a=0.005, r=0.2):
    k = np.arange(int(length * SR)) / SR
    e = np.minimum(1, k / a) * np.exp(-k / r)
    return e


def lowpass(x, alpha):
    y = np.zeros_like(x)
    acc = 0.0
    for i, v in enumerate(x):
        acc += alpha * (v - acc)
        y[i] = acc
    return y


# kick
kl = 0.35
kt = np.arange(int(kl * SR)) / SR
kick = np.sin(2 * np.pi * (50 + 90 * np.exp(-kt * 30)) * kt) * np.exp(-kt * 9)
# hihat
hl = 0.06
hat = rng.standard_normal(int(hl * SR)) * np.exp(-np.arange(int(hl * SR)) / SR * 70)
hat = hat - lowpass(hat, 0.3)
# snare/clap suave
sl = 0.18
snare = rng.standard_normal(int(sl * SR)) * np.exp(-np.arange(int(sl * SR)) / SR * 22)
snare = lowpass(snare, 0.25)

# progressão Am - F - C - G (1 compasso cada)
CH = [[57, 60, 64], [53, 57, 60], [48, 55, 60], [55, 59, 62]]
BASS = [45, 41, 48, 43]
f = lambda m: 440 * 2 ** ((m - 69) / 12)
bar = 4 * beat
nbars = int(DUR / bar) + 1
for b in range(nbars):
    t0 = b * bar
    ch = CH[b % 4]
    # pad (seno + 2º harmônico, ataque lento)
    L = bar + 0.3
    k = np.arange(int(L * SR)) / SR
    pe = np.minimum(1, k / 0.4) * np.minimum(1, (L - k) / 0.4)
    pad = sum(np.sin(2 * np.pi * f(m) * k) + 0.25 * np.sin(2 * np.pi * 2 * f(m) * k) for m in ch) * pe
    add(pad * 0.06, t0)
    # baixo
    for q in range(4):
        bl = beat * 0.9
        kb = np.arange(int(bl * SR)) / SR
        add(np.sin(2 * np.pi * f(BASS[b % 4]) * kb) * np.exp(-kb * 3) * 0.22, t0 + q * beat)
    # arpejo pluck nas colcheias
    for q in range(8):
        m = ch[[0, 1, 2, 1][q % 4]] + 12
        pl = 0.4
        kp = np.arange(int(pl * SR)) / SR
        add(np.sin(2 * np.pi * f(m) * kp) * np.exp(-kp * 9) * 0.05, t0 + q * beat / 2)
    # bateria (entra a partir do 2º compasso)
    if b >= 1:
        for q in range(4):
            add(kick * 0.55, t0 + q * beat)
            if q in (1, 3):
                add(snare * 0.18, t0 + q * beat)
        for q in range(8):
            add(hat * (0.10 if q % 2 else 0.06), t0 + q * beat / 2)

# fade in/out e normalização
fi = np.minimum(1, t / 1.0)
fo = np.minimum(1, (DUR - t) / 2.0)
mix *= fi * fo
mix /= np.max(np.abs(mix)) + 1e-9
mix *= 0.8
st = np.stack([mix, mix], 1)
with wave.open("/home/claude/reel/musica.wav", "w") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((st * 32767).astype(np.int16).tobytes())
print("ok", DUR)
