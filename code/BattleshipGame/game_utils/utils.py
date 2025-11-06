from .errors import * 

def print_welcome():
    """Print the welcome message"""
    print("=" * 50)
    print(f'{"Welcome to Battleship!":^50}')
    print("=" * 50)
    print("\nThere is an enemy ship.\nFind and destroy it!\n")

def print_game_title():
    print("="*50)
    print(f'{"Battleship":^50}')
    print("="*50)

def print_game_status(shot_number, shots_remaining, previous_shots):
    """Print current game status before each shot"""
    print(f'\n--- Shot #{shot_number} ---')
    print(f'Shots remaining: {shots_remaining}')
    if previous_shots:
        print(f'Previous shots: {", ".join(previous_shots)}')
    else:
        print('Previous shots: None')

def print_game_over(enemy_ships: list, player_shots: int):
    """Print final game results"""
    print("\n" + "=" * 50)
    print(f'{"GAME OVER": ^50}')
    # Check if all enemy ships are sunk
    for position in enemy_ships:
        if position in player_shots:
            all_sunk = True
        else:
            all_sunk = False
            break

    if all_sunk:
        print(f"Congratulations! You sank all ships in {len(player_shots)} tries!")
        print("VICTORY! You're a true naval commander!")
    else:
        print('The enemy got away!')
        print('Enemy Ships locations were:')
        for idx, position in enumerate(enemy_ships):
            print(f'   {position}')

def print_board(board_size: int, marked_positions: list = [], mark_symbol: str = "X"):
    """
    Print the game board with column labels as letters and row labels as numbers.
    Mark positions in shot_positions with 'X'.

    Args:
        board_size (int): The size of the board (e.g., 5 for a 5x5 board).
        mark_positions (list): A list of a string representing marked positions (e.g., ['A0', 'C3'] is [(0, 0), (2, 3)]).
    """
    # Create empty board
    board = [["~"] * board_size for _ in range(board_size)]

    # Get shot positions and mark them on the board
    for mark in marked_positions:
        row = int(mark[1])
        col = ord(mark[0]) - 65  # Convert letter to index (A=0, B=1, ...)
        if 0 <= row < board_size and 0 <= col < board_size:
            board[row][col] = mark_symbol

    # Print column headers (letters)
    print("    " + " ".join(chr(65 + i) for i in range(board_size)))

    # Print rows with row labels (numbers)
    for i, row in enumerate(board):
        print(f"{i}  " + " ".join(row))

def print_info(msg):
    print(f"[INFO] {msg}")

def print_warn(msg):
    print(f"[WARN] {msg}")


def get_shot(board_size: int, player_shots: list) -> str:
    """
    Get and validate the player's shot input. Infinite loop until a valid shot is entered.

    Args:
        board_size (int): The size of the game board (e.g., 8 for an 8x8 board).
        player_shots (list): List of previously taken shot positions.

    Returns:
        str: A valid shot position (e.g., 'B4').
    """
    while True:
        try:
            current_shot = input("Enter in a valid shot position > ")

            if len(current_shot) != 2: 
                errmsg = 'Invalid shot position length: ' + str(len(current_shot))
                raise PositionLengthError(errmsg)

            if not current_shot[0].isalpha(): 
                errmsg = 'Invalid position column type: ' + current_shot[0]
                raise PositionColumnError(errmsg)

            if ord(current_shot[0].upper()) - 65 >= board_size:
                errmsg = 'Invalid position column value type for board: ' + current_shot[0]
                raise PositionColumnError(errmsg)

            if not current_shot[1].isdigit(): 
                errmsg = 'Invalid position row type: ' + current_shot[1]
                raise PositionRowError(errmsg)

            if int(current_shot[1]) < 0 or int(current_shot[1]) >= board_size: 
                errmsg = 'Invalid position row value: ' + current_shot[1]
                raise PositionRowError(errmsg)

            if current_shot in player_shots:
                errmsg = 'Duplicate Shot Position: ' + current_shot
                raise DuplicateShotError(errmsg)

            return current_shot

        except PositionLengthError as err:
            print('PositionLengthError:',err)
            print('Please try again with a valid position.\n')
        except PositionRowError as err:
            print('PositionRowError:',err)
            print('Please try again with a valid position.\n')
        except PositionColumnError as err:
            print('PositionColumnError:',err)
            print('Please try again with a valid position.\n')
        except DuplicateShotError as err:
            print('DuplicateShotError:',err)
            print('Please try again with a different position.\n')