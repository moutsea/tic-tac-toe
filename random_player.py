import random


class RandomPlayer:
    def __init__(self):
        pass

    def __repr__(self):
        return 'Random Player'

    def action(self, board):
        steps = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    steps.append([i, j])
        return random.choice(steps)