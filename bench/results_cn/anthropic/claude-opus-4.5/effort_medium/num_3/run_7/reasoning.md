The user wants me to describe 3 mate-in-1 scenarios for white. Each scenario needs:
1. A name
2. FEN notation for the setup
3. The winning move for white

Let me think of 3 distinct and valid mate-in-1 puzzles.

**Scenario 1: Back Rank Mate**
A classic back rank mate where the black king is trapped on the back rank by its own pawns, and a white rook or queen delivers checkmate.

Setup:
- Black king on g8
- Black pawns on f7, g7, h7 (trapping the king)
- White rook on e1 (or any rank on the first column that can reach the 8th rank)

Let me construct the FEN:
- 8th rank: 6k1 (king on g8)
- 7th rank: 5ppp (pawns on f7, g7, h7)
- Other ranks mostly empty
- White rook on e1
- White king somewhere safe, say a1

FEN: 6k1/5ppp/8/8/8/8/8/R3K3 w - - 0 1

Wait, let me reconsider. The rook is on a1, king on e1 (but without castling rights it's fine). Actually let me put the white king somewhere else to avoid confusion.

FEN: 6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1

This means:
- 8th rank: empty, empty, empty, empty, empty, empty, black king, empty (6k1)
- 7th rank: empty, empty, empty, empty, empty, black pawn, black pawn, black pawn (5ppp)
- Ranks 2-6: empty (8)
- 1st rank: empty, empty, empty, empty, white rook, empty, white king, empty (4R1K1)


- The winning move is Re8#. The black king on g8 is checkmated since the rook controls f8 and h8, while the king's own pawns block f7, g7, and h7. The rook cannot be captured or the check blocked.

**Scenario 2: Queen and King Mate**

A queen delivers checkmate while supported by the white king. Consider this position: black king trapped on a8, white king on a6, white queen on b1.

The decisive move is Qb8#. Once the queen reaches b8, the king is in check with no escape—a7 is controlled by both the white king and queen, and the king cannot move anywhere else. I need to find a position where the queen delivers checkmate while being protected. Let me work through this systematically.

For a queen to give checkmate, the king must be in check with no escape squares and no way to capture the queen. The challenge is ensuring the queen itself is defended.

A workable setup: Black king on h8, White queen on g7, White king on f6. This gives Qg7# as mate since the king on h8 is checked, h7 is controlled by the queen, and g8 is also controlled. The queen on g7 would be protected by the king on f6.

Let me verify with the position: Black king h8, White queen g6, White king g1. If the queen moves to g7, that's checkmate—the king can't escape h8, can't take the queen since it's protected by... wait, the king on g1 doesn't protect g7.

I need the white king positioned to defend the queen's mating square. Placing the king on f6 or f7 would work to protect g7. g7#? Let me check:
- h8 king in check from g7 queen
- Can't go to h7 (queen controls)
- Can't go anywhere else since corner

Yes! This works.

Wait, I need to double-check the king can't escape. From h8, the king can potentially go to g8... but g8 is controlled by the queen on g7. So yes, it's mate.

**Scenario 3: Smothered Mate**
Classic knight smothered mate with the king boxed in by its own pieces. The king sits on g8 surrounded by friendly rooks and pawns on f8, h7, and g7. The white knight delivers mate by jumping to f7, where it can't be captured and the king has no escape squares. Knight on f6 does attack g8, so that position wouldn't work for mate in 1 since the king would already be in check. Let me reconsider the setup—I need a position where the knight delivers checkmate in a single move, not one that's already checking. If I place the Black king on h8 with a rook on g8 and pawn on h7, then a White knight on f7 could deliver the finishing blow.

Checking the knight's reach from f7: it can move to d8, d6, e5, g5, h6, and h8. That h8 square is key—the knight would give check to the king there, and with the rook blocking g8 and the pawn on h7, escape routes are cut off.

Adding a pawn on g7 would seal it. With the king trapped on h8, the rook on g8, and pawns on both g7 and h7, moving the knight from e5 to f7 delivers checkmate—the king has nowhere to move and the knight can't be captured or blocked. The 7th rank has pawns on g7 and h7, so that's 6pp. I'll place the white king on a1 to complete the position.

FEN: 6rk/6pp/8/4N3/8/8/8/K7 w - - 0 1

Checking the notation: rank 8 shows the rook on g8 and king on h8, rank 7 has the two pawns on the kingside, the knight sits on e5 in rank 5, and the white king is positioned on a1. This confirms Nf7 delivers checkmate since the black king has no escape squares. - Black king g8 in check from rook e8
- f8 and h8 both controlled by the rook
- f7, g7, h7 all blocked by pawns

That's checkmate. ✓

**Scenario 2 Refined: Queen Mate**

I'll construct another pattern - a queen delivering mate with minimal pieces.

Consider:
- Black king h8
- Black pawn h7
- White queen g6
- White king a1

The queen moves to g7, giving check. The king can't escape to h7 (blocked by its own pawn) or g8 (controlled by the queen). Qg7#

FEN: 7k/

7p/6Q1/8/8/8/K7 w - - 0 1

The queen on g7 checks the king on h8. The h7 pawn blocks that escape square, g8 is dominated by the queen, and the pawn can't capture on g7 since pawns only capture diagonally forward—from h7 that would be g6, not g7. Checkmate confirmed. ✓ The pawn on h7 can only move forward to h6 or capture diagonally to g6—moving horizontally to g7 isn't possible for a pawn. So the queen is safe there, and the checkmate holds.

Now I'm considering other classic mating patterns. An Arabian Mate with rook and knight could work: place the Black king on h8, a White knight on f7 to control escape squares and deliver check, then position a rook to seal off the back rank. g8 and g6, which means if the rook delivers check on h8, the king still has g7 as an escape square. I need the knight positioned to control both g8 and g7 instead. A knight on e6 would attack g7, so that might work better for cutting off all the king's flight squares.

Looking at which squares each piece controls: a knight on e6 reaches g7, but g8 requires a knight on e7, f6, or h6. Since no single knight square covers both escape squares, I need to reconsider the setup. The Arabian mate pattern typically involves a rook on the h-file with a knight controlling the critical escape squares, but I'm having trouble pinning down the exact configuration that works here.

I'll move forward with three concrete mate patterns instead. Back rank mate with the rook delivering checkmate on e8, a queen suffocation mate on g7 with the king trapped by its own pawns, and a smothered mate where the knight on e5 delivers the final blow.

For the smothered mate position, let me verify the knight can actually reach f7 from e5 to confirm this works as intended.

A knight from e5 can move one file and two ranks, which gets it to f7. From f7, the knight then attacks h8 where the black king sits, delivering checkmate since the king has no escape squares.

Now I need to verify that the queen on g7 actually delivers checkmate rather than just check. The king on h8 is trapped—h7 is blocked by its own pawn and g8 is controlled by the queen. The h7 pawn can't help either since it only captures diagonally forward to g6, not horizontally to g7 where the queen stands.

So that's definitely checkmate. I'm satisfied with all three scenarios now. The back rank mate uses the king's own pawns as a trap, the queen mate suffocates the king in the corner, and the smothered mate is the classic knight finish where the king is completely boxed in by its own pieces. The knight on e5 can deliver checkmate by moving to f7. The black king on h8 has no escape squares—g8 is controlled by the knight, g7 is blocked by its own pawn, and h7 is also blocked by a pawn. This is the classic smothered mate pattern where the king is trapped by its own pieces and the knight administers the final blow.