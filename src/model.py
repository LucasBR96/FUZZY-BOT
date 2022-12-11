import numpy as np

HARD_CLOCK = 0
CLOCKWISE  = 1
SOFT_CLOCK = 2
STRAIGHT   = 3
SOFT_CCLCK = 4
COUT_CLOCK = 5
HARD_CCLCK = 6

OUT_VEC = np.array(
    [1. , .75 , .5 , 0 , -.5 , -.75 , -1. ]
    )

def fuzz_decision( fuzzy_vision ):
    
    #--------------------------------------------------
    # Horizontal vision
    LEFT = fuzzy_vision[ 2 ]
    H_BEHIND = fuzzy_vision[ 1 ]
    RIGHT    = fuzzy_vision[ 0 ]

    #--------------------------------------------------
    # Vertical Vision
    UP = fuzzy_vision[ 3 ]
    V_BEHIND = fuzzy_vision[ 4 ]
    DOWN = fuzzy_vision[ 5 ]

    #--------------------------------------------------
    # Directional Vision
    DOWN_D = fuzzy_vision[ 6 ]
    LEFT_D = fuzzy_vision[ 7 ]
    UP_D   = fuzzy_vision[ 8 ]
    RIGHT_D = fuzzy_vision[ 9 ]

    decision = np.zeros( 5 )

    decision[ STRAIGHT ] = max(
        min( LEFT , V_BEHIND , RIGHT_D ),
        min( RIGHT , V_BEHIND , LEFT_D ),
        min( UP , H_BEHIND , DOWN_D ),
        min( DOWN , H_BEHIND , UP_D )
    )

    decision[ SOFT_CLOCK ] = max(
        min( RIGHT , DOWN , LEFT_D ),
        min( LEFT , UP , RIGHT_D ),
        min( RIGHT , UP , DOWN_D ),
        min( LEFT , DOWN , UP_D )
    )

    decision[ SOFT_CCLCK ] = max(
        min( RIGHT , UP , LEFT_D ),
        min( LEFT , UP , DOWN_D ),
        min( LEFT , DOWN , RIGHT_D ),
        min( RIGHT , DOWN , UP_D )
    )

    decision[ HARD_CLOCK ] = max(
        min( RIGHT , V_BEHIND , DOWN_D ),
        min( DOWN , H_BEHIND , LEFT_D ),
        min( LEFT , V_BEHIND , UP_D ),
        min( UP , H_BEHIND , RIGHT_D )
        
    )

    decision[ HARD_CCLCK ] = max(
        min( RIGHT , V_BEHIND , UP_D ),
        min( DOWN , H_BEHIND , RIGHT_D ),
        min( LEFT , V_BEHIND , DOWN_D ),
        min( UP , H_BEHIND , LEFT_D ),

        min( UP , UP_D ),
        min( RIGHT , RIGHT_D ),
        min( LEFT , LEFT_D ),
        min( DOWN , DOWN_D )
    )

    # direction = np.exp(decision)
    d_sum = max( decision.sum() , 1e-5 )
    resp = np.dot( ( decision ) , OUT_VEC  )/( d_sum )
    return np.clip( resp , -1 , 1. )