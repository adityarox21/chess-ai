# Main logic of ChessBuddy-AI
import stockfish_interface

if __name__ == '__main__':
    fen = input("Enter FEN or current position: ")
    best_move = stockfish_interface.get_best_move(fen)
    print(f"Best move: {best_move}")
