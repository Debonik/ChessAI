import chess
import chess.svg

def board_to_svg(board):
    return chess.svg.board(board=board)

def board_to_matrix(board):
    piece_map = board.piece_map()
    matrix = [['.' for _ in range(8)] for _ in range(8)]

    for square, piece in piece_map.items():
        row = 7 - (square // 8)
        col = square % 8
        matrix[row][col] = piece.symbol()

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(row))

if __name__ == "__main__":
    board = chess.Board()
    print("Board in SVG:")
    print(board_to_svg(board))

    print("Board as Matrix:")
    matrix = board_to_matrix(board)
    print_matrix(matrix)