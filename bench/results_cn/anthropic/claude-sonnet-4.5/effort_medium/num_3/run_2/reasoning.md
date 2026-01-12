I need to create 3 different chess positions where White can checkmate Black in one move. Each should be in code fences with:
1. Name of the scenario
2. FEN notation
3. The winning move

Let me think of 3 distinct mate-in-1 scenarios:

1. **Back Rank Mate with Rook**
   - Black king on e8, trapped by its own pieces on f7, g7, h7
   - White rook can move to e1 or d8 for checkmate
   - FEN: Let me construct this carefully
   - Position: Black king on e8, black pawns on f7, g7, h7, White rook on e1 or nearby
   - FEN: 4k3/5ppp/8/8/8/8/8/4R3 w - - 0 1
   - Move: Re8# (but wait, let me verify - king on e8, rook moves to e8? No, that's occupied. Let me reconsider)
   
   Let me try again:
   - Black king on e8, pawns on f7, g7, h7
   - White rook on a8 can deliver mate
   - FEN: 4k3/5ppp/8/8/8/8/8/R7 w - - 0 1
   - Move: Ra8# (No wait, the rook is already on a8. It should move TO a8 or e1)
   
   Actually, let me be more careful:
   - Black king on e8, black pawns on f7, g7, h7 blocking escape
   - White rook on e1
   - Move: Re8 would be checkmate? No, Re1-e8 means moving the rook from e1 to e8, but e8 is occupied by the king.
   
   Let me reconsider the whole position:
   I'm analyzing the king's potential escape routes carefully. The key is blocking all possible squares while positioning the rook to deliver a decisive blow. I need to ensure the king has no way to move, creating a perfect back-rank mate scenario.

   The rook on e8 creates a devastating checkmate. By attacking critical squares and preventing any king movement, the trap is complete. The pawns strategically block potential escape paths, leaving the king with no options.

2. **Queen and King Mate**
   I realize the initial king placement was incorrect. Positioning the white king on f7 and queen on f6 enables a precise checkmate. Moving the queen to g7 traps the black king, with no legal escape squares available.

3. **Knight Mate**
   A rare but powerful checkmate scenario involving a knight begins to take shape, focusing on the king's vulnerable position. I see a knight's strategic positioning to trap the black king. The knight's L-shaped movement creates a critical confinement, blocking potential escape routes. By controlling key squares around the king's position, the knight sets up a potential checkmate scenario. The rook's placement on the h-file further restricts the king's mobility, creating a tight defensive net that limits black's options. I see the knight's path to deliver a smothered mate. From e5, the knight can precisely jump to f7, attacking the h8 square and creating a checkmate scenario. The king is trapped by its own pieces, with no escape squares available.

The board configuration confirms the mating move, with the black king hemmed in by its rook and pawns. The knight's strategic positioning enables the decisive strike.

I verify the king's escape routes are systematically blocked. The knight's attack squares create a precise containment, leaving no avenue for the king's survival.

Exploring potential piece configurations, I recognize the challenge of creating a perfect smothered mate setup. The positioning requires careful coordination between pieces to trap the king completely.

The classic smothered mate demands precise placement: king cornered, surrounding pieces blocking potential escape routes, and a knight delivering the final checkmate strike.

I'm carefully mapping out each square's potential, noting how rook and pawn placement can strategically limit the king's movement. The goal is finding that precise arrangement where the king becomes utterly immobilized.

The FEN notation reveals intricate square positioning, with empty and occupied spaces creating a complex chess landscape. Tracking each file's configuration becomes crucial for understanding potential checkmate scenarios.

I want the king precisely positioned on h8, not g8. The knight's strategic move to f7 creates an inescapable trap, blocking all potential king movements and delivering a definitive checkmate.

I'll verify three classic checkmate scenarios, each demonstrating a unique mating pattern that exploits the king's restricted mobility and vulnerability.

Checking the first FEN's structure reveals precise placement: king on g8, pawns on f7-h7, white rook positioned strategically on e1, enabling a decisive back rank checkmate. The board configuration supports a clean, tactical execution.

The second scenario shows a queen delivering a conclusive mate, with the white king controlling key squares and preventing escape. The positioning suggests a precise, controlled checkmate mechanism.

The third position presents an intriguing tactical setup with a knight on g5 and a lone pawn on h7, creating potential mating threats against the black king trapped on h8.

The knight's move to f7 delivers a decisive check, completely immobilizing the king with no escape squares or defensive options. By attacking critical surrounding squares and blocking potential flight paths, the knight executes a precise checkmate.