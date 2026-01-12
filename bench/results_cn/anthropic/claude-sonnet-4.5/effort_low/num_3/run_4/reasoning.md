I need to create 3 different mate-in-1 scenarios for white. Each should be:
1. Valid chess positions
2. White to move and checkmate in 1 move
3. Distinct from each other (different types of checkmates)

Let me think of three different scenarios:

Scenario 1: Back rank mate with a rook
- Black king on e8, trapped by its own pieces
- White rook can move to e1 for checkmate
FEN: 6k1/5ppp/8/8/8/8/5PPP/4R1K1 w - - 0 1
Move: Re8#

Wait, let me verify this. Black king on g8, pawns on f7, g7, h7. White rook on e1. If Re8+, is it checkmate? The king on g8 cannot move to f8, h8, f7, g7, or h7. f8 and h8 would still be attacked by the rook on e8. f7, g7, h7 have pawns. So yes, this is mate.

Actually, let me reconsider the FEN. In FEN notation:
- Pieces are placed from rank 8 to rank 1
- Each rank goes from file a to file h
- Lowercase = black, uppercase = white

For a back rank mate: 6k1/5ppp/8/8/8/8/5PPP/4R1K1 w - - 0 1
This means:
- Rank 8: 6 empty squares, black king on g8, 1 empty
- Rank 7: 5 empty, then black pawns on f7, g7, h7
- Ranks 6-3: empty
- Rank 2: 5 empty, white pawns on f2, g2, h2
- Rank 1: 4 empty, white rook on e1, 1 empty, white king on g1, 1 empty


Move Re8# would indeed be checkmate.

I verify the back rank mate scenario is valid and checkmate is confirmed.

The queen checkmate requires careful positioning. I'm exploring potential configurations where the white queen can decisively trap the black king, ensuring no escape routes exist.

In this scenario, the queen moves to a8, creating a mating net that restricts the black king's movement. The white king's strategic placement on f6 prevents the black king from finding an escape square, making the queen's checkmate possible.

I verify the king's potential escape routes, systematically checking each adjacent square. The king cannot move to e8, e7, f7, or g7 due to the queen's or king's control. However, g8 appears open, suggesting this isn't a definitive checkmate.

The investigation continues with another potential mating configuration, exploring the precise positioning of pieces to achieve a successful checkmate. Queen on g7 delivers checkmate. King cannot escape to g8 or h7, as both squares are attacked by the queen. Mate confirmed.

Analyzing knight's potential checkmate move, I see the knight's attack squares from f7 include d6, d8, e5, g5, h6, and h8. This reveals strategic attack possibilities.

I'm exploring a classic smothered mate pattern with a specific board configuration. The positioning of pieces suggests a potential checkmate strategy involving the knight's unique movement capabilities.

I need to carefully analyze the knight's potential squares and how they interact with the king's restricted mobility. The challenge is finding a precise sequence that traps the king while delivering a decisive check.

My current approach involves experimenting with different piece placements to create a confined space where the knight can execute a decisive move. The king can't escape to f8 because the king on f6 controls that square. The bishop on g7 creates a deadly checkmate, trapping the black king with no legal moves.

Exploring classic checkmate patterns reveals precise positioning. Back rank mates with rook and queen demonstrate how a piece can completely restrict the king's movement when supported by the friendly king.

The queen's potential checkmate requires careful square control. Pawns and king placement become critical in determining whether a checkmate is possible.

I verify the king's escape routes systematically. The queen's attack covers key squares, blocking potential king movement. By examining each potential escape square, I confirm the king has no legal moves, resulting in a definitive checkmate.

Knight fork/mate scenario reveals a similar strategic pattern. Rook positioning creates an inescapable trap, with controlled squares preventing king movement. The precise placement eliminates all potential escape routes, demonstrating a clean, decisive checkmate.

These scenarios illustrate fundamental mating techniques, leveraging piece positioning to restrict the opponent's king and force an unavoidable conclusion.

The queen mate follows a comparable principle: strategic placement cuts off the king's potential moves, creating an immediate checkmate opportunity.

For the rook mate scenario, the two rooks strategically positioned on the 7th rank create a devastating confinement. By moving the rook from f7 to f8, I eliminate all escape routes for the black king. The king cannot move to any adjacent squares due to the rooks' controlling positions, resulting in a definitive checkmate.