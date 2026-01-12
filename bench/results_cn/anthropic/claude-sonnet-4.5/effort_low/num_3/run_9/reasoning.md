I need to create 3 valid mate-in-1 scenarios for White. Each scenario should be:
1. A valid chess position in FEN notation
2. A position where White can checkmate Black in one move
3. Distinct from the other scenarios

Let me think of three different mate-in-1 patterns:

**Scenario 1: Back Rank Mate**
White has a rook that can deliver checkmate on the 8th rank where the Black king is trapped by its own pawns.

Position: Black king on g8, Black pawns on f7, g7, h7 (trapping the king). White rook on a1.
FEN: Let me construct this carefully.
- Piece placement: Starting from rank 8: kg on g8, so "6k1" for rank 8
- Rank 7: pawns on f7, g7, h7: "5ppp"
- Ranks 6-2: empty: "8/8/8/8/8"
- Rank 1: White rook on a1, White king somewhere safe (let's say e1): "R3K3"

FEN: 6k1/5ppp/8/8/8/8/8/R3K3 w - - 0 1
Winning move: Ra8# (rook to a8 is checkmate)

**Scenario 2: Queen and King Mate**
White queen delivers checkmate with support from the White king.

Position: Black king on h8 (corner), White queen on g6, White king on g7 would be check already... let me reconsider.

Let me try: Black king on h1, White queen on g2 would be checkmate if Black king is on h1... but I need to make sure it's not already checkmate.

Actually, let me do: Black king on h8, White king on f7, White queen on h7 would be checkmate already.


FEN: 7k/6Q1/5K2/8/8/8/8/8 w - - 0 1
Winning move: Qh8# (queen to h8 is checkmate)

I verify the queen's control of escape squares. The queen on h1 prevents the king from moving to g1 or g2, while the king on f6 blocks the h7 escape route. I'm exploring potential checkmate scenarios with the queen. The king's escape routes are critical. With the White queen on a8, the Black king on h8 is under attack, but mobility depends on the White king's position. Controlling key squares prevents the king's escape, making a successful checkmate possible. I see the king's escape routes are blocked. White king on f6 doesn't control g8, so I'll check if the king can escape there. Moving the king to f7 changes the control - now g8 is controlled. Placing the queen on a8 creates a checkmate scenario where the black king has no legal moves.

The white king's precise positioning prevents the black king from finding an escape square, trapping it effectively. Knight's potential checkmate scenario seems complex. The king's escape routes are critical. Controlling g8 is key, but current piece placement doesn't definitively trap the king. The knight's check alone isn't sufficient to force checkmate. More strategic positioning or additional piece control would be needed to seal the king's fate. The king can escape to b8, as it's not controlled by the knight or rook. I need the white king positioned to block this escape square. By placing the white king on c6, I control several surrounding squares, but b8 remains uncontrolled. The knight's check from c7 doesn't prevent the king's retreat to b8.

Adding the queen on b1 changes the situation. The queen controls the b-file and prevents the king from moving to b8. However, the king still finds an escape route to a7, which isn't controlled by any white piece.

I'm exploring a smothered mate scenario with precise piece positioning. The classic setup requires the knight to deliver checkmate by attacking a king hemmed in by its own pieces.

The knight moves to f7, delivering a check the king cannot escape. Blocked by its own rook and pawns, the king has no legal moves. The rook on g8 cannot intervene, and no piece can block or capture the knight. I verify the checkmate by examining potential escape routes. The knight on f7 controls critical squares, blocking the king's movement. No piece can capture the knight - the rook and pawns are strategically positioned to prevent any rescue. From Black's perspective, pawn movement rules confirm no diagonal capture is possible. This confirms the smothered mate scenario. I verify the board layout systematically. Rank 8 has a rook and king, with six empty squares before them. Rank 7 contains two pawns, with six empty squares preceding them. The knight sits on f6, surrounded by empty squares. This precise configuration confirms the previous analysis about the checkmate scenario.

I'm exploring potential knight moves to deliver checkmate, carefully examining each possible destination and its control of critical squares. Some moves like Ne8 and Nd7 fail to threaten the king's position directly.

The knight's L-shaped movement offers multiple paths, but most routes are too distant from the target square to create an immediate threat. I need a precise calculation to find the decisive move.

Analyzing the knight's potential squares reveals limited attacking opportunities. The critical challenge is finding a position that directly threatens h8 while maintaining the smothered mate strategy.

I'm focusing on positioning the knight strategically to create a check from f7, which seems the most promising approach for disrupting the opponent's defensive structure.

Exploring possible knight movement paths shows several candidate squares that could potentially reach f7, each requiring careful tactical evaluation.

The knight on g5 delivers a smothered mate by checking the king on h8. Escape routes are completely blocked: rook prevents g8, pawns obstruct h7 and g7. No piece can capture or block the knight's decisive check.

The checkmate is confirmed through precise positional control and complete king immobilization. I see a rook delivering checkmate on a8, trapping the black king with no escape squares. The white king supports the rook's attack from e1, creating a decisive back rank mate.

The queen executes a similar back rank checkmate, landing on a8 and completely restricting the black king's movement with the white king positioned on f7.

The knight delivers a smothered mate by landing on f7, exploiting the confined black king surrounded by its own pieces, with no legal moves possible.

These three scenarios demonstrate precise, strategic checkmate techniques utilizing different pieces to trap the opponent's king.