import pygame
import sys
import some_gun



def polling(gun, screen):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                gun.right=True
            elif i.key == pygame.K_LEFT:
                gun.left=True
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_RIGHT:
                gun.right=False
            elif i.key == pygame.K_LEFT:
                gun.left=False


def updating(screen, gun, bg, enemy):

    bg.out()
    enemy.output()
    enemy.mov()
    gun.mov()
    gun.output()

    pygame.display.update()






