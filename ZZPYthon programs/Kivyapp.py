#Kivy app

import cv2
import numpy as np

img = cv2.imread("C://Users/rhysa/Pictures/AVAlogo.jpg", 0)

cv2.imshow('', img)
cv2.waitkey(0)
cv2.destroyAllWindows()
