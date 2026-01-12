I need to create 5 different mate-in-1 scenarios for white. Each should be:
1. A valid chess position in FEN notation
2. Have white to move
3. Have exactly one move that delivers checkmate
4. Be distinct from each other (different types of checkmates)

Let me think of different types of mate-in-1 patterns:

1. Back rank mate with a rook
2. Queen and knight mate
3. Bishop and queen mate
4. Pawn promotion checkmate
5. Knight checkmate

Let me construct these:

**Scenario 1: Back Rank Mate**
- Black king on e8, trapped by its own pawns on f7, g7, h7
- White rook can deliver mate on e1 moving to e8
- FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1
Actually, let me make sure the king is trapped: black king on g8, pawns on f7, g7, h7
- FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1
- Move: Re8#

Wait, let me verify this FEN is correct. The black king is on g8 (position 7 on rank 8, counting from a8). Let me recount:
Rank 8: 6 empty squares (a8-f8), then k on g8, then 1 empty (h8) = "6k1"
Rank 7: 5 empty squares (a7-e7), then pawns on f7, g7, h7 = "5ppp"
Ranks 6-3: all empty = "8/8/8/8"
Rank 2: all empty = "8"
Rank 1: 4 empty (a1-d1), R on e1, 2 empty (f1-g1), K on h1 = "4R2K"


Rook delivers checkmate by moving to e8, trapping the king with its own pawns.

Queen on h1 creates a checkmate scenario. The black king is completely blocked by pawns on g7 and h7, with no escape routes. Queen controls g8, preventing any potential king movement. Confirmed mate with Qh1#. The king cannot escape to g8 or h7 due to the white pawn's control, and staying on h8 is impossible. This results in checkmate.

**Scenario 3: Knight Checkmate**
I'm analyzing a knight's potential to deliver mate with the black king on a corner. The knight on f2 might deliver mate by moving to g3. From h1, the king could potentially move to g1, g2, or h2. I'll examine the knight's control of those squares.

The knight's position on g3 strategically limits the king's escape routes, blocking critical squares and creating a potential mating opportunity.

I'm exploring a smothered mate scenario with precise piece positioning. The knight's mobility allows multiple potential checkmate paths, carefully controlling key escape squares around the trapped king.

The knight on f7 delivers a definitive checkmate. No defensive piece can capture or block the knight's check. The rook and pawns are strategically positioned to restrict the king's movement, creating an inescapable trap.

I'm now considering a pawn promotion scenario, examining whether advancing the white pawn to f8 and promoting could create a decisive checkmate.

If f8=Q+, the queen's powerful control prevents the king's escape. Key squares like f7, g7, and g8 are dominated. The king's potential flight paths are critically limited, suggesting a potential mating position.

With a rook promotion, the situation requires careful analysis of the rook's control over critical squares and the king's potential escape routes. I see the king is trapped. The queen's move to e8 creates a critical checkmate scenario. With the queen controlling key squares and blocking escape routes, the black king has no legal moves. The surrounding pawns and queen's positioning eliminate potential flight squares, ensuring a decisive checkmate.

The strategic placement prevents the king from finding any safe retreat, demonstrating precise coordination between the queen's attacking power and the restrictive pawn structure. I analyze the queen's potential checkmate. The queen on d8 checks the king on g8, blocking escape routes. Pawns on f7, g7, h7 prevent king movement. The bishop on g6 initially seems blocked by the g7 pawn, limiting its control of key squares. This positioning requires careful examination of diagonal control and potential mating patterns.

The queen's placement on d8 creates a critical control zone. By covering g8 and h8, combined with the bishop's influence, the king faces severe movement restrictions. Pawns further constrain potential escape paths, suggesting a decisive mating configuration. I analyze the diagonals carefully. The bishop's control doesn't extend to g7, leaving a potential escape square. I recognize I need additional piece coverage for this square. Adding a pawn on g6 strategically blocks the king's movement, creating a more confined space for potential checkmate.

The queen on d8 delivers a decisive check. The black king finds itself trapped: f8 and h8 are controlled by the queen, f7 is blocked by the bishop, g7 is controlled by the white pawn, and h7 is occupied. Checkmate is confirmed.

Move: Qd8#

. The FEN confirms the board state, with precise placement of pieces revealing the inescapable trap for the black king.

I verify each potential checkmate move systematically, ensuring one-move solutions exist. Promotion and direct piece attacks both qualify as valid checkmate strategies.

The board configuration leaves the black king with no escape routes, making these mate-in-1 scenarios definitive. I verify the checkmate by analyzing the king's escape routes. The rook on e8 controls critical squares, blocking the black king's potential moves. Surrounded by pawns and the rook's control, the king has no legal escape. This confirms a decisive checkmate.

The strategic positioning of white's rook and the black pawns creates an impenetrable barrier, leaving the black king completely trapped. I analyze the knight's attack squares from f7, calculating its precise movement pattern. The knight threatens multiple coordinates by shifting two squares in one direction and one in another. Checking the valid board squares reveals key attack points near the black king's position.

The king has no escape routes. Surrounding pieces cannot capture the knight, blocking all potential defensive moves. This confirms a decisive smothered checkmate scenario, with the knight strategically positioned to trap the king.

The pawn promotion to queen or rook on f8 delivers the final, conclusive checkmate. The bishop's diagonal from a1 to h8 confirms the rook's mate by controlling the king's escape square g7. Without the bishop, the king could flee to g7, but the combined control of rook and bishop ensures checkmate. The bishop's placement doesn't create a checkmate scenario. Analyzing the knight's potential, it fails to deliver check to the king. Ultimately, queen or rook promotion on f8 provides the decisive checkmate, with the queen being the more standard choice.

Examining the rook promotion reveals a precise mating mechanism. The rook controls critical squares, trapping the king with no escape routes.

Shifting focus to the next scenario, I'll investigate the queen's potential checkmate from d1 to d8.

The king's escape paths are systematically blocked: the 8th rank controlled by the queen, f7 occupied by the bishop, g7 threatened by the white pawn's diagonal attack, and h7 blocked by a black pawn. No defensive resources remain for the black king.

These coordinated pieces create an impenetrable mating net, demonstrating the queen and bishop's strategic power.

I'm refining the naming conventions for these checkmate patterns, considering precise terminology that captures their unique characteristics. The goal is clarity and descriptive accuracy.

The Smothered Mate showcases a knight delivering checkmate while the opponent's king is completely blocked by its own pieces. This classic tactical pattern demonstrates how a knight can exploit restricted movement.

The Promotion Mate highlights the transformative power of a pawn reaching the final rank, converting into a queen to deliver the decisive blow. It's a dramatic moment illustrating the potential hidden within seemingly modest pieces.

The Queen and Bishop Mate reveals a coordinated attack where two powerful pieces work in perfect harmony to restrict the king's escape routes, culminating in a precise checkmate.

I'm systematically verifying each FEN notation to ensure absolute precision in representing these critical chess positions. The careful breakdown of ranks helps confirm the board's exact configuration.

Each scenario reveals a unique board state with strategic piece placements. The variations in king and piece positions suggest nuanced tactical scenarios requiring careful analysis. I'll methodically examine the spatial relationships and potential move sequences.

The notation's compact representation demands meticulous translation, translating board spaces into precise algebraic symbols that capture the entire positional landscape.

Checkmate strategies emerge through strategic piece movements - rook, queen, knight, and pawn transformations creating decisive endgame scenarios. The compact board states demand precise, calculated approaches to achieving victory.