The user wants me to describe 7 mate-in-1 scenarios for white. Each scenario should be in its own code block with:
1. Name of the scenario
2. FEN notation
3. Winning move

Let me think of 7 distinct mate-in-1 patterns:

1. **Back Rank Mate** - A rook or queen delivers checkmate on the back rank when the king is trapped by its own pawns.

Let me create a valid position:
- Black king on g8, pawns on f7, g7, h7
- White rook on e1, can move to e8 for mate

FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1
Move: Re8#

Wait, let me verify: Black king on g8, pawns on f7, g7, h7. White rook on e1, white king on h1.
After Re8+, the king on g8 is attacked, and it can't move to f8 (rook controls), h8 (rook controls), h7 is blocked by pawn, g7 blocked by pawn, f7 blocked by pawn.
That works!

2. **Scholar's Mate / Queen and Bishop Mate** - Queen delivers mate supported by bishop

Let me think of a position:
- Black king on e8
- White queen can go to f7 with bishop support

Position: Black king e8, some pieces blocking escape
White queen on h5, bishop on c4
After Qxf7#, the king is mated

Actually let me be more careful:
- Black king on e8
- White queen on h5, can go to f7
- White bishop on c4 supports f7
- Black has no pieces that can block or capture

FEN: 4k3/8/8/7Q/2B5/8/8/4K3 w - - 0 1


Move: Qf7#

After Qf7#: King on e8 is attacked by queen on f7, which is protected by bishop on c4. But I need to verify all escape squares are covered. The king could potentially escape to d8 or d7, which aren't controlled by the queen on f7. I need to adjust the position so the bishop covers those squares instead. Let me place the bishop on b5 to control d7 and the long diagonal, then position the queen to deliver mate while ensuring d8 is also covered.

I should work through some concrete mating patterns instead. Back rank mates are reliable: if Black has a king on g8 with pawns on f7, g7, h7, and I have a rook on d8, that's checkmate since the king has no escape squares. For a queen-based mate, I could place the king on h8 with a pawn on g7, then deliver Qg8# where the queen controls all escape squares and the pawn blocks the king's retreat.

Let me verify a specific position: Black king on h8, White queen on f6 with a pawn already advanced to g7. Playing Qf8# works because the queen attacks both h7 and g8, leaving the trapped king no legal moves.

Actually, checking the queen's coverage from f8—it controls the entire 8th rank including h8, and the diagonal toward h6 is blocked by the pawn on g7. That means h7 remains undefended, which breaks the mate. I need to ensure all escape squares are covered, so I should look for a different piece placement or move sequence. I need to find a position where a queen can deliver checkmate on a protected square. Let me reconsider the setup with the king on f8 instead, where the queen can move to deliver mate while being protected or controlling all escape squares.

For a smothered-adjacent pattern, I should place the king where its own pieces restrict its movement, then have the queen move to a square where it gives check and controls all flight squares. The queen on a3 with the king on f8 needs adjustment—I need to ensure the queen can reach a mating square and that escape routes are properly covered. Queen on a6 controls the a-file, 6th rank, and both diagonals including b7. The king on a8 has no escape: b8 is covered by the rook on h8, b7 is controlled by the queen, and a7 is blocked by its own pawn. This is checkmate with Qa6#.

The FEN position checks out—black king and pawn on the a-file, white queen on b6, rook on h8, and white king on h1 with the remaining squares empty.

For the next pattern, I'm setting up a back rank mate scenario with the rook. The black king goes on g8 with pawns on f7, g7, and h7 to restrict its movement, while white has a rook on a1 and king on h1.

Ra8 delivers checkmate since the rook controls both f8 and h8, and the pawns seal off f7, g7, and h7. Now I need to construct a queen and king mate pattern. A king on a8 with white's queen on b6 and king on c6 works—Qa7 is mate because the queen gives check and controls b8 while the white king covers b7. Queen on a7 attacks the entire a-file, the 7th rank, and both diagonals from that square. So the queen controls a8 (on the file), b8 (diagonal), b7 (on the rank), and b6 (diagonal). The black king on a8 has no legal moves—b8 and b7 are both covered by the queen, and a7 is occupied by it.

Wait, I need to verify b7 more carefully. The 7th rank runs from a7 to h7, so yes, b7 is attacked. That means Qa7 is actually mate.

Let me explore a different pattern instead. What if I use a queen and knight together? If the queen sits on g7 with a knight on f7, the king on g8 would be in check. The escape squares are f8 (controlled by the knight), h8 (controlled by the queen), f7 (the knight, but protected by the queen since they're adjacent), and h7 (blocked by a pawn). That's checkmate.

The position would be: Black king g8, black pawn h7, white queen h6, white knight f7, white king a1. After Qg7#, all escape routes are sealed.

I should also consider the smothered mate pattern, where a knight delivers mate against a king trapped by its own pieces. The FEN position 5rk1/6pp/7N/8/8/8/8/K7 w - - 0 1 with Nf7# works perfectly. The knight on h6 delivers checkmate on f7, where the king on g8 has no escape—the rook on f8 and pawns on g7 and h7 block three squares, while the knight controls h8.

Now considering a bishop and rook mating pattern: I need a position where these pieces work together. Black king on h8 with a rook on a8 and bishop on e5 could create a back rank mate threat, though I'm still working through the exact configuration. is blocked by pawn ✓

So that's mate. Let me verify: King on h8 is checked by Ra8, can't move to g8 (rook controls it), g7 is blocked by its own pawn, and h7 is blocked by its own pawn. That works as a mate-in-1.

Now I'm exploring if there's a more interesting diagonal mate pattern. With King on g8, pawn on f7, and pawn on h7, I'm checking whether a bishop on a2 can deliver mate by capturing on f7. The bishop would give check, but the king would have escape squares like f8 and h8 that aren't controlled, so this doesn't work as mate.

Let me shift to examining the Opera Mate pattern with a rook and bishop combination. I'm testing positions where a rook on d8 and bishop on b7 could work, though I need to be careful about the setup—having the bishop on b7 already gives check to a king on a8, so I need to reconfigure the pieces to find a genuine mate-in-one scenario.

After adjusting, I can place the king on a8, a knight blocking on b8, and a pawn on a7. With a rook moving to d8 and a bishop on c6, this creates mate: the king is in check from the rook, the knight blocks b8, the bishop controls b7, and the pawn seals a7. The FEN is kn6/p7/2B5/8/8/8/8/3R3K with Rd8# delivering mate.

Now exploring a different pattern with two rooks. If I place the black king on f8 with a white rook on a8 giving check, I need to verify escape squares—e8 and g8 are covered by the rook, but e7, f7, and g7 remain open. I'd need another rook controlling the 7th rank to complete the mating net.

Repositioning: Black king f8, white rooks on a7 and h1. Playing Rh8# delivers mate since the king is in check from h8, all escape squares (e8, g8, e7, f7, g7) are controlled by the rooks on h8 and a7. The FEN is 5k2/R7/8/8/8/8/8/R6K w - - 0 1, though I notice there's only one forcing move available here. Let me carefully map out the position:

Rank 1 has the white king on g1 and rook on h1, which gives "6KR" in FEN notation. The full position is 5k2/R7/8/8/8/8/8/6KR w - - 0 1, and Rh8# is checkmate since the rook controls the eighth rank while the king on g1 prevents any escape squares.

I should also consider other mating patterns like the Epaulette Mate, where a queen delivers the final blow.

In this setup, Black has rooks on d8 and f8 flanking the king on e8, while White has a queen on e6 and king on a1. Playing Qe7# works because the queen gives check, the rooks block d8 and f8, and the queen controls d7 and f7—all escape squares are covered. The position converts to FEN as 3rkr2/8/4Q3/8/8/8/8/K7 w - - 0 1.

For Damiano's Mate, the position has Black's king on g8 with a pawn on h7, and White's queen on f7 with a pawn on g6. After Qg7#, the king is in check with h8 and f8 controlled by the queen, h7 blocked by Black's own pawn, and f7 attacked diagonally by the queen on g7—leaving no legal moves. The queen move to g7 delivers checkmate. After Qg7+, the king on g8 is in check and has no legal moves—f7 and f8 are both controlled by the queen along the rank and diagonal respectively, h8 is attacked along the rank, and h7 is blocked by Black's own pawn. The h7 pawn cannot capture on g7 since pawns don't move backward. So the h7 pawn can only capture on g6, not g7 since that's on the same rank. There is a white pawn on g6, which works for this pattern.

Let me reconsider the classic Damiano's mate setup. The typical configuration has a black king trapped on h8 with a white queen delivering checkmate, usually supported by a pawn. My current position should work—let me verify the FEN notation and confirm the final move delivers mate. Qg7 is indeed checkmate—the queen controls all escape squares (h8, f8, f7) while the h7 pawn blocks that square. The move is legal since g7 is empty, and the resulting position with just the queen on f7, king on g8, and pawn on h7 delivers mate without needing the g6 pawn.

I notice this resembles Pattern 4 from my earlier analysis, so I should verify all seven patterns remain distinct. Looking at what I've identified: Back Rank Mate with a rook, Smothered Mate with a knight, Opera Mate using rook and bishop, Ladder Mate with two rooks, Epaulette Mate, and a queen mate with support. Some of these overlap—Qg7# appears in multiple contexts, and the back rank patterns share similar mechanics. I need to consolidate these into seven truly different mating patterns, each with its own unique characteristics and piece configuration. 7. **Queen and Pawn Mate / Support Mate** - Queen delivers mate with pawn support
FEN: 6kp/6p1/5Q2/8/8/8/K7 w - - 0 1
Move: Qf8#

The queen on f8 gives check to the king on h8, with g8 controlled by the queen. The pawn on g7 blocks the h7 escape square, trapping the king. empty squares, black pawn g7, black pawn h7 ✓
5Q2 = 5 empty squares, white queen f6, 2 empty ✓
K7 = white king a1, 7 empty ✓

The position works: Queen on f8 delivers mate since the king on h8 has no escape squares—g8 is controlled by the queen, while both g7 and h7 are blocked by pawns.

FEN: 7k/6pp/5Q2/8/8/8/8/K7 w - - 0 1
Move: Qf8#

My seven mating patterns are:

1. **Back Rank Mate**
FEN: 6k1/5ppp/8/8/8/8/8/R6K w - - 0 1
Move: Ra8#

2. **Smothered Mate**
FEN: 5rk1/6pp/7N/8/8/8/8/K7 w - - 0 1
Move: Nf7#

3. **Queen and Knight Mate (Suffocation Mate)**
FEN: 6k1/5N1p/7Q/8/8/8

/8/K7 w - - 0 1
Move: Qg7#

4. **Opera Mate**
FEN: kn6/p7/2B5/8/8/8/8/3R3K w - - 0 1
Move: Rd8#

5. **Ladder Mate (Lawn Mower Mate)**
FEN: 5k2/R7/8/8/8/8/8/6KR w - - 0 1
Move: Rh8#

6. **Epaulette Mate**
FEN: 3rkr2/8/4Q3/8/8/8/8/K7 w - - 0 1
Move: Qe7#

7. **Kill Box Mate**
FEN: 7k/6pp/5Q2/8/8/8/8/K7 w - - 0 1
Move: Qf8#

I need to rename #3 since I had duplicated "Suffocation Mate" with #7. Calling it "Arabian Mate" instead.

Now let me verify each position works. For the back rank mate, the rook delivers check from a8 with the king trapped on g8 by its own pawns on f7, g7, and h7. The smothered mate has the knight on h6 delivering mate to a king on g8 that's blocked in by its own rook on f8 and pawns on g7 and h7.

For the Arabian mate, I need to reconsider the setup since I already placed the knight on f7 in the position. The queen on h6 can move to g7 to deliver mate, but I should verify this configuration actually works with those pieces.

The queen move to g7 gives check to the king on g8. The escape squares are all covered: h8 is controlled by the queen along the rank, f8 is controlled by the knight, h7 is blocked by Black's own pawn, and f7 is occupied by my knight which the queen protects. That's mate.

For the Opera mate pattern, a rook moves from d1 to d8 to check the king on a8. The knight on b8 blocks one escape square, and the bishop on c6 controls b7, leaving no legal moves.

The Ladder mate uses a rook on h1 moving to h8 to deliver check to the king on f8, with all escape squares (e8, g8, and the seventh rank) covered by the rooks on h8 and a7.

In the Epaulette mate, the queen moves to e7 to give check to the king on e8, with the rooks on d8 and f8 blocking the adjacent escape squares.

For the Corridor mate, the queen delivers checkmate from f8 against a king trapped on h8 by its own pawns on g7 and h7, which prevent any retreat.

Let me verify these positions could actually occur in real games.

Back Rank Mate, Smothered Mate, Arabian Mate, and Opera Mate are all well-established patterns that arise regularly in play. Ladder Mate represents a standard endgame technique, Epaulette Mate shows how a king's own pieces become liabilities, and Corridor Mate is typical when a king gets trapped on the edge of the board. All seven positions are genuinely achievable.