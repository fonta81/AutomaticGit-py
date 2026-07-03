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
            self.MakeGit()
            self.commit()

    def MakeGit(self):
        subprocess.run(["git", "-C", self.PathBasic, "init"], capture_output=True)
        print("Se creo un repositorio correctamente")

    def commit(self):
        subprocess.run(["git", "add", "."], capture_output=True)
        subprocess.run(
            ["git", "commit", "-m", self.today, "-m", "this commit is automatic"],
            capture_output=True,
        )


# aa = AutomaticGit()
# aa.Exist()
