import socket
import getConfig

#This is used when you need to build a new connection
class newCon():
    def __init__(self):
        '''self.iIp = getConfig.getConfig(section="iServer",option="ip")
        self.iPort = int(getConfig.getConfig(section="iServer" ,option= "port"))
        self.iUrl = getConfig.getUrl("iServer")
        self.localIp = getConfig.getConfig("localServer","ip")
        self.localPort = int(getConfig.getConfig("localServer","port"))'''
        pass

    def build_new_tcp(self,ip,port):
        mySock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mySock.connect((ip,port))
        print("已连接到" + ip + ":"+ str(port))
        return mySock

    def build_new_udp(self):
        mySock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        pass
        return mySock

    def build_new_udp_server(self,ip,port):
        mySock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        pass
        return mySock

    def build_new_tcp_server(self,ip,port):
        mySock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mySock.bind((ip,port))
        mySock.listen(3)
        return mySock

if __name__ == "__main__":
    cnn = newCon()
    print(cnn.iIp,cnn.iPort,cnn.iUrl)
    print(type(cnn.localIp),type(cnn.localPort))