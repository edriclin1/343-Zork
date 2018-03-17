from weapon.hersheyKiss import HersheyKiss
from weapon.sourStraw import SourStraw
from weapon.chocolateBar import ChocolateBar
from weapon.nerdBomb import NerdBomb
import random

class Player(object):

    weapon_names = [HersheyKiss, SourStraw, ChocolateBar, NerdBomb]
    num_weapons = 10;

    def __init__(self):
        super().__init__()
        self.player_hp = random.randint(100, 125)
        self.player_attack = random.randint(10, 20)
        self.weapons = []
        for i in range(self.num_weapons):
            temp = random.choice(self.weapon_names))()
            self.weapons[i] = temp;

    def damage_player(self, population):
        

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
