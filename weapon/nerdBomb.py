from weapon import Weapon
import random

# Class to create the NerdBomb weapon. Inherits from 
# Weapon class
#
# @author Edric Lin
# @author Austin Maley
# @version 3/18/18

class NerdBomb(Weapon):

    # Constructor for NerdBomb weapon class
    def __init__(self):
        super(NerdBomb, self).__init__()
        super(NerdBomb, self).set_weapon_name('NerdBomb')
        super(NerdBomb, self).set_attack_mod(random.uniform(3, 3.5))
        super(NerdBomb, self).set_num_uses(1)