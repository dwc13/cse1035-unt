from .utils import *
import random

class Battleship():
    def __init__(self, number_of_shots: int = 3, board_size: int = 5):
        self.reset = False 
        self.stop = False
        self.number_of_shots = number_of_shots
        self.board_size = board_size
        self.enemy_ship = 'Z999'
        #TODO # HOW WOULD YOU GET MULTIPLE ENEMY SHIPS ONTO THE BOARD
        # self.enemy_ships = []

    def start_game(self) -> int:
        if self.number_of_shots <= 0:
            return -1 # Current game session can't start

        # Initialize Board
        print_board(self.board_size, [], '+')
        self.set_enemy_ship()

        player_shots = []
        shots_left = self.number_of_shots
        while shots_left > 0:
            print_game_status(self.number_of_shots - shots_left + 1, self.number_of_shots, player_shots)

            # Player shot and is valid
            valid_shot = get_shot(self.board_size, player_shots)
            shots_left -= 1
            player_shots.append(valid_shot)
            print_board(self.board_size, player_shots, '+')

            # Check if hit
            if valid_shot == self.enemy_ship:
                print_info("Hit! You sunk an enemy ship!")
                break   #TODO Remove this break when multiple ships are implemented
            else:
                print_info("Missed! No ship at this position.")

            #TODO Update Enemy Ship list for multiple ships
            # Must break out of loop if all ships are sunk
        
        #TODO Update for multiple ships
        print_game_over(list(self.enemy_ship), player_shots)  #TODO REMOVE this when multiple ships are implemented
        # print_game_over(self.enemy_ships, player_shots)

        return 0 # Current game session is over
    
    def reset_game(self):
        self.number_of_shots = 3
        self.board_size = 5

    def run(self):
        status = 0
        while True:
            if status == -999:
                #TODO MAKE A BETTER EXIT MESSAGE
                print_info("Goodbye!")
                break

            print_game_title()
            status = self.show_menu()

            if status == 1:
                print_welcome()

                status = self.start_game()
                self.reset_game()

                print_info("Game finished, returning to menu...")

            #TODO ADD IN OPTIONS MENU
            #NOTE Options would set number of shots or board size
            #NOTE Board size would have to be limited based on number of shots to 26 for A-Z

    def show_menu(self) -> int:
        menu = {
            "1": ["Start Game", 1], # Start a game session
            #TODO ADD IN OPTIONS
            "2": ["Options", 2], # Change game session options
            "9": ["Quit", -999], # Exit Battleship game
        }
        status = 0

        # Stay in loop till correct operation is choosen
        while True: 
            print(f'{"MENU":^50}')
            print("="*50)
            for key, op in menu.items():
                item = f"{key:<3} {op[0]}"
                print(f'{" ":<18}{item: <25}')
            choice = input("Choose: ")
            if choice not in menu:
                print_warn("Invalid choice, try again.")
            else:
                status = menu[choice][1]
                break

        return status

    #TODO show_option function to print out choices and set number of shots or board size

    def set_enemy_ship(self):
        letter = random.choice([chr(65 + i) for i in range(self.board_size)])
        col = random.randint(0, self.board_size)
        self.enemy_ship = ''.join([letter, str(col)])
        #TODO # HOW WOULD YOU GET MULTIPLE ENEMY SHIPS ONTO THE BOARD

    #TODO set the number of shots

    #TODO set the board size