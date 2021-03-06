from npc import Npc
from weapon.hersheyKiss import HersheyKiss
from weapon.sourStraw import SourStraw 
from weapon.chocolateBar import ChocolateBar 
from weapon.nerdBomb import NerdBomb
from player.player import Player
import random

# Class to create the Werewolf object. Inherits from
# the Npc class.
#
# @author Edric Lin
# @author Austin Maley
# @version 3/18/18

class Werewolf(Npc):

    # Constructor for Werewolf class
    def __init__(self):
        super(Werewolf, self).__init__()
        super(Werewolf, self).set_npc_name('Werewolf')
        super(Werewolf, self).set_npc_hp(200)
        super(Werewolf, self).set_npc_attack(random.randint(0, 40))

    # Called to damage the npc based on player weapons
    # @param player the player that damages the npc
    def damage_npc(self, player):

        # get player attack info
        player_base_attack = player.get_player_attack()
        player_weapons = player.get_weapons()

        # go through all player weapons
	for weapon in player_weapons:

            # damage equals player attack times weapon attack mod
            weapon_attack_mod = weapon.get_attack_mod()
            player_total_attack = player_base_attack * weapon_attack_mod

            # if weapon is NerdBomb, then 5x damage
            if (weapon.get_weapon_name() == 'ChocolateBar' or weapon.get_weapon_name() == 'SourStraw'):
                player_total_attack = 0

            # subtract damage from npc health
            updated_hp = super(Werewolf, self).get_npc_hp() - player_total_attack
            super(Werewolf, self).set_npc_hp(updated_hp)

            # if npc health is less than zero notify observer (home)
            if (updated_hp <= 0):
		super(Werewolf, self).notify_observers(self)