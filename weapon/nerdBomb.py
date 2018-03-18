from weapon import Weapon
import random

class NerdBomb(Weapon):
    def __init__(self):
        super(NerdBomb, self).__init__()
        super(NerdBomb, self).set_weapon_name('NerdBomb')
        super(NerdBomb, self).set_attack_mod(random.uniform(3, 3.5))
        super(NerdBomb, self).set_num_uses(1)