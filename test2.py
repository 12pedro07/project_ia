import numpy as np
import cv2
import time
import random
from math import *

class mousecoord:
    def __init__(self,img):
        self.click = False
        self.img = img

    def mouse_callback(self,event,x,y,flags,param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.click = True

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.click == True:
                print(x,y)

        elif event == cv2.EVENT_LBUTTONUP:
            self.click = False

# img parameters
w = 1400
h = 800
t = 0
path = []
# setup the black background
img = np.zeros((h, w, 3),np.uint8)
cv2.namedWindow('image')

signalX = []
signalY = []

mouse = mousecoord(img)
cv2.setMouseCallback('image',mouse.mouse_callback)
while(1):
    cv2.imshow('image',mouse.img)
    if cv2.waitKey(1) & 0xFF == 27:
        signalX = mouse.coordinatesX
        signalX += signalX[::-1]
        signalY = mouse.coordinatesY
        signalY += signalY[::-1]
        break
cv2.destroyAllWindows()
menuAux = False
