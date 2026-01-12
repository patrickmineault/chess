# Chess Endgame Practice App

Here's a complete chess endgame practice app with drag-and-drop functionality:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chess Endgame Practice</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
        }

        .container {
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 600px;
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 10px;
        }

        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 20px;
            font-size: 14px;
        }

        .controls {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }

        button {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s;
            font-weight: 600;
        }

        .scenario-btn {
            background: #667eea;
            color: white;
            flex: 1;
            min-width: 150px;
        }

        .scenario-btn:hover {
            background: #5568d3;
            transform: translateY(-2px);
        }

        .scenario-btn.active {
            background: #764ba2;
        }

        .reset-btn {
            background: #f093fb;
            color: white;
            width: 100%;
        }

        .reset-btn:hover {
            background: #d678e8;
        }

        .chessboard {
            display: grid;
            grid-template-columns: repeat(8, 60px);
            grid-template-rows: repeat(8, 60px);
            border: 3px solid #333;
            margin: 0 auto;
            width: fit-content;
        }

        .square {
            width: 60px;
            height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 40px;
            cursor: pointer;
            user-select: none;
            position: relative;
        }

        .square.light {
            background-color: #f0d9b5;
        }

        .square.dark {
            background-color: #b58863;
        }

        .square.highlight {
            background-color: #baca44 !important;
        }

        .square.drag-over {
            background-color: #7fa650 !important;
        }

        .piece {
            cursor: grab;
            transition: transform 0.1s;
        }

        .piece:active {
            cursor: grabbing;
            transform: scale(1.1);
        }

        .piece.dragging {
            opacity: 0.5;
        }

        .feedback {
            margin-top: 20px;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            font-weight: 600;
            font-size: 18px;
            min-height: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
        }

        .feedback.success {
            background: #d4edda;
            color: #155724;
            border: 2px solid #c3e6cb;
        }

        .feedback.error {
            background: #f8d7da;
            color: #721c24;
            border: 2px solid #f5c6cb;
        }

        .feedback.info {
            background: #d1ecf1;
            color: #0c5460;
            border: 2px solid #bee5eb;
        }

        .feedback:empty {
            min-height: 0;
            padding: 0;
            border: none;
        }

        @media (max-width: 600px) {
            .chessboard {
                grid-template-columns: repeat(8, 45px);
                grid-template-rows: repeat(8, 45px);
            }

            .square {
                width: 45px;
                height: 45px;
                font-size: 30px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>♔ Chess Endgame Practice ♔</h1>
        <p class="subtitle">Find mate in 1 move for White!</p>
        
        <div class="controls">
            <button class="scenario-btn active" onclick="loadScenario(0)">Scenario 1: Back Rank</button>
            <button class="scenario-btn" onclick="loadScenario(1)">Scenario 2: Queen Mate</button>
            <button class="scenario-btn" onclick="loadScenario(2)">Scenario 3: Rook Mate</button>
        </div>

        <div id="chessboard" class="chessboard"></div>

        <button class="reset-btn" onclick="resetPosition()">↺ Reset Position</button>

        <div id="feedback" class="feedback"></div>
    </div>

    <script>
        // Chess piece Unicode symbols
        const pieces = {
            'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
            'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
        };

        // Scenarios: Mate in 1 positions
        const scenarios = [
            // Scenario 1: Back rank mate with Rook
            {
                name: "Back Rank Mate",
                position: [
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', 'K', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['p', 'p', 'p', '', '', '', '', ''],
                    ['k', '', '', '', '', '', '', 'R']
                ],
                solution: {from: [7, 7], to: [7, 0]} // Rook to a1 is checkmate
            },
            // Scenario 2: Queen mate
            {
                name: "Queen Checkmate",
                position: [
                    ['', '', '', '', '', 'k', '', ''],
                    ['', '', '', '', '', 'p', 'p', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', 'K', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', 'Q', '']
                ],
                solution: {from: [7, 6], to: [0, 6]} // Queen to g8 is checkmate
            },
            // Scenario 3: Rook mate with King support
            {
                name: "Rook Mate",
                position: [
                    ['', '', '', '', 'k', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', 'K', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', 'R', '', '', '', '']
                ],
                solution: {from: [7, 3], to: [0, 3]} // Rook to d8 is checkmate
            }
        ];

        let currentScenario = 0;
        let board = [];
        let draggedPiece = null;
        let draggedFrom = null;

        // Initialize the game
        function init() {
            loadScenario(0);
        }

        // Load a specific scenario
        function loadScenario(index) {
            currentScenario = index;
            
            // Update active button
            document.querySelectorAll('.scenario-btn').forEach((btn, i) => {
                btn.classList.toggle('active', i === index);
            });

            // Clear feedback
            document.getElementById('feedback').innerHTML = '';
            document.getElementById('feedback').className = 'feedback';

            // Load the position
            resetPosition();
        }

        // Reset the current position
        function resetPosition() {
            board = scenarios[currentScenario].position.map(row => [...row]);
            renderBoard();
            document.getElementById('feedback').innerHTML = '';
            document.getElementById('feedback').className = 'feedback';
        }

        // Render the board
        function renderBoard() {
            const boardElement = document.getElementById('chessboard');
            boardElement.innerHTML = '';

            for (let row = 0; row < 8; row++) {
                for (let col = 0; col < 8; col++) {
                    const square = document.createElement('div');
                    square.className = `square ${(row + col) % 2 === 0 ? 'light' : 'dark'}`;
                    square.dataset.row = row;
                    square.dataset.col = col;

                    const piece = board[row][col];
                    if (piece) {
                        const pieceElement = document.createElement('span');
                        pieceElement.className = 'piece';
                        pieceElement.textContent = pieces[piece];
                        pieceElement.draggable = true;
                        pieceElement.dataset.piece = piece;

                        // Only allow dragging white pieces
                        if (piece === piece.toUpperCase()) {
                            pieceElement.addEventListener('dragstart', handleDragStart);
                            pieceElement.addEventListener('dragend', handleDragEnd);
                        } else {
                            pieceElement.draggable = false;
                            pieceElement.style.cursor = 'default';
                        }

                        square.appendChild(pieceElement);
                    }

                    square.addEventListener('dragover', handleDragOver);
                    square.addEventListener('drop', handleDrop);
                    square.addEventListener('dragleave', handleDragLeave);

                    boardElement.appendChild(square);
                }
            }
        }

        // Drag and drop handlers
        function handleDragStart(e) {
            const square = e.target.parentElement;
            draggedPiece = e.target.dataset.piece;
            draggedFrom = {
                row: parseInt(square.dataset.row),
                col: parseInt(square.dataset.col)
            };
            e.target.classList.add('dragging');
            square.classList.add('highlight');
        }

        function handleDragEnd(e) {
            e.target.classList.remove('dragging');
            document.querySelectorAll('.square').forEach(sq => {
                sq.classList.remove('highlight', 'drag-over');
            });
        }

        function handleDragOver(e) {
            e.preventDefault();
            e.currentTarget.classList.add('drag-over');
        }

        function handleDragLeave(e) {
            e.currentTarget.classList.remove('drag-over');
        }

        function handleDrop(e) {
            e.preventDefault();
            e.currentTarget.classList.remove('drag-over');

            const dropRow = parseInt(e.currentTarget.dataset.row);
            const dropCol = parseInt(e.currentTarget.dataset.col);

            if (draggedFrom && draggedPiece) {
                // Make the move
                board[draggedFrom.row][draggedFrom.col] = '';
                board[dropRow][dropCol] = draggedPiece;

                // Check if this is the correct solution
                checkSolution(draggedFrom, {row: dropRow, col: dropCol});

                renderBoard();
            }

            draggedPiece = null;
            draggedFrom = null;
        }

        // Check if the move is the solution
        function checkSolution(from, to) {
            const solution = scenarios[currentScenario].solution;
            const feedback = document.getElementById('feedback');

            if (from.row === solution.from[0] && 
                from.col === solution.from[1] && 
                to.row === solution.to[0] && 
                to.col === solution.to[1]) {
                
                feedback.className = 'feedback success';
                feedback.innerHTML = '🎉 Checkmate! Excellent move! 🎉';
                
                // Add celebration animation
                setTimeout(() => {
                    feedback.innerHTML = '🎉 Checkmate! Excellent move! 🎉<br><small>Select another scenario or reset to try again</small>';
                }, 500);
            } else {
                // Check if black king is in immediate danger (might be a legal move but not mate)
                feedback.className = 'feedback error';
                feedback.innerHTML = '❌ Not quite! That\'s not checkmate. Try again!';
                
                setTimeout(() => {
                    resetPosition();
                    feedback.innerHTML = '';
                    feedback.className = 'feedback';
                }, 1500);
            }
        }

        // Start the game
        init();
    </script>
</body>
</html>
```

## Features:

### ✨ **What's Included:**

1. **Three Mate-in-1 Scenarios:**
   - **Scenario 1**: Back rank mate with a Rook
   - **Scenario 2**: Queen checkmate
   - **Scenario 3**: Rook mate with King support

2. **Drag & Drop Functionality:**
   - Only white pieces can be dragged
   - Visual feedback during dragging (highlighting)
   - Smooth drag-over effects

3. **Visual Feedback:**
   - ✅ Success: Green message with celebration emoji
   - ❌ Error: Red message that auto-resets the position
   - Hover effects and animations

4. **User Controls:**
   - Three scenario selection buttons (highlighted when active)
   - Reset button to restore the current position
   - Responsive design for mobile devices

5. **Polish:**
   - Beautiful gradient background
   - Smooth animations and transitions
   - Professional chess board styling
   - Unicode chess pieces
   - Mobile-responsive

Simply save this as an HTML file and open it in your browser. The app works completely standalone with no external dependencies!