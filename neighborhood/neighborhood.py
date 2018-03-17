from home.home import Home

class Neighborhood(object):

    num_rows = 5
    num_cols = 5

    def __init__(self):
        super().__init__()
        self.homes = []
        for i in range(self.num_rows):
            self.homes.append([])
            for j in range(self.num_cols):
                self.homes[i].append(Home());
                
    def update(self):
        pass		
		

	
