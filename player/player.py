from weapon.hersheyKiss import HersheyKiss
from weapon.sourStraw import SourStraw
from weapon.chocolateBar import ChocolateBar
from weapon.nerdBomb import NerdBomb
import random

# Class to create the Player object. The player starts off
# with an array of 10 random weapons.
#
# @author Edric Lin
# @author Austin Maley
# @version 3/18/18

class Player(object):

    # the possible types of weapons
    weapon_names = [HersheyKiss, SourStraw, ChocolateBar, NerdBomb]

    # the number of weapons the player can hold
    num_weapons = 10;

    # Constructor for the Player class
    def __init__(self):
        super(Player, self).__init__()

        # the player health
        self.player_hp = random.randint(100, 125)

        # the player attack
        self.player_attack = random.randint(10, 20)

        # the array of player weapons
        self.weapons = []
        for i in range(self.num_weapons):
            temp = random.choice(self.weapon_names)()
            self.weapons.append(temp);

    # Called to damage the player based on monsters in a house
    # @param inhabitants the npcs in a house
    def damage_player(self, inhabitants):

        total_player_damage = 0

        for npc in inhabitants:
            total_player_damage = total_player_damage + npc.get_npc_attack()

        updated_player_hp = self.get_player_hp() - total_player_damage
        self.set_player_hp(updated_player_hp)

    # Called to print the list of weapons
    def print_weapons(self):
        for weapon in self.get_weapons():
                print('Weapon: {}\tUses Remaining: {}'.format(weapon.get_weapon_name(), weapon.get_num_uses()))

    # Get the player hp
    # @return the player hp
    def get_player_hp(self):
        return self.player_hp

    # Get the player attack
    # @return the player attack
    def get_player_attack(self):
        return self.player_attack

    # Get the player weapons
    # return the player weapons
    def get_weapons(self):
        return self.weapons

    # Set the player hp
    # @param player_hp the hp to set
    def set_player_hp(self, player_hp):
        self.player_hp = player_hp

    # Set the player attack
    # @param player_attack the attack to set
    def set_player_attack(self, player_attack):
        self.player_attack = player_attack
