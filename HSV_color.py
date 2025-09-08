import cv2 as cv
import numpy as np

def nothing(x):
    pass

#cv.namedWindow('Tracking')

while True:
    frame = cv.imread('./imgs/colour-ball-260nw-73830598.jpg')
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    lower_blue = np.array([110, 50, 50])
    upper_blue =np.array([130, 255, 255])
    
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    
    res = cv.bitwise_and(frame, frame, mask=mask)
    
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cv.destroyAllWindows()