import datetime
import os
import subprocess


class AutomaticGit:
    def __init__(self):
        self.path_basic = os.getcwd()
        self.today = datetime.datetime.now().strftime("%Y / %m / %d")

    def _run_git(self, *args):
        try:
            return subprocess.run(
                ["git", "-C", self.path_basic, *args],
                capture_output=True,
                text=True,
                check=False,
            )
        except FileNotFoundError:
            print("Error: Git no está instalado o no se encuentra en PATH.")
            return None
        except OSError as error:
            print(f"Error al ejecutar Git: {error}")
            return None

    def _ensure_repository(self):
        result = self._run_git("rev-parse", "--is-inside-work-tree")
        if result is None:
            return False
        if result.returncode == 0:
            return True

        try:
            answer = input(
                "No hay un repositorio Git. ¿Desea crear uno?\n1. Sí\n2. No\nElige: "
            )
        except EOFError:
            print("No se recibió una respuesta; operación cancelada.")
            return False
        if answer == "1":
            result = self._run_git("init")
            if result is None or result.returncode != 0:
                self._print_git_error(result)
                return False
            print("Se creó un repositorio correctamente.")
            return True
        if answer != "2":
            print("Ingrese un valor válido.")
        return False

    @staticmethod
    def _print_git_error(result):
        if result is None:
            return
        message = result.stderr.strip() or result.stdout.strip()
        if message:
            print(f"Error de Git: {message}")
        else:
            print(f"Error de Git: el comando terminó con código {result.returncode}.")

    def commit(self):
        result = self._run_git("status", "--short", "--untracked-files=all")
        if result is None:
            return
        if result.returncode != 0:
            self._print_git_error(result)
            return
        if not result.stdout.strip():
            print("No hay cambios para confirmar.")
            return

        print("\nCambios que se incluirán:")
        print(result.stdout.rstrip())
        try:
            answer = input(
                "¿Desea agregar todos estos cambios y crear el commit? (s/N): "
            )
        except EOFError:
            print("No se recibió una respuesta; operación cancelada.")
            return
        if answer.strip().lower() not in ("s", "si", "sí"):
            print("Operación cancelada; no se agregaron cambios.")
            return

        result = self._run_git("add", "-A")
        if result is None or result.returncode != 0:
            self._print_git_error(result)
            return

        result = self._run_git("diff", "--cached", "--quiet")
        if result is None:
            return
        if result.returncode == 0:
            print("No hay cambios preparados para confirmar.")
            return
        if result.returncode != 1:
            self._print_git_error(result)
            return

        result = self._run_git(
            "commit",
            "-m",
            self.today,
            "-m",
            "this commit is automatic",
        )
        if result is None:
            return
        if result.returncode != 0:
            self._print_git_error(result)
            return
        print("Se hizo el commit correctamente.")

    def Exist(self):
        if self._ensure_repository():
            self.commit()


def main():
    auto = AutomaticGit()

    while True:
        print("\n" + "=" * 60)
        print("1. Iniciar")
        print("2. Salir")
        try:
            elige = input("Elige: ")
        except EOFError:
            print("\nSaliendo...")
            break

        if elige == "2":
            print("Saliendo...")
            break
        if elige == "1":
            auto.Exist()
        else:
            print("Ingrese un valor válido.")


if __name__ == "__main__":
    main()
