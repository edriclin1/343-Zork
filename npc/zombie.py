from npc.npc import Npc
import random

class Zombie(Npc):

    def __init__(self):
        super().__init__()
        super().set_npc_hp(random.randint(50, 100)) #https://www.youtube.com/watch?v=KzqSDvzOFNA
        super().set_npc_attack(random.randint(0, 10))

    def harm(self, player):
        pass		
		