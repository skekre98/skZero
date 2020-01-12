import sys
import os
from board.move import Move
from stockfish import Stockfish

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
MODEL = "{}/skZero-model".format(BASE_DIR)

class SKZero:

    def __init__(self):
        self.AI = Stockfish(MODEL)
        self.AI.set_skill_level(100)
    
    def get_move(self):
        return self.AI.get_best_move()
