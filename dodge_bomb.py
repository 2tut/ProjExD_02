import sys
import random
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    tmr = 0

    bomb_color = (255, 0, 0)
    bomb_r = 10
    bomb_x = random.randint(0, WIDTH)
    bomb_y = random.randint(0, HEIGHT)
    bomb_img = pg.Surface((bomb_r*2, bomb_r*2))
    bomb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_img, bomb_color, (bomb_r, bomb_r), bomb_r)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        screen.blit(bomb_img, [bomb_x, bomb_y])

        pg.display.update()
        tmr += 1
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
