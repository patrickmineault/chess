The user wants me to describe 3 mate-in-1 scenarios for white. Each scenario needs:
1. A name
2. FEN notation for the setup
3. The winning move for white

Let me think of 3 distinct and valid mate-in-1 puzzles.

**Scenario 1: Back Rank Mate**
A classic back rank mate where the black king is trapped on the back rank by its own pawns, and a white rook or queen delivers checkmate.

Setup: Black king on g8, black pawns on f7, g7, h7. White rook on e1.
FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1

Wait, let me make sure this is correct. The king is on g8, pawns on f7, g7, h7. White rook on e1, white king somewhere safe like h1.

FEN breakdown:
- Rank 8: 6k1 (6 empty, king on g8, 1 empty)
- Rank 7: 5ppp (5 empty, pawns on f7, g7, h7)
- Rank 6: 8 (all empty)
- Rank 5: 8
- Rank 4: 8
- Rank 3: 8
- Rank 2: 8
- Rank 1: 4R2K (4 empty, Rook on e1, 2 empty, King on h1)

FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1

Move: Re8# (Rook to e8 checkmate)

Actually, let me double-check this. Rook on e1 moves to e8. Black king on g8 is attacked by the rook. Can the king escape?


- f8? Covered by Re8
- h8? Covered by Re8
- f7, g7, h7 are blocked by own pawns

Yes, this is checkmate. Re8# or 1. Re8#

In algebraic notation: Re8#

**Scenario 2: Queen and Bishop Mate**

I need a position where the queen delivers mate with bishop support. Let me set up the black king on e8 with the white queen positioned to give checkmate on f7, backed by a bishop on c4 that controls key escape squares.

Actually, I should try something more direct—perhaps a smothered mate or Arabian mate pattern instead. Let me work with a queen and knight combination: black king trapped on h8 with a rook on g8 and pawns on g7 and h7. If I place the white queen on a2, can it reach a mating square? The queen could potentially move to a8 or g8, but f8 is blocked by the rook and g8 is inaccessible. I need to reconsider the setup to find a forcing sequence that leads to mate.

Let me explore a queen sacrifice idea where the black king sits on h8 with a pawn on g7 and a rook on g8, while my queen approaches from d4. If the queen captures on g7, the king on h8 would be in check with no escape—g8 is controlled by the queen and h7 blocks retreat. But I need to verify the king can't simply capture the queen on g7 from h8.

I should reconsider the setup. With the king on h8 and a pawn blocking h7, if I place my queen on g1 and move to g8, that gives check. The queen on g8 would control h7 diagonally, trapping the king. However, I need to ensure nothing can interpose or capture the queen, so I'll need to add more black pieces to complete the mating net.

Let me shift toward established mating patterns instead. The Arabian mate uses a knight and rook working together—I can position the black king on h8, place a white knight on f7 to control escape squares, and use a rook to deliver the final blow. The rook on h8 gives check. The king can't escape to f7 since the knight occupies it, f8 is controlled by the rook along the 8th rank, g7 is blocked by Black's own pawn, and h7 is also controlled by the rook on the h-file. That's checkmate.

This is the Arabian Mate pattern. For the position to work as a mate-in-1, the knight needs to already be positioned to control escape squares without giving check itself, then the rook delivers the final blow.

If I place the knight on f6 with the king on h8, the rook can move from a1 to a8 for checkmate. The knight covers g8 and h7, while a pawn on g7 blocks that square. The king has no legal moves—g8 and h7 are controlled by the knight, and g7 is blocked by the pawn.

The position works: Black king on h8, pawn on g7, White knight on f6, rook on a1, and White king on b1. This gives the FEN: 7k/6p1/5N2/8/8/8/8/RK6 w - -

Ra8 is checkmate because the rook controls the entire eighth rank, and the king has no escape squares—g8 is covered by the knight, h7 is also controlled by the knight, and g7 is blocked by Black's own pawn.

For the smothered mate, I need a knight positioned to deliver mate when the king is trapped by its own pieces. With the king on h8, surrounded by a rook on g8 and pawns on g7 and h7, a knight on e5 can play Nf7#. The knight move is legal from e5, and all escape squares are either controlled by the knight or blocked by Black's own pieces.

The FEN for this position is 6rk/6pp/8/4N3/8/8/8/K7 w - - 0 1, and the move is Nf7#. and h7 pawns
- White knight e5, king a1
Move: Nf7#
- Knight delivers check from f7
- King trapped by its own pieces: rook on g8, pawns on g7 and h7
- Smothered mate ✓

These three positions each demonstrate a distinct mating pattern with the king constrained by its own pieces.