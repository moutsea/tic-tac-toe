
class HumanPlayer:
    def __init__(self):
        pass

    def __repr__(self):
        return 'Human player'

    def action(self, board):
        while True:
            position = input('Please choose your step: ')
            x, y = int(position.split(' ')[0]), int(position.split(' ')[1])
            # x and y needs to minus 1, since human may count from 1
            if x > 3 or y > 3 or board[x-1][y-1] != 0:
                print('Your step is illegal, please enter again')
                continue
            else:
                return [x-1, y-1]