The user wants me to describe 3 mate-in-1 scenarios for white. Each scenario needs:
1. A name
2. FEN notation for the setup
3. The winning move for white

Let me think of 3 distinct mate-in-1 puzzles.

**Scenario 1: Back Rank Mate**
A classic back rank mate where a rook or queen delivers checkmate on the 8th rank because the king is trapped by its own pawns.

Setup: Black king on g8, black pawns on f7, g7, h7. White rook on e1.
FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1

Wait, let me make sure this is correct. The FEN notation:
- Rank 8 (top): 6k1 means 6 empty squares, king on g8, 1 empty square
- Rank 7: 5ppp means 5 empty squares, pawns on f7, g7, h7
- Ranks 6-2: empty (8/8/8/8/8)
- Rank 1: 4R2K means 4 empty squares, Rook on e1, 2 empty squares, King on h1

Actually let me reconsider. The move Re8# would be checkmate.

Let me verify: King on g8, pawns on f7, g7, h7. Rook moves to e8. The king can't escape because:
- f8, g8, h8 are blocked/attacked
- f7, g7, h7 have pawns
Yes, Re8# is checkmate.

FEN: 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1

Move: Re8#

**Scenario 2: Queen and King Mate (simple)**


I need another classic mate-in-1. Let me consider a position where the queen delivers mate with support from my king. Black king trapped on h8, white queen on g6, white king on g1. The move Qg7# works because the king on h8 has no escape squares—g8 and h7 are controlled by the queen on g7, and the h-file is blocked.

FEN: 7k/8/6Q1/8/8/8/8/6K1 w - - 0 1

Move: Qg7#

Now for a smothered mate scenario. I want a position where a knight delivers checkmate while the enemy king is boxed in by its own pieces. The classic setup has the black king on g8 with a rook on h8 and pawns on f7 and g7, leaving the knight a perfect jumping square to deliver mate with no escape routes available. The knight needs to be positioned to deliver mate on f7. From h6, the knight can reach f7 with check, and the black king on h8 would have no escape squares—g8, g7, and h7 are all blocked by black's own pieces. So I need to get the knight to h6 first, then play Nf7#.

Let me verify this works: After Nf7+, the king is checkmated since it can't move to any adjacent square. The FEN position with the knight on h6 is 6rk/6pp/7N/8/8/8/8/6K1 w - - 0 1, and Nf7# delivers mate.

Now checking the back rank scenario: the position has a black king on g8 with pawns on f7, g7, and h7, while a white rook sits on e1 with the white king on h1. The FEN reads 6k1/5ppp/8/8/8/8/8/4R2K w - - 0 1, and Re8# is checkmate since the king has no escape squares.

For the queen mate setup, I'm placing the black king on h8 with a white queen on g6 and white king on g1. The FEN is 7k/8/6Q1/8/8/8/8/6K1 w - - 0 1, and either Qg7# or Qh7# delivers mate.

The smothered mate pattern involves a black king on h8 with a rook on g8 and pawns on g7 and h7, while a white knight positions itself on h6. The remaining ranks are empty except for the white king on g1. d by queen), h7 (attacked by queen) - no legal moves available. Both Qg7# and Qh7# deliver checkmate, so I'll use Qg7#.

I should verify the FEN notation follows the correct format, moving from rank 8 down to rank 1 and across files a through h. For Scenario 1, with the white king on h1, white rook on e1, black king on g8, and black pawns on f7, g7, h7, the position translates to the proper FEN string.

The rook move Re8# forces checkmate immediately since the black king has no escape squares. The queen delivers mate on g7. With the king trapped on h8, the queen controls g8 and h7 while giving check from g7—the king has no escape squares and no piece can block or capture the queen.

For the third scenario, White has a knight on h6 with Black's king on h8, blocked in by pawns on g7 and h7, and a rook on g8. This setup presents a different tactical puzzle to evaluate. are all classic, distinct mate patterns. For the second scenario, I'm considering better naming options—"Corridor Mate" doesn't fit, but "Queen's Kiss" captures the idea of the queen delivering mate adjacent to the king. Looking at the position with the king trapped in the corner and the queen on g7, this resembles an Epaulette pattern, though not precisely. I'll settle on calling it "Queen's Corner Mate" to clearly describe the mechanism. So the three patterns are: Back Rank Mate, Queen's Corner Mate, and Smothered Mate.

Wait, let me verify Scenario 2 works. The black king sits on h8, and after Qg7#, the queen attacks h8 diagonally. The king's escape squares—g8 and h7—are both controlled by the queen on g7, confirming it's checkmate.

All three scenarios check out. Now I'm reconsidering the terminology. The first two names feel solid, but the second scenario needs something more fitting than what I initially proposed. I'm cycling through options like "Queen Mate in the Corner," "Opera Mate," or "Arabian Mate," but none quite capture it. Maybe something simpler works better here.

Let me step back and use straightforward descriptive names instead of forcing classical terminology. I'll settle on Back Rank Mate for the first, Corner Mate for the second where the queen suffocates the king, and Smothered Mate for the third. These are clear and capture what's actually happening in each position.

Now I should verify each FEN to ensure the positions are set up correctly. The first one places the black king on g8 with pawns blocking escape on the seventh rank, while the rook delivers mate from e1.

The second position has the black king trapped on h8 with the white queen controlling g6, leaving no flight squares.

For the third, the black king sits on h8 with a rook on g8, and the knight on h6 will deliver the smothered mate since the king's own pieces block its escape. d knight move from h6 to f7 is valid (two files over, one rank up), and it delivers check to the king on h8 since knights on f7 attack h8. All three mates check out.