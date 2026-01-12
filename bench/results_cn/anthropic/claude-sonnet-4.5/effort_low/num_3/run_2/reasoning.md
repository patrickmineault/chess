I need to create 3 different mate-in-1 scenarios for White. Each should be:
1. A valid chess position
2. White to move and mate in 1
3. Distinct from each other (different mating patterns)

Let me think of three different scenarios:

Scenario 1: Back rank mate with a rook
- Black king on e8, trapped by its own pieces
- White rook can deliver checkmate on e1 or similar
- Let me construct: Black king on e8, black pawns on f7, g7, h7. White rook on a8.
- Move: Ra8-e8# would be checkmate
- FEN: Let me build this properly
  - Position: king on e8, pawns on f7,g7,h7 for black. White has rook on a8 and king somewhere safe like h1
  - Actually, let me think more carefully. For back rank mate:
  - Black: Ke8, pawns f7,g7,h7
  - White: Ra1, Kg1
  - Move: Ra8#
  - FEN: 4k3/5ppp/8/8/8/8/8/R5K1 w - - 0 1
  - Wait, the rook is on a1, so it could go Ra8#. Let me verify: Black king on e8, if rook goes to a8, is it checkmate? The king is on e8, rook on a8 gives check along the 8th rank. Can the king escape? e7 - is it controlled? No. So this isn't mate.
  
Let me reconsider. For a proper back rank mate:
- Black: Ke8, pawns f7, g7, h7 (blocking escape squares)
- White: Rook that can come to the 8th rank
- But I need to make sure all escape squares are covered

Actually, let's do a simple one:


I'm exploring a corner mate scenario with the rook. The key challenge is trapping the black king completely, ensuring no escape squares are available. I'll need to carefully position the pawns and rook to create a true checkmate situation.

The king's potential escape routes seem complex. Some squares appear blocked, but I need to verify each potential move systematically. The pawn structure and rook placement are critical to preventing any king movement.

I'm exploring different mating scenarios, carefully tracking each possible escape square and checking whether they're truly controlled or blocked. The challenge is ensuring complete king immobilization.

Back rank mate looks promising. With a rook on a8, I've confirmed the king's escape routes are systematically shut down - f8 and h8 controlled, h7, g7, and f7 blocked by pawns. This creates a textbook checkmate configuration.

The key is methodically eliminating every potential king movement through precise piece placement.

For the queen scenario, I'm exploring potential mating positions. The critical challenge is ensuring the queen controls key escape squares while preventing king movement. By carefully positioning the queen and understanding pawn blockades, a decisive checkmate emerges.

In the knight scenario, I'm investigating a classic smothered mate configuration. The key is finding a knight move that traps the king with no escape routes, utilizing surrounding pieces to restrict movement.

I carefully position the pieces to create a precise mating net. By placing the knight on f7, I control critical escape squares around the black king. The pawns on g7 and h7 block potential flight paths, while the rook on f8 prevents alternative king movement.

The strategic placement ensures a decisive checkmate, demonstrating the knight's unique ability to deliver a smothered mate through precise positioning. I verify the first position's FEN notation carefully, checking each rank's composition and confirming the placement matches the expected chess board representation. The notation accurately depicts the board state, with precise piece and empty square encoding.

For the second position, I'll systematically analyze the FEN notation's rank-by-rank breakdown, ensuring each segment correctly represents the board's configuration.

The third position requires a similar methodical verification, tracking piece placements and empty squares across different ranks to validate the chess board's structural integrity.

The white Knight's strategic positioning near the black King suggests a potential tactical opportunity for a decisive move.