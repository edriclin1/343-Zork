from weapon import Weapon
import random

# Class to create the ChocolateBar weapon. Inherits from 
# Weapon class
#
# @author Edric Lin
# @author Austin Maley
# @version 3/18/18

class ChocolateBar(Weapon):

    # Constructor for ChocolateBar weapon class
    def __init__(self):
        super(ChocolateBar, self).__init__()
        super(ChocolateBar, self).set_weapon_name('ChocolateBar')
        super(ChocolateBar, self).set_attack_mod(random.uniform(2, 2.4))
        super(ChocolateBar, self).set_num_uses(4)