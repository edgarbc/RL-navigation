from abc import ABC, abstractmethod
import random

class AbstractPolicy(ABC):

    def __init(self):
        super().__init__()

    @abstractmethod
    def select_action(self, values):
        # this method should accept a dict of action-value pairs and return an action
        pass


class EGreedyPolicy(AbstractPolicy):

    def __init__(self, epsilon=0.9):
        self.epsilon = epsilon

    def select_action(self, values):
        act_value_pairs = list(values.items())
        act_value_pairs.sort(key=lambda x:x[1], reverse=True)
        if random.random() < self.epsilon:
            return act_value_pairs[0][0]
        else:
            rand_index = random.randint(1,len(act_value_pairs)-1)
            try:
                return act_value_pairs[rand_index][0]
            except:
                print('check')