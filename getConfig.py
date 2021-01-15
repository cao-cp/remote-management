import configparser,os

#This is for getting configs from config.ini in the same path from where the files using this are in
def getConfig(section = "default", option = ""):
    config= configparser.ConfigParser()
    try:
        config.read(os.path.join(os.path.dirname(__file__),"config.ini"))
    except:
        print(os.path.join(os.path.dirname(__file__),"config.ini") + "下没有配置文件")
        return
    return config.get(section,option)

def getUrl(section = "default"):
    url = getConfig(section,"ip") + ":" + getConfig(section,"port")
    return url

if __name__ == "__main__":
    print(os.path.join(os.path.dirname(__file__),"config.ini"))