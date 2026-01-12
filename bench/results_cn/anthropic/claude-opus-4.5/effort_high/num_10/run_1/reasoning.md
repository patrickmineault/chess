The user wants me to describe 10 mate-in-1 scenarios for white. Each scenario needs:
1. A name
2. FEN notation for the setup
3. The winning move for white

Let me think of 10 distinct mate-in-1 scenarios:

1. **Back Rank Mate**
A classic scenario where the rook or queen delivers checkmate on the back rank while the king is trapped by its own pawns.

Setup: Black king on g8, black pawns on f7, g7, h7. White rook on a1.
FEN: 6k1/5ppp/8/8/8/8/8/R3K3 w Q - 0 1

Wait, let me be more careful. The white king should be somewhere safe, and the position should be legal.

Let me try: Black king on g8, pawns on f7, g7, h7. White rook on e1, white king on h1.
FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1
Winning move: Re8# (Rook to e8 is checkmate)

Actually, let me double-check. The rook on e1, moving to e8. The black king on g8 would be in check from the rook on the 8th rank. The king can't move to f8 (rook controls it), h8 (rook controls it), h7 (blocked by pawn), g7 (blocked by pawn), f7 (blocked by pawn). So yes, Re8# is mate.

2. **Scholar's Mate Pattern**
Queen delivers checkmate on f7 with support.

Setup: Standard position after 1.e4 e5 2.Bc4 Nc6 3.Qh5 ... and black made a bad move
Actually, let me set up a simpler mate-in-1 position.


Black king on e8, white queen on e5, white bishop on c4. Black has some pieces but the f7 square is weak. I need to verify that Qxf7 is mate. The king on e8 would be in check from the queen on f7. It can't escape to d8, e7 (queen controls), d7 (queen controls), or f8. Let me construct this more carefully with a legal position.

I'll work through concrete examples. For a back rank mate: Black king trapped on g8 with pawns on f7, g7, h7. If I place a white rook on e1, then Re8 is checkmate since the king has no escape squares. For the queen and bishop setup, I need to position pieces so that Qxf7 delivers mate with the bishop supporting from c4. The queen on f7 would give check, and the bishop on c4 defends it. The king can't move to e7, d7, or f8 since the queen controls those squares. For this to be mate, d8 must also be covered or blocked—perhaps by a black piece already positioned there.

The classic Scholar's Mate demonstrates this pattern: after 1.e4 e5 2.Bc4 Nc6 3.Qh5 Nf6?? 4.Qxf7# is checkmate because the queen and bishop coordinate to trap the king with no escape squares. Nf6, empty f6,g6, Nh6 ✓
- Rank 5: 4p2Q means empty a5-d5, pawn e5, empty f5,g5, Queen h5 ✓
- Rank 4: 2B1P3 means empty a4,b4, Bishop c4, empty d4, Pawn e4, empty f4,g4,h4 ✓
- Rank 3: 8 means all empty ✓
- Rank 2: PPPP1PPP means pawns a2,b2,c2,d2, empty e2, pawns f2,g2,h2 ✓
- Rank 1: RNB1K1NR means Ra1, Nb1, Bc1, empty d1, Ke1, empty f1, Ng1, Rh1 ✓

After Qxf7+, the black king has no escape—d8 is blocked by the queen, e7 and f8 are controlled by the white queen, and capturing is impossible since the bishop defends. That's checkmate. I'm recognizing this as Anastasia's Mate—a classic mating pattern where a knight and rook work together to trap the king. The typical setup has the king boxed in by its own pawn, the knight controlling key escape squares, and the rook delivering the final blow on an open file. In this position, the black king on h7 is hemmed in by the h6 pawn, the white knight on e7 cuts off g8 and g6, and the rook can move to h7 for checkmate. and the rook delivers checkmate along the h-file, with the king trapped by its own pawn on g7.

The typical setup has the Black king on h7, a pawn blocking on g7, the White knight positioned on e7 to control escape squares, and the White rook ready to move to h3 or deliver mate on the h-file. I'm working through the exact square placements—the knight needs to give check while covering key squares like h6, and the rook must be able to reach the h-file to finish the pattern. I need to reconsider the board setup. Let me place the king on g8 instead with pawns on h7 and g7, and position my rook on h1 with a knight on f6.

If I play Rh8+, the king is in check. It can't escape to f8 or e8 since the knight controls those squares from f6. The g7 pawn blocks that square, and h7 is also blocked. The only question is whether f7 is available—the knight on f6 doesn't control f7, so the king could potentially escape there.

Shifting the knight to e6 changes what it controls: d8, f8, c7, and g7. Now if I play Rh8+, the king still can't reach f8 (controlled by the knight), but f7 remains undefended. I need to block that escape square. Adding a bishop on f7 would seal it off, making Rh8# checkmate since f8 is controlled by the knight, f7 is blocked by my own piece, and g7 is controlled by the knight as well. .)

**2. Back Rank Mate (Queen)**
FEN: 6k1/5ppp/8/8/8/8/8/3QK3 w - - 0 1
Move: Qd8#

**3. Scholar's Mate Setup**
FEN: r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 4 4
Move: Qxf7#

**4. Fool's Mate**
FEN: rnbqkbnr/ppppp2p/5p2/6pQ/4P3/8/PPPP1PPP/RNB1

These positions demonstrate classic mating patterns—the queen delivering mate on d8 mirrors the rook's back rank tactic, Scholar's Mate shows how rapid piece coordination can create unstoppable threats, and Fool's Mate illustrates how early mistakes expose the king to immediate danger. The knight on f7 actually does cover h8, which is promising. Let me reconsider the setup more carefully. If the rook moves to h8 with check, the king on h8 would be in direct contact with the rook—that's not how this works. I need the rook to deliver check from a different square while the knight controls the escape routes. Let me try positioning the rook on h7 instead, with the knight still on f7 to cover h8 and other flight squares. d by rook on h8. The knight on f6 covers f8, the pawn blocks f7, and the rook controls g7—that's checkmate.

Let me verify the position: Black king on g8 with a pawn on f7, White rook on h7 and knight on f6. After Rh8#, the king has no escape squares and no piece can interpose or capture the rook. d by its own pieces. The king on h8 is trapped by the rook on g8 and pawns on f7 and h7, leaving no escape squares. A knight landing on f7 would deliver checkmate since it controls h8 while the king has no flight squares.

Let me verify the knight's reach from f7: moving in an L-shape (two squares in one direction, one square perpendicular), it can reach h8, h6, d8, d6, g5, and e5. That confirms Nf7 is indeed mate. I need to figure out which knight move delivers mate. From e5, the knight can jump to either g6 or f7, both giving check to the king on h8. Let me evaluate which one is actually mate by checking if the king has any escape squares after each move.

After Ng6+, the king's potential escape squares are blocked: h7 and g7 are covered by pawns, g8 by the rook. However, the rook can simply capture the knight with Rxg6, so this isn't mate.

After Nf7+, the same squares are unavailable to the king, but crucially the rook on g8 cannot reach f7 in one move. Since nothing can capture the knight, this is checkmate.

The position has White's knight on e5, Black's king on h8 with a rook on g8 and pawns on g7 and h7, with White's king on e1.

Playing Nf7 delivers checkmate—the knight gives check to the king on h8, which cannot escape because the rook, g-pawn, and h-pawn all control its flight squares. The rook on g8 cannot capture the knight since it's pinned by the White king's control of the escape route. Nf7# is checkmate.

For the hook mate pattern, I need a rook delivering check while a knight defends it and a pawn restricts the king's escape squares. With the black king on g8, a rook on e8 gives check, the knight on f6 both protects the rook and controls key squares, and a pawn on g7 blocks retreat options. they're on the same rank, so that's check. The king on f8 can't move to e8 where the rook sits, and e7 is also controlled by the rook along the file.

But I need to place the knight to complete the hook mate pattern. Let me reconsider—maybe I should look at simpler mating patterns instead. Back rank mates with rooks and queens work well, Scholar's Mate is straightforward, Arabian Mate with knight and rook is classic. I'm trying to recall which standard patterns would be clearest to demonstrate.

For Boden's Mate, two bishops coordinate on intersecting diagonals to trap the king. One bishop delivers check while the other controls escape squares—typically the king ends up on c8 with bishops positioned to cover the critical diagonals.

I need to construct a position where a single move completes the mate rather than just showing the final setup. The black king on c8 with pieces like a queen on d8 and rook on b8 blocking retreats, then one bishop moves into position while the other already controls the necessary squares to seal the mate.

Let me work through the bishop coverage: if one bishop sits on e5, it controls the long diagonal through c7 and d6, which are critical escape squares. A second bishop moving to a6 would give check along the long diagonal while the e5 bishop prevents the king from fleeing to d7 or c7. The rook on b8 and queen on d8 already block those squares, leaving the king with no legal moves. I need to reconsider the geometry here. The bishop on a6 delivers check along the a6-c8 diagonal, while the second bishop must control the remaining escape squares. For the king on c8 blocked by its own pieces on b8 and d8, I need to verify which squares require coverage—b7 is the critical one. The bishop on e5 controls the long diagonal, covering c7 and d6, but I should check if it reaches b7. Actually, b7 sits on the a6-c8 diagonal itself, so the attacking bishop handles that. The mate works when one bishop gives check while the other cuts off any flight squares the king might have. a6, I need the bishop on the f1-a6 diagonal. Placing it on f1 works.

FEN: 1nkq4/3p4/8/4B3/8/8/8/5BK1 w - - 0 1

Ba6 delivers checkmate—the bishop controls b7 while Be5 covers c7, and the king's own pieces on b8, d8, and the pawn on d7 seal off all escape squares.

For epaulette mate, the king gets trapped between its own rooks positioned like shoulder boards, then a major piece delivers mate along an open file. With Black's king on e8 flanked by rooks on d8 and f8, a queen move to e7 would be checkmate since those rooks block the king's lateral escape.

FEN: 3rkr2/8/8/8/8/8/8/4QK2 w - - 0 1

Qe7# works—the queen controls all flight squares including f7 diagonally, while the rooks prevent any sideways movement.

Actually, I need to verify the queen is protected. Looking at the position, nothing defends e7, so the king could simply capture it with Kxe7. This isn't checkmate after all.

Let me reconfigure: placing a rook on e1 to defend the queen. With White having Qb4, Re1, and Kf1 against Black's Ke8, Rd8, and Rf8, the move Qe7# works because the rook on e1 guards the queen. The king has no escape—d8 and f8 are blocked by Black's own rooks, d7 and f7 are controlled by the queen, and capturing on e7 is illegal since the rook defends it.

For the Opera Mate pattern, I'm looking at how a rook or queen delivers checkmate on the back rank while a bishop controls key escape squares. The typical setup has the king on h8 with a bishop covering g7 from the diagonal and a rook giving mate on the 8th rank. Testing with Kf8, a pawn on e7, Re1, and Bg5—the move Re8# should work, but I need to verify the escape squares are properly covered. The configuration needs adjustment to ensure all flight squares are controlled. The diagonal from c5 goes through d6, e7, and reaches f8, so the bishop does cover that square. But checking the position after Re8#: the rook controls e8, yet f7, g8, and g7 remain undefended—this setup fails.

I need a configuration with stronger piece coordination. The Opera Game's actual finish involved a more intricate arrangement where the rook and bishop work together more effectively on the back rank and its diagonals.

Let me reconsider: what if I place a black piece on h8 to restrict the king further? With Black having Kg8, Rh8, and a pawn on f7, and White positioning Rd1 and Be5, the move Rd8# becomes checkmate. The rook gives check along the eighth rank, the bishop on e5 controls g7, the black rook blocks h8, and the pawn prevents escape to f7.

But h7 remains open—the king could slip there. I need to cover that square. Adding a white pawn to h6 doesn't work since pawns don't control backward squares. Instead, I could place a white piece like a queen or position another bishop to guard h7 and complete the mating net.

Let me try a knight on f6. That controls h7 directly, but it also gives check to the king on g8, which breaks the mate pattern. Moving the knight to h6 instead covers both f7 and g8 without delivering check, which should work better. 1) = j7 = off), (h6+(+2,-1) = j5 = off)

So Nh6 controls: f7, f5, g8, g4.

Since the knight on h6 gives check to a king on g8, this position is invalid—the king can't be in check when it's White's turn. I need to try a different approach.

Let me consider placing a queen to cover h7 instead. A queen on a2 would control the a2-g8 diagonal (a2-b3-c4-d5-e6-f7-g8), but that doesn't include h7. I should explore other queen placements.

A queen on b1 can cover h7 via the b1-h7 diagonal (b1-c2-d3-e4-f5-g6-h7). With Rd1, Be5, and Qb1, plus Black's king on g8, rook on h8, and pawn on f7, Rd8 delivers checkmate. The king has no escape: h8 is blocked by its own rook, h7 is controlled by the queen, g7 is controlled by the bishop, f8 is controlled by the rook, and f7 is blocked by its own pawn. I need to identify the position and move for Damiano's Mate. The classic pattern involves the queen and a pawn coordinating to trap the king on the edge. In the final mating position, the king sits on h8 with the queen delivering mate from g8 or h7. Let me work out what the starting position should be before the mating move. Damiano's Mate typically involves the queen delivering checkmate along the h-file or g-file with the king boxed in, often by a pawn on g6 restricting escape squares.

I'm considering a position with Kh8 and a pawn on g7. If I play Qg8+, the king is in check, but it can capture the queen unless the queen has protection. I need to add a defender—perhaps a rook on d8 to guard g8, making the capture impossible and delivering mate.

With Qg8+ and Rd8 supporting it, the king on h8 has no legal moves: h7 is controlled by the queen on g8 (via the diagonal), and g8 itself is occupied by the queen. That's checkmate.

Let me verify the position: Black has only the king on h8 and a pawn on g7. White has the queen on f7 and rook on d1, which delivers the decisive check from d8. The FEN confirms this setup with the king trapped on the back rank.

Actually, I need the rook to defend g8 so the queen can deliver checkmate there. Moving the rook to b8 covers the entire eighth rank, allowing Qg8# to work since the rook protects the queen. The corrected position places the rook on b8 instead of d1.

With the rook defending from b8, Qg8 is checkmate—the king can't capture the queen and has no escape squares since g8 controls h7.

For Greco's mate, I need to reconsider the setup. The bishop should control the escape square while the rook delivers mate, but the positioning I'm imagining creates issues—the rook can't move to h8 if the king occupies it. Let me think about where the king actually needs to be positioned for this pattern to work.

If the king sits on g8 instead, with pawns on h7 and f7 blocking escape, then Rh8 becomes checkmate—provided the bishop covers g7. A bishop on c4 controls the long diagonal through f7 and g8, but that leaves g7 undefended. I need to either reposition the bishop or add another piece to secure that square.

Moving the bishop to c3 works perfectly. From there it commands the a1-h8 diagonal, covering both g7 and h8, while the rook on h8 controls the entire eighth rank including f8. With f7 blocked by a pawn and g7 covered by the bishop, the king has no escape—that's checkmate. Let me verify I have all 10 patterns correct. The back rank variations with rook and queen both deliver mate on the eighth rank, Arabian mate uses the rook and knight coordination, and the smothered mate involves the knight with the king trapped by its own pieces.

Continuing through the remaining positions: Boden's mate uses both bishops to control escape squares, the epaulette pattern has the queen delivering mate while rooks block the king's flight, Opera mate combines the bishop and rook for the final blow, and Damiano's mate uses the rook and queen working together. After checking the Scholar's Mate position, the queen on f7 delivers mate since the king on e8 has no escape—d8 holds its own queen, e7 and d7 are controlled by the queen, f8 is also covered, and the bishop on c4 prevents the king from capturing on f7. ✓

For the back rank mate with the queen, moving Qd8 checks the king on g8, which cannot escape to f8 or h8 as both squares fall under the queen's control, and the pawns on f7, g7, and h7 block retreat. ✓

All positions check out. Now I'll compile the final list. Rook on h8 covers the h-file and 8th rank, so g7 isn't controlled by it. I need to verify which squares the king can actually escape to.

From g8, the king could move to f8, f7, g7, or h7. The knight on f6 controls f8 (knights move in an L-shape: two squares in one direction, one square perpendicular). The rook on h8 controls h7. That leaves f7 and g7 to check—f7 has the pawn, and g7 is empty but also controlled by the knight. The king has no legal moves, confirming checkmate. Ne6 covers f8 and g7, the rook on h8 covers h7, and the pawn blocks f7—that's checkmate. The corrected Arabian Mate has the knight on e6 instead of f6, which was the key adjustment needed to control f8 and prevent the king's escape.

I'm verifying each pattern: the back rank mate with the rook delivers checkmate on e8 with the king trapped by its own pawns, the queen version works similarly on d8, Scholar's Mate follows the classic pattern with Qxf7#, and the Arabian Mate now has the proper knight placement to seal off all escape squares. 9. **Damiano's Mate**: 1R5k/5Qp1/8/8/8/8/8/6K1 w - - 0 1
   Move: Qg8#
   ✓

10. **Greco's Mate**: 6k1/5p1p/8/8/8/2B5/8/6KR w - - 0 1
    Move: Rh8#
    ✓

All verified! Now I should verify these positions could actually occur in real games. Scanning through them: the back rank patterns are standard endgame scenarios, Scholar's mate is a well-known opening trap, and the Arabian mate setup is geometrically feasible from normal play.

The smothered, Boden's, and Epaulette mates are all established tactical patterns. The Opera mate derives from the famous historical game, and both Damiano's and Greco's mates are classical positions. These all check out as legal positions.

Actually, I'm reconsidering the back rank queen position—having the king on e1 feels exposed. I'll adjust it to 6k1/5ppp/8/8/8/8/8/3Q2K1 w - - 0 to give the white king better placement.

With the queen on d1 and black king on g8, Qd8 is checkmate since the king can't escape to f8 or h8 (controlled by the queen on the 8th rank) and f7, g7, h7 are blocked by pawns.

For Boden's Mate, the position has Black's king on c8 with a knight on b8 and queen on d8, while White has bishops on e5 and f1. Playing Ba6 delivers mate because the bishop controls the escape square b7, the other bishop on e5 covers c7, and the pawn on d7 blocks that square, leaving the king with no legal moves.

Now I'll compile the final answer.