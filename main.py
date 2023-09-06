# Let's start by creating a skeleton code for main.py
# This code will initialize a chess board, print it, and allow a user and an AI to make moves in turns.

import chess
import chess.svg
from minimax import get_best_move
from evaluation import evaluate_board

def main():
    board = chess.Board()
    print("Initial board:")
    print(board)

    while not board.is_game_over():
        # User's turn
        print("Your turn:")
        user_move = input("Enter your move (e.g., e2e4): ")
        if chess.Move.from_uci(user_move) in board.legal_moves:
            board.push(chess.Move.from_uci(user_move))
        else:
            print("Illegal move. Try again.")
            continue

        print("Board after your move:")
        print(board)

        if board.is_game_over():
            break

        # AI's turn
        print("AI's turn:")
        ai_move = get_best_move(board)
        board.push(ai_move)
        print("Board after AI's move:")
        print(board)

if __name__ == "__main__":
    main()