import os

class boeyCommand():
    def __init__(self):
        pass
    def obey(self,command):
        if command.split(":")[0] == "cmd":
            result = os.popen(command.split(":")[1]).read()
            return result
        else:
            return "Sorry I can't understand what you want"

