from worlds import world


class Agent(world):
    # agent class
    def __init__(self):
        self.pos = [0,0]
        self.define_policy()
        self.color = [0, 0, 1]
        self.reward = 0
        self.task = 0
        self.world = world  # not quite sure how this is done but the agent needs to have access to the worlds
        # methods in order to access the objects

    def get_pos(self):
        # returns the current position of the agent
        return self.pos

    def get_object(self, direction):
        # returns the object that is located in the direction with respect to the current position of the agent
        # ERIC: how does the agent have access to the world? does it have a copy of the arena?
        return self.position + north

    def sense_world(self):
        # returns what is the positions that the agent is allowed to sense
        return [get_object('north'), get_object('south'), get_object('east'), get_object('west')]

    def display(self):
        # displays the agent
        pass
