import cv2 as cv
import numpy as np
import mediapipe as mp

cap = cv.VideoCapture(0)

x = 100
y = 200

ancho = 50
alto = 50

color = (0, 255, 0)

direccionX = 5
direccionY = 5

contador = 0

mp_deteccion_manos = mp.solutions.hands
deteccion_manos = mp_deteccion_manos.Hands()

while True:
    _, img = cap.read()
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    resultados = deteccion_manos.process(img)

    if resultados.multi_hand_landmarks:
        for mano in resultados.multi_hand_landmarks:
            for id, lm in enumerate(mano.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8:
                    cv.circle(img, (cx, cy), 15, (255, 0, 0), -1)

                    # Detectar colisión con el objeto azul
                    if (cx < x + ancho and cx > x - ancho and cy < y + alto and cy > y - alto):
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
    img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
    img = cv.flip(img, 1)

    cv.circle(img, (x, y), 30, color, -1)

    cv.putText(img, f"Puntos: {contador}", (10, 30),
               cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv.imshow('Seguimiento de manos', img)

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
