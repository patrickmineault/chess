The user wants me to describe 3 mate-in-1 scenarios for white. Each scenario needs:
1. A name
2. FEN notation for the setup
3. The winning move for white

Let me think of 3 distinct and valid mate-in-1 puzzles.

**Scenario 1: Back Rank Mate**
This is a classic pattern where a rook or queen delivers checkmate on the back rank when the king is trapped by its own pawns.

Setup: Black king on g8, pawns on f7, g7, h7 (trapping the king). White rook on e1.
FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1

Wait, let me make sure this is correct. The king is on g8, pawns on f7, g7, h7. White rook on e1, white king on h1.

If white plays Re8+, the black king cannot escape because of the pawns. That's checkmate!

Let me verify: 6k1/5ppp/8/8/8/8/8/4R2K
- 6k1 = 6 empty squares, black king, 1 empty square (rank 8)
- 5ppp = 5 empty squares, 3 black pawns (rank 7)
- Rest are empty except last rank
- 4R2K = 4 empty, white Rook, 2 empty, white King (rank 1)

Re8# - Rook to e8 is checkmate. Actually, let me recalculate. Re1-e8 is checkmate because the king on g8 cannot move:
- f8, g8, h8 are covered by the rook on e8
- f7, g7, h7 are blocked by black's own pawns

Wait, the king is ON g8, so f8 and h8 would be the escape squares. 

The rook on e8 controls the entire 8th rank, cutting off f8 and h8. Since the pawns block f7, g7, and h7, the king has no legal moves. Re8# is mate.

**Scenario 2: Queen and King Mate**
A simple setup where the queen delivers checkmate with support from the white king.

Black king on h8, White queen on g6, White king on g1.
FEN: 7k/8/6Q1/8/8/8/8/6K1 w - - 0 1

White plays Qg7#. The queen on g7 gives check, and h8 is the only square the king could move to, but h7 is controlled by the queen, leaving the king with no escape.

**Scenario 3: Smothered Mate**
A knight delivers checkmate while the enemy king is boxed in by its own pieces.

Black king on g8, black rook on f8, black pawns on g7 and h7. White knight on h6.
FEN: 5rk1/6pp/7N/8/8/8/8/6K1 w - - 0 1

Nf7# is mate. The knight gives check from f7, and the king cannot escape—f8 is blocked by the rook, g7 and h7 are blocked by pawns, and h8 is controlled by the knight. The knight on f7 gives check to the king on h8, and all escape squares are covered: g8 is blocked by the rook, g7 and h7 are blocked by pawns, and h8 itself is attacked by the knight. No piece can capture the knight or block, so this is checkmate.

For a proper "mate in 1" puzzle, I need to position the knight where it can deliver this checkmate in one move. Placing the knight on e5 allows Nf7# to be the winning move, with the black king trapped on h8 by its own pieces on g8, g7, and h7. The FEN notation checks out across all ranks. The rook on e1 can deliver mate on e8, controlling the escape squares while the black pawns on f7, g7, and h7 trap their own king.

For the second scenario, the queen on d4 moving to d8 gives check along the entire eighth rank. The king on h8 cannot escape to g8 (also attacked by the queen on d8) or to g7 and h7 (blocked by its own pawns), confirming checkmate.

The smothered mate with the knight on e5 moving to f7 works because the black king on h8 is boxed in by its own rook on g8 and pawns on g7 and h7—the knight delivers the final blow with no escape squares available. The king on h8 is completely trapped—surrounded by its own pieces on g8, g7, and h7 with no escape squares. When the knight lands on f7, it delivers checkmate since the king can't move anywhere and no piece can block or capture the knight.

Let me verify the notation is correct: Nf7# for the knight move, Re8# for the rook, and Qd8# for the queen. These three scenarios cover distinct mating patterns—back rank mate, queen mate with pawn support, and smothered mate—using different pieces and positions. I'm satisfied with this selection. The king's escape is blocked by its own pieces, which is the key to the pattern. Let me think through a concrete example: Black king on c8 with a rook on d8 and pawn on d7 blocking escape squares. If I place a White bishop on a6, it delivers check along the long diagonal. The second bishop needs to control the remaining flight squares—placing it on f4 or another square to cut off those routes. The mate occurs because the king has no legal moves; it's trapped by its own pieces and attacked by the bishops on the two intersecting diagonals. on b8?

- Black king: c8
- Black rook: d8
- Black knight: b8
- Black pawn: d7, b7

Now Ba6#:
- King c8 in check
- b8: blocked by own knight
- d8: blocked by own rook
- b7: blocked by own pawn
- d7: blocked by own pawn
- c7: I need to verify if the bishop on a6 controls this square. The bishop sits on the a6-c8 diagonal, which includes b7, but c7 isn't on that diagonal. On the other diagonal from a6, the bishop controls b5, c4, d3, e2, f1. So c7 appears to be undefended—the king could escape there.

This means Ba6 alone doesn't deliver mate. I'd need another piece controlling c7. A bishop on e5 would attack both c7 and b8, covering those escape squares. With Be5 already placed and Ba6 delivered as the move, the king on c8 would have no legal moves: b8 and c7 are controlled by the e5 bishop, b7 is controlled by the a6 bishop, and d8 and d7 are blocked by Black's own pieces.

For a mate-in-1, I can position the bishop on b5 so it delivers checkmate by moving to a6. The position would have Black's king on c8, rook on d8, and a pawn on d7, with White's bishops on b5 and e5, and the White king placed safely away from the action.

The FEN notation 2kr4/3p4/8/1B2B3/8/8/8/6K1 w - - 0 1 sets this up correctly: the back rank shows the Black king and rook in the right squares, the pawn sits on d7, both White bishops are positioned to control escape squares, and the White king is tucked away on g1.

The move Ba6# delivers checkmate. The bishop move from b5 to a6 puts the Black king in check, and I need to verify all escape routes are sealed: b8 falls to the e5 bishop's diagonal control, b7 is directly attacked by the bishop now on a6, c7 is covered by the e5 bishop, while d7 is blocked by Black's own pawn and d8 by the rook. No Black piece can capture on a6 or interpose, confirming the mate.

This is actually Boden's Mate—a classic pattern with two bishops controlling criss-crossing diagonals. I'll use this instead of my original scenario 2, giving me three distinct checkmate patterns: Back Rank Mate with a rook, Boden's Mate with the two bishops, and Smothered Mate with a knight.

Let me verify the Boden's Mate position works correctly. The king on c8 has escape squares at b8 and b7 before the move, but after Ba6#, both squares are controlled by the bishops and the king is checkmated.

I should also confirm the FEN position is valid and that moving the bishop from b5 doesn't create any unintended consequences. Since no pieces are blocked behind it, the move is sound. d be illegal or mean it's already over).

Scenario 1: Black king on g8 isn't in check from the rook on e1. ✓

Scenario 2: The bishops on b5 and e5 don't attack c8 where the black king sits. ✓

Scenario 3: The knight on e5 can't reach h8 where the black king is positioned. ✓

All three positions have the black king safe initially, then face checkmate in one move. Let me verify the Boden's mate setup more carefully—the king on c8 with a rook on d8 and pawn on d7 leaves escape squares covered: b8 and c7 are controlled by Be5, while b7 will be guarded by Ba6 after the move. The king has nowhere to go.