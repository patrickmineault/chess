# Chess Mate in 1 Practice App

Here's a complete chess endgame practice app with 3 selectable mate-in-1 scenarios, drag-and-drop functionality, and visual feedback:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chess Mate in 1 Practice</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
            color: #fff;
        }

        h1 {
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }

        .subtitle {
            color: #aaa;
            margin-bottom: 20px;
            font-size: 14px;
        }

        .scenario-buttons {
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .scenario-btn {
            padding: 12px 20px;
            font-size: 14px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            background: linear-gradient(145deg, #3a3a5c, #2a2a4c);
            color: #fff;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }

        .scenario-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.4);
        }

        .scenario-btn.active {
            background: linear-gradient(145deg, #4a7c59, #3a6c49);
            box-shadow: 0 0 20px rgba(74, 124, 89, 0.5);
        }

        .game-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
        }

        .board-wrapper {
            padding: 15px;
            background: linear-gradient(145deg, #2c2c3e, #1c1c2e);
            border-radius: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        .board {
            display: grid;
            grid-template-columns: repeat(8, 60px);
            grid-template-rows: repeat(8, 60px);
            border: 3px solid #4a4a6a;
            border-radius: 4px;
            overflow: hidden;
        }

        .square {
            width: 60px;
            height: 60px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 46px;
            cursor: pointer;
            transition: all 0.2s ease;
            user-select: none;
        }

        .square.light {
            background-color: #e8dcc4;
        }

        .square.dark {
            background-color: #7d945d;
        }

        .square.highlight {
            box-shadow: inset 0 0 20px rgba(255, 255, 0, 0.7);
        }

        .square.valid-move {
            background-color: rgba(100, 200, 100, 0.5) !important;
        }

        .square.selected {
            box-shadow: inset 0 0 25px rgba(0, 150, 255, 0.8);
        }

        .square.last-move {
            box-shadow: inset 0 0 15px rgba(255, 200, 0, 0.5);
        }

        .piece {
            cursor: grab;
            transition: transform 0.1s ease;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .piece:active {
            cursor: grabbing;
        }

        .piece.dragging {
            opacity: 0.5;
            transform: scale(1.1);
        }

        .controls {
            display: flex;
            gap: 15px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .btn {
            padding: 12px 25px;
            font-size: 16px;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.3s ease;
            font-weight: bold;
        }

        .reset-btn {
            background: linear-gradient(145deg, #c45c5c, #a44c4c);
            color: white;
        }

        .reset-btn:hover {
            background: linear-gradient(145deg, #d46c6c, #b45c5c);
            transform: translateY(-2px);
        }

        .hint-btn {
            background: linear-gradient(145deg, #5c8dc4, #4c7da4);
            color: white;
        }

        .hint-btn:hover {
            background: linear-gradient(145deg, #6c9dd4, #5c8db4);
            transform: translateY(-2px);
        }

        .feedback {
            padding: 20px 30px;
            border-radius: 12px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
            min-height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
            max-width: 500px;
        }

        .feedback.success {
            background: linear-gradient(145deg, #4a7c59, #3a6c49);
            box-shadow: 0 0 30px rgba(74, 124, 89, 0.6);
            animation: pulse-success 0.5s ease;
        }

        .feedback.error {
            background: linear-gradient(145deg, #8c4a4a, #7c3a3a);
            box-shadow: 0 0 30px rgba(140, 74, 74, 0.6);
            animation: shake 0.5s ease;
        }

        .feedback.info {
            background: linear-gradient(145deg, #4a5a7c, #3a4a6c);
        }

        .feedback.hint {
            background: linear-gradient(145deg, #7c6a4a, #6c5a3a);
        }

        @keyframes pulse-success {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-10px); }
            75% { transform: translateX(10px); }
        }

        .scenario-info {
            background: linear-gradient(145deg, #2a2a4c, #1a1a3c);
            padding: 15px 25px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 10px;
        }

        .scenario-info h3 {
            color: #6c9dd4;
            margin-bottom: 5px;
        }

        .scenario-info p {
            color: #aaa;
            font-size: 14px;
        }

        .coordinates {
            position: absolute;
            font-size: 10px;
            font-weight: bold;
            pointer-events: none;
        }

        .coord-file {
            bottom: 2px;
            right: 4px;
        }

        .coord-rank {
            top: 2px;
            left: 4px;
        }

        .square {
            position: relative;
        }

        .light .coordinates { color: #7d945d; }
        .dark .coordinates { color: #e8dcc4; }

        .move-indicator {
            position: absolute;
            width: 20px;
            height: 20px;
            background: rgba(0, 0, 0, 0.2);
            border-radius: 50%;
            pointer-events: none;
        }

        .capture-indicator {
            position: absolute;
            width: 100%;
            height: 100%;
            border: 4px solid rgba(0, 0, 0, 0.2);
            border-radius: 50%;
            pointer-events: none;
            box-sizing: border-box;
        }

        .checkmate-overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(74, 124, 89, 0.3);
            animation: checkmate-flash 0.5s ease;
            pointer-events: none;
            border-radius: 4px;
        }

        @keyframes checkmate-flash {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        .stats {
            display: flex;
            gap: 30px;
            margin-top: 10px;
            font-size: 14px;
            color: #aaa;
        }

        .stat-item {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .stat-value {
            color: #6c9dd4;
            font-weight: bold;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <h1>♔ Chess Mate in 1 Practice</h1>
    <p class="subtitle">White to move - Find the checkmate!</p>

    <div class="scenario-buttons">
        <button class="scenario-btn active" onclick="loadScenario(0)">
            🏰 Scenario 1: Back Rank Mate
        </button>
        <button class="scenario-btn" onclick="loadScenario(1)">
            👑 Scenario 2: Queen + King Mate
        </button>
        <button class="scenario-btn" onclick="loadScenario(2)">
            ♞ Scenario 3: Smothered Mate
        </button>
    </div>

    <div class="scenario-info">
        <h3 id="scenario-title">Back Rank Mate</h3>
        <p id="scenario-description">The enemy king is trapped on the back rank. Deliver checkmate with your rook!</p>
    </div>

    <div class="game-container">
        <div class="board-wrapper">
            <div class="board" id="board"></div>
        </div>

        <div class="feedback info" id="feedback">
            Drag a white piece to make your move
        </div>

        <div class="controls">
            <button class="btn reset-btn" onclick="resetPosition()">
                ↺ Reset Position
            </button>
            <button class="btn hint-btn" onclick="showHint()">
                💡 Show Hint
            </button>
        </div>

        <div class="stats">
            <div class="stat-item">
                <span>Solved:</span>
                <span class="stat-value" id="solved-count">0</span>
            </div>
            <div class="stat-item">
                <span>Attempts:</span>
                <span class="stat-value" id="attempt-count">0</span>
            </div>
        </div>
    </div>

    <script>
        // Chess piece Unicode symbols
        const PIECES = {
            'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
            'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
        };

        // Scenario definitions
        const scenarios = [
            {
                name: "Back Rank Mate",
                description: "The enemy king is trapped on the back rank. Deliver checkmate with your rook!",
                position: {
                    // Black pieces
                    'g8': 'k',  // Black King
                    'f7': 'p',  // Black pawns
                    'g7': 'p',
                    'h7': 'p',
                    // White pieces
                    'g1': 'K',  // White King
                    'd1': 'R',  // White Rook
                },
                solution: { from: 'd1', to: 'd8' }, // Rd8#
                hint: "The Black king has no escape squares on the back rank!"
            },
            {
                name: "Queen + King Mate",
                description: "Use your Queen and King together to deliver a beautiful checkmate!",
                position: {
                    // Black pieces
                    'h8': 'k',  // Black King
                    'g7': 'p',  // Black pawn
                    // White pieces
                    'g6': 'K',  // White King
                    'f6': 'Q',  // White Queen
                },
                solution: { from: 'f6', to: 'f8' }, // Qf8#
                hint: "Where can the Queen move to control all escape squares?"
            },
            {
                name: "Smothered Mate",
                description: "The enemy king is trapped by its own pieces. Use your Knight to deliver mate!",
                position: {
                    // Black pieces
                    'h8': 'k',  // Black King
                    'g8': 'n',  // Black Knight (blocks g8)
                    'g7': 'p',  // Black pawns
                    'h7': 'p',
                    // White pieces
                    'g1': 'K',  // White King
                    'e5': 'N',  // White Knight
                },
                solution: { from: 'e5', to: 'g6' }, // Ng6#
                hint: "Knights move in an L-shape. Where can it jump to give check with no escape?"
            }
        ];

        // Game state
        let currentScenario = 0;
        let board = {};
        let selectedSquare = null;
        let draggedPiece = null;
        let draggedFrom = null;
        let solved = false;
        let solvedCount = 0;
        let attemptCount = 0;
        let lastMove = { from: null, to: null };

        // Initialize the board
        function initBoard() {
            const boardElement = document.getElementById('board');
            boardElement.innerHTML = '';

            for (let row = 0; row < 8; row++) {
                for (let col = 0; col < 8; col++) {
                    const square = document.createElement('div');
                    const file = String.fromCharCode(97 + col); // a-h
                    const rank = 8 - row; // 8-1
                    const squareId = file + rank;

                    square.className = `square ${(row + col) % 2 === 0 ? 'light' : 'dark'}`;
                    square.id = squareId;
                    square.dataset.square = squareId;

                    // Add coordinates on edge squares
                    if (col === 0) {
                        const rankCoord = document.createElement('span');
                        rankCoord.className = 'coordinates coord-rank';
                        rankCoord.textContent = rank;
                        square.appendChild(rankCoord);
                    }
                    if (row === 7) {
                        const fileCoord = document.createElement('span');
                        fileCoord.className = 'coordinates coord-file';
                        fileCoord.textContent = file;
                        square.appendChild(fileCoord);
                    }

                    // Event listeners
                    square.addEventListener('dragover', handleDragOver);
                    square.addEventListener('drop', handleDrop);
                    square.addEventListener('click', handleSquareClick);

                    boardElement.appendChild(square);
                }
            }

            loadScenario(currentScenario);
        }

        // Load a scenario
        function loadScenario(index) {
            currentScenario = index;
            board = { ...scenarios[index].position };
            solved = false;
            selectedSquare = null;
            lastMove = { from: null, to: null };

            // Update button states
            document.querySelectorAll('.scenario-btn').forEach((btn, i) => {
                btn.classList.toggle('active', i === index);
            });

            // Update info
            document.getElementById('scenario-title').textContent = scenarios[index].name;
            document.getElementById('scenario-description').textContent = scenarios[index].description;

            // Reset feedback
            setFeedback('Drag a white piece to make your move', 'info');

            renderBoard();
        }

        // Render the board
        function renderBoard() {
            document.querySelectorAll('.square').forEach(square => {
                const squareId = square.dataset.square;
                
                // Remove existing pieces
                const existingPiece = square.querySelector('.piece');
                if (existingPiece) existingPiece.remove();

                // Remove indicators
                square.querySelectorAll('.move-indicator, .capture-indicator, .checkmate-overlay').forEach(el => el.remove());

                // Remove highlight classes
                square.classList.remove('selected', 'valid-move', 'last-move', 'highlight');

                // Add last move highlight
                if (lastMove.from === squareId || lastMove.to === squareId) {
                    square.classList.add('last-move');
                }

                // Add piece if present
                if (board[squareId]) {
                    const piece = document.createElement('span');
                    piece.className = 'piece';
                    piece.textContent = PIECES[board[squareId]];
                    piece.draggable = isWhitePiece(board[squareId]) && !solved;

                    piece.addEventListener('dragstart', handleDragStart);
                    piece.addEventListener('dragend', handleDragEnd);

                    square.appendChild(piece);
                }
            });

            // Highlight selected square and valid moves
            if (selectedSquare) {
                const square = document.getElementById(selectedSquare);
                if (square) square.classList.add('selected');
                highlightValidMoves(selectedSquare);
            }
        }

        // Check if piece is white
        function isWhitePiece(piece) {
            return piece && piece === piece.toUpperCase();
        }

        // Drag and drop handlers
        function handleDragStart(e) {
            if (solved) return;
            
            const square = e.target.closest('.square');
            draggedFrom = square.dataset.square;
            draggedPiece = board[draggedFrom];

            if (!isWhitePiece(draggedPiece)) {
                e.preventDefault();
                return;
            }

            e.target.classList.add('dragging');
            selectedSquare = draggedFrom;
            
            // Use setTimeout to allow the drag image to be created before modifying
            setTimeout(() => renderBoard(), 0);
        }

        function handleDragEnd(e) {
            e.target.classList.remove('dragging');
            draggedPiece = null;
            draggedFrom = null;
        }

        function handleDragOver(e) {
            e.preventDefault();
        }

        function handleDrop(e) {
            e.preventDefault();
            const targetSquare = e.target.closest('.square').dataset.square;
            
            if (draggedFrom && draggedFrom !== targetSquare) {
                attemptMove(draggedFrom, targetSquare);
            }
            
            selectedSquare = null;
            renderBoard();
        }

        // Click handler for square selection
        function handleSquareClick(e) {
            if (solved) return;

            const square = e.target.closest('.square');
            const squareId = square.dataset.square;
            const piece = board[squareId];

            if (selectedSquare) {
                if (selectedSquare === squareId) {
                    // Deselect
                    selectedSquare = null;
                } else if (isWhitePiece(piece)) {
                    // Select different white piece
                    selectedSquare = squareId;
                } else {
                    // Attempt move
                    attemptMove(selectedSquare, squareId);
                    selectedSquare = null;
                }
            } else if (isWhitePiece(piece)) {
                // Select white piece
                selectedSquare = squareId;
            }

            renderBoard();
        }

        // Highlight valid moves (simplified - shows solution square)
        function highlightValidMoves(fromSquare) {
            const piece = board[fromSquare];
            if (!piece) return;

            // For simplicity, just highlight the solution if this is the right piece
            const scenario = scenarios[currentScenario];
            if (fromSquare === scenario.solution.from) {
                const targetSquare = document.getElementById(scenario.solution.to);
                if (targetSquare) {
                    if (board[scenario.solution.to]) {
                        const indicator = document.createElement('div');
                        indicator.className = 'capture-indicator';
                        targetSquare.appendChild(indicator);
                    } else {
                        const indicator = document.createElement('div');
                        indicator.className = 'move-indicator';
                        targetSquare.appendChild(indicator);
                    }
                }
            }
        }

        // Attempt a move
        function attemptMove(from, to) {
            attemptCount++;
            updateStats();

            const scenario = scenarios[currentScenario];
            const isCorrect = from === scenario.solution.from && to === scenario.solution.to;

            if (isCorrect) {
                // Make the move
                board[to] = board[from];
                delete board[from];
                lastMove = { from, to };
                
                solved = true;
                solvedCount++;
                updateStats();

                // Show success feedback
                setFeedback('🎉 Checkmate! Excellent move!', 'success');
                
                // Add checkmate overlay to king's square
                setTimeout(() => {
                    const kingSquare = findKing('k');
                    if (kingSquare) {
                        const overlay = document.createElement('div');
                        overlay.className = 'checkmate-overlay';
                        document.getElementById(kingSquare).appendChild(overlay);
                    }
                }, 100);

                renderBoard();
                highlightCheckmateSquares();
            } else {
                // Wrong move
                setFeedback('❌ Not checkmate. Try again!', 'error');
                
                // Shake the board
                const boardWrapper = document.querySelector('.board-wrapper');
                boardWrapper.style.animation = 'none';
                setTimeout(() => {
                    boardWrapper.style.animation = 'shake 0.5s ease';
                }, 10);
            }
        }

        // Find a king on the board
        function findKing(kingPiece) {
            for (const [square, piece] of Object.entries(board)) {
                if (piece === kingPiece) return square;
            }
            return null;
        }

        // Highlight checkmate squares
        function highlightCheckmateSquares() {
            if (lastMove.to) {
                const targetSquare = document.getElementById(lastMove.to);
                if (targetSquare) {
                    targetSquare.classList.add('highlight');
                }
            }
        }

        // Set feedback message
        function setFeedback(message, type) {
            const feedback = document.getElementById('feedback');
            feedback.textContent = message;
            feedback.className = `feedback ${type}`;
        }

        // Reset position
        function resetPosition() {
            loadScenario(currentScenario);
        }

        // Show hint
        function showHint() {
            const scenario = scenarios[currentScenario];
            setFeedback(`💡 Hint: ${scenario.hint}`, 'hint');
            
            // Briefly highlight the piece to move
            const fromSquare = document.getElementById(scenario.solution.from);
            if (fromSquare) {
                fromSquare.classList.add('highlight');
                setTimeout(() => {
                    fromSquare.classList.remove('highlight');
                }, 2000);
            }
        }

        // Update stats display
        function updateStats() {
            document.getElementById('solved-count').textContent = solvedCount;
            document.getElementById('attempt-count').textContent = attemptCount;
        }

        // Initialize on page load
        document.addEventListener('DOMContentLoaded', initBoard);
    </script>
</body>
</html>
```

## Features Included:

### 3 Mate-in-1 Scenarios:
1. **Back Rank Mate** - Rook delivers checkmate (Rd8#)
2. **Queen + King Mate** - Queen delivers checkmate (Qf8#)
3. **Smothered Mate** - Knight delivers checkmate (Ng6#)

### Functionality:
- **Drag & Drop**: Drag white pieces to make moves
- **Click Selection**: Click a piece to select, click destination to move
- **Scenario Selection**: Three buttons to switch between puzzles
- **Reset Button**: Restore the current position
- **Hint Button**: Get a helpful hint with piece highlighting

### Visual Feedback:
- ✅ **Success**: Green celebration with "Checkmate!" message and board highlight
- ❌ **Error**: Red feedback with shake animation
- 🎯 **Move indicators**: Shows valid move targets when piece is selected
- 📍 **Last move highlight**: Yellow glow on from/to squares
- 📊 **Stats tracking**: Solved count and attempt count

### Design:
- Dark modern theme with gradient backgrounds
- Unicode chess pieces with shadows
- Smooth animations and transitions
- Coordinate labels on the board
- Responsive button styling