import pygame as py
from Player import player


class LaserShot(py.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = py.image.load("data/LaserShot.png")  # 32x32
        self.image = py.transform.scale(self.image, [60, 55])
        self.rect = self.image.get_rect()

        self.speed = 20

    def update(self, *args):
        self.rect.y -= self.speed

        if self.rect.bottom < -100:
            self.kill()