The user wants me to describe 3 mate-in-1 scenarios for white. Each scenario needs:
1. A name
2. FEN notation for the setup
3. The winning move for white

Let me think of 3 distinct and valid mate-in-1 puzzles.

**Scenario 1: Back Rank Mate**
A classic scenario where the white rook delivers checkmate on the back rank because the king is trapped by its own pawns.

Setup: Black king on g8, black pawns on f7, g7, h7. White rook on e1.
Let me work out the FEN:
- Rank 8: 6k1 (king on g8)
- Rank 7: 5ppp (pawns on f7, g7, h7)
- Other pieces: White rook, white king

Let me make a proper position:
Black: King on g8, pawns on f7, g7, h7
White: Rook on e1, King on g1 (or somewhere safe)

FEN: 6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1

Move: Re8# (Rook to e8 is checkmate)

Let me verify: King on g8, rook moves to e8. The king can't move to f8 (controlled by rook), h8 (controlled by rook), h7 blocked by pawn, g7 blocked by pawn, f7 blocked by pawn. Yes, this is mate.

**Scenario 2: Queen and King Mate (simple)**
Let me think of another classic: 

Scholar's Mate position or a simple queen mate.

How about: Black king on h8, White queen on g6, White king somewhere.
Queen to h7 is mate? Let's see:
- King on h8
- Queen moves to h7, checks the king


- King can't go to g8 (queen controls it from h7 diagonally)
- King can't stay on h8 (in check)

This works as mate. Let me set up the position properly with the queen positioned to deliver this in one move. I need to place the queen where it can reach h7 in one move. Queen on g6 works perfectly.

FEN: 7k/8/6Q1/8/8/8/8/6K1 w - - 0 1

Move: Qh7# (Queen to h7 is checkmate)

**Scenario 3: Smothered Mate**
A knight delivers mate while the king is blocked by its own pieces.

Black: King on h8, pawns on f7, g7
White: Knight on f6, King on e1

The knight moves to g8, giving check. The king on h8 has no escape squares because g8 is occupied by the knight, g7 and f7 are blocked by pawns, and h7 is controlled by the knight on g8.

FEN: 6k1/5pp1/5N2/8/8/8/8/4K2 w - - 0 1

Move: Ng8# (Knight to g8 is checkmate) I need to work through a clean smothered mate setup. The king on g8 needs to be boxed in by its own pieces—a rook on f8, pawns on g7 and h7, and another piece on h8. Then a knight can deliver mate from f6, since the king has no escape squares and can't capture the knight. Let me reconsider the FEN setup. Rank 8 has a rook on f8, king on g8, and rook on h8, which gives us 5rkr. Rank 7 has pawns on g7 and h7, so that's 6pp. The position is 5rkr/6pp/8/8/8/8/8/6K1, and I need to place the white knight to find mate in one.

If the knight lands on f7 with check, the king on g8 has no escape—h8 and f8 are blocked by rooks, and h7 is occupied by its own pawn. That's checkmate.

But wait, can the king simply capture the knight on f7? I need to protect that square. Adding a white queen on c4 controls the f7 diagonal, so if Nf7 is played, the king cannot take the knight because it's defended. This gives us the mate in one: the knight moves to f7, delivering checkmate. The knight on f7 delivers checkmate since the queen on c4 guards it along the diagonal, preventing the king from capturing.

Now considering a simpler mating pattern with just a queen. If the black king sits on f8 with no defenders, the queen from a3 could potentially reach f8 via the diagonal a3-b4-c5-d6-e7-f8, though I need to verify the exact positioning works for a clean mate.

Actually, let me focus on a concrete example: placing the black king on a1 with a white rook on b3 and white king on c3. Moving the rook to b1 gives check, and since the king cannot escape to a2 (controlled by the rook), this creates a mating net.

I can set this up with two rooks—one on a2 to control the escape square, and one delivering check from b1. The position would have the black king trapped on a1 with white rooks on a2 and b3, and the white king somewhere like e3 for support.

When Rb1# is played, the king has no legal moves: a2 is covered by Ra2, b2 is controlled by the rook now on b1, and b1 itself is occupied. That's checkmate.

For the back rank scenario, Re8# works because the rook on e8 gives check to the king on g8 while controlling both escape squares f8 and h8. The pawns on f7, g7, and h7 block any other retreat, leaving the king with no legal moves.

Now checking the second position more carefully. The FEN 5rkr/6pp/7N/8/2Q5/8/8/6K1 places Black's king on g8 with rooks on f8 and h8, pawns on g7 and h7, White's queen on c4, knight on h6, and king on g1. I need to verify the piece placement is correct before analyzing potential moves.

The knight move Nf7 delivers checkmate. The Black king on g8 cannot escape because all adjacent squares are either occupied by Black's own pieces (rooks on f8 and h8, pawns on g7 and h7) or controlled by White's queen on c4, which guards f7 along the diagonal. The knight itself cannot be captured since the queen protects it.

For Scenario 3, I'm verifying the position from the FEN string. Rank 3 shows 1R2K3, which means one empty square on a3, a rook on b3, two empty squares, the White king on e3, and three more empty squares through h3.

Rb1# delivers checkmate—the rook moves from b3 to b1, giving check to the Black king on a1. The king has no escape: a2 is controlled by the rook on a2, b2 is controlled by the rook on b1, and b1 itself is occupied by the attacking rook.

The three mating patterns I've identified are: a back rank mate with Re8#, a knight mate on f7# supported by the queen, and the double rook mate with Rb1#. For the second scenario, the knight on f7 is protected by the queen while the king sits trapped by its own pieces on f8, h8, g7, and h7—this differs from a pure smothered mate where the knight would be undefended, relying solely on the king's own pieces to prevent escape. the knight must be protected for this to work as mate. If the knight on f7 sits undefended, the king simply captures it. So in a true smothered mate, either a queen guards f7, or another piece controls that square, preventing the king from taking the knight while all escape squares remain blocked by the king's own pieces.

I should probably construct a clearer example—perhaps using the classic pattern where a queen sacrifices itself to force the rook to g8, then a knight delivers mate on f7. Or I could look at Philidor's Legacy, which is a well-known smothered mate pattern.

Let me work through Philidor's Legacy: After 1. Nf6+ Kh8 2. Qg8+! Rxg8 3. Nf7#, the king on h8 is trapped. The rook on g8 blocks one escape square, the g7 pawn blocks another, and the h7 pawn prevents Kh7. The knight on f7 delivers checkmate since the king cannot capture it or move anywhere else. I need to verify the knight can deliver checkmate from f7. A knight on f7 attacks h8 via the (2,1) offset, confirming it gives check to a king trapped there. The rook on g8 and pawns on g7 and h7 block all escape squares, making it mate.

For the position, I can place the knight on e5 where it can reach f7 in one move—the (1,2) offset gets there. With Black's king on h8, rook on g8, and pawns on g7 and h7, White just needs a king (say on g1) to complete a legal position.

The FEN breaks down as: rank 8 has the rook and king on the kingside, rank 7 has the two pawns, rank 5 has the knight on e-file, and rank 1 has White's king on g-file.

Nf7 delivers checkmate. The knight from e5 moves to f7, giving check to the king on h8. The king cannot escape—g8 and g7 are blocked by Black's own rook and pawns respectively, h7 is also blocked by a pawn, and the king cannot capture the knight since f7 is two squares away diagonally, beyond the king's one-square movement range.

This is a smothered mate pattern. I've now identified two complete scenarios: a back rank mate with Re8# and this smothered mate with Nf7#.

For the third scenario, I'm working with a ladder mate setup where the rooks coordinate to deliver checkmate on b1. The position has the black king on a6 trapped by white's rooks on b3 and a7, with the move Rb1# delivering mate since the king has no escape squares.

Now checking scenario 2 more carefully. The knight from e5 can legally move to f7, and from there it controls h8 where the black king sits—that's check. From f7, the knight's available squares include g5, e5, h6, d8, and d6, with h8 being the critical attacking square. The king on h8 is now in check and needs to find a legal move.

Looking at escape squares: g8 has the rook, g7 and h7 both have pawns. Every adjacent square is blocked by Black's own pieces, so the king has no legal moves. This confirms checkmate for scenario 2.

For scenario 3, I need to verify the position more carefully. Black's king sits on a1, White has rooks on a2 and b3, and the White king is on e3. Translating to FEN notation: rank 1 shows the black king at a1 with the rest empty, rank 2 has a White rook on a2, and rank 3 has a White rook on b3 with the White king on e3.

The full position in FEN is 8/8/8/8/8/1R2K3/R7/k7 w - - 0 1. The move Rb1# delivers checkmate because the rook controls a2 while the b1 rook gives check, leaving the king with no escape squares.

Wait—I need to reconsider whether the king can capture the rook on a2. The rook there isn't defended by the rook on b1, since b1 only controls the b-file and first rank. So if the king takes on a2, is it actually protected? The rook on b1 doesn't control a2 since that square isn't on the b-file or first rank, leaving the rook on a2 undefended. This means the king can simply capture it with Kxa2, so Rb1+ is just check, not mate.

I need to reconfigure this. Either I protect a2 with another piece, or I try a completely different setup. Let me test: Black king on a3, White rooks on a4 and b8, White king on c1. If I play Rb3, does that deliver checkmate?

The king on a3 would be in check from the rook on b3. Looking at escape squares: Ka4 is blocked by the rook there, Kb2 is controlled by the rook on b3 along the b-file, and Kb4 is controlled by the rook on a4 along the fourth rank. But wait—is the rook on a4 actually protected? The rook on b3 can't reach a4 directly, so it's undefended and the king could capture it. King captures the rook.

This is getting too tangled. Let me try a different setup.

**Revised Scenario 3: Queen and King Mate in Corner**

Black: King on h8
White: Queen on f6, King on f8

Actually, that doesn't work—the white king would be occupying f8. Let me adjust.

Black: King on h1
White: Queen on g3, King on f1

If I play Qg1#:
King on h1, queen moves to g1. From g1, the queen controls the g-file, first rank, and diagonals including h2. When the king tries h2, is that square covered?

Yes—the diagonal from g1 reaches h2. The king can't escape there. If Black captures the queen with Kxg1, the white king on f1 is right next to g1, so the queen is defended.

That's checkmate: the queen gives check, h2 is controlled, and the queen is protected.

The FEN would be: ranks 8 through 4 are empty, rank 3 has the queen on g-file, rank 2 is empty, and rank 1 has the white king on f-file and black king on h-file.

FEN: 8/8/8/8/8/6Q1/8/5K1k w - - 0 1

Move: Qg1#

Verify:
- Queen on g3 moves to g1.
- Black king on h1 is in check.
- Kh2: Queen on g1 attacks h2 (diagonal). ✓
- Kxg1: Queen protected by king on f1 (f1 adjacent to g1). ✓

So my final three scenarios are:

**Scenario 1: Back Rank Mate**
FEN: 6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1
Move: Re8#

**Scenario 2: Smothered Mate**
FEN: 6rk/6pp/8/4N3/8/8/8/6K1 w - - 0 1
Move: Nf7#

**Scenario 3: Queen and King Mate**
FEN: 8/8/8/8/8/6Q1/8/5K1k w - - 0 1
Move: Qg1#

Let me verify once more:

Scenario 1:
- Position: White king g1, white rook e1, black king g8, black pawns f7, g7, h7.
- Move: Re8#
- Verification: Rook delivers check on e8. King on g8 can't escape: f8/h8 controlled by rook, f7/g7/h7 blocked by own pawns. ✓

Scenario 2:
- Position: White king g1, white knight e5, black king h8, black rook g8, black pawns g7, h7.
- Move: Nf7#
- Verification: Knight gives check on f7. King on h8 has no escape squares: g8 occupied by rook, g7/h7 blocked by pawns, and the knight controls all available moves. ✓

Scenario 3:
- Position: White king f1, white queen g3, black king h1.
- Move: Qg1#
- Verification: Queen delivers check on g1. King on h1 is trapped: h2 is controlled by the queen on the diagonal, and g1 is occupied by the queen and protected by the white king on f1. ✓

All three scenarios deliver checkmate.

The queen on g1 controls the critical escape squares: g2 via the g-file, h2 along the diagonal, and f2 through the long diagonal. With the king trapped on h1 and no legal moves available, it's checkmate.

**Scenario 3: King and Queen Mate**
FEN: 8/8/8/8/8/6Q1/8/5K1k w - - 0 1
Move: Qg1#