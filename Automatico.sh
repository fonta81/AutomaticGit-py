#!/bin/bash
hoy=$(date +%Y-%m-%d)

echo "Existe un ya un repo? "
echo "1.Si"
echo "2.no"
read -r repo

if [ "$repo" -eq "1" ]; then
  git add -A
  git commit -m "$hoy" -m "This commit is automatic"
elif [ "$repo" -eq "2" ]; then
  git init
  git add -A
  git commit -m "$hoy" -m "This commit is automatic"
else
  echo "Ingrese un valor valido "
fi
