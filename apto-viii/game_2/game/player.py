import numpy as np
import food as fd
import random as r


class player:
    puntos = 10
    color = (255, 0, 0)

    def __init__(self, cv, ancho_v):
        self.cv = cv
        self.ancho_v = ancho_v
        self.lower_color = np.array([100, 100, 20])
        self.upper_color = np.array([125, 255, 255])

    def detectarColision(self, comida1, x1, y1, w1, h1):
        x2, y2, w2, h2 = comida1.x, comida1.y, comida1.w, comida1.h
        if (x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2):
            return True
        else:
            return False

    def comer(self, comidas, comida):
        self.puntos += comida.puntos
        comidas.remove(comida)

    def generarComida(self, comidas):
        comida_w = r.randint(20, 60)
        comida_x = r.randint(0, self.ancho_v - comida_w)
        comida = fd.food(comida_x, 30, comida_w, 60)
        comidas.append(comida)

    def dibujar(self, img, comidas):
        hsv = self.cv.cvtColor(img, self.cv.COLOR_BGR2HSV)
        mask = self.cv.inRange(hsv, self.lower_color, self.upper_color)
        res = self.cv.bitwise_and(img, img, mask=mask)

        contours, _ = self.cv.findContours(
            mask, self.cv.RETR_EXTERNAL, self.cv.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            x1, y1, w1, h1 = self.cv.boundingRect(contour)
            if (w1 > 70 and h1 > 70):
                self.cv.rectangle(
                    img, (x1, y1), (x1+w1, y1+h1), self.color, -1)
                for comida in comidas:
                    choque = self.detectarColision(comida, x1, y1, w1, h1)
                    if (choque):
                        self.comer(comidas, comida)
                        self.generarComida(comidas)

        self.cv.putText(img, "Jugador 1: "+str(self.puntos), (10, 30),
                        self.cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
