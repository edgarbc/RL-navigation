from abc import ABC, abstractmethod
import numpy as np


class AbstractTask(ABC):

    def __init(self):
        super().__init__()

    @abstractmethod
    def get_current_state(self):
        # this method should return the agent's current state in the task
        pass

    @abstractmethod
    def execute_action(self, action):
        # this method should perform the specified action in the task, and return the reward
        pass

    @abstractmethod
    def get_allowed_actions(self, state):
        # this method should return the set of actions allowed from the given state
        pass


