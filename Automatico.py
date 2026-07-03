import os
import subprocess
import datetime

now = datetime.datetime.now()
today = now.strftime("%Y / %m / %d")


class AutomaticGit:
    def __init__(self):
        self.PathBasic = os.getcwd()
        self.PathGit = os.path.join(self.PathBasic, ".git")

    def Exist(self):
        if os.path.exists(self.PathGit):
            print("si we")
        else:
            print("no we")

    def MakeGit(self):
        pass

    def commit(self, today):
        pass


aa = AutomaticGit()
aa.Exist()
