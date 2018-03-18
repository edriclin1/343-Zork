from observer_pattern.observer import Observer
from neighborhood.neighborhood import Neighborhood
from player.player import Player


class Game(Observer):

    def __init__(self):
        super(Game, self).__init__()
        self.neighborhood = Neighborhood()
        self.player = Player()
	self.current_home = self.neighborhood.get_homes()[0][0]
	self.total_num_monsters = 0
	self.total_num_people = 0
	self.game_over = 0

    # called when a house population changes
    def update(self, arg):

        self.total_num_monsters = self.total_num_monsters - 1
        self.total_num_people = self.total_num_people + 1

    def move(self, new_row, new_col):
        if (new_row < 0 or new_col < 0):
            print('> Invalid input! Please enter a valid row and column to move to.')
        else:
            set_current_home(self.neighborhood.get_homes()[new_row][new_col])

    def attack(self):
        self.current_home.damage_monsters(self.player)
        self.player.damage_player(self.current_home.get_inhabitants())

    def get_neighborhood(self):
        return self.neighborhood

    def get_player(self):
        return self.player

    def get_current_home(self):
        return self.current_home

    def get_total_num_monsters(self):
        return self.total_num_monsters

    def get_total_num_people(self):
        return self.total_num_people

    def get_game_over(self):
        return self.game_over

    def set_neighborhood(self, neighborhood):
        self.neighborhood = neighborhood

    def set_player(self, player):
        self.player = player

    def set_current_home(self, current_home):
        self.current_home = current_home

    def set_total_num_monsters(self, total_num_monsters):
        self.total_num_monsters = total_num_monsters

    def set_total_num_people(self, total_num_people):
        self.total_num_people = total_num_people

    def set_game_over(self, game_over):
        self.game_over= game_over


	