The user wants me to describe 3 mate-in-1 scenarios for white. Each should be in code fences with:
1. Name of scenario
2. FEN notation
3. Winning move

Let me think of 3 classic mate-in-1 patterns:

**Scenario 1: Back Rank Mate**
A classic where the rook or queen delivers mate on the back rank because the king is trapped by its own pawns.

Setup: White has a rook, black king is on g8 with pawns on f7, g7, h7.
FEN: Let me construct this.
- Black king on g8
- Black pawns on f7, g7, h7
- White rook on e1 (or a1)
- White king somewhere safe, say g1

FEN: 6k1/5ppp/8/8/8/8/8/R5K1 w - - 0 1

White plays Ra8# (back rank mate)

Let me verify: 
- Black king on g8
- Pawns on f7, g7, h7 blocking escape
- White rook on a1 moves to a8, giving check
- King cannot escape to f8, g7, h8 because... wait, h8 would be available unless something blocks it.

Let me redo: 6k1/5ppp/8/8/8/8/8/R5K1 w - - 0 1
- 8th rank: nothing except... position 7 (g8) has black king
- 7th rank: f7, g7, h7 have pawns
- White rook on a1, white king on g1

Ra8+ - the rook goes to a8, giving check. King on g8 can go to:
- h7? No, pawn there
- g7? No, pawn there  
- f7? No, pawn there


- h8? Yes! h8 is free

This setup doesn't work since the king escapes to h8. I need to control that square as well. Let me place a white piece that covers h8—perhaps a queen on e5 would work, or I could position a rook on the h-file instead. A simpler approach: place white's rook on the h-file so Re8 delivers mate, with the king still boxed in by its pawns.

Actually, trying a different configuration with a rook on h6 to cover h8 and another rook on a1 for Ra8#. But checking the escape squares: the king on g8 can't go to h8 (covered by Rh6), h7, g7, or f7 (all blocked by pawns), but f8 remains uncontrolled. I need to reconsider the piece placement entirely.

Let me shift to using a rook on d1 that can deliver check from d8. With the king still on g8 and pawns on f7, g7, h7, Rd8+ gives check but h8 becomes an escape square. The back rank is too open without additional control.

A queen on b8 delivers mate more efficiently—Qb8# works because the queen controls the escape squares while the king is trapped by its own pawns. The queen on b8 delivers checkmate—it controls the entire 8th rank, so the king on g8 has no escape squares on f8 or h8, and the pawns on f7, g7, and h7 block retreat to the 7th rank.

For a smothered mate pattern, I need the king boxed in by its own pieces so a knight can deliver the final blow. Setting up: Black king trapped on h8 with a rook on g8 and pawns on g7 and h7, White knight positioned on f6. From there, the knight can jump to h7, giving checkmate since the king has no legal moves. Let me reconsider the setup. With the king on h8, rook on g8, and pawns on g7 and h7, I need the knight to deliver mate from a square where the king has no escape. A knight on f7 attacks h8 and d8, but that doesn't give check to a king on h8 since the rook blocks. Let me try positioning the knight on e7 instead—that would give check to the king on h8 while the surrounding pieces prevent any flight squares. The FEN breaks down correctly: rook on f8, king on h8, pawns on g7 and h7, with the white knight positioned on e5. When the knight moves to f7, it delivers checkmate—the black king is trapped on h8 with all escape squares (g8, g7, h7) controlled or blocked by its own pieces.

For the queen and king scenario, I'm setting up a position where the black king on e8 faces mate from a queen on e7 supported by the white king on e6. The queen controls all the king's flight squares (d8, d7, f8, f7), leaving no escape. The white king's placement reinforces the queen's dominance without creating any interference. Let me consider the Arabian Mate pattern with a rook and knight. The king sits on h8, with a rook delivering check along the h-file and a knight on f6 controlling the escape squares at g8 and h7.

Testing the position: after Rh8+, the king on h8 has g7 available as an escape, so this isn't quite mate yet. I need to add another piece to seal off that square.

If I place a black pawn on g7, then Rh8# becomes checkmate—the king is in check from the rook, g8 is controlled by the knight, and g7 is blocked by its own pawn. The Arabian Mate position checks out: king on h8, pawn on g7, knight on f6, with rook and king positioned on the first rank. Rh8# delivers checkmate since the king has no escape squares and the rook controls the back rank. So the knight on f6 controls h7 through its L-shaped movement pattern, which means the king has no escape squares—g8 is covered by the knight, g7 is blocked by its own pawn, and h7 is also controlled by the knight.

Now checking the FEN notation for accuracy: the back rank mate position has the queen on b2 with the king trapped on h8, and the smothered mate setup places a knight on e5 with the black king boxed in on h8 by its own pawns on g7 and h7.