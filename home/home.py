from observer_pattern.observer import Observer
from observer_pattern.observable import Observable
from npc.zombie import Zombie
from npc.vampire import Vampire
from npc.ghoul import Ghoul
from npc.werewolf import Werewolf
from npc.person import Person
import random

class Home(Observer, Observable):

    monster_names = [Zombie, Vampire, Ghoul, Werewolf]

    def __init__(self):
        super().__init__()
        self.num_monsters = random.randint(0,10)
        self.population = []
        for i in range(self.num_monsters):
            temp = random.choice(self.monster_names)()
            temp.addObserver(self)
            self.population[i] = temp;

    # called when a monster hp reaches 0, when a monster calls notify_observers
    def update(self):
        num_monsters = num_monster - 1
        print('> Updated monster population: {}'.format(num_monsters))		
		

	
