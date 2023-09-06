import chess
import numpy as np
import tensorflow as tf

class ChessDQN:
    def __init__(self):
        self.model = self.create_model()
    
    def create_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.InputLayer(input_shape=(8, 8, 12)),
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(1)
        ])
        model.compile(optimizer='adam', loss='mean_squared_error')
        return model

    def board_to_input(self, board):
        piece_map = board.piece_map()
        input_matrix = np.zeros((8, 8, 12))

        for square, piece in piece_map.items():
            row = 7 - (square // 8)
            col = square % 8
            channel = self.piece_to_channel(piece)
            input_matrix[row, col, channel] = 1

        return np.expand_dims(input_matrix, axis=0)

    def piece_to_channel(self, piece):
        piece_order = 'pnbrqkPNBRQK'
        return piece_order.index(piece.symbol())

    def train(self, board, target):
        input_data = self.board_to_input(board)
        self.model.train_on_batch(input_data, np.array([target]))

if __name__ == "__main__":
    dqn = ChessDQN()
    board = chess.Board()
    dqn.train(board, 0.5)