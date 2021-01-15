import time
import win32gui, win32ui, win32con, win32api, win32print

class getPic():
    def __init__(self,fps):
        self.fps = fps#刷新率
    def window_capture(self,filename):
      hwnd = 0 # 窗口的编号，0号表示当前活跃窗口
      # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
      hwndDC = win32gui.GetWindowDC(hwnd)
      # 根据窗口的DC获取mfcDC
      mfcDC = win32ui.CreateDCFromHandle(hwndDC)
      # mfcDC创建可兼容的DC
      saveDC = mfcDC.CreateCompatibleDC()
      # 创建bigmap准备保存图片
      saveBitMap = win32ui.CreateBitmap()
      w,h = self.getWH()
      print(w,h)#图片大小
      # 为bitmap开辟空间
      saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
      # 高度saveDC，将截图保存到saveBitmap中
      saveDC.SelectObject(saveBitMap)
      # 截取从左上角（0，0）长宽为（w，h）的图片
      saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
      saveBitMap.SaveBitmapFile(saveDC, filename)
      self.beg = time.time()

    def getWH(self):
        """获取真实的分辨率"""
        hDC = win32gui.GetDC(0)
        # 横向分辨率
        w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
        # 纵向分辨率
        h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
        return w,h
    def capture(self):
        for i in range(self.fps):
          self.window_capture("haha.jpg")
        self.end = time.time()
        print(self.end - self.beg)

if __name__ == "__main__":
    gp = getPic(1)
    gp.capture()

