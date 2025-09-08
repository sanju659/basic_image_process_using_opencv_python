import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

cap = cv.VideoCapture(0)

#img = cv.imread('./imgs/doraemon.jpg', -1)


while True:
    ret, img = cap.read()
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    if ret == 0:
        break
    else:
        plt.imshow(img)
        ## removing x and y ticks
        plt.xticks([]), plt.yticks([])
        plt.show()
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
plt.close()

