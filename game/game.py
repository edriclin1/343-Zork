from observer_pattern.observer import Observer
from neighborhood.neighborhood import Neighborhood
from player.player import Player


class Game(Observer):

    def __init__(self):
        super(Game, self).__init__()
        self.neighborhood = Neighborhood()
        self.player = Player()
        self.current_row = 0
        self.current_col = 0
	self.current_home = self.neighborhood.get_homes()[self.current_row][self.current_col]
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
            self.current_row = new_row
            self.current_col = new_col
            self.set_current_home(self.neighborhood.get_homes()[self.current_row][self.current_col])

    def attack(self):
        self.current_home.damage_monsters(self.player)
        self.player.damage_player(self.current_home.get_inhabitants())

    def get_neighborhood(self):
        return self.neighborhood

    def get_player(self):
        return self.player

    def get_current_home(self):
        return self.current_home

    def get_current_row(self):
        return self.current_row

    def get_current_col(self):
        return self.current_col

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

    def set_current_row(self, current_row):
        self.current_row = current_row

    def set_current_col(self, current_col):
        self.current_col = current_col

    def set_total_num_monsters(self, total_num_monsters):
        self.total_num_monsters = total_num_monsters

    def set_total_num_people(self, total_num_people):
        self.total_num_people = total_num_people

    def set_game_over(self, game_over):
        self.game_over= game_over


	