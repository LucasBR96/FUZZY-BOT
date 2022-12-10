import numpy as np

class plane:
    
    '''
    
    Bot that "flies" over a plane on constant speed,
    and can turn its direction clock-wise or counter
    clock-wise.

    It is represented by an isocele triangle

    '''
    
    SPEED = 30       # Pixels per second
    ROTSP = np.pi/4  # Hardest it can turn

    # -----------------------------------------------------
    # The airplane is triangular in shape, these would be its
    # edege points if the center of the plane would align with
    # the center of the coord system
    POINTS = np.array([
        [ 15 , 0. ],
        [ -7 , -7],
        [ -7 , 7]
    ])

    def __init__( self , pos , theta ):
        
        self.pos   = pos
        self.theta = theta

    def reset_pos( self , xlim , ylim ):

        r = np.random.random( 2 )
        inf_lmt = np.array( [ xlim[ 0 ] , ylim[ 0 ] ] )
        sup_lmt = np.array( [ xlim[ 1 ] , ylim[ 1 ] ] )

        self.pos = inf_lmt*r + sup_lmt*( 1 - r )
        self.theta = 0 

    def get_u_vector( self ):
        
        theta = self.theta
        vx = np.cos( theta )
        vy = np.sin( theta )
        
        return np.array([ vx , vy ])
 
    def update_pos( self , dt ):
        
        vel_vec = self.get_u_vector()*plane.SPEED
        self.pos = self.pos + vel_vec*dt 

    def update_theta( self , direc , dt):
        
        try:
            assert( abs( direc ) <= 1. )
        except AssertionError:
            print( direc )

        omega = plane.ROTSP*direc
        theta = self.theta + omega*dt

        if theta < 0:
            theta = 2*np.pi + theta
        self.theta = theta%(2*np.pi)

    def get_triangle( self ): 
                
        direc_vec = self.get_u_vector()
        rot_mat = np.zeros( ( 2 , 2 ) )

        rot_mat[ 0 , 0 ] =  direc_vec[ 0 ]   # cos( x )
        rot_mat[ 0 , 1 ] =  direc_vec[ 1 ]   # sin( x )
        rot_mat[ 1 , 0 ] =  direc_vec[ 1 ]   # sin( x )
        rot_mat[ 1 , 1 ] =  -direc_vec[ 0 ]  # -cos( x )

        return plane.POINTS@rot_mat + self.pos