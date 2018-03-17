from weapon.weapon import Weapon

class HersheyKiss(Weapon):
    def __init__(self):
        super().__init__()
        super().set_weapon_name('HersheyKiss')
        super().set_attack_mod(1)
        super().set_num_uses(-1)