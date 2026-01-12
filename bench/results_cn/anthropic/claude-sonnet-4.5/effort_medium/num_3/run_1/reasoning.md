I need to create 3 different mate-in-1 scenarios for white. Each scenario should be:
1. A valid chess position in FEN notation
2. A position where white can checkmate in 1 move
3. Distinct from the other scenarios

Let me think of three different types of mate-in-1:

**Scenario 1: Back Rank Mate**
White has a rook that can deliver checkmate on the back rank.
Let me construct: Black king on g8, trapped by its own pawns on f7, g7, h7. White rook on a8 can move to g8#... wait, that doesn't work because the rook is already on the 8th rank.

Let me try: Black king on g8, pawns on f7, h7 blocking escape. White rook on d1. The move would be Rd8#.
FEN: 6k1/5p1p/8/8/8/8/8/3R2K1 w - - 0 1
Move: Rd8#

Actually, let me verify this is mate: King on g8, after Rd8+, the king cannot go to f8 (controlled by Rd8), cannot go to h8 or h7 (blocked/controlled), cannot go to g7 or f7 (pawns or controlled). Yes, this works.

**Scenario 2: Queen Mate**
Black king in the corner, white queen delivers mate.
Black king on h8, maybe some pieces blocking escape. White queen on a1, moves to h1#.
FEN: 7k/6pp/8/8/8/8/8/Q5K1 w - - 0 1
Move: Qh1#

Let me verify: King on h8, pawns on g7 and h7. After Qh1+, the king cannot move anywhere (h7 has pawn, g8 and g7 are controlled by queen). 

I'll confirm the knight mate scenario's checkmate possibilities. The king's escape routes are limited by the knight's positioning. If the knight moves to f7, the king's movement becomes critically restricted. The knight's unique jumping ability creates a precise mating net that traps the king effectively.

The smothered mate concept requires careful piece placement to block all potential king escape squares. Strategic positioning of pawns and pieces around the king creates a confined space where the knight can deliver a decisive checkmate.

I'm exploring various knight maneuvering techniques to restrict the black king's movement and create a winning position. The challenge involves precise coordination of pieces to limit escape routes.

After Ne6+, the black king faces severe mobility constraints. With the white king positioned strategically and the knight controlling critical squares, the black king has extremely limited options for escape.

The key is understanding how the knight's moves and the white king's position combine to create a decisive positional advantage. Analyzing checkmate scenarios with rook and king positioning. Rf8 creates a critical control zone, blocking king's escape routes. Verifying each potential move reveals strategic piece placement prevents king movement. Confirmed mate when all potential escape squares are controlled by white pieces.

Exploring different checkmate configurations, focusing on back rank and corner scenarios. Precise positioning of rook and king determines successful checkmate strategy. I verify the checkmate scenarios, confirming each position's unique mating pattern. The rook and queen demonstrate precise control of escape squares, systematically trapping the black king with strategic king support. These compact checkmate configurations showcase elegant positional domination through careful piece placement and movement.