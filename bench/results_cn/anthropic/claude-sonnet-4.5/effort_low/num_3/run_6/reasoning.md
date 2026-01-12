I need to create 3 different mate-in-1 scenarios for white. Each scenario should be:
1. A valid chess position
2. Where white can checkmate in one move
3. Distinct from each other

Let me think of three different types of mate-in-1:

**Scenario 1: Back Rank Mate**
White has a rook that can deliver checkmate on the back rank where the black king is trapped by its own pawns.

Setup: Black king on g8, black pawns on f7, g7, h7. White rook on d1, white king somewhere safe like h1.
FEN: 6k1/5ppp/8/8/8/8/8/3R2K1 w - - 0 1
Winning move: Rd8#

Let me verify: The rook moves to d8, giving check to the king on g8. The king cannot escape because f8, h8 are controlled by the rook, and f7, g7, h7 are blocked by black's own pawns. This is checkmate.

**Scenario 2: Queen and King Mate**
White queen delivers mate with support from the white king.

Setup: Black king on h8 (corner), white queen on g6, white king on g7 (supporting).
Wait, if white king is on g7, the black king on h8 is already in an impossible position.

Let me reconsider: Black king on h8, white queen on f6, white king on g6.
FEN: 7k/8/5QK1/8/8/8/8/8 w - - 0 1
Winning move: Qg7#

Verify: Queen on g7 gives check. King on h8 cannot move to g8 (controlled by queen), h7 (controlled by king), or g7 (occupied by queen). This is checkmate.
 
**Scenario 3: Knight Mate**
I'll explore a knight checkmate in the corner with strategic pawn blocking.

The knight creates a mating net by jumping to f7, trapping the king with help from the white king and black's own pawns. The positioning ensures no escape routes for the black king.

Verification confirms the knight's precise movement delivers a decisive checkmate by controlling all potential escape squares.