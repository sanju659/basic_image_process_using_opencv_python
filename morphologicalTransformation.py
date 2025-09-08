import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('./imgs/colour-ball-260nw-73830598.jpg', 0)
_, mask = cv.threshold(img, 220, 225, cv.THRESH_BINARY_INV)

kernel = np.ones((2, 2), np.uint8)
dilation = cv.dilate(mask, kernel, iterations=2)
erosion = cv.dilate(mask, kernel, iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
closeing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)

titles = ['Image', 'Mask', 'Dilation', 'Erosion', 'Opening', 'Closeing']
images = [img, mask, dilation, erosion, opening, closeing]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()


