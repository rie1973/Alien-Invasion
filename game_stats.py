class GameStats:
    #track stats for game
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        #start game in active state
        self.game_active = True

        #start game in inactive state
        self.game_active = False

    def reset_stats(self):
    #initialize stats tat can change during game play
        self.ships_left =self.settings.ship_limit
