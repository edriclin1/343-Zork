from npc.npc import Npc
from weapon.hersheyKiss import HersheyKiss
from weapon.sourStraw import sourStraw 
from weapon.chocolateBar import chocolateBar 
from weapon.nerdBomb import nerdBomb
import random

class Ghoul(Npc):

    def __init__(self):
        super().__init__()
        super().set_npc_hp(random.randint(40, 80)) #https://www.youtube.com/watch?v=KzqSDvzOFNA
        super().set_npc_attack(random.randint(15, 30))

    def damage_npc(self, player):

        # get player attack info
        player_base_attack = player.get_player_attack()
        player_weapons = player.get_Weapons()

        # go through all player weapons
	for weapon in player_weapons:

            # damage equals player attack times weapon attack mod
            weapon_attack_mod = weapon.get_attack_mod()
            player_total_attack = player_base_attack * weapon_attack_mod

            # if weapon is NerdBomb, then 5x damage
            if (weapon.get_weapon_name() == 'NerdBomb'):
                player_total_attack = player_total_attack * 5

            # subtract damage from npc health
            updated_hp = super().get_npc_hp() - player_total_attack
            super().set_npc_hp(updated_hp)

            # if npc health is less than zero notify observer (home)
            if (updated_hp <= 0):
		npc.notifyObservers(super.get_npc_name())

            # reduce weapon uses
            updated_num_uses = weapon.get_num_uses - 1
            weapon.set_num_uses(updated_num_uses)

            # remove weapon if out of uses
            if (updated_num_uses == 0):
                player_weapons.remove(weapon)      
            
        