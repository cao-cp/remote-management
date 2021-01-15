import conn,compress,getConfig,obey_command
import struct

#This is the client which is being controlled
class client():
    def __init__(self):
        self.ip = getConfig.getConfig("client","ip")
        self.port = int(getConfig.getConfig("client","port"))
        con = conn.newCon()
        self.client = con.build_new_tcp(self.ip,self.port)
        self.compress = compress.compress(5)#初始化压缩类
        self.buffer = 1024
        self.obey = obey_command.boeyCommand()#命令处理类

    def sendMsg(self,msg):
        msg= msg.encode()
        size = len(msg)
        pack_len = struct.pack("i",size)
        self.client.send(pack_len)#发送报头长度
        i = 0
        while size > 0:
            if size > self.buffer:
                partData = msg[i*self.buffer:(i+1)*self.buffer]
                self.client.send(partData)
                size -= self.buffer
                i+=1
            else:
                self.client.send(msg[i*self.buffer:])
                size = 0
                break

    def waitingCommand(self):
        command = self.client.recv(1024)
        result = self.obey.obey(command.decode())#处理命令
        self.sendMsg(result)



if __name__ == "__main__":
    cli = client()
    while 1:
        cli.waitingCommand()


