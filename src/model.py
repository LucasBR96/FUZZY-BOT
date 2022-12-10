import numpy as np

HARD_CLOCK = 0
SOFT_CLOCK = 1
STRAIGHT   = 2
SOFT_CCLCK = 3
HARD_CCLCK = 4

OUT_VEC = np.array([
    [ -1. , -.5 , 0 , .5 , 1. ]
])

def fuzz_decision( fuzzy_vision ):
    
    LEFT = fuzzy_vision[ 0 ]
    DOWN = fuzzy_vision[ 1 ]
    DOWN_D = fuzzy_vision[ 2 ]
    LEFT_D = fuzzy_vision[ 3 ]
    UP_D   = fuzzy_vision[ 4 ]
    RIGHT_D = fuzzy_vision[ 5 ]