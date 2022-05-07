# import sys

# import pygame
# def check_keydown_events(event, ship):
#     ''' it wld respond to the keypresses'''
#     if event.key == pygame.K_RIGHT:
#         ship.moving_right = False
#     elif eventy.key == pygame.K_LEFT:
#         ship.moving_right = False
        
# def check_events(ship):
#     ''' respond to events by the user(keypresses and mouse events)'''
#      #watch for key board and mouse events.
#     for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#             sys.exit()

#        elif event.type == pygame.KEYDOWN:
#            check_keydown_events(event, ship)
       
#        elif event.type == pygame.KEYUP:
#            check_keydown_events(events, ship)
           
#            #if event.type == pygame.K_RIGHT:
#                #move the ship to the right
#             #    ship.rect.centerx += 1

# def update_screen(ai_settings, screen, ship):
#     ''' update images on the screen and flip to the new screen'''
#         #redraw the screen during each pass thrgh loop
#     screen.fill(ai_settings.bg_color)
#     ship.blitme()
        
#     #make the most recently drawn scrren visible.
#     pygame.display.flip()
