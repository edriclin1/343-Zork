from weapon import Weapon
import random

class SourStraw(Weapon):
    def __init__(self):
        super(SourStraw, self).__init__()
        super(SourStraw, self).set_weapon_name('SourStraw')
        super(SourStraw, self).set_attack_mod(random.uniform(1, 1.75))
        super(SourStraw, self).set_num_uses(2)