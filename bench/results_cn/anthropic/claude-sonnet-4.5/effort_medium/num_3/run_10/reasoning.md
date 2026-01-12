I need to create 3 different chess positions where White can deliver checkmate in one move. Each scenario should be:
1. Valid (legal position)
2. Distinct from the others (different mating patterns)
3. Actually mate in 1 (the move delivers checkmate immediately)

Let me think of three different mating patterns:

**Scenario 1: Back Rank Mate**
Let me create a position where White delivers back rank mate with a rook.
- Black king on e8, trapped by its own pieces
- White rook can move to e1 or similar to deliver mate

FEN: 6k1/5ppp/8/8/8/8/8/4R3 w - - 0 1
Wait, let me check this. Black king on g8, pawns on f7, g7, h7. White rook on e1. 
Move: Re8# - This would be checkmate as the king is trapped by its own pawns.

Actually, let me make sure the FEN is correct:
6k1/5ppp/8/8/8/8/8/4R3 w - - 0 1
Starting from rank 8: 6 empty squares, king on g8, 1 empty square
Rank 7: 5 empty, then pawns on f7, g7, h7
Ranks 6-2: all empty (8/8/8/8/8)
Rank 1: 4 empty squares, Rook on e1, 3 empty squares

Move: Re8# - the rook moves from e1 to e8, giving check. The king on g8 cannot move to f8, f7, g7, h7, or h8, and the rook cannot be captured or blocked.

Wait, can the king go to h8 or h7? h7 has a pawn. h8 is empty and not attacked by the rook on e8. 

I realize the initial position doesn't create a true checkmate. The king has an escape square, so I need to modify the setup to ensure a complete back rank mate.

The rook's placement and the pawns' configuration are crucial. I need to block all potential king escape routes, ensuring no available squares exist for the king to move.

Rook check fails because the black rook can capture, preventing a decisive checkmate. The king's mobility and surrounding pawns complicate the mating attempt.

Queen to h8 seems promising but the king can capture, neutralizing the attack. No blocking pieces exist, yet the move does not secure checkmate.

Analyzing the position carefully, the queen's placement on g7 creates a critical check. The king's movement options are severely restricted: f8 blocked by rook, f7 controlled by rook, g7 occupied by queen, h8 and h7 blocked by pawn. Potential escape routes appear limited, suggesting a potential checkmate scenario.

I'm exploring precise queen positioning to create an inescapable trap. The challenge involves finding a definitive mating move that leaves no king movement possible. Standard mating patterns require careful calculation of control squares and piece coordination.

Repositioning pieces to create a decisive checkmate requires strategic placement, ensuring the king has no legal escape routes.

I see a potential checkmate with the queen controlling critical squares, trapping the black king completely. By moving the queen to d8, I block all potential king movements, creating an inescapable position.

The queen's placement prevents the king from moving to any adjacent squares, effectively sealing its fate. I see the king's escape routes on f8 and h8 aren't blocked. The rook's check alone isn't sufficient for checkmate. I'll need to prevent the king's lateral movement, ensuring those squares are controlled or occupied. The pawns on f7, g7, h7 restrict vertical movement, but horizontal escape remains possible. I see the chess position with two black rooks blocking potential escape squares. The initial attempts at checkmate fail because the king can still find refuge. The rook checks don't completely trap the black king.

I'm exploring a different approach using a knight to potentially create a smothered mate scenario. The key strategy involves positioning the knight to check the king while surrounding pawns prevent escape.

The critical elements for a successful smothered mate require precise knight placement and ensuring the king has no available flight squares. I'm exploring knight moves to create a smothered mate, analyzing potential check squares and king positions. Checking knight moves reveals several options, but most don't lead to a decisive checkmate. The challenge is finding a precise sequence that traps the black king while maintaining tactical control.

The knight's potential to attack multiple squares creates interesting positional pressure. However, the king's escape routes require careful evaluation to ensure a true checkmate scenario.

I'm exploring different knight placement options to restrict the black king's movement, analyzing attack patterns and potential escape paths.

The knight on f7 provides a critical check to the black king on h8, effectively trapping it with limited mobility. This strategic positioning creates a decisive checkmate opportunity.

I need to verify the king's escape routes and potential defensive moves. The rook could potentially capture the knight, preventing an immediate checkmate.

Analyzing knight moves reveals specific attack paths to h8, confirming potential mating squares at f7 and g6. The goal is finding a precise knight placement that traps the black king.

Examining the position, the knight's check creates critical limitations. The rook on g8 cannot capture the knight, and pawns have restricted movement, potentially setting up a decisive mating configuration.

A knight's unique L-shaped movement threatens the king's escape routes. With surrounding pieces blocking potential retreats, the strategic placement suggests an imminent checkmate scenario.

The knight can indeed reach h8, attacking the king directly while preventing any defensive moves by the surrounding pieces.

The checkmate is precise: Nf7#, trapping the black king with no escape routes.

For the bishop scenario, I realize the initial placement doesn't attack a8. I need to position the bishop strategically on the diagonal connecting a8, carefully selecting a square that controls the king's movement while ensuring the white king supports the attack.

The bishop must occupy a square that threatens the black king's mobility, creating a decisive mating net. I notice the rook on a7 creates a critical checking situation. The white king on b6 and bishop on g2 seem positioned to restrict the black king's movement. I'm analyzing whether the rook's current placement definitively prevents the black king's escape, considering the potential checkmate configuration.

The position reveals complex positional constraints that require careful verification of legal moves and check conditions. I'll examine the precise interactions between the white king, rook, and bishop to determine potential checkmate scenarios. The queen's diagonal path does not reach b8. King can escape to b8, so it's not checkmate. The specific diagonals from h1 do not control the b8 square, leaving an escape route for the black king. I'm exploring a potential back rank checkmate scenario. The king seems partially blocked by pawns, but needs complete confinement. I'll analyze the king's escape routes carefully. Rook placement on a8 doesn't immediately trap the king. I need to ensure the king has no legal moves when the rook checks.

The pawn structure looks promising for restricting king movement. I'll methodically check each potential escape square and the rook's attacking capabilities. Pawn on f7 promotes to queen, delivering checkmate. White pawns on g7 and h7 block king's escape routes. Black king on h8 cannot move to g8, h7, or g7 due to pawn control. Checkmate confirmed. The king faces a critical check after f8=Q+, with limited escape options. Capturing the queen is impossible from h8, and blocking is not feasible. Potential moves to g8 and g7 are controlled by pawns or the queen's attack. The queen on f8 threatens multiple lines, making escape challenging. The king's movement is severely restricted by the queen's powerful positioning.

Analyzing h7 reveals a potential capture of the white pawn, which would remove the check. By taking the pawn at h7, the king escapes the immediate threat and finds a safe square. This strategic move prevents checkmate and provides a temporary reprieve from the queen's attack.

The diagonal control and pawn positioning create a complex defensive scenario that initially seems decisive but actually offers the king an escape route.

I analyze the queen's attack pattern, noting its coverage of multiple squares. Despite threatening several key positions, the king retains mobility to certain undefended squares. By systematically checking potential king movements against the queen's attack range, I discover potential escape paths that prevent an immediate checkmate.

The strategic positioning requires precise evaluation of each potential king move, considering both direct attacks and potential blocking squares. The black king can escape to c5 since Qd3 doesn't attack that square and Ke5 also doesn't control it. This means the proposed move is not checkmate. I see the queen on d3 threatens the black king, but the escape square c5 seems open. The knight's position becomes crucial in determining checkmate potential. I'll analyze the knight's attack range carefully to see if c5 remains uncontrolled.

The knight's control of key squares prevents the king's escape. Queen and knight collaborate to block every potential move. The black king finds itself completely trapped, with no legal squares to move. I verify the checkmate pattern, confirming the queen and knight coordinate perfectly to trap the black king. The queen's move to d3 creates an inescapable position, blocking all potential escape routes while the knight controls critical squares.

The strategic placement leaves the black king with no legal moves, definitively ending the game. The black king is trapped. The rook can't capture the knight, and pawns are blocked. No piece can intervene. Checkmate confirmed.

The black king is cornered. Queen controls critical squares, preventing escape. Knight and white king collaborate to seal the king's fate. No defensive options remain.

Black king has no refuge. Queen dominates key squares, knight blocks potential escape routes. White king supports the attack. Absolute checkmate achieved.