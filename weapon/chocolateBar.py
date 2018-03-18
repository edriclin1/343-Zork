from weapon import Weapon
import random

class ChocolateBar(Weapon):
    def __init__(self):
        super(ChocolateBar, self).__init__()
        super(ChocolateBar, self).set_weapon_name('ChocolateBar')
        super(ChocolateBar, self).set_attack_mod(random.uniform(2, 2.4))
        super(ChocolateBar, self).set_num_uses(4)