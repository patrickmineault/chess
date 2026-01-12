#!/usr/bin/env python3
"""
Chess scenario verifier - validates FEN positions and checkmate-in-one puzzles.
"""

import chess
import chess.svg
import cairosvg


def render_board(board: chess.Board, filename: str) -> None:
    """Render the board to a PNG file."""
    svg_string = chess.svg.board(board)
    cairosvg.svg2png(bytestring=svg_string.encode(), write_to=filename)


def validate_checkmate_in_one(board: chess.Board, move_san: str) -> tuple[bool, str]:
    """
    Validate that the given move results in checkmate.

    Returns (is_valid, error_message)
    """
    # Parse the move
    try:
        move = board.parse_san(move_san)
    except chess.InvalidMoveError:
        return False, f"Invalid move notation: {move_san}"
    except chess.IllegalMoveError:
        return False, f"Illegal move: {move_san}"
    except chess.AmbiguousMoveError:
        return False, f"Ambiguous move notation: {move_san}"

    # Check if move is legal
    if move not in board.legal_moves:
        return False, f"Move {move_san} is not legal in this position"

    # Make the move and check for checkmate
    board.push(move)

    if not board.is_checkmate():
        if board.is_check():
            return (
                False,
                f"Move {move_san} gives check but is not checkmate - black can escape",
            )
        else:
            return False, f"Move {move_san} does not give check"

    return True, ""


def main():
    print("Enter chess scenario (3 lines):")
    print("  Line 1: Name of the setup")
    print("  Line 2: FEN notation")
    print("  Line 3: Winning move for white (e.g., 1.Qb8#)")
    print()

    # Read input
    name = input("Name: ").strip()
    fen_input = input("FEN: ").strip()
    # Accept either raw FEN or "Fen: <fen>" (case-insensitive)
    if fen_input.lower().startswith("fen: "):
        fen = fen_input[5:].strip()
    else:
        fen = fen_input
    move_line = input("Move: ").strip()

    # Parse the move - remove move number prefix if present (e.g., "1.Qb8#" -> "Qb8#")
    move_san = move_line
    if "." in move_san:
        move_san = move_san.split(".")[-1].strip()

    print()
    print(f"Verifying: {name}")
    print(f"Position: {fen}")
    print(f"Move: {move_san}")
    print("-" * 40)

    # Parse FEN
    try:
        board = chess.Board(fen)
    except ValueError as e:
        print(f"FAILED: Invalid FEN notation - {e}")
        return 1

    # Validate position
    if not board.is_valid():
        print("FAILED: Invalid position")
        return 1

    print("✓ Position is valid")

    # Check it's white to move
    if board.turn != chess.WHITE:
        print("FAILED: It must be white's turn to move")
        return 1

    print("✓ White to move")

    # Render the starting position
    render_board(board, "board_before.png")
    print("Starting position rendered to board_before.png")

    # Validate checkmate in one
    is_valid, error = validate_checkmate_in_one(board, move_san)
    if not is_valid:
        print(f"FAILED: {error}")
        return 1

    print("✓ Move results in checkmate")
    print("-" * 40)
    print(f"SUCCESS: '{name}' is a valid mate-in-one puzzle!")

    # Render the final position (board was modified by validate_checkmate_in_one)
    render_board(board, "board_after.png")
    print("Final position rendered to board_after.png")

    return 0


if __name__ == "__main__":
    exit(main())
