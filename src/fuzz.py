import numpy as np

# For fuzzy position.
def fuzzy_slope( x , start , end , flip = False ):

    if x < start:
        result = 0
    elif x > end:
        result = 1
    else:
        result = ( x - start )/( end - start )
    
    if flip:
        result = 1 - result
    
    return result

# For fuzzy angle.
def fuzzy_hat( x , start , end ):

    if not ( start < x < end ):
        return 0
    
    mid = 0.5*( start + end )
    if x < mid:
        return ( x - start )/( mid - start )
    return ( end - x )/( end - mid )

def fuzz_trap( x , a , b , c , d ):

    if ( a < x < b ):
        return ( x - a )/( b - a )
    if ( c < x < d ):
        return ( d - x )/( d - c )
    if ( b < x < c ):
        return 1
    return 0

def fuzzy_info( plane_pos , plane_theta , box_pos , box_side ):

    x , y = plane_pos
    theta = plane_theta
    box_x , box_y = box_pos

    return np.array([

        fuzzy_slope( x , box_x - box_side, box_x ),           #LEFT
        fuzzy_hat( x , box_x - box_side , box_x + box_side ), #H_BEHIND
        1 - fuzzy_slope( x , box_x, box_x + box_side ),       #RIGHT

        1 - fuzzy_slope( y , box_y - box_side, box_y ),       #UP
        fuzzy_hat( y , box_y - box_side , box_y + box_side ), #V_BEHIND
        fuzzy_slope( y , box_y, box_y + box_side ),           #DOWN

        fuzzy_hat( theta , 0 , np.pi ),                        #DOWN_D
        fuzzy_hat( theta , 0.5*np.pi , 1.5*np.pi ),            #LEFT_D
        fuzzy_hat( theta , np.pi , 2*np.pi ),                  #UP_D
        1 - fuzz_trap( theta , 0 , .5*np.pi , 1.5*np.pi , 2*np.pi )   #RIGHT_D
    ])