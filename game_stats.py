class GameStats():
    '''Track statistics for the game'''

    def __init__(self, ai_settings):
        '''initialize staistics'''
        self.ai_settings = ai_settings
        self.reset_stats()
        
        #start the game in an inactive state
        self.game_active = False
        
        #high score should never be reset
        self.high_score = 0

    def reset_stats(self):
        '''initialize statistics that can change during the game'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1