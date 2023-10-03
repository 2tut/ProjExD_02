import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


delta = {
    pg.K_UP: (0, -5),
    pg.K_DOWN: (0, +5),
    pg.K_LEFT: (-5, 0),
    pg.K_RIGHT: (+5, 0),
}

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")

    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_img_x = 900
    kk_img_y = 400
    kk_img_rect = kk_img.get_rect()
    kk_img_rect.center = kk_img_x, kk_img_y

    clock = pg.time.Clock()
    tmr = 0

    bomb_color = (255, 0, 0)
    bomb_r = 10
    bomb_x = random.randint(0, WIDTH)
    bomb_y = random.randint(0, HEIGHT)

    bomb_img = pg.Surface((bomb_r*2, bomb_r*2))
    bomb_img.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_img, bomb_color, (bomb_r, bomb_r), bomb_r)
    bomb_img_rct = bomb_img.get_rect()
    bomb_img_rct.center = bomb_x, bomb_y

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        keys = pg.key.get_pressed()
        kk_speeds = [0, 0]
        for key, mv in delta.items():
            if (keys[key]):
                kk_speeds[0] += mv[0]
                kk_speeds[1] += mv[1]

        kk_img_rect.move_ip(kk_speeds)
        bomb_img_rct.move_ip(5, 5)

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_img_rect)
        screen.blit(bomb_img, bomb_img_rct)

        pg.display.update()

        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
