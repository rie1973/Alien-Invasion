#image file from Eric Matthes https://nostarch.com/pythoncrashcourse2e/

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

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    
