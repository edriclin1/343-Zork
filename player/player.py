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
            temp = random.choice(self.weapon_names)()
            self.weapons[i] = temp;
		