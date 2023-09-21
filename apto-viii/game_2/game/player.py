import numpy as np
import food as fd
import obstacle as ob
import random as r


class player:

    def __init__(self, cv, ancho_v, alto_v, jugador_num):
        self.cv = cv
        self.ancho_v = ancho_v
        self.alto_v = alto_v
        self.jugador_num = jugador_num
        self.puntos = 10
        if self.jugador_num == 1:
            self.color = (255, 0, 0)
            self.lower_color = np.array([100, 100, 20])
            self.upper_color = np.array([125, 255, 255])
        elif self.jugador_num == 2:
            self.color = (0, 0, 255)
            self.lower_color = np.array([0, 100, 20])
            self.upper_color = np.array([10, 255, 255])

    def detectarColision(self, comida1, x1, y1, w1, h1):
        x2, y2, w2, h2 = comida1.x, comida1.y, comida1.w, comida1.h
        return x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2

    def detectarColisionObstaculo(self, obstaculo1, x1, y1, w1, h1):
        x2, y2, w2, h2 = obstaculo1.x, obstaculo1.y, obstaculo1.w, obstaculo1.h
        return x1 < x2 + w2 and x1 + w1 > x2 and y1 < y2 + h2 and y1 + h1 > y2

    def comer(self, comidas, comida):
        self.puntos += comida.puntos
        comidas.remove(comida)

    def generarComida(self, comidas):
        comida_w, comida_h = r.randint(20, 60), r.randint(20, 60)
        comida_x, comida_y = r.randint(
            0, self.ancho_v - comida_w), r.randint(0, self.alto_v - comida_h)
        comidas.append(fd.food(comida_x, 30, comida_w, 60, self))

    def restarPuntos(self, obstaculo, obstaculos):
        self.puntos -= obstaculo.puntos
        obstaculos.remove(obstaculo)
        if self.puntos <= 0:
            self.puntos = 0

    def generarObstaculos(self, obstaculos):
        obstaculo_w, obstaculo_h = r.randint(20, 60), r.randint(20, 60)
        obstaculo_x, obstaculo_y = r.randint(
            0, self.ancho_v - obstaculo_w), r.randint(0, self.alto_v - obstaculo_h)
        obstaculos.append(ob.obstacle(obstaculo_x, 30, obstaculo_w, 60, self))

    def dibujar(self, img, comidas, obstaculos):
        hsv = self.cv.cvtColor(img, self.cv.COLOR_BGR2HSV)
        mask = self.cv.inRange(hsv, self.lower_color, self.upper_color)
        res = self.cv.bitwise_and(img, img, mask=mask)

        contours, _ = self.cv.findContours(
            mask, self.cv.RETR_EXTERNAL, self.cv.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            x1, y1, w1, h1 = self.cv.boundingRect(contour)
            if w1 > 70 and h1 > 70:
                self.cv.rectangle(
                    img, (x1, y1), (x1+w1, y1+h1), self.color, -1)
                for comida in comidas:
                    if self.detectarColision(comida, x1, y1, w1, h1):
                        self.comer(comidas, comida)
                        self.generarComida(comidas)
                        if comida.y > self.alto_v:
                            comidas.remove(comida)
                            print("Comida eliminada")

                for obstaculo in obstaculos:
                    if self.detectarColisionObstaculo(obstaculo, x1, y1, w1, h1):
                        self.restarPuntos(obstaculo, obstaculos)
                        self.generarObstaculos(obstaculos)
                        if obstaculo.y > self.alto_v:
                            obstaculos.remove(obstaculo)
                            print("Obstaculo eliminado")

        self.cv.putText(img, f"Jugador {self.jugador_num}: {self.puntos}", (10, 30 * self.jugador_num),
                        self.cv.FONT_HERSHEY_SIMPLEX, 1, self.color, 2)
