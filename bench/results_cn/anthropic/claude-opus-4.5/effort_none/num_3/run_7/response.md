<budget:thinking>
I need to come up with 3 distinct mate-in-1 scenarios for white. Let me think through each one carefully.

**Scenario 1: Back Rank Mate**
A classic pattern where a rook or queen delivers checkmate on the back rank when the king is trapped by its own pawns.

Setup: White rook on a1, Black king on e8, Black pawns on f7, g7, h7 blocking escape.
FEN: Let me construct this properly.
- Black king on e8
- Black pawns on f7, g7, h7
- White rook on a1
- White king somewhere safe, say g1

FEN: 4k3/5ppp/8/8/8/8/8/R5K1 w - - 0 1

White plays Ra8# - the rook delivers checkmate on the 8th rank, and the king cannot escape because f7, g7, h7 pawns block f8, g8, h8.

Wait, let me verify: King on e8, rook goes to a8. The king is in check from a8. Can it escape?
- d8? No, attacked by Ra8
- d7? Yes, this is free! 

I need to block d7 too. Let me add a piece or pawn.

Better setup: 
- Black king on g8
- Black pawns on f7, g7, h7
- White rook on a1
- White king on g1

FEN: 6k1/5ppp/8/8/8/8/8/R5K1 w - - 0 1

Ra8# - King on g8, check from a8. Can king escape?
- f8? Attacked by rook on a8
- h8? Attacked by rook on a8
- Kf8, Kh8 both attacked
- King can't go to 7th rank because of own pawns

Yes! This works.

**Scenario 2: Queen and King Mate (Kiss of Death / Support Mate)**

White queen supported by king delivers mate.

Setup:
- Black king on h8
- White king on g6
- White queen on f7

Wait, let me check: Qg7#?
King on h8, Queen goes to g7. King in check.
- Can't take queen (protected by king on g6)
- Can't go to h7 (attacked by queen)
- Can't stay on h8 (in check)

But wait, is this position legal? White king on g6, that's fine. Black king on h8. White to move. The black king isn't currently in check, so white plays Qg7#.

Actually, I need to place the queen somewhere first. Let me set up:
- Black king on h8
- White king on g6  
- White queen on f6

FEN: 7k/8/5QK1/8/8/8/8/8 w - - 0 1

Qf8#? No wait, that doesn't work because the queen would be on f8, checking the king on h8... the king could go to h7.

Let me reconsider. With king on g6 and queen on f6:
Qg7# - King on h8 is in check, can't go to h7 (queen attacks), can't take queen (king protects).

Wait, queen on f6 to g7. Let me verify:
- Queen on g7 attacks h8, h7, g8
- King on g6 supports queen on g7
- Black king on h8 has no escape

Yes! FEN: 7k/8/5QK1/8/8/8/8/8 w - - 0 1
Move: Qg7#

**Scenario 3: Fool's Mate Pattern / Scholar's Mate style**

Let me do a different classic - Arabian Mate or Anastasia's Mate... Actually, let me do a simple queen delivery mate.

Setup:
- Black king on e8 
- White queen on h5
- White bishop on c4 (attacking f7)

Qxf7#? No, that only works if f7 is weak and there's no escape.

Let me think of another pattern - Smothered Mate!

- Black king on g8
- Black rook on f8
- Black rook on h8 (or pawn on h7, g7)
- White knight on f7

Wait, if knight is already on f7, then Nh6+ is discovered... no that's not mate in 1.

Classic smothered mate position:
- Black king on g8
- Black rook on f8
- Pawns on g7, h7
- White knight on e7 (or somewhere to jump to f7 or h7)

Actually, the classic smothered mate is knight on f7 playing Nh6# with king trapped... no wait, it's Nf7 playing to h6 or Ne7 playing to f7... 

Let me set it up:
- Black king on h8
- Black rook on g8
- Black pawn on h7
- White knight on f7

Nf7 is already there. Can it deliver mate? Ng5 doesn't help. Let me reconsider.

The real smothered mate:
- Black king on g8
- Black pieces on f8, g7, h7 surrounding the king
- White knight delivers Nf7# or Nh6#

Position: King g8, Rook f8, Pawns g7, h7. Knight plays from e6 to f8? No, that's capturing the rook.

Correct smothered mate:
King on h8, Rook on g8, pawn on h7. Knight on f7 plays Ng5... no.

Let me try: King on g8, pawns on f7, g7, h7, rook on f8. White knight on e7.
Ne7-f5? Ne7-g6? Ng6 would check the king... King on g8, knight on g6 gives check. King can go to h8 (if not blocked) or f8 is occupied by rook, h7 blocked by pawn, h8 is free!

I need to block h8 too. Let me add a black rook on h8.
King g8, Rook f8, Rook h8, pawns g7 h7. White knight on e7.
Ng6# - but wait, can king take the knight? g8 to g6? No, that's two squares. Can anything block? Nothing can block a knight check.

So: King on g8 in check from Ng6. Escape squares:
- f8: blocked by own rook
- h8: blocked by own rook  
- h7: blocked by own pawn
- f7: needs to check if attacked by knight - knight on g6 attacks f8, h8, e7, e5, f4, h4. It does NOT attack f7.

So the king escapes to f7! This doesn't work.

Let me try again with a queen present:
Position for smothered mate where knight is giving final blow:
- Black king h8
- Black rook g8  
- Black pawn h7
- White knight f7

The knight on f7 attacks h8 and g5 and other squares. Knight on f7 is already checking the king on h8? Let me see: Knight on f7 attacks d8, d6, e5, g5, h6, h8. Yes! So if the knight moves to f7, it would be checkmate if king is on h8 and can't escape.

Setup before the move:
- King h8, Rook g8, Pawn h7
- White knight on e5 (attacks f7, g6, d7, etc.)
- Oh wait, I need the knight to come from somewhere that allows Nf7#

Knight to f7 can come from: d8, d6, e5, g5, h6, h8
From e5: Ne5-f7 is not a valid knight move. Knight on e5 can go to f7? e5 to f7: that's 1 right, 2 up... no wait, e5 to f7 is 2 right, 2 up which isn't a knight move.

Knight moves in L-shape: 2+1 or 1+2.
From f7, knight could have come from: d6, d8, e5, g5, h6, h8.
e5 to f7: e to f is 1 file, 5 to 7 is 2 ranks. That's 1+2 = valid knight move!

So: Knight on e5, plays Nf7#. King on h8, rook on g8, pawn on h7.
Check: King in check from f7. Escape squares:
- g7: blocked by pawn? No wait, I said pawn on h7. g7 is free!

Let me add pawn on g7 too:
King h8, Rook g8, Pawns g7, h7, White knight e5. 
But now can the rook block? Rook is on g8, it can't block a check from f7 to h8.
Escape squares for king:
- g7: blocked by own pawn
- h7: blocked by own pawn
- g8: blocked by own rook

Nf7# is mate!

FEN construction:
- Black king h8: k on h8
- Black rook g8: r on g8
- Black pawns g7, h7: p on g7, p on h7
- White knight e5: N on e5
- White king somewhere: let's say a1

8th rank: .......k = 7k
7th rank: ......pp = 6pp
6th rank: empty = 8
5th rank: ....N... = 4N3
Others empty, white king on a1.

FEN: 7k/6pp/8/4N3/8/8/8/K7 w - - 0 1

Wait, I forgot the rook on g8!
8th rank: ......rk = 6rk
7th rank: ......pp = 6pp

FEN: 6rk/6pp/8/4N3/8/8/8/K7 w - - 0 1

Move: Nf7#

Let me double-check this is valid:
- Knight on e5 moves to f7 (valid L-move: 1 file right, 2 ranks up)
- Knight on f7 attacks h8 where black king sits
- King's escape routes: g8 (rook), h7 (pawn), g7 (pawn) - all blocked
- Nothing can capture the knight on f7
- Nothing can block (can't block knight checks)

This is checkmate!

So my three scenarios:
1. Back Rank Mate: 6k1/5ppp/8/8/8/8/8/R5K1 w - - 0 1, Ra8#
2. Queen Support Mate: 7k/8/5QK1/8/8/8/8/8 w - - 0 1, Qg7#
3. Smothered Mate: 6rk/6pp/8/4N3/8/8/8/K7 w - - 0 1, Nf7#

Wait, I should double-check scenario 2 again.
Queen on f6, King on g6, Black king on h8.
Qg7#: Queen moves from f6 to g7, giving check to king on h8.
- Can king take queen on g7? No, protected by white king on g6.
- Can king escape to h7? No, queen on g7 attacks h7.
- Any other escape? No, king is on the corner.

This is mate!

Actually wait - let me recheck scenario 1 one more time.
Rook on a1, Black king on g8, pawns on f7, g7, h7, White king on g1.
Ra8#: Rook moves to a8, giving check along the 8th rank.
- King on g8, in check from a8
- Can king go to h8? Attacked by rook on a8? Yes, rook on a8 attacks entire 8th rank.
- Can king go to f8? Attacked by rook on a8? Yes.
- Can king go to h7? That square exists and isn't attacked by the rook. But is it blocked? h7 has a pawn!
- Can king go to g7? g7 has a pawn!
- Can king go to f7? f7 has a pawn!

All escape squares are blocked by own pawns or attacked by rook. Checkmate!

All three scenarios verified!
</budget:thinking>

```
Back Rank Mate
6k1/5ppp/8/8/8/8/8/R5K1 w - - 0 1
Ra8#
```

```
Queen Support Mate
7k/8/5QK1/8/8/8/8/8 w - - 0 1
Qg7#
```

```
Smothered Mate
6rk/6pp/8/4N3/8/8/8/K7 w - - 0 1
Nf7#
```