import torch
import random
import numpy as np 
from collections import deque
from ../UNO_GAME/oopsBasedGame.py import UnoGame 

MAX_MEMORY = 1_000_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:

    def __init__(self):
        self.n_games = 0 
        self.epsilon = 0  #randomness
        self.gamma = 0    #discount
        self.memory = deque(maxlen=MAX_MEMORY) #popleft

        pass
    def get_state(self, game):
        pass
    
    def remember(self, state, action, reward, next_state, done):
        pass

    def train_long_memory(self):
        pass

    def train_short_memory(self, state, action, reward, next_state, done):
        pass

    def get_action(self, state):

    
def train():
    agent = Agent()
    game = UnoGame()
    while True :
    #get the old state 
    state_old = agent.get_state(game)

    #get move
    final_move = agent.get_action(state_old)

    #perform move and get new state 
    

    #train the short memory 
    agent.train_short_memory(state_old, final_move, reward, state_new, done)

    #remember
    agent.remember(state_old, final_move, reward, state_new, done)

    if done: 
    #TRAIN the long memory

if __name__ == "__main__":
    pass 
