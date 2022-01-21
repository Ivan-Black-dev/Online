import settings as st
import pygame as pg
from random import randint


def main():
    player_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    x_start = randint(0, )
    pg.init()
    screen = pg.display.set_mode(st.WINDOW_SIZE)
    pg.display.set_caption(st.GAME_NAME)
    clock = pg.time.Clock()
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                return
        clock.tick(st.FPS)
            


if __name__ == '__main__':
    main()