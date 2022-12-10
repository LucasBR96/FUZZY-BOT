import pygame
from pygame.locals import *

from src.plane import plane
from src.env import env
from src.simmu import simu

import numpy as np
import sys

SCREEN_W , SCREEN_H = 1000 , 600
BACKGROUND = ( 255 , 255 , 255 )
PLANE_COLOR = ( 0 , 0 , 0 )
BOX_COLOR = ( 0 , 0 , 255 )

DISPLAY_SURF = pygame.display.set_mode( ( SCREEN_W , SCREEN_H ) )
holding_up , holding_down = False , False

pl = plane(
    np.array([ SCREEN_W/2 , SCREEN_H/2 ]),
    0
)
sqr = env(
    0.75*np.array([ SCREEN_W , SCREEN_H ]),
    SCREEN_W,
    SCREEN_H
)
simm = simu( pl , sqr )

dt = 1/45
if __name__ == "__main__":
    # keep game running till running is true
    while True:

        # Check for event if user has pushed
        # any event in queue
        for event in pygame.event.get():

            # if event is of type quit then set
            # running bool to false
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        simm.update( dt = dt )

        #-------------------------------------------------
        # Drawing the plane

        # set background color to our window
        DISPLAY_SURF.fill(BACKGROUND)

        pl_points = pl.get_triangle()
        pygame.draw.lines( DISPLAY_SURF , PLANE_COLOR , True , pl_points, width = 2 )

        sqr_points = sqr.get_edges()
        pygame.draw.lines( DISPLAY_SURF , BOX_COLOR , True , sqr_points, width = 2 )
        
        # Update our window
        pygame.display.update()