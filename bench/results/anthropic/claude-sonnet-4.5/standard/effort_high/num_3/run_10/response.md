# Chess Endgame Practice App

Here's a complete chess endgame practice app with drag-and-drop functionality and 3 mate-in-1 scenarios:

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
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            max-width: 600px;
        }

        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 20px;
            font-size: 28px;
        }

        .controls {
            margin-bottom: 20px;
            text-align: center;
        }

        .scenario-btn {
            margin: 5px;
            padding: 10px 20px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s;
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
            margin: 10px 5px 5px 5px;
            padding: 10px 20px;
            background: #f39c12;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 14px;
            transition: all 0.3s;
        }

        .reset-btn:hover {
            background: #e67e22;
            transform: translateY(-2px);
        }

        .board-container {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }

        .chessboard {
            display: grid;
            grid-template-columns: repeat(8, 60px);
            grid-template-rows: repeat(8, 60px);
            border: 3px solid #333;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }

        .square {
            width: 60px;
            height: 60px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 40px;
            position: relative;
            transition: all 0.2s;
        }

        .square.light {
            background-color: #f0d9b5;
        }

        .square.dark {
            background-color: #b58863;
        }

        .square.highlight {
            background-color: #baca44 !important;
            animation: pulse 0.6s ease-in-out;
        }

        .square.drop-target {
            background-color: rgba(127, 201, 127, 0.6);
            box-shadow: inset 0 0 0 3px #4a9b4a;
        }

        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }

        .piece {
            cursor: grab;
            user-select: none;
            font-size: 45px;
            position: relative;
            z-index: 10;
            transition: transform 0.1s;
        }

        .piece:hover {
            transform: scale(1.1);
        }

        .piece.dragging {
            opacity: 0.5;
            cursor: grabbing;
        }

        .piece.not-draggable {
            cursor: default;
        }

        .piece.not-draggable:hover {
            transform: none;
        }

        .feedback {
            margin-top: 20px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            min-height: 30px;
            padding: 10px;
            border-radius: 5px;
            transition: all 0.3s;
        }

        .feedback.success {
            color: #27ae60;
            background: rgba(39, 174, 96, 0.1);
            animation: successPop 0.5s ease-out;
        }

        .feedback.error {
            color: #e74c3c;
            background: rgba(231, 76, 60, 0.1);
            animation: shake 0.5s ease-out;
        }

        @keyframes successPop {
            0% { transform: scale(0.8); opacity: 0; }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); opacity: 1; }
        }

        @keyframes shake {
            0%, 100% { transform: translateX(0); }
            25% { transform: translateX(-10px); }
            75% { transform: translateX(10px); }
        }

        .info {
            text-align: center;
            margin-top: 15px;
            color: #666;
            font-size: 16px;
            font-weight: 500;
        }

        .scenario-name {
            text-align: center;
            color: #764ba2;
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>♔ Chess Endgame Practice ♔</h1>
        <div class="controls">
            <button class="scenario-btn active" data-scenario="0">Scenario 1: Back Rank Mate</button>
            <button class="scenario-btn" data-scenario="1">Scenario 2: Queen Mate</button>
            <button class="scenario-btn" data-scenario="2">Scenario 3: Knight Mate</button>
            <br>
            <button class="reset-btn">🔄 Reset Position</button>
        </div>
        <div class="scenario-name" id="scenarioName"></div>
        <div class="board-container">
            <div class="chessboard" id="chessboard"></div>
        </div>
        <div class="feedback" id="feedback"></div>
        <div class="info">⚔️ White to move and checkmate in 1! ⚔️</div>
    </div>

    <script>
        // Chess piece Unicode characters
        const pieces = {
            'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
            'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
        };

        // Mate in 1 scenarios
        // Board is represented as 8x8 array [row][col] where row 0 = rank 8, col 0 = file a
        const scenarios = [
            {
                name: "Back Rank Mate",
                description: "Classic back rank checkmate with the rook",
                board: [
                    ['', '', '', '', 'k', '', '', ''],     // rank 8
                    ['', '', '', '', 'p', 'p', 'p', ''],   // rank 7
                    ['', '', '', 'K', '', '', '', ''],     // rank 6
                    ['', '', '', '', '', '', '', ''],      // rank 5
                    ['', '', '', '', '', '', '', ''],      // rank 4
                    ['', '', '', '', '', '', '', ''],      // rank 3
                    ['', '', '', '', '', '', '', ''],      // rank 2
                    ['', '', '', '', 'R', '', '', ''],     // rank 1
                ],
                solution: { from: [7, 4], to: [0, 4] } // Re1-e8#
            },
            {
                name: "Queen Mate",
                description: "Deliver mate with the powerful queen",
                board: [
                    ['', '', '', '', '', 'k', '', ''],     // rank 8
                    ['', '', '', '', 'p', 'p', 'p', ''],   // rank 7
                    ['', '', '', '', '', 'K', '', ''],     // rank 6
                    ['', '', '', '', '', '', '', ''],      // rank 5
                    ['', '', '', '', '', '', '', ''],      // rank 4
                    ['', '', '', '', '', '', '', ''],      // rank 3
                    ['', '', 'Q', '', '', '', '', ''],     // rank 2
                    ['', '', '', '', '', '', '', ''],      // rank 1
                ],
                solution: { from: [6, 2], to: [0, 2] } // Qc2-c8#
            },
            {
                name: "Knight Mate",
                description: "The knight delivers checkmate",
                board: [
                    ['', '', '', '', '', '', 'k', ''],     // rank 8
                    ['', '', '', '', '', '', 'p', 'p'],    // rank 7
                    ['', '', '', '', '', 'K', '', 'R'],    // rank 6
                    ['', '', '', '', '', 'N', '', ''],     // rank 5
                    ['', '', '', '', '', '', '', ''],      // rank 4
                    ['', '', '', '', '', '', '', ''],      // rank 3
                    ['', '', '', '', '', '', '', ''],      // rank 2
                    ['', '', '', '', '', '', '', ''],      // rank 1
                ],
                solution: { from: [3, 5], to: [1, 4] } // Nf5-e7#
            }
        ];

        let currentScenario = 0;
        let board = [];
        let draggedPiece = null;
        let draggedFrom = null;
        let isSolved = false;

        // Initialize
        function init() {
            loadScenario(currentScenario);
            setupEventListeners();
        }

        function loadScenario(index) {
            currentScenario = index;
            board = scenarios[index].board.map(row => [...row]);
            isSolved = false;
            renderBoard();
            clearFeedback();
            updateScenarioName();
            
            // Update active button
            document.querySelectorAll('.scenario-btn').forEach((btn, i) => {
                btn.classList.toggle('active', i === index);
            });
        }

        function updateScenarioName() {
            const nameEl = document.getElementById('scenarioName');
            nameEl.textContent = scenarios[currentScenario].description;
        }

        function renderBoard() {
            const chessboard = document.getElementById('chessboard');
            chessboard.innerHTML = '';

            for (let row = 0; row < 8; row++) {
                for (let col = 0; col < 8; col++) {
                    const square = document.createElement('div');
                    square.className = 'square';
                    square.className += (row + col) % 2 === 0 ? ' light' : ' dark';
                    square.dataset.row = row;
                    square.dataset.col = col;

                    const piece = board[row][col];
                    if (piece) {
                        const pieceEl = document.createElement('div');
                        pieceEl.className = 'piece';
                        pieceEl.textContent = pieces[piece];
                        pieceEl.dataset.piece = piece;
                        pieceEl.dataset.row = row;
                        pieceEl.dataset.col = col;
                        
                        // Only white pieces should be draggable (uppercase letters)
                        if (piece === piece.toUpperCase() && !isSolved) {
                            pieceEl.draggable = true;
                            pieceEl.addEventListener('dragstart', handleDragStart);
                            pieceEl.addEventListener('dragend', handleDragEnd);
                        } else {
                            pieceEl.draggable = false;
                            pieceEl.classList.add('not-draggable');
                        }
                        
                        square.appendChild(pieceEl);
                    }

                    square.addEventListener('dragover', handleDragOver);
                    square.addEventListener('drop', handleDrop);
                    square.addEventListener('dragleave', handleDragLeave);

                    chessboard.appendChild(square);
                }
            }
        }

        function handleDragStart(e) {
            if (isSolved) return;
            
            draggedPiece = e.target;
            draggedFrom = {
                row: parseInt(e.target.dataset.row),
                col: parseInt(e.target.dataset.col)
            };
            e.target.classList.add('dragging');
            e.dataTransfer.effectAllowed = 'move';
        }

        function handleDragEnd(e) {
            e.target.classList.remove('dragging');
            document.querySelectorAll('.square').forEach(sq => {
                sq.classList.remove('drop-target');
            });
        }

        function handleDragOver(e) {
            if (isSolved) return;
            e.preventDefault();
            e.dataTransfer.dropEffect = 'move';
            e.currentTarget.classList.add('drop-target');
            return false;
        }

        function handleDragLeave(e) {
            e.currentTarget.classList.remove('drop-target');
        }

        function handleDrop(e) {
            if (isSolved) return;
            
            e.preventDefault();
            e.stopPropagation();

            const square = e.currentTarget;
            const toRow = parseInt(square.dataset.row);
            const toCol = parseInt(square.dataset.col);

            if (draggedPiece && draggedFrom) {
                makeMove(draggedFrom.row, draggedFrom.col, toRow, toCol);
            }

            square.classList.remove('drop-target');
            draggedPiece = null;
            draggedFrom = null;
            return false;
        }

        function makeMove(fromRow, fromCol, toRow, toCol) {
            // Don't allow moving to same square
            if (fromRow === toRow && fromCol === toCol) {
                renderBoard();
                return;
            }

            const piece = board[fromRow][fromCol];
            
            // Make the move
            board[toRow][toCol] = piece;
            board[fromRow][fromCol] = '';
            
            renderBoard();
            
            // Check if this is the correct solution
            setTimeout(() => checkSolution(fromRow, fromCol, toRow, toCol), 100);
        }

        function checkSolution(fromRow, fromCol, toRow, toCol) {
            const solution = scenarios[currentScenario].solution;
            
            if (fromRow === solution.from[0] && 
                fromCol === solution.from[1] && 
                toRow === solution.to[0] && 
                toCol === solution.to[1]) {
                isSolved = true;
                showFeedback('🎉 Checkmate! Well done! 🎉', 'success');
                highlightSquare(toRow, toCol);
            } else {
                showFeedback('❌ Not quite right. Try again!', 'error');
            }
        }

        function highlightSquare(row, col) {
            const squares = document.querySelectorAll('.square');
            const index = row * 8 + col;
            if (squares[index]) {
                squares[index].classList.add('highlight');
            }
        }

        function showFeedback(message, type) {
            const feedback = document.getElementById('feedback');
            feedback.textContent = message;
            feedback.className = 'feedback ' + type;
        }

        function clearFeedback() {
            const feedback = document.getElementById('feedback');
            feedback.textContent = '';
            feedback.className = 'feedback';
        }

        function setupEventListeners() {
            // Scenario buttons
            document.querySelectorAll('.scenario-btn').forEach(btn => {
                btn.addEventListener('click', (e) => {
                    const scenario = parseInt(e.target.dataset.scenario);
                    loadScenario(scenario);
                });
            });

            // Reset button
            document.querySelector('.reset-btn').addEventListener('click', () => {
                loadScenario(currentScenario);
            });
        }

        // Start the app
        init();
    </script>
</body>
</html>
```

## Features:

1. **3 Mate-in-1 Scenarios:**
   - **Back Rank Mate**: Rook delivers checkmate on the back rank
   - **Queen Mate**: Queen delivers checkmate from the side
   - **Knight Mate**: Knight delivers a checkmate assisted by king and rook

2. **Drag and Drop**: All white pieces can be dragged and dropped to any square

3. **Visual Feedback**: 
   - ✅ Success message with green animation when correct
   - ❌ Error message with red shake animation when incorrect
   - Highlighting of the winning square

4. **Scenario Selection**: Click buttons to switch between scenarios

5. **Reset Position**: Reset button restores the current scenario

6. **Polish**:
   - Beautiful gradient background
   - Smooth animations and transitions
   - Hover effects on pieces and buttons
   - Drop target highlighting
   - Pieces lock after solving

Simply save this as an `.html` file and open it in any modern web browser to play!