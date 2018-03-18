class Weapon(object):

    def __init__(self):
        super(Weapon, self).__init__()
        self.weapon_name = ''
        self.attack_mod = 0
        self.num_uses = 0

    def get_weapon_name(self):
        return self.weapon_name
        
    def get_attack_mod(self):
        return self.attack_mod

    def get_num_uses(self):
        return self.num_uses

    def set_weapon_name(self, weapon_name):
        self.weapon_name = weapon_name

    def set_attack_mod(self, attack_mod):
        self.attack_mod = attack_mod

    def set_num_uses(self, num_uses):
        self.num_uses = num_uses