The user wants me to describe 7 distinct mate-in-1 scenarios for white. Each scenario should be in code fences with:
1. Name of the scenario
2. FEN notation
3. The winning move for white

Let me think of 7 classic mate-in-1 patterns:

1. **Back Rank Mate** - A rook or queen delivers checkmate on the back rank when the king is trapped by its own pawns.

Let me set up a position:
- Black king on g8
- Black pawns on f7, g7, h7 (trapping the king)
- White rook on e1 (can move to e8 for mate)

FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1

Wait, I need to make sure the white king is also on the board. Let me put it on h1.

FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1

Move: Re8# (or 1. Re8#)

Let me verify: Rook goes to e8, black king on g8 is in check, can't move to f8 (controlled by rook), h8 (controlled by rook), f7/g7/h7 blocked by own pawns. That's checkmate!

2. **Scholar's Mate style / Queen mate on f7** - This is a common pattern where the queen delivers mate on f7.

Setup:
- Black king on e8
- White queen can deliver mate on f7 (supported by bishop on c4)

Actually, let me think of a simpler setup:
- Black king on e8
- Black pieces blocking escape
- White queen delivers mate

Let me try:
- Black king e8
- Black rook on d8
- Black bishop on f8
- White queen on e7 would be mate? No wait, e7 adjacent to e8 means Kxe7 unless protected.


- Black king on e8, no castling rights
- White queen on h5 and bishop on c4
- If f7 is empty or capturable, Qxf7 could be mate if escape squares are controlled

For a clean mate-in-1 here, I need the king boxed in. Let me position: Black Ke8, Qd8, Bf8, pawns on d7 and e7. White Qh5 and Bc4. Then Qxf7 is mate since the king can't escape to d7 (pawn), e7 (pawn), or f8 (queen controls it).

FEN: r1bqkb1r/ppp2ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 0 1

Actually, let me simplify further with just the necessary pieces for mate-in-1. I need to reconsider the position. After 1.e4 e5 2.Bc4 Nc6 3.Qh5, Black has a knight on c6 and a pawn on e5. The queen on h5 threatens f7, but Qxf7+ isn't mate because the king can escape to e7. I'm working through what configuration would actually deliver mate in one move, but I'm constructing the position incorrectly—I keep mixing up which pieces belong to which side and where the pawns sit.

The classic scholar's mate line works: after 1.e4 e5 2.Bc4 Nc6 3.Qh5 Nf6?? 4.Qxf7# is checkmate because the queen on f7 is protected by the bishop on c4, and the king has no escape squares.

For smothered mate, I need the king boxed in by its own pieces so a knight can deliver mate. The typical pattern has the king on g8 with a rook on f8 and pawns on g7 and h7, allowing a knight to jump to f7 for checkmate.

Actually, let me reconsider - if the king is on h8 in the corner with a rook on g8 and pawns blocking, a knight landing on f7 would attack h8 and deliver mate since the king has no escape squares. I can construct this by placing the knight on e5 or h6, then moving it to f7 for the finishing blow. The knight on f7 delivers checkmate—the king on h8 has no escape squares and can't capture the knight. But I need to verify the rooks can't intervene. If a rook sits on f8, it could take the knight, so I should remove it. 

For a clean smothered mate pattern, I need the king boxed in by its own pieces: the rook on g8, pawn on h7, and ideally something controlling g6. The minimal setup requires just the king on h8, a piece on g8, a pawn on h7, and the knight delivering mate from f7.

Testing the position with Black king h8, queen g8, pawn h7, and White knight h6: after Nf7+, the king is in check and truly mated since the queen can't reach f7 from g8.

Let me try replacing the queen with a rook instead. With rook on g8, after Nf7+ the king has no escape—the rook can't move diagonally to capture the knight, and both g8 and h7 remain blocked. That's checkmate.

This demonstrates a classic mating pattern where knight and rook work together to trap the king, particularly effective on the h-file with the king confined to h7 or h8. I need to verify which knight placement actually controls the escape squares. From e5, the knight reaches c4, c6, d3, d7, f3, f7, g4, and g6—so it covers g6 and g4 but leaves g8 open. Repositioning the knight to e7 is better since it controls c6, c8, d5, f5, g6, and g8, which seals off the king's flight squares. With the rook delivering check from h3 or h4 against a king on h7 with only a pawn on g7, the Ne7 placement prevents the king from escaping to g8 or g6.

But wait—h8 and h6 remain available, so this isn't checkmate yet. The classic pattern for this type of position involves a pawn on g6 rather than g7, which would block h6 as well. I should reconsider the exact piece placement to achieve the mating net. The classic pattern has the black king trapped on h7 with a pawn on g7. White delivers mate with a rook on h4 giving check, while a knight on e5 controls the g6 escape square. The king cannot move to g8 (blocked by its own pawn), g6 (controlled by the knight), h8 or h6 (both controlled by the rook on h4).

But that leaves g8 open as an escape. I need an additional piece to cover that square, or there's a different piece arrangement I'm missing. Looking at variations, the setup often includes a black pawn on g6 as well, which would naturally block that escape route rather than requiring the knight to control it.

Let me reconsider the classic pattern: Black king trapped on h7 with pawns on g6 and g7, White knight on e7 controlling the key squares, and a rook delivering mate along the h-file. The position would need the rook to reach h8 or h1 to finish, with the knight ensuring the king has no flight squares.

7 is controlled by the queen on b8, so the king can't escape there either. Let me verify this is actually mate: the king on a8 has no legal moves, the queen on b8 gives check, and the queen is protected by the king on c6. That works.

I'm going to go with simpler examples that are easier to verify. The queen and king combination in the corner creates a straightforward mating pattern where the queen controls escape squares while the king provides support. controls b8 diagonally. Ka7 is also impossible since the king on b6 guards that square. Let me verify this works: the queen on a7 gives check to the king on a8, and both escape squares are covered—b8 by the queen's diagonal control and a7 by the king. That's checkmate.

Now for the Arabian Mate, which uses a rook and knight to trap the king in the corner. The setup has the knight on f7 and rook on h2, delivering mate with Rh8#.

Let me verify this works: with the king on h8, the rook moves to h8 giving check. The king cannot escape to g7 because the knight on f7 controls that square. The knight also covers h8, so the rook can safely deliver mate there. I'm getting tangled up here. Let me reconsider the position from scratch.

The Arabian mate pattern has the Black king on g8 with White's rook on h8 and knight on f7. When Rh8+ is played, the king can't escape because f7 is controlled by the knight and h7 is covered by the rook. The knight on f7 is the key piece preventing Kf7 or Kh7, making it checkmate. After Rh8+, the king on g8 is in check with no escape squares. Kf8 is controlled by the rook on the 8th rank, Kf7 is covered by the knight on h6, Kh7 is also controlled by the rook, and g7 is blocked by Black's own pawn. It's checkmate. The Epaulette Mate occurs when a queen delivers checkmate to a king hemmed in by its own rooks positioned on adjacent files. With Black's king on e8 flanked by rooks on d8 and f8, White's queen can move to e6, controlling all escape squares—d7, e7, and f7 are all dominated by the queen while d8 and f8 remain blocked by Black's own pieces. Queen on e6 controls the e-file, 6th rank, and diagonals, which means it covers d7, e7, and f7. The d8 and f8 squares are blocked by Black's rooks, so the king has no escape—that's checkmate.

From c4, the queen can reach e6 diagonally in one move, delivering mate. 4 empty, K (e1), 3 empty → 4K3 ✓

FEN: 3rkr2/8/8/8/2Q5/8/8/4K3 w - - 0 1

The move Qe6# delivers checkmate. Now I need to construct a mate-in-1 puzzle. Fool's Mate is the quickest checkmate possible at just 2 moves, so I'll position the board after White's opening blunder and Black's terrible response. Following 1. f3 e5 2. g4??, Black has the winning move available.

However, this won't work since Black delivers the mate, not White. I need to find a different pattern. Let me explore other classical mates like Damiano's Mate or simpler configurations using a rook and bishop, or perhaps a double bishop setup. A Queen and Bishop diagonal battery could work well—positioning the Black king on g8 with pawns on f7, g7, and h7, while White has a Queen on b3 and Bishop on c4.

Actually, that's too similar to Scholar's Mate. A Ladder Mate using two rooks seems more promising: Black king trapped on h8, with White rooks on g8 and a7 delivering checkmate. The king has no escape since g8 is occupied by the rook and h7 is controlled by the rook on a7. Let me verify g7 isn't available—the rook on a7 should control that square as well, making it a clean mate.

Alternatively, I could explore Boden's Mate, where two bishops coordinate on intersecting diagonals to trap the king.

For this pattern, I need the Black king somewhat confined—say on c8 with pawns on b7 and d7 blocking escape squares. White's bishops would need to control the critical diagonals: one on a6 eyeing the long diagonal, another positioned to cover b7 or nearby squares. The classic setup involves a queen sacrifice that forces the bishop placement, though I can construct a simpler position showing just the mating configuration itself. Bb5 controls the long diagonal through to e8. For a mating pattern, I need the king trapped on e8 with escape squares blocked—d8 and f8 would need to be controlled or obstructed, while d7 and f7 are already blocked by pawns. A second bishop could control e7, preventing the king from escaping there. The challenge is positioning both bishops so they deliver mate while the king has no flight squares.

Bg5 works perfectly—it controls e7 via the diagonal through f6. With Bb5 giving check and Bg5 controlling e7, the king on e8 becomes trapped: d8 and f8 are blocked by pieces, d7 and f7 by pawns, and e7 is covered. That's checkmate.

The position needs Black's king on e8, knights on d8 and f8, pawns on d7 and f7, and White's bishops on b5 and g5. I'm setting up the FEN but realizing I need to be more careful about piece placement—too many rooks creates an impossible position. Let me reconsider using just the essential pieces: the king, two knights, two pawns for Black, and the two bishops for White.

For Boden's mate specifically, I should position the king on c8 with a rook on b8, queen on d8, and a pawn on d7. White's bishops on f4 and a6 can deliver mate—Ba6 gives check along the long diagonal, and the king has no escape squares since d8 is blocked by its own queen, c7 is controlled by the Bf4, and b7 is also controlled by the Ba6.

To set this up properly, I need White to have a bishop that can reach a6 from c4, with the other bishop already on f4. The FEN position should reflect Black's king on c8 rather than e8, so I need to adjust the board layout accordingly.

Let me construct the rank 8 correctly: a8 is empty, b8 has the rook, c8 has the king, d8 has the queen, and e8-h8 are empty. That gives me 1rkq4 for the eighth rank. With the pawns and bishops positioned as needed, the FEN becomes 1rkq4/3p4/8/8/2B2B2/8/8/4K3 w - - 0 1.

Now Ba6 delivers checkmate—the bishop moves from c4 to a6, and I should verify this actually works.

The king on c8 is in check from the bishop on a6. Looking at escape squares: Kd8 is blocked by its own queen, Kb8 is blocked by its own rook, Kb7 is controlled by the bishop on a6, Kc7 is controlled by the other bishop on f4, and Kd7 is blocked by the pawn. That's mate.

I've found seven different mating patterns so far. The back rank mate uses a rook on e8 against a king trapped on g8. Scholar's mate delivers checkmate with the queen taking on f7. The smothered mate features a knight on f7 with the king boxed in on g8. A queen and king coordinate to trap the opponent's king on a7. The Arabian mate uses a rook and knight combination. The epaulette mate involves a queen delivering mate while the king's own rooks block escape routes. 2. **Scholar's Mate**: r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR
   - Position after 1.e4 e5 2.Bc4 Nc6 3.Qh5 Nf6
   - White delivers checkmate with Qxf7#
   - The king on e8 is in check from the queen. I need to verify the king has no escape squares: Kd8 appears open since the queen on f7 doesn't control that square. Let me reconsider whether this is actually mate.
   
   Actually, this is the classic Scholar's Mate and it is indeed checkmate. The queen on f7 controls the critical escape squares through its diagonals—it attacks e8 directly, and also commands e6 and d5 along one diagonal while covering g6 and h5 on the other. The king cannot escape.

   Looking at each potential flight square: d8 is blocked by Black's own queen sitting there, f8 is occupied by Black's bishop, and e7 falls under the queen's control since it's adjacent to f7. The king has no legal moves.

   For d7, I need to verify what controls it. The queen on f7 doesn't reach d7 (they're not on the same rank, file, or diagonal). The bishop on c4 also doesn't control d7—its diagonals extend to d5, e6, f7 in one direction and d3, e2, f1 in another, but not to d7. Something must be controlling that square in the actual mate position, so I should reconsider how the classic scholar's mate actually unfolds after 1.e4 e5 2.Bc4 Nc6 3.Qh5 Nf6 4.Qxf7#.

   Looking at the position before the final capture, the black pawn on d7 is still there—it blocks the king from moving to d7. The queen takes on f7, and now Ke7 is controlled by the queen on the 7th rank, Kd8 is blocked by black's own queen, and the king has no escape squares.

   For the smothered mate pattern, the knight on f7 delivers check to the king trapped on h8. The rook blocks g8, the pawn blocks h7, and the knight itself can't be captured. The king is completely hemmed in by its own pieces.

Now examining a queen and king mate: with the queen moving to a7, the black king on a8 is in check. The b8 square falls under the queen's control, while the white king on b6 dominates a7. No escape routes remain.

For the Arabian mate pattern, the rook delivers mate from h8 against the king on g8. The knight on h6 seals off f7, the rook controls both the 8th rank and h-file, and the pawn blocks g7. All four potential escape squares are covered.

In the epaulette mate, Qe6 gives checkmate to the king on e8. The rooks on d8 and f8 prevent movement to those squares, while the queen dominates d7, e7, and f7. The king has no legal moves.

For Boden's mate, Ba6 is the key move, with the two bishops on the long diagonal and a-file creating a mating net against the king on c8. Rank 1 checks out: K on a1, then 6 empty squares through g1, then R on h1. The knight on h6 is correctly placed with 7 empty squares before it on rank 6. All positions are accurate.

For the smothered mate position, the setup is confirmed: black rook on g8, king on h8, pawn on h7, and the knight positioned on h6. Moving the knight to f7 delivers the final blow.