import pygame as py
from pygame.locals import *

class player(py.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        player.image = py.image.load("data/nave1.png")  # 32x32
        player.image = py.transform.scale(self.image, [100, 100])
        player.rect = py.Rect(50, 50, 100, 100)

        self.speed = 0
        self.aceleration = 5.5

    def update(self, *args):

        keys = py.key.get_pressed()

        if keys[py.K_w]:
            self.rect.y -= self.aceleration

        if keys[py.K_UP]:
            self.rect.y -= self.aceleration

        if keys[py.K_d]:
            self.rect.x += self.aceleration

        if keys[py.K_RIGHT]:
            self.rect.x += self.aceleration

        if keys[py.K_a]:
            self.rect.x -= self.aceleration

        if keys[py.K_LEFT]:
            self.rect.x -= self.aceleration

        if keys[py.K_s]:
            self.rect.y += self.aceleration

        if keys[py.K_DOWN]:
            self.rect.y += self.aceleration
        else:
            self.speed *= 0.55
        self.rect.y += self.speed


        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0
        if self.rect.bottom > 780:
            self.rect.bottom = 780
            self.speed = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.speed = 0
        if self.rect.right > 560:
            self.rect.right = 560
            self.speed = 0

