I need to describe 3 distinct mate-in-1 scenarios for white. Let me think of some classic mate-in-1 patterns.

**Scenario 1: Back Rank Mate**
A classic back rank mate where the white rook delivers checkmate on the back rank because the black king is trapped by its own pawns.

Setup: Black king on g8, black pawns on f7, g7, h7. White rook can deliver mate on the 8th rank.

Let me set up a position:
- Black king on g8
- Black pawns on f7, g7, h7
- White rook on a1 (or any file on the 1st rank that can reach the 8th rank)
- White king somewhere safe, say e1

FEN: 6k1/5ppp/8/8/8/8/8/R3K3 w Q - 0 1

Wait, let me reconsider. The FEN notation:
- 6k1 means 6 empty squares, king, 1 empty square on the 8th rank - king on g8
- 5ppp means 5 empty squares, then ppp on f7, g7, h7
- White rook on a1, white king on e1

FEN: 6k1/5ppp/8/8/8/8/8/R3K3 w - - 0 1

The winning move would be Ra8# (Rook to a8 is checkmate)

Let me verify: Ra8+, the king is on g8, the rook attacks from a8. The king cannot move to f8 (rook controls), g8 is where it is, h8 (rook controls). f7, g7, h7 are blocked by pawns. So yes, Ra8#.

**Scenario 2: Queen and King Mate (Scholar's Mate style or simple queen mate)**


A position where the queen delivers mate with support from the white king. Black king on h8, white queen on f7, white king on g6 supporting the queen's mating squares.

If White plays Qg8#, the black king on h8 has no escape: g8 is occupied by the queen, g7 and h7 are both controlled by the queen, and g7 is additionally covered by the white king on g6. This is checkmate.

For a smothered mate pattern, I can set up a classic knight mate: Black king on h8 trapped by its own rook on g8 and pawns on g7 and h7. White knight on h6 delivers mate with Nf7#, since the king cannot escape to any adjacent square—all are either blocked by black's own pieces or controlled by the knight.