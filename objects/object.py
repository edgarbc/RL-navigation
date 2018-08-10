

class Object:
    # This class is for walls, lava and the goal.
    def __init__(self, type, num_units):
        self.type = type
        self.pos = [0, 2]
        self.color = [0, 0, 0]
        self.reward = -1
        self.num_units = num_units
        for i in range (0, num_units):
            self.units[i] = Unit([0,0])

    def get_properties(self):
        return [self.type, self.pos, self.color, self.reward]

    def display(self):
        # displays itself
        print('object showed')

