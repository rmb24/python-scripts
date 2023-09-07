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
        area = cv.contourArea(contour)
        if (area > 500):
            rect = cv.minAreaRect(contour)
            box = cv.boxPoints(rect)
            box = np.int0(box)
            cv.drawContours(img, [box], 0, (255, 0, 0), -1)

            # Detectar colisión con el objeto azul
            if (rect[0][0] - rect[1][0]/2 < x + ancho and rect[0][0] + rect[1][0]/2 > x and rect[0][1] - rect[1][1]/2 < y + alto and rect[0][1] + rect[1][1]/2 > y):
                direccionX = -direccionX
                direccionY = -direccionY
                contador += 1
                print("Colisión")

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

    cv.circle(img, (x, y), 50, color, -1)

    cv.putText(img, f"Puntos: {contador}", (10, 30),
               cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv.imshow('Seguimiento de color', img)

    if cv.waitKey(1) & 0xFF == ord('s'):
        break

cap.release()
cv.destroyAllWindows()
cv.waitKey(1)
cv.waitKey(1)
cv.waitKey(1)
