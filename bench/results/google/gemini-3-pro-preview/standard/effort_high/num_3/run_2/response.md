Here is a complete, single-file solution.

To keep the code clean and functional without requiring you to install complex build tools, I have utilized two standard libraries via CDN (Content Delivery Network):
1.  **Chess.js**: Handles the game logic (valid moves, checkmate detection).
2.  **Chessboard.js**: Handles the graphical board and drag-and-drop interactions.

### How to use this:
1.  Create a file on your computer named `index.html`.
2.  Paste the code below into it.
3.  Open that file in any web browser.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Mate in 1 - Practice App</title>
    <!-- CSS for Chessboard.js -->
    <link rel="stylesheet"
      href="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css"
      integrity="sha384-q94+BZtLrkL1/ohfjR8c6L+A6qzNH9R2hBLwyoAfu3i/WCvQjzL2RQJ3uNHDISdU"
      crossorigin="anonymous">

    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #2c3e50;
            color: white;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
        }

        .container {
            width: 400px; /* Board width */
            text-align: center;
        }

        h1 { margin-bottom: 20px; }

        .controls {
            margin: 20px 0;
            background: #34495e;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        select, button {
            padding: 8px 12px;
            margin: 5px;
            border-radius: 4px;
            border: none;
            font-size: 14px;
            cursor: pointer;
        }

        button {
            background-color: #e67e22;
            color: white;
            font-weight: bold;
        }

        button:hover { background-color: #d35400; }

        #status {
            margin-top: 15px;
            font-size: 1.2em;
            font-weight: bold;
            min-height: 1.5em;
        }

        .success { color: #2ecc71; }
        .error { color: #e74c3c; }

        /* Board Container */
        #myBoard {
            width: 100%;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Mate in 1 Practice</h1>
        
        <div id="myBoard"></div>

        <div class="controls">
            <label for="scenarioSelect">Choose Scenario:</label>
            <select id="scenarioSelect">
                <option value="0">Scenario 1: Back Rank</option>
                <option value="1">Scenario 2: Scholar's Mate Pattern</option>
                <option value="2">Scenario 3: Queen & King</option>
            </select>
            <br>
            <button id="resetBtn">Reset Position</button>
            <div id="status">White to move</div>
        </div>
    </div>

    <!-- DEPENDENCIES -->
    <!-- jQuery (Required by Chessboard.js) -->
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"
        integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0="
        crossorigin="anonymous"></script>
    <!-- Chess.js (Logic) -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.3/chess.min.js"></script>
    <!-- Chessboard.js (UI) -->
    <script src="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js"
        integrity="sha384-8Vi8VHwn3vjQ9eUHUxex3JSN/NFqUg3QbPyX8kWyb93+8AC/pPWTzj+nHtbC5bxD"
        crossorigin="anonymous"></script>

    <script>
        // --- 1. CONFIGURATION & STATE ---
        
        // Logic engine
        var game = new Chess();
        
        // UI Board
        var board = null;
        
        // 3 "Mate in 1" Scenarios (FEN strings)
        const scenarios = [
            // 1. Back Rank Mate (Rook to a8)
            "6k1/5ppp/8/8/8/8/5PPP/R5K1 w - - 0 1", 
            
            // 2. Scholar's Mate Style (Queen to f7)
            "r1bqkb1r/pppp1ppp/2n2n2/4p2Q/2B1P3/8/PPPP1PPP/RNB1K1NR w KQkq - 0 1",
            
            // 3. Simple Queen Mate (Queen to h7 matches King)
            "6rk/6pp/7P/6Q1/8/8/8/7K w - - 0 1" 
        ];

        var currentScenarioIndex = 0;

        // --- 2. GAME FUNCTIONS ---

        function onDragStart (source, piece, position, orientation) {
            // Do not allow picking up pieces if the game is over
            if (game.game_over()) return false;

            // Only allow White to move (since it's White to move puzzles)
            if (piece.search(/^b/) !== -1) return false;
        }

        function onDrop (source, target) {
            // see if the move is legal
            var move = game.move({
                from: source,
                to: target,
                promotion: 'q' // NOTE: always promote to a queen for simplicity
            });

            // illegal move
            if (move === null) return 'snapback';

            updateStatus();
        }

        // Update the board position after the piece snap
        // for castling, en passant, pawn promotion
        function onSnapEnd () {
            board.position(game.fen());
        }

        function updateStatus () {
            const statusEl = document.getElementById('status');
            
            if (game.in_checkmate()) {
                statusEl.innerText = "Checkmate! You win!";
                statusEl.className = "success";
            } else {
                // If the move was legal but didn't result in mate
                // We undo it to let them try again, or leave it and say incorrect.
                // For a puzzle app, strict feedback is usually better.
                statusEl.innerText = "That move is valid, but not Mate in 1. Try again.";
                statusEl.className = "error";
                
                // Optional: Undo the move automatically after 1 second
                setTimeout(() => {
                    game.undo();
                    board.position(game.fen());
                    statusEl.innerText = "White to move";
                    statusEl.className = "";
                }, 1500);
            }
        }

        function loadScenario(index) {
            currentScenarioIndex = index;
            let fen = scenarios[index];
            
            // Load Logic
            game.load(fen);
            
            // Load UI
            board.position(fen);
            
            // Reset Text
            const statusEl = document.getElementById('status');
            statusEl.innerText = "White to move";
            statusEl.className = "";
        }

        // --- 3. INITIALIZATION ---

        var config = {
            draggable: true,
            position: 'start',
            onDragStart: onDragStart,
            onDrop: onDrop,
            onSnapEnd: onSnapEnd
        }
        
        board = Chessboard('myBoard', config);

        // Load the first scenario by default
        loadScenario(0);

        // --- 4. EVENT LISTENERS ---

        // Dropdown change
        document.getElementById('scenarioSelect').addEventListener('change', function(e) {
            loadScenario(parseInt(e.target.value));
        });

        // Reset Button
        document.getElementById('resetBtn').addEventListener('click', function() {
            loadScenario(currentScenarioIndex);
        });

        // Responsive sizing
        window.addEventListener('resize', board.resize);

    </script>
</body>
</html>
```

### Key Features Explained:

1.  **3 Scenarios**: The `scenarios` array contains 3 distinct FEN strings (standard chess notation for positions).
    1.  **Back Rank**: White moves Rook to the back rank (Ra8#).
    2.  **Scholar's Mate Pattern**: White Queen captures on f7 (Qxf7#).
    3.  **Tactical Queen**: White moves Queen to g7 (Qg7#).
2.  **Visual Feedback**:
    *   Once you drop a piece, the code checks `game.in_checkmate()`.
    *   **If Successful**: The text turns green.
    *   **If Incorrect** (Legal move, but not mate): The text turns red, tells you it's wrong, and the piece automatically snaps back to the start position after 1.5 seconds so you can try again.
3.  **Selectors**:
    *   You can change the scenario using the Dropdown menu.
    *   You can restart the current puzzle using the Reset button.
4.  **Drag and Drop**:
    *   Handled by `Chessboard.js` config.
    *   `onDragStart`: Prevents you from moving Black pieces or moving after the game ends.
    *   `onDrop`: Validates if the move is legal according to chess rules.
    *   `onSnapEnd`: Ensures board graphics sync with internal game state (important for castling or promotions).