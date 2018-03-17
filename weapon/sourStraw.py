from weapon.weapon import Weapon
import random

class SourStraw(Weapon):
    def __init__(self):
        super().__init__()
        super().set_weapon_name('SourStraw')
        super().set_attack_mod(random.uniform(1, 1.75))
        super().set_num_uses(2)