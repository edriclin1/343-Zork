from npc import Npc

# Class to create the Person object. Inherits from
# the Npc class.
#
# @author Edric Lin
# @author Austin Maley
# @version 3/18/18

class Person(Npc):

    # Constructor for Person class
    def __init__(self):
        super(Person, self).__init__()
        super(Person, self).set_npc_name('Person')
        super(Person, self).set_npc_hp(100)
        super(Person, self).set_npc_attack(-1)

    # Called to damage the npc based on player weapons
    # @param player the player that damages the npc
    def damage_npc(self, player):
        super(Person, self).damage_npc(player)