from weapon import Weapon

class HersheyKiss(Weapon):
    def __init__(self):
        super(HersheyKiss, self).__init__()
        super(HersheyKiss, self).set_weapon_name('HersheyKiss')
        super(HersheyKiss, self).set_attack_mod(1)
        super(HersheyKiss, self).set_num_uses(-1)