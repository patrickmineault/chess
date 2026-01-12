I need to create 3 different chess positions where White can checkmate Black in one move. Each should be in a code block with:
1. Name of the scenario
2. FEN notation
3. The winning move

Let me think of three distinct mate-in-1 scenarios:

Scenario 1: Back Rank Mate
- Black king on e8, trapped by its own pawns on f7, g7, h7
- White rook can deliver checkmate on e1 moving to e8
- FEN notation needs to represent this

Let me construct a simple back rank mate:
- Black king on e8
- Black pawns on f7, g7, h7
- White rook on e1
- White king somewhere safe, like g1

FEN: 4k3/5ppp/8/8/8/8/8/4R1K1 w - - 0 1
Winning move: Re8#

Scenario 2: Queen and King Mate
- Black king in the corner, say h8
- White queen can deliver checkmate
- Let's say Black king on h8, White queen on g6, White king on f6
- Queen to g7 or h7 would be checkmate

FEN: 7k/8/5KQ1/8/8/8/8/8 w - - 0 1
Winning move: Qg7#

Scenario 3: Knight checkmate
- Let's have a smothered mate scenario
- Black king on h8, blocked by own pieces
- White knight can deliver mate
- Black king h8, black rook h7, black pawns g7
- White knight on f7 giving check, or knight can move to f7

Actually, let me make it simpler - knight on e6 can go to f8 or g7:
Black king h8, black rook g8, black pawn h7, g7
White knight e6


FEN: 6rk/6pp/4N3/8/8/8/8/6K1 w - - 0 1

I'm struggling to find the precise knight checkmate. The positioning is tricky, with the knight needing to attack critical squares while the king is trapped. I'll need to carefully map out the escape routes and blocking pieces to create a valid smothered mate scenario.

The knight's movement requires precise calculation to control the king's potential escape paths. I'll continue analyzing the board's configuration to identify the winning move.

Exploring knight placement on f7 and g6 reveals critical attack squares that restrict the black king's mobility. These positions create checkmate opportunities by controlling key escape routes.

Analyzing knight movement from e5 to g6, I verify the move's validity and check potential king escape paths. The knight's attack squares and pawn blockades determine checkmate potential.

Careful examination shows the king can potentially escape to g8, preventing an immediate checkmate. Strategic positioning requires blocking all potential king movements.

Confirming the checkmate involves verifying each escape route: h7 blocked by pawn, g8 blocked by rook, g7 blocked by pawn. No defensive options remain for the black king.

Ng6# represents the decisive winning move, trapping the king with no legal escape squares. I'm exploring a back rank mate scenario with precise positional analysis. The white rook on d1 can move to d8, delivering checkmate when the black king is on g8. The surrounding pawns block potential escape squares, and the rook's control doesn't fully restrict the king's movement to f8 or h8. This reveals a nuanced tactical challenge in executing the back rank mate. I analyze the back rank checkmate scenario. The rook on d8 checks the king, while the queen on h6 strategically controls critical escape squares. The king cannot flee to h8 due to the queen's control. However, the f8 square remains potentially open, complicating the mate's execution.

In the simplified scenario, the rook's potential checkmate depends on blocking pieces. If a black piece occupies h7, the rook can capture it, delivering a decisive blow. The king's limited mobility on the back rank becomes the critical factor in determining checkmate possibilities.

The white rook strategically positions itself to control key squares, preventing the black king's escape. By analyzing potential movement paths, the rook's ability to threaten and potentially capture blocking pieces becomes evident.

The checkmate is confirmed through precise positioning, eliminating all possible king movements and leaving no defensive options for the black king.

Rook Mate scenario validates the strategic capture, blocking escape routes and ensuring the king's complete immobilization. The white rook's calculated move prevents any potential counterplay, decisively ending the game.

The knight's positioning creates a tactical trap, restricting the king's mobility and setting up an unavoidable checkmate sequence. A true smothered mate requires the king to be completely surrounded by its own pieces, with a knight delivering the decisive check. This scenario differs slightly from the classic definition, as not all squares are blocked.

The key characteristic is the king's extreme confinement, preventing any escape while a knight executes the final blow. Precise piece positioning creates an impenetrable trap. I verify the FEN notation, focusing on the precise placement of pieces on rank 8. The black rook sits on g8, with the black king positioned on h8, while positions a8 through f8 remain empty. This configuration ensures accurate piece positioning for the chess board state.

The rank 7 contains a black bishop on h7, with all other squares empty. I'll continue analyzing the board's remaining details systematically. I notice the queen is unprotected on g8, which means the black king can capture it. This breaks the checkmate assumption. I need a strategy to prevent the king from capturing the queen, such as adding a protective white piece near g8 or positioning the queen so the king cannot reach it directly.

The current scenario requires rethinking the checkmate configuration to ensure the black king cannot escape or capture the attacking piece. I see a checkmate configuration with the rook on g2 strategically protecting g8, preventing the black king's escape. The queen delivers a decisive check on g8, blocked by pawns on both potential escape squares. The rook's protection makes capturing the queen impossible. All potential king movements are neutralized, confirming a definitive checkmate.

In the second scenario, the rook's capture on h7 initially seems promising but lacks protection. The unguarded rook allows the king to potentially counterattack, invalidating the checkmate attempt. Strategic positioning of supporting pieces becomes crucial to secure a successful mating move.

Exploring alternative checkmate patterns reveals challenges with pawn blockades and king positioning. Each attempted configuration encounters specific obstacles preventing a clean checkmate sequence.

The search continues for a precise rook or queen mating configuration that eliminates the king's escape routes and ensures piece safety. I see a classic back rank checkmate scenario. The white rook moves to a8, delivering an inescapable check. Black's king is hemmed in by its own pawns on f7, g7, and h7, with no legal escape squares. The rook controls the entire eighth rank, blocking all potential king movements. This precise positioning creates a definitive mate in one move.

The queen and knight scenarios follow similar strategic principles of restricting the king's movement through precise piece placement and control of key squares.

I verify the knight's move from e5 to g6, confirming it's a legal L-shaped knight move. The knight's new position attacks critical squares and delivers a decisive check to the black king, with all potential escape routes blocked by black's own pieces.

The checkmate is precise and leaves no room for the king to evade capture. I verify the knight's move to g6 creates a definitive checkmate. The king has no escape routes: g8 blocked by rook, g7 blocked by pawn, h7 blocked by another pawn. The rook cannot capture the knight due to the g7 pawn's interference. Black's pawn lacks a diagonal capture path to the knight. With no alternative defensive moves, the position confirms a conclusive checkmate.

The three scenarios demonstrate distinct mating patterns using a rook, queen, and knight, each exploiting unique positional constraints to deliver a swift, decisive victory.