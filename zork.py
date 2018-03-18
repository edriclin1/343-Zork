from game.game import Game

if __name__ == "__main__":
    game = Game()
    command = -1
    while (command != 0):
        print('--------------------------------------------------')
        print('| COMMANDS')
        print('|')
        print('| 1: Attack monsters')
        print('| 2: Move to different house')
        print('| 3: Show current location')
        print('| 4: List weapons')
        print('| 5: Restart game')
        print('| 0: Exit')
        print('--------------------------------------------------')

        try:
            command = input('Enter a command: ')
        except NameError:
            print('> Please enter a valid command (0-3).')
            continue

        # if command is 1, player and monsters fight
        if (command == 1):
            game.attack()

        # if command is 2, player moves to a different house
        elif (command == 2):

            row = 0
            col = 0

            # get user input for move location
            try:
                row = input('Enter a row (0-4): ')
                col = input('Enter a column (0-4): ')

                # throw error if out of bounds
                if (row < 0 or row > 4 or col < 0 or col > 4):
                    raise NameError
                    
            # print error message
            except NameError:
                print('> Invalid row or column (0-4).')
                continue

            game.move(row, col)

        # if command is 3, show curent location
        elif (command == 3):
            print('[Current Location]')
            row = game.get_current_row()
            col = game.get_current_col()
            print('({}, {})'.format(row, col))

        # if command is 4, list weapons
        elif (command == 4):
            print('[Weapons]')
            game.get_player().print_weapons()

        # if command is 5, restart game
        elif (command == 5):
            game = Game()
            print('> You have started a new game!')

        elif (command == 0):
            print('> Exiting game')

        # else invalid command
        else:
            print('> Please enter a valid command (0-3).')
