from npc.npc import Npc
import random

class Ghoul(Npc):

    def __init__(self):
        super().__init__()
        super().set_npc_hp(random.randint(40, 80)) #https://www.youtube.com/watch?v=KzqSDvzOFNA
        super().set_npc_attack(random.randint(15, 30))

    def harm(self, player):
        pass		
		