import pygame

class Bg():
    def __init__(self, screen):
        self.surf=pygame.image.load("img/bg.jpg")
        self.rect=self.surf.get_rect()
        self.screen=screen

    def out(self):
        self.screen.blit(self.surf, self.rect)
