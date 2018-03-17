from weapon.weapon import Weapon
import random

class NerdBomb(Weapon):
    def __init__(self):
        super().__init__()
        super.set_weapon_name('NerdBomb')
        super.set_attack_mod(random.uniform(3, 3.5))
        super.set_num_uses(1)