I need to create 3 different mate-in-1 scenarios for white. Each should be:
1. A valid chess position
2. Where white can checkmate in one move
3. Distinct from each other (different types of checkmates)

Let me think of three different scenarios:

Scenario 1: Back rank mate with a rook
- Black king on e8, white rook on a8, black pawns blocking the king on f7, g7, h7
- FEN: Position needs to have white to move
- Let me construct: King on e8, pawns on f7, g7, h7, white rook on e1
- White plays Re1-e8#

Actually, let me be more careful with FEN notation. FEN has this format:
[piece placement] [active color] [castling rights] [en passant] [halfmove clock] [fullmove number]

Scenario 1: Back Rank Mate
- Black king on e8, black pawns on f7, g7, h7
- White rook on e1
- White king somewhere safe, say g1
- FEN: 4k3/5ppp/8/8/8/8/8/4K2R w - - 0 1
- Wait, that puts white king on e1 and rook on h1. Let me reconsider.
- FEN notation: ranks from 8 to 1, files a to h
- 4k3 means rank 8: empty-empty-empty-empty-king-empty-empty-empty
- Let me try: r3k3/5ppp/8/8/8/8/8/R3K3
- That's Black rook on a8, black king on e8, black pawns f7 g7 h7, white rook a1, white king e1
- Winning move: Ra1-a8#
- But wait, the black rook is in the way. 

I'll refine the back rank mate scenario. The FEN 4k3/5ppp/8/8/8/8/8/R3K3 w - - 0 1 represents a precise position where the white rook can deliver checkmate by moving to a8, eliminating any blocking pieces.

The winning move is straightforward: Ra8#, which traps the black king with no escape routes.

For the queen mate scenario, the key is positioning the queen to control critical squares while the king supports the attack. The winning move Qg7# decisively ends the game by cutting off the king's potential escape paths.

The knight mate scenario highlights a classic smothered mate setup, where surrounding pieces restrict the king's movement, allowing the knight to deliver a surprising checkmate. I see a potential smothered mate scenario with specific piece placements. The knight can't immediately reach f7, which complicates the mating pattern. The king and queen positions suggest a blocked configuration, but the knight's movement is restricted. The FEN notation reveals precise board positioning that prevents an immediate checkmate.

Exploring alternative knight placement and movement reveals strategic challenges in creating a checkmate sequence. The pawn blocking on f7 disrupts the initial mating attempt, requiring careful repositioning of pieces.

I'll verify the knight's potential paths and confirm the precise conditions for a successful checkmate.

The king's escape routes are now blocked by pawns on e7, f7, g7, and h7. The rook on a8 controls d8 and f8, leaving no legal moves for the black king. This confirms a definitive checkmate.

I'll explore alternative checkmate scenarios with different piece placements to understand potential escape routes.

Analyzing king's movement reveals limited options. Rook's check restricts mobility, with pawns and rook blocking key squares. Potential checkmate requires precise positioning to eliminate all escape paths.

Investigating further reveals the king's vulnerability, with strategic rook placement threatening a decisive move.

The queen scenario demonstrates another checkmate technique, strategically controlling escape routes and preventing king movement through precise positioning.

Knight checkmate reveals a complex scenario where the knight's unique movement creates an inescapable trap. The black king is hemmed in by its own rook, pawns, and the white knight's precise check, leaving no legal escape squares.

I verify the king's position and confirm the checkmate's legality by exploring additional scenarios with different piece configurations. These scenarios demonstrate strategic positioning that leads to decisive checkmate opportunities.

The knight's unique movement creates a powerful mating pattern, trapping the opponent's king with precision. Each scenario reveals a distinct checkmate technique, showcasing chess's tactical complexity.

The board positions confirm the notation's accuracy, highlighting strategic placement of pieces to execute decisive checkmates. White's positioning enables multiple winning approaches.

I've selected descriptive names capturing each scenario's essence: a back rank trap, a queen-driven checkmate, and a smothered mate utilizing a knight's unique movement.