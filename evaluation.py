import chess

def evaluate_board(board):
    piece_values = {
        'P': 1, 'N': 3, 'B': 3,
        'R': 5, 'Q': 9, 'K': 100
    }
    evaluation = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            value = piece_values[piece.symbol().upper()]
            evaluation += value if piece.color == chess.WHITE else -value

    return evaluation

if __name__ == "__main__":
    board = chess.Board()
    print(evaluate_board(board))