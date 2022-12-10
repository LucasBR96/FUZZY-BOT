from src.plane import plane
from src.env import env
from src.fuzz import fuzzy_info
from src.model import fuzz_decision

import numpy as np
import pygame
from pygame.locals import *

kb = pygame.key

def is_clockwise( u , v ):

    '''
    check if the orientation between two 2d vectors is clockwise
    by the right hand rule
    '''

    return u[0]*v[1] - u[1]*v[0] < 0

def orientation( a , b , c ):

    '''
    returns if the orietation of segments AB and AC are clockwise

    '''

    u = b - a
    v = c - a
    return is_clockwise( u , v )

def line_seg_intercept( p1 , p2 , q1 , q2 ):
    
    a = orientation( p1 , p2 , q1 )
    b = orientation( p1 , p2 , q2 )
    c = orientation( q1 , q2 , p1 )
    d = orientation( q1 , q2 , p2 )

    return ( a != b ) and( c != d )

class simu:

    # Colision Flags ------------------------------------
    NO_COL    = 0
    INNER_COL = 1
    OUTER_COL = 2

    def __init__( self , pl : plane , sqr : env , interactive : bool = True ):

        self.pl = pl
        self.sqr = sqr
        self.inter = interactive

    def update_plane( self , dt ):

        klst = kb.get_pressed()
        if self.inter:
            s = 0
            if klst[ K_UP ]:
                s = 1
            elif klst[ K_DOWN ]:
                s = -1
        
        else:
            fuzzy_vision = fuzzy_info(
                self.pl.pos,
                self.pl.theta,
                self.sqr.pos,
                self.sqr.SIDE
            )
            s = fuzz_decision( fuzzy_vision )

        self.pl.update_theta( s , dt )
        self.pl.update_pos( dt )

    def switch_mode( self ):
        self.inter = not self.inter
        
        s = "ON" if self.inter else "OFF"
        print( f"interactive mode {s}")

    def update( self , **kwargs ):

        #-------------------------------------------------
        # Updating plane position, interactive mode            
        dt = kwargs.get( 'dt' , 1/30 )
        self.update_plane( dt )

        #--------------------------------------------------
        # checking for colisions and giving proper handling
        while True:

            flag = self.collide()

            if flag == simu.NO_COL:
                break

            if flag == simu.INNER_COL:
                self.sqr.reset_pos()
                continue

            if flag == simu.OUTER_COL:
                sqr = self.sqr
                xlim = np.array( [ 0 , sqr.screen_w ] )
                ylim = np.array( [ 0 , sqr.screen_h ] )

                self.pl.reset_pos( xlim , ylim )

    def collide( self ):

        pl_pts = self.pl.get_triangle()
        sqr_pts = self.sqr.get_edges()
        out_pts = self.sqr.get_outer()

        for i in range( 3 ):
            p1 = pl_pts[ i ]
            p2 = pl_pts[ ( i + 1 )%3 ]
            for j in range( 4 ):

                q1 = sqr_pts[ j ]
                q2 = sqr_pts[ ( j + 1 )%4 ]
                if line_seg_intercept( p1 , p2 , q1 , q2 ):
                    return simu.INNER_COL
                
                q1 = out_pts[ j ]
                q2 = out_pts[ ( j + 1 )%4 ]
                if line_seg_intercept( p1 , p2 , q1 , q2 ):
                    return simu.OUTER_COL

        return simu.NO_COL