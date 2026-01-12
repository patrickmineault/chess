I need to create 5 different mate-in-1 scenarios for white. Each should be:
1. A valid chess position in FEN notation
2. A scenario where white can checkmate in one move
3. Distinct from the others (using different pieces or patterns)

Let me think of 5 different checkmating patterns:

1. **Back Rank Mate with Rook** - A classic scenario where a rook delivers checkmate on the back rank
2. **Queen and King Mate** - Queen delivers checkmate with king support
3. **Knight Mate** - A knight delivers the final blow
4. **Bishop Mate** - A bishop delivers checkmate
5. **Pawn Promotion Mate** - A pawn promotes and delivers checkmate

Let me create valid FEN positions for each:

1. **Back Rank Mate**
Position: Black king on g8, black pawns on f7, g7, h7, white rook on d1
FEN: 6k1/5ppp/8/8/8/8/8/3R2K1 w - - 0 1
Winning move: Rd8#

2. **Queen Mate**
Position: Black king on h8, black pawn on h7, white queen on g7, white king on f6
FEN: 7k/6Qp/5K2/8/8/8/8/8 w - - 0 1
Winning move: Qg8#

Wait, let me verify this - if the black king is on h8, there's a pawn on h7, and white queen on g7... can the queen go to g8? Yes, and that would be checkmate because the king can't move anywhere.

3. **Knight Mate**
Position: Black king on h8, black pawns on g7 and h7, white knight on f6, white queen on g8
Actually, let me make this simpler with just a knight delivering mate.


FEN: 7k/5N1p/8/8/8/8/8/K7 w - - 0 1
Winning move: Ng6#

I verify the knight's move carefully. The knight on g6 attacks h8 and f8, trapping the king. The pawn on h7 blocks the h8 escape, and the knight controls g8 and g7, ensuring a complete checkmate. I'm analyzing knight checkmate patterns. The knight's positioning is critical - I need to ensure it controls key escape squares. In the current position, I'm carefully checking whether the knight truly restricts the king's movement. From c7 to a6, the knight attacks strategic squares, potentially trapping the black king. The white king's placement on b6 further limits potential escape routes. I'm verifying each potential square the king might use to escape.

The knight's attack covers multiple squares: a6, b8, c7, creating a tight net around the black king. With the white king blocking key escape paths, this looks like a definitive checkmate scenario.

I'm analyzing a bishop mate configuration, carefully tracking diagonal attack lines and potential king movements. The positioning requires precise coordination between pieces to restrict the opponent's king.

I'll explore a straightforward checkmate strategy, focusing on controlling critical squares and limiting the king's mobility. I'm exploring checkmate patterns with a bishop and king, carefully analyzing each position's potential. The key challenge is trapping the black king while ensuring no escape routes exist. I've been systematically testing different board configurations, checking king movement and piece interactions to find a definitive checkmate sequence.

My current focus involves understanding how the white bishop can restrict the black king's mobility, particularly in scenarios with limited pawn presence. Each attempted position reveals nuanced positional constraints that prevent or enable checkmate.

The critical insight involves controlling key escape squares and leveraging piece placement to create an inescapable mating net. I'm methodically examining each configuration to identify the precise geometric relationship between pieces that guarantees checkmate. The pawn's promotion creates a decisive checkmate. By advancing to e8 and transforming into a queen, it delivers check to the black king on d8. The newly promoted queen controls critical squares, preventing the king's escape. With c8, d7, and c7 all under attack by the queen and white king, the black monarch has no legal moves. The king is trapped. The knight delivers a decisive blow by moving to a6, creating an inescapable checkmate. The white king supports the knight's attack, leaving no escape routes for the black king.

The bishop also demonstrates a similar mating pattern, moving to g7 and cutting off all potential escape squares. The white king provides crucial support, ensuring the black king cannot evade the attack.

A pawn promotion scenario emerges, suggesting the potential for transforming a pawn into a more powerful piece at the edge of the board. I verify each checkmate scenario systematically. The knight move to a6 traps the king, blocking escape routes. The bishop on g7 controls critical squares, preventing king movement. The pawn's promotion to queen creates a devastating checkmate, controlling key squares around the black king. Each solution demonstrates precise tactical execution, leaving no escape for the opponent's king.