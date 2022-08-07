import pygame
import sys
from some_bullet import Bull
from enemy import Enemy
import random


SCORE=0
LIFE = 3
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


def updating(screen, gun, bg, enemies, bullets, f1, f2, width, height):
    global SCORE, LIFE
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
        if enemy.rect.centery==gun.rect.centery:
            LIFE-=1
        if LIFE<1:
            text3 = f2.render('YOU LOST', True, (200, 10, 10))
            txt=text3.get_rect()
            txt.centerx=width//2
            txt.centery=height//2
            screen.blit(text3, txt)




    text1 = f1.render('Your score: '+str(SCORE), True, (200, 10, 10))
    screen.blit(text1, (800, 0))
    text2 = f1.render('Your life: ' + str(LIFE if LIFE>0 else 0), True, (200, 10, 10))
    screen.blit(text2, (800, 25))

    pygame.display.update()






