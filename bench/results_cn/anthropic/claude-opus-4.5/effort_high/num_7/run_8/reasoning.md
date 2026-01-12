The user wants me to describe 7 mate-in-1 scenarios for white. Each scenario needs:
1. A name
2. FEN notation for the setup
3. The winning move for white

Let me think of 7 distinct mate-in-1 scenarios:

**Scenario 1: Back Rank Mate**
A classic mate where a rook or queen delivers checkmate on the back rank while the king is trapped by its own pawns.

Setup: Black king on g8, pawns on f7, g7, h7. White rook on e1.
If I put a white rook on e1 and the black king on g8 with pawns blocking, then Re8# would be mate.

FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1
Move: Re8#

Wait, let me verify this. King on g8, pawns on f7, g7, h7. White rook on e1, white king on h1.
After Re8+, the king on g8 is in check. Can it escape? 
- Kf7? No, pawn is there
- Kg7? No, pawn is there  
- Kh7? No, pawn is there
- Kf8? Rook controls e8-f8
- Kh8? Rook controls e8? No wait, from e8 the rook controls the 8th rank, so Kh8 is not possible.

Actually wait, if the rook is on e1 and plays Re8, the rook is now on e8. The black king is on g8. The rook on e8 attacks all of the 8th rank. So the king cannot go to f8 or h8. The king also cannot go to f7, g7, h7 because of the pawns. That's checkmate! Good.


Re8# is mate.

**Scenario 2: Queen and Bishop Mate**
I need a position where the queen delivers mate with bishop support. Let me try a king trapped on h8 with a queen on g6 and bishop controlling g7. Qg7# would be mate since the queen is protected by the bishop and the king has no escape squares. White has King on g1, Queen on g6, and Bishop on c3 against Black's King on h8. After Qg7+, the king is trapped—it can't escape to g8 or h7 since the queen controls both squares, and there are no other pieces to block or capture. That's checkmate.

For the smothered mate scenario, I'm considering a position where Black's king sits on h8 boxed in by its own rook on g8 and pawns on g7 and h7, allowing a White knight to deliver mate from a nearby square like g6. Nf7 delivers checkmate here. The king on g8 is in check from the knight, and every escape square is covered: f8 has the rook, h8 has the rook, g7 and h7 are blocked by pawns, and f7 is occupied by the knight itself. So the position needs Black's king on g8, rooks on f8 and h8, pawns on g7 and h7, with White's knight able to reach f7 from e5. White has a knight on e5 that can deliver checkmate with Nf7#. I need to construct a position where the knight move works.

Let me set up the board properly: Black king on g8, rooks on f8 and h8, pawns on g7 and h7. White king on g1 with the knight on e5. The FEN should show the king boxed in by its own pieces, so Nf7 becomes mate since the knight can't be captured and the king has no escape squares. I need to cover h8 to prevent the king's escape. Adding a white piece like a bishop or queen could work, but the position is becoming unwieldy. Let me consider the classic smothered mate pattern instead—the one typically involving a queen sacrifice on g8 followed by a knight delivering mate on f7. The setup would have Black's king on g8 with rooks or queen on the back rank and pawns blocking g7 and h7, then after White plays Qg8+ and Black recaptures with the rook, Nf7 becomes checkmate.

But I'm looking for a position that's already mate in one, not a sacrifice sequence. Let me test if a knight on f5 works with Black's king on g8, rook on g7, rook on h8, and a pawn on h7—from there Ne7+ gives check, though the king might escape to f8 if that square is open. I should verify whether a knight on f7 actually delivers mate against a king on h8 with a rook on g8 and pawns on g7 and h7.

A knight on f7 does attack h8, putting the king in check. The king can't move to g8 (occupied by the rook), g7 (blocked by pawn), or h7 (blocked by pawn). The rook on g8 can't reach f7 since it only controls the g-file and the 8th rank. That's checkmate.

For the position to work, I need to reconsider the knight placement. A knight on f6 can't actually reach f7—it moves to d5, d7, e4, e8, g4, g8, h5, or h7. I need a square from which the knight can jump to f7: d6, d8, e5, g5, or h6. Placing it on g5 works, since from there it can move to e4, e6, f3, f7, h3, and h7.

With the knight on g5 and the black king trapped on h8 by its own rook and pawns, Nf7 delivers checkmate. The king has no escape squares—g8 and g7 are blocked by its own pieces, h7 is blocked by a pawn, and the rook can't capture the knight on f7.

For fool's mate, I need to construct a position where White can deliver a similar quick checkmate. The pattern involves weakening the kingside with pawn moves. If Black plays f6 and g5, White can play Qh5# with the queen delivering mate on h5, since the king on e8 has no defense against the attack on the weakened kingside. The queen on h5 delivers check along the diagonal, and Black's king has no legal moves. The e7 square is blocked by Black's own pawn, f7 is controlled by the queen, d8 is occupied by Black's queen, and f8 lies outside the queen's attack range. Black cannot escape the check. The bishop on f8 moves diagonally—to e7, d6, c5, and so on—not to f7. Let me check if anything can block the diagonal check from h5 to e8. The queen's attack runs through g6 and f7, both empty squares. The knight on g8 can only reach e7, f6, or h6, so it cannot interpose on g6. Nothing can block on f7either. This appears to be checkmate.

Wait, I should verify the queen's full range of attack. Beyond the diagonal, the queen also controls the h-file and the 5th rank, which limits Black's options further.

The diagonal from h5 to e8 passes through g6 and f7. Converting to coordinates: h5 is (8,5) and e8 is (5,8), giving a difference of (-3,3)—equal absolute values confirm it's a valid diagonal. The position works. Now I'll construct the FEN.

FEN: rnbqkbnr/ppppp2p/5p2/6p1/3PP3/8/PPP2PPP/RNBQKBNR w KQkq - 0 3

Move: Qh5#

For Anastasia's Mate, I need a king trapped on h7 by its own pawn on g7, a knight controlling escape squares from e7, and a rook delivering mate along the h-file. Let me position: Black king h7, pawn g7, white knight e7, white rook on the h-file. The rook on the h-file delivers check to the king on h7. If the king tries h8, the knight on e7 controls g8, preventing that escape. The knight from e7 reaches c6, c8, d5, f5, g6, and g8—so g8 is covered, cutting off h8 as a flight square.

To complete the mating net, I need to block h8 itself. A white queen or bishop positioned on the h-file would seal that square. The classic Anastasia pattern uses a knight controlling the escape squares while a rook delivers mate along the file, often with a pawn on g6 or another piece preventing the king's retreat.

With a knight on e5 covering g6 and a rook on h1 giving check, the king still has h8 available. Adding a bishop on d3 attacks along the long diagonal toward h7, but that doesn't prevent the king from moving to h8. For mate to work, I need to ensure all escape squares are covered—the rook gives check on the h-file, but I must also control h8 to trap the king completely. Let me reconsider the setup. If Black has Kh7 with a rook on h8 and a pawn on g6, and I place White's knight on e7 to cover g8, then a rook on h1 would give check along the h-file. But Black could block with Rh8-h7, which doesn't lead to mate in one.

I need the checking move to be unstoppable—either the king has no escape squares and can't block the check. A queen might work better positioned to deliver an unblockable check. the king has no legal moves after the check, it's checkmate in one move.

Let me verify this works. With Black's king on h7, pawns on g7 and g6, and White's knight on e7 and rook on h1, playing Rh1+ delivers check. The king cannot escape to h8 since the rook controls the entire h-file, cannot go to g8 because the knight covers that square, and g7 and g6 are blocked by pawns. That's mate. I'm getting tangled up on the mechanics here. The rook on the h-file gives check to the king on h7 without needing to capture anything—it just needs a clear line. So if the rook moves from a1 to h1, that's checkmate since the king has no escape squares with the pawns blocking g7 and g6.

Let me verify the position works: the king on h7 is in check from Rh1, can't move to h8 (still attacked by the rook), can't go to g8 (the knight on e7 controls that), and g6 and g7 are blocked by pawns. There's no way to block or capture the rook either.

For the FEN, I need to account for all the pieces—the rook on a1, knight on e7, king on f1, the black king on h7, and both black pawns on g7 and g6. (4), e7 has white knight N, f7 empty (1), g7 has black pawn p, h7 has black king k = 4N1pk

Rank 6: a6-f6 empty (6), g6 has black pawn, h6 empty (1) = 6p1

Ranks 5-2 are all empty = 8 for each

Rank 1: a1 white rook R, b1-e1 empty (4), f1 white king K, g1-h1 empty (2) = R4K2

The complete FEN is 8/4N1pk/6p1/8/8/8/8/R4K2 w - - 0 1, and the move is Rh1#.

After Rh1+, the black king on h7 is in check. The king cannot escape to h8 since the rook controls that square on the h-file. Moving to g8 is blocked by the knight on e7, which covers that square. Both g7 and g6 are occupied by black pawns, eliminating those options. The f8 square is too far away—the king can only move one square from h7, so it's unreachable.

The h6 square is adjacent but also attacked by the rook on h1. There's no way to block the check since black has no pieces besides the king and pawns that could interpose on the h-file. The rook on h1 cannot be captured by any black piece.

Let me verify this is a legal position: White has a rook on a1, king on f1, and knight on e7. Black has a king on h7 with pawns on g6 and g7. Both sides have kings and the position is reachable, so Rh1# is indeed checkmate.

For the Arabian mate pattern, the typical setup involves a black king trapped in a corner like h8, with a white knight on f7 controlling escape squares and a white rook delivering mate along the h-file.

Let me reconsider the knight placement more carefully. A knight on f7 can reach d6, d8, e5, g5, h6, and h8—so it does cover h8 and h6. But if the king is already on h8 with the knight attacking it, the king would already be in check before the mating move.

I need to find a position where the king isn't in check initially. Let me try placing the king on h8, the knight on d7, and the rook on h1 instead.

From d7, the knight can move to b6, b8, c5, e5, f6, or f8. Testing Nf6 as checkmate—the knight from f6 attacks d5, d7, e4, e8, g4, g8, h5, and h7, but not h8 itself. That won't work. Similarly, Nf8 attacks d7, e6, g6, and h7, but again misses h8.

The only knight squares that actually attack h8 are f7 and g6, so I need to position the knight on one of those squares for the final move.

A knight can reach f7 from d6, d8, e5, g5, h6, or h8. It can reach g6 from e5, e7, f4, f8, h4, or h8. Since e5 connects to both, I'll place the knight there with a rook on h1 to support. From e5, moving to f7 gives checkmate—the knight attacks h8 directly, putting the king in check with no escape squares available.

Wait, after Nf7+, the king could flee to g8 since the knight doesn't control that square. I need to cover g8 somehow. The rook on h1 only controls the h-file, so it won't help. Adding a bishop on the long diagonal through a2 won't work either—the knight on f7 would block its line to g8. A bishop on h7 would be adjacent to g8 and could control it instead.

But placing the bishop on h7 creates a new problem. After Nf7+, if the king tries g7, that square isn't controlled by a bishop on h7 since they're on the same rank. The bishop only attacks diagonally, so g7 remains an escape square.

I need to block g7 somehow. Adding a Black pawn there would prevent the king from escaping in that direction. With the position adjusted to include a pawn on g7, the bishop on h7 can still reach g8 and g6 diagonally, which helps restrict the king's options further.

After the knight moves to f7 with check, the king's escape squares disappear: g8 falls to the bishop, g7 is occupied by Black's own pawn, and h7 is controlled by the rook on h1, so capturing the bishop isn't safe. The knight from f7 also prevents h6 as an escape.

Black has no way to block or capture the checking piece since only the king and pawn remain. This suggests the Arabian Mate pattern—king trapped in the corner with a rook on the adjacent file and knight controlling escape squares. The final mating position would be Kh8 with Rh7 and Nf7, achievable in one move from the current setup.

Testing Rh7#: the rook gives check along the 7th rank, but the king can escape to g8 since the knight on f7 doesn't cover that square (it only reaches d6, d8, e5, g5, h6, h8). I need a different piece arrangement—perhaps the knight positioned on g6 instead to properly seal off the escape squares.

But wait, if the knight is already on g6 attacking h8, the king can't legally be there before the move. Let me reconsider the setup entirely. For a clean Arabian mate pattern with Kh8, I'd need Rh7 and Nf7 in the final position, which means one of these pieces must move into place on the final move. Before that, the position needs to be legal with the king not in check.

If I place the king on g8 instead, the knight still creates problems—Nf6 attacks g8, so that's check again. I need to find a configuration where neither the rook nor knight is giving check before the final move.

For mate-in-1 to work, the king must be safe initially, then after White's move it's checkmated. The attacking piece shouldn't be checking the king beforehand. If I put the rook on g7 and the king on h8, the rook doesn't attack h8 yet. But when the rook moves to h7, it does attack h8 along the file—that's check. The issue is ensuring the king has no escape squares and the rook truly delivers mate, not just check. After Rh7, the rook controls the entire 7th rank, so g7 becomes unavailable. Kg8 is also blocked by the knight on f6. That leaves no legal moves—it's checkmate.

The position needs a white rook on h7, a knight on f6 controlling g8, and the black king trapped on h8. Adding some pawns would make it more realistic. The king has no escape squares—g8 is controlled by the knight, g7 is attacked by the rook on h7, and h7 itself is occupied by the rook and defended by the knight on f6, so the king cannot capture. With no other pieces to block or intervene, it's checkmate. This is the Arabian Mate pattern, where a rook and knight coordinate to trap the king on the back rank.

For Damiano's Mate, the queen typically delivers the final blow with support from another piece like a pawn or bishop. I can construct a position with Black's king on g8 and pawns on f7 and h7 to restrict movement, then place White's queen on h3 where it can move to h8 for checkmate. After Qh8+, the king is in check with no legal moves available. The bishop on a1 can't protect h8 because the diagonal is blocked by Black's pawn on g7. I need a different defender—a rook on the h-file works. With Qh3-h8#, if the king captures on h8, the rook on h1 defends the queen along the file. The king can't escape to f8 since the queen controls that square on the 8th rank.

But let me reconsider what Damiano's Mate actually is. The classic pattern involves a queen sacrifice that forces the king into a mating net, typically with the final mate delivered by a supporting piece like a pawn or bishop. For a pure queen mate in one, I should construct a position where the queen delivers checkmate directly with proper support.

A cleaner setup: Black king on g8 with pawns on f7 and h7, White queen on h6 and a pawn on f6. Playing Qg7# works because the queen gives check, the king can't move to f8 or h8 (both controlled by the queen), and if the king tries to capture on g7, the f6 pawn defends it. No blocks are available, so it's checkmate.

The position is 6k1/5p1p/5PQ1/8/8/8/8/4K3 with Qg7#.

Now I need seven distinct mating patterns. I have back rank mate, smothered mate, Fool's mate, Anastasia's mate, Arabian mate, and this queen-pawn mate. For the seventh, I should use something different from the queen-g7 pattern I already have. An Epaulette Mate would work well—where the king is trapped by its own pieces flanking it, and the queen delivers mate on the file or diagonal. With the king on e8 and rooks on d8 and f8, a queen move to e8 would be checkmate since the king has no escape squares and the rooks block d8 and f8 while the queen controls the diagonals. Kd8 and Kf8 are blocked by Black's own rooks. For Kxe8, I need the queen defended—a white rook on e1 would protect it along the e-file.

The position would be: Black king on e8 with rooks on d8 and f8, White queen on a4 and rook on e1. After Qe8#, the king has no legal moves since d7 and f7 are controlled by the queen, the back rank squares are occupied, and capturing the queen loses to the rook. However, Black's rooks can also capture on e8, so I need to verify this doesn't provide an escape.

To prevent Rxe8, I could pin the d8 rook with another piece, though positioning this correctly requires careful setup. The Epaulette pattern typically features the king trapped on the back rank by its own pieces, with mate delivered along the front rank.

Let me try: King on e8, Black rooks on d8 and f8, White Queen on e4. If Qe8 is checkmate, the queen gives check while the king cannot escape to d7 or f7 (controlled by the queen), cannot move to d8 or f8 (occupied by its own rooks), and cannot capture the queen if it's protected. Adding a White Rook on e1 would defend the queen on e8, but after Rdxe8, Rxe8+ just continues the sequence rather than delivering mate in one move. piece can recapture. But this approach is getting tangled.

Let me try a cleaner setup. In Epaulette Mate, the queen typically delivers check from a diagonal where the rooks can't intervene. If I position the king on e8 with rooks on d8 and f8, and place the queen on a4, then Qa4-e8+ gives check along the diagonal. The rooks flanking the king can't capture on e8 since they move only along ranks and files. That's the key—the queen's attacking line bypasses the rooks' defensive capabilities. is on the d-file while the king sits on e8, so there's no pin along that file. To create a pin, I'd need the attacking piece, the rook, and the king all on the same line—like having a rook on e1 pinning a piece on e4 to a king on e8. But that setup doesn't work with my current check scenario.

Let me simplify and try a different approach for scenario 2. I'll set up a position where the queen delivers mate with knight support instead. If I place the queen on f6 and knight on h6, the queen can move to g7 for checkmate. With the king on g8 and the rook already on h8 blocking escape, this creates a cleaner mating pattern.

After Qg7#, the king has no legal moves—h8 is blocked by its own rook and also attacked by the queen along the diagonal, f8 is controlled by the queen, and capturing the queen fails because the knight on f5 defends g7. The FEN position is 6kr/6p1/5Q2/5N2/8/8/8/4K3 w - - 0 1, with the Black king on g8, rook on h8, and pawn on g7. White's queen on f6 and knight on f5 deliver checkmate with Qxg7#. The queen captures the pawn with check, and the king has no escape—f8 and h8 are both controlled by the queen, while g7 itself is defended by the knight, making it an illegal capture. k/6pp/8/6N1/8/8/8/4K3 w - - 0 1, Nf7#
4. Scholar's Mate style (for White): rnbqkbnr/ppppp2p/5p2/6p1/3PP3/8/PPP2PPP/RNBQKBNR w KQkq - 0 3, Qh5#
5. Anastasia's Mate: 8/4N1pk/6p1/8/8/8/8/R4K2 w - - 0 1, Rh1#
6. Arabian Mate: 7k/6R1/5N2/8/8/8/8/4K3 w - - 0 1, Rh7#
7. Queen and Pawn Mate (

Damiano style): 6k1/5p1p/5PQ1/8/8/8/8/4K3 w - - 0 1, Qg7#

I should verify each position carefully. The back rank mate has the rook on e1 with the king trapped on g8 by its own pawns. Scholar's mate works because the queen delivers checkmate on h5 after the f-pawn advances. Anastasia's mate uses the knight and rook in coordination—the knight controls escape squares while the rook delivers mate. The Arabian mate combines rook and knight similarly, with the rook on h7 and knight on f6 controlling key squares around the trapped king. For the Damiano pattern, the queen on g7 is mate with the pawn on f6 supporting it and the king boxed in on g8. 6 empty, N on g5, 1 empty ✓
   - Ranks 4-2: empty ✓
   - Rank 1: 4 empty, K on e1, 3 empty ✓
Move: Nf7# ✓

4. Scholar's Mate style:
   FEN: rnbqkbnr/ppppp2p/5p2/6p1/3PP3/8/PPP2PPP/RNBQKBNR
   Let me verify the position:
   - Rank 8: pieces on a8-h8 (r, n, b, q, k, b, n, r) ✓
   - Rank 7: pawns on a7-

e7, gaps at f7-g7, pawn on h7 ✓
   - Rank 6: five empty squares, pawn on f6, two empty ✓
   - Rank 5: six empty, pawn on g5, one empty ✓
   - Rank 4: three empty, white pawns on d4 and e4, three empty ✓
   - Rank 3: all empty ✓
   - Rank 2: white pawns on a2-c2, gaps at d2-e2, pawns on f2-g2-h2 ✓
   - Rank 1: back rank pieces starting with R

, then N, B, Q, K, B, N, R ✓
   Move: Qh5# ✓

5. Anastasia's Mate:
   FEN: 8/4N1pk/6p1/8/8/8/8/R4K2
   - Rank 8: empty ✓
   - Rank 7: four empty, knight on e7, gap, pawn on g7, king on h7 ✓
   - Rank 6: six empty, pawn on g6, one empty ✓
   - Ranks 5-2: all empty ✓
   - Rank 1: rook on a1, four empty squares, king on f1, two empty ✓
   Move: Rh1# (rook delivers mate along the h-file) ✓

6. Arabian Mate:
   FEN: 7k/6R1/5N2/8/8/8/8/4K3
   - Rank 8: seven empty, king on h8 ✓
   - Rank 7: six empty, rook on g7, one empty ✓
   - Rank 6: five empty, knight on f6, two empty ✓
   - Ranks 5-2: empty ✓
   - Rank 1: four empty, king on e1, three empty ✓
   Move: Rh7# ✓

7. Queen and Pawn Mate

:
   FEN: 6k1/5p1p/5PQ1/8/8/8/8/4K3
   - Rank 8: six empty, king on g8, one empty ✓
   - Rank 7: five empty, pawn on f7, one empty, pawn on h7 ✓
   - Rank 6: five empty, pawn on f6, queen on g6, one empty ✓
   - Ranks 5-2: empty ✓
   - Rank 1: four empty, king on e1, three empty ✓
   Move: Qg7# ✓

All positions verified correctly!

Actually, I need to reconsider—the queen sits on g6, not h6. Let me verify the checkmate works from there.

The queen moves from g6 to g7, delivering check to the king on g8. The king has no escape: f8 and h8 are both controlled by the queen on g7 diagonally, f7 and h7 are blocked by pawns, and capturing on g7 is impossible since the f6 pawn defends it. This is indeed checkmate.

All seven scenarios appear to produce valid mate-in-1 positions.