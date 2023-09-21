import cv2 as cv
import numpy as np
import food as fd
import player as p
import obstacle as ob

cap = cv.VideoCapture(0)

ancho_pantalla = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
alto_pantalla = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

comidas = []
obstaculos = []


def capturaVideo(cap):
    _, img = cap.read()
    return img


def mostrarImagen(image):
    cv.imshow("Juego", image)


def cerrarTodo():
    cap.release()
    cv.destroyAllWindows()
    cv.waitKey(1)
    cv.waitKey(1)
    cv.waitKey(1)


jugador1 = p.player(cv, ancho_pantalla, alto_pantalla, 1)
jugador2 = p.player(cv, ancho_pantalla, alto_pantalla, 2)


comida1 = fd.food(20, 30, 60, 60, jugador1)
comida2 = fd.food(100, 30, 60, 60, jugador1)
comidas.append(comida1)
comidas.append(comida2)

# Obstaculos
obstaculo1 = ob.obstacle(40, 30, 60, 60, jugador1)
obstaculo2 = ob.obstacle(200, 30, 60, 60, jugador1)
obstaculos.append(obstaculo1)
obstaculos.append(obstaculo2)


while True:
    frame = capturaVideo(cap)
    frame = cv.flip(frame, 1)

    for comida in comidas:
        comida.mover(comidas)
        comida.dibujar(cv, frame)

    for obstaculo in obstaculos:
        obstaculo.mover(obstaculos)
        obstaculo.dibujar(cv, frame)

    jugador1.dibujar(frame, comidas, obstaculos)
    jugador2.dibujar(frame, comidas, obstaculos)

    if jugador1.puntos <= 0 or jugador2.puntos <= 0:
        for comida in comidas:
            comida.vel_y = 0
        for obstaculo in obstaculos:
            obstaculo.vel_y = 0

        cv.putText(frame, "Juego terminado", (200, 200),
                   cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv.putText(frame, "El ganador es el jugador " + str(
            1 if jugador1.puntos > 0 else 2), (200, 300), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    mostrarImagen(frame)

    key = cv.waitKey(1)
    if key == ord('s'):
        break

cerrarTodo()
