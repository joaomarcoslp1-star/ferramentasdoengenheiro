#!/bin/bash
# Uso: publicar.sh "mensagem do commit"
set -e
cd /home/claude && python3 site_src/build_site.py | tail -1
cd /home/claude/ferramentasdoengenheiro
rm -rf /tmp/ig_keep && cp -r docs/ig /tmp/ig_keep
rm -rf docs && cp -r /home/claude/site docs && cp -r /tmp/ig_keep docs/ig
cp /home/claude/site_src/build_site.py /home/claude/site_src/compor_capas.py src/
for d in torque nr13 vigas inercia tabelas; do mkdir -p src/$d && cp /home/claude/site_src/$d/* src/$d/; done
cp /home/claude/site_src/posts/*.html src/posts/
cp /home/claude/publicar.sh src/
git add -A
git -c user.name="joaomarcoslp1-star" -c user.email="joaomarcoslp1-star@users.noreply.github.com" commit -q -m "$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_011LuAZDoX5ECSYeQCwGAVeP"
git -c push.negotiate=true push -q origin main
git log --oneline -1
