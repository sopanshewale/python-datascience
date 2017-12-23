#!/usr/local/Cellar/python3/3.6.3/bin/python3
import cv2
import numpy as np

# load certificate in gray scale
img = cv2.imread('flower.jpg', 1)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
