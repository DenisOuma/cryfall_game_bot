import numpy as np
import win32gui, win32ui, win32con


class cryofallScreenCapture:
    width = 0
    height = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    def __init__(self, window_name = None):
        if window_name is None:
            self.hwnd = win32gui.GetDesktopWindow()
        else:
            self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))

        window_rect = win32gui.GetWindowRect(self.hwnd)  
        self.width = window_rect[2] - window_rect[0]
        self.height = window_rect[3] - window_rect[1]

    def capture_screenshot(self):

        hwnd = None
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.width, self.height)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(self.width, self.height) , dcObj, (self.cropped_x,self.cropped_y), win32con.SRCCOPY)

        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.height, self.width,4)

        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        img = img[...,:3]
        img = np.ascontiguousarray(img)

        return img

    @staticmethod
    def list_window_names():
        print("Check the windo Name of Cryofall Here:")

        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)

        # def get_screen_position(self, pos):
        #     return (pos[0] + self.offset_x, pos[1] + self.offset_y)


