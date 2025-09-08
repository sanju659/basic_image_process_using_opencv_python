import cv2
import numpy as np

img = cv2.imread('imgs/IMG20220930162317.jpg', 1)

print(img.shape) # returns a tuple of number of rows, columns and channels
print(img.size) #returns total number of pixels is accessed
print(img.dtype) # returns image datatype is obtained

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

#img[y1:y2, x1:x2]
horse = img[245:269, 417:455] # copied the horse
horse = cv2.resize(horse, (41, 27)) # Rsizing the image
img[270:297, 279:320] = horse # pasted the horse in the image

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()