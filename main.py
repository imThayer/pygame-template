#MAIN TEMPLATE

import pygame, sys
import random
import math
import os
from os.path import join
from random import randint as rnd
from pygame.time import delay as slp

import assets.colors as clrs
import config as cfig
import classes_and_objects.shapes as shapes
import classes_and_objects.boxes as boxes

def init_game():
    """Initiates Pygame, Pygame.font, and sets the Screen window and caption"""
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(cfig.CAPTION) # Window Caption
    # pygame.display.set_icon(ICON) #UNCOMMENT WHEN ICON IS DEFINED

    #Pygame Window
    window = pygame.display.set_mode((cfig.SCREEN_WIDTH,cfig.SCREEN_HEIGHT))
    return window

# Draw Function to update graphics
def draw(window):
    """DRAW FUNCTION | allows screen graphics to be added"""
    #BACKGROUND
    window.fill(clrs.WHITE) # 15
    

    #FOREGROUND
    

    #UPDATE DISPLAY
    pygame.display.update()

def handle_events():
    """Handles any pygame event such as key input"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            return False
    
    keys = pygame.key.get_pressed()

    return True

def main(): # MAIN FUNCTION
    """Main Function : main"""
    window = init_game()
    clock = pygame.time.Clock()
    # ADD ALL OBJECTS/CLASSES BELOW HERE

    
    
    # ADD ALL OBJECTS/CLASSES ABOVE HERE
    run = True
    while run: # run set to true, program runs while run is true.

        clock.tick(cfig.FPS) # FPS Tick

        run = handle_events()
        

        
        draw(window) # UPDATES SCREEN

    pygame.quit()
    sys.exit()
    quit()
# ADD CLASSES HERE



# ADD CLASSES ABOVE
if __name__ == "__main__": 
    main()