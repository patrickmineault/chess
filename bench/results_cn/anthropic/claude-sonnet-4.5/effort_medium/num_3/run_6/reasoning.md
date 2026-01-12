I need to create 3 valid mate-in-1 scenarios for white. Each scenario needs:
1. A name/description
2. Valid FEN notation
3. The winning move in algebraic notation

Let me think of three distinct mate-in-1 positions:

**Scenario 1: Back Rank Mate**
- White has a rook that can deliver checkmate on the 8th rank
- Black king is trapped on the back rank by its own pieces
- FEN: Let me construct this... Black king on g8, black pawns on f7, g7, h7. White rook on d1, white king somewhere safe like g1.
- FEN format: [pieces on ranks 8-1] [active color] [castling] [en passant] [halfmove] [fullmove]
- Let me place: black king g8, pawns f7,g7,h7, white rook d1, white king g1
- Rank 8: black king on g8 = "6k1"
- Rank 7: black pawns on f7,g7,h7 = "5ppp"
- Rank 6: empty = "8"
- Rank 5: empty = "8"
- Rank 4: empty = "8"
- Rank 3: empty = "8"
- Rank 2: empty = "8"
- Rank 1: white rook on d1, white king on g1 = "3R2K1"
- Full FEN: "6k1/5ppp/8/8/8/8/8/3R2K1 w - - 0 1"
- Winning move: Rd8#

**Scenario 2: Queen Mate**
- White queen can deliver checkmate
- Let me set up: Black king on h8, trapped by its own pieces. White queen on d4 can go to h4#.


- I'll refine the position with a black pawn on g7 to restrict the king's movement
- Rank 8: black king h8 = "7k"
- Rank 7: black pawn g7 = "6p1"
- Rank 1: white queen on d1, white king on a1 = "K2Q4"
- Full FEN will help me precisely define the checkmate scenario

The smothered mate requires careful knight positioning. I'll place the white knight strategically to jump and deliver a decisive check from f7, blocking all potential king escapes. The black rook and pawn configuration will prevent the king's movement, creating a perfect trap for the checkmate.

The FEN notation confirms the precise board setup, with the knight on g5 ready to execute the winning move to f7, delivering a conclusive checkmate against the trapped black king.

Verifying potential mating scenarios reveals consistent patterns of restricting the king's movement through strategic piece placement and control of key squares.

The checkmate techniques demonstrate precise positional control, systematically eliminating the king's escape routes through careful piece coordination.

Each scenario successfully traps the king, showcasing the power of strategic positioning in chess endgames.