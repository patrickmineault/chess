I need to create 3 different mate-in-1 scenarios for white. Each should be:
1. A valid chess position
2. Where white can checkmate in one move
3. Distinct from each other (different types of checkmates)

Let me think of three different types of mate-in-1:

**Scenario 1: Back Rank Mate**
A classic back rank mate where white delivers checkmate with a rook or queen on the opponent's back rank.

For example:
- Black king on g8, pawns on f7, g7, h7 blocking escape
- White rook on d8 delivers mate by moving to e8 or staying on d8, or white queen somewhere that can deliver mate

Let me construct: Black King on g8, black pawns on f7, g7, h7. White Queen on d1 can deliver Qd8#.

FEN: Let me build this position:
- Rank 8: Black king on g8, so: 6 empty, king, 1 empty = "6k1"
- Rank 7: pawns on f7, g7, h7, so: 5 empty, 3 pawns = "5ppp"
- Rank 6: empty = "8"
- Rank 5: empty = "8"
- Rank 4: empty = "8"
- Rank 3: empty = "8"
- Rank 2: empty = "8"
- Rank 1: White queen on d1, white king somewhere safe like a1: "K2Q4"

Full FEN: "K2Q4/8/8/8/8/8/5ppp/6k1 w - - 0 1"

Wait, let me reconsider. The rank numbering should be from 8 to 1, and I need to make sure the position is legal.

Let me restart with proper FEN:


I'm working on constructing a precise back rank mate scenario, carefully building the FEN notation to ensure a valid chess position with a clear checkmate possibility.

The queen's strategic placement on d8 creates an inescapable trap for the black king. By controlling critical squares and blocking potential escape routes, the checkmate becomes inevitable. The knight and queen combination offers another elegant mating pattern, demonstrating the power of coordinated piece play.

I'll focus on developing a concise example that illustrates the core principles of back rank and knight-queen checkmate techniques. I verify the checkmate by checking king's escape routes. The knight controls g8, a pawn blocks g7, and the queen controls h7. No escape exists for the king.

The smothered mate involves a knight delivering checkmate while the king is trapped by its own pieces. I'll explore positioning the knight to jump into a decisive square, blocking all potential king movements.

The FEN notation confirms the strategic placement, with the knight positioned to deliver the final blow on f7, completely immobilizing the black king.

I verify the king's escape routes are blocked by the rook and pawn, creating a classic smothered mate scenario. The knight's unique movement prevents any defensive counterplay.

I'll carefully validate the board positions and potential checkmate configurations, ensuring legal and precise tactical execution.

The queen and knight strategically control critical squares, trapping the king with no possibility of movement or defense. Each scenario demonstrates a precise mating pattern where the king becomes completely immobilized.

The knight's unique movement creates a devastating checkmate by blocking escape routes and delivering a decisive check. Precise piece coordination eliminates all potential king retreats.

I'll verify the FEN notation matches the board state, confirming each component represents the correct chess position. The halfmove clock and move number align with standard notation requirements.

Queen moves decisively to d8, delivering checkmate by controlling critical squares and trapping the black king.

The knight and queen coordinate effectively in the second scenario, creating a strategic mating net that limits the black king's escape routes. I verify the checkmate by examining the queen's attack and the king's escape routes:
- Queen on h4 threatens the king on h8
- King cannot move to g8 due to knight's control
- King blocked by pawn on g7 and queen controls h7

No black pieces can capture or block the queen. This confirms checkmate. Knight delivers checkmate by moving to f7, completely immobilizing the black king. No defensive moves are possible - all escape squares are blocked, and no piece can capture the knight. The king is trapped, confirming a decisive checkmate.

The positioning creates a perfect smothered mate scenario, with the knight exploiting the king's restricted movement and lack of defensive options.