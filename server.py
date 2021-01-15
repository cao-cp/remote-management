#-*-encoding:utf-8-*-
import os,argparse,configparser,re
import conn,compress,deal_command

class serverBuild():
    def __init__(self):
        cf = configparser.ConfigParser()
        configDir = os.path.join(os.path.dirname(__file__),"./config.ini")
        cf.read(configDir)
        self.con = conn.newCon()
        self.press = compress.compress(5)
        self.port = int(cf.get("server","port"))
        self.get_ipv4()
        self.deal = deal_command.deal()
        if self.netStatus:
            print("running on " + self.ip + ":" + str(self.port) )
        else:
            print("network not be found")

    def get_ipv4(self):
        #获取内网IP地址
        ipv4 = os.popen("ipconfig").read()
        try:
            ipv4 = re.findall(r'无线局域网适配器 WLAN:(.*?)默认网关', ipv4, re.S)[0]
            ipv4 = re.findall(r'IPv4 地址 . . . . . . . . . . . . :(.*?)子网掩码', ipv4, re.S)[0].replace(" ", "")
            self.ip = ipv4
            self.netStatus = 1
        except:
            ipv4 = re.findall(r'以太网适配器 以太网:(.*?)默认网关', ipv4, re.S)[0]
            ipv4 = re.findall(r'IPv4 地址 . . . . . . . . . . . . :(.*?)子网掩码', ipv4, re.S)[0].replace(" ", "")
            if "媒体以断开" in ipv4:
                print("未连接网络")
                self.netStatus = 0
            else:
                self.ip = ipv4
                self.netStatus = 1

    def runIpv4(self):
        cnn = conn.newCon()
        ms = cnn.build_new_udp_server("0.0.0.0",self.port)
        pass

    def runOnInternet(self):
        ms = self.con.build_new_tcp_server("0.0.0.0",self.port)
        print("----listening on port " + str(self.port) + "----")
        cli, addr = ms.accept()
        while 1:
            command = input("What do you want me to do: ")
            if command == "cmd":
                self.deal.dealWithIt(command, cli)
            #接收完整数据


    def changePort(self,port):
        self.port = port
        print("port would been changed to " + str(self.port) + " after you build the connection")

    def rebuildIpv4(self):
        self.runIpv4()

    def rebuildOnInternet(self):
        self.runOnInternet()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="server in")
    parser.add_argument("-LAN",help="in LAN or not(True in LAN, otherwise in internet)",default=0,action="store_true")
    arg = parser.parse_args()
    serB = serverBuild()
    if arg.LAN:
        serB.runIpv4()
    else:
        serB.runOnInternet()