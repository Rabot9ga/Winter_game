import pygame



class Gun():

    def __init__(self, screen):
        self.surf=pygame.image.load('img/gun.png')
        self.rect=self.surf.get_rect()
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.right=False
        self.left=False
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom


    def output(self):
        self.screen.blit(self.surf, self.rect)

    def mov(self):
        if self.right and self.rect.x<self.screen_rect.width-self.rect.width:
            self.rect.centerx+=10
        elif self.left and self.rect.x>0:
            self.rect.centerx-=10












