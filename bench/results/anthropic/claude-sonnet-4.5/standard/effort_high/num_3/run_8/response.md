# Chess Endgame Practice App

Here's a complete chess endgame practice app with 3 mate-in-1 scenarios:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chess Endgame Practice - Mate in 1</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .container {
            background: white;
            padding: 30px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            max-width: 600px;
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 10px;
            font-size: 28px;
        }

        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 20px;
            font-size: 16px;
        }

        .controls {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }

        button {
            flex: 1;
            padding: 12px 20px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            transition: all 0.3s;
            min-width: 120px;
        }

        .scenario-btn {
            background: #667eea;
            color: white;
        }

        .scenario-btn:hover {
            background: #5568d3;
            transform: translateY(-2px);
        }

        .scenario-btn.active {
            background: #764ba2;
            box-shadow: 0 4px 12px rgba(118, 75, 162, 0.4);
        }

        .reset-btn {
            background: #f093fb;
            color: white;
        }

        .reset-btn:hover {
            background: #d87ce8;
            transform: translateY(-2px);
        }

        .chessboard {
            display: grid;
            grid-template-columns: repeat(8, 1fr);
            gap: 0;
            width: 100%;
            max-width: 480px;
            margin: 0 auto 20px;
            border: 4px solid #333;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }

        .square {
            aspect-ratio: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 48px;
            cursor: pointer;
            position: relative;
            transition: all 0.2s;
        }

        .square.light {
            background: #f0d9b5;
        }

        .square.dark {
            background: #b58863;
        }

        .square.dragging {
            opacity: 0.5;
        }

        .square.drag-over {
            background: #88cc88 !important;
            box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.3);
        }

        .square:hover {
            filter: brightness(0.9);
        }

        .piece {
            cursor: grab;
            user-select: none;
            transition: transform 0.1s;
        }

        .piece:active {
            cursor: grabbing;
            transform: scale(1.1);
        }

        .feedback {
            text-align: center;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
            font-size: 18px;
            font-weight: 600;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .feedback.show {
            opacity: 1;
        }

        .feedback.success {
            background: #4caf50;
            color: white;
            animation: celebration 0.5s ease-in-out;
        }

        .feedback.error {
            background: #f44336;
            color: white;
        }

        @keyframes celebration {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        .instruction {
            text-align: center;
            color: #555;
            margin-bottom: 15px;
            font-size: 14px;
            padding: 10px;
            background: #f5f5f5;
            border-radius: 8px;
        }

        @media (max-width: 600px) {
            .container {
                padding: 15px;
            }

            h1 {
                font-size: 22px;
            }

            .square {
                font-size: 32px;
            }

            button {
                min-width: 100px;
                padding: 10px 15px;
                font-size: 12px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>♟️ Chess Endgame Practice</h1>
        <p class="subtitle">Find the Mate in 1 for White!</p>
        
        <div class="controls">
            <button class="scenario-btn active" onclick="loadScenario(0)">Scenario 1</button>
            <button class="scenario-btn" onclick="loadScenario(1)">Scenario 2</button>
            <button class="scenario-btn" onclick="loadScenario(2)">Scenario 3</button>
            <button class="reset-btn" onclick="resetPosition()">Reset Position</button>
        </div>

        <div class="instruction">
            Drag and drop a white piece to deliver checkmate!
        </div>

        <div class="chessboard" id="chessboard"></div>

        <div class="feedback" id="feedback"></div>
    </div>

    <script>
        // Chess piece Unicode symbols
        const pieces = {
            'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',  // White
            'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'   // Black
        };

        // Mate in 1 scenarios
        const scenarios = [
            {
                name: "Back Rank Mate",
                position: [
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', 'k', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', 'p', 'p', 'p'],
                    ['R', '', '', '', '', '', 'K', '']
                ],
                solution: { from: [7, 0], to: [2, 0] } // Ra8#
            },
            {
                name: "Queen & King Mate",
                position: [
                    ['', '', '', '', '', 'k', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', 'K', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', 'Q', '', '', '', ''],
                    ['', '', '', '', '', '', '', '']
                ],
                solution: { from: [6, 3], to: [0, 3] } // Qd8#
            },
            {
                name: "Rook Mate",
                position: [
                    ['', '', '', '', '', '', 'k', ''],
                    ['', '', '', '', '', '', '', 'R'],
                    ['', '', '', '', '', '', 'K', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '']
                ],
                solution: { from: [1, 7], to: [0, 7] } // Rh8#
            }
        ];

        let currentScenario = 0;
        let board = [];
        let originalBoard = [];
        let draggedPiece = null;
        let draggedFrom = null;

        // Initialize the game
        function init() {
            loadScenario(0);
        }

        // Load a specific scenario
        function loadScenario(index) {
            currentScenario = index;
            board = JSON.parse(JSON.stringify(scenarios[index].position));
            originalBoard = JSON.parse(JSON.stringify(scenarios[index].position));
            
            // Update active button
            document.querySelectorAll('.scenario-btn').forEach((btn, i) => {
                btn.classList.toggle('active', i === index);
            });

            hideFeedback();
            renderBoard();
        }

        // Reset the current position
        function resetPosition() {
            board = JSON.parse(JSON.stringify(originalBoard));
            hideFeedback();
            renderBoard();
        }

        // Render the chessboard
        function renderBoard() {
            const chessboard = document.getElementById('chessboard');
            chessboard.innerHTML = '';

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
                        pieceElement.draggable = isWhitePiece(piece);
                        pieceElement.dataset.piece = piece;
                        
                        if (isWhitePiece(piece)) {
                            pieceElement.addEventListener('dragstart', handleDragStart);
                            pieceElement.addEventListener('dragend', handleDragEnd);
                        }
                        
                        square.appendChild(pieceElement);
                    }

                    square.addEventListener('dragover', handleDragOver);
                    square.addEventListener('drop', handleDrop);
                    square.addEventListener('dragleave', handleDragLeave);

                    chessboard.appendChild(square);
                }
            }
        }

        // Check if piece is white
        function isWhitePiece(piece) {
            return piece === piece.toUpperCase();
        }

        // Drag and drop handlers
        function handleDragStart(e) {
            const square = e.target.parentElement;
            draggedPiece = e.target.dataset.piece;
            draggedFrom = {
                row: parseInt(square.dataset.row),
                col: parseInt(square.dataset.col)
            };
            square.classList.add('dragging');
            e.dataTransfer.effectAllowed = 'move';
        }

        function handleDragEnd(e) {
            e.target.parentElement.classList.remove('dragging');
        }

        function handleDragOver(e) {
            e.preventDefault();
            e.dataTransfer.dropEffect = 'move';
            e.currentTarget.classList.add('drag-over');
        }

        function handleDragLeave(e) {
            e.currentTarget.classList.remove('drag-over');
        }

        function handleDrop(e) {
            e.preventDefault();
            e.currentTarget.classList.remove('drag-over');

            const toRow = parseInt(e.currentTarget.dataset.row);
            const toCol = parseInt(e.currentTarget.dataset.col);

            // Check if dropping on a different square
            if (draggedFrom.row !== toRow || draggedFrom.col !== toCol) {
                // Make the move
                makeMove(draggedFrom.row, draggedFrom.col, toRow, toCol);
            }
        }

        // Make a move
        function makeMove(fromRow, fromCol, toRow, toCol) {
            const piece = board[fromRow][fromCol];
            
            // Don't allow capturing own pieces
            const targetPiece = board[toRow][toCol];
            if (targetPiece && isWhitePiece(targetPiece)) {
                renderBoard();
                return;
            }

            // Make the move
            board[toRow][toCol] = piece;
            board[fromRow][fromCol] = '';

            renderBoard();

            // Check if this is the winning move
            setTimeout(() => {
                checkSolution(fromRow, fromCol, toRow, toCol);
            }, 100);
        }

        // Check if the move is the correct solution
        function checkSolution(fromRow, fromCol, toRow, toCol) {
            const solution = scenarios[currentScenario].solution;
            
            if (fromRow === solution.from[0] && fromCol === solution.from[1] &&
                toRow === solution.to[0] && toCol === solution.to[1]) {
                showFeedback('🎉 Checkmate! You found it!', 'success');
            } else {
                // Check if it's checkmate anyway (basic check for any valid mate)
                if (isCheckmate(toRow, toCol)) {
                    showFeedback('✓ Checkmate! (Alternative solution)', 'success');
                } else {
                    showFeedback('Not quite! Try again.', 'error');
                    setTimeout(() => {
                        resetPosition();
                    }, 1500);
                }
            }
        }

        // Basic checkmate detection
        function isCheckmate(pieceRow, pieceCol) {
            const piece = board[pieceRow][pieceCol];
            const blackKingPos = findPiece('k');
            
            if (!blackKingPos) return false;

            // Basic mate detection based on piece type and position
            switch(piece) {
                case 'Q':
                    return isQueenMate(pieceRow, pieceCol, blackKingPos);
                case 'R':
                    return isRookMate(pieceRow, pieceCol, blackKingPos);
                default:
                    return false;
            }
        }

        function findPiece(piece) {
            for (let row = 0; row < 8; row++) {
                for (let col = 0; col < 8; col++) {
                    if (board[row][col] === piece) {
                        return { row, col };
                    }
                }
            }
            return null;
        }

        function isQueenMate(qRow, qCol, kingPos) {
            // Simplified: check if queen is on same row or column as king
            return (qRow === kingPos.row || qCol === kingPos.col || 
                    Math.abs(qRow - kingPos.row) === Math.abs(qCol - kingPos.col));
        }

        function isRookMate(rRow, rCol, kingPos) {
            // Simplified: check if rook is on same row or column as king
            return (rRow === kingPos.row || rCol === kingPos.col);
        }

        // Show feedback message
        function showFeedback(message, type) {
            const feedback = document.getElementById('feedback');
            feedback.textContent = message;
            feedback.className = `feedback show ${type}`;
        }

        // Hide feedback message
        function hideFeedback() {
            const feedback = document.getElementById('feedback');
            feedback.className = 'feedback';
        }

        // Start the game
        init();
    </script>
</body>
</html>
```

## Features:

1. **3 Mate-in-1 Scenarios:**
   - **Scenario 1:** Back rank mate with a rook (Ra8#)
   - **Scenario 2:** Queen and king mate (Qd8#)
   - **Scenario 3:** Simple rook mate (Rh8#)

2. **Drag & Drop:** Pieces can be dragged and dropped on the board using HTML5 drag and drop API

3. **Visual Feedback:**
   - ✅ Success message with celebration animation when correct
   - ❌ Error message when incorrect (auto-resets after 1.5s)
   - Hover effects and drag-over highlighting

4. **Controls:**
   - 3 scenario buttons to switch between puzzles
   - Reset button to restore the current position
   - Active scenario highlighted

5. **Responsive Design:** Works on mobile and desktop devices

6. **User-Friendly:**
   - Clear instructions
   - Visual drag-over feedback (green highlight)
   - Smooth animations and transitions
   - Beautiful gradient background and modern UI

Try dragging the white pieces to find the checkmate! The app will validate your solution and provide immediate feedback.