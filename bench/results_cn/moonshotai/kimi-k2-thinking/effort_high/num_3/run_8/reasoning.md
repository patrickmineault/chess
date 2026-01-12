We need to provide three mate-in-1 scenarios for white. Each scenario should be in its own code block (three backticks). The first line is the name of the scenario, the second line is the FEN notation for the setup, and the third line is the winning move for white.

The scenarios should be valid and distinct from each other.

Let me think of three simple and distinct mate-in-1 scenarios:

1. **Classic Back Rank Mate**: This is a common pattern where the black king is trapped on the back rank by its own pieces, and white delivers check with a rook or queen.
2. **Smothered Mate**: A knight delivering mate to a king that is completely surrounded by its own pieces and unable to move.
3. **Queen Delivery Mate**: A simple scenario where the queen directly gives checkmate, perhaps with support.

Let me design these scenarios:

**Scenario 1: Back Rank Mate**
- White: King on g1, Rook on d8
- Black: King on g8, pawns on f7, g7, h7 (blocking escape squares), other pieces don't interfere
- FEN: Let's say it's white to move. So the FEN should end with "w". 
- Setup: 8/3R4/5p1p/5K1k/8/8/8/8 w - - 0 1
Wait, that doesn't look right. Let me reconsider.

A proper back rank mate:
- Black king on g8
- Pawns on f7, g7, h7
- White rook on d8 delivering check
- White king somewhere safe

FEN: 3R4/5p1p/8/8/8/8/7P/6K1 w - - 0 1
Wait, that doesn't have the black king.

Let me be more systematic:
Rank 8: ..k.....
Rank 7: ..ppp...
Wait, let's build it properly.

For a back rank mate:
- Black King on g8
- Black pawns on f7, g7, h7
- White Rook on d8 delivering the check
- White King somewhere safe, say on g1

So the board from rank 8 to rank 1:
Rank 8: . . . R . . k .
Rank 7: . . . . . p p p
Rank 6: . . . . . . . .
Rank 5: . . . . . . . .
Rank 4: . . . . . . . .
Rank 3: . . . . . . . .
Rank 2: . . . . . . . .
Rank 1: . . . . . . K .

FEN: 3R3k/5ppp/8/8/8/8/8/6K1 w - - 0 1

Wait, the black king should be on g8, not h8. Let me fix that.
Rank 8: . . . R . . k .
That's "3R2k1" in FEN notation? Let's count: squares a8,b8,c8,d8,e8,f8,g8,h8
3 empty, R, 2 empty, k, 1 empty -> 3R2k1

Rank 7: . . . . . p p p
That's "5ppp"

So FEN: 3R2k1/5ppp/8/8/8/8/8/6K1 w - - 0 1

Winning move: Rg8#

**Scenario 2: Smothered Mate**
- Black king on h8
- Surrounding pieces: knight on g8, pawn on h7, maybe a bishop on g7
- White knight delivers mate from f7

Setup:
- Black king on h8
- Black knight on g8 (blocking)
- Black pawn on h7 (blocking)
- White knight on f7 delivering check
- White king somewhere safe

Rank 8: . . . . . . n k
Rank 7: . . . . . . N p
Rank 6: . . . . . . . .
Rank 5: . . . . . . . .
Rank 4: . . . . . . . .
Rank 3: . . . . . . . .
Rank 2: . . . . . . . .
Rank 1: . . . . . . K .

FEN: 6nk/6Np/8/8/8/8/8/6K1 w - - 0 1

Wait, that doesn't look right. Let me recount rank 8: a8,b8,c8,d8,e8,f8,g8,h8
6 empty, n, k -> 6nk

Rank 7: a7,b7,c7,d7,e7,f7,g7,h7
6 empty, N, p -> 6Np

But smothered mate usually requires the king to be completely surrounded. Let me add more pieces:
- Black king on h8
- Black pawn on g7
- Black pawn on h7
- Black knight on g8
- White knight on f7

Rank 8: . . . . . n k .
That's "5nk1"

Rank 7: . . . . . N p p
That's "5Npp"

FEN: 5nk1/5Npp/8/8/8/8/8/6K1 w - - 0 1

Wait, the king on h8, knight on g8, pawns on g7 and h7. Knight from f7 attacks g5, h6, h8, g9(offboard), f9(offboard), e9(offboard), e5, d6. Actually from f7, the knight attacks h8, h6, g5, e5, d6, d8. So yes, it attacks h8. Let me verify:

From f7:
- +2,+1: h8 (check!)
- +2,-1: h6
- +1,+2: g9 (offboard)
- +1,-2: g5
- -1,+2: e9 (offboard)
- -1,-2: e5
- -2,+1: d8
- -2,-1: d6

So Nf7+ attacks Kh8. The squares around Kh8:
- g8 is occupied by black knight
- g7 is occupied by black pawn
- h7 is occupied by black pawn

The king cannot capture the knight (it's protected? Actually it doesn't need to be protected for smothered mate).
The king cannot move anywhere. So yes, Nf7 is checkmate.

But let me double-check the FEN. The pieces are:
- Black: king on h8, knight on g8, pawns on g7, h7
- White: knight on f7, king on g1

Rank 8: a8 empty, b8 empty, c8 empty, d8 empty, e8 empty, f8 empty, g8 knight, h8 king
= 5nk1 (5 empty, n, k, 1 empty)

Rank 7: a7 empty, b7 empty, c7 empty, d7 empty, e7 empty, f7 knight, g7 pawn, h7 pawn
= 5Npp

Rank 6: all empty = 8
Rank 5: all empty = 8
Rank 4: all empty = 8
Rank 3: all empty = 8
Rank 2: all empty = 8
Rank 1: a1 empty, b1 empty, c1 empty, d1 empty, e1 empty, f1 empty, g1 king, h1 empty
= 6K1

So FEN: 5nk1/5Npp/8/8/8/8/8/6K1 w - - 0 1

Move: Nf7# (or is it Nxg7#? No, the white knight is already on f7 delivering mate). Actually in the FEN, the knight is on f7, so the move would be something else? Wait, no. The FEN represents the current position. So if the knight is already on f7, then it's already delivering checkmate, which is not what we want.

I need the knight to move TO the delivering square. So let's place the white knight on d6 or e5 or somewhere that can move to f7.

Let me redesign:
- White knight on d6 moves to f7#
- Black king on h8
- Black pieces on g8, g7, h7 blocking

Position:
Rank 8: . . . . . . n k = 5nk1
Rank 7: . . . . . . p p = 5pp
Rank 6: . . N . . . . . = 2N5
Rank 5: . . . . . . . . = 8
Rank 4: . . . . . . . . = 8
Rank 3: . . . . . . . . = 8
Rank 2: . . . . . . . . = 8
Rank 1: . . . . . . K . = 6K1

Wait, rank 6: a6 empty, b6 empty, c6 knight, d6 empty... that's "2N5" (2 empty, N, 5 empty)

FEN: 5nk1/5pp/2N5/8/8/8/8/6K1 w - - 0 1

Move: Nf7#

Let me verify: Knight from c6 goes to: a7, a5, b8, b4, d8, d4, e7, e5. None of those are f7. Oops.

Let me place the knight on e5:
From e5 to f7 is +1,+2, yes that works.

Rank 6: . . . . N . . . = 4N3

FEN: 5nk1/5pp/4N3/8/8/8/8/6K1 w - - 0 1

Wait, rank 6 is "4N3" (4 empty, N, 3 empty)

But I said rank 6, let me rebuild:
Rank 8: 5nk1
Rank 7: 5pp
Rank 6: . . . . N . . . = 4N3
Rank 5: 8
Rank 4: 8
Rank 3: 8
Rank 2: 8
Rank 1: 6K1

FEN: 5nk1/5pp/4N3/8/8/8/8/6K1 w - - 0 1

From e5, the knight can go to f7. Let me verify squares around Kh8:
- g8: occupied by black knight
- g7: occupied by black pawn
- h7: occupied by black pawn
- Cannot capture the checking knight

Yes, this works. The move is Nf7#.

**Scenario 3: Simple Queen Mate**
This could be a scenario where the queen directly checks the king with no escape.

Option A: Queen on h7 delivering mate to king on h8
- Black king on h8
- Black pawn on g7 (blocking g7)
- White queen on h7 delivering check
- But the queen would be adjacent to the king, and the king could capture if not protected.

Let me add protection:
- White queen on h7
- White bishop on g6 protecting h7
- Black king on h8
- Black pawn on g7 (blocking)
- Black pawn on h7? No, queen is there.

Setup:
Rank 8: . . . . . . . k = 7k
Rank 7: . . . . . . q . = 6q
Rank 6: . . . . . . B . = 6B
Rank 5: . . . . . . . . = 8
Rank 4: . . . . . . . . = 8
Rank 3: . . . . . . . . = 8
Rank 2: . . . . . . . . = 8
Rank 1: . . . . . . K . = 6K1

FEN: 7k/6q/6B/8/8/8/8/6K1 w - - 0 1

But wait, if it's white to move and the queen is already on h7, then it's already delivering checkmate. That's not right.

The queen needs to MOVE to deliver mate.

Let me redesign:
- White queen on d3
- White bishop on g6
- Black king on h8
- Black pawn on g7
- Black pawn on h7

The move would be Qh3# or Qh7#? Let's think.

If queen moves to h7:
- From d3 to h7 is diagonal up-right
- On h7, queen attacks h8 (vertical)
- Squares around Kh8: g8 empty? Let me fill it.

Better setup:
- Black king on h8
- Black pawn on g7 (blocks g7)
- Black pawn on h7 (blocks h7, but queen will capture or go there)
- White queen on d3
- White bishop on g6 (protects h7)

If queen goes to h7:
- g7 is blocked by pawn
- g8 is escape square - need to block it

Let me try a different pattern. Queen on g6 delivering mate to king on h8:
- From g6, queen attacks h7 and h8 and g8
- If we have: black king on h8, black pawn on h7, black pawn on g7
- Queen on g6 would be delivering check to h7? No, that's not right.

I think I should go for a simpler pattern. Let's do a "queen sacrifice" or direct delivery:

**Scenario 3: Corridor Mate**
- Black king on h8
- Black rook on g8 (blocking)
- White queen on h2 delivering Qh7#

Setup:
Rank 8: . . . . . . r k = 5rk
Rank 7: . . . . . . . . = 8
Rank 6: . . . . . . . . = 8
Rank 5: . . . . . . . . = 8
Rank 4: . . . . . . . . = 8
Rank 3: . . . . . . . . = 8
Rank 2: . . . . . . q . = 6q
Rank 1: . . . . . . K . = 6K1

FEN: 5rk/8/8/8/8/8/6q/6K1 w - - 0 1

Move: Qh7#

Let me verify:
- Queen from h2 to h7
- From h7, queen attacks h8 vertically
- King on h8 cannot move to g7 (empty, but is it attacked?), g8 (occupied by rook), or stay on h8
- Actually, can the king capture the queen on h7? No, because h7 is adjacent and the queen is protected? Let me add protection.

Let me add a white piece protecting h7:
- White bishop on g6 protecting h7

Rank 8: 5rk
Rank 7: 8
Rank 6: . . . . . . B . = 6B
Rank 5: 8
Rank 4: 8
Rank 3: 8
Rank 2: 6q
Rank 1: 6K1

FEN: 5rk/8/6B1/8/8/8/6q/6K1 w - - 0 1

Move: Qh7#

But wait, if the queen is on h2, going to h7, and the bishop is on g6, yes, h7 is protected.

Actually, let me simplify even more. A classic queen deliver:

**Scenario 3: Queen on 7th rank**
- Black king on g8
- White queen on g7 delivering Qxg7#

Setup:
Rank 8: . . . . . . k . = 6k
Rank 7: . . . . . . q . = 6q
Rank 6: . . . . . . . . = 8
Rank 5: . . . . . . . . = 8
Rank 4: . . . . . . . . = 8
Rank 3: . . . . . . . . = 8
Rank 2: . . . . . . . . = 8
Rank 1: . . . . . . K . = 6K1

FEN: 6k/6q/8/8/8/8/8/6K1 w - - 0 1

Move: Qxg7#

But this is already checkmate in the position, not a move delivering it.

I need the queen to MOVE to a square that gives mate.

Let me try one more time:

**Scenario 3: Arabian Mate style but with queen**
Actually, let me do a simple one:
- White queen on e6
- White rook on g8 (or a piece controlling g8)
- Black king on h8
- Black pawn on h7

The move Qxh7# would work if g8 is controlled.

Rank 8: . . . . . . . k = 7k
Rank 7: . . . . . . . p = 7p
Rank 6: . . . . . Q . . = 5Q2
Rank 5: . . . . . . . . = 8
Rank 4: . . . . . . . . = 8
Rank 3: . . . . . . . . = 8
Rank 2: . . . . . . . . = 8
Rank 1: . . . . . . K . = 6K1

FEN: 7k/7p/5Q2/8/8/8/8/6K1 w - - 0 1

But from e6, queen to h7 is not a straight line. e6 to h7 is diagonal? e-f-g-h (4 files), 6-7 (1 rank) = not a clear diagonal.

Let me do queen on f6 to h6:
- Queen on f6 to h6#
- King on g8, pawn on g7, king surrounded

Rank 8: . . . . . . k . = 6k
Rank 7: . . . . . p p . = 5pp
Rank 6: . . . . . Q . . = 5Q2
Rank 5: . . . . . . . . = 8
Rank 4: . . . . . . . . = 8
Rank 3: . . . . . . . . = 8
Rank 2: . . . . . . . . = 8
Rank 1: . . . . . . K . = 6K1

FEN: 6k/5pp/5Q2/8/8/8/8/6K1 w - - 0 1

Move: Qh6#

Let me verify:
- Queen on f6 to h6 (horizontal)
- From h6, queen attacks h8 (vertical)
- From h6, queen attacks g8 (diagonal)
- King on g8: 
  - Cannot move to g7 (occupied by pawn)
  - Cannot move to h8 (attacked by queen)
  - Cannot move to f7 (attacked by queen? From h6 to f7 is diagonal? h-g-f (2 left), 6-7 (1 up) - yes, that's a diagonal attack)
  - Cannot move to f8 (attacked by queen horizontally)
  - Cannot capture queen (too far)

Actually, from h6, queen attacks:
- Vertical: h1-h8
- Horizontal: a6 through h6
- Diagonal: a1-h8 and a8-h1 directions

So from h6, queen attacks g8 (diagonal) and h8 (vertical). The king on g8 is in check from the queen on h6.

Escape squares for king on g8:
- f8: attacked by queen (horizontal from h6)
- g7: occupied by pawn
- h8: attacked by queen (vertical)
- h7: attacked by queen (vertical)
- f7: attacked by queen (diagonal)

Wait, is f7 attacked? From h6 to f7 is left 2, up 1, which is NOT a queen line. Let me think again.

Coordinates:
- h6: file h, rank 6
- f7: file f, rank 7
Difference: 2 files left, 1 rank up = diagonal? No, queen moves in straight lines. For a diagonal, file difference = rank difference. Here 2 ≠ 1, so not a diagonal.

Let me recalculate:
From h6, queen attacks:
- Rank 6: all squares a6-h6
- File h: all squares h1-h8
- Diagonal h6-a8: squares g7, f8
- Diagonal h6-b1: squares g5, f4, e3, d2, c1

So from h6, queen attacks g7 and f8 (diagonal h6-a8 style).

So if king is on g8:
- g7 is attacked by queen (yes! from h6 to g7 is diagonal)
- f8 is attacked by queen (yes! from h6 to f8 is diagonal)
- h8 is attacked by queen (vertical)
- The king cannot move to g7 (attacked)
- The king cannot move to f8 (attacked)
- The king cannot move to h8 (attacked)
- The king cannot stay on g8 (in check)
- The king cannot capture the queen (distance > 1)

What about f7 and h7?
- f7 is NOT attacked by queen on h6 (not same rank, file, or diagonal)
- h7 IS attacked by queen on h6 (same file)

So the setup should be:
- King on g8
- Pawn on g7 (blocks g7 but it's attacked anyway)
- We need to block/control f7 and h7

Let me redesign scenario 3 completely:

**Scenario 3: King and Queen Mate**
White king and queen vs black king trapped at the edge.

- White king on g6 (controlling f7, g7, h7)
- White queen on e5 delivering Qe8# or similar

Let's try:
- Black king on h8
- White king on g6
- White queen on h5 delivering Qh7#

Rank 8: . . . . . . . k = 7k
Rank 7: . . . . . . . . = 8
Rank 6: . . . . . . K . = 6K
Rank 5: . . . . . . q . = 6q
Rank 4: . . . . . . . . = 8
Rank 3: . . . . . . . . = 8
Rank 2: . . . . . . . . = 8
Rank 1: . . . . . . . . = 8

FEN: 7k/8/6K/6q/8/8/8/8 w - - 0 1

Move: Qh7#

From h5 to h7 is vertical 2 squares. With white king on g6 controlling f7, g7, h7:
- King on g6 controls squares: f7, g7, h7, f5, g5, h5, f6, h6

So after Qh7+:
- King on h8 is in check from queen on h7 (vertical)
- King cannot capture queen on h7 because it's protected by king on g6
- King cannot move to g8 (empty, but is it controlled?) From g6, the king doesn't control g8 (2 squares away)
- King cannot move to h7 (occupied by queen)
- King cannot move to g7 (controlled by white king)

Let me add a white rook or something controlling g8.

Actually, this is getting too complex. Let me simplify:

**Scenario 3: Clear Queen Delivery**
- White queen on h5
- Black king on h8
- White bishop on c3 controlling g7

The move Qh7# works if:
- King on h8 cannot capture queen (protected)
- King cannot move to g8 (controlled)
- King cannot move to g7 (controlled)

Setup:
- White queen on e5
- White bishop on g5
- Black king on h8
- Black pawn on g7 (blocks but also is a target)

Rank 8: . . . . . . . k = 7k
Rank 7: . . . . . . p . = 6p
Rank 6: . . . . . . . . = 8
Rank 5: . . . . . Q B . = 4QB2? Let me count: a5,b5,c5,d5,e5=queen,f5 empty,g5=bishop,h5 empty = 4Q1B1
Rank 4: . . . . . . . . = 8
Rank 3: . . . . . . . . = 8
Rank 2: . . . . . . . . = 8
Rank 1: . . . . . . K . = 6K1

FEN: 7k/6p/8/4Q1B1/8/8/8/6K1 w - - 0 1

Move: Qg7#

From e5 to g7 is diagonal. Pawn on g7 is captured by queen. Bishop on g5 protects g7.

After Qxg7#:
- King on h8 is in check from queen on g7 (adjacent)
- King cannot capture queen (protected by bishop)
- King cannot move to g8 (is it controlled?) 
- King cannot move to h7 (does queen attack h7? Yes, from g7 queen attacks h8, h7, h6..., also g8, f8, e8...)

From g7, queen attacks:
- h8 (diagonal) - check
- h7 (horizontal) - controlled
- g8 (vertical) - controlled
- f8 (diagonal) - controlled
- f7 (horizontal) - controlled
- etc.

So the king on h8:
- In check from queen on g7
- Cannot capture queen (protected by bishop on g5)
- Cannot move to h7 (attacked by queen)
- Cannot move to g8 (attacked by queen)
- Therefore: checkmate.

This works! But the notation would be Qxg7#.

Actually, let me make it even simpler - a classic pattern:

**Scenario 3: Queen and King vs Trapped King**
- White queen on g5
- White king on g6
- Black king on h8

Rank 8: . . . . . . . k = 7k
Rank 7: . . . . . . . . = 8
Rank 6: . . . . . . K . = 6K
Rank 5: . . . . . . q . = 6q
Rank 4: . . . . . . . . = 8
Rank 3: . . . . . . . . = 8
Rank 2: . . . . . . . . = 8
Rank 1: . . . . . . . . = 8

FEN: 7k/8/6K/6q/8/8/8/8 w - - 0 1

Move: Qh5#

From q5 to h5 is horizontal. With king on g6:
- Queen on h5 attacks h8 (vertical)
- King on g6 controls g7, h7, f7, f6, h6, f5, g5, h5

After Qh5+:
- King on h8 is in check
- King cannot capture queen (adjacent but protected by white king on g6? Wait, g6 to h5 is diagonal distance sqrt(2), that's one square away diagonally, so yes, white king protects h5)
- King cannot move to h7 (attacked by queen)
- King cannot move to g7 (controlled by white king)
- King cannot move to g8 (empty, but is it controlled? From g6, white king doesn't control g8. From h5, queen attacks g6, f5, f7, g8, h8, h6-h1, a5-g5...)

From h5, queen attacks g8 (diagonal), so g8 is controlled. This is checkmate.

Let me verify all three scenarios one more time:

**Scenario 1: Back Rank Mate**
FEN: 3R4/5ppp/8/8/8/8/8/6K1 w - - 0 1
Move: Rd8# (or is it already there?)

Let me rebuild scenario 1 properly:
I want a rook to MOVE to the back rank.

White rook on d7, moves to d8#
Black king on g8
Black pawns on f7,g7,h7

Rank 8: . . . . . . k . = 6k
Rank 7: . . . R p p p = 3R3ppp? Let's count: a7,b7,c7 empty, d7=R, e7 empty, f7=pawn, g7=pawn, h7=pawn = 3R1ppp

FEN: 6k/3R1ppp/8/8/8/8/8/6K1 w - - 0 1

Move: Rd8#

From d7 to d8, the rook attacks the black king on g8 horizontally (through e8 and f8). Wait, that's not direct line. Let me place the king on e8.

Better: Black king on e8, rook moves to e8.

Setup:
- Black king e8
- Black pawns f7,g7,h7
- White rook d8 delivering check

Rank 8: . . . . k . . . = 4k3
Rank 7: . . . . p p p = 4ppp

FEN: 4k3/4ppp/8/8/8/8/8/6K1 w - - 0 1

But this is already checkmate, no move needed.

Let me do the classic: rook on d1 moves to d8

Setup:
Rank 8: . . . . . k . . = 5k2
Rank 7: . . . . . p p p = 5ppp
Rank 6: . . . . . . . . = 8
Rank 5: . . . . . . . . = 8
Rank 4: . . . . . . . . = 8
Rank 3: . . . . . . . . = 8
Rank 2: . . . . . . . . = 8
Rank 1: . . . . R . . K = 4R2K

FEN: 5k2/5ppp/8/8/8/8/8/4R2K w - - 0 1

Move: Rd8#

This is clean and classic.

**Scenario 2: Smothered Mate**
FEN: 5nk1/5pp/4N3/8/8/8/8/6K1 w - - 0 1
Move: Nf7#

Let me verify the pieces: 
- Rank 8: 5nk1 = a8 empty, b8 empty, c8 empty, d8 empty, e8 empty, f8 empty, g8 knight, h8 king
- Rank 7: 5pp = a7 empty, b7 empty, c7 empty, d7 empty, e7 empty, f7 empty, g7 pawn, h7 pawn
- Rank 6: 4N3 = a6 empty, b6 empty, c6 empty, d6 empty, e6 knight, f6 empty, g6 empty, h6 empty
- Rank 1: 6K1 = a1 empty, b1 empty, c1 empty, d1 empty, e1 empty, f1 empty, g1 king, h1 empty

Black pieces: king h8, knight g8, pawns g7,h7
White pieces: king g1, knight e6

From e6, knight goes to f7. From f7, knight attacks h8. After Nf7#:
- King on h8 is attacked by knight
- g8 is occupied by black knight
- g7 is occupied by black pawn
- h7 is occupied by black pawn
- King cannot capture the knight (not adjacent)
- King has no moves
- Checkmate.

This is correct.

**Scenario 3: Queen Mate**
FEN: 7k/8/6K/6q/8/8/8/8 w - - 0 1
Move: Qh5#

Wait, the FEN has queen on g5, not h5. Let me check rank 5: 6q = a5 empty, b5 empty, c5 empty, d5 empty, e5 empty, f5 empty, g5 queen, h5 empty.

Yes, queen on g5. Move to h5.

After Qh5+:
- King h8 is in check from queen on h5 (vertical)
- King cannot capture queen on h5 (adjacent? No, h8 to h5 is 3 squares away)
- King cannot move to h7 (attacked by queen)
- King cannot move to g7 (king g6 controls g7)
- King cannot move to g8 (queen g5 attacks g8 via diagonal g5-h6-f7-e8? Wait, from g5 the diagonal to g8 is vertical, not diagonal. From g5, queen attacks g8 (vertical), yes!)

From g5, queen attacks g8 (vertical up). So after moving to h5, queen still attacks g8? No, queen on h5 attacks g6, f5, f7, g8, h8, h6-h1, a5-g5...

From h5, queen attacks:
- g6 (diagonal down-left)
- f7 (diagonal down-left 2)
- e8 (diagonal down-left 3) - yes! This attacks the king on e8, but our king is on h8.

From h5 to g8: file h->g (left 1), rank 5->8 (up 3). Not same file, rank, or diagonal (1 ≠ 3). So queen on h5 does NOT attack g8.

Let me recalculate queen attacks from h5:
- Horizontal: a5-h5
- Vertical: h1-h8
- Diagonal h5-a8: g6, f7, e8
- Diagonal h5-b1: g4, f3, e2, d1

So from h5, queen attacks e8, f7, g6 on the h5-a8 diagonal. It does not attack g8.

So my scenario 3 doesn't work. The king on h8 can move to g8.

Let me fix this:

**Scenario 3: Final Version**
Setup:
- White queen on g6
- White king on g5
- Black king on h8
- Black pawn on h7 (to block h7 and be captured)

Rank 8: . . . . . . . k = 7k
Rank 7: . . . . . . . p = 7p
Rank 6: . . . . . . q . = 6q
Rank 5: . . . . . . K . = 6K
Rank 4: . . . . . . . . = 8
Rank 3: . . . . . . . . = 8
Rank 2: . . . . . . . . = 8
Rank 1: . . . . . . . . = 8

FEN: 7k/7p/6q/6K/8/8/8/8 w - - 0 1

Move: Qxh7#

From g6 to h7 is diagonal. After Qxh7#:
- King on h8 is in check from queen on h7 (adjacent vertical)
- King cannot capture queen (protected by white king on g6? g6 to h7 is diagonal distance sqrt(2), yes, that's one square away diagonally, so king protects h7)
- King cannot move to h7 (occupied by queen)
- King cannot move to g7 (attacked by queen? From h7, queen attacks g7 horizontally. Yes!)
- King cannot move to g8 (attacked by queen? From h7, queen attacks g8 diagonal. Yes!)

From h7, queen attacks:
- g7 (horizontal left)
- g8 (diagonal up-left)
- h8 (vertical up)
- etc.

This is checkmate.

Let me triple-check:
- White pieces: king g5, queen g6
- Black pieces: king h8, pawn h7

Position: 7k/7p/6q/6K/8/8/8/8 w - - 0 1

Move: Qxh7#

Yes, this works.

Actually, you know what, let me make Scenario 3 even simpler and more classic:

**Scenario 3: Queen on 7th**
- White queen on g5
- Black king on g8
- Black pawn on g7

Rank 8: . . . . . . k . = 6k
Rank 7: . . . . . . p . = 6p
Rank 6: . . . . . . . . = 8
Rank 5: . . . . . . q . = 6q
Rank 4: . . . . . . . . = 8
Rank 3: . . . . . . . . = 8
Rank 2: . . . . . . . . = 8
Rank 1: . . . . . . K . = 6K1

FEN: 6k/6p/8/6q/8/8/8/6K1 w - - 0 1

Move: Qxg7#

From g5 to g7 is vertical. After Qxg7#:
- King on g8 is in check from queen on g7 (adjacent vertical)
- King cannot capture queen (not adjacent, queen is below)
- King cannot move to f8 (attacked by queen? From g7, queen attacks f8 diagonal. Yes!)
- King cannot move to h8 (attacked by queen? From g7, queen attacks h8 diagonal. Yes!)
- King cannot move to f7 (attacked by queen? From g7, queen attacks f7 horizontal. Yes!)
- King cannot move to h7 (attacked by queen? From g7, queen attacks h7 horizontal. Yes!)

This is checkmate!

Let me verify the FEN: 6k/6p/8/6q/8/8/8/6K1
- Rank 8: a8 empty, b8 empty, c8 empty, d8 empty, e8 empty, f8 empty, g8 king, h8 empty = 6k
- Rank 7: a7 empty, b7 empty, c7 empty, d7 empty, e7 empty, f7 empty, g7 pawn, h7 empty = 6p
- Rank 6: all empty = 8
- Rank 5: a5 empty, b5 empty, c5 empty, d5 empty, e5 empty, f5 empty, g5 queen, h5 empty = 6q

Perfect. This is clean and simple.

So my three scenarios:
1. Back rank: 4R3k/5ppp/8/8/8/8/8/6K1 w - - 0 1 with Rd8# 
Wait, I need to be consistent. Let me finalize all three with proper FEN and moves.

**Final Scenario 1: Back Rank Mate**
White rook moves from d1 to d8, delivering mate to black king on g8 trapped by pawns.

FEN: 5k2/5ppp/8/8/8/8/8/4R2K w - - 0 1
Move: Rd8#

Let me verify this FEN:
Rank 8: 5k2 = a8 empty, b8 empty, c8 empty, d8 empty, e8 empty, f8 king, g8 empty, h8 empty
Wait, that's wrong. 5k2 means 5 empty, k, 2 empty. That's king on f8. I want king on g8.

5k2: a8,b8,c8,d8,e8 empty, f8 king, g8 empty, h8 empty.
6k1: a8,b8,c8,d8,e8,f8 empty, g8 king, h8 empty.

So for king on g8: 6k1

Rank 8: 6k1
Rank 7: 5ppp (king on g8, pawns on f7,g7,h7)

So: 6k1/5ppp/8/8/8/8/8/4R2K

Now where is the rook? On d1. Rank 1: a1 empty, b1 empty, c1 empty, d1 rook, e1 empty, f1 empty, g1 empty, h1 king = 3R3K

Wait, the notation is: pieces from a to h. So:
a1 empty, b1 empty, c1 empty, d1 rook, e1 empty, f1 empty, g1 empty, h1 king = 3R3K

Rank 1: 3R3K

So FEN: 6k1/5ppp/8/8/8/8/8/3R3K w - - 0 1

Move: Rd8#

This is correct.

**Final Scenario 2: Smothered Mate**
White knight moves to f7 delivering mate to black king on h8 trapped by own pieces.

FEN: 5nk1/5pp/4N3/8/8/8/8/6K1 w - - 0 1
Move: Nf7#

Let me verify:
Rank 8: 5nk1 = g8 knight, h8 king
Rank 7: 5pp = g7 pawn, h7 pawn
Rank 6: 4N3 = e6 knight
Rank 1: 6K1 = g1 king

Move: Knight from e6 to f7 is checkmate. Correct.

**Final Scenario 3: Queen Mate**
White queen captures on g7 delivering mate to black king on g8.

FEN: 6k/6p/8/6q/8/8/8/6K1 w - - 0 1
Move: Qxg7#

Let me verify:
Rank 8: 6k = g8 king
Rank 7: 6p = g7 pawn
Rank 5: 6q = g5 queen
Rank 1: 6K1 = g1 king

Move: Queen from g5 captures pawn on g7. From g7, queen gives check to king on g8. King cannot capture queen (queen is below). King cannot move to f8, h8, f7, h7 (all attacked by queen). Checkmate. Correct.

All three scenarios are distinct:
1. Rook mate (back rank)
2. Knight mate (smothered)
3. Queen mate (corridor/7th rank)

All are valid FEN with white to move ("w" in FEN). All are checkmate in 1 move.

I will format each in its own code block as requested.