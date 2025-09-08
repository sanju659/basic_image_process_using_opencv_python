import cv2

##Reading video from web camera
cap = cv2.VideoCapture(0)

##Reading videos from device's hard disk
#cap = cv2.VideoCapture('imgs/22464-328008656_small.mp4')

#while (cap.isOpened()):
    #ret, frame = cap.read()
    
    ## Changing the colored image to gray
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #cv2.imshow('frame', frame)

    #if cv2.waitKey(1) & 0xFF == ord('e'):
        #break

while (True):
    ret, frame = cap.read()
    
    ## Changing the colored image to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()
