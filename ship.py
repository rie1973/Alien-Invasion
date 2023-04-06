#image file from Eric Matthes https://nostarch.com/pythoncrashcourse2e/

import pygame

#create ship class
class Ship:

    #initialize ship, set start position
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #load ship image, get rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #start new ship at center bottom of screen
        self.rect.midbottom = self.screen_rect.midbottom

        #movement flag
        self.moving_right = False

    def update(self):
        if self.moving_right:
            self.rect.x += 1
    

    #draw shop at current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
