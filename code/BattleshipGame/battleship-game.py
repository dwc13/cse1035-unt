from game_utils.game_logic import Battleship

def main() -> None:
    print(f'{"RUNNING GAME AS A PACKAGE":=^50}\n')
    game = Battleship()
    game.run()

if __name__ == "__main__":
    main()