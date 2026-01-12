I need to create 5 different mate-in-1 scenarios for white. Each should be:
1. Valid chess positions
2. Where white can checkmate in one move
3. Distinct from each other (different pieces, different mating patterns)

Let me think of different mating patterns:

1. Back rank mate with a rook
2. Queen mate
3. Knight mate
4. Bishop mate
5. Pawn promotion mate

Let me create valid FEN notations for each:

1. **Back Rank Mate with Rook**
- Black king on g8, trapped by its own pawns on f7, g7, h7
- White rook can move to d8#
FEN: 6k1/5ppp/8/8/8/8/5PPP/3R2K1 w - - 0 1
Move: Rd8#

2. **Queen Mate**
- Black king on h8, trapped
- White queen can deliver mate from various squares
FEN: 7k/5Qpp/6p1/8/8/8/5PPP/6K1 w - - 0 1
Move: Qg8# or Qg7#
Actually let me make it clearer: 7k/6pp/8/8/8/8/5PPP/5QK1 w - - 0 1
Move: Qf8#

3. **Knight Mate (Smothered Mate)**
- Black king on h8, surrounded by own pieces
- White knight delivers mate
FEN: 6rk/6pp/6N1/8/8/8/5PPP/6K1 w - - 0 1
Move: Nf7# 
Wait, let me verify - king on h8, pawns on g7 and h7, rook on g8. Knight on g6 can go to f7... that's not checkmate because the king could take the knight if nothing protects f7. 

I'm struggling to find a clear smothered mate scenario. The positioning needs to completely restrict the king's movement while ensuring the knight can deliver a decisive blow. I'll need to carefully arrange the pieces to create a truly confined position where the knight can checkmate without being captured. I see the knight on f6 moving to f7, delivering a decisive checkmate. The king on h8 is completely trapped - blocked by pawns on h7 and g7, and the queen on g8. The knight's move to f7 attacks the king directly, with no possible escape or defensive capture. This smothered mate scenario perfectly demonstrates the knight's unique attacking potential.

The king's confinement by its own pieces creates an inescapable situation, showcasing a classic chess tactical motif where mobility is completely eliminated.

White bishop on c7 moves to b6, creating an unstoppable checkmate. The black king on a8 has no escape squares, while the white king on b6 provides crucial support. The bishop's precise positioning ensures absolute control of the critical squares, rendering the black king helpless.

The pawn promotion scenario offers two mating possibilities - promoting to either queen or rook on b8. With the white king supporting from b6 and the black king trapped on a8, the promoted piece delivers an immediate and decisive checkmate.

The rook delivers a devastating check from d1 to d8. Black's king on g8 finds itself completely trapped, with surrounding pawns blocking all potential escape routes. No defensive piece can intervene or capture the rook, confirming the mate.

The knight executes a precise smothered mate on f7, attacking the king while being completely protected. Black's king remains immobilized by the surrounding queen and pawns, unable to move or find relief. The knight's strategic positioning ensures an inescapable checkmate.

A bishop mate requires careful diagonal control, with the white king supporting the attacking bishop's movement to trap the black king.

The first scenario demonstrates a precise bishop checkmate on g7, where the white king prevents escape and the pawn blocks potential flight squares. The second scenario shows a pawn promotion creating a queen mate, strategically trapping the black king with no legal moves.

I'll capture these elegant chess mating patterns with descriptive names that highlight their unique characteristics.