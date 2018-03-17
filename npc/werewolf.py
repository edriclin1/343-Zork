from npc.npc import Npc
import random

class Werewolf(Npc):

    def __init__(self):
        super().__init__()
        super().set_npc_hp(200)
        super().set_npc_attack(random.randint(0, 40))

    def harm(self, player):
        pass		
		