**Creating mate-in-1 puzzles**

I need to set up three mate-in-1 puzzles for White. Each one needs to include the FEN for the board setup and a winning move. I’ll ensure these scenarios are correct, with each puzzle having a unique solution that leads to checkmate in one move.

So, I’ll put each scenario in a separate code fence with three lines: the name, FEN notation, and the winning move for White. It’s crucial that the positions are legal and verify that it's indeed a mate in one!**Designing FEN strings for puzzles**

I need to generate FEN strings that include the active color, castling rights, en passant target, halfmove clock, and fullmove number. It’s vital to ensure there are no illegal setups, like both kings being in check or inconsistent pieces. Since FEN doesn't directly encode history except for en passant, I can just set that to "-".

To craft three unique puzzles, I’ll need to analyze for alternative mates carefully. I might consider creating classic patterns like a smothered mate, ensuring there’s only one valid checking move that guarantees a win.**Creating unique mate-in-1 positions**

I can design the positions so that only the specified move results in check, ensuring no other piece can deliver check in one move except the one I choose. This might be challenging, but I think it’s doable. 

The user didn’t explicitly ask for uniqueness in the moves, just described wanting three scenarios where White can deliver a mate in one. I believe it’s fine if I list one winning move for each position. I just need to confirm that the move is a true checkmate! Let's move forward with crafting these positions carefully.**Designing Puzzle 1**

For Puzzle 1, I’m considering a straightforward setup: White has a king on g1, a queen on h6, a rook on f1, a bishop on c4, and a knight on f6, along with pawns on g2 and h2. Black has a king on g8, a queen on d4, and a few other pieces. I need to ensure there are no escape squares for Black.

I’ll try to create scenarios with minimal pieces, focusing on placing the Black king where it can't escape. A simpler option could be having just two kings, with White controlling critical squares, such as a queen on g7 against a Black king on h5 and checking with Qg5#.**Finalizing Puzzle 1 Design**

For Puzzle 1, I want to create a position where White can deliver a checkmate in one move. I have the Black king on h8, the White king on f6, and the White queen on f7. My goal is to ensure that Black cannot escape after White’s move.

Firstly, I need to confirm that the Black king isn’t already in check from the White queen or king before the move. I’ll check if moving the queen to g7 results in a checkmate. The Black king cannot move to g8, g7, or h7, making Qg7# a valid checkmate!**Designing Checkmate Puzzles**

I need to check how pieces attack h8. The White queen on f7 doesn't attack h8 directly, and the White king on f6 does not attack that square either. So, the Black king on h8 is initially safe. 

Now, considering moves like Qg8+ or Qf8+, I realize they won’t lead to checkmate because the Black king could capture the queen or escape. Thus, Qg7# is the winning move for this scenario.

I'll encode this in FEN as "7k/5Q2/5K2/8/8/8/8/8 w - - 0 1" and call it "Corner Queen Mate." Next, I'll design the second puzzle, focusing on a different mating pattern, perhaps a rook delivering a back-rank mate.**Designing Rook Mate Puzzle**

For the second puzzle, I want to create a scenario for a rook mate. To do this, I plan to set up a minimum of pieces—maybe three to five. 

Let's set the Black king on a8, the White king on c6, and the White rook on h1. The goal is to move the rook to h8 to deliver checkmate. First, I need to ensure that the Black king isn't already in check from the rook.

After checking the positions, I find that moving 1.Rh8# will indeed check the Black king. I must also verify that all squares around the Black king a8 are attacked or blocked to finalize it as a mate.**Verifying Check and Pieces Position**

First, I need to verify that the Black king isn't currently in check. The White rook on h1 doesn't attack the Black king on a8, so that's safe. The White king on b6 attacks the squares around it, confirming the Black king is not in check. 

Now, I’ll create the position for the puzzle in FEN notation. I’ve got: "k7/8/1K6/8/8/8/8/7R w - - 0 1". 

Next, for puzzle three, I want a knight smothered mate with a specific arrangement to ensure that the Black king has no legal moves after the knight's check. I’ll need to position minimal Black pieces around it and design the setup for a checkmate with the knight.**Verifying Check and Piece Placement**

I need to ensure the initial position is valid. The knight on h6 isn't putting the Black king on h8 in check since it only attacks squares like f5, f7, g4, and g8. After moving to Nf7+, the knight would attack h8. 

Now, I want to ensure the Black king has no legal moves after that. By placing a White rook on g1, it controls g8, preventing the Black king from moving there after the knight check. I also need to place a White king somewhere safe, verifying that it won’t check the Black king. Let's see how that setup looks!**Analyzing Check and Moves**

After White plays 1.Nf7+, the Black king on h8 is indeed in check. I need to see what its possible moves are. Unfortunately, h7 and g7 are occupied by Black pawns, preventing moves there. The only escape route to g8 are blocked by the rook on g1 because the pawn on g7 is in the way, so it can't be used to attack g8.

To fix this, I need a different piece, such as a knight or a bishop, that can attack g8 without being blocked. It could be a White bishop on h7, but that would mean there can't be a pawn there. Let's examine the possible placements carefully!**Final Check for Checkmate**

With the move 1.Nf7+, the Black king on h8 is trapped. I need to ensure that the king can't legally move to any adjacent squares, like g7 or h7 because they're occupied by Black's own pawns, and g8 is blocked by the rook. For the knight at f7, no Black piece can capture it, and the other Black pieces are either blocked or unable to move to attack.

The initial setup seems valid, as no checks are happening on the kings. So, it appears we have a checkmate!**Validating FEN Setup**

I need to confirm that the FEN is valid. The primary rule is that we shouldn't list castling rights for the king or rook if they aren’t in their starting positions. Since I set those as "-", this check is passed. Now, I need to ensure that I used the correct letter casing for the pieces: uppercase for white and lowercase for black. Everything looks good on that front. I’m ready to provide the answer!