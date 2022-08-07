import pygame
import random

class Enemy():
    def __init__(self, screen):
        self.surf=pygame.image.load("img/en.png")
        self.rect=self.surf.get_rect()
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.rect.centerx=random.randint(int(self.rect.width/2), self.screen_rect.width-int(self.rect.width/2))
        self.rect.centery=-self.rect.height



    def output(self):
        self.screen.blit(self.surf, self.rect)

    def mov(self):
        self.rect.y+=5
        if self.rect.centery==self.screen_rect.height+self.rect.height:
            self.kill()


