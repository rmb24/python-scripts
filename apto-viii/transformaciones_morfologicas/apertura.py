import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../images/tigre.jpg', 0)
kernel = np.ones((7, 7), np.uint8)
apertura = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

plt.subplot(121)
plt.imshow(img)
plt.title("Original")
plt.show()
plt.subplot(122)
plt.imshow(apertura)
plt.imshow('Erosionada')
plt.show
