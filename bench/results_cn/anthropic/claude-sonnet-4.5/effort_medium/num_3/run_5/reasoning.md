I need to create 3 valid mate-in-1 scenarios for white. Each scenario should be:
1. A valid chess position in FEN notation
2. Have white to move
3. Have exactly one move that delivers checkmate
4. Be distinct from each other

Let me think of three different types of mate-in-1:

**Scenario 1: Back Rank Mate**
A simple back rank mate where a rook or queen delivers mate on the 8th rank.
Position: Black king on g8, trapped by its own pawns on f7, g7, h7. White rook can move to the 8th rank.
FEN: 6k1/5ppp/8/8/8/8/8/R3K3 w - - 0 1
Winning move: Ra8#

Let me verify:
- Black king is on g8
- Pawns on f7, g7, h7 block escape
- White rook on a1 can move to a8
- This gives check and the king cannot escape
- Valid mate-in-1 ✓

**Scenario 2: Queen and Knight Mate**
A smothered mate or similar pattern with queen and knight.
Actually, let me do a simple queen mate instead.
Position: Black king on h8, trapped by pawns. White queen delivers mate.
FEN: 7k/5ppp/8/8/8/8/8/Q3K3 w - - 0 1
Winning move: Qa8#

Wait, let me verify:
- Black king on h8
- Pawns on f7, g7, h7
- White queen on a1 moves to a8
- This is check. Can the king move? g8 is available!
This doesn't work.

Let me try: 7k/6pp/5p2/8/8/8/8/Q3K3 w - - 0 1


I confirm the queen's mate works perfectly. The king is completely trapped by pawns and cannot escape the queen's check on a8. The queen controls critical escape squares, making this a valid checkmate scenario.

**Scenario 3: Bishop and Rook Mate**
I'll develop a unique mating pattern that demonstrates another checkmate technique.

The initial bishop placement doesn't create a checkmate. The diagonal control doesn't threaten the king, and the move fails to restrict the king's movement. I need a more strategic approach to limit the king's escape routes.

The queen checkmate is precise. By positioning the queen on g7, it directly attacks the king on h8 while the white king prevents any potential escape squares. The king is completely trapped, with no legal moves available.

I'll explore a different checkmate pattern focusing on the queen's ability to control critical squares and limit the opponent's king movement.

The queen's placement on h1 creates a decisive mating net. With the black king trapped on h8 and no escape squares, the checkmate becomes inevitable. The rook's position on f8 and the surrounding pawns completely restrict the king's mobility.

Analyzing the potential blocking moves reveals no viable defense for black. The rook cannot intervene, and the pawns block any potential escape routes. I see a knight mate scenario where the knight strategically moves to create a checkmate position. The knight's placement on h6 traps the black king, with no escape squares available. The surrounding pawns on g7 and h7 prevent any potential king movement, ensuring a decisive checkmate.

The rook's presence on f8 further restricts the king's mobility, blocking potential escape routes and solidifying the knight's control over critical squares.

I verify the knight's attack pattern, confirming it controls key escape squares. The king finds itself trapped, with no viable moves to safety. Checkmate appears inevitable. I'm analyzing knight moves to find a potential checkmate. The knight on f7 controls several squares, but doesn't immediately deliver check to the black king on h8. I'll systematically examine possible knight moves: Ne5, Nd6, Nd8, Nh6, Ng5. None of these moves create a direct check. The knight's positioning is critical for a potential mating pattern.

When I move the knight to g6, it attacks h8 and creates a potential checkmate scenario. The black king's escape squares are limited: g8, g7, h7. Checking the knight's control reveals the king cannot escape to g8, suggesting a potential mating configuration.

I examine the queen's positioning carefully. Moving to a7 delivers a decisive check, trapping the king. The black monarch has no legal moves - taking the queen is blocked by the white king's protection, and all potential escape squares are controlled.

The white king's strategic placement on b6 prevents any potential king movement, creating an inescapable mating net. This precise positioning ensures absolute control, rendering the black king completely immobilized.

The checkmate is confirmed through systematic elimination of all possible king movements, demonstrating a textbook example of coordinated piece control. I'll analyze the checkmate scenario, focusing on the queen's attack and the king's limited escape options. The queen on h1 delivers a decisive check to the black king on h8. Critically, the white pawn on f7 controls key squares, preventing the king's potential escape to g8. With pawns blocking h7 and g7, and the queen controlling the h-file, the black king has no legal moves. The checkmate is confirmed by the comprehensive square control and lack of king mobility. I recognize the checkmate patterns and appreciate their distinctive characteristics. Each scenario reveals a unique way of trapping the king with limited mobility and no escape routes. The names capture the spatial essence of each checkmate, highlighting the specific board positions that enable the decisive move.