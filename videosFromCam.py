import cv2

##Reading video from web camera
cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    
    ## Changing the colored image to gray
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame', frame)
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()

