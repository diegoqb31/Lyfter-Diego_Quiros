from Swimmer import Swimmer
from Flyer import Flyer
from Walker import Walker

class Duck(Swimmer, Flyer, Walker):
    
    def __init__(self):
        super().__init__()
