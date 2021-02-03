from game import Game

if __name__ == "__main__":
    game = Game()

    print('''
    Welcome to tic toc game!
    Pleaser choose two players!
    r: random player
    h: human player
    ''')

    while len(game.players) < 2:
        p = input('Please choose an player\n')
        if p == 'r':
            game.add_player('r')
        elif p == 'h':
            game.add_player('h')
        else:
            print('Invalid input, please choose again')

    game.play()