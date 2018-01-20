from abc import ABC, abstractmethod

class AbstractAgent(ABC):

    def __init(self):
        super().__init__()

    @abstractmethod
    def set_task(self, task):
        pass

    @abstractmethod
    def set_policy(self, policy):
        pass

    @abstractmethod
    def step(self):
        pass