The user wants me to describe 3 mate-in-1 scenarios for white. Each scenario should be in its own code block with:
1. Name of the scenario
2. FEN notation for the setup
3. The winning move for white

Let me think of 3 distinct mate-in-1 puzzles.

**Scenario 1: Back Rank Mate**
A classic pattern where the rook or queen delivers checkmate on the back rank because the king is trapped by its own pawns.

Setup: Black king on g8, black pawns on f7, g7, h7. White rook on e1.
Let me set this up properly:
- Black king: g8
- Black pawns: f7, g7, h7
- White rook: e1
- White king: let's say g1

FEN: 6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1

White plays Re8# - the rook moves to e8, delivering checkmate because the king can't escape (blocked by its own pawns on f7, g7, h7, and the rook controls the entire 8th rank).

Let me verify:
- King on g8
- After Re8+, can the king move?
  - f7: blocked by pawn
  - g7: blocked by pawn
  - h7: blocked by pawn
  - h8: controlled by rook on e8
  - f8: controlled by rook on e8
- Can anything block or capture the rook? No other pieces.

Yes, this is checkmate.

**Scenario 2: Queen and King Mate (simple)**
Let me think of a scenario where the queen delivers mate with king support.

Setup: Black king on h8, White queen on g6, White king on g2.
FEN: 7k/8/6Q1/8/8/8/6K1/8 w - - 0 1


White plays Qg8# - the queen moves to g8, giving check. The king on h8 has no escape since h7 is controlled by the queen and the corner traps it completely.

**Scenario 3: Smothered Mate**
A knight delivers checkmate while the king is blocked in by its own pieces. Black king on h8, black pawns on f7, g7, h7, White knight on f6, White king on g2.

FEN: 7k/5ppp/5N2/8/8/8/6K1/8 w - - 0 1
White plays Ng8# - the knight moves to g8, giving check. The king cannot escape because all surrounding squares are either occupied by its own pawns or controlled by the knight. I'm verifying the FEN positions and moves for each scenario.

For the back rank mate, the rook on e1 moves to e8, giving check to the king on g8. The king cannot escape to f8 or h8 since the rook controls those squares, and its own pawns block f7, g7, and h7. No piece can capture the rook or block.

The queen mate works with the queen moving from b6 to a7. The king on a8 is in check from the adjacent queen, and both b8 and b7 fall under the queen's control, leaving no escape squares. The queen cannot be captured or blocked.

For the smothered mate, the knight jumps from e5 to f7, delivering check to the king on h8. The rook on g8 and pawns on g7 and h7 completely surround the king, preventing any escape. The knight cannot be taken or the check blocked.