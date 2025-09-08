import cv2 as cv
import numpy as np

def nothing(x):
    pass

cv.namedWindow('image')

cv.createTrackbar('Current Position', 'image', 20, 200, nothing)

switch = 'color: 0\n gray: 1\n'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    img = cv.imread('./imgs/doraemon.jpg', 1)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
    cp = cv.getTrackbarPos('Current Position', 'image')
    font = cv.FONT_HERSHEY_COMPLEX
    cv.putText(img, str(cp), (100,100), font, 4, (0, 200, 0), 3)
    
    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    cv.imshow('image', img)
      
      
cv.destroyAllWindows()

