from observer_pattern.observer import Observer
from neighborhood.neighborhood import Neighborhood
from player.player import Player

# Class to create the game object. Holds an
# instance of a player and a neighborhood.
#
# @author Edric Lin
# @author Austin Maley
# @version 3/18/18

class Game(Observer):


    # Consutrucor for the game class
    def __init__(self):
        super(Game, self).__init__()

        # the game neighborhood
        self.neighborhood = Neighborhood()

        # the game player
        self.player = Player()

        # current player location row
        self.current_row = 0

        # current player location column
        self.current_col = 0

        # current home the player is in
        self.current_home = self.neighborhood.get_homes()[self.current_row][self.current_col]

        # total monster population
        self.total_num_monsters = self.count_monsters()

        # total people population
        self.total_num_people = 0

        # game over status
        self.game_over = 0

    # Called when a house population changes
    # @param arg information passed by the observable
    def update(self, arg):

        self.total_num_monsters = self.total_num_monsters - 1
        self.total_num_people = self.total_num_people + 1

    # Used to move the player to a different home array location
    # @param new_row the new row to move to
    # @param new_col the new col to move to
    def move(self, new_row, new_col):
        if (new_row < 0 or new_col < 0):
            print('> Invalid input! Please enter a valid row and column to move to.')
        else:
            self.current_row = new_row
            self.current_col = new_col
            self.set_current_home(self.neighborhood.get_homes()[self.current_row][self.current_col])

    # Used to attack in the game. Players and Npcs take damage accordingly
    def attack(self):
        self.current_home.damage_monsters(self.player)
        self.player.damage_player(self.current_home.get_inhabitants())

    # Count the current population of monsters
    # @return the current population of monsters
    def count_monsters(self):
        count = 0
        for row in self.neighborhood.get_homes():
            for home in row:
                count = count + home.get_num_monsters()
        return count

    # Checks if game is over. sets game_over to 1 if win, and -1 if lose.
    def check_game_over(self):
        if (self.total_num_monsters == 0):
            self.set_game_over(1)
        elif (self.player.get_player_hp() <= 0):
            self.set_game_over(-1)
        else:
            self.set_game_over(0)

    # Get the game neighborhood
    # @return the game neighborhood
    def get_neighborhood(self):
        return self.neighborhood

    # Get the game player
    # @return the game player
    def get_player(self):
        return self.player

    # Get the current home the player is in
    # @return the current home the player is in
    def get_current_home(self):
        return self.current_home

    # Get the current row the player is in
    # @return the current row the player is in
    def get_current_row(self):
        return self.current_row

    # Get the current column the player is in
    # @return the current column the player is in
    def get_current_col(self):
        return self.current_col

    # Get the total monster population
    # @return the total monster population
    def get_total_num_monsters(self):
        return self.total_num_monsters

    # Get the game over status. 1 is win -1 is lose and 0 otherwise
    # @return the game over status
    def get_game_over(self):
        return self.game_over

    # Set the game neighborhood
    # @param the neighborhood to set to
    def set_neighborhood(self, neighborhood):
        self.neighborhood = neighborhood

    # Set the game player
    # @param the player to set to
    def set_player(self, player):
        self.player = player

    # Set the current home
    # @param the home to set to
    def set_current_home(self, current_home):
        self.current_home = current_home

    # Set the player row location
    # @param the row to set to
    def set_current_row(self, current_row):
        self.current_row = current_row

    # Set the player column location
    # @param the column to set to
    def set_current_col(self, current_col):
        self.current_col = current_col

    # Set the game monster population
    # @param the population to set to
    def set_total_num_monsters(self, total_num_monsters):
        self.total_num_monsters = total_num_monsters

    # Set the game over status. 1 is win, -1 is lose, and 0 otherwise.
    # @param the status to set to
    def set_game_over(self, game_over):
        self.game_over= game_over


	