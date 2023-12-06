1
from logic import TicTacToe
import logging
import os

def initialize_logging():
    logging.basicConfig(filename='game_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_player_move(player, row, col):
    logging.info(f"Player {player} made a move to ({row}, {col})")

def get_game_mode():
    while True:
        try:
            mode = int(input("Choose game mode (1 for single-player, 2 for two-player): "))
            if mode in [1, 2]:
                return mode == 1
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    initialize_logging()
    is_single_player = get_game_mode()
    tic_tac_toe_game = TicTacToe(is_single_player)

    winner = None
    while winner is None:
        tic_tac_toe_game.print_board()
        try:
            row, col = tic_tac_toe_game.get_player_input()

            if tic_tac_toe_game.board[row][col] is not None:
                print("Spot taken, try again.")
                continue
            else:
                if tic_tac_toe_game.first_move:
                    tic_tac_toe_game.first_move_position = (int(row), int(col))
                    tic_tac_toe_game.first_move = False
                tic_tac_toe_game.add_move_number()
                log_player_move(tic_tac_toe_game.current_player, row, col)
        except (ValueError, IndexError):
            print("Invalid input, try again.")
            continue

        tic_tac_toe_game.board[row][col] = tic_tac_toe_game.current_player
        winner = tic_tac_toe_game.check_winner()
        tic_tac_toe_game.switch_player()

    tic_tac_toe_game.print_board()
    if winner == "draw":
        logging.info("Game ended in a draw.")
        print("It's a draw!")
    else:
        logging.info(f"Winner is Player {winner}")
        print(f"Player {winner} wins!")

    if not os.path.exists('database.csv'):
        with open('database.csv', 'w') as f:
            f.write('move_number,winner,single_player,first_move_loc\n')

    with open('database.csv', 'a') as f:
        f.write(f"{tic_tac_toe_game.move_number},{winner},{is_single_player},{tic_tac_toe_game.first_move_position[0]*3+tic_tac_toe_game.first_move_position[1]}\n")

if __name__ == "__main__":
    main()
