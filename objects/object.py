
class Object:
	# This class is for walls, lava and the goal. ERIC: maybe we should have another class for having a set of units
    def __init__(self, type, num_units):
    	self.type = type
    	self.pos = [0, 2]
    	self.color = [0, 0, 0]
		self.num_units = num_units
		for i in range (0, num_units):
			self.units[i] = Unit([0,0])

    def display(self):
        # displays itself
        print('object showed')

	

class Unit:
	def __init__(self):
		self.pos = []
		self.color = []
		self.type = []
	
