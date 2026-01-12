I need to create 3 distinct mate-in-1 scenarios for white. Each scenario should be:
1. A valid chess position in FEN notation
2. A position where white can checkmate black in one move
3. Distinct from the other scenarios (using different pieces/patterns)

Let me think of three different mate-in-1 patterns:

**Scenario 1: Back Rank Mate with Rook**
- Black king on e8, trapped by its own pieces
- White rook can deliver checkmate on e1 moving to e8

Let me construct a FEN:
- Black king on e8
- Black pawns on f7, g7, h7 (blocking king's escape)
- White rook on e1
- Some other pieces to make it valid

FEN: `r3k3/5ppp/8/8/8/8/8/4R3 w - - 0 1`
- Black: king e8, rook a8, pawns f7,g7,h7
- White: rook e1
- White to move
- Move: Re8#

Wait, let me verify this is checkmate:
- Re1 to e8 gives check
- King cannot move to d8, d7, e7, f8, f7 - let me check each:
  - d8: safe? No other white pieces attacking
  - d7: safe? No other white pieces attacking
  
This won't be mate because the king can escape. Let me reconsider.

**Scenario 1: Back Rank Mate (revised)**
Black king on g8, pawns on f7, g7, h7
White rook on a8
Move: Ra8-g8# would be checkmate but the rook is already on a8...

Let me try: 
FEN: `6k1/5ppp/8/8/8/8/8/6R1 w - - 0 1`


I see the challenge is finding a clear checkmate path with the rook blocked by pawns.

Analyzing the board, the white rook needs a precise move to deliver checkmate. The black king's mobility is restricted by its own pawns on f7, g7, and h7. By moving the rook to the eighth rank, I can control the king's potential escape squares.

The key is selecting the right rook file to create an inescapable mating net, ensuring the king has no legal moves when the rook delivers check.

For the queen scenario, the positioning is critical. By moving the queen to create a check that simultaneously blocks escape routes, I can force a decisive checkmate. The white king's supportive position prevents the black king from capturing the queen, completing the mating pattern.

For the knight scenarios, I'm exploring potential mating configurations. The challenge involves finding precise knight movements that restrict the king's mobility while maintaining strategic piece coordination. A smothered mate pattern emerges as a promising approach, requiring careful calculation of knight placement.

The current position suggests limited mating opportunities, with the knight struggling to create decisive attacking lines. Strategic positioning near the opponent's king remains critical for executing a successful knight-driven checkmate.

I'm exploring potential knight movement patterns that could restrict the black king's escape routes, carefully analyzing each potential square to identify a conclusive mating sequence.

The knight's mobility offers intriguing tactical possibilities, particularly when coordinating with the king and potentially other pieces to compress the opponent's defensive zone.

Examining the knight's potential squares reveals strategic opportunities for limiting the king's movement, with careful attention to blocking paths and creating decisive checkmate scenarios.

The rook on the back rank delivers a powerful checkmate, trapping the king with no escape routes. The queen's positioning similarly controls critical squares, preventing any king movement and securing a decisive victory. Qg8# confirms the checkmate:
- Queen controls critical squares around black king
- No legal escape routes for the king
- Decisive mating move

The bishop scenario requires careful positioning to trap the king effectively. Strategic placement of pieces creates an inescapable net.

Analyzing the potential checkmate move reveals nuanced square control and diagonal limitations. The bishop's precise location determines its attacking potential.

I'm carefully tracking square colors and diagonal paths to ensure a valid checkmate sequence. The king's restricted movement and specific square control become critical in solving this chess positioning challenge.

A bishop on f6 could potentially deliver a decisive check, but placement requires precise coordination with the rook's position. The light squares and dark squares create a strategic constraint that demands careful analysis.

I need to verify the exact configuration that enables a conclusive checkmate, paying close attention to the king's potential escape routes.

The current board setup suggests multiple potential mating patterns, but each requires meticulous verification of square control and piece interaction.

I'm exploring scenarios where the queen can deliver checkmate, focusing on the queen's ability to attack critical squares while blocking escape routes. The queen's mobility allows for precise positioning to trap the king.

In this specific configuration, the queen's move to g7 appears decisive, simultaneously attacking the king and blocking potential escape paths.

The rook's strategic placement on g6 prevents the king from capturing the queen, creating a definitive checkmate by controlling key defensive squares.

I'll verify the queen and king checkmate scenario, focusing on the precise control of escape routes.

The queen's strategic placement on g7 creates a decisive checkmate. By controlling critical squares around the black king, the white queen eliminates all potential escape paths. The white king's supportive position prevents the black king from capturing the queen, ensuring a definitive checkmate.

The rook's presence adds an extra layer of protection, blocking potential king movements and reinforcing the queen's control. I'll verify the FEN notation for the second position:

Rank 8 shows a king on h8 with 7 empty squares. Rank 7 contains a white Queen on f7. Rank 6 has the white King on g6. All other ranks are empty. The notation checks out correctly.

The position appears valid and represents a potential checkmate scenario. White's pieces are strategically positioned to control key squares.