I need to create 3 different mate-in-1 scenarios for white. Each should be:
1. Valid chess positions
2. Where white can checkmate in exactly one move
3. Distinct from each other (using different pieces/tactics)

Let me think of three different scenarios:

**Scenario 1: Back Rank Mate with Rook**
- Black king on e8, trapped by its own pieces
- White rook can deliver checkmate on e1 or the 8th rank
- Let me construct: Black king on e8, black pawns on f7, g7, h7 blocking escape
- White rook on a8 can play Ra8-e8# or white rook on e1 can play Re1-e8#

FEN: Let me build it carefully:
- Black king on e8
- Black pawns on f7, g7, h7
- White rook on e1
- White king somewhere safe, say g1

FEN format: [pieces on rank 8][/rank 7][/rank 6][/rank 5][/rank 4][/rank 3][/rank 2][/rank 1] [turn] [castling] [en passant] [halfmove] [fullmove]

Rank 8: black king on e8: "4k3"
Rank 7: black pawns on f7, g7, h7: "5ppp"
Rank 6: empty: "8"
Rank 5: empty: "8"
Rank 4: empty: "8"
Rank 3: empty: "8"
Rank 2: empty: "8"
Rank 1: white rook on e1, white king on g1: "4R1K1"

FEN: "4k3/5ppp/8/8/8/8/8/4R1K1 w - - 0 1"


Winning move: Re8#

I'm exploring a queen checkmate scenario. The challenge is positioning the queen to deliver a decisive blow in the corner. I need to carefully arrange the pieces to create a mating net that traps the black king with no escape routes. The queen must have a clear path to deliver checkmate while ensuring no defensive moves are possible.

The key is controlling key squares and using pawns to limit the king's movement. A rook on the h-file provides additional control, creating a tight defensive formation that leaves the black king with no way out.

I'm exploring potential checkmate patterns, carefully positioning white pieces to restrict the king's escape routes while ensuring a decisive attack.

The key is controlling h7 with the bishop on f5, which prevents the black king's retreat when the queen delivers check from f8. This strategic placement creates a decisive mating net.

Verifying the checkmate reveals no escape routes for the black king. The queen's check from f8 is absolute, with no blocking pieces or potential king movements possible.

Exploring a knight-based checkmate scenario, I'm analyzing potential smothered mate configurations. The key challenge involves positioning the knight to attack while surrounding squares are controlled, trapping the king with no legal moves.

Carefully examining the board, I'm checking knight placement options. The potential Ne7+ move looks promising, with surrounding pawns and rook potentially restricting the king's movement. Each possible square needs precise evaluation to confirm a definitive checkmate. I verify the knight's checkmate move. The knight on e7 attacks the king, blocking all escape routes. Pawns and rook prevent the king from moving to adjacent squares. The checkmate is conclusive, with no legal moves for the black king.

I'll quickly check another potential mating scenario involving a rook on the back rank, confirming its legal checkmate configuration.

The queen and bishop combination offers another elegant mating pattern, strategically trapping the king with precise positioning. The smothered knight mate demonstrates a classic tactical motif, using piece coordination to restrict the king's movement.

I'll need to refine the terminology for the knight scenario, as it doesn't perfectly match the traditional definition of a smothered mate. The positioning reveals an interesting tactical limitation for the trapped king.

The back rank scenario demonstrates a classic confinement technique. The rook exploits the king's restricted movement, with pawns and the rook's control eliminating escape routes.

The queen and bishop coordination showcases precise positional control. Their combined attack leaves the king with no viable escape, highlighting the power of piece synergy in creating a decisive checkmate.

The knight scenario presents a unique positional trap, where the king's mobility is severely restricted by surrounding pawns and the knight's strategic placement.