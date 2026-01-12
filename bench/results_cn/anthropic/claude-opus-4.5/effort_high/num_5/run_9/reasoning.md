The user wants me to describe 5 mate-in-1 scenarios for white. Each scenario should be in its own code block with:
1. Name of the scenario
2. FEN notation
3. The winning move for white

Let me think of 5 distinct mate-in-1 patterns:

1. **Back Rank Mate**
A classic pattern where the rook or queen delivers checkmate on the back rank while the king is trapped by its own pawns.

Let me construct a position:
- Black king on g8
- Black pawns on f7, g7, h7
- White rook on a1
- White king somewhere safe

FEN: 6k1/5ppp/8/8/8/8/8/R3K3 w Q - 0 1

Wait, let me verify this. The king is on g8, pawns on f7, g7, h7. White rook on a1.
Ra8# would be checkmate.

Actually let me be more careful with FEN notation:
- Row 8: 6k1 means 6 empty squares, king, 1 empty square
- Row 7: 5ppp means 5 empty squares, then p p p (f7, g7, h7)
- Rows 6-2: all empty (8/8/8/8/8)
- Row 1: R3K3 means Rook on a1, 3 empty, King on e1, 3 empty

FEN: 6k1/5ppp/8/8/8/8/8/R3K3 w - - 0 1

Move: Ra8#

Let me verify: Rook moves from a1 to a8. King on g8 is in check. Can king move?
- f8: rook controls it
- h8: rook controls it
- g8: that's where the king is


- f7, g7, h7: blocked by own pawns

Yes, this is checkmate.

2. **Queen and Bishop Battery**
A position where the queen delivers mate with support from a bishop on the long diagonal.

Black king on h8, pawn on g7. White queen on h5 can play Qh7# since the king has no escape squares—g8 is controlled by the queen and g7 is blocked by its own pawn.

3. **Smothered Mate**
A knight can deliver checkmate when the enemy king is trapped by its own pieces. Black king on h8 with rook on g8 and pawns on g7 and h7 creates the perfect setup. A white knight on f7 gives check, and since the king cannot move to g8 (occupied by rook) or g7 (occupied by pawn), it's mate. King on h8, rook on g8, pawn on h7 - the knight needs to deliver mate from a square that attacks h8. A knight on g6 can reach h8, so I need to figure out how to get the knight there. From f7, the knight can move to d6, d8, e5, g5, h6, or h8 - but h8 is occupied by the king. Let me reconsider the standard smothered mate setup: typically the king sits on g8 with a queen nearby delivering the final blow.

If the knight lands on h6 with the king on g8, it gives check since h6 attacks g8. But the king escapes to h8 since the knight from h6 only controls f5, f7, g4, and g8 - not h8. So that's not mate unless something else prevents the escape.

Let me reconsider the classic smothered mate setup. If Black has the king on h8 with a rook on g8 and pawns on g7 and h7, and I place a White knight on f7, it would attack h8 directly. A knight on f7 reaches d6, d8, e5, g5, h6, and h8 via its L-shaped moves. So the knight would indeed give check to a king on h8, and with the rook blocking g8 and pawns on g7 and h7, the king has no escape squares - that's mate. d or too far
- Kg8 blocked by own rook
- Move rook: Rxf7 but then Qg8# (assuming white queen)

The classic smothered mate typically involves a queen sacrifice. Let me try a different setup where the knight delivers mate directly.

Black: King g8, Rook f8, Queen e8, Pawns f7, g7, h7
White: Knight e7

A knight on e7 controls c6, c8, d5, f5, g6, and g8—so it would give check to a king on g8. But I need to verify the knight is actually attacking that square.

Working backward from the mating position: if the king sits on g8 with a rook on f8 and pawns on g7 and h7, a knight on h6 would attack f5, f7, g4, and g8. That's checkmate since the king cannot move to f7 (blocked by pawn), h7 (blocked by pawn), h8 (not controlled by the knight), or f8 (occupied by rook).

So h8 needs to be covered. If there's a black rook or bishop already on h8, then Nh6 becomes mate. Let me verify the knight move to f7 instead—from there it would attack d6, d8, e5, g5, h8, and h6, but crucially not g8 itself, so that doesn't work as a mating move.

For a smothered mate pattern, I need the king trapped on h8 with a knight delivering check from either f7 or g6. A knight on g6 does attack h8, so if I position a black king on h8 with pieces blocking escape squares like a rook on g8 and pawns on g7 and h7, then Ng6 would be checkmate. The king can't move to g8 (occupied), h7 (pawn), or g7 (pawn), and can't capture the knight if the h7 pawn is still there. I need to clarify the board position using proper notation. The black king sits on h8 with a rook on g8, and pawns occupy g7 and h7. The white knight is positioned on e5.

Using FEN notation: 6rk/6pp/8/4N3/8/8/8/4K3 w - - 0 1

This confirms the setup where Ng6 delivers checkmate—the knight controls h8 while the king has no escape squares and no piece can capture the knight or block the attack. I need to reconsider the pawn capture mechanics. A black pawn on h7 can indeed capture diagonally forward to g6, so Ng6 wouldn't be checkmate. I need h7 blocked by a piece that cannot capture on g6—a rook would work since it can only move along ranks and files. Let me set up: Black king h8, rook g8, rook h7, pawn g7, with my knight on e5. The rook on h7 controls the escape square but can't reach g6, making Ng6 a true checkmate. The rook on h7 can't reach g6, and the black pawn on g7 moves toward rank 1, so it captures on f6 or h6—not backward to g6. The rook also can't capture on g6 from h7 since rooks move in straight lines. This means Ng6# is checkmate.

Let me verify the king's escape squares more carefully. From h8 in check from the knight on g6, the king can't move to g8 (occupied by rook), h7 (occupied by rook), or g7 (occupied by pawn). The knight from g6 also controls f8, so that square is unavailable too. There's no legal move.

I should also confirm no piece can capture the knight or block—but knight checks can't be blocked anyway. Since all escape routes are sealed and the knight is protected or unreachable, this is checkmate.

Actually, constructing these positions is getting unwieldy. Let me start fresh with simpler, more straightforward mate-in-1 scenarios instead.

For a back rank mate setup: I'll place the black king on g8 with pawns on f7, g7, and h7 (the typical castled position), then put a white rook on the first rank. Moving the rook to the eighth rank delivers mate since the king has no escape squares and can't capture the rook.

For a queen and king mate: I need the black king trapped in a corner with limited mobility. If I position the black king on a8 and the white queen on b6, moving to a7 gives check, but the king can escape to b8 since the queen doesn't control that square. I should adjust the queen placement to ensure it covers all escape routes.

Actually, from a7 the queen controls the entire a-file, the 7th rank, and both diagonals—including b8. So Qa7 is indeed checkmate. I'll set up the position with the white king on e1 to keep it legal.

But I realize the black king could capture the queen on a7 if it's undefended. The white king on e1 doesn't protect a7, so I need to reposition it. Let me place the white king on b5 instead to guard the queen and ensure the mate is sound.

Actually, for a mate-in-1 puzzle, I should set up the position so the queen delivers checkmate in one move. Let me reconsider: black king on a8, white queen on b3, and white king on a6 to control b7 and defend the queen if it moves to a7.

Testing Qb8#: the king on a8 is in check from the queen on b8. The king cannot escape to a7 (controlled by the white king on a6) or b7 (also controlled by the white king). The queen on b8 is protected by the king on a6, so Kxb8 is illegal. This works as checkmate. The queen on b8 isn't protected by the king on a6, so the black king can simply capture it—not checkmate after all.

Let me reconsider with a clearer setup. I'll place the black king in a corner where it has fewer escape squares. Black king on h1, white queen on f3, white king on g3. If the queen moves to f1, it gives check to the king on h1. The king can't move to g2 since the queen controls that square, and g1 is also covered. With the white king on g3 controlling h2 and h3, the black king has no legal moves and no piece can block or capture the queen. The white king on g3 also controls h2, making that square unavailable. So the only escape squares are blocked: g2 falls to the queen, h2 to the king, and the king can't capture on f1 since it's two squares away. Qf1 is checkmate. The lawnmower mate is more of a process than a single position. Let me consider a simpler rook and king mate instead.

Actually, I'll go with Opera Mate as a cleaner example. I need a Black king on g8 with a piece blocking f8, then deliver mate with a rook on the back rank while a bishop controls the escape squares. Let me set up: Black king g8, Black rook f8, White rook d1 moving to d8, and White bishop b2 covering the g7 diagonal. But I should verify Kh7 isn't available as an escape. A simpler configuration might work better—Black king g8 with a Black rook on f8.

Actually, placing the bishop on a1 covers the long diagonal through g7, which already has a Black pawn anyway. When the rook moves to d8 for checkmate, the king can't escape to f7 since that square isn't controlled by either piece on the d-file or 8th rank, nor is it on the a1-h8 diagonal.

I need to reconsider the setup. If I add a queen to control f7, then with the rook on d8, the Black king has no legal moves—f8 is blocked by the rook, f7 and g7 and h7 are all blocked by pawns, and h8 is attacked by the rook. But this is just back rank mate with the rook and pawns doing the work, which is essentially what I already explored.

Let me try a different mating pattern. What about using a bishop and king in the corner? If the Black king is on h8, I could try placing a White bishop on f6, but that doesn't directly attack h8 since the diagonal from f6 goes through g7. I need to think about diagonal mates more carefully—maybe a queen on the long diagonal attacking g8, with a bishop supporting on c4, though having both pieces on the same diagonal creates redundancy rather than a true mate.

Actually, Scholar's Mate seems more promising. If I place the Black king on e8 with pieces blocking on d8 and f8, remove the f7 pawn, and position the White queen on h5, the queen can deliver checkmate on f7 since the king has no escape squares and the queen is protected.

Let me construct this carefully: Black king e8, Black queen on d8 to block that square, White queen on h5 moving to f7. The king can't move to d8 (occupied), can't stay on e8 (in check), and can't capture on f7 if I protect it. A White bishop on c4 guards f7, making this work as checkmate.

For the Arabian Mate setup, I need a rook and knight working together. King trapped on h8, knight on f7 controlling key escape squares like g8 and h6. But if the rook gives check from a8, the king can still slip to g7 since the knight doesn't cover that square. I need to adjust the knight's positioning to seal off g6 as an escape route. Knight on f7 covers h8, h6, g5, e5, d8, and d6, but not g8. Let me recalculate the squares: from f7, the knight reaches g5, e5, h8, h6, d8, and d6 using standard knight moves. Since g8 isn't covered, I need to reconsider the knight's placement—perhaps e6 or another square would work better to control both g8 and the king's escape routes.

Checking e6: the knight covers d4, d8, c5, c7, f4, f8, g5, and g7—still missing g8. But from f6, the knight reaches d5, d7, e4, e8, g4, g8, h5, and h7. That covers g8! For the Arabian mate pattern, I need the Black king on h8, a White knight on f6 to control g8, and a rook delivering mate on h7. The position would be: Black king h8, White rook on b7 (or nearby), White knight f6, with White king on e1.

After Rh7#, Black has no escape—the king can't go to g8 because the knight controls it, and capturing the rook with Kxh7 is illegal since the knight on f6 also guards h7. So the king can't capture the rook since the knight guards h7. That's checkmate—an Arabian Mate pattern.

Now considering Boden's Mate instead. This requires two bishops on intersecting diagonals both attacking the king's square. I'd position the Black king on c8 with a White bishop on a6 controlling that diagonal, and another bishop positioned to attack c8 from a different angle while the king has no escape squares. awn blocks this). 

Actually, the pawn on b7 blocks the diagonal, so Ba6 isn't giving check. Let me reconsider.

If the black king is on c8 with a rook on d8 blocking that escape, I need the bishops positioned so one delivers check while the other controls b8. The bishop on a6 doesn't work if b7 is occupied. I should try placing a bishop on the long diagonal instead—say Bh3—to attack c8 via h3-g4-f5-e6-d7-c8, with the other bishop controlling the remaining escape squares. Rank 6 has the bishop on a6 with the rest empty. But the bishop is already positioned there, so I need a different piece to deliver mate, or move the bishop from elsewhere.

Let me try: White bishop starts on c4 and plays Ba6#. Or I could use two bishops—one on b2, another on d5—to create the mating pattern. The key is ensuring the Black king on c8 has no escape squares while the bishops control the critical diagonals.

For Boden's Mate specifically, I'm looking at the classic pattern where bishops on criss-crossing diagonals trap the king. The Black king sits on c8, blocked by pieces on b8 and d8, while White's bishops on a6 and another diagonal deliver the final blow. The mate works because the bishops control all escape routes around c8. c8 is a light square. Counting from c1 as dark, the pattern alternates up the column: c2 light, c3 dark, c4 light, c5 dark, c6 light, c7 dark, c8 light. So there's one bishop that can reach c8.

Two light-squared bishops can attack c8 simultaneously—one positioned on the a6-c8 diagonal and another on the h3-c8 diagonal. If a bishop moves to c8 while the king is trapped there with all escape squares controlled, that delivers mate. The key is whether one bishop can move to create the decisive double attack while the other already covers the square.

In Boden's mate specifically, one bishop gives check while the second bishop controls the critical escape square. Setting it up: Black has a king on c8 with a rook on d8 and pawns on a7 and b7. White plays Ba6+, and the king cannot escape to d8 (blocked by its own rook), c7 (controlled by the other bishop), or b8 (also controlled). That's mate.

For the escape squares to be properly covered, I need a bishop that can simultaneously defend both b8 and c7. A bishop positioned on f4 works perfectly—it controls the long diagonal through c7 and extends to b8, sealing off both flight squares while the first bishop delivers check from a6. d to reconsider the setup. Maybe the blocking piece isn't on d8, or the bishops are positioned differently. Let me think about what configuration actually works for Boden's mate.

Actually, I should verify the exact piece placement. If Kd7 is a legal escape with the current setup, then this isn't the right configuration for the mate pattern. The second bishop needs to control d7 as well, or there's a different piece arrangement I'm missing. The bishop is on b5, not a6 yet. Moving Ba6 delivers checkmate since the king on c8 has no escape squares—Kb7 is controlled by the bishop on a6, Kb8 and Kc7 are both covered by the bishop on f4, and d8 is blocked by Black's own rook while d7 is blocked by the pawn. a6 is light, b5 is light, and f4 is light—all consistent with the bishops being on light squares. Since c8 is also light, the light-squared bishops can deliver the final blow. ✓

I have five checkmate positions ready:

1. **Back Rank Mate**: Ra8# in the position 6k1/5ppp/8/8/8/8/8/R3K3 w - - 0 1
2. **Queen and King Mate**: Qf1# in 8/8/8/8/8/5QK1/8/7k w - - 0 1
3. **Scholar's Mate**: Qf7# in 3qk3/8/8/7Q/2B5/8/8/4K3 w - - 0 1
4. **Arabian Mate**: Rh7# in 7k/1R6/5N2/8/8/8/8/4K3 w - - 0 1
5. **Boden's Mate**: Ba6# in 2kr4/3p4/8/1B6/5B2/8/8/4K3 w - - 0 1

For the smothered mate variation, I'm working with 6rk/6pr/8/4N3/8/8/8/4K3 w - - 0 1, where Ng delivers mate. Let me verify the Queen and King position once more. The FEN places the black king on h1, white queen on f3, and white king on g3. When the queen moves to f1, it delivers checkmate—the king can't escape to g2 or g1 because the queen controls those squares, and h2 is blocked by the white king on g3. That confirms this pattern works.

I'll stick with my original five examples since they're the most recognizable checkmate patterns.