import cv2 as cv
import numpy as np

img = cv.imread('./imgs/IMG_20250102_205740.jpg', 0)

width, height = 400, 600 # Set the desired width and height
img = cv.resize(img, (width, height))

## Binary thresholding
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

cv.imshow('image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)

cv.waitKey(0)
cv.destroyAllWindows()
