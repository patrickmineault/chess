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
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .container {
            background: white;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
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
            font-size: 14px;
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
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .scenario-btn.active {
            background: #4c51bf;
            box-shadow: 0 5px 15px rgba(76, 81, 191, 0.4);
        }

        .reset-btn {
            background: #f56565;
            color: white;
        }

        .reset-btn:hover {
            background: #e53e3e;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(245, 101, 101, 0.4);
        }

        .board-container {
            display: inline-block;
            border: 3px solid #333;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }

        .chessboard {
            display: grid;
            grid-template-columns: repeat(8, 60px);
            grid-template-rows: repeat(8, 60px);
            margin: 0 auto;
        }

        .square {
            width: 60px;
            height: 60px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 40px;
            cursor: pointer;
            position: relative;
            user-select: none;
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

        .square.check {
            background-color: #ff6b6b !important;
        }

        .square.dragging {
            opacity: 0.5;
        }

        .piece {
            cursor: grab;
            transition: transform 0.1s;
        }

        .piece:hover {
            transform: scale(1.1);
        }

        .piece:active {
            cursor: grabbing;
        }

        .feedback {
            margin-top: 20px;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            font-size: 18px;
            font-weight: 600;
            display: none;
            animation: slideIn 0.5s;
        }

        .feedback.success {
            background: #48bb78;
            color: white;
            display: block;
        }

        .feedback.error {
            background: #f56565;
            color: white;
            display: block;
        }

        .feedback.info {
            background: #4299e1;
            color: white;
            display: block;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateY(-10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .scenario-description {
            background: #edf2f7;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            text-align: center;
            color: #2d3748;
            font-weight: 500;
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

            .container {
                padding: 15px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>♔ Chess Endgame Practice ♔</h1>
        <p class="subtitle">Find the mate in 1 for White!</p>
        
        <div class="controls">
            <button class="scenario-btn active" onclick="loadScenario(1)">Scenario 1</button>
            <button class="scenario-btn" onclick="loadScenario(2)">Scenario 2</button>
            <button class="scenario-btn" onclick="loadScenario(3)">Scenario 3</button>
            <button class="reset-btn" onclick="resetPosition()">Reset Position</button>
        </div>

        <div class="scenario-description" id="description">
            Back Rank Mate - Move the white rook to deliver checkmate!
        </div>

        <div class="board-container">
            <div class="chessboard" id="chessboard"></div>
        </div>

        <div class="feedback" id="feedback"></div>
    </div>

    <script>
        // Chess pieces in Unicode
        const pieces = {
            'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
            'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
        };

        // Scenarios: each position is an 8x8 array (rank 8 to rank 1)
        const scenarios = {
            1: {
                name: "Back Rank Mate",
                description: "Back Rank Mate - Move the white rook to deliver checkmate!",
                position: [
                    ['r', '', '', '', 'k', '', '', 'r'],  // rank 8
                    ['p', 'p', 'p', '', '', 'p', 'p', 'p'],  // rank 7
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', 'R', '', '', 'K']   // rank 1
                ],
                solution: { from: [7, 4], to: [0, 4] } // Re1 to e8#
            },
            2: {
                name: "Queen Mate on the Edge",
                description: "Queen and King Mate - Deliver checkmate with the queen!",
                position: [
                    ['', '', '', '', '', '', '', 'k'],  // rank 8
                    ['', '', '', '', '', '', 'K', ''],  // rank 7
                    ['', '', '', '', '', 'Q', '', ''],  // rank 6
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '']   // rank 1
                ],
                solution: { from: [2, 5], to: [1, 6] } // Qf6 to g7#
            },
            3: {
                name: "Rook and King Mate",
                description: "Rook and King Mate - Use the rook to deliver checkmate!",
                position: [
                    ['', '', '', '', '', '', 'k', ''],  // rank 8
                    ['', '', '', '', '', '', '', ''],  // rank 7
                    ['', '', '', '', '', 'K', '', ''],  // rank 6
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', 'R', '', '', '', '', '', '']   // rank 1
                ],
                solution: { from: [7, 1], to: [0, 1] } // Rb1 to b8#
            }
        };

        let currentScenario = 1;
        let board = [];
        let draggedPiece = null;
        let draggedFrom = null;

        function initBoard() {
            const chessboard = document.getElementById('chessboard');
            chessboard.innerHTML = '';
            board = JSON.parse(JSON.stringify(scenarios[currentScenario].position));

            for (let row = 0; row < 8; row++) {
                for (let col = 0; col < 8; col++) {
                    const square = document.createElement('div');
                    square.className = `square ${(row + col) % 2 === 0 ? 'light' : 'dark'}`;
                    square.dataset.row = row;
                    square.dataset.col = col;

                    const piece = board[row][col];
                    if (piece) {
                        const pieceElement = document.createElement('span');
                        pieceElement.textContent = pieces[piece];
                        pieceElement.className = 'piece';
                        pieceElement.draggable = isWhitePiece(piece);
                        
                        if (isWhitePiece(piece)) {
                            pieceElement.addEventListener('dragstart', handleDragStart);
                        }
                        
                        square.appendChild(pieceElement);
                    }

                    square.addEventListener('dragover', handleDragOver);
                    square.addEventListener('drop', handleDrop);
                    square.addEventListener('dragleave', handleDragLeave);

                    chessboard.appendChild(square);
                }
            }
            
            hideFeedback();
        }

        function isWhitePiece(piece) {
            return piece === piece.toUpperCase() && piece !== '';
        }

        function handleDragStart(e) {
            const square = e.target.parentElement;
            draggedPiece = e.target.textContent;
            draggedFrom = {
                row: parseInt(square.dataset.row),
                col: parseInt(square.dataset.col)
            };
            
            e.target.parentElement.classList.add('dragging');
            e.dataTransfer.effectAllowed = 'move';
        }

        function handleDragOver(e) {
            e.preventDefault();
            e.dataTransfer.dropEffect = 'move';
            e.currentTarget.classList.add('highlight');
        }

        function handleDragLeave(e) {
            e.currentTarget.classList.remove('highlight');
        }

        function handleDrop(e) {
            e.preventDefault();
            e.currentTarget.classList.remove('highlight');

            if (!draggedPiece) return;

            const toRow = parseInt(e.currentTarget.dataset.row);
            const toCol = parseInt(e.currentTarget.dataset.col);

            // Remove dragging effect
            document.querySelectorAll('.square').forEach(sq => sq.classList.remove('dragging'));

            // Make the move
            makeMove(draggedFrom.row, draggedFrom.col, toRow, toCol);

            draggedPiece = null;
            draggedFrom = null;
        }

        function makeMove(fromRow, fromCol, toRow, toCol) {
            const piece = board[fromRow][fromCol];
            
            // Move the piece
            board[toRow][toCol] = piece;
            board[fromRow][fromCol] = '';

            // Redraw board
            initBoard();

            // Check if it's checkmate
            checkForMate(fromRow, fromCol, toRow, toCol);
        }

        function checkForMate(fromRow, fromCol, toRow, toCol) {
            const solution = scenarios[currentScenario].solution;
            
            // Check if the move matches the solution
            if (fromRow === solution.from[0] && fromCol === solution.from[1] &&
                toRow === solution.to[0] && toCol === solution.to[1]) {
                
                showFeedback('success', '🎉 Checkmate! Excellent move! 🎉');
                highlightKingInCheck();
            } else {
                // Check if king is attacked (for partial credit feedback)
                if (isKingAttacked(toRow, toCol)) {
                    showFeedback('error', '⚠️ Good try, but that\'s not checkmate. The king can escape!');
                } else {
                    showFeedback('error', '❌ Not quite! Try again.');
                }
            }
        }

        function isKingAttacked(pieceRow, pieceCol) {
            // Find black king
            let kingPos = null;
            for (let row = 0; row < 8; row++) {
                for (let col = 0; col < 8; col++) {
                    if (board[row][col] === 'k') {
                        kingPos = { row, col };
                        break;
                    }
                }
                if (kingPos) break;
            }

            if (!kingPos) return false;

            const piece = board[pieceRow][pieceCol];
            
            // Check if the moved piece attacks the king
            if (piece === 'R') {
                // Rook attacks on same row or column
                if (pieceRow === kingPos.row || pieceCol === kingPos.col) {
                    return isPathClear(pieceRow, pieceCol, kingPos.row, kingPos.col);
                }
            } else if (piece === 'Q') {
                // Queen attacks on row, column, or diagonal
                if (pieceRow === kingPos.row || pieceCol === kingPos.col ||
                    Math.abs(pieceRow - kingPos.row) === Math.abs(pieceCol - kingPos.col)) {
                    return isPathClear(pieceRow, pieceCol, kingPos.row, kingPos.col);
                }
            }

            return false;
        }

        function isPathClear(fromRow, fromCol, toRow, toCol) {
            const rowStep = toRow > fromRow ? 1 : (toRow < fromRow ? -1 : 0);
            const colStep = toCol > fromCol ? 1 : (toCol < fromCol ? -1 : 0);
            
            let currentRow = fromRow + rowStep;
            let currentCol = fromCol + colStep;

            while (currentRow !== toRow || currentCol !== toCol) {
                if (board[currentRow][currentCol] !== '') {
                    return false;
                }
                currentRow += rowStep;
                currentCol += colStep;
            }

            return true;
        }

        function highlightKingInCheck() {
            // Find and highlight the black king
            for (let row = 0; row < 8; row++) {
                for (let col = 0; col < 8; col++) {
                    if (board[row][col] === 'k') {
                        const squares = document.querySelectorAll('.square');
                        const index = row * 8 + col;
                        squares[index].classList.add('check');
                    }
                }
            }
        }

        function showFeedback(type, message) {
            const feedback = document.getElementById('feedback');
            feedback.className = `feedback ${type}`;
            feedback.textContent = message;
        }

        function hideFeedback() {
            const feedback = document.getElementById('feedback');
            feedback.className = 'feedback';
            feedback.style.display = 'none';
        }

        function loadScenario(scenarioNum) {
            currentScenario = scenarioNum;
            
            // Update button states
            document.querySelectorAll('.scenario-btn').forEach((btn, index) => {
                btn.classList.toggle('active', index + 1 === scenarioNum);
            });

            // Update description
            document.getElementById('description').textContent = scenarios[scenarioNum].description;

            initBoard();
        }

        function resetPosition() {
            initBoard();
        }

        // Initialize on load
        initBoard();
    </script>
</body>
</html>
```

## Features:

### **3 Mate-in-1 Scenarios:**
1. **Back Rank Mate** - White rook delivers mate on the back rank (Re1-e8#)
2. **Queen and King Mate** - Queen delivers mate with king support (Qf6-g7#)
3. **Rook and King Mate** - Rook delivers mate on the edge (Rb1-b8#)

### **Functionality:**
- ✅ **Drag & Drop** - Drag white pieces to move them
- ✅ **Visual Feedback** - Success (green), Error (red) messages
- ✅ **Scenario Selection** - Click buttons to switch between puzzles
- ✅ **Reset Button** - Reset current position
- ✅ **Highlighted Checks** - King highlights in red when checkmated
- ✅ **Responsive Design** - Works on mobile devices
- ✅ **Beautiful UI** - Modern gradient background and smooth animations

### **How to Use:**
1. Save as an `.html` file
2. Open in any modern browser
3. Drag white pieces to find the checkmate
4. Get instant feedback on your move
5. Try all 3 scenarios!

The app provides helpful feedback even for incorrect moves, distinguishing between moves that give check (but not mate) and moves that don't threaten the king at all.