import pygame
import sys
from some_bullet import Bull



def polling(gun, screen, bullets):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_RIGHT:
                gun.right=True
            elif i.key == pygame.K_LEFT:
                gun.left=True
            elif i.key ==pygame.K_SPACE:
                bullet=Bull(screen)
                bullet.rect.centerx=gun.rect.centerx
                bullet.flag=True
                bullets.add(bullet)
                print(len(bullets))
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_RIGHT:
                gun.right=False
            elif i.key == pygame.K_LEFT:
                gun.left=False


def updating(screen, gun, bg, enemy, bullets):

    bg.out()
    enemy.output()
    enemy.mov()
    bullets.draw(screen)
    bullets.update()
    gun.mov()
    gun.output()



    pygame.display.update()






