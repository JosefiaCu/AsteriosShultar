import random
import pygame as py
import math



class asteroideEsquerda(py.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = py.image.load("data/meteoro1.png")  # 32x32
        self.image = py.transform.scale(self.image, [55, 55])
        self.rect = py.Rect(50, 55, 100, 100)

        self.rect.x = -900 + random.randint(1, 900)
        self.rect.y = random.randint(1, 720)
        self.speed = 1 + random.random() * 2


    def update(self, *args):
        self.rect.x += self.speed



class asteroideDeCima(py.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = py.image.load("data/meteoro1.png")  # 32x32
        self.image = py.transform.scale(self.image,[55, 55])
        self.rect = py.Rect(50, 55, 100, 100)

        self.rect.x = random.randint(1, 500)
        self.rect.y = -715 + random.randint(2, 720)
        self.speed = 2 + random.random() * 2

    def update(self, *args):
        self.rect.y += self.speed

        if self.rect.bottom > 890:
            self.kill()
            print("cukill")


class asteroideDeBaixo(py.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = py.image.load("data/meteoro1.png")  # 32x32
        self.image = py.transform.scale(self.image, [55, 55])
        self.rect = py.Rect(50, 55, 100, 100)

        self.rect.x = random.randint(1, 900)
        self.rect.y = 720 + random.randint(1, 720)
        self.speed = 1 + random.random() * 2


    def update(self, *args):
        self.rect.y -= self.speed




class asteroideDireita(py.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = py.image.load("data/meteoro1.png")  # 32x32
        self.image = py.transform.scale(self.image, [55, 55])
        self.rect = py.Rect(50, 55, 100, 100)

        self.rect.x = 900 + random.randint(1, 900)
        self.rect.y = random.randint(1, 720)
        self.speed = 1 + random.random() * 2


    def update(self, *args):
        self.rect.x -= self.speed



