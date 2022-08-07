import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("img/en.png")
        self.rect=self.image.get_rect()
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.rect.centerx=random.randint(int(self.rect.width/2), self.screen_rect.width-int(self.rect.width/2))
        self.rect.centery=-self.rect.height



    def update(self):
        self.rect.y += 5
        if self.rect.y > self.screen_rect.height:
            self.kill()






