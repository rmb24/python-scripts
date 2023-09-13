import cv2 as cv
import numpy as np
import food as fd
import player as p

cap = cv.VideoCapture(0)

ancho_pantalla = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
alto_pantalla = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))


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


comidas = [fd.food(20, 0, 60, 60), fd.food(100, 0, 60, 60), fd.food(
    200, 0, 60, 60), fd.food(300, 0, 60, 60), fd.food(400, 0, 60, 60)]
jugador = p.player(cv)

while True:
    frame = capturaVideo(cap)

    for comida in comidas:
        comida.mover()
        comida.dibujar(cv, frame)
    jugador.dibujar(frame, comidas)
    mostrarImagen(frame)

    key = cv.waitKey(1)
    if key == ord('s'):
        break

cerrarTodo()
