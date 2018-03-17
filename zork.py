from game.game import Game

if __name__ == "__main__":
    game = Game()
    command = -1
    while (command != 0):
        command = input('Enter a command: ')
        print('lol {}'.format(command))