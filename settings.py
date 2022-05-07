class Settings():
    ''' A class to store al settings of the game'''

    def __init__(self):
        '''initializing game,s static settings'''
        #screen settings
        self.screen_width = 900
        self.screen_height = 700
        self.bg_color = (250, 250, 250)

       # ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

       # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        #how quickly the game speeds up
        self.speedup_scale = 1.1
        #how quickly the alien point value increases
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def increase_speed(self):
        '''increase speed settings and alien point values.'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        
    def initialize_dynamic_settings(self):
        '''initialize speed settings and alien point values'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor
        self.alien_speed_factor = 1
        
        #fleet_direction of represents right, -1 represnts left
        self.fleet_direction = 1

        #scoring!!!
        self.alien_points = 50
        