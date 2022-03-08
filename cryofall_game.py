import cv2 as cv
import numpy as np
import os
from time import time
from cryofallScreenCapture import cryofallScreenCapture
from prime import Prime

os.chdir(os.path.dirname(os.path.abspath(__file__)))
# Image Loop
cryofallScreenCapture.list_window_names()
wincap = cryofallScreenCapture('CryoFall')
Prime_resources = Prime('find_stone.png')
time_loop = time()
while(True):
    screenshot = wincap.capture_screenshot()
    # cv.imshow('Computer Vision', screenshot)
    points = Prime_resources.findClickPositions(screenshot, 0.63, 'rectangles')

    # print('Frames Per Second {}'.format(1 / (time() - time_loop)))
    time_loop = time()


    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


capture_window()
print('Done.')





# install the following packages
# sudo apt-get install scrot
# sudo apt-get install python3-tk python3-dev