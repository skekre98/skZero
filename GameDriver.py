import pygame as pg

pg.init()
gameDisplay = pg.display.set_mode((800,800))
pg.display.set_caption("skZero")
clock = pg.time.Clock()

quitGame = False

while not quitGame:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quitGame = True
            pg.quit()
            quit()


    pg.display.update()
    clock.tick(60)

