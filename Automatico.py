import os
import subprocess
import datetime


class AutomaticGit:
    def __init__(self):
        self.PathBasic = os.getcwd()
        self.PathGit = os.path.join(self.PathBasic, ".git")
        self.now = datetime.datetime.now()
        self.today = self.now.strftime("%Y / %m / %d")

    def Exist(self):
        if os.path.exists(self.PathGit):
            self.commit()
        else:
            Repo = input("no hay repositorio, desea crear uno?\n1.si\n2.no\nElige: ")
            if Repo == "1":
                self.MakeGit()
                self.commit()
            elif Repo == "2":
                return
            else:
                print("ingrese un valor valido")

    def MakeGit(self):
        subprocess.run(["git", "-C", self.PathBasic, "init"], capture_output=True)
        print("Se creo un repositorio correctamente")

    def commit(self):
        subprocess.run(["git", "add", "-A"], capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", self.today, "-m", "this commit is automatic"],
            capture_output=True,
        )
        print("Se hizo el commit correctamente")


def main():  # El menu principal
    auto = AutomaticGit()

    while True:
        print("\n" + "=" * 60)
        print("1. Iniciar")
        print("2. Salir")
        elige = input("Elige: ")

        if elige == "2":
            print("Saliendo...")
            break
        elif elige == "1":
            auto.Exist()
        else:
            print("Ingrese un valor válido")


if __name__ == "__main__":
    main()
