# importar librerias
import os
import subprocess
import datetime


class AutomaticGit:
    def __init__(self):
        self.PathBasic = os.getcwd()  # path donde se ejecuta el py
        self.PathGit = os.path.join(self.PathBasic, ".git")  # el path del git
        self.now = datetime.datetime.now()  # el dia de hoy
        self.today = self.now.strftime("%Y / %m / %d")  # el dia de hoy

    def Exist(self):  # si existe un repo
        if os.path.exists(self.PathGit):  # si existe:
            self.commit()  # hace commit
        else:  # si no existe: crea uno
            Repo = input("no hay repositorio, desea crear uno?\n1.si\n2.no\nElige: ")
            if Repo == "1":
                self.MakeGit()  # crea un repo
                self.commit()  # hace commit
            elif Repo == "2":
                return  # se sale
            else:
                print("ingrese un valor valido")

    def MakeGit(self):  # se crea un repo en el path del py
        subprocess.run(["git", "-C", self.PathBasic, "init"], capture_output=True)
        print("Se creo un repositorio correctamente")

    def commit(self):  # se agregan todos los archivos:
        subprocess.run(["git", "add", "-A"], capture_output=True)
        subprocess.run(  # se agrega comentario y dice que se hizo automaticamente
            ["git", "commit", "-m", self.today, "-m", "this commit is automatic"],
            capture_output=True,
        )
        print("Se hizo el commit correctamente")  # mensaje de exito


def main():  # El menu principal
    auto = AutomaticGit()  # asigna variable a AutomaticGit

    while True:  # menu
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


if __name__ == "__main__":  # inicia el programa
    main()
