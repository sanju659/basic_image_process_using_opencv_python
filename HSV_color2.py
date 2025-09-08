import cv2 as cv
import numpy as np

def nothing(x):
    pass
# Taking input from camera
cap = cv.VideoCapture(0)

cv.namedWindow('Tracking')
cv.createTrackbar('LowerHeu', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LowerSaturation', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LowerValue', 'Tracking', 0, 255, nothing)
cv.createTrackbar('UpperHeu', 'Tracking', 255, 255, nothing)
cv.createTrackbar('UpperSaturation', 'Tracking', 255, 255, nothing)
cv.createTrackbar('UpperValue', 'Tracking', 255, 255, nothing)

while True:
    #frame = cv.imread('./imgs/colour-ball-260nw-73830598.jpg')
    _, frame = cap.read()
    
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    l_h = cv.getTrackbarPos('LowerHeu', 'Tracking')
    l_s = cv.getTrackbarPos('LowerSaturation', 'Tracking')
    l_v = cv.getTrackbarPos('LowerValue', 'Tracking')
    u_h = cv.getTrackbarPos('UpperHeu', 'Tracking')
    u_s = cv.getTrackbarPos('UpperSaturation', 'Tracking')
    u_v = cv.getTrackbarPos('UpperValue', 'Tracking')
 
    
    lower_blue = np.array([l_h, l_s, l_v])
    upper_blue =np.array([u_h, u_s, u_v])
    
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    
    res = cv.bitwise_and(frame, frame, mask=mask)
    
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()    
cv.destroyAllWindows()
