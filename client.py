import socket
import pygame as pg
from random import randint
import settings as st

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 4321))


player_color = (randint(100, 255), randint(100, 255), randint(100, 255))
x = randint(0, st.WINDOW_X)
y = randint(0, st.WINDOW_Y)
pg.init()
screen = pg.display.set_mode(st.WINDOW_SIZE)
pg.display.set_caption("Клиент")
clock = pg.time.Clock()


while True:
    
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()
            quit()

    data = client.recv(1024).decode('utf-8') 
    if data:
        screen.fill((0, 0, 0))
        data = data.split(',')
        x = int(data[0])
        y = int(data[1])
        pg.draw.rect(screen, player_color, (x, y, 10, 10))
        pg.display.update()