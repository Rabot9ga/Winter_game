import pygame
import random
class Bull(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("img/drop.png")
        self.rect=self.image.get_rect()
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.rect.centery=self.screen_rect.height+self.rect.height
        self.screen=screen
        self.flag=False



    def update(self):
        if self.flag and self.rect.y > -self.rect.height:
            self.rect.y-=10
            if self.rect.y<-self.rect.height:
                self.kill()








