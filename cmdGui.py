#-*- coding:utf-8 -*-
import tkinter,os,struct
from tkinter.scrolledtext import ScrolledText


class cmd():
    def __init__(self,ip,cli):
        self.root = tkinter.Tk()
        self.setAttribute(ip)
        print(" ")
        self.setText()
        self.cli = cli
        self.buffer = 1024
    def setAttribute(self,ip):
        self.root.title(str(ip) + " 的cmd")
        self.root.minsize(780,450)
        self.root.geometry("780x450+300+200")
        self.root["background"] = "black"

    def setText(self):
        self.te = ScrolledText(self.root,state='d',fg='white',bg='black',insertbackground='white',font=('consolas',13),selectforeground='black',selectbackground='white',takefocus=False)

        self.te.tag_config('red', foreground='red', selectforeground='#00ffff', selectbackground='#ffffff')
        self.te.tag_config('white', foreground='white', selectforeground='#ff7eff', selectbackground='#ffffff')
        self.te.tag_config('blue', foreground='blue', selectforeground='#ffff7e', selectbackground='#ffffff')
        self.te.tag_config('cyan', foreground='cyan', selectforeground='red', selectbackground='#ffffff')

        self.te['state'] = 'n'
        self.te.insert('end', 'by my dear Changpei Cao\n')
        self.te.insert('end', f'{os.getcwd()}>', 'white')
        self.te.bind('<KeyRelease-Return>', lambda x:self.function())
        #绑定回车
        self.te.pack(fill='both',expand='yes')#bind要在pack之前，否则不行。

    def function(self):
        print("命令执行完毕",self.te.index('insert'))
        cmd = self.te.get(float(self.te.index("insert"))-float(1.0),self.te.index("insert")).split(os.getcwd() + ">")[1]
        print(cmd)
        self.sendCmd(cmd)
        result = self.getResult()
        self.PrintR(result)
        self.te.insert('end', f'{os.getcwd().strip()}>', 'white')
        self.te.delete(self.te.index("insert"),"end")
        self.te.see(tkinter.END)

    def sendCmd(self,cmd):
        cmd = "cmd:" + cmd
        self.cli.send(cmd.encode())

    def PrintR(self,result):
        if result == None:
            self.te.insert('end',f'\n',"white")
        else:
            self.te.insert("end",result + "\n","white")

    def getResult(self):
        result = self.recvData(self.cli)
        return result

    def recvData(self,cli):
        while 1:
            pack_len =cli.recv(4) #报头长度
            if pack_len:
                data_len = struct.unpack("i",pack_len)[0]
                content = b''
                while data_len>0:
                    if data_len>=self.buffer:
                        content_temp = cli.recv(self.buffer)
                        content += content_temp
                        data_len -= self.buffer
                    else:
                        content_temp = cli.recv(data_len)
                        content += content_temp
                        data_len = 0
                return content.decode()
            break

    def startGui(self):
        self.root.mainloop()

if __name__ == "__main__":
    tk=cmd(127)
    tk.startGui()
