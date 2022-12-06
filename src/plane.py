import numpy as np

class plane:
    
    '''
    
    Bot that "flies" over a plane on constant speed,
    and can turn its direction clock-wise or counter
    clock-wise.

    It is represented by an isocele triangle

    '''
    
    SPEED = 50       # Pixels per second
    ROTSP = np.pi/6  # Hardest it can turn
    BASE  = 5        # Minor side of the triangle, in pixels
    SIDE  = 10       # Major sides

    def __init__( self , pos , theta ):
        
        self.pos   = pos
        self.theta = theta

    def get_u_vector( self ):
        
        theta = self.theta
        vx = np.cos( theta )
        vy = np.sin( theta )
        
        return np.array([ vx , vy ])
 
    def update_pos( self , dt ):
        
        vel_vec = self.get_u_vector()*plane.SPEED
        self.pos = self.pos + vel_vec*dt 

    def update_theta( self , direc , dt):
        
        assert( abs( direc ) <= 1. )

        omega = plane.ROTSP*direc
        theta = self.theta + omega*dt

        if theta < 0:
            theta = 2*np.pi + theta
        self.theta = theta%(2*np.pi)

    def get_triangle( self ) 
        pass


