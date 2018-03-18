from npc import Npc
from weapon.hersheyKiss import HersheyKiss
from weapon.sourStraw import SourStraw 
from weapon.chocolateBar import ChocolateBar 
from weapon.nerdBomb import NerdBomb
from player.player import Player
import random

class Vampire(Npc):

    def __init__(self):
        super(Vampire, self).__init__()
        super(Vampire, self).set_npc_name('Vampire')
        super(Vampire, self).set_npc_hp(random.randint(100, 200)) #https://www.youtube.com/watch?v=KzqSDvzOFNA
        super(Vampire, self).set_npc_attack(random.randint(10, 20))	

    def damage_npc(self, player):

        # get player attack info
        player_base_attack = player.get_player_attack()
        player_weapons = player.get_weapons()

        # go through all player weapons
	for weapon in player_weapons:

            # damage equals player attack times weapon attack mod
            weapon_attack_mod = weapon.get_attack_mod()
            player_total_attack = player_base_attack * weapon_attack_mod

            # if weapon is ChocolateBar, then 0 damage
            if (weapon.get_weapon_name() == 'NerdBomb'):
                player_total_attack = 0

            # subtract damage from npc health
            updated_hp = super(Vampire, self).get_npc_hp() - player_total_attack
            super(Vampire, self).set_npc_hp(updated_hp)

            # if npc health is less than zero notify observer (home)
            if (updated_hp <= 0):
		super(Vampire, self).notify_observers(self)

            # reduce weapon uses
            updated_num_uses = weapon.get_num_uses() - 1
            weapon.set_num_uses(updated_num_uses)

            # remove weapon if out of uses
            if (updated_num_uses == 0):
                player_weapons.remove(weapon)	