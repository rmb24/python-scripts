import cv2 as cv
import numpy as np

# Crear una imagen en blanco
img = np.ones((512, 512, 3), np.uint8) * 0

# Dibujar un rectángulo en la imagen
cv.putText(img, 'Computer Vision', (30, 100),
           cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Mostrar la imagen
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()
