import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
###

import random, pygame as py
from Player import player
from Asteroisdes import asteroideDeCima
from LaserShot import LaserShot
from time import sleep
from pygame.sprite import Group

py.init()

tela = py.display.set_mode([560, 780])

py.display.set_caption("Homen VS PedraS no espaço HD")

# definições

timer = 0
clock = py.time.Clock()
run = False

ObjetosGroup = py.sprite.Group()
AsteroideGrup = py.sprite.Group()
BackGroudGrup = py.sprite.Group()
ShotGroup: Group = py.sprite.Group()
PlayerGroup = py.sprite.Group()

keys = py.key.get_pressed()

player(ObjetosGroup, PlayerGroup)
shotHeat = 0
Conldonw = False
Conldonw_timer = 0

Recharg = False
Recharg_timer = 0

gameover = False

asteroideDeCima(AsteroideGrup)

# backgroud

bg = py.sprite.Sprite(BackGroudGrup)
bg.image = py.image.load("data/SpaceBg.png")
bg.image = py.transform.scale(bg.image, [560, 780])
bg.rect = bg.image.get_rect()

# musica
py.mixer.music.load("data/MenuStart.wav")
py.mixer.music.play(1)

# sons
shot = py.mixer.Sound("data/Laser2.wav")
explosao = py.mixer.Sound("data/explosao.wav")
Up_sond = py.mixer.Sound("data/MenuStart.wav")
OverHeat = py.mixer.Sound("data/ShotOverHeat.wav")

# fonte
# fonte = py.font.SysFont("comicsans", 30, True)

if __name__ == "__main__":
    run = True

    while run:
        clock.tick(60)  # fps
        for event in py.event.get():
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    run = False
                if event.key == py.K_j and not Conldonw and not gameover:
                    shot.play()
                    newShot = LaserShot(ShotGroup)
                    Recharg = True
                    while Recharg_timer:
                        Recharg_timer = 0
                    newShot.rect.center = player.rect.center
                    shotHeat += 1

        if not gameover:

            Conldonw_timer += 1
            if shotHeat > 23:
                shotHeat = 0
                Conldonw = True
                Conldonw_timer = True
                OverHeat.play()

            if Conldonw_timer > 170:
                Conldonw_timer = 0
                Conldonw = False

            if shotHeat == 0:
                Recharg = False

            if Recharg:
                Recharg_timer += 1
            if Recharg_timer > 100:
                shotHeat = 0
                OverHeat.play()
                Recharg = False
                Recharg_timer = 0

            colisoes = py.sprite.spritecollide(player, AsteroideGrup, False, py.sprite.collide_mask)
            if colisoes:
                gameover = True

            acertos = py.sprite.groupcollide(ShotGroup, AsteroideGrup, True, True, py.sprite.collide_mask)
            if acertos:
                explosao.play()

            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 1:
                    novoAsteroide = asteroideDeCima(AsteroideGrup, ObjetosGroup)

            # desenhar na tela
            BackGroudGrup.draw(tela)
            ShotGroup.draw(tela)
            ObjetosGroup.draw(tela)
            PlayerGroup.draw(tela)

            # update
            ObjetosGroup.update()
            ShotGroup.update()
            PlayerGroup.update()
            py.display.update()
