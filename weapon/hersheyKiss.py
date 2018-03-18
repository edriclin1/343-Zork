from weapon import Weapon

# Class to create the HersheyKiss weapon. Inherits from 
# Weapon class
#
# @author Edric Lin
# @author Austin Maley
# @version 3/18/18

class HersheyKiss(Weapon):
    def __init__(self):
        super(HersheyKiss, self).__init__()
        super(HersheyKiss, self).set_weapon_name('HersheyKiss')
        super(HersheyKiss, self).set_attack_mod(1)
        super(HersheyKiss, self).set_num_uses(-1)