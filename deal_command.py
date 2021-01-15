import cmdGui

class deal():
    def __init__(self):
        pass
    def dealWithIt(self,command,cli):
        while 1:
            if command == "cmd":
                self.cmdG = cmdGui.cmd("您",cli)
                #cmd = input("input your command: ")
                #cmdData = "cmd:" + cmd
                self.cmdG.startGui()
                result = self.getResult()

                break
            else:
                print("try cmd")
                command = input("What do you want me to do: ")
                continue

