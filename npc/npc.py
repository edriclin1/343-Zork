from observer_pattern.observable import Observable

class Npc(Observable):

    def __init__(self):
        super(Npc, self).__init__()
	self.npc_name = ''
        self.npc_hp = 0
        self.npc_attack = 0.0

    def __eq__(self, other):
        if (self.get_npc_name() == other.get_npc_name() and 
                self.get_npc_hp() == other.get_npc_hp() and 
                self.get_npc_attack() == other.get_npc_attack()):
            return True
        else:
            return False

    def get_npc_name(self):
        return self.npc_name

    def get_npc_hp(self):
        return self.npc_hp

    def get_npc_attack(self):
        return self.npc_attack

    def set_npc_name(self, npc_name):
       self.npc_name = npc_name

    def set_npc_hp(self, npc_hp):
        self.npc_hp = npc_hp

    def set_npc_attack(self, npc_attack):
        self.npc_attack = npc_attack

    def damage_npc(self, player):
        pass