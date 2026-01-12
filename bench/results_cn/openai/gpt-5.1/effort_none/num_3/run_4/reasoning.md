**Designing mate-in-1 problems**

I need to create three mate-in-1 problems, each in separate code blocks. They should include a name, FEN, and the winning move. It’s crucial to ensure these FENs represent legal positions where White can achieve a checkmate in one move. I must double-check that the side to move is White and that the Black king is in check without any legal moves available. I want to avoid illegal scenarios, so I'll keep it simple yet effective. Let's get started!**Creating a back-rank mate problem**

I'm working on a scenario where White can deliver mate with the queen. For this back-rank crush, the goal is for White to play Qg8#, while the Black king is on g8 with its escape squares controlled. I’ll set Black’s position with Kg8 and pawns on g7, h7, and f7. White's setup will include Kg1, Qe7, Re1, Bc4, and pawns f2, g2, h2. I need to ensure that after Qxe8#, the Black king has no escape options. Let’s finalize this setup!**Analyzing king's escape options**

I'm looking at the squares around the Black king on g8. After the move Qxe8+, the Black king has no legal escape squares because f8 is empty and g8 is occupied by the king. The king can't move to e8 either, since that would involve moving two squares, which is illegal. I’ve checked the Black pawns on f7, g7, and h7, but they can't defend e8. Now, I need to see if h8 is controlled by White. If it is, that confirms checkmate!**Checking control of h8**

I need to clarify that the queen on e8 controls the line e8-f8-g8-h8, but this line can be blocked. Since the Black king is on g8, it blocks the queen’s attack to h8—meaning the queen does not control that square. So, if the king moves from g8 to h8, it might be legal if no other White pieces control h8. I checked the bishop on c4, and it attacks g8 but not h8, which keeps h8 open!**Validating the checkmate scenario**

Alright, I need to ensure everything checks out for the checkmate scenario. After Qxf7, I confirmed that h7 is not under attack. The Black king can't move to h7, f8 is under attack by the queen, and g7 is blocked by its own pawn. So, I figured Kg8 can't move to any legal squares. Interpositions or captures don’t work either, as there are no available pieces to block or capture the attacking bishop on c4. Thus, after thorough checks, it seems that this scenario indeed leads to checkmate!**Generating FEN for scenarios**

I'm creating FEN for the first scenario. For White, I have a king on g1, queen on e7, rook on f1, bishop on c4, and pawns on f2, g2, h2, representing "1K + Q + R + B + 3P". For Black, there’s a king on g8, a rook on h8, and pawns on f7, g7, h7, which is "1k + R + 3P". After compiling everything together, I arrive at the complete FEN: "6kr/4Qppp/8/8/2B5/8/5PPP/5RK1 w - - 0 1." 

Now, for the second scenario, I’m exploring a smothered checkmate with a knight. If the Black king is on h8, and the knight moves to f7, I’ll make sure the surrounding squares are controlled. To achieve this, I can position the white queen on g8 and a knight on h6 to deliver check. I’m checking every angle to ensure everything aligns for this checkmate scenario!**Evaluating legal moves and checkmate**

I'm assessing the area around h8 for the black king. The only nearby squares are occupied by black's own pieces, leaving no legal moves. The black rook on g8 is blocked by the pawn at g7, so it can't capture the knight on f7. This confirms it's a checkmate since the knight's position doesn’t attack h8 directly but limits movements. I’ll ensure the white king is safe and then finalize the FEN for the configuration. 

In my second scenario, I'm exploring pawn promotion for checkmate. I place the black king on h8 with a rook on g8 and a pawn on h7, while the white pawn is on g7 ready to promote on the next turn. Once promoted, the new queen will deliver checkmate! I need to make sure that post-promotion, the black king has no escape. 

It’s important to confirm all positions are reachable legally, as these scenarios must be valid chess configurations!**Analyzing legal game mechanics**

I’m considering the implications of the black king being in check while it's not their turn. Legally, the side not to move can't be in check, so I need to ensure the board position is valid. To avoid confusion, I'll place the black king in a safe position, like h7, while maintaining the white pawn on g7 for promotion to checkmate. 

For my next scenario, I’m thinking about using a rook move instead of promotion to create a straightforward checkmate pattern. This should help clarify the setup while ensuring all conditions are met!**Designing checkmate scenarios**

I'm brainstorming checkmate scenarios and analyzing different setups. For instance, using a rook to deliver check along the back rank seems promising, with the black king on h7. However, I need to ensure that black's pieces don’t block potential escape squares. I'm considering several options, including a "ladder mate" or positioning black pieces in a corner for an easier setup. 

Ultimately, I’m leaning towards a bishop mate to create a straightforward victory. It’s easier to ensure correctness with bishops or queens, following the user's request for distinct positions while maintaining effective tactics.**Crafting legal checkmate scenarios**

I'm working on creating another queen checkmate that'll be geometrically distinct. I'm considering using known mating patterns like Scholar's Mate but need to ensure everything is legally consistent. For example, I can derive the FEN from the common opening moves leading to checkmate. 

After some calculations, I confirmed the FEN and adjusted the positions accordingly. The winning move, Qxf7#, results in checkmate, with the queen supported. This scenario seems safe and legal, making it a solid example!**Ensuring distinct scenarios**

I realized both scenario 1 and scenario 3 use the same winning move, Qxf7#, but I want to ensure they're distinct. I could swap out the move in scenario 1 for something like Qxf8# or change to Qg7#. For clarity and to avoid confusion, I decided to keep scenario 1 with Qxf7# and ensure each scenario has its unique position, even if the mechanics are similar. I double-checked that the black king isn’t in check and confirmed everything was legal before planning to output the three scenarios in the specified format.