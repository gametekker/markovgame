import numpy as np
from discrete_time_markov.game_utility import Game
#return the next state based on the probability matrix
def mc_probas(game: Game,state):
    bins=np.cumsum([0]+game[state,:-1])
    # Generate a random number between 0 and 1
    random_number = np.random.rand()
    bin_index=np.digitize(random_number,bins)
    return bin_index

def monte_carlo_average(iterations):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(iterations):
                result = func(*args, **kwargs)
                results.append(result)
            avg_result = np.mean(results, axis=0)
            return avg_result
        return wrapper
    return decorator

@monte_carlo_average(iterations=100)
def calculate_cumulative_reward_mc(game: Game, state, player, depth=0):
    cumulative_reward=0
    for depth in range(10):
        if depth == 0:
          cumulative_reward = game.rewards(state, player) # Immediate reward term for player 1
        else:
          cumulative_reward += game.get_gamma() * game.rewards(state, player)  # Immediate reward term for player 1
        next_state = mc_probas(game,state)
        #if next_state!=state:
        state=next_state
    return cumulative_reward