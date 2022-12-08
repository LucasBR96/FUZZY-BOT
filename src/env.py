import numpy as np

class env:

    SIDE = 25 # Half side

    def __init__( self , pos ):
        self.pos = pos

    def get_edges( self ):

        return np.array([
            self.pos + np.array( [ env.SIDE , env.SIDE ] ),   # BOTTOM RIGHT
            self.pos + np.array( [ env.SIDE , -env.SIDE ] ),  # TOP RIGHT
            self.pos + np.array( [ -env.SIDE , -env.SIDE ] ), # TOP LEFT
            self.pos + np.array( [ -env.SIDE , env.SIDE ] )   # BOTTOM LEFT
        ]) 