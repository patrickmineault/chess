We need to provide 3 mate-in-1 scenarios for white. Each scenario should be in its own code fences, with:
- First line: name of the scenario
- Second line: FEN notation
- Third line: winning move for white

The scenarios should be valid (i.e., the FEN should represent a legal chess position, and the move should indeed be checkmate) and distinct from each other.

Let me think of three distinct mate-in-1 scenarios:

1. A simple back-rank mate
2. A smothered mate
3. A queen delivering mate on the long diagonal

Let me work these out:

**Scenario 1: Back Rank Mate**
A classic back-rank mate where white's rook delivers mate on the 8th rank, while black's king is trapped by its own pieces.

Position: White rook on e8, white pawn on e7, black king on e8 is not possible. Let me rethink.
White rook on e8 delivering check to black king on e8? No, that's not right.

Better: White rook on e8, black king on g8, black pawns on f7, g7, h7, and white rook on e8 gives check. But the black king could move to f8 or h8.

Let me construct a proper back-rank mate:
White: Rook on e8
Black: King on g8, pawns on f7, g7, h7, and maybe some pieces blocking escape squares.

Actually, a typical back-rank mate: White rook on e8, black king on g8, black pawn on g7, black pawn on f7, black pawn on h7, and black pieces blocking f8 and h8.

Let's say black has a bishop on f8 and a knight on h8.
FEN: 4Rbk1/5ppp/8/8/8/8/8/4K3 w - - 0 1
Wait, that would be: white rook e8, black bishop f8, black king g8, black pawn g7, black pawn h7, black pawn f7.
Let me check: 
- white rook on e8
- black bishop on f8
- black king on g8
- black pawn on f7, g7, h7

FEN: 4Rbk1/5ppp/8/8/8/8/8/4K3 w - - 0 1

Is this valid? Let's parse: ranks 8 to 1.
Rank 8: 4Rbk1 = empty, empty, empty, empty, R, b, k, empty
Rank 7: 5ppp = empty, empty, empty, empty, empty, p, p, p
So: white rook e8, black bishop f8, black king g8, black pawns f7, g7, h7.
Black's pieces block f8 and h8. The king on g8 is trapped by its own pawn on g7.
White rook on e8 gives check along the e-file. Can the king move? No, all squares are covered:
- f8: occupied by black bishop
- h8: would be off board? No, h8 is empty in this FEN. Wait, let me recount: 4Rbk1 is 4 empties, R, b, k, 1 empty. So squares are: a8 empty, b8 empty, c8 empty, d8 empty, e8 R, f8 b, g8 k, h8 empty.
So the king could move to h8? No wait, the rook on e8 attacks e8 horizontally and vertically. From e8, it attacks g8? No, e8 to g8 is horizontal: e8-f8-g8. f8 has a black bishop, so the rook doesn't attack g8 through the bishop. That's wrong.

Let me reconsider. The rook needs to attack the king directly.
For a back-rank mate, the rook (or queen) delivers check on the 8th rank, and the king is trapped by its own pieces.

Example: White rook on e8 delivering check to black king on g8.
But for the rook on e8 to attack g8, the squares between must be empty.
So: white rook on e8, black king on g8, and f8 must be empty.
But then the king could move to f8 or h8.

Let me create a proper position:
White: Rook on e8
Black: King on g8, pawn on g7, pawn on f7, pawn on h7, piece on f8, piece on h8

Let's try:
White rook e8, black king g8, black pawn f7, g7, h7, black knight f8, black bishop h8.
FEN: 4Rnk1/5ppp/8/8/8/8/8/4K3 w - - 0 1

Wait, that's: a8 empty, b8 empty, c8 empty, d8 empty, e8 R, f8 n, g8 k, h8 empty. No, that's not right.
"4Rnk1" = 4 empties, R, n, k, 1 empty. So: a8., b8., c8., d8., e8R, f8n, g8k, h8.

Let's try again with proper notation:
Rank 8: a8 empty, b8 empty, c8 empty, d8 empty, e8 white rook, f8 black knight, g8 black king, h8 empty
Rank 7: a7 empty, b7 empty, c7 empty, d7 empty, e7 empty, f7 black pawn, g7 black pawn, h7 black pawn

FEN: 4Rnk1/5ppp/8/8/8/8/8/4K3 w - - 0 1

Now, does Re8+ mate the black king on g8? No, the rook on e8 doesn't attack g8 because the knight on f8 blocks.

I need the checking piece to attack the king directly.

Better approach: Let's use a queen for a back-rank mate.
White queen on e8 delivering check to black king on e8? No, that's capture.

White queen on e8 delivering check to black king on g8.
For queen on e8 to attack g8, squares between must be empty: f8 must be empty.
Position:
White queen e8, black king g8, black pawn g7, black pawn f7, black pawn h7, black rook f8, black bishop h8.

FEN: 4Qrk1/5ppp/8/8/8/8/8/4K3 w - - 0 1

Let's parse: a8., b8., c8., d8., e8Q, f8r, g8k, h8.
Rank 7: a7., b7., c7., d7., e7., f7p, g7p, h7p.

Queen on e8 attacks g8 horizontally: e8-f8-g8. f8 has a black rook, so queen does NOT attack g8. Wrong again.

The checking piece must have line-of-sight to the king.

Let me think of a real back-rank mate pattern:
White rook on e8, black king on g8 trapped between pieces. The rook doesn't need to attack the king directly if it's a discovered check? No, that's not a back-rank mate.

Standard back-rank mate: White rook (or queen) on the 8th rank gives check, and the king cannot move because its own pieces block escape squares, and it cannot capture because the checking piece is protected or out of reach.

Example: White queen on e8, black king on g8, black pawn on g7, white bishop on h8 (protecting queen), black pieces blocking f8 and h8.

Wait, if white queen is on e8 and black king on g8, they don't interact directly.

Let me simplify: King on e8, queen on e1 gives check on the file. But that's not back-rank.

**Proper Back-Rank Mate:**
White queen on e8 delivering check to black king on e8? No.

Let's use: White rook on e8 delivering check to black king on e8? No, that's capture.

I think I'm confusing myself. A back-rank mate is when a rook or queen gives check ON the back rank (rank 8 for black), and the opponent's king is trapped on that rank by its own pieces.

The checking piece attacks the king along the rank.
Example: White queen on a8, black king on e8, black pieces on b8, c8, d8, f8, g8, h8 blocking escape.

But the queen needs line-of-sight: a8 to e8 requires b8, c8, d8 to be empty. So that doesn't work.

**Correct Pattern:** The checking piece is adjacent to the king or attacks it directly with nothing in between.

Let's try: White queen on e8, black king on e8? No.

White queen on f8 delivering check to black king on e8. Yes! That's a direct attack.
If queen on f8 attacks e8, and black's own pieces block all escape squares on the 8th rank and the 7th rank squares are controlled or occupied.

Position:
White queen f8, black king e8, black pawn e7, black pieces on d8 and g8 blocking escape, black pieces or white control of d7 and f7.

FEN: 3qk3/4p3/8/8/8/8/8/4K3 w - - 0 1
This is: d8q, e8k, f8., with black queen on d8. But white queen is delivering the mate.

Let's create it properly:
White: Queen f8
Black: King e8, pawn e7, rook d8, knight g8, and white controls/occupies d7 and f7.

FEN: 2rqk2Q/4p3/8/8/8/8/8/4K3 w - - 0 1
No, that's black queen on d8.

Let me use a simpler, clearly valid position:
**Scenario 1: Rook Back-Rank Mate**
White rook on e8, black king on g8, black knight on f8 (blocking), black pawn on g7. This doesn't work.

Okay, let me look up a standard FEN for back-rank mate and adapt it.

Standard example: 
White pieces: Re8
Black pieces: Kg8, Pf7, Pg7, Ph7, Nf8, Bh8
But as established, Re8 doesn't give check to Kg8.

**Another pattern:** White queen on e7 delivering check to king on e8, with the back rank blocked.
FEN: 3rkb1r/4Qppp/8/8/8/8/8/4K3 w - - 0 1
This is: d8r, e8k, f8b, g8., h8r. Queen on e7 attacks e8. Black's back rank has r k b r. 
King on e8 can move to f8 (occupied by bishop), d8 (occupied by rook), or g8 (empty). Not mate.

This is harder than I thought. Let me be more systematic.

**Mate in 1 means:**
1. White makes a move
2. That move puts black in check
3. Black has NO legal moves to get out of check

The move can be:
- A direct checking move (move a piece to give check)
- A discovered check (move a piece that reveals a checking line)
- En passant (rare but possible)
- Promotion (which also gives check)

**Scenario 1: Back-Rank Mate with Rook**
Let's create a proper one:
Black king on f8. White rook on f1. But that requires the whole file to be empty.

White rook on f8 delivering check to black king on f8? No, that's capture.

**I got it:** White queen moves to the back rank, delivering check, and the king is trapped.
The key is the checking piece must attack the king.

Black king on e8. White queen on e1. The file is empty. Qe8#.
But for that to be mate, black's back rank must be blocked.

Position:
- White: King e1, Queen d1, Rook a1, Rook h1
- Black: King e8, Queen d8, Rook a8, Rook h8, pawns a7, b7, c7, d7, e7, f7, g7, h7

FEN: r2qk2r/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1

Now, if white could play Qd8+, is that mate? No, black king on e8, queen on d8 attacks e8. 
Black's escape squares: d7 (occupied by pawn), e7 (pawn), f7 (pawn), f8 (empty), d8 (now queen), f8 (empty), d7, e7, f7.

Let me create a forced mate position:

**Scenario 1: Smothered Mate**
This is a classic. White knight delivers check to a king surrounded by its own pieces.

Position: Black king on h8, black pawn on h7, black pawn on g7, black bishop/knight on g8.
White knight on f7 delivers mate: Nf7# or Ng6# if the king is on h8 and g8 is blocked.

Let's construct:
Black king h8, black pawn g7, black pawn h7, black piece on g8 (say, a queen).
White knight on f6: Nf7#? No, from f6, knight goes to g8 or h7 or h5, etc.

From f6, knight to g8 attacks h6 and e7, not the king.

White knight on f7 attacks g5, h6, h8, g9(offboard), e9(offboard), d8, d6, e5.
So knight on f7 attacks h8! Yes!

FEN for smothered mate:
Black: King h8, Queen g8, pawn g7, pawn h7
White: Knight f7, King somewhere

FEN: 6qk/5pp1/8/8/8/8/8/4K3 w - - 0 1

Let's parse: a8., b8., c8., d8., e8., f8., g8q, h8k
Rank 7: a7., b7., c7., d7., e7., f7., g7p, h7p

Knight on f7? The FEN says "6qk" which means g8 is queen, h8 is king. Square f8 is empty. Where is the knight?

The FEN should include the white knight on f7.
Rank 8: a8., b8., c8., d8., e8., f8., g8q, h8k
Rank 7: a7., b7., c7., d7., e7., f7N, g7p, h7p

So: 6qk/5Np1/8/8/8/8/8/4K3 w - - 0 1

Let's recount rank 7: "5Np1" = 5 empties, N, p, 1 empty? No.
"5Np1" = a7 empty, b7 empty, c7 empty, d7 empty, e7 empty, f7 N, g7 p, h7 empty. That's wrong, we need pawn on h7.

"5Npp" = a7., b7., c7., d7., e7., f7N, g7p, h7p
So: 6qk/5Npp/8/8/8/8/8/4K3 w - - 0 1

Now, white knight on f7. The move is Nh6#? No, from f7 knight moves to h8, g9(offboard), e9(offboard), d8, d6, e5, g5, h6.
Knight on f7 attacks h8 (the black king) and d8. 

Wait, from f7:
- +2 ranks, +1 file: g9 (offboard)
- +2 ranks, -1 file: e9 (offboard)
- +1 rank, +2 files: h8 (YES!)
- +1 rank, -2 files: d8 (square)
- -1 rank, +2 files: h6
- -1 rank, -2 files: d6
- -2 ranks, +1 file: g5
- -2 ranks, -1 file: e5

So knight on f7 attacks h8 (the king) and d8. The move is Nxh8? No, that's capture.

The move is simply: The knight is already on f7? No, the knight must MOVE to deliver mate.

The position should have the knight ready to move to the mating square.

For smothered mate: Knight moves to a square where it attacks the surrounded king.
Example: King on h8, surrounded by pawn h7, pawn g7, piece on g8. Knight moves to f7 to attack h8.

But the knight should start elsewhere and move to f7.

Position before move:
White knight on d6 or h6 or g5 or e5, etc.

Let's use: White knight on d6 moves to f7#.
FEN: 6qk/5pp1/3N4/8/8/8/8/4K3 w - - 0 1

Rank 8: a8., b8., c8., d8., e8., f8., g8q, h8k
Rank 7: a7., b7., c7., d7., e7., f7., g7p, h7p
Rank 6: a6., b6., c6., d6N, e6., f6., g6., h6.

So FEN: 6qk/5pp1/3N4/8/8/8/8/4K3 w - - 0 1

Is this valid?
- White king on e1
- White knight on d6
- Black king on h8
- Black queen on g8
- Black pawn g7, h7

Move: Nd6-f7#. The knight on f7 attacks h8. Is the king surrounded?
King on h8: squares are:
- g8: occupied by black queen
- h7: occupied by black pawn
- g7: occupied by black pawn
- g8 is not a move anyway (king can't move into check from knight)
- The knight on f7 attacks h8. Can the knight be captured? No, by nothing (queen on g8 doesn't attack f7).
Can king move? No. g8 is occupied by own piece. h7 is occupied by own piece. g7 is occupied by own piece.

This seems like a valid smothered mate pattern! The black queen on g8 is actually helping.

Let me verify the knight's move: Nf7# from d6 is correct. The knight lands on f7 and attacks h8.

**Scenario 2: Simple Queen Mate**
Queen delivers check on a square adjacent to the king, and all escape squares are covered.

Black king on h8. White queen on h7 delivering check.
But we need queen to move to h7.

Position:
White queen on d3, black king on h8, black pawn on h7, white bishop on g6 covering h7.

If queen moves to h7: Qxh7#? But that's capture of pawn.

Queen moves to h7, delivering check to king on h8 (adjacent).
FEN: 5bk1/6pp/6B1/8/8/3Q4/8/4K3 w - - 0 1

Let's parse:
Rank 8: a8., b8., c8., d8., e8., f8b, g8k, h8.
No, "5bk1" = a8., b8., c8., d8., e8., f8b, g8k, h8.
Rank 7: "6pp" = a7., b7., c7., d7., e7., f7., g7p, h7p
Rank 6: "6B1" = a6., b6., c6., d6., e6., f6., g6B, h6.

So: black king g8, black bishop f8, black pawns g7, h7, white bishop g6, white queen d3.

If queen moves to h7: Qxh7+, but that's check to king on g8? No, queen on h7 attacks g8 (adjacent). Yes!

Qxh7#: Queen captures pawn on h7 and attacks g8. Can black king on g8 move?
- g8 to f8: f8 occupied by own bishop
- g8 to f7: f7 empty, but is it attacked? Queen on h7 attacks f7 (diagonal). Yes!
- g8 to g7: g7 occupied by own pawn
- g8 to h7: now queen
- g8 to h8: h8 empty? Wait, "5bk1" means h8 is the '1' (empty). But that can't be right.

Let's recount: "5bk1" = 5 empties, b, k, 1 empty. So squares: a8., b8., c8., d8., e8., f8b, g8k, h8.
Wait, "5bk1" is 8 squares: 5 + 1 + 1 + 1 = 8.
So: a8 empty, b8 empty, c8 empty, d8 empty, e8 empty, f8 bishop, g8 king, h8 empty.

But we want king on h8. So "6bk" would be 6 empties, b, k = a8., b8., c8., d8., e8., f8., g8b, h8k.

Let's fix:
**Scenario 2: Queen Mate**
Black king on h8, black pawn on g7, black pawn on h7, white queen moves to h7.

FEN before move: 6k1/5pp1/8/8/8/3Q4/8/4K3 w - - 0 1

Rank 8: a8., b8., c8., d8., e8., f8., g8., h8k
Rank 7: a7., b7., c7., d7., e7., f7., g7p, h7p

Move: Qxh7#. Queen on d3 captures pawn on h7.
From h7, queen attacks g8 (empty), h8 (king's square), g8.
Wait, queen on h7 attacks g8 (diagonal), but the king is on h8. Queen on h7 attacks h8 vertically! Yes!

From h7, queen attacks:
- Vertically: h8 (king), h6, h5...
- Horizontally: a7-g7, i7(offboard)
- Diagonally: g8, f9(offboard), g6, f5...

So Qxh7# delivers check to king on h8. Can the king move?
- g8: empty, but attacked by queen on h7
- h8 is the square it's on
- g7: occupied by own pawn

What about capture? King on h8 cannot capture queen on h7 because the queen is protected? By what? In this position, nothing protects it. So the king COULD capture: Kxh7.

So I need to protect the queen. Let's add a white bishop on g6:
FEN: 6k1/5pp1/6B1/8/8/3Q4/8/4K3 w - - 0 1

Rank 8: a8., b8., c8., d8., e8., f8., g8., h8k
Rank 7: a7., b7., c7., d7., e7., f7., g7p, h7p
Rank 6: a6., b6., c6., d6., e6., f6., g6B, h6.

Position: Black king h8, black pawns g7,h7, white bishop g6, white queen d3.
Move: Qxh7#.
Check: Yes, queen on h7 attacks h8.
Can king capture? King on h8 could capture queen on h7 (Kxh7), but the queen is protected by bishop on g6! Bishop on g6 attacks h7. So Kxh7 is illegal.
Can king move to g8? g8 is attacked by queen on h7. Illegal.
Can king move to g7? g7 occupied by own pawn.
So it's checkmate. This works!

**Scenario 3: Arabian Mate or Rook+Bishop Mate**
Rook delivers check on back rank, bishop covers escape square.

Black king on h8. White rook on h7 delivering check? No, need to move.

Black king on g8. White rook on g7 delivering check? Rook moves to g7.

Position: Black king g8, black pawn f7, black pawn g7, black pawn h7, white rook on a7, white bishop on h7? No.

Let's do: White rook moves to g8, delivering check to king on h8. Bishop covers escape square f8.

Black king h8, black pawn f7, g7, h7. White bishop on b4 covering f8? No, diagonal.

White bishop on c5 attacks f8 (c5-d6-e7-f8). Yes!

FEN: 6k1/4ppp1/8/2B5/8/8/8/4K3 w - - 0 1

Rank 8: a8., b8., c8., d8., e8., f8., g8., h8k
Rank 7: a7., b7., c7., d7., e7., f7p, g7p, h7p
Rank 6: a6., b6., c6., d6., e6., f6., g6., h6.

Position: Black king h8, black pawns f7,g7,h7, white bishop c5, white rook... where?
White rook needs to move to g8.

So add white rook on a8? No, it needs to move.
White rook on g3? It moves to g8.

FEN with white rook: 6k1/4ppp1/8/2B5/8/6R1/8/4K3 w - - 0 1

Rank 3: a3., b3., c3., d3., e3., f3., g3R, h3.

Move: Rg8#. 
Does rook on g8 give check to king on h8? Yes, horizontally adjacent.
Can king move? 
- g7: occupied by pawn
- h7: occupied by pawn
- g8: now the rook
Can king capture? Kxg8? Is the rook protected? Bishop on c5 attacks g1, not g8. Bishop on c5 attacks f8, g7, h6.

From c5, bishop attacks:
- NE: d6, e7, f8
- NW: b6, a7
- SE: d4, e3, f2, g1
- SW: b4, a3

So bishop on c5 does NOT protect g8. So Kxg8 is legal unless something else protects it.

Let me add a white pawn on g2 that protects g3? No, that doesn't help.

Better: White queen on g2 protects g8, but that's too powerful.

Alternative pattern: Rook on h7 delivering check to king on h8, bishop covers g8.

Position: Black king h8, black pawn g7, black pawn h7, white bishop on c4 covering g8? c4-d5-e6-f7-g8. Yes!

FEN: 6k1/5pp1/8/8/2B5/7R/8/4K3 w - - 0 1

Rank 8: a8., b8., c8., d8., e8., f8., g8., h8k
Rank 7: a7., b7., c7., d7., e7., f7., g7p, h7p
Rank 4: a4., b4., c4B, d4., e4., f4., g4., h4.
Rank 3: a3., b3., c3., d3., e3., f3., g3R, h3.

Move: Rh3-h7#? No, that's not a standard notation. The rook is on h3, moving to h7.
Notation: Rh7#.

Rook on h7 attacks h8 (king) vertically. Check.
Can king capture? Kxh7? Is the rook protected?
From h7, it's protected by bishop on c4? c4-d5-e6-f7-g8-h7? No, that's not the diagonal. c4 to h7 is c4-d5-e6-f7-g8-h9(offboard). Wrong direction.

c4 to h7 is: c4-d5-e6-f7-g8-h9(offboard). No.
c4 to h7: c4-d5-e6-f7-g8-h9. No.

c4-b5-a6
c4-d5-e6-f7-g8
c4-b3-a2
c4-d3-e2-f1

So bishop on c4 does NOT protect h7. Let me recalculate.

A bishop on d4 would protect h8 (d4-e5-f6-g7-h8) and a7 (d4-c5-b6-a7).

I need the bishop to protect the rook's mating square OR control the king's escape squares.

**Arabian Mate:** Rook on h7, king on h8, bishop on g7? No.

Let me try a different simple pattern:
**Scenario 3: En Passant Mate** (less common, interesting)
This would be distinctive.

Black pawn on g7 moves from g7 to g5 (two squares), passing white pawn on h5 which can capture en passant: hxg6#.
For this to be mate, the resulting position must be checkmate.

Position before black's move:
White: King e1, pawn h5, bishop g5 (giving check along the 5th rank?), no.

Standard en passant mate pattern:
Black king on e8. Black pawn on g7 moves to g5. White pawn on h5 captures en passant: hxg6, delivering check by opening a line for bishop or rook.

Let's try: White bishop on b5 giving diagonal check after pawn moves.
White rook on h1 giving horizontal check? No.

Better: White queen or bishop battery.
White bishop on h5, white queen on g5. Black pawn on g7-g5 blocks. After hxg6, bishop gives check.

Wait, en passant capture happens on the 6th rank for white (if black moved 7->5).
So hxg6 means white pawn from h5 goes to g6.

Position BEFORE en passant:
White: King e1, pawn h5, bishop b1-d3-f5-h7 diagonal? Let's trace: b1-c2-d3-e4-f5-g6-h7.
So white bishop on f5 attacks h7. Black pawn on g6 blocks? No.

This is getting too complex. Let me use a simpler, more direct pattern.

**Revised Scenario 3: Pawn Promotion Mate**
White pawn promotes to queen (or other piece) delivering checkmate.

Pawn on g7 promotes to queen on g8, mating king on h8.

Position: White pawn g7, black king h8, black pawn h7, black pawn g8? No, pawn promotes on g8.

FEN: 6k1/6Pp/7P/8/8/8/8/4K3 w - - 0 1

Rank 8: a8., b8., c8., d8., e8., f8., g8., h8k
Rank 7: a7., b7., c7., d7., e7., f7., g7P, h7p
Rank 6: a6., b6., c6., d6., e6., f6., g6., h6P

White pawn on g7, black king h8, black pawn h7, white pawn h6 blocking? No.

Let's try again:
Pawn on g7, black king h8, black pawn h7.
FEN: 6k1/6Pp/8/8/8/8/8/4K3 w - - 0 1

Rank 8: a8., b8., c8., d8., e8., f8., g8., h8k
Rank 7: a7., b7., c7., d7., e7., f7., g7P, h7p

Move: g8=Q# 
Pawn moves from g7 to g8 and becomes queen. 
Does this give check? Queen on g8 attacks h8 horizontally. Yes!
Can king move?
- g7: empty now (pawn moved)
- h7: occupied by pawn
- g8: now queen

Can king move to g7? Is g7 attacked? Queen on g8 attacks g7 vertically. Yes!
Can king capture? Kxg8? Nothing protects g8. So it's NOT mate.

Need to protect the promotion square.
White bishop on d5 protects g8? d5-e6-f7-g8. Yes!

FEN: 6k1/6Pp/8/3B4/8/8/8/4K3 w - - 0 1

Rank 8: a8., b8., c8., d8., e8., f8., g8., h8k
Rank 7: a7., b7., c7., d7., e7., f7., g7P, h7p
Rank 5: a5., b5., c5., d5B, e5., f5., g5., h5.

Move: g8=Q# (or g8=Q+ but it should be #)
Promotion gives check from g8 to h8.
King cannot capture: Kxg8 is illegal because bishop on d5 protects g8.
King cannot move to g7: g7 is attacked by queen on g8.
King cannot move to h7: occupied by own pawn.

Yes! This works.

**Summary of three scenarios:**

1. **Smothered Mate**: Knight delivers mate to a king surrounded by its own pieces.
   FEN: 6qk/5Npp/8/8/8/8/8/4K3 w - - 0 1
   Move: Nf7# (Wait, need the knight to move TO the mating square, not start there)

   Let me fix this once more. The FEN shows the position BEFORE white moves.

   **Corrected Scenario 1: Smothered Mate**
   White knight moves to f7, delivering check to king on h8 which is surrounded.
   
   Position before: Black king h8, black queen g8, black pawns g7,h7. White knight on d6 or e5 or h6.
   
   Let's use knight on e5: Ne5-f7#
   FEN: 6qk/5pp1/8/4N3/8/8/8/4K3 w - - 0 1

   Rank 8: a8., b8., c8., d8., e8., f8., g8q, h8k
   Rank 7: a7., b7., c7., d7., e7., f7., g7p, h7p
   Rank 5: a5., b5., c5., d5., e5N, f5., g5., h5.

   Move: Nf7# 
   Knight from e5 to f7 attacks h8. King surrounded by Qg8, pg7, ph7. Kxg7 illegal, Kxg8 illegal, Kh7 illegal. Works!

2. **Queen Mate**: Queen captures pawn delivering check, protected by bishop.
   FEN: 6k1/5pp1/6B1/8/3Q4/8/8/4K3 w - - 0 1
   Move: Qxh7#

3. **Promotion Mate**: Pawn promotes to queen with check, protected by bishop.
   FEN: 6k1/6Pp/8/3B4/8/8/8/4K3 w - - 0 1
   Move: g8=Q#

Wait, I need to double-check all these FENs and moves for validity.

**Final Verification:**

**Scenario 1: Smothered Mate**
FEN: `6qk/5pp1/8/4N3/8/8/8/4K3 w - - 0 1`
Board:
- Rank 8: a8., b8., c8., d8., e8., f8., g8q, h8k
- Rank 7: a7., b7., c7., d7., e7., f7., g7p, h7p
- Rank 5: a5., b5., c5., d5., e5N, f5., g5., h5.
- Rank 1: e1K

Move: `Nf7#`
Knight e5 to f7. Knight on f7 attacks h8.
Black king on h8: possible moves:
- Kxg8: illegal (king cannot capture own queen)
- Kxg7: illegal (king cannot capture own pawn)
- Kh7: illegal (occupied by own pawn)
- Kg8: illegal (occupied by own piece)
- The king is in check from the knight, cannot move to any adjacent square that isn't occupied by own piece. All empty squares (if any) would be g8 (occupied) and... actually that's it. The 8 squares around h8 are:
  - g7 (occupied by pawn), h7 (pawn), g8 (queen)
  - Plus squares the king could move to if empty: g7, g8
  - g7 is attacked by the knight? From f7, knight attacks g5, h6, h8, d8, d6, e5, g9(offboard), e9(offboard). So g7 is NOT attacked by the knight. But g7 is occupied.
  - g8 is not attacked by the knight either, but occupied.

Wait, smothered mate usually means the king has NO MOVES because all squares are occupied. The knight's check is unavoidable because the king cannot capture the knight and cannot move.

In this position, the king has no legal moves regardless of the check. So the checkmate is valid.

But IS the knight on f7 delivering check? Yes, knights attack in an L-shape. From f7: 
- (+2,+1) = g9 (offboard)
- (+2,-1) = e9 (offboard)
- (+1,+2) = h8 (YES!)
- (+1,-2) = d8
- (-1,+2) = h6
- (-1,-2) = d6
- (-2,+1) = g5
- (-2,-1) = e5

So yes, the knight on f7 attacks h8. The king is in check. King cannot capture the knight. King cannot move due to own pieces. Checkmate. Valid!

**Scenario 2: Queen Mate**
FEN: `6k1/5pp1/6B1/8/3Q4/8/8/4K3 w - - 0 1`
Board:
- Rank 8: a8., b8., c8., d8., e8., f8., g8., h8k
- Rank 7: a7., b7., c7., d7., e7., f7., g7p, h7p
- Rank 6: a6., b6., c6., d6., e6., f6., g6B, h6.
- Rank 4: a4., b4., c4., d4Q, e4., f4., g4., h4.
- Rank 1: e1K

Move: `Qxh7#`
Queen d4 captures pawn on h7 (Qxh7+). Queen now on h7.
Check: Queen on h7 attacks h8 (vertical), so black king is in check.
Can king capture? Kxh7? Bishop on g6 attacks h7 (diagonal g6-h7). Yes! So Kxh7 is illegal.
Can king move to g8? g8 is empty and not attacked by queen on h7? Wait, queen on h7 attacks g8 (diagonal h7-g8). Yes! So Kg8 is illegal.
Can king move to g7? g7 occupied by own pawn.
Perfect. This is valid checkmate.

**Scenario 3: Promotion Mate**
FEN: `6k1/6Pp/8/3B4/8/8/8/4K3 w - - 0 1`
Board:
- Rank 8: a8., b8., c8., d8., e8., f8., g8., h8k
- Rank 7: a7., b7., c7., d7., e7., f7., g7P, h7p
- Rank 5: a5., b5., c5., d5B, e5., f5., g5., h5.
- Rank 1: e1K

Move: `g8=Q#`
Pawn from g7 moves to g8 and becomes queen (or Q for short).
New position: Queen on g8, pawn removed from g7.
Check: Queen on g8 attacks h8 (horizontal), so king is in check.
Can king capture? Kxg8? Bishop on d5 attacks g8 (diagonal d5-e6-f7-g8). Yes! So Kxg8 is illegal.
Can king move to g7? g7 is now empty (pawn moved). Is g7 attacked? Queen on g8 attacks g7 vertically. Yes! So Kg7 is illegal.
Can king move to h7? h7 occupied by own pawn.
Valid checkmate!

All three scenarios are distinct and valid. Let me format them as requested.