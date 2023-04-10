import pygame.font

class Button:
    #initialize attributes for button
    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #button properties and dimensions
        self.width, self.height = 300, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # build and center button rect
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #prep button message inly once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        #change rendered image to text, center text on button
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)