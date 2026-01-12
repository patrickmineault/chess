<budget:thinking>
I need to describe 3 distinct mate-in-1 scenarios for white. Let me think through some classic checkmate patterns.

**Scenario 1: Back Rank Mate**
A classic pattern where the king is trapped on the back rank by its own pawns.

Setup: White has a rook, black king is on g8 with pawns on f7, g7, h7 blocking escape.
FEN: Let me construct this...
- Black king on g8
- Black pawns on f7, g7, h7
- White rook on e1 (or a1)
- White king somewhere safe, say g1

FEN: 6k1/5ppp/8/8/8/8/8/R5K1 w - - 0 1

White plays Ra8# - the rook delivers checkmate on the back rank.

Let me verify:
- Black king on g8
- Pawns on f7, g7, h7 block f8, g7, h8
- Ra8 attacks g8, king cannot escape to f8 (blocked by f7 pawn's control? No wait, f8 is a square the king could go to but Ra8 doesn't control f8...

Let me reconsider. For back rank mate:
- King on g8
- Pawns on f7, g7, h7
- Rook goes to a8 or e8 or d8, etc.

If rook is on e1 and plays Re8#:
- King is on g8
- Re8 attacks the 8th rank
- King can't go to f8 (not attacked, but wait... Re8 attacks e8, f8, g8, h8 along the rank? No, the rook on e8 attacks along the 8th rank and the e-file.
- From g8, king could go to f8, h8, f7, g7, h7
- f7, g7, h7 are blocked by own pawns
- f8 - is this attacked by Re8? Yes, the rook on e8 attacks f8
- h8 - is this attacked by Re8? Yes, the rook on e8 attacks h8

So Re8# works. Let me set up the FEN:
6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1

- 6k1 = 6 empty squares, black king, 1 empty square on rank 8
- 5ppp = 5 empty squares, then pawns on f7, g7, h7
- 8/8/8/8 = empty ranks 6,5,4,3
- 8 = empty rank 2
- 4R1K1 = 4 empty, Rook on e1, 1 empty, King on g1, 1 empty

Actually let me recount: 4R1K1
e1 is the 5th file, so a1-d1 is 4 squares, then R on e1, then f1 empty (1), then K on g1, then h1 empty (1).
4 + R + 1 + K + 1 = positions a1,b1,c1,d1 (4 empty), e1 (R), f1 (1 empty), g1 (K), h1 (1 empty). That's 8 squares, correct.

Move: Re8#

**Scenario 2: Scholar's Mate style / Queen and Bishop mate**
Let me think of a simple queen mate.

How about queen delivering mate with support:
Black king on h8, white queen can go to h7 or g8 with support.

FEN: Let's say black king on e8, white queen on d1, white bishop on b5 giving check... no that's not mate in 1.

Let me think of a simpler one. 

**Smothered Mate:**
King is surrounded by own pieces and knight delivers mate.

Classic position:
- Black king on g8
- Black rook on f8
- Black pawns on g7, h7 (or pieces there)
- White knight can jump to f7 giving mate? No, that's not quite right.

Smothered mate: Kg8, Rh8, Rf8 (or N on h8), pawns on g7, h7
Knight on f7 doesn't give mate... 

Actually the classic smothered mate:
- Black king on h8
- Black rook on g8
- Black pawn on h7, g7
- White knight goes to f7... no that doesn't work either.

The real smothered mate position:
- Kg8, Rg7 (or pawn), something on h8, something on f8
- Knight delivers mate from h6 or f6? No...

Let me think again. Knight on f7 attacks g8, h8, e8, d8, d6, e5, h6, g5.
If king is on g8:
- Knight on f7 attacks g8 (check) but king can go to h8, f8, h7, g7...

For smothered mate, typically:
- King on g8
- Own pieces on f8, g7, h7 (or h8)
- Knight on f7 or h6? 

Nf7 check to Kg8 - king can go to h8
If there's a piece on h8, then Nf7 is mate? Let's see:
- Kg8, piece on h8, piece on g7, piece on f8
- Nf7# attacks g8 (where king is) and h8 (blocked), and king can't go to f8 (blocked), g7 (blocked), h7 (controlled by knight? No, Nf7 controls e5,g5,h6,d6,h8,d8,e8... not h7).

Hmm, this is getting complicated. Let me try Nh6 instead:
Knight on h6 attacks g8, f7, f5, g4.
If Kg8, pawn on g7, piece on f8, pawn on h7:
- Nh6+ attacks g8
- Kf8 blocked by piece
- Kg7? blocked by pawn
- Kh8? is h8 attacked by Nh6? No. So king escapes to h8.

Let me try a different approach. Classic smothered mate:
Position after Qg8+ Rxg8, Nf7#
- King on h8 (forced there)
- Rook on g8 (just captured queen)
- Knight goes to f7

Wait, I need the position BEFORE the mate:
- Kh8
- Rg8 (black rook)
- Knight on e5 or h6 ready to go to f7

Nf7# from where? Knight on h6 can go to f7? No, h6 to f7 is not a valid knight move.
Knight moves in L-shape: 2+1 or 1+2.
From h6: g8, f7, f5, g4, e5, e7 (wait let me recalculate)
h6 -> (h±1, 6±2) or (h±2, 6±1)
h6 -> g8, g4 (h-1, 6±2) 
h6 -> f7, f5 (h-2, 6±1)
Also h6 -> i-files don't exist.
So from h6, knight can go to g8, g4, f7, f5.

So yes! Knight on h6 can go to f7.

Let's set up: Kh8, Rook on g8, Knight on h6 plays Nf7#
- King on h8
- Rook on g8 blocks g8 and prevents Kg8, Kg7 (rook doesn't prevent Kg7, the rook on g8 just occupies g8)

Hmm wait, for this to be mate:
- Kh8, threatened by Nf7
- Kg8 - blocked by own rook
- Kg7 - is this blocked or attacked? Need something there.
- Kh7 - is this attacked? Nf7 doesn't attack h7. Need something.

So we need more pieces. Let's say:
- Kh8
- Rg8 (blocks Kg8)
- Pawn on g7 (blocks Kg7)
- Pawn on h7 (blocks Kh7)
- White knight on h6, plays Nf7#

FEN: 6rk/6pp/7N/8/8/8/8/6K1 w - - 0 1

Let me verify:
- Rank 8: 6 empty, rook on g8, king on h8 → 6rk ✓
- Rank 7: 6 empty, pawns on g7 and h7 → 6pp ✓
- Rank 6: 7 empty, knight on h6 → 7N ✓
- Ranks 5-2: empty → 8/8/8/8 ✓
- Rank 1: 6 empty, king on g1, 1 empty → 6K1 ✓

Move Nf7#:
- Knight attacks h8 where king is ✓
- Kg8 blocked by rook ✓
- Kg7 blocked by pawn ✓ 
- Kh7 blocked by pawn ✓
This is mate! ✓

**Scenario 3: Simple Queen Mate**

Let me do a simple one where the queen delivers mate against a king on the edge.

King on h8, queen on g6, can play Qg8# if g8 and h7 are covered.

Actually, let's do: King in the corner at a8, Queen can deliver mate.

Setup:
- Black king on a8
- White queen on a1, plays Qa7# (need to make sure b8 and b7 are covered)

Or simpler:
- Black king on h1
- White queen on g3
- Queen plays Qg1#? King can go to h2.

Let me try:
- Black king on e8
- White queen on e1
- Supporting pieces...

Actually, let's do the classic:
- Black king on f8 or somewhere
- White queen delivers mate with king support

How about:
- Black king on h8
- White queen on f6
- White king on f8? No that's not possible (kings can't be adjacent to enemy king)

Let me try:
- Black king on h8
- White queen on g7 is already checkmate? Let's see: Qg7 attacks h8, g8, h7, h6, f8, f6, etc. King on h8 cannot go to g8 (Qg7), h7 (Qg7), g7 (Qg7). But can it go anywhere else? From h8, king can go to g8, h7, g7. All attacked by Qg7. So Qg7 is already checkmate if we're in this position.

So I need the queen NOT on g7 yet. Let's say:
- Black king on h8
- White queen on g1, plays Qg7#? But then black has other moves...

No wait, I need to ensure the king truly has no escapes. Let's carefully construct:

Position:
- Black king on h8
- White queen on f6
- White pawn on g7

Is Qf6 to where giving mate? Qf8#? Let's check:
- Qf8+ attacks h8 along the 8th rank
- Kg7 blocked by white pawn
- Kh7 - is h7 attacked? Qf8 attacks h8 and f-file and diagonals. Qf8's diagonals: a3-f8-h6 and c5-f8-e7-d6 etc. h7 is not on these. So Kh7 escapes.

Let me try another setup:

- Black king on e8
- White queen on d6
- Black has no pieces to block

Qd8#? Or Qe7#?
- Qe7#: attacks e8, so it's check. King from e8 can go to d8, f8, d7, f7. Qe7 attacks d8? No. e7 attacks d8? Let me see. Qe7 attacks: e-file, 7th rank, diagonals a3-e7-h4 (nope, wrong diagonal), let me reconsider. Qe7 diagonals: a3-b4-c5-d6-e7-f8-g8..wait no. e7 diagonals: d8-e7-f6-g5-h4 and b4-c5-d6-e7-f8.

So Qe7 attacks d8 and f8 via diagonals. Also attacks d7, e7, f7 on the 7th rank. So from e8:
- d8 attacked by Qe7 ✓
- f8 attacked by Qe7 ✓
- d7 attacked by Qe7 ✓
- f7 attacked by Qe7 ✓

What about e7? The king can't go to e7 because the queen is there.

So Qe7 is checkmate against Ke8 if the queen can get there! But we need the queen to not already be on e7. Let me set up:

- Black king on e8
- White queen on e1 (or somewhere she can reach e7)

FEN: 4k3/8/8/8/8/8/8/4Q1K1 w - - 0 1

Hmm wait, queen on e1 to e7 - can she do that in one move? Yes, along the e-file.

But is it actually mate? Let me re-examine Ke8 with Qe7:
- Qe7+ is check
- Kd8: attacked by Qe7 (diagonal d8-e7) ✓
- Kf8: attacked by Qe7 (diagonal e7-f8) ✓
- Kd7: attacked by Qe7 (7th rank) ✓
- Kf7: attacked by Qe7 (7th rank) ✓

Yes, that's checkmate!

FEN: 4k3/8/8/8/8/8/8/4Q1K1 w - - 0 1
Move: Qe7#

Let me double-check the FEN:
- Rank 8: 4 empty (a8-d8), king on e8, 3 empty (f8-h8) → 4k3 ✓
- Ranks 7-2: all empty → 8/8/8/8/8/8 ✓
- Rank 1: 4 empty (a1-d1), queen on e1, 1 empty (f1), king on g1, 1 empty (h1) → 4Q1K1 ✓

So my three scenarios:

1. Back Rank Mate - 6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1, Re8#
2. Smothered Mate - 6rk/6pp/7N/8/8/8/8/6K1 w - - 0 1, Nf7#
3. Queen Mate - 4k3/8/8/8/8/8/8/4Q1K1 w - - 0 1, Qe7#

Actually wait, scenario 3 seems too simple. Let me double-check there's no issue.

The position 4k3/8/8/8/8/8/8/4Q1K1:
- Black has only a king on e8
- White has queen on e1, king on g1

Move Qe7#:
- Queen moves from e1 to e7, giving check
- Black king on e8 is in check
- Possible moves for black king: d8, d7, f7, f8 (not e7 - queen there)
- d8: controlled by Qe7 (diagonal)
- d7: controlled by Qe7 (rank)
- f7: controlled by Qe7 (rank)
- f8: controlled by Qe7 (diagonal)
- All squares blocked or attacked. Checkmate! ✓

All three scenarios verified!

Wait, I want to reconsider the smothered mate more carefully.

Position: 6rk/6pp/7N/8/8/8/8/6K1

That's:
- a8-f8 empty (6), g8 black rook (r), h8 black king (k)
- a7-f7 empty (6), g7 black pawn (p), h7 black pawn (p)
- a6-g6 empty (7), h6 white knight (N)
- Ranks 5-2 empty
- a1-f1 empty (6), g1 white king (K), h1 empty (1)

Move Nf7#:
- Knight moves from h6 to f7
- Is h6 to f7 valid? From h6, knight can go to g8, g4, f7, f5. Yes, f7 is valid.
- Nf7+ gives check because... wait, does Nf7 attack h8? Let me check.
- From f7, knight attacks: e5, g5, h6, h8, d6, d8, e9(invalid), g9(invalid)
- Yes! Nf7 attacks h8. ✓
- Black king on h8, in check from Nf7
- Possible moves: g8, g7, h7 (can't go to f7 - knight there)
- g8: occupied by black rook ✓ (blocked)
- g7: occupied by black pawn ✓ (blocked)
- h7: occupied by black pawn ✓ (blocked)
- Checkmate! ✓

Great, all three are valid!

One more check on scenario 1:

Position: 6k1/5ppp/8/8/8/8/8/4R1K1
- Rank 8: a8-f8 empty (6), g8 black king (k), h8 empty (1)
- Rank 7: a7-e7 empty (5), f7 pawn (p), g7 pawn (p), h7 pawn (p)
- Ranks 6-2: empty
- Rank 1: a1-d1 empty (4), e1 white rook (R), f1 empty (1), g1 white king (K), h1 empty (1)

Move Re8#:
- Rook from e1 to e8
- Re8+ gives check (rook attacks along 8th rank, including g8)
- Black king on g8, in check
- Possible moves: f8, h8, f7, g7, h7
- f8: attacked by Re8 (along 8th rank) ✓
- h8: attacked by Re8 (along 8th rank) ✓
- f7: occupied by black pawn ✓ (blocked)
- g7: occupied by black pawn ✓ (blocked)
- h7: occupied by black pawn ✓ (blocked)
- Checkmate! ✓

All scenarios verified.

Hmm, let me reconsider: in the smothered mate, it's traditionally called smothered mate because the king is "smothered" by its own pieces and the knight delivers the final blow. My scenario has the king on h8 surrounded by its own rook and pawns, with a knight delivering mate from f7. This fits the definition.

However, I realize I should double-check my FEN notation is correct.

FEN format: [piece placement] [active color] [castling] [en passant] [halfmove] [fullmove]

1. 6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1
   - Piece placement from rank 8 to rank 1, correct.
   - w = white to move, correct.
   - - = no castling available (simplified), acceptable.
   - - = no en passant, correct.
   - 0 1 = halfmove and fullmove clocks, acceptable.

2. 6rk/6pp/7N/8/8/8/8/6K1 w - - 0 1
   - Same format, correct.

3. 4k3/8/8/8/8/8/8/4Q1K1 w - - 0 1
   - Same format, correct.

All good! Let me present the final answer.

Oh wait, I realize for scenario 3, this might be considered trivial or "helpmate-like" since Black has no pieces at all. Let me consider a slightly more realistic position while still being simple.

Alternative Scenario 3: Anastasia's Mate or something similar

Let me think of another common mate pattern:

**Arabian Mate**: Rook and knight cooperate.
- King in corner, rook on adjacent file, knight supports.

Position:
- Black king on h8
- White rook on h1 (or h-file)
- White knight on f7

Wait, Rf1 to Rh1? Let me set up:
- Black king h8
- White rook on h2, moves to h8? No, that's not one move checkmate, that's just capturing or the king isn't in check yet.

Let me reconsider. For Rook + Knight mate (Arabian mate):
- King on h8
- Rook delivers check on h-file, knight covers escape squares

Position:
- Kh8
- Rook on a8, delivering check? Ra8+ - king can go to g7, h7, g8...
  We need knight to cover those.
- Knight on f7: covers h8, g5, e5, d6, d8, e9(no), h6. Doesn't cover g7 or g8.

Hmm, this is getting complicated. Let me try:
- Kh8
- Rook on h1, plays Rh7+? No wait, Rh7 doesn't attack h8.
- Rook on h3, plays Rh8#? That works if g8, g7, h7 are blocked/attacked.

Setup:
- Kh8
- Nf7 covers h8 (wait, does it? From f7: d8, e5, g5, h6, h8, d6. Yes, h8!)
- Actually no. The knight on f7 attacks h8, but we want the ROOK to deliver mate, with the knight supporting.

Standard Arabian mate:
- Kh8
- Rook on h1 plays Rh1-h7? No.
- Rook on a8 plays Ra8#? For this, g8, h7, g7 need to be covered.

Alright, let me look this up mentally:
- Arabian Mate: Knight on f6 (or f7?), Rook on h-file.
- King on g8, Rook on h8 is mate with knight on f6 because:
  - Rh8# attacks g8
  - Kf7 is attacked by Nf6
  - Kh7 is attacked by Rh8
  - Kf8 is attacked by Nf6? Let me check. Nf6 attacks: d7, e8, g8, h7, h5, g4, e4, d5. 
  - Kf8 is not attacked by Nf6. Hmm.

Let me try again:
- Kg8
- Nf6 attacks e8, d7, h7, g8, h5, g4, d5, e4
- So Nf6 attacks g8 (giving check) and h7 (blocking escape)
- If rook is on h8, Rh8#:
  - Rh8 attacks g8 (check!)
  - Kf7 - attacked by Nf6? f7 is not in knight's range from f6.
  - Kh7 - attacked by Rh8? Yes, Rh8 attacks h7.
  - Kf8 - attacked? Not by Nf6 or Rh8 directly. Rh8 attacks along h-file and 8th rank. f8 is on 8th rank! So yes.

Actually wait, let me re-examine. If rook is currently NOT on h8 and we play Rh8#:
- Rh8+ attacks along h-file and 8th rank.
- 8th rank: a8, b8, c8, d8, e8, f8, g8, h8
- h-file: h1-h8
- So Rh8 attacks f8, g8 (directly, on 8th rank) and h7, h6, etc (on h-file).
- Kg8 is in check.
- Kf8 attacked by Rh8? Yes (8th rank).
- Kf7 attacked by Nf6? No, Nf6 doesn't attack f7.

So this isn't actually mate because Kf7 escapes. Arabian mate must have something else.

Let me look for a different pattern. I'll just use a supported queen mate which is more straightforward.

**Simple Queen + King mate:**
- Kc6 (white)
- Qa8 (white, can move to a7)
- Ka8 (black)

No wait, that doesn't work. Let me think...

- Black king on a1
- White queen on b3
- White king on c1 (supporting but also blocking a2? No, king on c1 doesn't block anything from a1)

Hmm, let me try:
- Black king on a1
- White queen on c1 (giving check along the 1st rank and diagonal)
- Qc1+ - king can go to a2, b2. Not mate.

Let me try:
- Black king on h1
- White queen on h3
- White king on g3 (or f2)

Qh3 to Qh2#? 
- Qh2+ attacks h1
- Kg1 - is it blocked? Need something on g1 or attacking g1.

Ugh, this is getting complicated. Let me just go with my original scenario 3 which is valid (queen smothering the king against the edge), or choose another simple pattern.

**Fool's Mate (almost):** Not applicable as white delivers mate.

**Simple pawn promotion mate?** Too complex.

Let me just do a **Support Mate** where the queen is supported by a piece:

- Black king on h8
- White queen on g7 (delivering mate)
- For this to be a "mate in 1", queen must not be on g7 yet.

Position:
- Kh8 (black)
- Qg1 (white), plays Qg7#
- But we need Qg7 to be protected (otherwise black... well black doesn't have pieces, so it doesn't matter)

If black has no other pieces:
- Kh8, Qg1 (white), Kg1 or wherever white king is
- Qg7#: attacks h8, g8, h7. King cannot escape to g8, h7, g7. Checkmate!

Wait, from h8, king can go to g8, h7, g7 only. If Qg7 is there:
- g8: attacked by Qg7 ✓
- h7: attacked by Qg7 ✓
- g7: occupied by Qg7 ✓
Checkmate!

FEN: 7k/8/8/8/8/8/8/6QK w - - 0 1
Move: Qg7#

Let me verify FEN:
- Rank 8: 7 empty, k on h8 → 7k ✓
- Ranks 7-2: empty → 8/8/8/8/8/8 ✓
- Rank 1: 6 empty (a1-f1), Q on g1, K on h1 → 6QK ✓

Move Qg7#:
- Q moves from g1 to g7 (valid move along g-file)
- Qg7 attacks h8 (diagonal), giving check
- Kh8 cannot move: g8 (attacked by Qg7), h7 (attacked by Qg7), g7 (occupied by Q)
- Checkmate! ✓

Actually, let me re-examine. Qg7 attacks h8? 
- g7 to h8 is diagonal (one square diagonally). Yes, queen attacks diagonally. ✓

OK so this works. But it's basically the same as my original scenario 3, just with the queen on a different square.

Let me keep my original three or swap scenario 3 to this new one. Actually, let me verify my original scenario 3 once more:

Original Scenario 3: 4k3/8/8/8/8/8/8/4Q1K1 w - - 0 1, Qe7#
- Ke8 (black king)
- Qe1, Kg1 (white)
- Qe7# attacks e8 via e-file

Wait, Qe7 attacks e8? Let me check. Queen on e7 attacks along e-file (e1-e8), 7th rank, and diagonals. The e-file from e7 goes to e8, e6, e5, etc. So yes, Qe7 attacks e8. ✓

Both scenarios work! I'll keep my original three.

Final Answer:
1. Back Rank Mate: 6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1, Re8#
2. Smothered Mate: 6rk/6pp/7N/8/8/8/8/6K1 w - - 0 1, Nf7#
3. Queen Corridor Mate: 4k3/8/8/8/8/8/8/4Q1K1 w - - 0 1, Qe7#

Actually, "Queen Corridor Mate" isn't a standard name. Let me call it "Queen Smother" or "Epaulette Mate"? No, Epaulette mate is different (king is blocked by own pieces on both sides with queen giving mate). 

Let me call it "Queen Staircase Mate" or just "Queen Mate". Or better yet, "Queen Invasion Mate" or "Queen Domination". 

Actually, I'll just call it "Queen Domination" - where the queen single-handedly covers all escape squares due to the king being on the edge.

Hmm, even simpler, I'll call it "Kiss of Death" (queen adjacent to king delivering mate) or "Queen Kiss Mate"? No, that's not standard either.

Let me just call it "Queen and King Mate" since it's the basic endgame checkmate pattern.

Or actually, thinking about it more - this is sometimes called "Corridor Mate" when the queen traps the king along a corridor (rank, file, or diagonal). Since the king is on e8 and the queen on e7 controls d8, f8, d7, f7 (all exits), it's a form of corridor mate.

I'll call it "Corridor Mate".

Final scenarios:
1. Back Rank Mate
2. Smothered Mate
3. Corridor Mate

All three are distinct and classic patterns!
</budget:thinking>

```
Back Rank Mate
6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1
Re8#
```

```
Smothered Mate
6rk/6pp/7N/8/8/8/8/6K1 w - - 0 1
Nf7#
```

```
Corridor Mate
4k3/8/8/8/8/8/8/4Q1K1 w - - 0 1
Qe7#
```