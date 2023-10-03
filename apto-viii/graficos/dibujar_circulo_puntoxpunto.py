import cv2 as cv
import numpy as np

# Crear una imagen en blanco
img = np.ones((400, 400, 3), np.uint8) * 255

# Definir las coordenadas del circulo y el radio
center = (200, 200)
radius = 150

# Calcular los puntos del bordo del circulo en el sentido de las agujas del reloj
points = []
for i in range(0, 360, 10):
    angle = i * np.pi / 180
    x = int(center[0] + radius * np.cos(angle))
    y = int(center[1] + radius * np.sin(angle))
    points.append((x, y))


# Dibujar el circulo punto a punto
for point in points:
    cv.circle(img, (int(point[0]), int(point[1])), 1, (0, 0, 0), -1)
    cv.imshow('image', img)
    cv.waitKey(50)

cv.waitKey(0)
cv.destroyAllWindows()
