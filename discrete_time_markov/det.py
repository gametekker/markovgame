from discrete_time_markov.game_utility import Game
from functools import lru_cache

@lru_cache(maxsize=None)  # Set maxsize to None for an unbounded cache
def calculate_cumulative_reward(game: Game, state, player, depth=0):
    if depth == 10:
        return 0
    if depth == 0:
        cumulative_reward = game.rewards(state, player)  # Immediate reward term for player 1
    else:
        cumulative_reward = game.get_gamma() * game.rewards(state, player)  # Immediate reward term for player 1
    for next_state in range(len(game)):
        #if next_state != state:
        cumulative_reward += game[state,next_state] * calculate_cumulative_reward(game,next_state, player, depth+1)
    return cumulative_reward