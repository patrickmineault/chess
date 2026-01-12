The user wants me to describe 3 mate-in-1 scenarios for white. Each scenario needs:
1. A name
2. FEN notation for the setup
3. The winning move for white

Let me think of 3 distinct mate-in-1 puzzles.

**Scenario 1: Back Rank Mate**
A classic back rank mate where the king is trapped by its own pawns and a rook or queen delivers checkmate.

Setup: Black king on g8, black pawns on f7, g7, h7. White rook on e1.
FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1

Wait, let me make sure this is correct. The king is on g8, pawns on f7, g7, h7. White rook on e1, white king on h1.
The move Re8# would be checkmate.

FEN notation: 
- Rank 8: 6 empty squares, k, 1 empty = 6k1
- Rank 7: 5 empty, p, p, p = 5ppp
- Ranks 6-2: all empty = 8/8/8/8/8
- Rank 1: 4 empty, R, 2 empty, K = 4R2K

FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1

Move: Re8# or 1. Re8#

**Scenario 2: Queen and Bishop Mate (or simple queen mate)**
Let me think of another classic pattern.

How about a simple queen checkmate where the queen delivers mate supported by another piece?

Setup: Black king on h8, White queen on g6, White king on g1. The queen can go to g8 or h7 for mate.

Actually, let me try: Black king on h8, white queen on f6, white bishop on c3.


I need to find a position where the queen can deliver mate in one move. Let me try a simpler setup: Black king on h8, white queen on h6, white knight on f6. The queen could move to g7 for checkmate if it's protected. The knight on f6 doesn't defend g7 though. Let me reconsider the piece placement to ensure the mating move works cleanly. I need to set up a smothered mate position. The black king goes on h8 with a rook on g8, pawns on g7 and h7. I'll place a white knight on f6 that can deliver mate by moving to e8 or another square. Let me construct the FEN: the back rank has the rook and king (6rk), rank 7 has the pawns (6pp), rank 6 has the knight (5N2), and I'll put the white king safely on e1 (4K3). This gives me 6rk/6pp/5N2/8/8/8/8/4K3 w - - 0 1. Now the knight needs to find the mating move—it can go to e8 to deliver checkmate since the king has no escape squares. The knight move to f7 delivers checkmate. The king on h8 is in check and has no escape—g8 is blocked by the rook, while h7 and g7 are occupied by pawns. The knight itself can't be captured since none of Black's pieces control f7.

Now I should consider a different mating pattern. What about exploring Fool's Mate, which is the quickest possible checkmate in chess?

Actually, I need to think about Arabian Mate instead—where a rook and knight work together. Let me set this up: Black king trapped on h8, with a White rook on h1 and knight on f7. But moving the rook to h8 doesn't work since the king already occupies that square. I need to reconsider how this pattern actually functions, since the rook would need to deliver mate from a different square while the knight controls the escape routes. Let me work through this setup. I need the black king trapped on h8 with limited escape squares. If I place a knight on f7, it controls h8 and h6. Adding black pawns on g7 and h7 blocks those squares, so Rg8 becomes checkmate—the king has no legal moves.

The position would be: black king on h8 with pawns on g7 and h7; white rook on g1, white knight on f7, and white king on e1. With the pawn only on g7, the knight on f6 can cover h7. Moving the rook to g8 delivers mate since the king on h8 has no escape squares—g8 is occupied by the rook, g7 by the pawn, and h7 is controlled by the knight. 7. Rook on e1 goes to e8, attacking the king on g8. The escape squares f8 and h8 are both controlled by the rook, while f7, g7, and h7 are blocked by Black's own pawns. That's checkmate.

For the smothered mate, the knight moves from h6 to f7, giving check to the king on h8. The knight controls the escape square, and g8 has Black's rook while g7 and h7 are occupied by pawns, so the king has no legal moves.

The Arabian mate follows a similar pattern: the rook moves to g8 delivering check, the knight on f6 covers h7, and g7 is blocked by a pawn.

Now I should verify the FEN positions are accurate. The first position has the king on g8 with pawns on f7, g7, and h7, which matches the notation 6k1/5ppp/8/8/8/8/8/4R2K.

For the second position, the rook sits on g8 with the king on h8, the knight occupies h6, and pawns are on g7 and h7—this corresponds to 6rk/6pp/7N/8/8/8/8/4K3.

The third position has the king on h8, a pawn on g7, and the knight positioned on f6. The King and Rook are on e1 and h1 respectively, giving us 7k/6p1/5N2/8/8/8/8/4K1R1.