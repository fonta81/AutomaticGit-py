# nesesito un programa que solo con abrirlo detecte si hay una carpeta .git
# si la hay -> haga un commit
# si no, que la cree y lo haga
import os
import subprocess
import datetime

now = datetime.datetime.now()
today = now.strftime("%Y / %m / %d")


class AutomaticGit:
    def __init__(self):
        self.PathBasic = os.path.join("")

    def Exist(self, PathOfGit):
        pass

    def MakeGit(self):
        pass

    def commit(self, today):
        pass
