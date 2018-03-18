from observer_pattern.observer import Observer
from observer_pattern.observable import Observable
from npc.zombie import Zombie
from npc.vampire import Vampire
from npc.ghoul import Ghoul
from npc.werewolf import Werewolf
from npc.person import Person
import random
from copy import deepcopy

# Class to create the Home object. Each home starts off
# with up to 10 monsters.
#
# @author Edric Lin
# @author Austin Maley
# @version 3/18/18

class Home(Observer, Observable):

    # list of possible monster types
    monster_names = [Zombie, Vampire, Ghoul, Werewolf]


    # Constructor for Home class
    def __init__(self):
        super(Home, self).__init__()

        # number of starting monsters
        self.num_monsters = random.randint(0,10)

        # array of monsters
        self.inhabitants = []
        for i in range(self.num_monsters):
            temp = random.choice(self.monster_names)()
            self.inhabitants.append(temp);

    # Called when a monster hp reaches 0
    # @param arg the monster to send to observer
    def update(self, arg):
        
        # remove monster and add person to population
        for npc in self.inhabitants:
            if (npc == arg):
                self.inhabitants.remove(npc)
                self.inhabitants.append(Person())

                # update number of monsters
                self.num_monsters = self.num_monsters - 1

                # print message for user
                print('> You have defeated a {}! It transforms back into a person.'.format(arg.get_npc_name()))
                print('> Updated number of monsters in the house: {}'.format(self.num_monsters))

                # notify the game of population change
	        super(Home, self).notify_observers('')

    # Damage monsters in the house based on player stats
    # @param player the player that damages the monsters
    def damage_monsters(self, player):

        print('')
        print('[Before]')
        self.print_npcs()
        print('')

        # call each npc's damage function
	for npc in self.inhabitants:
            npc.damage_npc(player)

        print('')
        print('[After]')
        self.print_npcs()

        # update weapon count
        player_weapons = player.get_weapons()
        index_mod = 0
        for i in range(len(player_weapons)):

            # index changes when modifying list
            index = i - index_mod

            # reduce weapon uses by 1
            updated_num_uses = player_weapons[index].get_num_uses() - 1
            player_weapons[index].set_num_uses(updated_num_uses)

            # remove weapon if out of uses
            if (updated_num_uses == 0):
                player_weapons.remove(player_weapons[index])
                index_mod = index_mod + 1  


    # print npc list
    def print_npcs(self):
        for npc in self.inhabitants:
            print('NPC: {}\tHP: {}'.format(npc.get_npc_name(), npc.get_npc_hp()))

    # get the number of monsters in the house
    # @return the number of monsters in the house
    def get_num_monsters(self):
        return self.num_monsters

    # get the array of inhabitants in the house
    # @return the array of inhabitants
    def get_inhabitants (self):
        return self.inhabitants

    # set the number of monsters in the house
    # @param num_monsters the number of monsters to set
    def set_num_monsters(self, num_monsters):
        self.num_monsters = num_monsters

    # set the array of inhabitants in the house
    # @param inhabitants the array of inhabitants to set
    def set_inhabitants (self, inhabitants):
        self.inhabitants = inhabitants



	
