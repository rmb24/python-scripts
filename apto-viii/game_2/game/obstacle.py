import random as r
import cv2 as cv


class obstacle:
    color = (0, 0, 255)

    def __init__(self, x, y, w, h, player):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vel_y = r.randint(3, 10)
        self.puntos = r.randint(5, 15)
        self.player = player
        self.img_dir = "./items/obstacle"
        self.img_name = "obs"+str(r.randint(1, 4))+".png"
        self.img = cv.imread(self.img_dir+"/"+self.img_name)
        self.img = cv.resize(self.img, (self.w, self.h))

    def puntoMedio(self, p1, p2):
        return ((p2 + p1)/2)

    def mover(self, obstaculos):
        if self.y < self.player.alto_v:
            self.y += self.vel_y
        else:
            self.player.generarObstaculos(obstaculos)
            obstaculos.remove(self)
            print("Obstaculo eliminado")

    def dibujar(self, cv, img):
        px = int(self.puntoMedio(self.x, self.x+self.w)) - 10
        py = int(self.puntoMedio(self.y, self.y+self.h))
        if self.x >= 0 and self.x + self.w <= img.shape[1] and self.y >= 0 and self.y + self.h <= img.shape[0]:
            img[self.y:self.y + self.h, self.x:self.x + self.w] = self.img
            cv.putText(img, "" + "-" + str(self.puntos),
                       (px, py),
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
