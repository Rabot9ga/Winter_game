import pygame
from some_gun import Gun
import game_event
from bground import Bg
from enemy import Enemy

WIDTH=1024
HEIGHT=768
pygame.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
framerate=pygame.time.Clock()
pygame.display.set_caption('Gaming')






gun=Gun(screen)
bg=Bg(screen)
enemy=Enemy(screen)



while True:
    framerate.tick(60)

    game_event.polling(gun, screen)


    game_event.updating(screen, gun, bg, enemy)

