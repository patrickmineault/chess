The user wants me to describe 3 mate-in-1 scenarios for white. Each scenario needs:
1. A name
2. FEN notation for the setup
3. The winning move for white

Let me think of 3 distinct mate-in-1 puzzles.

**Scenario 1: Back Rank Mate**
A classic back rank mate where the king is trapped by its own pawns.

Setup: Black king on g8, black pawns on f7, g7, h7. White rook on a1 or e1.
Let me create a valid position:
- Black king: g8
- Black pawns: f7, g7, h7
- White rook: e1
- White king: somewhere safe, say g1

FEN: 6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1
Move: Re8# (Re1-e8 checkmate)

Let me verify: 
- King on g8
- Pawns on f7, g7, h7
- Rook moves to e8, gives check
- King can't go to f8 (rook covers), h8 (rook covers), f7/g7/h7 are blocked by pawns
Yes, this is checkmate.

**Scenario 2: Queen and King Mate (simple)**
Let me think of a scenario with the queen delivering mate.

Setup: Black king on h8, White queen on g6, White king on g1
FEN: 7k/8/6Q1/8/8/8/8/6K1 w - - 0 1
Move: Qg7# or Qg8#

Wait, let me verify Qg7#:
- Queen on g7 gives check
- King on h8 can't escape: g8 is covered by queen, h7 is covered by queen


- That's checkmate.

The queen move to g7 delivers mate since the king has no escape squares—both g8 and h7 fall under the queen's control.

The position breaks down as: black king on h8, white queen on g6, white king on g1. In FEN notation, this reads 7k/8/6Q1/8/8/8/8/6K1 w - - 0 1, and Qg7# ends it.

I'm considering other classic mating patterns now. An Arabian Mate involves coordinating a rook and knight to trap the opposing king.

For a smothered mate, I need the black king boxed in by its own pieces while a white knight delivers the final blow. The typical setup has the king on g8 with friendly pieces blocking escape squares—perhaps a rook on f8 and another on h8, with a pawn on g7. A knight positioned on e7 or f7 could then administer mate, though I need to verify the exact configuration works. The knight on f7 controls h8, so the king has no escape squares—f8 is blocked by the rook, g7 and h7 by pawns. I need to work backwards to find where the knight starts before delivering this mate. The position requires the black king on g8 with pieces sealing off f8, g7, and h7, then a knight move to f7 completes the trap.

A knight on h6 can reach f7 in one move. Setting up the position: black king g8, rook f8, pawns on g7 and h7, white knight on h6, and I need to include a white king. After Nf7#, the black king is checkmated—it cannot escape to any square since the knight controls h8 while the other squares are already occupied or blocked. Rank 1 checks out: a1-f1 empty (6), g1 king (K), h1 empty (1) → 6K1 ✓

The position is 5rk1/6pp/7N/8/8/8/8/6K1 w - - 0 1, and Nf7# delivers checkmate—a classic smothered mate pattern.

I've identified three key checkmate scenarios so far: a back rank mate with Re8#, a queen mate with Qg7#, and I'm working through the third example.

For the queen mate position, I need to verify the coverage. The black king sits on h8, the white queen on g6. After Qg7#, the queen controls both g8 and h7, leaving the king with no escape squares. Queen on g7 covers the entire 7th rank and g-file, plus two diagonals. Along the a1-h8 diagonal, it reaches f6 and h8. Along the other diagonal, it covers f8 and h6. So the king on h8 would be in check from the queen on g7 via the diagonal, and h6 would also be under attack.

From h8, the king can only move to g8, h7, or g7—all controlled by the queen. That's checkmate for scenario 2. from the queen's diagonal attack on h8). That's checkmate.

Let me double-check scenario 1 as well.

Starting position: Black king on g8 with pawns on f7, g7, h7; White rook on e1 and king on g1.

After Re8#, the rook delivers check along the eighth rank. The king cannot escape to f8 or h8 (both controlled by the rook), and its own pawns block f7, g7, and h7. This is also mate.

For scenario 3, I have Black's king on g8, rook on f8, pawns on g7 and h7, White's knight on h6 and king on g1. Playing Nf7 puts the king in check. The knight from f7 controls specific squares around the king.

Let me verify the knight's attack pattern from f7. Moving in L-shapes: two squares vertically or horizontally, then one square perpendicular gives me d8, d6, e5, g5, h8, and h6. I need to check if g8 is actually under attack from this position.

A knight on f7 doesn't reach g8—I made an error there. For a smothered mate to work, the knight needs to deliver check, which means it must occupy a square that attacks the king's position. If the king sits on g8, I need to find which squares a knight can reach to give check: e7 would work, as would other squares following the knight's L-shaped movement pattern. Knight on f7 does give check to a king on h8 since f7 attacks h8. For this to be a smothered mate, the king would need all escape squares (g8, g7, h7) blocked by Black's own pieces—typically a rook on g8, a pawn on g7, and another piece controlling h7. Black bishop or knight on h7, pawn on g7, and White knight positioned on f7. The knight gives check to the king on h8 since it controls that square. The rook on g8 and pawn on g7 block escape routes, but I need a piece on h7 to complete the mating net—perhaps another rook there. Let me verify the position works: king h8, rooks on g8 and h7, pawn g7, with White's knight on f7 delivering mate since all flight squares are covered.

Actually, I should reconsider where the knight came from. If it moved to f7, it could have originated from d6, d8, e5, g5, h6, or h8. Testing h6 as the departure square: a knight there can reach f7, but it wouldn't give check from h6 to a king on h8. So the setup has the knight already on f7 attacking h8, with Black's pieces arranged to block the remaining escape squares.

Let me verify the position works: the king on h8 is in check from the knight on f7, and all escape routes are sealed—g8 has a rook, g7 has a pawn, h7 has another rook. That's checkmate.

For the FEN, I need to map out each rank carefully. Rank 8 has the black rook on g8 and king on h8, so that's 6rk. Rank 7 has a black pawn on g7 and rook on h7, giving 6pr. Rank 6 has the white knight on h6, so 7N. The white king can be placed anywhere safe, like a1.

The complete FEN becomes: 6rk/6pr/7N/8/8/8/8/K7 w - - 0 1

Now I can verify the move Nf7# works: the knight moves from h6 to f7, delivering checkmate to the black king on h8. The king has no escape squares and can't capture the knight or block. After Nf7, the king has no escape—g8, g7, and h7 are all blocked. The knight on f7 delivers checkmate. I should verify the knight can't be captured: the rook on g8 can't reach f7 diagonally, and while the g7 pawn could theoretically take it, that doesn't matter since it's already checkmate. This setup with two pawns instead of two rooks is cleaner. and h6 (diagonal forward for black). The knight on f7 isn't reachable by either pawn, so it's checkmate.

Let me verify with the other pawn: h7 can only capture on g6, so f7 remains untouchable there too.

I'll document a couple of concrete checkmate positions: one with a rook delivering back rank mate (Re8# with the king trapped on g8), and another using a queen to achieve a similar mating pattern.

For the smothered mate example, a knight on f7 delivers mate when the king sits on h8 with pawns blocking escape on g7 and h7. The black king on h8 is blocked by its own rook on g8 and pawns on g7 and h7. A knight move from h6 to f7 delivers checkmate since the king has no escape squares—g8, g7, and h7 are all controlled or occupied by black's own pieces. This is indeed a smothered mate pattern.

I should verify the FEN notation is correct, making sure the piece placement reads from rank 8 down to rank 1 with each rank separated by a forward slash. empty (1) ✓

Move: Qg8# — Queen from g6 to g8, checkmate ✓

I'm verifying the second position's FEN notation and confirming the queen delivers mate on g8. The black king on h8 has no escape squares, and the queen controls all adjacent files and ranks from g8.

For the third position, I need to parse the smothered mate setup: black king trapped on h8 with pawns blocking g7 and h7, a black rook on g8, and my knight positioned on h6 ready to deliver the final blow.

The knight moves to f7, giving checkmate since the king has no escape squares. All three checkmate patterns check out. For the second scenario, I'm reconsidering the name—"Queen Mate" feels too generic. The position features the black king cornered on h8 with the queen delivering mate from g7, which some call the "Kiss of Death." I'll use a more descriptive label that captures this specific mating pattern.

Looking at legality, the back rank mate is a standard endgame that occurs frequently. The queen mate scenario, while simplified with just kings and queen, is a perfectly valid endgame position that could arise in actual play.

For the smothered mate, the material distribution—black king with rook and pawns, white king with knight—is reasonable and the position, though specific, could plausibly develop from a real game. All three positions check out as legal.

I'm confident in these three examples. The names are clear: Back Rank Mate, Queen Corner Mate, and Smothered Mate, which accurately describes the knight checkmate where the king is trapped by its own pieces. g8 is blocked by the rook, and g7/h7 are blocked by pawns, so the king has no escape squares). This confirms the smothered mate works.

All three positions deliver checkmate through different tactical patterns, and each one is sound.