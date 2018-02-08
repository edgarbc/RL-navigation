from agents.abstract_agent import AbstractAgent


class BasicQLearner(AbstractAgent):

    def __init__(self, alpha=0.1, gamma=0.9, initial_q=10):
        self.alpha = alpha
        self.gamma = gamma
        self.initial_q = initial_q
        self.Q = dict()

    def expand_Qtable(self, state, allowed_actions):

        # add an entry for this state if none exists
        if state not in self.Q:
            self.Q[state] = {act: self.initial_q for act in allowed_actions}

        # update the Q table entry with any new actions (allows for tasks where actions vary by state, and over time)
        else:
            self.Q[state] = {act: self.Q[state][act] if act in self.Q[state] else self.initial_q
                             for act in allowed_actions}

    def select_action(self, state, allowed_actions):
        self.expand_Qtable(state, allowed_actions)

        # pick an action
        return self.policy.select_action(self.Q[state])

    def update(self, state, action, reward, new_state, new_allowed_actions):
        self.expand_Qtable(new_state, new_allowed_actions)

        # get max Q value of new state
        max_Q = max(self.Q[new_state].values())

        # update Q value
        self.Q[state][action] = self.Q[state][action] + \
                             self.alpha * (reward + self.gamma * max_Q - self.Q[state][action])





class TabularModelBasedRL(AbstractAgent):
    pass



