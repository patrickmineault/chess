Here is a complete, single-file solution. You can save this code as an `.html` file (e.g., `chess-practice.html`) and open it in any web browser.

It uses **Chessboard.js** for the visual interface and drag-and-drop mechanics, and **Chess.js** for the game logic (move validation and checkmate detection).

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chess Endgame Practice: Mate in 1</title>
    
    <!-- CSS for Chessboard.js -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.css">
    
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
        }

        h1 { color: #333; }

        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
        }

        #myBoard {
            width: 400px;
            margin-bottom: 20px;
        }

        .controls {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            justify-content: center;
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
            background-color: #4a4e69;
            color: white;
            transition: background 0.2s;
        }

        button:hover {
            background-color: #22223b;
        }

        button.active {
            background-color: #9a8c98;
            outline: 2px solid #22223b;
        }

        #resetBtn {
            background-color: #c9ada7;
            color: #222;
            font-weight: bold;
        }

        #status {
            font-size: 24px;
            font-weight: bold;
            height: 40px; /* Preserve space */
            margin-top: 10px;
        }

        .success { color: #2a9d8f; }
        .error { color: #e76f51; }
        .neutral { color: #666; }

    </style>
</head>
<body>

    <h1>Mate in 1 Practice</h1>

    <div class="container">
        <!-- Status Message Area -->
        <div id="status" class="neutral">Select a scenario to start</div>

        <!-- The Chess Board -->
        <div id="myBoard"></div>

        <!-- Scenario Selection Buttons -->
        <div class="controls">
            <button onclick="loadScenario(1)" id="btn1" class="scen-btn">Back Rank</button>
            <button onclick="loadScenario(2)" id="btn2" class="scen-btn">Arabian Mate</button>
            <button onclick="loadScenario(3)" id="btn3" class="scen-btn">Scholar's Mate</button>
        </div>

        <!-- Game Control -->
        <div class="controls">
            <button onclick="resetCurrentPosition()" id="resetBtn">Reset Position</button>
        </div>
    </div>

    <!-- External Libraries -->
    <!-- jQuery (Required for Chessboard.js) -->
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <!-- Chessboard.js (UI) -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.js"></script>
    <!-- Chess.js (Logic) -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.3/chess.min.js"></script>

    <script>
        // 1. Define the Scenarios (FEN strings)
        // FEN is a standard notation for describing a board position
        const scenarios = {
            1: {
                name: 'Back Rank Mate',
                fen: '6k1/5ppp/8/8/8/8/5PPP/4R1K1 w - - 0 1' 
                // Solution: Re8#
            },
            2: {
                name: 'Arabian Mate',
                fen: '7k/1R6/5N2/8/8/8/8/7K w - - 0 1'
                // Solution: Rh7#
            },
            3: {
                name: 'Scholar\'s Mate',
                fen: 'r1bqk2r/pppp1ppp/2n2n2/2b1p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 0 1'
                // Solution: Qxf7#
            }
        };

        let board = null;
        let game = new Chess();
        let currentScenarioId = 1;
        let isGameOver = false;

        const statusEl = document.getElementById('status');
        const boardEl = document.getElementById('myBoard');

        // 2. Initialize the board logic
        function onDragStart(source, piece, position, orientation) {
            // Do not allow picking up pieces if the game is over
            if (isGameOver) return false;

            // Only allow user to move White pieces
            if (piece.search(/^b/) !== -1) return false;
        }

        function onDrop(source, target) {
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

        // 3. Logic to check win condition and update UI
        function updateStatus() {
            if (game.in_checkmate()) {
                statusEl.innerText = "Checkmate! Well done!";
                statusEl.className = 'success';
                isGameOver = true;
            } else {
                // If the move was legal but NOT checkmate
                statusEl.innerText = "Legal move, but not Mate in 1. Try again.";
                statusEl.className = 'error';
                
                // Undo the move after a short delay to let them retry
                setTimeout(() => {
                    game.undo();
                    board.position(game.fen());
                    statusEl.innerText = "Find the Mate in 1...";
                    statusEl.className = 'neutral';
                }, 1000);
            }
        }

        // 4. Function to Load specific Scenarios
        function loadScenario(id) {
            currentScenarioId = id;
            const scenario = scenarios[id];
            
            // Highlight active button
            document.querySelectorAll('.scen-btn').forEach(btn => btn.classList.remove('active'));
            document.getElementById(`btn${id}`).classList.add('active');

            // Reset Game Logic
            game.load(scenario.fen);
            isGameOver = false;

            // Update Board UI
            board.position(scenario.fen);
            
            // Update Text
            statusEl.innerText = `${scenario.name}: White to move`;
            statusEl.className = 'neutral';
        }

        function resetCurrentPosition() {
            loadScenario(currentScenarioId);
        }

        // Initialize Board Config
        var config = {
            draggable: true,
            position: 'start',
            onDragStart: onDragStart,
            onDrop: onDrop
        };

        board = Chessboard('myBoard', config);

        // Start with Scenario 1
        loadScenario(1);

        // Make board responsive
        window.addEventListener('resize', board.resize);
    </script>
</body>
</html>
```

### How to use this:
1.  Copy the code block above.
2.  Create a new file on your computer named `chess.html`.
3.  Paste the code and save.
4.  Double-click `chess.html` to open it in your browser.

### Features included:
1.  **3 Scenarios:**
    *   **Back Rank Mate:** A classic rook checkmate.
    *   **Arabian Mate:** Uses a Knight and Rook combination.
    *   **Scholar's Mate:** A common opening trap using the Queen.
2.  **Drag and Drop:** You can drag white pieces to move them.
3.  **Strict Validation:**
    *   Illegal moves snap back.
    *   Legal moves that **don't** result in checkmate will show an error message and reset the piece automatically after 1 second (so you can try again).
    *   Checkmate moves lock the board and show a green success message.
4.  **Reset:** A dedicated button to reset the current puzzle.