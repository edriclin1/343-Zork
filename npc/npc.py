from observer_pattern.observable import Observable

class Npc(Observable):

    def __init__(self):
        super().__init__()
        self.npc_hp = 0
        self.npc_attack = 0.0

    def get_npc_hp(self):
        return self.npc_hp

    def get_npc_attack(self):
        return self.npc_attack

    def set_npc_hp(self, npc_hp):
        self.npc_hp = npc_hp

    def set_npc_attack(self, npc_attack):
        self.npc_attack = npc_attack

    def harm(self, player):
        pass