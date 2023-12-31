import random as r
import cv2 as cv
import numpy as np


class food:
    color = (0, 255, 0)

    def __init__(self, x, y, w, h, player):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel_y = r.randint(3, 10)
        self.puntos = r.randint(2, 10)
        self.player = player
        self.img_dir = "./items/food"
        self.img_name = "food"+str(r.randint(1, 5))+".png"
        self.img = cv.imread(self.img_dir+"/"+self.img_name)
        self.img = cv.resize(self.img, (self.w, self.h))

    def puntoMedio(self, p1, p2):
        return ((p2 + p1)/2)

    def mover(self, comidas):
        if self.y < self.player.alto_v:
            self.y += self.vel_y
        else:
            self.player.generarComida(comidas)
            comidas.remove(self)
            print("Comida eliminada")

    def dibujar(self, cv, img):
        px = int(self.puntoMedio(self.x, self.x+self.w)) - 10
        py = int(self.puntoMedio(self.y, self.y+self.h))
        if self.x >= 0 and self.x + self.w <= img.shape[1] and self.y >= 0 and self.y + self.h <= img.shape[0]:
            img[self.y:self.y + self.h, self.x:self.x + self.w] = self.img
            cv.putText(img, "" + "+" + str(self.puntos),
                       (px, py),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
