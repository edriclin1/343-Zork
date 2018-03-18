# Class to create the Weapon object. 
#
# @author Edric Lin
# @author Austin Maley
# @version 3/18/18

class Weapon(object):

    # Constructor for weapon object
    def __init__(self):
        super(Weapon, self).__init__()

        # the weapon name
        self.weapon_name = ''

        # the weapon attack mod for player attack
        self.attack_mod = 0

        # the number of uses the weapon has
        self.num_uses = 0


    # get the weapon name
    # @return the weapon name
    def get_weapon_name(self):
        return self.weapon_name
        
    # get the attack mod
    # @return the attack mod
    def get_attack_mod(self):
        return self.attack_mod

    # get the number of uses
    # return the number of uses
    def get_num_uses(self):
        return self.num_uses

    # set the weapon name
    # @param weapon_name the name to set
    def set_weapon_name(self, weapon_name):
        self.weapon_name = weapon_name

    # set the attack mod
    # @param attack_mod the attack mod to set
    def set_attack_mod(self, attack_mod):
        self.attack_mod = attack_mod

    # set the number of uses
    # @param the number of uses to set
    def set_num_uses(self, num_uses):
        self.num_uses = num_uses