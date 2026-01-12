I need to create 3 different chess positions where White can checkmate in 1 move. Let me think of valid mate-in-1 scenarios.

For each scenario, I need:
1. A descriptive name
2. A valid FEN notation
3. The winning move in algebraic notation

Let me create three distinct scenarios:

**Scenario 1: Back Rank Mate with Rook**
A classic back rank mate where White's rook delivers checkmate on the 8th rank.

Position: Black king on e8, trapped by its own pawns on f7, g7, h7. White rook on a1 can move to e1#.

FEN: Let me construct this carefully:
- Black king on e8
- Black pawns on f7, g7, h7
- White rook on a1
- White king somewhere safe, say on g1

FEN format: [pieces on rank 8][/rank 7][/rank 6]...[/rank 1] [turn] [castling] [en passant] [halfmove] [fullmove]

Rank 8: k (black king on e8) - so "4k3"
Rank 7: pawns on f7,g7,h7 - "5ppp"
Rank 6: empty - "8"
Rank 5: empty - "8"
Rank 4: empty - "8"
Rank 3: empty - "8"
Rank 2: empty - "8"
Rank 1: White rook on a1, white king on g1 - "R5K1"

FEN: 4k3/5ppp/8/8/8/8/8/R5K1 w - - 0 1

Winning move: Re1#

**Scenario 2: Queen and Knight Mate**
White queen on d7, black king on e8, white knight can give checkmate.


I'm struggling to find a precise configuration that creates a genuine mate-in-1 scenario. The king's escape routes need careful blocking to ensure a single-move checkmate.

The positioning requires strategic placement of pieces to limit the black king's movement. I'll need to visualize the exact square where the knight could deliver a decisive check that the king cannot escape.

The queen seems promising for creating a tight mating net, especially when supported by pawns or other pieces that restrict the king's potential flight squares.

I notice the knight could potentially jump to f7, delivering a smothered mate. The black king is hemmed in by its own pieces - a rook on g8 and pawns on g7 and h7 - which prevents escape routes.

The positioning looks critical: blocking pieces trap the king, allowing the knight a decisive strike. Knight on e5 creates a checkmate threat by controlling f7. The board setup shows the white king on a1, with the knight strategically positioned to limit black's escape routes. Verifying the mate reveals precise positioning is crucial for successful execution.

The rook's potential to deliver a back rank mate highlights the importance of piece coordination in creating decisive checkmate opportunities. I see the king's escape routes are completely blocked. The queen on f8 delivers a decisive checkmate, with the rook on g8 and pawn on h7 preventing any king movement. The black king has no legal squares to escape, and no piece can capture or block the queen's attack.

The knight's smothered mate follows a similar pattern. On f7, the knight checks the king, who finds every potential escape route sealed by his own pieces - the rook on g8 and pawns on g7 and h7. This precise positioning creates an inescapable trap.

I verify the knight's movement: one square right and two squares up from e5 to f7 matches the classic L-shaped knight trajectory. Checkmate confirmed.