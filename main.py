import pygame
from some_gun import Gun
import game_event
from bground import Bg
import random


WIDTH=1024
HEIGHT=768

pygame.init()
pygame.font.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
framerate=pygame.time.Clock()
pygame.display.set_caption('Gaming')

pygame.time.set_timer(pygame.USEREVENT, random.randint(500, 1500))

f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 150)




gun=Gun(screen)
bg=Bg(screen)
enemies=pygame.sprite.Group()
bullets=pygame.sprite.Group()


while True:
    framerate.tick(60)

    game_event.polling(gun, screen, bullets, enemies)



    game_event.updating(screen, gun, bg, enemies, bullets, f1, f2, WIDTH, HEIGHT)




