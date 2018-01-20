from agents.basic_rl import BasicQLearner
from policies.basic_policies import EGreedyPolicy
from tasks.grid_world import BasicGridWorld
from matplotlib import pyplot as plt
import numpy as np

agent = BasicQLearner()
agent.set_task(BasicGridWorld())
agent.set_policy(EGreedyPolicy(epsilon=0.9))
sum_steps = 10000

reward_history = [0]*sum_steps
for i in range(1, sum_steps):
    reward_history[i] = agent.step()
    print('step {step}, cumulative reward = {rew}'.format(step=i, rew=sum(reward_history)))

plt.plot(np.cumsum(reward_history))
plt.show()

