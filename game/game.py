from observer_pattern.observer import Observer
from neighborhood.neighborhood import Neighborhood
from player.player import Player


class Game(Observer):

    def __init__(self):
        super().__init__()
        self.current_neighborhood = Neighborhood()
        self.current_player = Player()
        self.current_x = 0
        self.current_y = 0