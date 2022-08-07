import pygame
import sys
from some_bullet import Bull
from enemy import Enemy
import random


SCORE=0
def polling(gun, screen, bullets, enemies):
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
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_RIGHT:
                gun.right=False
            elif i.key == pygame.K_LEFT:
                gun.left=False
        elif i.type == pygame.USEREVENT:
            enemies.add(Enemy(screen))


def updating(screen, gun, bg, enemies, bullets, f1):
    global SCORE
    bg.out()
    enemies.draw(screen)
    enemies.update()
    bullets.draw(screen)
    bullets.update()
    gun.mov()
    gun.output()

    for enemy in enemies:
        for bullet in bullets:
            if enemy.rect.center[0]-enemy.rect.height<bullet.rect.center[0]<enemy.rect.center[0]+enemy.rect.height and enemy.rect.center[1]-enemy.rect.height<bullet.rect.center[1]<enemy.rect.center[1]+enemy.rect.height:
                enemy.kill()
                bullet.kill()
                SCORE+=1

    text1 = f1.render('Your score: '+str(SCORE), True, (200, 10, 10))
    screen.blit(text1, (800, 0))

    pygame.display.update()






