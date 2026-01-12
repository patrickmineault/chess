I need to create 3 different mate-in-1 scenarios for white. Each scenario should be:
1. A valid chess position in FEN notation
2. Have white to move
3. Have exactly one move that delivers checkmate
4. Be distinct from each other

Let me think of three different types of mate-in-1:

Scenario 1: Back rank mate with a rook
- Black king on e8, trapped by its own pawns on f7, g7, h7
- White rook can move to e1 for checkmate
FEN: 4k3/5ppp/8/8/8/8/8/4R3 w - - 0 1
Wait, the rook is already on e1, so Re1 isn't valid. Let me adjust.
FEN: 4k3/5ppp/8/8/8/8/8/R7 w - - 0 1
Move: Ra8#

Actually, let me be more careful. In this position:
- Black king on e8
- Black pawns on f7, g7, h7 (blocking escape)
- White rook on a1
If White plays Ra8+, is it checkmate? The king on e8 is attacked by the rook on a8. Can it escape to d8, d7, e7, f8? d7 and e7 and f8 need to be controlled or blocked. Let me reconsider.

Let me use a simpler back rank mate:
FEN: 6k1/5ppp/8/8/8/8/8/6R1 w - - 0 1
- Black king on g8
- Black pawns on f7, g7, h7
- White rook on g1
Move: Rg1-g8# would be written as Rg8#
Wait, rook is on g1 already. Actually, checking the FEN again: the rook is on g1. 

I'll verify the checkmate by confirming the king's escape routes are blocked by pawns. The rook on g8 attacks the king, and the pawns prevent any potential escape.

The king cannot move to f8 or h8 because the rook controls those squares. The surrounding pawns trap the king, creating a definitive checkmate scenario.

Queen delivers mate from b6. Two potential mating moves emerge: Qb8# and Qa7#. Both moves attack the king on a8 and control critical escape squares, ensuring a checkmate. I'll explore knight mating possibilities, focusing on controlling escape squares and potential smothered mate patterns. The knight needs strategic positioning to limit the king's movement and create a decisive checkmate opportunity. Analyzing the board configuration reveals critical challenges in achieving a knight-based mate.

Examining potential knight moves and their impact on the king's mobility suggests a complex tactical challenge requiring precise piece coordination. I'm exploring smothered mate configurations, focusing on positioning pieces to trap the king. The knight needs precise placement to deliver a decisive check while blocking escape routes. I'm testing various board arrangements, carefully analyzing potential knight moves and king movements to create an inescapable mating scenario.

The challenge involves strategically surrounding the king with its own pieces, preventing any potential escape while setting up a knight check. My current approach involves experimenting with different piece placements to understand the precise conditions required for a successful smothered mate. I see a checkmate configuration with the bishop on g8. The white bishop controls critical escape squares around the black king. The king is trapped by its own pawn on h6 and the bishop's strategic placement. The white king supports this mating pattern from a distance, ensuring the black king has no legal moves.

The positioning creates a decisive blocking mechanism where the black king cannot escape the impending mate. Strategic piece placement limits the king's mobility, demonstrating a precise geometric control of the board.

The white queen strategically occupies b6, cutting off potential escape routes and preparing to deliver a conclusive checkmate. The white king's placement on a1 supports the queen's dominant positioning.

The queen's move to b8 directly attacks the black king, simultaneously controlling critical squares and preventing any potential retreat. This precise maneuver ensures an immediate checkmate.

Exploring knight-based checkmate strategies, I analyze the knight's potential moves from c7. By moving to a6, the knight delivers a decisive check, trapping the king with no escape routes. The white king's strategic positioning further restricts the black king's movement, creating an inescapable mating net.

The knight's precise positioning and the supporting king's control of key squares demonstrate a classic example of a knight checkmate, highlighting the piece's unique ability to create decisive tactical opportunities.

I'll verify the position's legality, ensuring the minimum requirements for a valid chess scenario are met. The key focus is on the knight's strategic placement and the king's supporting role in executing the mate.

I confirm the knight's critical position on c7, trapping the black king on a8. The white king's positioning on b6 provides crucial support, preventing any potential escape routes. The position meets all legal game requirements.

The checkmate demonstrates precise tactical execution, with the knight controlling key squares and the white king strategically positioned to block potential king movement.