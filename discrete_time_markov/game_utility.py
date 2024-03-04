import numpy as np

class Game:
    def __init__(self, transition_matrix, rewards_matrix, gamma):
        """
        Initialize the game with a transition matrix and a rewards matrix.

        Parameters:
        - transition_matrix: A numpy array representing the transition probabilities between states.
        - rewards_matrix: A numpy array or list of lists representing the rewards for each action in each state.
        """
        self.__transition_matrix = np.array(transition_matrix)
        self.rewards_matrix = np.array(rewards_matrix)
        self.gamma=gamma

    def rewards(self, state, player):
        """
        Return the rewards matrix of the game.
        """
        return self.rewards_matrix[state,player]

    def get_gamma(self):
        return self.gamma

    def __getitem__(self,index):
        """
        :param index:
        :return: appropriate entry of transition matrix
        """
        if isinstance(index,int):
            return self.__transition_matrix[index]
        row,col=index
        return self.__transition_matrix[row,col]

    def __len__(self):
        return self.__transition_matrix.shape[0]