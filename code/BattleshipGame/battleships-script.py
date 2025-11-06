def print_welcome():
    """Print the welcome message and game instructions"""
    print("Welcome to Battleship!")
    print("Your mission: Sink all 3 ships!")
    print("Ships to find: Carrier, Submarine, Destroyer")
    print("Grid: Columns A-H, Rows 1-8")
    print("=" * 40)

def print_game_status(shot_number, shots_remaining, ships_sunk, previous_shots):
    """Print current game status before each shot"""
    print(f'\n--- Shot #{shot_number} ---')
    print(f'Shots remaining: {shots_remaining}')
    print(f'Ships sunk: {ships_sunk}/3')
    if previous_shots:
        print(f'Previous shots: {", ".join(previous_shots)}')
    else:
        print('Previous shots: None')

def print_shot_prompt(shot_number):
    """Print the input prompt for the shot"""
    print('Enter position to fire #{} torpedos \
       \n  (Col A-H)(Row 1-8) e.g., B4: '.format(shot_number), end='')

def print_hit_result(position, ship_name):
    """Print hit result message"""
    print(f'HIT! You sunk the {ship_name}!')

def print_miss_result(position):
    """Print miss result message"""
    print(f'MISS! No ship at {position}')

def print_game_over(ships_sunk, total_shots, board, shots_taken):
    """Print final game results"""
    print("\n" + "=" * 40)
    print("GAME OVER")
    if ships_sunk == 3:
        print(f"Congratulations! You sank all ships in {total_shots} tries!")
        print("VICTORY! You're a true naval commander!")
    else:
        print(f'Sorry, but you were not able to sink my ships! Tough break....')
        print(f'You sunk {ships_sunk} out of 3 ships in {total_shots} shots.')
        print('Ship locations were:')
        for position, ship in board.items():
            status = "SUNK" if position in [shot.upper() for shot in shots_taken] else "MISSED"
            print(f'   {position}: {ship} - {status}')


class Error(Exception):
	"""Base class for other exceptions"""
	pass

class PositionLengthError(Error):
	"""Raised when position length is not equal to 2"""
	pass

class PositionRowError(Error):
	"""Raised when position row type or value is invalid"""
	pass

class PositionColumnError(Error):
	"""Raised when position column type or value is invalid"""
	pass

class DuplicateShotError(Error):
	"""Raised when the same position is shot twice"""
	pass

def check_board():
	print_game_status(num_of_shots_taken + 1, num_of_shots, num_sunk, shots)
	print_shot_prompt(num_of_shots_taken + 1)
	valid_shot = False
	hit = False
	try:
		position = input()

		if len(position) != 2: 
			errmsg = 'Invalid position length: ' + str(len(position))
			raise PositionLengthError(errmsg)

		if not position[0].isalpha(): 
			errmsg = 'Invalid position column type: ' + position[0]
			raise PositionColumnError(errmsg)

		if ord(position[0].upper()) < 65 or ord(position[0].upper()) > 72: 
			errmsg = 'Invalid position column value: ' + position[0]
			raise PositionColumnError(errmsg)

		if not position[1].isdigit(): 
			errmsg = 'Invalid position row type: ' + position[1]
			raise PositionRowError(errmsg)

		if int(position[1]) < 1 or int(position[1]) > 8: 
			errmsg = 'Invalid position row value: ' + position[1]
			raise PositionRowError(errmsg)

		if position in shots:
			errmsg = 'Duplicate Shot Position: ' + position
			raise DuplicateShotError(errmsg)
		
		shots.append(position)

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
	else:
		valid_shot = True
		hit = True if position.upper() in board else False
		if hit:
			ship_name = board[position.upper()]
			print_hit_result(position, ship_name)
		else:
			print_miss_result(position.upper())

	return valid_shot, hit

num_of_shots = 5
num_of_shots_taken = 0
num_sunk = 0
shots = []
board = {'B4':'Carrier', 'H3':'Submarine', 'C3':'Destroyer'}

if __name__ == "__main__":
	print_welcome()

	while num_of_shots > 0:
		valid_shot, sunk = check_board()
		
		if valid_shot:
			if sunk:
				num_sunk += 1
			num_of_shots_taken += 1
			num_of_shots -= 1

	print_game_over(num_sunk, num_of_shots_taken, board, shots)