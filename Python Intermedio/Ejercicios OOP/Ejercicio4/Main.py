from Torso import Torso
from Head import Head 
from Arm import Arm 
from Leg import Leg 
from Hand import Hand 
from Feet import Feet

class Main:
    
    right_hand = Hand()
    left_hand = Hand()
    
    right_arm = Arm(right_hand)
    left_arm = Arm(left_hand)
    
    right_feet = Feet()
    left_feet = Feet()
    
    right_leg = Leg(right_feet)
    left_leg = Leg(left_feet)
    
    head = Head()
    
    torso = Torso(head, right_arm, left_arm, right_leg, left_leg)
    
Main()