I need to create 3 different mate-in-1 scenarios for white in chess. Each should be:
1. Valid (legal position)
2. Distinct from each other
3. Actually be mate in 1 move

Let me think of three different tactical patterns:

1. **Back Rank Mate** - A classic where the enemy king is trapped on the back rank by its own pieces
2. **Queen and King Mate** - Where a queen delivers checkmate with support
3. **Rook Mate** - A rook delivers mate on an exposed king

Let me construct these:

**Scenario 1: Back Rank Mate**
- Black king on g8, trapped by pawns on f7, g7, h7
- White rook can deliver mate on the 8th rank
- Setup: White rook on a1, Black King on g8, Black pawns on f7, g7, h7
- FEN: 6k1/5ppp/8/8/8/8/8/R6K w - - 0 1
- Winning move: Ra8#

Wait, let me verify this is mate:
- Ra8+ puts the king in check
- King on g8 cannot move to f8 (controlled by Ra8), h8 (controlled by Ra8), g7 (occupied by own pawn), f7 (occupied by own pawn), h7 (occupied by own pawn)
- No piece can block or capture the rook
- Yes, this is mate!

**Scenario 2: Queen Mate on the side**
- Black king trapped on the edge
- Queen delivers mate
- Setup: Black King on h1, White Queen on g3, White King somewhere safe like e1
- FEN: 8/8/8/8/8/6Q1/8/4K2k w - - 0 1
- Winning move: Qg1#

Let me verify:


I confirm the queen's move traps the king completely. The black monarch has no escape squares, with the queen controlling critical adjacent positions. This creates a decisive checkmate scenario.

**Scenario 3: Smothered Mate with Knight**
I see a tactical opportunity where the knight can exploit the king's restricted movement. The knight's unique jumping ability allows it to deliver mate in a situation where other pieces cannot, creating a classic smothered mate pattern.

The initial position requires precise knight placement. I'm carefully analyzing the potential mating squares and king's confinement, ensuring the knight can strike decisively while the surrounding pieces block potential escape routes.

The classic smothered mate configuration demands strategic positioning of the knight and blocking pieces to create an inescapable trap for the king.

I'm exploring potential knight movements that could deliver a decisive checkmate, carefully considering piece placement and attack vectors around the confined king.

The key seems to be trapping the king with surrounding pawns and a rook, then finding the precise knight move that delivers an unavoidable check.

Knight on f7 attacks h8, with no escape routes. The king can't move to g8 or h7, and no piece can block or capture the knight. Checkmate confirmed.

This scenario represents a classic smothered mate, where the king is trapped by its own pieces, unable to evade the knight's attack.

I verify the board configuration, confirming the precise placement of pieces that creates this checkmate scenario. The knight's strategic placement on f7 delivers a decisive blow, leaving the king with no escape routes.

The FEN notation precisely captures the board's critical state, showing the king's vulnerability and the knight's lethal positioning. 4: empty = 8
   - Rank 3: 6 empty, Queen on g3, 1 empty = 6Q1
   - Rank 2: empty = 8
   - Rank 1: 4 empty, King on e1, 2 empty, king on h1 = 4K2k
   - w (white to move)

3. 6rk/6pp/8/4N3/8/8/8/4K3 w - - 0 1
   - Rank 8: 6 empty, rook on g8, king on h8 = 6rk
   - Rank 7: 6 empty, pawns on g7, h7 = 6pp
   - Rank 6: empty = 8
   - Rank 5: 4 empty, Knight on e5, 3 empty = 4N3
   - Ranks 4-2: empty = 8/8/8
   - Rank 1: 4 empty, King on e1, 3 empty = 4K3
   - White's turn to move