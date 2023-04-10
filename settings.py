#Setting file for Alien Invasion Game

#Class to store all setting for game
class Settings:
    #initialize games atatic settings
    def __init__(self):
        #initialize game settings for screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship settings
        #self.ship_speed = 1.5
        self.ship_limit = 3 

        #bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3 

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        #setting how game speeds up
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

        #set fleet direction: 1 = moves right, -1 = moves left
        self.fleet_direction = 1

    def initialize_dynamic_settings(self):
        #initialize setting that change during game play
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #fleet_direction of 1 = right, -1 = left
        self.fleet_direction = 1

        #scoring
        self.alien_points = 50

    def increase_speed(self):
        #increase speed settings
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale


