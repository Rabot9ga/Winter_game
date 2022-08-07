import pygame



class Gun():

    def __init__(self, screen):
        self.surf=pygame.image.load('img/drop.png')
        self.rect=self.surf.get_rect()
        self.screen=screen
        self.right=False
        self.left=False
        self.rect.centerx=400


    def output(self):
        self.screen.blit(self.surf, self.rect)

    def mov(self):
        if self.right and self.rect.x<800-20:
            self.rect.centerx+=10
        elif self.left and self.rect.x>0:
            self.rect.centerx-=10












