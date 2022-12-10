import numpy as np

class env:

    SIDE = 25 # Half side

    def __init__( self , pos , screen_w , screen_h ):

        self.pos = pos
        self.screen_w = screen_w
        self.screen_h = screen_h

    def reset_pos( self ):
        
        r = np.random.random( 2 )
        inf_lmt = np.array( [ env.SIDE , env.SIDE ] )
        sup_lmt = np.array( [self.screen_w , self.screen_h ] ) - inf_lmt

        self.pos = inf_lmt*r + sup_lmt*( 1 - r )

    def get_edges( self ):

        return np.array([
            self.pos + np.array( [ env.SIDE , env.SIDE ] ),   # BOTTOM RIGHT
            self.pos + np.array( [ env.SIDE , -env.SIDE ] ),  # TOP RIGHT
            self.pos + np.array( [ -env.SIDE , -env.SIDE ] ), # TOP LEFT
            self.pos + np.array( [ -env.SIDE , env.SIDE ] )   # BOTTOM LEFT
        ])

    def get_outer( self ):

        return np.array([
            [ 0 , 0 ],
            [ self.screen_w , 0 ],
            [ self.screen_w , self.screen_h ],
            [ 0 , self.screen_h ]
        ])