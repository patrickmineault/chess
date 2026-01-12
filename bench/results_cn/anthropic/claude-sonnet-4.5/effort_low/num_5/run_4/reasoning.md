I need to create 5 different mate-in-1 scenarios for white. Each should be:
1. A valid chess position
2. White to move
3. White can deliver checkmate in one move
4. Distinct from each other (different types of checkmates)

Let me think of different types of mate-in-1:
1. Back rank mate with a rook
2. Queen and knight mate
3. Smothered mate with a knight
4. Bishop and queen mate
5. Pawn promotion mate

Let me create valid FEN notations for each:

1. Back Rank Mate with Rook:
Black king on h8, trapped by its own pawns on f7, g7, h7
White rook can deliver mate on h1 moving to h8? No wait, let me think more carefully.

Black king on g8, pawns on f7, g7, h7
White rook on a8 can deliver Ra8#? No, that's not check.
White rook on h1 can deliver Rh8#

FEN: 6k1/5ppp/8/8/8/8/8/7R w - - 0 1
Move: Rh8#

2. Queen Mate:
Black king on h8, trapped by pawns
White queen can deliver mate from various squares

FEN: 7k/5ppp/8/8/8/8/8/Q7 w - - 0 1
Move: Qa8#

3. Smothered Mate with Knight:
Black king on h8, surrounded by own pieces
White knight delivers mate

FEN: 6rk/5ppp/8/8/8/8/8/5N2 w - - 0 1
Move: Nf6# - wait, the knight is on f1, can it reach a square to give mate?
Let me reconsider.

For smothered mate, king on h8, pieces on g8, g7, h7


I need the knight to move to f6 to create a smothered mate scenario. The knight's position and the surrounding pieces are crucial for this type of checkmate.

The diagonal mate requires precise queen positioning to trap the king. Pawn promotion offers another potential mating strategy, transforming a seemingly weak piece into a powerful checkmate weapon.

Each mating pattern demands careful piece placement and understanding of the king's limited escape routes. 1. Back Rank Mate: Rook delivers checkmate by controlling the entire back rank, trapping the king with blocked escape routes.

2. Queen Mate on Back Rank: Queen achieves checkmate by occupying the back rank, cutting off all potential king movements.

3. Smothered Mate: Knight executes a precise check, exploiting the king's restricted position with surrounding pawns and pieces preventing escape.

4. Queen Mate via Diagonal: Positioning suggests a potential diagonal checkmate strategy, with the queen targeting the confined king.

Exploring queen movement options from different board positions, carefully analyzing potential checkmate configurations and escape routes.

Investigating queen placement and checking possible mating patterns, noting pawn and king positions that restrict movement.

Systematically testing various scenarios to identify precise checkmate opportunities, recognizing blocking mechanisms and strategic limitations.

Exploring different board configurations to find a definitive mating sequence, carefully analyzing each potential move's effectiveness.

The queen on g6 provides a decisive checkmate by controlling key squares and trapping the king with the support of the h7 pawn. This strategic placement leaves the king with no escape routes, demonstrating a clean and effective mating pattern.

Pawn promotion to a queen on f8 creates an immediate checkmate. The newly promoted queen controls critical squares, preventing the king's movement and securing victory through precise positional control.

I'll verify the FEN notation carefully, ensuring each position represents a unique checkmate scenario with precise king and piece placement.

I'll name these distinct checkmate patterns systematically, focusing on the key piece and technique used to deliver the final blow. Each pattern demonstrates a different strategic approach to ending the game decisively.

The notation requires careful checking to confirm the precise checkmate move, ensuring accuracy in representing the final position.

The pawn promotion mate completes the sequence with a transformative final move, converting a humble pawn into a powerful queen to deliver checkmate.