from npc.npc import Npc

class Person(Npc):

    def __init__(self):
        super().__init__()
        super().set_npc_hp(100)
        super().set_npc_attack(-1)

    def damage_npc(self, player):
        super().damage_npc(player)