<budget:thinking>
I need to come up with 3 distinct mate-in-1 scenarios for white. Let me think of some classic patterns.

**Scenario 1: Back Rank Mate**
A classic where a rook or queen delivers mate on the back rank when the king is trapped by its own pawns.

Setup: White has a rook, black king is on g8 with pawns on f7, g7, h7.
Let's say: White King on g1, White Rook on e1, Black King on g8, Black pawns on f7, g7, h7.

FEN: 6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1
Move: Re8# (Rook to e8 is checkmate)

Let me verify: Black king on g8, pawns on f7, g7, h7. Rook goes to e8. King can't go to f8 (rook controls it), can't go to h8 (rook controls it), can't go to g7, f7, h7 (own pawns). Yes, that's mate.

**Scenario 2: Scholar's Mate type / Queen and Bishop mate**
Let's do a simple queen mate with support.

Setup: Black king on e8, White Queen on h5, White Bishop on c4 aiming at f7. Queen can go to f7 for mate.

Actually let me think of a cleaner one. 

White Queen on d1, can go to d8 for back rank mate? Let's try a different pattern.

**Smothered Mate:**
Black king on g8, Black rook on f8, Black pawns on g7, h7. White Knight on f7. Knight goes to h6... no wait, that's not right.

Actually for smothered mate: King on g8, own pieces on f8, g7, h7. Knight delivers mate from f7 or h6? 

Knight on f7 gives check. King can't move to h8 (knight covers), f8 is blocked, g7 is blocked, h7 is blocked. That's smothered mate if knight is already attacking from somewhere.

Setup: White Knight on e5, Black King on g8, Black Rook on f8, Black pawns on g7, h7, h6.
Knight goes from e5 to f7? Let me check: e5 to f7 is a valid knight move? e5 -> d7, f7, g6, g4, c4, c6, d3, f3. Yes, f7 is valid.

Nf7#: King on g8 is in check from knight on f7. King can't go to:
- h8: knight on f7 covers h8? Knight on f7 covers: e5, g5, h6, h8, d6, d8. Yes h8 is covered!
- f8: blocked by rook
- g7: blocked by pawn
- h7: blocked by pawn

Yes! That works.

FEN: 5rk1/6pp/7p/4N3/8/8/8/6K1 w - - 0 1
Move: Nf7#

Wait, I need to double-check the knight on f7 coverage. A knight on f7 attacks: e5, g5, d6, h6, d8, h8. Yes, h8 is covered.

**Scenario 3: Anastasia's Mate or simple Queen + Rook mate**

Let me do a simple one - Queen supported by another piece.

Black King on h8, White Queen on g6, White Knight on f7. 
Qg8#? Knight supports g8? No, knight on f7 doesn't cover g8. Knight on f7 covers e5, g5, d6, h6, d8, h8.

Let me try: White Queen on a1, Black King on h8, White Bishop on b2.
Qa8#? Bishop on b2 attacks the a1-h8 diagonal. If Queen goes to a8, is it mate? King on h8, Queen on a8 gives check along the 8th rank. King can go to g7? Yes, not blocked. Not mate.

Let me try another classic - the Arabian Mate:
Rook and Knight combo. King in corner, Rook gives check, Knight covers escape squares.

Black King on h8, White Rook on h1, White Knight on f7.
Rh8 is where the king is, so Rh8 is not legal as a move (that square is occupied). 

Wait, I need to set up a position where white can DELIVER mate in one move.

Black King on g8, White Rook on h1, White Knight on e7.
Rh8#? King on g8, Rook goes to h8. Check. King can go to f7 (is it blocked? no). Not mate.

Let me think more carefully.

Arabian Mate setup: King in corner (h8), Rook on the h-file giving check, Knight covering g8 and f7 escape.

Position: Black King on h8, White Knight on f7 (covers g5, e5, d6, h6, d8, h8). Hmm, knight on f7 doesn't cover g8.

Knight on g6! Knight on g6 covers: f8, h8, e7, e5, f4, h4. 
So Black King on h8 (covered by Ng6), and if we have Rook that can go to h-file...

Setup: Black King h8, Black pawn g7, White Knight on f6, White Rook on h1.
Knight on f6 covers: e8, g8, d7, h7, d5, h5, e4, g4.
Rh8+? But King is on h8... I need king to not be on the mating square.

Let me restart. In Arabian mate, typically:
- King on h8
- Rook delivers check from, say, h1 by going to h8? No.

Actually, a standard Arabian Mate:
- Black King on g8
- White Rook on h8 giving check
- White Knight on f7 covering g5 and e5... no wait.

Hmm, let me look at this differently. Let me set up a position:

Black King on g8
White Rook can move to h8 - but that would require the h8 square empty
White Knight on f6

If Rh8#:
- King on g8 gets check from Rh8
- King tries to escape: f7 (is it covered? Knight on f6 doesn't cover f7. f6 covers e8, g8, d7, h7, d5, h5, e4, g4). f7 is free!

This isn't working. Let me try knight on e6.
Knight on e6 covers: f8, d8, c7, g7, c5, g5, d4, f4.
If Rh8+, King on g8 can go to f7. Not covered. Not mate.

Let me try a two-piece mate that's simpler.

**Queen and King mate (ladder/box mate):**
Black King on a8, White Queen on b6, White King on c6.
Qa7#. King on a8 in check from Qa7. King can go to b8? Queen on a7 covers b8 (a7 covers a8, b8, c7, etc along ranks/files/diagonals). Is b8 covered? Yes, Queen on a7 attacks b8 diagonally. What about... that's it. Qa7#.

FEN: k7/8/1QK5/8/8/8/8/8 w - - 0 1
Move: Qa7#

Let me verify: Queen on b6 moves to a7. King on a8 is in check. 
- b8: Queen on a7 attacks b8 (diagonal). Covered.
- a7: Queen is there.
- b7: Queen on a7 attacks b7 (diagonal). Covered.
So it's mate!

Actually wait - the King on c6 also matters for coverage. Let me re-examine.
- a8: King in check from Qa7
- b8: covered by Qa7 (diagonal a7-b8)
- b7: covered by Qa7 (diagonal)
- a7: Queen is there

Yes, checkmate.

Let me compile my three scenarios:

1. Back Rank Mate
FEN: 6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1
Move: Re8#

2. Smothered Mate (Knight)
FEN: 5rk1/6pp/8/4N3/8/8/8/6K1 w - - 0 1
Move: Nf7#

Wait, I had h6 pawn before. Let me recheck without it.
Black: King g8, Rook f8, pawns g7, h7.
White: Knight e5, King g1.
Nf7#: King in check. Can go to h8? Knight on f7 covers h8. Can go to f8? Blocked by rook. g7? pawn. h7? pawn. 
Checkmate!

FEN: 5rk1/6pp/8/4N3/8/8/8/6K1 w - - 0 1
Move: Nf7#

3. Queen and King Box Mate
FEN: k7/8/1QK5/8/8/8/8/8 w - - 0 1
Move: Qa7#

These all look good! Let me just double-check the FEN notations.

FEN 1: 6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1
Row 8: 6 empty, k, 1 empty = 6k1 ✓
Row 7: 5 empty, p, p, p = 5ppp ✓
Row 6-2: all empty = 8 each ✓
Row 1: 4 empty, R, 1 empty, K, 1 empty = 4R1K1 ✓

FEN 2: 5rk1/6pp/8/4N3/8/8/8/6K1 w - - 0 1
Row 8: 5 empty, r, k, 1 empty = 5rk1 ✓
Row 7: 6 empty, p, p = 6pp ✓
Row 6: 8 empty ✓
Row 5: 4 empty, N, 3 empty = 4N3 ✓
Row 4-2: 8 each ✓
Row 1: 6 empty, K, 1 empty = 6K1 ✓

FEN 3: k7/8/1QK5/8/8/8/8/8 w - - 0 1
Row 8: k, 7 empty = k7 ✓
Row 7: 8 empty ✓
Row 6: 1 empty, Q, K, 5 empty = 1QK5 ✓
Row 5-1: 8 each ✓

All look correct!
</budget:thinking>

```
Back Rank Mate
6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1
Re8#
```

```
Smothered Mate
5rk1/6pp/8/4N3/8/8/8/6K1 w - - 0 1
Nf7#
```

```
Queen and King Box Mate
k7/8/1QK5/8/8/8/8/8 w - - 0 1
Qa7#
```