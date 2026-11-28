#!/bin/bash
# Uso: publicar.sh "mensagem do commit"
# Numa sessão nova: clonar o repositório em /home/claude/ferramentasdoengenheiro e rodar
#   bash /home/claude/ferramentasdoengenheiro/src/publicar.sh --preparar
# para recriar /home/claude/site_src a partir de src/ (e as capas a partir de docs/img).
set -e
R=/home/claude/ferramentasdoengenheiro
S=/home/claude/site_src
if [ "$1" = "--preparar" ]; then
  rm -rf $S && cp -r $R/src $S && cp -r $R/docs/img $S/img
  for f in post-calculadora-tinta-blogger.html post-queda-tensao-blogger.html post-peso-perfis-blogger.html \
           post-perda-carga-blogger.html post-simulado-mecanica-70.html pg-sobre.html pg-contato.html pg-privacidade.html; do
    cp $S/posts/$f /home/claude/
  done
  cp $S/capa-simulado.svg /home/claude/
  echo "ambiente pronto em $S"; exit 0
fi
cd /home/claude && python3 $S/build_site.py > /tmp/build.log && tail -1 /tmp/build.log
cd $R
rm -rf /tmp/ig_keep && cp -r docs/ig /tmp/ig_keep
rm -rf docs && cp -r /home/claude/site docs && cp -r /tmp/ig_keep docs/ig
# fontes (sem as imagens, que já ficam em docs/img)
rm -rf src && cp -r $S src && rm -rf src/img src/questoes/simulado_tool.html && find src -name __pycache__ -prune -exec rm -rf {} +
git add -A
git -c user.name="joaomarcoslp1-star" -c user.email="joaomarcoslp1-star@users.noreply.github.com" commit -q -m "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011LuAZGoZPc6ioWfb8s6UiQ"
git -c push.negotiate=true push -q origin main
git log --oneline -1
