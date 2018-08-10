import numpy as np
from matplotlib import pyplot
from agents.agent import Agent
from objects.object import Object


class World:
    # world where the agent and objects live.

    def __init__(self):
        # create the world

        # parameter setting
        self.size = 10
        self.num_agents = 1
        self.num_walls = 5
        self.num_lava = 5

        # create the arena
        self.arena = np.zeros((self.size, self.size, 3))
        # create walls
        self.walls = self.createWalls()
        # create lava
        self.lava = self.createLava()
        # create the goal
        self.goal = self.createGoal()
        # create agents
        self.agents = self.create_agents()

    def create_walls(self):
        # random creation of walls
        obj = Object('wall')
        return obj

    def create_goal(self):
        # create a random position that is available (no wall, no lava, no agent)
        return self

    def create_agents(self):
        # creates all the agents in the world
        for i in range(0, self.num_agents):
            self.agents[i] = Agent()
        return self.agents

    def display(self):
            self.arena.display()
            self.walls.display()
            self.agent.display()

    def update(self):
        # updates the world one time step

        # updates all the objects in the world
        for i in range(0, self.num_objects):
            self.objects(i).update()

        # update all the agents in the world
        for i in range(0, self.num_agents):
            self.agents(i).update()

