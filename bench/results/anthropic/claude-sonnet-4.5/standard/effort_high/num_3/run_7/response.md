# Chess Endgame Practice App

Here's a complete chess endgame practice app with drag-and-drop functionality:

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
            font-size: 14px;
        }

        .scenario-selector {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
        }

        .scenario-btn {
            flex: 1;
            padding: 12px;
            background: #f0f0f0;
            border: 2px solid #ddd;
            border-radius: 8px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s;
            min-width: 150px;
        }

        .scenario-btn:hover {
            background: #e0e0e0;
            transform: translateY(-2px);
        }

        .scenario-btn.active {
            background: #667eea;
            color: white;
            border-color: #667eea;
        }

        .board-container {
            display: inline-block;
            border: 3px solid #333;
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 20px;
        }

        .chessboard {
            display: grid;
            grid-template-columns: repeat(8, 60px);
            grid-template-rows: repeat(8, 60px);
            gap: 0;
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

        .square.dragging {
            opacity: 0.5;
        }

        .square.drag-over {
            background-color: #87ceeb !important;
        }

        .square.highlight {
            box-shadow: inset 0 0 0 3px #ffeb3b;
        }

        .piece {
            cursor: grab;
            transition: transform 0.1s;
        }

        .piece:active {
            cursor: grabbing;
            transform: scale(1.1);
        }

        .controls {
            display: flex;
            gap: 10px;
            margin-top: 20px;
        }

        .btn {
            flex: 1;
            padding: 12px 24px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-size: 16px;
            transition: all 0.3s;
        }

        .btn:hover {
            background: #5568d3;
            transform: translateY(-2px);
        }

        .btn:active {
            transform: translateY(0);
        }

        .feedback {
            margin-top: 20px;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            opacity: 0;
            transition: opacity 0.3s;
        }

        .feedback.show {
            opacity: 1;
        }

        .feedback.success {
            background: #4caf50;
            color: white;
        }

        .feedback.error {
            background: #f44336;
            color: white;
        }

        .info {
            text-align: center;
            color: #666;
            margin-bottom: 15px;
            font-size: 14px;
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
        <p class="subtitle">Find the Mate in 1 for White</p>
        
        <div class="scenario-selector">
            <button class="scenario-btn active" onclick="loadScenario(1)">Scenario 1<br>Back Rank Mate</button>
            <button class="scenario-btn" onclick="loadScenario(2)">Scenario 2<br>Queen Mate</button>
            <button class="scenario-btn" onclick="loadScenario(3)">Scenario 3<br>Rook Mate</button>
        </div>

        <div class="info" id="scenarioInfo">Drag a white piece to deliver checkmate!</div>

        <div class="board-container">
            <div class="chessboard" id="chessboard"></div>
        </div>

        <div class="controls">
            <button class="btn" onclick="resetPosition()">↺ Reset Position</button>
        </div>

        <div class="feedback" id="feedback"></div>
    </div>

    <script>
        // Chess pieces unicode characters
        const pieces = {
            'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
            'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
        };

        // Three mate-in-1 scenarios
        const scenarios = {
            1: {
                name: "Back Rank Mate",
                position: [
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', 'K', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['p', 'p', 'p', '', '', '', '', ''],
                    ['k', '', '', 'R', '', '', '', '']
                ],
                solution: { from: [7, 3], to: [7, 0] }, // Rook from d1 to a1
                description: "Move the rook to a1 for back rank mate!"
            },
            2: {
                name: "Queen Mate",
                position: [
                    ['', '', '', '', 'k', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', 'K', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', 'Q', '', '', ''],
                    ['', '', '', '', '', '', '', '']
                ],
                solution: { from: [6, 4], to: [0, 4] }, // Queen from e2 to e8
                description: "Move the queen to e8 for checkmate!"
            },
            3: {
                name: "Rook and King Mate",
                position: [
                    ['', '', '', '', '', '', 'k', ''],
                    ['', '', '', '', '', '', '', 'K'],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['R', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', '']
                ],
                solution: { from: [6, 0], to: [0, 0] }, // Rook from a2 to a8
                description: "Move the rook to a8 for checkmate!"
            }
        };

        let currentScenario = 1;
        let currentPosition = [];
        let draggedPiece = null;
        let draggedFrom = null;

        function initBoard() {
            const board = document.getElementById('chessboard');
            board.innerHTML = '';
            
            for (let row = 0; row < 8; row++) {
                for (let col = 0; col < 8; col++) {
                    const square = document.createElement('div');
                    square.className = `square ${(row + col) % 2 === 0 ? 'light' : 'dark'}`;
                    square.dataset.row = row;
                    square.dataset.col = col;
                    
                    const piece = currentPosition[row][col];
                    if (piece) {
                        const pieceSpan = document.createElement('span');
                        pieceSpan.className = 'piece';
                        pieceSpan.textContent = pieces[piece];
                        pieceSpan.draggable = isWhitePiece(piece);
                        
                        if (isWhitePiece(piece)) {
                            pieceSpan.addEventListener('dragstart', handleDragStart);
                        }
                        
                        square.appendChild(pieceSpan);
                    }
                    
                    square.addEventListener('dragover', handleDragOver);
                    square.addEventListener('drop', handleDrop);
                    square.addEventListener('dragleave', handleDragLeave);
                    
                    board.appendChild(square);
                }
            }
        }

        function isWhitePiece(piece) {
            return piece === piece.toUpperCase() && piece !== '';
        }

        function handleDragStart(e) {
            const square = e.target.parentElement;
            draggedPiece = e.target;
            draggedFrom = {
                row: parseInt(square.dataset.row),
                col: parseInt(square.dataset.col)
            };
            square.classList.add('dragging');
            e.dataTransfer.effectAllowed = 'move';
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
            
            const toSquare = e.currentTarget;
            const toRow = parseInt(toSquare.dataset.row);
            const toCol = parseInt(toSquare.dataset.col);
            
            // Remove dragging class
            const fromSquare = document.querySelector('.dragging');
            if (fromSquare) {
                fromSquare.classList.remove('dragging');
            }
            
            // Make the move
            makeMove(draggedFrom.row, draggedFrom.col, toRow, toCol);
        }

        function makeMove(fromRow, fromCol, toRow, toCol) {
            const piece = currentPosition[fromRow][fromCol];
            
            // Update position
            currentPosition[toRow][toCol] = piece;
            currentPosition[fromRow][fromCol] = '';
            
            // Redraw board
            initBoard();
            
            // Check if this is the correct solution
            const solution = scenarios[currentScenario].solution;
            if (fromRow === solution.from[0] && fromCol === solution.from[1] &&
                toRow === solution.to[0] && toCol === solution.to[1]) {
                showFeedback('success', '🎉 Checkmate! Well done!');
                highlightSquares([fromRow, fromCol], [toRow, toCol]);
            } else {
                showFeedback('error', '❌ Not quite! Try again.');
                setTimeout(resetPosition, 1500);
            }
        }

        function highlightSquares(from, to) {
            const squares = document.querySelectorAll('.square');
            squares.forEach(square => {
                const row = parseInt(square.dataset.row);
                const col = parseInt(square.dataset.col);
                if ((row === from[0] && col === from[1]) || (row === to[0] && col === to[1])) {
                    square.classList.add('highlight');
                }
            });
        }

        function showFeedback(type, message) {
            const feedback = document.getElementById('feedback');
            feedback.className = `feedback ${type} show`;
            feedback.textContent = message;
            
            if (type === 'error') {
                setTimeout(() => {
                    feedback.classList.remove('show');
                }, 1500);
            }
        }

        function loadScenario(scenarioNum) {
            currentScenario = scenarioNum;
            
            // Update button states
            const buttons = document.querySelectorAll('.scenario-btn');
            buttons.forEach((btn, index) => {
                btn.classList.toggle('active', index + 1 === scenarioNum);
            });
            
            // Update info
            document.getElementById('scenarioInfo').textContent = 
                scenarios[scenarioNum].description;
            
            // Reset feedback
            const feedback = document.getElementById('feedback');
            feedback.classList.remove('show');
            
            resetPosition();
        }

        function resetPosition() {
            // Deep copy the scenario position
            currentPosition = scenarios[currentScenario].position.map(row => [...row]);
            
            // Hide feedback
            const feedback = document.getElementById('feedback');
            feedback.classList.remove('show');
            
            initBoard();
        }

        // Initialize on load
        loadScenario(1);
    </script>
</body>
</html>
```

## Features:

### 🎯 **Three Mate-in-1 Scenarios:**
1. **Back Rank Mate** - Rook delivers mate on the back rank
2. **Queen Mate** - Queen delivers mate on the 8th rank
3. **Rook and King Mate** - Rook delivers mate with king support

### 🎨 **Visual Features:**
- Beautiful gradient background
- Responsive chess board
- Drag-and-drop piece movement
- Visual feedback on drag (blue highlight)
- Success/error messages with animations
- Active scenario highlighting
- Move highlighting after successful checkmate

### 🎮 **User Interactions:**
- **Drag & Drop**: Click and drag white pieces to make moves
- **Scenario Selection**: Switch between three different puzzles
- **Reset Button**: Restore the current position
- **Instant Feedback**: Know immediately if you found the right move

### ✨ **How It Works:**
1. Select a scenario from the buttons at the top
2. Drag a white piece to deliver checkmate
3. If correct, you'll see a success message and highlighted squares
4. If incorrect, the position resets automatically after 1.5 seconds
5. Click "Reset Position" anytime to start over

The app is fully self-contained in a single HTML file and works in any modern browser!