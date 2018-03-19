from observer_pattern.observable import Observable

# Class to create the Npc object. Inherits from
# the Observable class.
#
# @author Edric Lin
# @author Austin Maley
# @version 3/18/18

class Npc(Observable):

    # Constructor for the Npc class
    def __init__(self):
        super(Npc, self).__init__()

        # name of npc
	self.npc_name = ''

        # health of npc
        self.npc_hp = 0

        # attack of npc
        self.npc_attack = 0.0

    # Equal compare for comparing npc objects. matches all instance variables
    # @param other the object to compare to
    # return whether the objects are equal
    def __eq__(self, other):
        if (self.get_npc_name() == other.get_npc_name() and 
                self.get_npc_hp() == other.get_npc_hp() and 
                self.get_npc_attack() == other.get_npc_attack()):
            return True
        else:
            return False

    # Get the npc name
    # @return the npc name
    def get_npc_name(self):
        return self.npc_name

    # Get the npc hp
    # @return the npc hp
    def get_npc_hp(self):
        return self.npc_hp

    # Get the npc attack
    # @return the npc attack
    def get_npc_attack(self):
        return self.npc_attack

    # Set the npc_name
    # @param npc_name the name to set
    def set_npc_name(self, npc_name):
       self.npc_name = npc_name

    # Set the npc_hp
    # @param npc_hp the hp to set
    def set_npc_hp(self, npc_hp):
        self.npc_hp = npc_hp

    # Set the npc attack
    # @param npc_attack the attack to set
    def set_npc_attack(self, npc_attack):
        self.npc_attack = npc_attack

    # Method to damage the npc. overidden by inheriting classes
    # @param player the player that attacks
    def damage_npc(self, player):
        pass