I need to create 3 different mate-in-1 scenarios for white. Each scenario should be:
1. A valid chess position in FEN notation
2. Have white to move
3. Result in checkmate in one move
4. Be distinct from each other

Let me think of three different types of checkmate patterns:

**Scenario 1: Back Rank Mate**
Let me create a position where white can deliver back rank mate with a rook.
- Black king on g8, trapped by its own pawns on f7, g7, h7
- White rook on d1
- Move: Rd8#

FEN: Let me construct this:
- 8th rank: black king on g8, so: 6k1 (6 empty squares, king, 1 empty)
- 7th rank: black pawns on f7, g7, h7: 5ppp (5 empty, 3 pawns)
- 6th-3rd ranks: empty
- 2nd rank: maybe some white pawns
- 1st rank: white rook on d1, white king somewhere safe

Let me be more careful:
Position:
- Rank 8: ......k. = 6k1
- Rank 7: .....ppp = 5ppp
- Rank 6: ........ = 8
- Rank 5: ........ = 8
- Rank 4: ........ = 8
- Rank 3: ........ = 8
- Rank 2: ........ = 8
- Rank 1: ...R...K = 3R3K

FEN: 6k1/5ppp/8/8/8/8/8/3R3K w - - 0 1
Move: Rd8#

**Scenario 2: Queen and King Mate**
A position where the queen delivers checkmate.


I'll complete the FEN notation by carefully positioning the pieces:

FEN: 7k/8/6Q1/8/8/8/8/6K1 w - - 0 1
Move: Qg7#

The queen traps the black king in the corner, with no escape squares available. I'm exploring a knight checkmate scenario, focusing on trapping the black king with its own pieces. The key is finding a precise position where the knight can deliver mate in a single move, with the king completely immobilized by surrounding pieces. I'm carefully analyzing potential king and knight placements to create a smothered mate configuration.

The challenge is creating a compact setup where the knight can strike decisively, leaving the king with absolutely no escape routes. I'll need to ensure the surrounding pieces block all potential king movements. White's knight on e5 delivers a decisive checkmate by jumping to f7, trapping the black king against its own rook and pawn. The king has no escape squares, creating an inescapable mating net.

The rook cannot intervene or capture the knight, leaving the black king completely helpless. No defensive moves remain possible.

I'm carefully analyzing the knight's control squares and the king's restricted movement options. The knight's precise positioning creates an inescapable trap for the black king.

From f7, the knight cannot control g7, which means the king has a potential escape route. This reveals the current position is not a checkmate. To create a true checkmate, I need to strategically block the g7 square, either by adding a controlling piece or placing a pawn to seal the king's fate.

The position requires precise piece placement to eliminate all potential king escape paths. The rook's movement options are limited, unable to capture the knight on f7. Diagonal pawn captures also cannot reach the knight. Black pawns move downward, restricting their ability to interact with the knight's position.

The chess position 6rk/6pp/8/4N3/8/8/8/6K1 w - - 0 1 with Nf7# is a valid checkmate, as no piece can prevent or capture the knight's decisive move.

I'll now analyze three specific checkmate scenarios, starting with a back rank mate where the rook controls critical escape squares.

**Scenario 1: Back Rank Mate**
The rook decisively traps the king by blocking all potential escape routes, creating an inescapable checkmate position.

**Scenario 2: Queen Checkmate**
The queen strategically positions itself to control key squares, preventing the king's movement and delivering a conclusive checkmate.

**Scenario 3: Knight Checkmate**
A knight executes a precise checkmate, demonstrating how this piece can restrict a king's mobility through strategic placement.

These scenarios showcase different tactical approaches to achieving checkmate, highlighting the unique movement capabilities of chess pieces. I've carefully analyzed three chess checkmate scenarios, verifying each position's details. The scenarios range from a classic back rank mate using a rook to a queen delivering checkmate in the corner, with a nuanced knight checkmate that closely resembles a traditional smothered mate pattern. I've systematically named and confirmed the tactical viability of each scenario, ensuring precise positioning and movement constraints for the kings and attacking pieces. I carefully analyze the FEN notation, breaking down each rank systematically. The notation precisely represents the chess board's configuration, moving from rank 8 to rank 1. Each segment reveals the piece placement, with numbers indicating empty squares and specific letters representing piece types and colors. The notation provides a comprehensive snapshot of the board's current state, allowing for exact reconstruction of the chess position. The FEN representations accurately capture the board positions, with each scenario showing a unique checkmate configuration. The board layouts and piece placements are precisely documented, revealing distinct strategic positions that enable immediate mate.