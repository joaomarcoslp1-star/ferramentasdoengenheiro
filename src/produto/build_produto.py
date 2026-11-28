# Stub: o gerador original da página de vendas não está no repositório.
# Reaproveita a página publicada (site_src/produto/publicado.html) sem alterações.
import os, shutil
def build(m):
    d = m.OUT + "/cai-na-prova"; os.makedirs(d, exist_ok=True)
    shutil.copy(os.path.join(os.path.dirname(__file__), "publicado.html"), d + "/index.html")
    return [("/cai-na-prova/", m.TODAY)]
