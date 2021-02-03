from board import Board
from human_player import HumanPlayer
from random_player import RandomPlayer
import os

class Game:
    def __init__(self):
        self.board = Board()
        self.players = []
        self.markers = ['O', 'X']
        self.numbers = [1, -1]


    def add_player(self, player):
        if player == 'h' or player == 'human':
            self.players.append(HumanPlayer())
        elif player == 'r' or player == 'random':
            self.players.append(RandomPlayer())

    
    def game_over(self):

        def row_count(board, row):
            for m in [-1, 1]:
                flag = True
                for i in range(3):
                    if board[row][i] != m:
                        flag = False
                        break
                if flag:
                    return m
            return 0

        def column_count(board, column):
            for m in [-1, 1]:
                flag = True
                for i in range(3):
                    if board[i][column] != m:
                        flag = False
                        break
                if flag:
                    return m
            return 0

        def diagonal_count(board):
            for m in [-1, 1]:
                flag = True
                for i in range(3):
                    if board[i][i] != m:
                        flag = False
                        break

                if flag:
                    return m

                flag = True
                for i in range(3):
                    if board[i][2-i] != m:
                        flag = False
                        break

                if flag:
                    return m

            return 0

        for i in range(3):
            row, col = row_count(self.board, i), column_count(self.board, i)
            if row != 0:
                return row
            elif col != 0:
                return col

        return diagonal_count(self.board)


    def play(self):

        if len(self.players) != 2:
            print('You must assign two players!')
            return 

        current = 0

        while self.game_over() == 0:
            # os.system('clear')
            self.board.print_board()
            player = self.players[current]
            x, y = player.action(self.board)
            print('{} player: {}, choose: {} {}'.format('offensive position' if current == 0 else 'defensive position', player, x, y))
            self.board[x][y] = self.numbers[current]
            current = 1 - current
        # os.system('clear')
        self.board.print_board()
        
        print('{} wins'.format(self.players[1 - current]))