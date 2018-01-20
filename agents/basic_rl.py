from agents.abstract_agent import AbstractAgent


class BasicQLearner(AbstractAgent):

    def __init__(self, alpha=0.1, gamma=0.9, initial_q=10):
        self.alpha = alpha
        self.gamma = gamma
        self.initial_q = initial_q
        self.Q = dict()

    def set_task(self, task):
        self.task = task
        self.state = task.get_current_state()
        available_actions = self.task.get_allowed_actions(self.state)
        self.Q[self.state] = {act: self.initial_q for act in available_actions}


    def set_policy(self, policy):
        self.policy = policy

    def expand_Qtable(self, state):
        available_actions = self.task.get_allowed_actions(state)

        # add an entry for this state if none exists
        if state not in self.Q:
            self.Q[state] = {act: self.initial_q for act in available_actions}

        # update the Q table entry with any new actions (allows for tasks where actions vary by state, and over time)
        else:
            self.Q[state] = {act: self.Q[state][act] if act in self.Q[state] else self.initial_q
                             for act in available_actions}


    def step(self):
        state = self.state
        self.expand_Qtable(state)

        # pick an action
        act = self.policy.select_action(self.Q[state])

        # execute action
        reward = self.task.execute_action(act)

        # observe new state
        new_state = self.task.get_current_state()
        self.expand_Qtable(new_state)

        # get max Q value of new state
        max_Q = max(self.Q[new_state].values())

        # update Q value
        self.Q[state][act] =self.Q[state][act] + \
                            self.alpha * (reward + self.gamma*max_Q - self.Q[state][act])

        # update current state
        self.state = new_state

        return reward



class TabularModelBasedRL(AbstractAgent):
    pass



