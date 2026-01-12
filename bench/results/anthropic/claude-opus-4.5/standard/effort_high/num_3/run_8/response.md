# Chess Mate-in-1 Practice App

Here's a complete chess endgame practice app with three mate-in-1 scenarios, drag-and-drop functionality, and visual feedback.

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
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        
        .container {
            text-align: center;
            max-width: 600px;
        }
        
        h1 {
            color: #fff;
            margin-bottom: 20px;
            font-size: 2rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        
        .scenario-selector {
            margin-bottom: 20px;
            display: flex;
            gap: 10px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        .scenario-btn {
            padding: 12px 20px;
            font-size: 14px;
            cursor: pointer;
            border: none;
            border-radius: 8px;
            background: linear-gradient(145deg, #4a4a8a, #3a3a6a);
            color: white;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        
        .scenario-btn:hover {
            background: linear-gradient(145deg, #5a5a9a, #4a4a7a);
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.4);
        }
        
        .scenario-btn.active {
            background: linear-gradient(145deg, #7a7aca, #6a6aba);
            box-shadow: 0 0 20px rgba(122, 122, 202, 0.5);
        }
        
        .description {
            color: #aaa;
            margin-bottom: 20px;
            font-style: italic;
            padding: 0 20px;
            line-height: 1.5;
            min-height: 50px;
        }
        
        .board-container {
            display: inline-block;
            padding: 15px;
            background: linear-gradient(145deg, #8b5a2b, #6b3a1b);
            border-radius: 12px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.5);
        }
        
        .board {
            display: grid;
            grid-template-columns: repeat(8, 60px);
            border: 3px solid #4a2a0a;
            border-radius: 4px;
            overflow: hidden;
        }
        
        .square {
            width: 60px;
            height: 60px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 48px;
            cursor: pointer;
            user-select: none;
            position: relative;
            transition: background-color 0.2s ease;
        }
        
        .square.light {
            background-color: #f0d9b5;
        }
        
        .square.dark {
            background-color: #b58863;
        }
        
        .square.selected {
            background-color: #f7f769 !important;
            box-shadow: inset 0 0 10px rgba(0,0,0,0.3);
        }
        
        .square.drag-over {
            background-color: #aaf0aa !important;
        }
        
        .square.correct {
            animation: correctPulse 1s ease-out forwards;
        }
        
        .square.wrong {
            animation: wrongShake 0.4s ease-out;
        }
        
        .square.checkmate {
            background-color: #ff6b6b !important;
            animation: checkmateGlow 1s ease-out infinite alternate;
        }
        
        @keyframes correctPulse {
            0% { background-color: #4caf50; transform: scale(1); }
            50% { background-color: #69f0ae; transform: scale(1.05); }
            100% { background-color: #81c784; transform: scale(1); }
        }
        
        @keyframes wrongShake {
            0%, 100% { transform: translateX(0); background-color: inherit; }
            10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); background-color: #ef5350; }
            20%, 40%, 60%, 80% { transform: translateX(5px); background-color: #ef5350; }
        }
        
        @keyframes checkmateGlow {
            0% { background-color: #ff6b6b; }
            100% { background-color: #ff8a80; }
        }
        
        .piece {
            cursor: grab;
            transition: transform 0.15s ease;
            line-height: 1;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            z-index: 1;
        }
        
        .piece:hover {
            transform: scale(1.1);
        }
        
        .piece.dragging {
            opacity: 0.4;
            cursor: grabbing;
        }
        
        .piece.black {
            cursor: default;
        }
        
        .coordinates {
            position: absolute;
            font-size: 11px;
            font-weight: bold;
            pointer-events: none;
            z-index: 0;
        }
        
        .file-coord {
            bottom: 2px;
            right: 4px;
        }
        
        .rank-coord {
            top: 2px;
            left: 4px;
        }
        
        .light .coordinates { color: #b58863; }
        .dark .coordinates { color: #f0d9b5; }
        
        .controls {
            margin-top: 25px;
        }
        
        .reset-btn {
            padding: 14px 28px;
            font-size: 16px;
            cursor: pointer;
            border: none;
            border-radius: 8px;
            background: linear-gradient(145deg, #e74c3c, #c0392b);
            color: white;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
        
        .reset-btn:hover {
            background: linear-gradient(145deg, #ff6b5b, #e74c3c);
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.4);
        }
        
        .message {
            margin-top: 25px;
            padding: 15px 25px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: 600;
            min-height: 60px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
        }
        
        .message.info {
            background: rgba(52, 152, 219, 0.2);
            color: #5dade2;
            border: 2px solid rgba(52, 152, 219, 0.3);
        }
        
        .message.success {
            background: rgba(46, 204, 113, 0.2);
            color: #58d68d;
            border: 2px solid rgba(46, 204, 113, 0.3);
            animation: successBounce 0.5s ease;
        }
        
        .message.error {
            background: rgba(231, 76, 60, 0.2);
            color: #ec7063;
            border: 2px solid rgba(231, 76, 60, 0.3);
            animation: errorShake 0.4s ease;
        }
        
        @keyframes successBounce {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        
        @keyframes errorShake {
            0%, 100% { transform: translateX(0); }
            20%, 60% { transform: translateX(-8px); }
            40%, 80% { transform: translateX(8px); }
        }
        
        .move-notation {
            margin-top: 15px;
            color: #888;
            font-family: monospace;
            font-size: 14px;
        }
        
        @media (max-width: 550px) {
            .square {
                width: 42px;
                height: 42px;
                font-size: 34px;
            }
            
            .board {
                grid-template-columns: repeat(8, 42px);
            }
            
            h1 { font-size: 1.4rem; }
            
            .scenario-btn {
                padding: 10px 14px;
                font-size: 12px;
            }
            
            .message { font-size: 14px; padding: 12px 15px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>♔ Mate in 1 Practice ♚</h1>
        
        <div class="scenario-selector">
            <button class="scenario-btn" onclick="loadScenario(0)">1: Back Rank Mate</button>
            <button class="scenario-btn" onclick="loadScenario(1)">2: Queen Corridor</button>
            <button class="scenario-btn" onclick="loadScenario(2)">3: King & Queen</button>
        </div>
        
        <p class="description" id="description">Select a scenario to begin practicing checkmates!</p>
        
        <div class="board-container">
            <div class="board" id="board"></div>
        </div>
        
        <div class="controls">
            <button class="reset-btn" onclick="resetPosition()">🔄 Reset Position</button>
        </div>
        
        <div class="message info" id="message">Choose a scenario above to start!</div>
        <div class="move-notation" id="moveNotation"></div>
    </div>

    <script>
        // Chess piece Unicode symbols
        const PIECES = {
            'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
            'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
        };
        
        const FILES = 'abcdefgh';
        
        // Scenario definitions
        // board[row][col]: row 0 = rank 1 (bottom), row 7 = rank 8 (top)
        const scenarios = [
            {
                name: "Back Rank Mate",
                description: "The black king is trapped behind its pawns. Move your rook to the 8th rank to deliver checkmate!",
                board: [
                    ['', '', '', '', 'R', '', 'K', ''],  // Rank 1
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', 'p', 'p', 'p'], // Rank 7
                    ['', '', '', '', '', '', 'k', '']    // Rank 8
                ],
                solution: { from: [0, 4], to: [7, 4] },
                solutionNotation: "Re8#",
                blackKingPos: [7, 6]
            },
            {
                name: "Queen Corridor Mate",
                description: "Your king cuts off the g7 escape square. Find the queen move that traps the black king in the corner!",
                board: [
                    ['Q', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', 'K', '', ''],
                    ['', '', '', '', '', '', '', 'p'],
                    ['', '', '', '', '', '', '', 'k']
                ],
                solution: { from: [0, 0], to: [7, 0] },
                solutionNotation: "Qa8#",
                blackKingPos: [7, 7]
            },
            {
                name: "King & Queen Mate",
                description: "Your king controls b7. Move your queen to deliver the final blow!",
                board: [
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', 'Q', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['', '', 'K', '', '', '', '', ''],
                    ['', '', '', '', '', '', '', ''],
                    ['k', '', '', '', '', '', '', '']
                ],
                solution: { from: [3, 1], to: [7, 1] },
                solutionNotation: "Qb8#",
                blackKingPos: [7, 0]
            }
        ];
        
        // Game state
        let currentScenario = null;
        let board = [];
        let selectedSquare = null;
        let draggedFrom = null;
        let solved = false;
        
        // Initialize the board UI
        function initBoard() {
            const boardEl = document.getElementById('board');
            boardEl.innerHTML = '';
            
            for (let row = 7; row >= 0; row--) {
                for (let col = 0; col < 8; col++) {
                    const square = document.createElement('div');
                    const isLight = (row + col) % 2 === 1;
                    square.className = `square ${isLight ? 'light' : 'dark'}`;
                    square.dataset.row = row;
                    square.dataset.col = col;
                    
                    if (col === 0) {
                        const rankCoord = document.createElement('span');
                        rankCoord.className = 'coordinates rank-coord';
                        rankCoord.textContent = row + 1;
                        square.appendChild(rankCoord);
                    }
                    if (row === 0) {
                        const fileCoord = document.createElement('span');
                        fileCoord.className = 'coordinates file-coord';
                        fileCoord.textContent = FILES[col];
                        square.appendChild(fileCoord);
                    }
                    
                    square.addEventListener('dragover', handleDragOver);
                    square.addEventListener('dragleave', handleDragLeave);
                    square.addEventListener('drop', handleDrop);
                    square.addEventListener('click', handleSquareClick);
                    
                    boardEl.appendChild(square);
                }
            }
        }
        
        // Load a scenario
        function loadScenario(index) {
            currentScenario = index;
            solved = false;
            selectedSquare = null;
            
            board = scenarios[index].board.map(row => [...row]);
            
            document.getElementById('description').textContent = scenarios[index].description;
            document.getElementById('moveNotation').textContent = '';
            updateMessage('info', "⚪ White to play - Find the checkmate in 1!");
            
            document.querySelectorAll('.scenario-btn').forEach((btn, i) => {
                btn.classList.toggle('active', i === index);
            });
            
            renderBoard();
        }
        
        // Render the board
        function renderBoard() {
            const squares = document.querySelectorAll('.square');
            
            squares.forEach(square => {
                const row = parseInt(square.dataset.row);
                const col = parseInt(square.dataset.col);
                
                const existingPiece = square.querySelector('.piece');
                if (existingPiece) existingPiece.remove();
                
                const isLight = (row + col) % 2 === 1;
                square.className = `square ${isLight ? 'light' : 'dark'}`;
                
                const piece = board[row][col];
                if (piece) {
                    const pieceEl = document.createElement('span');
                    pieceEl.className = 'piece';
                    pieceEl.textContent = PIECES[piece];
                    
                    const isWhite = piece === piece.toUpperCase();
                    if (isWhite && !solved) {
                        pieceEl.draggable = true;
                        pieceEl.addEventListener('dragstart', handleDragStart);
                        pieceEl.addEventListener('dragend', handleDragEnd);
                    } else {
                        pieceEl.classList.add('black');
                        pieceEl.draggable = false;
                    }
                    
                    square.appendChild(pieceEl);
                }
                
                if (solved && currentScenario !== null) {
                    const kingPos = scenarios[currentScenario].blackKingPos;
                    if (row === kingPos[0] && col === kingPos[1]) {
                        square.classList.add('checkmate');
                    }
                }
            });
        }
        
        // Drag handlers
        function handleDragStart(e) {
            if (solved || currentScenario === null) return;
            
            const square = e.target.closest('.square');
            draggedFrom = {
                row: parseInt(square.dataset.row),
                col: parseInt(square.dataset.col)
            };
            
            e.target.classList.add('dragging');
            e.dataTransfer.effectAllowed = 'move';
            e.dataTransfer.setData('text/plain', '');
        }
        
        function handleDragEnd(e) {
            e.target.classList.remove('dragging');
            draggedFrom = null;
            
            document.querySelectorAll('.square.drag-over').forEach(sq => {
                sq.classList.remove('drag-over');
            });
        }
        
        function handleDragOver(e) {
            e.preventDefault();
            if (!draggedFrom || solved) return;
            e.dataTransfer.dropEffect = 'move';
            e.currentTarget.classList.add('drag-over');
        }
        
        function handleDragLeave(e) {
            e.currentTarget.classList.remove('drag-over');
        }
        
        function handleDrop(e) {
            e.preventDefault();
            e.currentTarget.classList.remove('drag-over');
            
            if (!draggedFrom || solved) return;
            
            const toRow = parseInt(e.currentTarget.dataset.row);
            const toCol = parseInt(e.currentTarget.dataset.col);
            
            attemptMove(draggedFrom.row, draggedFrom.col, toRow, toCol);
            draggedFrom = null;
        }
        
        // Click-to-move
        function handleSquareClick(e) {
            if (solved || currentScenario === null) return;
            
            const square = e.currentTarget;
            const row = parseInt(square.dataset.row);
            const col = parseInt(square.dataset.col);
            const piece = board[row][col];
            
            if (selectedSquare) {
                if (selectedSquare.row !== row || selectedSquare.col !== col) {
                    attemptMove(selectedSquare.row, selectedSquare.col, row, col);
                }
                clearSelection();
            } else if (piece && piece === piece.toUpperCase()) {
                selectedSquare = { row, col };
                square.classList.add('selected');
            }
        }
        
        function clearSelection() {
            selectedSquare = null;
            document.querySelectorAll('.square.selected').forEach(sq => {
                sq.classList.remove('selected');
            });
        }
        
        // Attempt move
        function attemptMove(fromRow, fromCol, toRow, toCol) {
            if (currentScenario === null) return;
            if (fromRow === toRow && fromCol === toCol) return;
            
            const solution = scenarios[currentScenario].solution;
            const isCorrect = (
                fromRow === solution.from[0] && 
                fromCol === solution.from[1] &&
                toRow === solution.to[0] && 
                toCol === solution.to[1]
            );
            
            if (isCorrect) {
                board[toRow][toCol] = board[fromRow][fromCol];
                board[fromRow][fromCol] = '';
                solved = true;
                
                renderBoard();
                
                const destSquare = getSquare(toRow, toCol);
                destSquare.classList.add('correct');
                
                const notation = scenarios[currentScenario].solutionNotation;
                document.getElementById('moveNotation').textContent = `Move: ${notation}`;
                
                updateMessage('success', "🎉 Checkmate! Excellent work!");
            } else {
                const fromSquare = getSquare(fromRow, fromCol);
                const toSquare = getSquare(toRow, toCol);
                
                fromSquare.classList.add('wrong');
                toSquare.classList.add('wrong');
                
                setTimeout(() => {
                    fromSquare.classList.remove('wrong');
                    toSquare.classList.remove('wrong');
                }, 400);
                
                updateMessage('error', "❌ That's not checkmate. Try again!");
            }
        }
        
        function getSquare(row, col) {
            return document.querySelector(`.square[data-row="${row}"][data-col="${col}"]`);
        }
        
        function updateMessage(type, text) {
            const msgEl = document.getElementById('message');
            msgEl.className = `message ${type}`;
            msgEl.textContent = text;
        }
        
        function resetPosition() {
            if (currentScenario !== null) {
                loadScenario(currentScenario);
            } else {
                updateMessage('info', "Please select a scenario first!");
            }
        }
        
        // Initialize
        initBoard();
    </script>
</body>
</html>
```

## Features

1. **Three Mate-in-1 Scenarios:**
   - **Back Rank Mate:** White rook delivers checkmate on the 8th rank (Re8#)
   - **Queen Corridor Mate:** Queen traps the king in the corner (Qa8#)
   - **King & Queen Mate:** King and queen coordinate to deliver mate (Qb8#)

2. **Interaction Methods:**
   - **Drag and drop:** Grab white pieces and drop them on target squares
   - **Click-to-move:** Click a piece to select it, then click the destination

3. **Visual Feedback:**
   - ✅ Green pulsing animation for correct moves
   - ❌ Red shaking animation for wrong moves
   - 🔴 Highlighted king square showing checkmate
   - Success/error messages below the board

4. **Controls:**
   - Scenario selection buttons (highlighted when active)
   - Reset button to restart the current position
   - Move notation displayed after successful checkmate

5. **Board Features:**
   - Coordinate labels (files a-h, ranks 1-8)
   - Proper piece symbols using Unicode chess characters
   - Responsive design for mobile devices