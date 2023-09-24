import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../images/tigre.jpg', 0)
kernel = np.ones((7, 7), np.uint8)
gradiente = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)

plt.subplot(121)
plt.imshow(img)
plt.title("Original")
plt.show()
plt.subplot(122)
plt.imshow(gradiente)
plt.imshow('Erosionada')
plt.show
