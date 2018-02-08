from abc import ABC, abstractmethod

class AbstractAgent(ABC):

    def set_policy(self, policy):
        self.policy = policy

    @abstractmethod
    def select_action(self, state, allowed_actions):
        pass

    @abstractmethod
    def update(self, state, action, reward, new_state, new_allowed_actions):
        pass
