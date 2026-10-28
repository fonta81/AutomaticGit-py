#!/usr/bin/env bash

set -u
repo_path=$(pwd)

if ! command -v git >/dev/null 2>&1; then
  echo "Error: Git no está instalado o no se encuentra en PATH." >&2
  exit 127
fi

run_git() {
  git -C "$repo_path" "$@"
}

if ! run_git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "No hay un repositorio Git. ¿Desea crear uno?"
  echo "1. Sí"
  echo "2. No"
  if ! read -r -p "Elige: " repo; then
    echo "No se pudo leer la respuesta." >&2
    exit 1
  fi
  if [[ "$repo" == "1" ]]; then
    if ! run_git init; then
      echo "Error: no se pudo crear el repositorio." >&2
      exit 1
    fi
    echo "Se creó un repositorio correctamente."
  elif [[ "$repo" == "2" ]]; then
    echo "Saliendo..."
    exit 0
  else
    echo "Ingrese un valor válido." >&2
    exit 1
  fi
fi

if ! status=$(run_git status --short --untracked-files=all); then
  echo "Error: no se pudo consultar el estado del repositorio." >&2
  exit 1
fi

if [[ -z "$status" ]]; then
  echo "No hay cambios para confirmar."
  exit 0
fi

echo
echo "Cambios que se incluirán:"
printf '%s\n' "$status"
if ! read -r -p "¿Desea agregar todos estos cambios y crear el commit? (s/N): " answer; then
  echo "No se pudo leer la respuesta." >&2
  exit 1
fi
case "${answer,,}" in
  s|si|sí) ;;
  *)
    echo "Operación cancelada; no se agregaron cambios."
    exit 0
    ;;
esac

if ! run_git add -A; then
  echo "Error: no se pudieron agregar los cambios." >&2
  exit 1
fi

if run_git diff --cached --quiet; then
  echo "No hay cambios preparados para confirmar."
  exit 0
else
  diff_status=$?
  if [[ "$diff_status" -ne 1 ]]; then
    echo "Error: no se pudo comprobar los cambios preparados." >&2
    exit "$diff_status"
  fi
fi

hoy=$(date '+%Y / %m / %d')
if ! run_git commit -m "$hoy" -m "this commit is automatic"; then
  echo "Error: no se pudo crear el commit." >&2
  exit 1
fi
echo "Se hizo el commit correctamente."
