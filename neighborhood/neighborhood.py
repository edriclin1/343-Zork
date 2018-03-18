from home.home import Home
from observer_pattern.observable import Observable

class Neighborhood(object):

    num_rows = 5
    num_cols = 5

    def __init__(self):
        super(Neighborhood, self).__init__()
        self.homes = []
        for i in range(self.num_rows):
            self.homes.append([])
            for j in range(self.num_cols):
                self.homes[i].append(Home());
		monsters = self.homes[i][j].get_inhabitants()
                for monster in monsters:
                    monster.add_observer(self.homes[i][j])

    def get_homes(self):
        return self.homes

    def set_homes(self, homes):
        self.homes = homes
		

	
