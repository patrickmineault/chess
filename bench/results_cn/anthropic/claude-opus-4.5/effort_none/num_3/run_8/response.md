<budget:thinking>
I need to come up with 3 distinct mate-in-1 scenarios for white. Let me think through each one carefully.

**Scenario 1: Back Rank Mate**
A classic back rank mate where a rook or queen delivers checkmate on the 8th rank while the king is trapped by its own pawns.

Setup: White has a rook, Black king is on g8 with pawns on f7, g7, h7 blocking escape.
- White Rook on a1, can move to a8 for mate
- Black King on g8, pawns on f7, g7, h7
- Need a white king somewhere safe

FEN: 6k1/5ppp/8/8/8/8/8/R3K3 w Q - 0 1

Wait, let me verify: White rook on a1, white king on e1. Black king on g8, pawns on f7, g7, h7.
Move: Ra8# - The rook goes to a8, the king can't escape because f7, g7, h7 pawns block f8, g7 is blocked, h8 is covered by the rook.

Actually let me reconsider - Ra8+ and king is on g8. The rook on a8 attacks the 8th rank. King on g8 can't go to f8 (rook covers it), can't go to h8 (rook covers it), can't go to h7 (pawn there), can't go to g7 (pawn there), can't go to f7 (pawn there). That's checkmate!

FEN: 6k1/5ppp/8/8/8/8/8/R3K3 w - - 0 1

**Scenario 2: Queen and King Mate (Kiss of Death)**
Queen delivers mate supported by the king.

Setup: Black king on h8, White queen can go to g7 or h7 for mate, supported by white king.
- White King on f7, White Queen on d7
- Black King on h8

Let me think: King on f7, Queen on d7. Queen can move to g7 for mate?
Qg7: King on h8, queen on g7. King can't go anywhere - g8 is covered by queen, h7 is covered by queen. Is g7 protected? Yes by king on f7. That's mate!

FEN: 7k/3Q1K2/8/8/8/8/8/8 w - - 0 1
Move: Qg7#

**Scenario 3: Fool's Mate Pattern / Scholar's Mate style**
Let me do a classic smothered mate or something different.

Smothered Mate:
Black king on g8, surrounded by pieces on f8, g7, h8. White knight delivers mate from f7 or h7.

Setup: Black king g8, black rook f8, black rook h8, black pawn g7. White knight on f7 would give check but king could take... need knight protected or coming from elsewhere.

Knight on e5, can jump to f7 for mate if f7 delivers check and king is trapped.
Actually for smothered mate, knight on f7 isn't check to g8... knight on h7 isn't either.

Classic smothered mate: King g8, pieces on f8, f7, g7, h7, h8. Knight delivers from f7? No, knight on f7 doesn't attack g8.

Knight attacks from: If king is on g8, knight checking from e7, f6, or h6.

Let me set up: Black king g8, black queen f8 (or rook), black rook h8, black pawns f7, g7, h7. White knight comes to f6 or e7 or h6.

Nf6 is double check if there's also a discovered piece? No, let me keep it simple.

If knight goes to e7: Knight on e7 attacks g8? Knights on e7 attack: d5, f5, c6, g6, c8, g8. Yes! g8 is attacked.

Setup: King g8, pieces blocking all squares. Pawns on f7, g7, h7. Something on f8. 
Ne7#: King can't move to f8 (need something there), h8 (need to block), g7/f7/h7 blocked by pawns.

FEN: 5rk1/4Nppp/8/8/8/8/8/4K3 w - - 0 1

Knight on e7, check to king on g8. King can't go to:
- f8: rook there
- h8: is h8 covered? Knight on e7 attacks g8, g6, f5, d5, c6, c8. h8 is not attacked by knight. Need something else.

Let me add a piece. White queen or rook on the h-file.

FEN: 5rk1/4Nppp/8/8/8/8/8/4K2R w - - 0 1

Ne7+? Wait, knight is already on e7. I need the knight to MOVE to e7.

Let me redo: Knight on c6 or g6 or c8 or d5 or f5.

FEN: 5rk1/5ppp/8/3N4/8/8/8/4K2R w - - 0 1

Nf6+? Knight on d5 to f6. Does knight on f6 attack g8? Knight on f6 attacks: e4, g4, d5, h5, d7, h7, e8, g8. Yes!

King on g8, knight checks from f6. King can't go to:
- h8: Rook on h1 covers h8? Rook on h1 covers h-file, so h8 is covered.
- f8: Rook there
- h7: Pawn there
- g7: Pawn there  
- f7: Pawn there

That's mate! Nf6#

FEN: 5rk1/5ppp/8/3N4/8/8/8/4K2R w - - 0 1
Move: Nf6#

Wait, I should double-check. After Nf6+:
- The knight is on f6, giving check to the king on g8
- Kh8 is illegal because the rook on h1 controls h8
- Kf8 is illegal because there's a rook on f8
- Kh7 is illegal because there's a pawn on h7
- Kg7 is illegal because there's a pawn on g7
- Kf7 is illegal because there's a pawn on f7

Yes, that's checkmate!

Let me try a third different pattern. How about a simple queen mate or bishop mate?

**Scenario 3: Anastasia's Mate or simple diagonal mate**

Let me do a bishop and rook mate or a queen sacrifice leading to mate.

Simple one: Opera Game style back rank but different from #1.

How about: Queen sacrifices, then back rank mate? No, that's 2 moves.

Let me do: White queen delivers mate on h7 (or similar) with king trapped.

Black king on g8, pawn on h7 and f7. White queen can come to h7 to mate but h7 has a pawn... 

Black king on h8, pawns on g7, h7 (wait h7 and king on h8 doesn't work).

Let me try: Black king h8, pawn g7. White queen comes to h7? No pawn there.

King h8, pawn g7, pawn f7. Queen to h7 - but what protects h7? Need a supporting piece.

Actually simpler - Queen to h6 or h7 depending on position.

FEN: 7k/5ppQ/8/8/8/8/8/4K3 w - - 0 1

Nope, queen already on h7. Let me have queen elsewhere:

FEN: 7k/5pp1/8/7Q/8/8/8/4K3 w - - 0 1

Queen on h5. Can queen go to h7 or h8?
Qh8# - but is h8 next to king on h8? That doesn't make sense. King is on h8, queen can't go to h8.

Qh7 - is that mate? King on h8, queen on h7. King can go to g8. Not mate.

Let me add a piece. King h8, if I put a piece on g8, then Qh7 might be mate.
Or control g8 with another piece.

FEN: 6Bk/5pp1/7Q/8/8/8/8/4K3 w - - 0 1

Queen on h6. Bishop on g8. King on h8. But wait, king can't be on h8 if bishop is on g8 (that would be check or illegal).

Let me reconsider:

FEN: 7k/5ppB/7Q/8/8/8/8/4K3 w - - 0 1

Queen on h6, bishop on h7, king on h8. That's not right either - bishop on h7 is already checking or blocking.

New approach:
FEN: 7k/5pp1/7Q/8/8/8/8/4KB2 w - - 0 1

Bishop on f1, queen on h6, king on h8. Qg7#? Queen to g7, but wait there's a pawn on g7.

Hmm let me just do a different classic mate.

**Scholar's Mate setup (not the full game, just the mate-in-1 position):**

FEN: r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 0 1

This isn't quite mate in 1. Qxf7 is mate? Let's check: Queen takes f7, check. King can't take queen (bishop covers f7). King can't go to e7 (queen covers). King can't go to d8 or other squares... actually Ke7 might not be covered by queen on f7. Queen on f7 attacks e6, g6, e8, g8, f8, f6, and along the f-file and 7th rank. e7 is not directly attacked by queen on f7. But wait, is e7 covered by the bishop on c4? No, bishop is on c4 which is light squared.

Hmm, Qxf7 isn't mate because Ke7 is possible.

Let me think of another setup. 

Actually, let me just do three clean, distinct mates:

**1. Back Rank Mate with Rook**
```
Back Rank Mate
6k1/5ppp/8/8/8/8/8/4K2R w - - 0 1
Rh8#
```
Wait let me verify: White rook h1, white king e1. Black king g8, black pawns f7, g7, h7.
Rh8#: Rook to h8, check. King on g8 can't go to h8 (rook), can't go to f8 (rook covers), can't go to h7 (pawn), g7 (pawn), f7 (pawn). Checkmate!

**2. Queen and Bishop Mate**
FEN: 6k1/5ppp/8/8/1Q6/5B2/8/4K3 w - - 0 1

Queen on b4, bishop on f3. Queen to g7? Qg7#. But pawn on g7.

Let me try: Diagonal mate with queen supported by bishop.

FEN: 6k1/5p1p/6p1/8/8/5B2/6Q1/4K3 w - - 0 1

Queen on g2, bishop on f3. Qb7? No. Qg7? No pawn on g7. Wait I moved the g7 pawn to g6.

Hmm, this is getting complicated. Let me just do standard mates.

**Scenario 2: Arabian Mate**
Rook and knight mate. Rook on the edge, knight covers escape squares.

FEN: 7k/7R/5N2/8/8/8/8/4K3 w - - 0 1

Rook on h7, knight on f6, king on h8.
Is this already mate? Let's see: Rook on h7 attacks h8 (where king is)... wait, that means black king is in check. This isn't a mate-in-1, it's already checkmate or an illegal position.

Let me fix: Rook not giving check yet.

FEN: 7k/8/5N1R/8/8/8/8/4K3 w - - 0 1

Rook on h6, knight on f6, black king on h8.
Move Rh7#? Rook to h7, check. King on h8 can go to g8? Knight on f6 covers g8. Can king go anywhere else? h7 has rook, g8 has knight covering. What about Kh8-h7? No, rook is on h7. It's check from h7. g8 is covered by knight. That's mate!

Wait, Rh7# doesn't work because king is on h8, rook comes to h7, king can still... no wait, the only squares king could go are g8 (covered by knight) and "off the board". That's mate!

Actually wait - I need to double-check the knight coverage. Knight on f6 attacks: e4, g4, d5, h5, d7, h7, e8, g8. Yes, g8 is covered. Rh7 is checkmate.

**Scenario 3: Simple Queen Mate**

FEN: 7k/8/5K2/8/8/8/8/7Q w - - 0 1

White queen h1, white king f6, black king h8.
Queen can go to h7#? Queen on h7, king on h8. King can go to g8? Is g8 covered? King on f6 covers e5, e6, e7, f5, f7, g5, g6, g7. g8 is not covered by king on f6. And queen on h7 doesn't cover g8 either (queen on h7 attacks g7, g8, h8, h6, etc. - wait, does queen on h7 attack g8? Diagonally from h7, the queen attacks g8, f5, etc. Yes! h7 to g8 is diagonal.).

So Qh7#: King on h8, queen on h7. King can't go to g8 (queen covers diagonally). Can't go anywhere else. That's mate!

But actually I realize the position I wrote has the queen on h1 and it would be Qh7#. Let me double-check this is a legal position and the move works.

FEN: 7k/8/5K2/8/8/8/8/7Q w - - 0 1
- Black king h8
- White king f6
- White queen h1

Move: Qh7#
- Queen moves from h1 to h7 (along h-file), giving check
- Black king on h8 cannot move to g8 (queen covers g8 diagonally)
- Black king cannot move to g7 (queen covers g7)
- Checkmate!

Great, this works.

Let me compile my three scenarios:

1. **Back Rank Mate**
FEN: 6k1/5ppp/8/8/8/8/8/4K2R w - - 0 1
Move: Rh8#

2. **Arabian Mate**
FEN: 7k/8/5N1R/8/8/8/8/4K3 w - - 0 1
Move: Rh7#

3. **Queen Mate (King and Queen)**
FEN: 7k/8/5K2/8/8/8/8/7Q w - - 0 1
Move: Qh7#

Let me verify each one more time:

1. Back Rank Mate:
Position: White Ke1, Rh1. Black Kg8, pawns f7, g7, h7.
Move: Rh8#
Check: Rook to h8 gives check. King on g8 can't go to h8 (rook), f8 (rook covers), h7 (pawn), g7 (pawn), f7 (pawn). ✓

2. Arabian Mate:
Position: White Ke1, Rh6, Nf6. Black Kh8.
Move: Rh7#
Check: Rook to h7 gives check. King on h8 can only try g8, which is covered by knight on f6. ✓

3. Queen Mate:
Position: White Kf6, Qh1. Black Kh8.
Move: Qh7#
Check: Queen to h7 gives check. King on h8 can't go to g8 (queen covers diagonally), g7 (queen covers). ✓

All three are valid and distinct!
</budget:thinking>

```
Back Rank Mate
6k1/5ppp/8/8/8/8/8/4K2R w - - 0 1
Rh8#
```

```
Arabian Mate
7k/8/5N1R/8/8/8/8/4K3 w - - 0 1
Rh7#
```

```
Queen and King Mate
7k/8/5K2/8/8/8/8/7Q w - - 0 1
Qh7#
```