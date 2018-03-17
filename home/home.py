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
        self.inhabitants = []
        for i in range(self.num_monsters):
            temp = random.choice(self.monster_names)()
            temp.addObserver(self)
            self.inhabitants[i] = temp;

    # called when a monster hp reaches 0
    def update(self, arg):

        # remove monster and add person to population
        self.inhabitants.remove(arg)
        self.inhabitants.append(Person())

        # update number of monsters
        self.num_monsters = self.num_monster - 1

        # print message for user
        print('> You have defeated a {}! It transforms back into a person.'.format(arg))
        print('> Updated number of monsters in the house: {}'.format(self.num_monsters))

    # damage monsters in the house
    def damage_monsters(self, player):

        # call each npc's damage function
	for npc in inhabitants:
            npc.damage_npc(player)

    def get_num_monsters(self):
        return self.num_monsters

    def get_inhabitants (self):
        return self.inhabitants

    def set_num_monsters(self, num_monsters):
        self.num_monsters = num_monsters

    def set_inhabitants (self, inhabitants):
        self.inhabitants = inhabitants



	
