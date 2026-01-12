The user wants me to describe 3 mate-in-1 scenarios for white. Each scenario should be in its own code block with:
1. Name of the scenario
2. FEN notation
3. The winning move for white

Let me think of 3 distinct and valid mate-in-1 puzzles.

**Scenario 1: Back Rank Mate**
A classic back rank mate where the king is trapped by its own pawns.

Setup: Black king on g8, black pawns on f7, g7, h7. White rook on e1 (or a1). White king somewhere safe.

Let me construct this:
- Black king: g8
- Black pawns: f7, g7, h7
- White rook: e1
- White king: g1 (for example)

FEN: 6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1

White plays Re8# - the rook delivers checkmate on the back rank, and the king cannot escape because its own pawns block the squares f7, g7, h7.

Let me verify:
- White rook on e1 goes to e8
- Black king on g8 is in check
- Can the king move? f7 is blocked by pawn, g7 is blocked by pawn, h7 is blocked by pawn
- h8 and f8 are attacked by the rook
- The king has no escape squares and no piece can block or capture the rook
- This is checkmate!

FEN: 6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1
Move: Re8# or in algebraic notation: 1. Re8#

**Scenario 2: Queen and King Mate (Queen Ladder/Support Mate)**
The queen delivers mate supported by another piece, with the enemy king on the edge.


Black king on a8, White queen on b6, White rook on a1. The queen moves to a7 for mate.

Let me verify:
- 1. Qa7#
- Black king on a8 is in check from queen on a7
- Can the king move to b8? The queen on a7 also attacks b8
- Can anything block or capture the queen? If there are no other black pieces, no.

FEN: k7/1Q6/8/8/8/8/R7/6K1 w - - 0 1
Move: Qa7# on a7 delivers check to the king on a8. The king has no escape squares—b8 and b7 are both controlled by the queen. If the king captures the queen with Kxa7, the rook on a1 still gives check along the a-file, so that's not a legal move either. This is checkmate.

For an Arabian Mate pattern, I can set up: Black king on h8, White rook on a8 delivering check along the 8th rank, and White knight on f7 controlling g8 as an escape square.

But the king also needs to be cut off from h7 and g7. The knight on f7 covers h7, so I need to ensure g7 is blocked or controlled as well. Let me reconsider the positioning—perhaps the rook should be on the h-file instead, with the knight positioned to cover multiple escape squares around the cornered king. Let me recalculate the knight's coverage from f7. A knight moves in an L-shape, so from f7 it reaches h8, h6, d8, d6, g5, and e5. That means f7 covers h8 where the king would be trapped, plus h6 to prevent escape in that direction.

If I place the Black king on g8 with a White rook delivering check from h7, the king can't move to f8 without blocking it somehow, and capturing the rook depends on whether it's protected. Let me consider a smothered mate pattern instead—Black king on g8 boxed in by its own pieces on f8 and h8, with a White knight on f7 delivering the final blow.

Actually, a knight on h6 gives check to g8 and controls f7. If Black's own pieces occupy f8, g7, and h8, the king has no escape squares. The knight just needs to reach h6 from somewhere on the board to complete the mate. The knight from e5 delivers checkmate on f7. With the king trapped on h8, it has no escape squares—g8 is blocked by its own rook, while g7 and h7 are occupied by pawns. The knight's L-shaped move from f7 reaches h8, confirming the check with no legal moves available. on f7 attacks h8 where the black king sits, and the king has no escape squares since g8 is blocked by its own rook and both g7 and h7 are occupied by pawns. That's checkmate.

So I have three solid scenarios now: a back rank mate with Re8#, a queen support mate with Qa7#, and this knight mate with Nf7#.

Let me verify the first position though. The rook on e1 delivers mate on e8 against a king on g8 that's hemmed in by pawns on f7, g7, and h7, with the white king safely on g1. - King can't move to h7, g7, or f7 since pawns occupy those squares ✓
- The rook can't be captured and no piece can interpose
- That's checkmate ✓

All three positions work. Let me verify scenario 2 again though—I want to make sure the queen support mate is sound.

For the second scenario with the queen on b6, rook on a1, and Black's king trapped on a8, I need to confirm the FEN is correct and the mating pattern holds up.

Moving the queen to a7 delivers check. The king has no escape since b8 and b7 are both controlled by the queen on a7, and crucially, the rook on a1 guards the queen itself, preventing capture. That's mate.

I've identified three distinct mating patterns here. Let me make sure the position notation is accurate—the rook should be on e1 with the king on g1, which translates to 4R1K1 for the first rank. The move notation also needs verification to ensure it follows standard conventions.

For the mating sequences, I'm checking: Re8# delivers back rank mate, Qa7# is the queen-supported mate, and Nf7# is the smothered mate. I should also verify the knight can actually reach f7 from e5 by calculating its available squares—the knight moves in an L-shape, so from e5 it can go to g6, g4, c6, and other squares depending on the full calculation.

Let me trace through: moving one square horizontally and two vertically gets me to f7, which is valid. From f7, the knight does attack h8, confirming the smothered mate works. All three mating patterns check out. Let me verify the FEN notation for the smothered mate position. Row 8 has a black rook on g8 and black king on h8, which gives 6rk. Row 7 has pawns on g7 and h7 with six empty squares before them, so that's 6pp. The notation checks out correctly.

Now I'm considering more descriptive names for these positions. The first one works well as "Back Rank Mate." For the second scenario, I need something that captures the queen's role with the rook providing support from behind. Options like "Queen and Rook Battery Mate" or "Corridor Mate" come to mind, though I'm not certain which classical terminology applies best here. The key dynamic is the queen delivering mate while the rook prevents escape, so something reflecting that coordination would be appropriate. 's Mate, Max Lange's Mate, Opera Mate, Pillsbury's Mate, Réti's Mate, Suffocation Mate, and Swallow's Tail Mate are all possibilities. I'll select one that works as a straightforward mate-in-1.

Arabian Mate uses a knight and rook working together, where the knight cuts off escape squares while the rook delivers the final blow. The typical setup has the black king on g8 with a white rook positioned on the back rank, though I need to verify the exact piece placement to ensure the mate works correctly.

Let me reconsider the positioning more carefully. The king typically sits in a corner like h8, with the rook moving to deliver check along the 7th rank, and the knight positioned to control the remaining escape squares. A knight on f8 would attack d7, e6, g6, and h7, which could work depending on where the rook moves. So the knight on f8 controls h7, d7, g6, and e6—but not g8, which means the king escapes after Rh7+.

Let me reconsider the position. I need the knight to cover g8 as well. If I place the knight on g6 instead, it would attack h8 directly and potentially control the escape squares the king needs.

Checking the knight moves from g6: it reaches e7, e5, h8, h4, f8, and f4. This covers h8, which is promising, but I need to verify whether this actually prevents the king's escape after Rh7+.

Actually, if the king is already in check from the knight on g6 attacking h8, that's an illegal position to begin with. I need to reconsider the setup.

Let me try a different configuration: place the Black king on g8 instead, position a White rook on h1 ready to deliver check on h8, and put a White knight on e7. From e7, the knight controls g8, g6, f5, d5, c6, and c8—crucially including g8 where the king sits. After Rh8+, the king on g8 is in check. If it moves to f7, the knight on e7 doesn't actually control that square. Moving to g7 is the only option to explore.

But checking the knight's reach from e7: it can't get to g7 either. So the king still has escape squares. I need to add blocking pieces—place pawns on f7 and g7 to eliminate those flight squares. Then after Rh8+, the king can't move to either square, and if it captures the rook on h8, I need something defending it or delivering checkmate.

A knight on g6 would attack h8, preventing the king from taking the rook. The challenge is positioning the knight there without giving check prematurely, since the king is on g8.

Let me construct a position: Black king on g8 with pawns on g7 and f7 to block those escape squares. White has a rook on h1 and a knight on g6. When the rook moves to h8 with check, the king cannot escape to f8 (controlled by the knight), g7 or f7 (blocked by pawns), or capture on h8 (the knight guards it). This creates the illegal position where the king has no legal moves. no valid escape squares since f7 and g7 are blocked by pawns, and both f8 and h8 are controlled by the knight on g6. This is indeed the Arabian Mate pattern.

I now have three distinct mating scenarios to present: the back rank mate, this Arabian mate, and the smothered mate. Each represents a classic, recognizable pattern that demonstrates different tactical themes. is the knight actually giving check? Let me verify what squares a knight on g6 controls. From g6, it can reach e7, e5, f8, h8, f4, and h4—notably not g8 where the king sits. So the position holds up. Looking back at the first rank in the Arabian Mate FEN, I have the king on e1 and rook on h1 positioned correctly.

Let me systematically verify each scenario's FEN notation. For the back rank mate setup, I need to map out the board from rank 8 down to rank 1, accounting for the white king on g1, white rook on e1, black king on g8, and black pawns on f7, g7, and h7.

Continuing through the remaining ranks: ranks 6, 5, 4, 3, and 2 are all empty, giving me three consecutive 8s. On rank 1, I have four empty squares, the rook on e1, one empty square, the king on g1, and one final empty square, which produces 4R1K1. This gives me the complete FEN: 6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1.

For the Arabian mate position, the setup includes a white king on e1, white rook on h1, white knight on g6, black king on g8, and black pawns on f7 and g7. Rank 8 shows six empty squares, the black king, and one empty square (6k1). Rank 7 has five empty squares followed by the two black pawns and one empty square (5pp1).

The knight sits on g6 with six empty squares before it and one after (6N1). Ranks 5 through 2 are completely empty. On rank 1, there are four empty squares, the white king on e1, two empty squares, and the rook on h1 (4K2R). The resulting FEN is 6k1/5pp1/6N1/8/8/8/8/4K2R w - - 0 1.

For the smothered mate scenario, I'm positioning the white king on e1 and white knight on e5 against a black king on h8, black rook on g8, and black pawns on g7 and h7. Rank 8 contains six empty squares, the rook on g8, and the king on h8 (6rk). Rank 7 has six empty squares followed by both pawns (6pp). Rank 6 is empty, and on rank 5, I place the knight on e5 with four empty squares before it and three after (4N3).

The remaining ranks are empty except rank 1, which has four empty squares, the white king on e1, and three empty squares (4K3). This gives the FEN 6rk/6pp/8/4N3/8/8/8/4K3 w - - 0 1.

All three positions convert correctly to FEN notation. The algebraic moves are properly formatted: Re8# for the back rank mate, Rh8# for the rook's checkmate, and Nf7# for the knight's smothered mate pattern.