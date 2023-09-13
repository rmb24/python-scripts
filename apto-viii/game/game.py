import cv2 as cv
import numpy as np
import food as fd
import player as p
import random as r

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


# comidas = [fd.food(20, 0, 60, 60), fd.food(100, 0, 60, 60), fd.food(
#     200, 0, 60, 60), fd.food(300, 0, 60, 60), fd.food(400, 0, 60, 60)]

comidas = []
num_comidas = 10
comida_w = 60
comida_h = 60
comida_x = 20
comida_y = 0

for i in range(num_comidas):
    comida_x = r.randint(0, ancho_pantalla - comida_w)
    comidas.append(fd.food(comida_x, comida_y, comida_w, comida_h))


jugador = p.player(cv)

while True:
    frame = capturaVideo(cap)
    frame = cv.flip(frame, 1)

    for comida in comidas:
        comida.mover()
        comida.dibujar(cv, frame)
    jugador.dibujar(frame, comidas)
    mostrarImagen(frame)

    key = cv.waitKey(1)
    if key == ord('s'):
        break
    elif key == ord('r'):

        # comidas = [fd.food(20, 0, 60, 60), fd.food(100, 0, 60, 60), fd.food(
        #     200, 0, 60, 60), fd.food(300, 0, 60, 60), fd.food(400, 0, 60, 60)]
        comidas = []
        for i in range(num_comidas):
            comida_x = r.randint(0, ancho_pantalla - comida_w)
            comidas.append(fd.food(comida_x, comida_y, comida_w, comida_h))
        jugador = p.player(cv)


cerrarTodo()
