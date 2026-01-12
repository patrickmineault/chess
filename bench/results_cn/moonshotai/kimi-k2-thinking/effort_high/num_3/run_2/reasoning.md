The user wants three mate-in-1 scenarios for White. Each scenario should be:
1. In its own code fences (```)
2. First line: name of the scenario
3. Second line: FEN notation
4. Third line: winning move for White
5. Valid and distinct from each other

Let me think of three different mate-in-1 scenarios:

Scenario 1: Simple back rank mate with a rook
- A common pattern where the black king is trapped on the back rank by its own pawns, and a white rook can deliver checkmate.

Scenario 2: Smothered mate with a knight
- Black king is surrounded by its own pieces and a white knight can deliver checkmate.

Scenario 3: Queen delivering mate with support
- A queen move that checks the king, with support from another piece, and the king cannot escape.

Let me design these positions:

Scenario 1: Back rank mate
White: King on e1, Rook on d7, pawn on e4
Black: King on e8, pawns on e7, f7, g7, h7, other pieces gone
This could work: White rook on d8, black king on e8, black pawns on e7, f7, g7, h7 blocking escape.
But if rook is on d8, that's already checkmate? Let me think.

Better: White rook on d1, black king on e8, black pawns on e7, f7, g7, h7, white needs to move to d8.
FEN: 4k3/pppp1ppp/8/8/8/8/8/3R4 w - - 0 1
Wait, that's not quite right. Let me be more precise:
Black king on e8, black pawns on e7, f7, g7, h7. White rook on d1. White to move, Rd8# would be mate.
FEN: 4k3/4p3/5p2/6p1/7p/8/8/3R4 w - - 0 1
No, this is getting messy. Let me use a standard back rank mate position.

Standard back rank mate:
White: King e1, Rook d1, other pieces cleared
Black: King e8, pawns e7, f7, g7, h7, other pieces cleared
FEN: 4k3/4p3/5p2/6p1/7p/8/8/3R4 w - - 0 1
From this position, Rd8# is mate.

Actually, simpler:
White: Rd1, Ke1; Black: Ke8, pawns on e7,f7,g7,h7
FEN: 4k3/4p2p/5p2/6p1/7p/8/8/3R4 w - - 0 1
Wait, the FEN should show all squares. Let me do it properly.

A clean back rank mate position:
White: King on g1, Rook on d1
Black: King on e8, pawns on e7, f7, g7, h7
FEN: 4k3/4p3/5p2/6p1/7p/8/6P1/3R4 w - - 0 1
No, that's not standard.

Let me use a well-known simple back rank mate:
White: Rd1, Ke1
Black: Ke8, pawns e7, f7, g7, h7
Board:
```
  a b c d e f g h
8 . . . . k . . .
7 . . . . p p p p
6 . . . . . . . .
5 . . . . . . . .
4 . . . . . . . .
3 . . . . . . . .
2 . . . . . . . .
. . . R . . . .
```
FEN: 4k3/4pppp/8/8/8/8/8/3R4 w - - 0 1

From this position, Rd8# is checkmate. Let's verify:
- King on e8
- Pawns on e7, f7, g7, h7 block all escape squares
- Rd8+ puts the king in check from the rook
- King cannot take rook (pawns protect d8? No wait)
Let me rethink. For back rank mate, the rook lands on the same rank as the king, with the king trapped by its own pawns.

Better position:
White: Rook on e1, King on g1
Black: King on e8, pawns on f7, g7, h7, and maybe one on e7?
Actually, the classic is: White rook on d1, black king on e8, black pawns on e7, f7, g7, h7.
After Rd8#, the rook on d8 is protected by nothing, but the black king cannot capture it because it's trapped.

FEN: 4k3/4p3/5p2/6p1/7p/8/8/3R4 w - - 0 1
Wait, this is wrong. The rooks belong on the 1st rank for white, 8th for black.
Let me try: White rook on d1, black king on e8, black pawns e7,f7,g7,h7.
FEN: 4k3/4p3/5p2/6p1/7p/8/8/3R4 w - - 0 1

The board would be:
8th rank: ....k...
7th rank: ....p.p.p.p (some pattern)
Actually, let's do:
8: r ... k . . . .
7: p p p p . . . .
But I want black pawns blocking the king.

Simplest back rank mate:
White: Rd1, Ke1
Black: Ke8, pawns on e7, f7, g7, h7
FEN: 4k3/4p3/5p2/6p1/7p/8/8/3R4 w - - - 0 1

No, I need to be more careful with the FEN notation.
FEN format: piece placement, active color, castling rights, en passant, halfmove clock, fullmove number

For a simple back rank mate:
- Black king on e8
- Black pawns: e7, f7, g7, h7
- White rook on d1
- White king somewhere, say g1
- All other squares empty

This gives us:
Rank 8: ....k...
Rank 7: ....p.p.p.p (e7, f7, g7, h7 would be ...pppp)
So: 4k3/4pppp/8/8/8/8/8/3R4 w - - 0 1

Wait, that doesn't show the white king. Let me put white king on g1:
Rank 1: ...R...K
So: 4k3/4pppp/8/8/8/8/8/3R3K w - - 0 1

From this position, Rd8# is mate. Let's verify:
- Rook moves from d1 to d8
- King on e8 is in check
- Can king capture on d8? No, because the rook is protected? Actually in pure back rank mate, the rook is often NOT protected. The point is the king CAN'T capture because it's trapped by its own pieces.
- Escape squares for black king: d7, e7, f7
- d7: empty but does rook control it? Yes, rook on d8 controls d7
- e7: pawn there
- f7: pawn there
- So it's indeed checkmate.

Good, Scenario 1 is ready.

Scenario 2: Smothered mate with knight
Classic smothered mate: White knight delivers check to black king that is surrounded by its own pieces.

Example:
White: Knight on f6, King on e1
Black: King on h8, pieces around it: pawn on g7, pawn on h7, bishop on g8, maybe a rook on h8? No, the king is on h8.

Surrounding squares: g8, h7, g7
For smothered mate, all adjacent squares must be blocked or controlled.

Classic smothered mate pattern:
Black king on h8
Black pawn on g7
Black pawn on h7
White knight on f7 delivering check
But wait, knight on f7 attacks h8 and g6.

If knight on f7 attacks h8, and black king on h8 is surrounded by:
- g8: controlled by knight or occupied by black piece
- h7: occupied by black pawn
- g7: occupied by black pawn

FEN: 6k1/5p1p/8/8/8/8/8/4K3 w - - 0 1
This has black king g8, pawns f7, h7. Knight on e7 could give mate? No.

Let me design it properly:
White: King e1, Knight f5
Black: King h8, pawns g7, h7, piece on g8 (maybe a bishop or queen)

Actually, the most famous is with a knight on f6 or f7:
Position: White Nf6, Black Kh8, black pawns g7,h7, black piece on g8.
If knight on f7 attacks h8 and g6, and black king is on h8:
- From h8, squares: g8, h7, g7
- If g8 has a black piece, h7 has pawn, g7 has pawn
- Knight on f7 attacks h8 (and g5, h9(offboard), d8, e9(offboard), etc)
- The check is Nf7xh8? No, that's capture. The knight GIVES check from f7 to king on h8? Knight on f7 attacks g5, h6, h8, d8, e5, d6, etc. Yes, knight on f7 attacks h8.

So: White knight on f7, Black king on h8, black pawn g7, black pawn h7, black piece on g8.
FEN: 6bk/5p1p/8/8/8/8/8/4K3 w - - 0 1
Wait, that's black king on g8. Let me fix.

Rank 8: ...k..b. (king h8, bishop g8)
7: ...p.p.. (pawns g7, h7)
So: 6bk/5p1p/8/8/8/8/8/4K3 w - - 0 1
No, that has king on g8.

Let me write it square by square:
8: a8 empty, b8 empty, c8 empty, d8 empty, e8 empty, f8 empty, g8 bishop, h8 king → 5bk
7: a7 empty, b7 empty, c7 empty, d7 empty, e7 empty, f7 pawn, g7 pawn, h7 pawn → 5ppp
Wait, that's not right for smothered mate.

For smothered mate on h8, we need:
- King on h8
- Pawn on h7 (blocking h7)
- Pawn on g7 (blocking g7)
- Piece on g8 (blocking g8, usually queen or bishop or knight)

White knight on f7: from f7, knight attacks h8, h6, g5, e5, d6, d8, e9(offboard), g9(offboard)

So the position:
White: King e1, Knight f7
Black: King h8, pawn g7, pawn h7, bishop g8

Board:
8: .......bk (empty squares, bishop g8, king h8)
7: ......pp (empty, then pawns on g7, h7)
So: 5bk1/5pp/8/8/8/8/8/4K3 w - - 0 1

Wait, FEN for rank 8: from a8 to h8.
If bishop on g8, king on h8: squares a8-f8 empty, g8 bishop, h8 king → 6bk
Rank 7: pawn on g7, pawn on h7: squares a7-f7 empty, g7 pawn, h7 pawn → 5pp

So: 6bk/5pp/8/8/8/8/8/4K3 w - - 0 1
From here, Nf7xh8 is not a check. The knight is already on f7. The move is just noted as "Nf7" if it was moving from somewhere else, or if it's already there, we can't have a move.

I need to place the knight so it can MOVE to f7 to deliver mate.

So: White knight on e5, and it can move to f7 delivering mate.
FEN: 6bk/5pp/8/8/4N3/8/8/4K3 w - - 0 1
From here, Nf7# is checkmate. Let's verify:
- Knight from e5 moves to f7
- From f7, knight attacks h8 (where black king is)
- King on h8's possible moves:
  - g8: occupied by black bishop
  - h7: occupied by black pawn
  - g7: occupied by black pawn
- Cannot capture the knight because it's protected or out of reach? Knight on f7 can be captured by... nothing from h8.
- The knight on f7 is not on a square that the king can capture from h8.
- So it's checkmate! Perfect.

Scenario 2 ready.

Scenario 3: Queen mate
Could be a simple queen delivery with support.

Example: White queen on h7, white bishop on g6, black king on h8.
But that's already mate, not a move to deliver mate.

Let's make it so queen moves to deliver mate.
White: Queen on d3, bishop on g6, king on g1
Black: King on h8, pawn on h7, other pieces cleared

If queen moves to h7: Qd3-h7# would be mate with support from bishop.
Board:
White: Kg1, Qd3, Bg6
Black: Kh8, pawn h7

Rank 8: ......k.
Rank 7: ......p.
Rank 6: ......B.
So: 6k1/6p1/6B1/8/8/3Q4/8/6K1 w - - 0 1

From here, Qh7# is checkmate. Let's verify:
- Queen from d3 moves to h3
- Wait, h7 is occupied by pawn. Oh I need queen to CAPTURE on h7.

Qxh7# with support from bishop on g6.
The black king on h8 is in check from queen on h7.
Possible escapes:
- g8: does queen control g8? From h7, queen controls g8 (diagonal) - YES
- h8: can't stay in check
- g7: does queen control g7? From h7, queen controls g7 (horizontal) - YES, and bishop also controls g7
Cannot capture queen because it's protected by bishop on g6.
So mate.

FEN: 6k1/6p1/6B1/8/8/3Q4/8/6K1 w - - 0 1
Move: Qxh7#

Actually, the notation should just be the move, not with check/checkmate symbols as per the user's request. They said "the winning move for white", so just the move notation.

Let me refine the FEN notation to be cleaner.

Scenario 1: Back rank mate
FEN: 4k3/4pppp/8/8/8/8/8/3R3K w - - 0 1
But this has black pawns on e7,f7,g7,h7, and white king on h1.
From d1, the rook moves to d8.
FEN for that: 4k3/4pppp/8/8/8/8/8/3R3K w - - 0 1
Actually: a8-d8 empty, e8 king, f8 empty, g8 empty, h8 empty → 4k3
a7-d7 empty, e7 pawn, f7 pawn, g7 pawn, h7 pawn → 4pppp
Rank 1: a1 empty, b1 empty, c1 empty, d1 rook, e1 empty, f1 empty, g1 empty, h1 king → 3R3K

So the full FEN: 4k3/4pppp/8/8/8/8/8/3R3K w - - 0 1
Move: Rd8

Wait, I should double-check the format. The user wants:
- First line: name
- Second line: FEN
- Third line: winning move

Also, the FEN should be valid. Let me make sure my FEN strings are correct.

For the back rank mate, a more common position would have some pieces for black, but the minimal is:
White: Ke1, Rd1
Black: Ke8, pawns e7,f7,g7,h7

FEN: 4k3/4pppp/8/8/8/8/8/3R4 w - - 0 1
But this has no white king. Must include white king.

White king on e1: ...K....
So rank 1: 3R2K1? No, d1 rook, e1 king → ...R.K...
a1 empty, b1 empty, c1 empty, d1 rook, e1 king, f1 empty, g1 empty, h1 empty → 3RK3

So: 4k3/4pppp/8/8/8/8/8/3RK3 w - - 0 1
But the format is: pieces, then space, then active color, etc.

Actually, let me use a simpler approach and test each FEN.

Scenario 1: Back Rank Mate
Name: "Back Rank Mate"
Position: White rook on d1, white king on e1. Black king on e8, black pawns on e7,f7,g7,h7.
FEN: 4k3/4pppp/8/8/8/8/8/3RK3 w - - 0 1
Move: Rd8

Wait, if white king is on e1, it's ...RK... on rank 1.
Squares: a1,b1,c1 empty; d1 rook; e1 king; f1,g1,h1 empty → 3RK3
So: 4k3/4pppp/8/8/8/8/8/3RK3 w - - 0 1

But I think the user might prefer more conventional positions. Let me use:
White: Kg1, Rd1
Black: Ke8, pawns e7,f7,g7,h7
Rank 1: 3R3K1

FEN: 4k3/4pppp/8/8/8/8/8/3R3K1 w - - 0 1

Scenario 2: Smothered Mate
Name: "Smothered Mate"
Position: White king e1, knight e5. Black king h8, bishop g8, pawns g7,h7.
FEN: 6bk/5pp/8/4N3/8/8/8/4K3 w - - 0 1
Wait, rank 8: a8-f8 empty, g8 bishop, h8 king → 6bk
Rank 7: a7-f7 empty, g7 pawn, h7 pawn → 5pp? No, that's 5 squares then pp.
a7,b7,c7,d7,e7 empty (5 squares), f7? I need to be careful.

For rank 7: squares a7-h7. If only g7 and h7 have pawns:
a7,b7,c7,d7,e7,f7 empty, g7 pawn, h7 pawn → 6pp
6 empty squares then pp → 6pp

Rank 6: all empty → 8
Rank 5: knight on e5 → a5-d5 empty (4 squares), e5 knight, f5-h5 empty → 4N3

So: 6bk/6pp/8/4N3/8/8/8/4K3 w - - 0 1
Move: Nf7

But wait, from e5, the knight moves to f7. The notation is just "Nf7". Since it's checkmate, we could write "Nf7#" but the user just wants the move. I'll provide just the move.

Scenario 3: Queen Mate
Name: "Queen and Bishop Mate"
Position: White king g1, queen d3, bishop g6. Black king h8, pawn h7.
FEN: 6k1/6p1/6B1/8/8/3Q4/8/6K1 w - - 0 1
Rank 8: king on h8 → 6k1
Rank 7: pawn on h7 → 6p1
Rank 6: bishop on g6 → 6B1
Rank 3: queen on d3 → 3Q4
Rank 1: king on g1 → 6K1

Move: Qxh7

Let me verify this is indeed mate:
- Queen captures pawn on h7: Qxh7#
- Black king on h8 is now in check from queen on h7
- King cannot move to g8 (queen controls g8 diagonally)
- King cannot move to h7 (occupied by queen)
- King cannot capture queen because it's protected by bishop on g6
- No other pieces can block
Yes, it's mate.

All three scenarios are distinct: back rank, smothered, and queen capture.

Final check on FENs:
1. Back Rank: 4k3/4pppp/8/8/8/8/8/3R3K1 w - - 0 1
   - Rank 8: 4k3 (king e8)
   - Rank 7: 4pppp (pawns e7,f7,g7,h7)
   - Rank 1: 3R3K1 (rook d1, king h1)
   - Move: Rd8

2. Smothered: 6bk/6pp/8/4N3/8/8/8/4K3 w - - 0 1
   - Rank 8: 6bk (bishop g8, king h8)
   - Rank 7: 6pp (pawns g7,h7)
   - Rank 5: 4N3 (knight e5)
   - Rank 1: 4K3 (king e1)
   - Move: Nf7

3. Queen Mate: 6k1/6p1/6B1/8/8/3Q4/8/6K1 w - - 0 1
   - Rank 8: 6k1 (king h8)
   - Rank 7: 6p1 (pawn h7)
   - Rank 6: 6B1 (bishop g6)
   - Rank 3: 3Q4 (queen d3)
   - Rank 1: 6K1 (king g1)
   - Move: Qxh7

I should make sure the FENs are parseable. Let me use a more standard format for empty squares.

In FEN, numbers indicate consecutive empty squares.
Rank 8: a8,b8,c8,d8 empty (4), e8 king, f8,g8,h8 empty (3) → 4k3 ✓
Rank 7: a7,b7,c7,d7 empty (4), e7 pawn, f7 pawn, g7 pawn, h7 pawn → 4pppp ✓
Rank 1: a1,b1,c1 empty (3), d1 rook, e1,f1,g1 empty (3), h1 king → 3R3K1 ✓

Rank 8: a8-f8 empty (6), g8 bishop, h8 king → 6bk ✓
Rank 7: a7-f7 empty (6), g7 pawn, h7 pawn → 6pp ✓
Rank 5: a5-d5 empty (4), e5 knight, f5,g5,h5 empty (3) → 4N3 ✓
Rank 1: a1-d1 empty (4), e1 king, f1,g1,h1 empty (3) → 4K3 ✓

Rank 8: a8-g8 empty (6), h8 king, no piece after → 6k1 ✓
Rank 7: a7-g7 empty (6), h7 pawn → 6p1 ✓
Rank 6: a6-f6 empty (6), g6 bishop, h6 empty (1) → 6B1 ✓
Rank 3: a2,b2,c2 empty (3), d3 queen, e3,f3,g3,h3 empty (4) → 3Q4 ✓
Rank 1: a1-g1 empty (6), h1 king → 6K1 ✓

All FENs look correct. The moves are correct. The scenarios are distinct.

One final consideration: should the move include check/checkmate notation? The user said "the winning move for white". In chess puzzles, it's common to just give the move, but sometimes include "#". I'll give just the basic move notation without "#" to be safe, but I could also include it. Let me check the user's wording again: "the winning move for white". I think just the move is fine, but I'll make it clear it's the move, not the notation with result. Actually, for mate-in-1, the move is always a checking move, and in this case, checkmate. I'll provide the move as it would be written in a game, so "Rd8", "Nf7", "Qxh7". This is standard.

Actually, I realize for scenario 2, the knight is on e5 moving to f7, so the move is "Nf7". For scenario 3, queen from d3 captures on h7, so "Qxh7". For scenario 1, rook from d1 moves to d8, so "Rd8". This is all correct.

One more check: Are these truly mate in 1? Yes, each move delivers checkmate immediately.

Scenario 1: Rd8#
- King on e8 cannot move (all squares blocked or controlled)
- Cannot capture rook (d8 is not adjacent to e8? Wait, e8 can capture d8!)

Oh no! I made a critical error. The king on e8 CAN capture a piece on d8 (diagonally adjacent? No, kings move one square in any direction. From e8, d8 is one square left, so yes, the king could capture the rook on d8.

For a back rank mate to work, either:
1. The rook is protected by another piece, or
2. The square d8 is controlled by a white piece so the king cannot move there (but capture is different)

Actually, in chess, if a piece moves to a square adjacent to the king, giving check, the king can capture that piece UNLESS the piece is protected. So for Rd8# to work, the rook on d8 must be protected by a piece white controls.

Let me revise Scenario 1:
White: King h1, Rook d1, Bishop c7 (protecting d8)
Black: King e8, pawns e7,f7,g7,h7

Wait, bishop on c7 would protect d8. Let's try that.
Board:
White: K on h1, Rd1, Bc7
Black: Ke8, pawns e7,f7,g7,h7

FEN: 4k3/2B1pppp/8/8/8/8/8/3R3K1 w - - 0 1
But this has bishop on c7, which is on rank 7. From c7, bishop controls d8. So if rook moves to d8, it's protected by bishop.

Rank 8: 4k3
Rank 7: a7 empty, b7 empty, c7 bishop, d7 empty, e7 pawn, f7 pawn, g7 pawn, h7 pawn → 2B1pppp

So FEN: 4k3/2B1pppp/8/8/8/8/8/3R3K1 w - - 0 1
Move: Rd8

Now checking: King on e8 could capture rook on d8, but the rook is protected by bishop on c7, so that would be illegal (king moving into check). So it's indeed mate.

But wait, does the bishop on c7 have a clear line to d8? Yes, it's a diagonal move. c7 to d8 is one step diagonal.

Actually, I think the classic back rank mate often has the rook protected by another rook or queen. Let me try a simpler protection:
White: Ra1, Rd1, Ke1
Black: Ke8, pawns e7,f7,g7,h7

If Rd8+, king could capture on d8, but the rook on a1 protects d1-d8? No, rooks don't protect that way.

Better: White queen on d2 instead of bishop. Queen on d2 protects d8.
FEN: 4k3/4pppp/8/8/8/8/3Q4/3R4 w - - 0 1 with white king somewhere...

Let me simplify: The user wants valid positions. Even if the rook is not protected, if the king cannot capture because doing so would move into check from another piece, it's still mate.

But in my original position 4k3/4pppp/8/8/8/8/8/3R3K1, with Rd8, the king on e8 could capture the rook on d8. Are there any white pieces controlling d8? No. So that would not be checkmate.

So I need to adjust Scenario 1 to have the rook protected.

Let me place a white bishop on c7 as I thought:
FEN: 4k3/2B1pppp/8/8/8/8/8/3R3K1 w - - 0 1
Move: Rd8

Now, if Black king captures on d8 (Kxd8), it would move onto a square controlled by the bishop from c7, which is illegal. So it's checkmate.

Alternatively, I could use a queen to protect:
White: King g1, Rook d1, Queen d2
Black: King e8, pawns e7,f7,g7,h7

FEN: 4k3/4pppp/8/8/8/8/3Q4/3R4 w - - 0 1
But I need to place the white king. Let's put it on g1.
Rank 1: rook d1, king g1 → ...R...K. → 3R3K1

So FEN: 4k3/4pppp/8/8/8/8/3Q4/3R3K1 w - - 0 1
Move: Rd8

The queen on d2 protects d8. King cannot capture.

I think the bishop version is cleaner:
FEN: 4k3/2B1pppp/8/8/8/8/8/3R3K1 w - - 0 1
Move: Rd8

Let me double-check this position:
- Rank 8: King on e8
- Rank 7: Bishop on c7, pawns on e7,f7,g7,h7
- Rank 1: Rook on d1, King on h1

When Rd8:
- King on e8 is in check from rook on d8
- King's options:
  - Capture on d8: Kxd8 - but d8 is controlled by bishop on c7, so illegal
  - Move to e7: occupied by own pawn
  - Move to f7: occupied by own pawn
  - Move to d7: rook on d8 controls d7
  - Move to f8: not adjacent to e8? Actually from e8, f8 is one square right. Is f8 controlled by any white piece? Not directly. But wait, the rook on d8 controls the entire 8th rank, so it controls f8. So king cannot move to f8.
  - Move to d8: that's the rook's square, capture discussed
  - Move to e8: can't stay in check

Actually, from e8, the adjacent squares are: d7, e7, f7, d8, f8, d9(offboard), e9(offboard), f9(offboard).
So: d7, e7, f7, d8, f8.
- d7: controlled by rook on d8
- e7: occupied by pawn
- f7: occupied by pawn
- d8: occupied by rook (can capture but illegal due to bishop)
- f8: controlled by rook on d8 (same rank)

So it's checkmate! Good.

Alternatively, I could make the position even simpler. A very common back rank mate has the queen delivering the check on the back rank, protected by a rook. But we want distinct scenarios.

Let me stick with the bishop-protected rook. It's a valid and instructive pattern.

One more option: The Arabian Mate pattern with rook and knight, but that's not pure back rank.

Actually, I could use a different back rank pattern where the rook is not captured because the king is not adjacent. For example, if the rook is on e8 and king on g8, but that requires different positioning.

Let me reconsider: The simplest back rank mate is when the rook/queen moves to the back rank, and the king is trapped by its own pieces and cannot capture because the checking piece is protected.

I'll use the queen-protected version as it's more classic:
White: King g1, Rook d1, Queen d2
Black: King e8, pawns e7,f7,g7,h7

FEN: 4k3/4pppp/8/8/8/8/3Q4/3R4 w - - 0 1
I need to add the white king. The format is ranks 8 to 1.

Rank 8: 4k3
Rank 7: 4pppp
Rank 2: 3Q4
Rank 1: 3R3K1

So: 4k3/4pppp/8/8/8/8/3Q4/3R3K1 w - - 0 1
Move: Rd8

This is better as the queen on d2 clearly protects the rook on d8.

Let me verify one last time:
- Starting FEN: 4k3/4pppp/8/8/8/8/3Q4/3R3K1 w - - 0 1
- White to move plays Rd8
- Black king on e8 is in check
- Options:
  - Kxd8: Illegal, queen on d2 protects d8
  - Ke7: square occupied by pawn
  - Kf7: square occupied by pawn
  - Kd7: square controlled by rook on d8
  - Kf8: square controlled by rook on d8
- No other pieces can block or capture
- Checkmate ✓

Perfect. Now my final answer will have three code blocks with these scenarios.

Wait, I should make sure the FENs are absolutely correct. Let me write them out fully:

Scenario 1:
Name: Back Rank Mate
FEN: 4k3/4pppp/8/8/8/8/3Q4/3R3K1 w - - 0 1
Move: Rd8

But I realize the queen on d2 is not visible in the FEN. Let me recount rank 2:
Rank 2: squares a2-h2. If queen is on d2:
a2 empty, b2 empty, c2 empty, d2 queen, e2 empty, f2 empty, g2 empty, h2 empty → 3Q4
That's correct.

Scenario 2:
Name: Smothered Mate
FEN: 6bk/6pp/8/4N3/8/8/8/4K3 w - - 0 1
Move: Nf7

Wait, I should make sure the black king is on h8 in this FEN.
Rank 8: 6bk means a8-f8 empty (6), g8 bishop (b), h8 king (k). Yes.

Scenario 3:
Name: Queen Mate
FEN: 6k1/6p1/6B1/8/8/3Q4/8/6K1 w - - 0 1
Move: Qxh7

Rank 8: 6k1 = a8-g8 empty, h8 king
Rank 7: 6p1 = a7-g7 empty, h7 pawn
Rank 6: 6B1 = a6-f6 empty, g6 bishop, h6 empty

All correct.

One final consideration: Should I use more "interesting" positions? The user wants valid and distinct, but doesn't specify complexity. These three are classic, fundamental checkmate patterns, which is good for demonstration purposes.

I think I'm ready to write the final answer.