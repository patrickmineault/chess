To create a fully functional, drag-and-drop chess app, the best approach is to use two standard open-source libraries:
1.  **Chessboard.js**: Handles the visual board, pieces, and drag-and-drop interactions.
2.  **Chess.js**: Handles the game logic (move validation, checkmate detection, FEN parsing).

Here is a complete, single-file solution. You can save this code as an `.html` file (e.g., `chess-practice.html`) and open it in your browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mate in 1 Practice App</title>
    
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
            background-color: #34495e;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            text-align: center;
        }

        h1 { margin-top: 0; }

        #board {
            width: 400px;
            margin: 20px auto;
        }

        .controls {
            margin-top: 15px;
            display: flex;
            gap: 10px;
            justify-content: center;
        }

        select, button {
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }

        select { background-color: #ecf0f1; color: #2c3e50; }
        
        button {
            background-color: #e67e22;
            color: white;
            font-weight: bold;
            transition: background 0.2s;
        }

        button:hover { background-color: #d35400; }

        #status {
            margin-top: 15px;
            font-size: 1.2rem;
            font-weight: bold;
            height: 30px; /* Prevent jumpiness */
        }

        .success { color: #2ecc71; }
        .error { color: #e74c3c; }
    </style>
</head>
<body>

<div class="container">
    <h1>Mate in 1 Practice</h1>
    
    <div class="controls">
        <select id="scenarioSelect">
            <option value="0">Scenario 1: Back Rank</option>
            <option value="1">Scenario 2: The Battery</option>
            <option value="2">Scenario 3: Arabian Mate</option>
        </select>
    </div>

    <div id="board"></div>

    <div id="status">White to move. Find Mate in 1!</div>

    <div class="controls">
        <button id="resetBtn">Reset Position</button>
    </div>
</div>

<!-- Scripts Dependencies -->
<!-- jQuery (Required for Chessboard.js) -->
<script src="https://code.jquery.com/jquery-3.5.1.min.js"
        integrity="sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/6Z/hRTt8+pR6L4N2"
        crossorigin="anonymous"></script>

<!-- Chessboard.js (UI) -->
<script src="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js"
        integrity="sha384-8Vi8VHwn3vjQ9eUHUxex3JSN/NFqUg3QbPyX8kWyb93+8AC/pPWTzj+nHtbC5bxD"
        crossorigin="anonymous"></script>

<!-- Chess.js (Logic) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.3/chess.min.js" integrity="sha512-xRllwz3FhULJyBoMCvP1wPSZ8Sp038720yAV97mdcK1T/y7yT4I06I7UwmGwxB5yJ7+QJ4fO33l5oE66bA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

<script>
    // --- Configuration and Data ---

    // FEN strings representing the board state (Standard chess notation for positions)
    const scenarios = [
        {
            name: "Back Rank Mate",
            fen: "6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1" 
            // Solution: Re8#
        },
        {
            name: "Queen Bishop Battery",
            fen: "7k/6pp/8/8/8/3Q4/2B5/6K1 w - - 0 1" 
            // Solution: Qh7#
        },
        {
            name: "Arabian Mate",
            fen: "7k/2R4p/5N2/8/8/8/8/7K w - - 0 1" 
            // Solution: Rh7#
        }
    ];

    let board = null;
    let game = new Chess();
    let currentScenarioIndex = 0;
    const statusEl = document.getElementById('status');
    const scenarioSelect = document.getElementById('scenarioSelect');

    // --- Core Logic ---

    function onDragStart(source, piece, position, orientation) {
        // Do not pick up pieces if the game is over
        if (game.game_over()) return false;

        // Only pick up pieces for White (since it's White to move)
        if (piece.search(/^b/) !== -1) return false;
    }

    function onDrop(source, target) {
        // see if the move is legal
        let move = game.move({
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
    function onSnapEnd() {
        board.position(game.fen());
    }

    function updateStatus() {
        let statusText = '';
        let statusClass = '';

        if (game.in_checkmate()) {
            statusText = 'SUCCESS: Checkmate!';
            statusClass = 'success';
        } else if (game.in_draw()) {
            statusText = 'Draw! Reset to try again.';
            statusClass = 'error';
        } else {
            // Game is still going, but the user didn't find mate in 1
            // In a puzzle context, this is a failure.
            statusText = 'Incorrect. That is not checkmate.';
            statusClass = 'error';
            
            // Optional: You could undo the move here if you want strict enforcement
            // game.undo(); 
            // board.position(game.fen());
        }

        statusEl.innerText = statusText;
        statusEl.className = statusClass;
    }

    // --- App Management ---

    function loadScenario(index) {
        currentScenarioIndex = index;
        const fen = scenarios[index].fen;
        
        // Reset logic
        game.load(fen);
        
        // Reset Board UI
        board.position(fen);
        
        // Reset Text
        statusEl.innerText = "White to move. Find Mate in 1!";
        statusEl.className = "";
    }

    // --- Initialization ---

    const config = {
        draggable: true,
        position: 'start',
        onDragStart: onDragStart,
        onDrop: onDrop,
        onSnapEnd: onSnapEnd
    };

    board = Chessboard('board', config);

    // Event Listeners
    scenarioSelect.addEventListener('change', (e) => {
        loadScenario(parseInt(e.target.value));
    });

    document.getElementById('resetBtn').addEventListener('click', () => {
        loadScenario(currentScenarioIndex);
    });

    // Load first scenario on startup
    loadScenario(0);

    // Responsive fix for window resizing
    window.addEventListener('resize', board.resize);

</script>

</body>
</html>
```

### How to use this:
1.  Copy the code block above.
2.  Create a new file on your computer named `chess.html`.
3.  Paste the code into that file and save it.
4.  Double-click `chess.html` to open it in your web browser.

### Features included:
1.  **3 Scenarios**: A Back Rank mate, a Queen/Bishop battery mate, and an Arabian mate (Rook + Knight).
2.  **Logic**: It uses `chess.js` to validate that moves are legal chess moves.
3.  **Feedback**:
    *   If you deliver Checkmate, the text turns **Green** and says "SUCCESS".
    *   If you make a move that doesn't end the game (or causes a stalemate), the text turns **Red** indicating it wasn't the correct solution.
4.  **Drag and Drop**: You can drag pieces to squares. If the move is illegal (e.g., knight moving like a rook), the piece snaps back.
5.  **Reset**: A button to reset the current board to the start of the puzzle.