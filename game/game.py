from observer_pattern.observer import Observer
from neighborhood.neighborhood import Neighborhood
from player.player import Player


class Game(Observer):

    def __init__(self):
        super().__init__()
        self.neighborhood = Neighborhood()
        self.player = Player()
	self.current_home = neighborhood[current_row][current_col]
	self.turn = 0

    def move(self, new_row, new_col):
        if (new_row < 0 or new_col < 0):
            print('> Invalid input! Please enter a valid row and column to move to.')
        else:
            set_current_home(neighborhood[new_row][new_col])

    def attack(self):
        current_home.damage_monsters(player)
        player.damage_player(current_home.get_inhabitants)

    def get_neighborhood(self):
        return self.neighborhood

    def get_player(self):
        return self.player

    def get_current_home(self):
        return self.current_home

    def set_neighborhood(self, neighborhood):
        self.neighborhood = neighborhood

    def set_player(self, player):
        self.player = player

    def set_current_home(self, current_home):
        self.current_home = current_home



	