#!/bin/bash
hoy=$(date +%Y-%m-%d)

if [ -d ".git" ]; then
  git add -A
  git commit -m "$hoy" -m "This is a commit automatic"
else
  echo "No hay un repo, quisieras crear uno?"
  echo "1.si"
  echo "2.no"
  read -r repo
  if [ "$repo" -eq "1" ]; then
    git init
    git add -A
    git commit -m "$hoy" -m "This is a commit automatic"
  else
    echo "Saliendo..."
  fi
fi
