import cv2
import numpy as np

img = cv2.imread('imgs/Planning-for-Trekking.jpg', 1)
#img2 = np.zeros([512, 512, 3])

#img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5)
#img = cv2.arrowedLine(img, (0, 0), (255, 255), (255, 0, 0), 5)

rect = cv2.rectangle(img, (384, 10), (510, 128), (0, 255, 0), 4)
#rect = cv2.rectangle(img, (384, 10), (510, 128), (0, 255, 0), -1)

#circ = cv2.circle(img, (200, 200), 80, (0, 255, 0), -1)

#font = cv2.FONT_HERSHEY_SIMPLEX
#img = cv2.putText(img, 'hello there', (10, 400), font, 2, (255, 0, 0), 10, cv2.LINE_AA)

cv2.imshow('image', rect)

cv2.waitKey(0)
cv2.destroyAllWindows()