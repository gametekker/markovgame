import numpy as np

from discrete_time_markov.mc import calculate_cumulative_reward_mc
from discrete_time_markov.det import calculate_cumulative_reward

from discrete_time_markov.game_utility import Game

# Define the probability transition matrix
P = np.array([[0.1, 0.4, 0.4, 0.1],
              [0.1, 0.4, 0.4, 0.1],
              [0.1, 0.4, 0.4, 0.1],
              [0.1, 0.4, 0.4, 0.1]])

# Define the rewards and payoffs
r1, r2 = 3, 3  # Reward for mutual cooperation
t1, t2 = 5, 5  # Temptation payoff
p1, p2 = 0, 0  # Punishment payoff
s1, s2 = 1, 1  # Sucker's payoff
gamma = 0.9    # Discount rate

# Define the rewards matrix
rewards_matrix = [
    [r1, r2],  # Payoffs for when both cooperate
    [t1, p2],  # Payoffs for when one defects and the other cooperates
    [p1, t2],  # Payoffs for when one defects and the other cooperates
    [s1, s2]   # Payoffs for when both defect
]

game = Game(P,rewards_matrix,gamma)

cumulative_rewards_p0 = np.zeros(len(P))
cumulative_rewards_p1 = np.zeros(len(P))

print("deterministic")

for i in range(len(P)):
    cumulative_rewards_p0[i] = calculate_cumulative_reward(game,i, 0)
print(cumulative_rewards_p0)

for i in range(len(P)):
    cumulative_rewards_p1[i] = calculate_cumulative_reward(game,i, 1)
print(cumulative_rewards_p1)

print("monte carlo")

for i in range(len(P)):
    cumulative_rewards_p0[i] = calculate_cumulative_reward_mc(game, i, 0)
print(cumulative_rewards_p0)

for i in range(len(P)):
    cumulative_rewards_p1[i] = calculate_cumulative_reward_mc(game, i, 1)
print(cumulative_rewards_p1)

# ask Florian if he wants us to tune the matrix

# do simgd attempting to tune the matrix

# implement Q-learning