

class Agent:
    # agent class
    def __init__(self):
        self.pos = [0,0]
		self.define_policy()
		self.color = [0, 0, 1]
		self.reward = 0
		self.task = 0

    def get_pos(self):
        # returns the current position of the agent
        return self.pos

    def display(self):
        pass
	
	