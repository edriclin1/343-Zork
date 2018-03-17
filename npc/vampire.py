from npc.npc import Npc
import random

class Vampire(Npc):

    def __init__(self):
        super().__init__()
        super().set_npc_hp(random.randint(100, 200)) #https://www.youtube.com/watch?v=KzqSDvzOFNA
        super().set_npc_attack(random.randint(10, 20))

    def harm(self, player):
        pass		
		