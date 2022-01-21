from http import server
import settings as st
import pygame as pg
from random import randint
import socket


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 4321))
    server.listen()
    client, _ = server.accept()


    player_color = (randint(100, 255), randint(100, 255), randint(100, 255))
    x = randint(0, st.WINDOW_X)
    y = randint(0, st.WINDOW_Y)
    pg.init()
    screen = pg.display.set_mode(st.WINDOW_SIZE)
    pg.display.set_caption(st.GAME_NAME)
    clock = pg.time.Clock()
    while True:


        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.quit()
                return
            elif i.type == pg.KEYDOWN:
                if i.key == pg.K_LEFT:
                    x -= st.PLAYER_SPEED
                if i.key == pg.K_RIGHT:
                    x += st.PLAYER_SPEED
                if i.key == pg.K_UP:
                    y -= st.PLAYER_SPEED
                if i.key == pg.K_DOWN:
                    y += st.PLAYER_SPEED

            client.send(f'{x}, {y}'.encode('utf-8'))

        screen.fill((0, 0, 0))
        pg.draw.rect(screen, player_color, (x, y, 10, 10))
        pg.display.update()
        clock.tick(st.FPS)
            


if __name__ == '__main__':
    main()