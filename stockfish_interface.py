# Stockfish Engine Integration
from stockfish import Stockfish

stockfish = Stockfish(path="./stockfish.exe")  # Ensure stockfish.exe is placed in the same folder

def get_best_move(fen):
    stockfish.set_fen_position(fen)
    return stockfish.get_best_move()
