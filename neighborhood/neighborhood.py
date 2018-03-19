from home.home import Home
from observer_pattern.observable import Observable

# Class to create the Neighborhood object. Contains an
# array of homes in a 5x5 list.
#
# @author Edric Lin
# @author Austin Maley
# @version 3/18/18

class Neighborhood(object):

    # number of rows in neighborhood
    num_rows = 5

    # number of columns in the neighborhood
    num_cols = 5

    # Constructor for the Neighborhood class
    def __init__(self):
        super(Neighborhood, self).__init__()

        # array of homes in neighborhood
        self.homes = []
        for i in range(self.num_rows):
            self.homes.append([])
            for j in range(self.num_cols):
                self.homes[i].append(Home());
                monsters = self.homes[i][j].get_inhabitants()
                for monster in monsters:
                    monster.add_observer(self.homes[i][j])

    # Get the array of homes in the neighborhood
    # @return the array of homes
    def get_homes(self):
        return self.homes

    # Set the array of homes in the nieghborhood
    # @param homes the array of homes to set to
    def set_homes(self, homes):
        self.homes = homes
		

	
