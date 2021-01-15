#-*- coding=utf-8 -*-
import zlib,os
from PIL import Image

class compress():
    def __init__(self,level):
        self.level = level#level为1-9，越大压缩等级越高
        #self.w,self.h = getPic.getPic.getWH(self) #获取屏幕分辨率
    def compressPic(self,filepath):
        """
        压缩图片
        :return:
        """
        fpsize = os.path.getsize(filepath) / 1024  # 获得图片多少K   os.path.getsize(self.picPath)返回的是字节
        im = Image.open(filepath)  # 打开图片
        imBytes = im.tobytes()  # 把图片转换成bytes流
        imBytes = zlib.compress(imBytes, self.level)  # 对图像字节串进行压缩
        im2 = Image.frombytes('RGB', im.size, zlib.decompress(imBytes))  # 压缩成新的图片
        im2.save(filepath)
        return (filepath, os.path.getsize(filepath))

    def compressMsg(self,msg):
        msg = zlib.compress(msg)
        return msg

    def decompressMsg(self,msg):
        msg = zlib.decompress(msg)
        msg = msg.decode("utf-8")
        return msg

if __name__ == "__main__":
    cmp = compress(1)#压缩等级1
    '''filepath,size = cmp.compressPic("./haha.jpg")
    print(filepath,size)'''
    msg = '''2021/01/11  22:25    <DIR>          .
2021/01/11  22:25    <DIR>          ..
2020/12/31  21:01    <DIR>          .android
2020/07/15  09:21    <DIR>          .AndroidStudio4.0
2020/12/31  21:00    <DIR>          .BigNox
2020/12/30  17:37    <DIR>          .docker
2020/07/15  10:29                16 .emulator_console_auth_token
2020/07/15  09:32    <DIR>          .gradle
2020/07/21  14:15    <DIR>          .Icecream PDF Candy Desktop
2019/11/10  21:18    <DIR>          .idlerc
2021/01/11  00:58    <DIR>          .lemminx
2021/01/11  00:38    <DIR>          .m2
2020/12/16  15:42    <DIR>          .MemuHyperv
2020/07/30  15:04    <DIR>          .myeclipse
2020/12/02  13:25    <DIR>          .oracle_jre_usage
2020/07/30  14:58                24 .pulse2.locator
2019/11/10  20:14    <DIR>          .PyCharmCE2019.2
2020/08/12  17:32    <DIR>          .swt
2021/01/08  23:25    <DIR>          .tooling
2020/06/25  12:58    <DIR>          .vscode
2020/12/16  14:41    <DIR>          3D Objects
2020/12/16  14:41    <DIR>          Contacts
2020/12/31  21:01               298 d4ac4633ebd6440fa397b84f1bc94a3c.7z
2021/01/11  13:01    <DIR>          Desktop
2021/01/09  11:25    <DIR>          Documents
2020/12/16  14:41    <DIR>          Downloads
2020/12/16  14:41    <DIR>          Favorites
2020/11/17  18:18    <DIR>          fotiaoqiang
2020/07/23  12:29                66 inittk.ini
2020/07/23  12:28                41 inst.ini
2020/12/16  14:41    <DIR>          Links
2020/12/16  14:41    <DIR>          Music
2020/08/30  14:08    <DIR>          Nox_share
2020/07/23  12:28                45 nuuid.ini
2020/12/30  18:03    <DIR>          OneDrive
2020/12/16  14:41    <DIR>          Pictures
2021/01/11  22:23    <DIR>          pip
2020/12/16  14:41    <DIR>          Saved Games
2020/12/16  14:41    <DIR>          Searches
2020/08/15  15:59    <DIR>          ShakaApktool
2019/12/09  12:12                16 skb.kc
2021/01/09  11:40    <DIR>          source
2020/08/05  16:58        10,581,537 trace.html
2020/07/23  12:28                53 useruid.ini
2020/12/16  14:41    <DIR>          Videos
2020/12/31  21:00    <DIR>          vmlogs
               9 个文件     10,582,096 字节
              37 个目录 55,221,350,400 可用字节'''
    msg, l = cmp.compressMsg(msg)
    print(msg,"\n",l)
    msg = cmp.decompressMsg(msg)
    print(msg)

