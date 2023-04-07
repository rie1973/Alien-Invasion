import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #create alien
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load image, set rect attribute
        self.image =pygame.image.load('images/alien.bmp')
        self.rect =self.image.get_rect()

        #start alien top left of screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed
        self.rect.x = self.x
