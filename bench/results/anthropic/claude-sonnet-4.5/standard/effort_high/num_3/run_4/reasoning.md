I'll create a chess endgame practice app with the following features:
1. Three different mate-in-1 scenarios for white
2. Selectable scenarios
3. Drag and drop functionality for pieces
4. Visual feedback when the user finds the correct move
5. Reset button to restore the position

I'll use HTML, CSS, and vanilla JavaScript to keep it simple and self-contained. I'll implement a chess board from scratch with drag-and-drop functionality.

Let me plan the three mate-in-1 scenarios:
1. Back rank mate: White Queen on the 7th rank, Black King on the back rank trapped by its own pieces
2. Rook mate: White Rook can deliver checkmate on the back rank
3. Queen and King mate: Simple Queen delivers mate with King support

Here's my approach:
- Create a chessboard using HTML/CSS
- Implement piece rendering with Unicode chess symbols
- Add drag and drop functionality
- Track piece positions
- Implement move validation for the mate-in-1 scenarios
- Add visual feedback (green for correct, red for wrong)
- Add scenario selection buttons
- Add reset functionality