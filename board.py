
class Board(object):
    def __init__(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]

    def print_board(self):
        print('-' * 13)
        for i in range(3):
            for j in range(3):
                print('| {} '.format(' ' if self.board[i][j] == 0 else 'O' if self.board[i][j] > 0 else 'X'), end='')
            print('|')
        print('-' * 13)
            
    def __getitem__(self, i):
        return self.board[i]