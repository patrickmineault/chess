The user wants me to describe 5 mate-in-1 scenarios for white. Each scenario should be in code fences with:
1. Name of the scenario
2. FEN notation
3. Winning move for white

Let me think of 5 distinct mate-in-1 positions.

**Scenario 1: Back Rank Mate**
A classic where a rook or queen delivers mate on the back rank when the king is trapped by its own pawns.

Setup: Black king on g8, pawns on f7, g7, h7. White rook on e1, can move to e8.
FEN: Let me construct this properly.
- Black king on g8
- Black pawns on f7, g7, h7
- White rook on e1
- White king somewhere safe, say a1

FEN: 6k1/5ppp/8/8/8/8/8/R3R2K w - - 0 1

Wait, let me be more careful. FEN notation goes from rank 8 to rank 1, and from file a to h.

Rank 8: 6k1 means 6 empty squares, king on g8, 1 empty square
Rank 7: 5ppp means 5 empty squares, pawns on f7, g7, h7
Rank 6-2: all empty (8/8/8/8/8)
Rank 1: R3R2K means rook on a1, 3 empty, rook on e1, 2 empty, king on h1

Actually let me simplify:
- Black king on g8
- Black pawns on f7, g7, h7
- White rook on e1
- White king on h1

FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1

Winning move: Re8# (Rook from e1 to e8, checkmate)


The rook moves to e8 delivering mate—the king on g8 has no escape since f8 and h8 are controlled by the rook, while f7, g7, and h7 are blocked by its own pawns.

**Scenario 2: Scholar's Mate pattern**
Queen delivers mate on f7 (or similar weak point).

Setup: Black king on e8, queen can deliver mate on f7 with bishop support.
- Black king on e8
- White queen on h5 (can go to f7)
- White bishop on c4
- White king on e1

FEN: 4k3/8/8/7Q/2B5/8/8/4K3 w - - 0 1

Winning move: Qf7# - the queen moves to f7 protected by the bishop on c4, giving checkmate since the king cannot escape or capture the queen.

Actually, let me reconsider. If the king is on e8 and the queen moves to f7, the king can escape to d8. That's not mate. I need to set up a position where the queen on f7 truly traps the king.

Let me try a different approach: Black king on h8, pawns on g7 and h7, White queen on f6.

FEN: 7k/6pp/5Q2/8/8/8/8/4K3 w - - 0 1

From here, Qf8# works—the queen gives check from f8, and the king cannot move to g8 (controlled by the queen), h7 (blocked by pawn), or g7 (blocked by pawn).

**Scenario 3: Smothered Mate**
A knight delivers mate when the king is completely surrounded by its own pieces.

Classic setup: Black king on g8, rooks on f8 and h8, pawns on g7 and h7, White knight on h6.

FEN: 5rkr/6pp/7N/8/8/8/8/4K3 w - - 0 1

Move: Nf7# - the knight jumps to f7 giving check. The king cannot escape because f8 and h8 are blocked by rooks, g7 and h7 are blocked by pawns, and the knight on f7 also controls h8.

**Scenario 4: Two Rooks Mate (Ladder Mate)**
One rook cuts off escape squares while the other delivers mate.

Setup: Black king on a8, White rook on b7 controlling the 7th rank, White rook on c1 ready to move.

FEN: k7/1R6/8/8/8/8/8/2R1K3 w - - 0 1

Move: Rc8# - the rook moves to c8 giving check along the 8th rank. The king cannot go to b8 (controlled by the rook on c8), a7 (controlled by the rook on b7), or b7 (occupied).

**Scenario 5: Queen and King Mate**
The White king and queen work together to trap the Black king.

Setup: Black king on h8, White king on f7, White queen on g1.

FEN: 7k/5K2/8/8/8/8/8/6Q1 w - - 0 1

Move: Qg8# - the queen moves to g8 giving check. The king cannot move to h7 (attacked by both queen and king), g7 (attacked by both), or g8 (occupied by queen).

I've now constructed five distinct mating patterns: back rank mate with a rook, queen delivering mate on the back rank, smothered mate with a knight, ladder mate with two rooks, and queen-king coordination mate. Each demonstrates a different tactical principle and piece coordination. The bishop on a6 controls b7 and c8, while the bishop positioned on g1 covers the b6 escape square. If the king tries to move from c8 after being checked, b8 becomes the critical square to monitor.

A bishop on h2 works perfectly here—it commands the long diagonal through b8 and c7, preventing the king from escaping in those directions. With the black king trapped on c8, a black pawn blocking d7, and a black rook on d8, the white bishops on a6 and h2 deliver checkmate: the king cannot move to b8 (controlled by h2), cannot reach d8 (occupied by its own rook), cannot go to c7 (also controlled by h2), cannot escape to b7 (controlled by a6), and cannot move to d7 (blocked by its own pawn). This is Boden's Mate.

Now I need to construct the FEN. The position has the black king on c8 with a rook on d8 and pawn on d7, white bishops positioned on e2 and h2. Rank 8 reads: two empty squares, then the king, rook, and four empty. Rank 7 has three empty squares, the pawn on d7, then four more empty. The middle ranks are clear. Rank 2 needs the bishop on e2 and bishop on h2—that's four empty, bishop, two empty, bishop.

For rank 1, I'll place the white king on g1: six empty squares, king, one empty.

The resulting position is: 2kr4/3p4/8/8/8/8/4B2B/6K1 w - - 0 1

The winning move is Ba6#, delivering checkmate. Let me verify each rank matches the FEN notation correctly before finalizing.

When the bishop moves from e2 to a6, it gives check along the long diagonal. The black king on c8 has no escape: b8 is controlled by the h2 bishop via the long diagonal, b7 is attacked by the a6 bishop itself, c7 falls to the h2 bishop, and d7 and d8 are blocked by Black's own pawn and rook.

For the second scenario, I'll use Qa8# instead to keep it distinct from the rook mate. Then I should create a third example that's fundamentally different—perhaps a queen delivering mate on g7 with the king trapped on g8 by its own pawn on f7 and rook on f8. h8 (the queen on g7 controls that square diagonally). The king also can't capture on g7 since the queen would be protected. I need to add a piece defending g7—a bishop on b2 works perfectly, controlling the long diagonal through g7.

The corrected position places a white bishop on b2 to protect the queen, making Qg7 a true checkmate since the black king has no legal moves and the queen is untouchable. Queen Mate with Bishop Support**
   FEN: 5rk1/5p2/8/8/6Q1/8/1B6/4K3 w - - 0 1
   Move: Qg7#

3. **Smothered Mate**
   FEN: 5rkr/6pp/7N/8/8/8/8/4K3 w - - 0 1
   Move: Nf7#

4. **Ladder Mate (Double Rook Mate)**
   FEN: k7/1R6/8/8/8/8/8/2R1K3 w - - 0 1
   Move: Rc8#

5. **Boden's Mate**
   FEN: 2kr4/3p4/8/8/8/8/

4B2B/6K1 w - - 0 1
   Move: Ba6#

Let me verify the second position more carefully. The FEN breaks down to a rook on f8, king trapped on g8, and a pawn blocking on f7. The queen on g4 can deliver mate on g7 since the king has no escape squares. me double-check the escape squares more carefully. The king on g8 has f8, h8, f7, and h7 as potential moves. f8 is blocked by the rook, h8 is controlled by the queen on g7, f7 has a pawn, and h7 is also attacked by the queen. No piece can interpose or capture the queen since the bishop on b2 guards it along the long diagonal. This confirms Qg7 is indeed checkmate.

The starting position checks out as legal—the black king isn't in check from the queen on g4 or bishop on b2, and it's white's turn to move. All five scenarios have been verified.

Let me reconsider the smothered mate position more carefully. The knight on h6 moving to f7 should give check to the king on g8, but I need to verify the knight actually attacks that square from f7.

A knight on f7 can reach d6, d8, e5, g5, h6, and h8—it doesn't attack g8 at all. I need to find which squares allow a knight to attack g8: that would be e7, f6, or h6.

If I place the knight on g6, it can move to e7, which does attack g8 (along with c6, c8, d5, f5, and g6). So Ne7 would deliver check to the king. With the king trapped by its own pawns on g7 and h7, and rooks on f8 and h8 blocking escape squares, Ne7 would be checkmate.

But wait—f7 is empty in this position, and the knight on e7 doesn't control it. The king could escape there. I need to add another piece to cover f7, like a bishop on b3.

With a bishop on b3 attacking along the diagonal through f7, Ne7 becomes checkmate. The king on g8 is checked by the knight, can't move to f8 or h8 (blocked by rooks), can't go to f7 (controlled by the bishop), and h7 and g7 are blocked by pawns. This works, though it's no longer a pure smothered mate since the bishop participates in the mating net.

For a true smothered mate, the king needs to be on h8 instead, with the rook on g8 and pawns on g7 and h7. A knight landing on f7 would deliver mate—it attacks h8 and the king has no escape squares. The knight could reach f7 from several squares like h6, e5, or d6.

Using a knight on h6, the position would be: Black king on h8, rook on g8, pawns on g7 and h7, with White's knight on h6 and king on e1. Playing Nf7 is checkmate since the knight controls h8 and the king is boxed in by its own pieces.