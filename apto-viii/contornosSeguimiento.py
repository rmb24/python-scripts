import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

x = 100
y = 200

ancho = 50
alto = 50

color = (0, 255, 0)

direccionX = 5
direccionY = 5

contador = 0

while True:
    _, img = cap.read()
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Rango de colores detectados:
    # Color azul
    lower_color = np.array([100, 100, 20])
    upper_color = np.array([125, 255, 255])

    mask = cv.inRange(hsv, lower_color, upper_color)
    res = cv.bitwise_and(img, img, mask=mask)

    contours, _ = cv.findContours(
        mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x1, y1, w1, h1 = cv.boundingRect(contour)
        if (w1 > 70 and h1 > 70):
            cv.rectangle(img, (x1, y1), (x1+w1, y1+h1), (255, 0, 0), -1)

            # Detectar colisión con el objeto azul
            if (x1 < x + ancho and x1 + w1 > x and y1 < y + alto and y1 + h1 > y):
                direccionX = -direccionX
                direccionY = -direccionY
                contador += 1

    x += direccionX
    y += direccionY

    # Detectar colisión con los bordes de la pantalla
    ancho_pantalla = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    alto_pantalla = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    if (x > ancho_pantalla - ancho or x < 0):
        direccionX = -direccionX
    if (y > alto_pantalla - alto or y < 0):
        direccionY = -direccionY

    # Voltear la imagen horizontalmente
    img = cv.flip(img, 1)

    cv.circle(img, (x, y), 30, color, -1)

    cv.putText(img, f"Puntos: {contador}", (10, 30),
               cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv.imshow('Seguimiento de color', img)

    key = cv.waitKey(1)
    if key == ord('s'):
        break
    elif key == ord('r'):
        contador = 0
        x = 100
        y = 200


cap.release()
cv.destroyAllWindows()
cv.waitKey(1)
cv.waitKey(1)
cv.waitKey(1)
