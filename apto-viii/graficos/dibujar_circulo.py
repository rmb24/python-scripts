import cv2 as cv
import numpy as np

# Crear una imagen en blanco
img = np.ones((512, 512, 3), np.uint8) * 255

# Dibujar un rectángulo en la imagen
cv.circle(img, (256, 256), 50, (0, 255, 0), 2)

# Mostrar la imagen
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
