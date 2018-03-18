from weapon.hersheyKiss import HersheyKiss
from weapon.sourStraw import SourStraw
from weapon.chocolateBar import ChocolateBar
from weapon.nerdBomb import NerdBomb
import random

class Player(object):

    weapon_names = [HersheyKiss, SourStraw, ChocolateBar, NerdBomb]
    num_weapons = 10;

    def __init__(self):
        super(Player, self).__init__()
        self.player_hp = random.randint(100, 125)
        self.player_attack = random.randint(10, 20)
        self.weapons = []
        for i in range(self.num_weapons):
            temp = random.choice(self.weapon_names)()
            self.weapons.append(temp);

    def damage_player(self, inhabitants):

        total_player_damage = 0

        for npc in inhabitants:
            total_player_damage = total_player_damage + npc.get_npc_attack()

        updated_player_hp = self.get_player_hp() - total_player_damage
        self.set_player_hp(updated_player_hp)

    def print_weapons(self):
        for weapon in self.get_weapons():
                print('Weapon: {}\tUses Remaining: {}'.format(weapon.get_weapon_name(), weapon.get_num_uses()))

    def get_player_hp(self):
        return self.player_hp

    def get_player_attack(self):
        return self.player_attack

    def get_weapons(self):
        return self.weapons

    def set_player_hp(self, player_hp):
        self.player_hp = player_hp

    def set_player_attack(self, player_attack):
        self.player_attack = player_attack
