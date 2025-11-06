from .game_logic import Battleship

"""
Customer Complaint FIX ERRORS:
1. Issue: Not able to change board size and number of shots before starting game.
2. Issue: When entering a shot it is counting as valid shot but it not marked on the board.
    - Steps to reproduce:
        - Start game with default settings.
        - Enter a shot b3 (which is valid).
        - Observe that the shot is accepted but not marked on the board.
3. Issue: Shot count is not updating correctly after each shot.
"""

if __name__ == "__main__":
    print(f'{"RUNNING UNDER PACKAGE":=^50}\n')
    game = Battleship()
    game.run()

