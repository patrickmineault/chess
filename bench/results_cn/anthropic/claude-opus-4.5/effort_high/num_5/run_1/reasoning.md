The user wants me to describe 5 mate-in-1 scenarios for white. Each scenario needs:
1. A name
2. FEN notation for the setup
3. The winning move for white

Let me think of 5 distinct mate-in-1 patterns:

1. **Back Rank Mate** - A classic pattern where the rook or queen delivers checkmate on the back rank because the king is trapped by its own pawns.

Let me set up a position:
- Black king on g8, pawns on f7, g7, h7
- White rook on e1, can move to e8 for mate

FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1
Move: Re8#

Wait, let me verify: Black king on g8, pawns on f7, g7, h7. White rook on e1, White king on h1.
If Re8+, the king can't escape (blocked by pawns), can anything block? No. Is e8 protected by anything? No. So Re8#. ✓

2. **Scholar's Mate / Queen + Bishop Mate** - Queen delivers mate supported by bishop

Position: Black king on e8, White queen on h5 can go to f7, White bishop on c4 supports f7
- Let's say: Black king e8, some pieces around
- White: Queen on h5, Bishop on c4

FEN: r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 0 1
Wait, this is complicated. Let me simplify.

Actually, for a mate-in-1, I need the position right before the mating move.

Let me reconsider:
FEN: r1bqkb1r/pppp1Qpp/2n2n2/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQkq - 0 1


No wait, that's after the move. Let me set up a simpler position.

Black king on e8, pawn on f7, White queen can go to f7 with support from bishop on c4. I need to verify if Qf7 is actually mate—the king on e8 would be in check from the queen, and the bishop on c4 protects it. The king can't move to d8, e7, or f8 because those squares are either controlled or blocked. Nothing can capture the queen or block, so this works.

FEN: rnbqkbnr/pppp1ppp/8/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 0 1
Move: Qf7#

Actually, let me reconsider—d8 isn't controlled, so the king escapes there. I need a different setup where d8 is also covered. Let me try positioning the queen on f3 first, then capturing on f7 with the bishop already supporting.

FEN: rnbqkbnr/ppppp1pp/8/8/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 0 1

If Qxf7#, the queen attacks e7 but d8 remains open for the king to escape. I need to block that escape square too.

Let me explore actual mate patterns instead. Back rank mate is straightforward—a rook on the 8th rank delivers mate when the king is trapped by its own pawns. With the king on g8 and pawns on f7, g7, h7, Ra8# works because the king can't move to f7, g7, or h7 (blocked by pawns), and f8 and h8 are both controlled by the rook.

FEN: 6k1/5ppp/8/8/8/8/8/R6K w - - 0 1
Move: Ra8#

For Anastasia's mate, I need a knight and rook working together. If the king is on h7 with a pawn on g7, a knight on e7 controls both g6 and g8, cutting off escape squares. The rook then delivers mate on the h-file. With the knight controlling g6 and g8, the king on h7 has nowhere to go when the rook moves to h8. The king can't be left undefended on the back rank—if the rook lands on h8, Black just captures it. I need the knight on e7 controlling the escape squares while another piece delivers the final blow. In the standard pattern, the Black king sits on h7 with its own pawn on g7 blocking retreat, the knight controls g8 and g6, and then a queen or rook finishes on the h-file. Let me test a position: queen on h5, knight on e7, Black king on h8 with pawns on f7, g7, h7. Taking on f7 doesn't lead anywhere, so I should reconsider the piece placement entirely.

A cleaner setup might be queen on a1, knight still on e7, with the Black king on g8 and pawns blocking f7, g7, h7. If the queen moves to a8 with check, the king has nowhere to go—h7 is blocked by its pawn, f7 is occupied, h8 is controlled by the queen, and f8 is where the rook sits.

But wait, Re8 can block the check, so that's not mate. I need a different approach.

For a smothered mate pattern, the king needs to be completely boxed in by its own pieces. The knight would deliver the final blow from a square like f7 or h6, but I need to verify the king actually has no escape squares with this particular piece arrangement. on f7 or g6 to deliver check. For mate, the king must have no escape squares.

With the Black king trapped on h8 by its own rook on g8 and pawns on g7 and h7, a knight move to f7 would give check. The king can't move to g8 (occupied by rook), h7 (occupied by pawn), or g7 (occupied by pawn)—that's checkmate. Qh6 is mate. The king on h8 has no escape squares—g8 and g7 are controlled by the White king on g6, and h7 is blocked by its own pawn. The queen on h7 delivers checkmate. The Black king on h8 has no escape: g8 is controlled by the queen, and h7 itself is defended by the White king on g6, so the king cannot capture the queen.

Now considering a position with bishop support. I'll set up the Black king on h8 with a pawn on g7, place a White bishop on b2 along the long diagonal, and position the queen to deliver mate on g7.

FEN: 7k/6p1/8/8/8/8/1B6/6QK w - - 0 1

The queen captures on g7 with check. The king cannot recapture because the bishop on b2 controls that square along the diagonal. This is checkmate.

For the back rank scenario, the rook moves to a8 delivering mate. The black king on g8 has no escape squares—f7, g7, and h7 are all blocked by pawns, leaving no legal moves.

Now I need to verify these are truly distinct patterns. I have back rank mate with the rook controlling the 8th rank, smothered mate using a knight with the king boxed in by its own pieces, queen and king working together, and queen with bishop support. That's only four solid patterns, so I should add a fifth that's genuinely different. An Arabian mate using rook and knight coordination would work well as a distinct combination.

Let me construct this: placing the knight on f6 and rook on the h-file to trap the Black king on h8. With Rh1-h1 giving check, the king has no escape—g8 and g7 are both controlled by the knight on f6, and h7 is covered by the rook.

Wait, I need to verify the knight's attack squares from f6. A knight there reaches d5, d7, e4, e8, g4, g8, h5, and h7—but not g7. That means Kg7 would be a legal escape, so this isn't mate yet. attack g7.

For Arabian mate, the standard pattern places the knight on f6 with the rook delivering mate from h7. Let me construct this position:
FEN: 7k/7R/5N2/8/8/8/8/6K1 w - - 0 1

But this puts the rook already on h7, which gives check to the king on h8 along the file—making the position invalid since Black would already be in check. I need to set up the position so the rook can move to h7 for mate instead. Let me place the rook elsewhere initially and have it move to deliver the final blow.

With the rook on h2, knight on f6, and Black's king on h8, the move Rh7# works because the knight controls both escape squares. The king cannot capture on h7 since the knight defends it, and cannot flee to g8 since the knight covers that square as well. The king has no legal moves and is in check—that's mate. - Kg7: Rook controls that square
- Kh7: Rook occupies it, and the knight covers it as well

This confirms the Arabian Mate pattern. The rook move from h2 to h7 delivers checkmate, with all escape squares covered by either the rook or knight.

Now I'm compiling the five checkmate patterns with their positions and moves. For the fourth scenario with the bishop on b2 and queen on g1, I should verify whether the queen can actually capture on g7 given the piece placement and whether this truly delivers mate with the bishop's support.

The queen takes the pawn on g7, checking the king on h8. The king cannot recapture since the bishop controls g7, and both g8 and h7 are covered by the queen's adjacent squares. The white king's position on h1 doesn't interfere with this pattern. The position checks out as mate. 5-2: empty
Rank 1: 7 empty, Q (queen h1)

After Qh7#, the black king on h8 is checkmated. The king cannot move to g8 since the queen controls that square, cannot capture on h7 because the white king on g6 defends it, and has no other escape squares along the edge of the board with g7 blocked by both pieces.

For the smothered mate position, I need to verify the FEN setup with the rook on g8 and king on h8.

Knight from h6 can reach f7 via a valid (−2, +1) move. From there, the knight on f7 attacks h8 directly, delivering check to the trapped king. The knight on f7 gives check to the king on h8. If the king captures with Kxf7, I need to verify whether f7 is defended. It's not—so the king can simply take the knight, which means this isn't actually a smothered mate position. For a true smothered mate, the king must be unable to capture the checking piece. The king on h8 and knight on f7 are separated by two files and one rank, making them non-adjacent squares, so the king cannot reach the knight anyway—but since nothing defends f7, the king can still capture it.

Wait, I'm confusing myself. Let me reconsider: the king can only move to adjacent squares (g8, g7, h7), and all three are blocked by Black's own pieces. The knight on f7 is giving check from a square the king cannot reach. That's the smothered mate—the king is trapped by its own pieces and cannot escape or capture the knight.

Now I should verify the first position once more. The rook moves from a1 to a8, delivering check along the 8th rank to the king on g8. The king's escape squares—f8, f7, and h8—are either controlled by the rook or blocked by pawns, leaving no legal moves. All five patterns are distinct - back rank mate with the rook trapping the king against pawns, a smothered mate using the knight with the king boxed in by its own pieces, queen and king working together, queen supported by a bishop, and finally a rook-knight combination. Each demonstrates a different mating mechanism.

Now I should verify the FEN strings are properly formatted. For mate-in-1 puzzles, I'm using simplified FENs with just the position and white to move indicator. Checking the syntax: the piece placements look correct with rank notation, the active color is set to "w", and I'm omitting unnecessary fields since these are straightforward positions. 6: 5+N+2 = 8 ✓; Ranks 5-2: 8 each ✓; Rank 1: 7+R+K = 8 ✓

Each position checks out—all ranks sum to exactly 8 squares. The piece placements are valid across all five positions. 4. Queen and Bishop Diagonal Mate
5. Arabian Mate

These are all standard chess terminology. Let me verify the FEN for #5 one more time: 7k/8/5N2/8/8/8/7R/6K1 w - - 0 1. Rank 8 has the black king on h8, rank 6 has the knight on f6, rank 2 has the rook on h2, and rank 1 has the white king on g1—all positions check out correctly.

The winning move is Rh7#. After the rook moves to h7, the black king is in check and has no escape: g8 is controlled by the knight on f6, g7 is attacked by the rook on the same rank, and h7 itself is defended by the knight. This confirms mate.

To verify the knight coverage, I'm checking its attack squares from f6 using coordinate offsets. The knight reaches g8 and h7 among other squares, which are exactly the critical escape squares needed to seal the checkmate.

The knight on f6 successfully guards h7, confirming that Kxh7 is illegal and the smothered mate pattern holds.

3. King and Queen Mate
   FEN: 7k/8/6K1/8/8/8/8/7Q w - - 0 1
   Move: Qh7#

4. Queen and Bishop Mate
   FEN: 7k/6p1/8/8/8/8/1B6/6QK w - - 0 1
   Move: Qxg7#

5. Arabian Mate
   FEN: 7k/8/5N2/8/8/8/7R/6K1 w - - 0 1
   Move: Rh7#