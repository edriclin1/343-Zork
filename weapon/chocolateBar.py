from weapon.weapon import Weapon
import random

class ChocolateBar(Weapon):
    def __init__(self):
        super().__init__()
        super().set_weapon_name('ChocolateBar')
        super().set_attack_mod(random.uniform(2, 2.4))
        super().set_num_uses(4)