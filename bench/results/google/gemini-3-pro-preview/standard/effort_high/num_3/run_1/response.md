Here is a complete, single-file solution. I have used two standard, open-source libraries to handle the heavy lifting: **Chess.js** (for game logic/rules) and **Chessboard.js** (for the UI and drag-and-drop).

You can save the code below as an `.html` file (e.g., `chess-practice.html`) and open it in any web browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mate in 1 Practice</title>
    
    <!-- CSS for Chessboard.js -->
    <link rel="stylesheet" href="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css">
    
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }

        .container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
            width: 400px;
        }

        h2 { margin-top: 0; color: #333; }

        #board {
            width: 100%;
            margin: 20px 0;
        }

        .controls {
            display: flex;
            gap: 10px;
            justify-content: center;
            margin-bottom: 15px;
        }

        select, button {
            padding: 8px 12px;
            border: 1px solid #ccc;
            border-radius: 4px;
            cursor: pointer;
            font-size: 14px;
        }

        button {
            background-color: #007bff;
            color: white;
            border: none;
        }

        button:hover { background-color: #0056b3; }

        #status {
            font-weight: bold;
            font-size: 1.1em;
            min-height: 1.5em;
            margin-top: 10px;
        }

        .success { color: #28a745; }
        .error { color: #dc3545; }
        .neutral { color: #666; }
    </style>
</head>
<body>

<div class="container">
    <h2>Mate in 1 Trainer</h2>

    <div class="controls">
        <select id="scenarioSelect">
            <option value="0">Scenario 1: Back Rank</option>
            <option value="1">Scenario 2: Queen & King</option>
            <option value="2">Scenario 3: Arab Mate</option>
        </select>
        <button id="resetBtn">Reset Board</button>
    </div>

    <div id="board"></div>
    
    <div id="status" class="neutral">White to move. Find the Mate in 1!</div>
</div>

<!-- Dependencies -->
<!-- jQuery (Required for Chessboard.js) -->
<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
<!-- Chess.js (Game Logic) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.3/chess.min.js"></script>
<!-- Chessboard.js (UI) -->
<script src="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js"></script>

<script>
    // 1. Define the Scenarios (FEN strings)
    // FEN is a standard notation for describing a board position.
    const scenarios = [
        {
            name: "Back Rank Mate",
            fen: "6k1/5ppp/8/8/8/8/5PPP/4R1K1 w - - 0 1" 
            // Solution: Re8#
        },
        {
            name: "Queen & King Mate",
            fen: "8/8/8/8/8/5K2/5Q2/7k w - - 0 1"
            // Solution: Qg2#
        },
        {
            name: "Arabian Mate Pattern",
            fen: "7k/4N2p/8/8/8/8/8/1R5K w - - 0 1"
            // Solution: Rb8# or Rh1? No, wait. 
            // In this specific position: Rb8+ lets king move to g7. 
            // Let's create a clearer Arabian mate or Hook mate.
            // Revised FEN below:
        }
    ];

    // Fixing Scenario 3 to be a definitive Mate in 1 (Arabian Mate style)
    scenarios[2].fen = "7k/4N3/8/8/8/8/8/1R5K w - - 0 1"; 
    // Wait, if move Rb8+, K can move. Let's do a pure Rook/Knight corner mate.
    scenarios[2].fen = "r6k/4N2p/8/8/8/8/8/6RK w - - 0 1"; 
    // Solution: Rg8# (Rook takes rook checkmate is NOT mate, rook can take back).
    // Let's go with a simple "Hook Mate" pattern setup.
    scenarios[2].fen = "6rk/5N1p/8/8/8/8/8/7K w - - 0 1"; // Smothered check, but game over? No.
    
    // FINAL DECISION SCENARIO 3: Battery Mate
    scenarios[2].name = "Battery Mate";
    scenarios[2].fen = "k7/1R6/1K6/8/8/8/8/2R5 w - - 0 1";
    // Solution: Rc8# or Rh1# (if no blockage). Here Rc8 is mate.

    let board = null;
    let game = new Chess();
    let currentScenarioIndex = 0;
    const statusEl = document.getElementById('status');

    // 2. Initialize Logic
    function initGame() {
        const config = {
            draggable: true,
            position: 'start',
            onDragStart: onDragStart,
            onDrop: onDrop,
            onSnapEnd: onSnapEnd
        };
        board = Chessboard('board', config);
        loadScenario(0);
    }

    // 3. Load specific scenario
    function loadScenario(index) {
        currentScenarioIndex = index;
        const fen = scenarios[index].fen;
        
        game.load(fen);
        board.position(fen);
        
        updateStatus("neutral", "White to move. Find the Mate in 1!");
    }

    // 4. Drag and Drop Logic
    function onDragStart(source, piece, position, orientation) {
        // Do not pick up pieces if the game is over
        if (game.game_over()) return false;

        // Only allow picking up White pieces
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

        // 5. Check Success/Failure
        if (game.in_checkmate()) {
            updateStatus("success", "Correct! Checkmate.");
            // Lock board? The game.game_over check handles this.
        } else {
            // If it was a legal move but NOT checkmate
            updateStatus("error", "Legal move, but not Mate in 1. Try again!");
            
            // Undo the move immediately so they can try again
            setTimeout(() => {
                game.undo();
                board.position(game.fen());
                updateStatus("neutral", "White to move. Find the Mate in 1!");
            }, 800);
        }
    }

    function onSnapEnd() {
        // Update the board position after the piece snap
        // for castling, en passant, pawn promotion
        board.position(game.fen());
    }

    // 6. UI Helpers
    function updateStatus(type, message) {
        statusEl.textContent = message;
        statusEl.className = type;
    }

    // 7. Event Listeners
    document.getElementById('scenarioSelect').addEventListener('change', (e) => {
        loadScenario(parseInt(e.target.value));
    });

    document.getElementById('resetBtn').addEventListener('click', () => {
        loadScenario(currentScenarioIndex);
    });

    // Start
    initGame();

</script>
</body>
</html>
```

### Features included:

1.  **3 Scenarios**:
    *   **Back Rank Mate**: A classic rook mate punishing a king trapped by their own pawns.
    *   **Queen & King**: A standard pattern closing the net on the enemy King.
    *   **Battery Mate**: Where two rooks (or pieces) work together to cut off escape squares.
2.  **Drag & Drop**: Uses `chessboard.js` for smooth piece movement.
3.  **Visual Feedback**:
    *   **Green**: "Correct! Checkmate."
    *   **Red**: "Legal move, but not Mate in 1. Try again!" (The piece automatically moves back if you fail, allowing you to retry instantly).
    *   Snapback: If you drop a piece on an illegal square, it snaps back.
4.  **Controls**:
    *   A dropdown menu to switch between puzzles immediately.
    *   A reset button to restart the current puzzle.

### How to use:
Simply copy the code into a file named `chess.html` and open it in Chrome, Firefox, or Safari. It pulls the necessary move-logic and image assets from the web (CDN), so you will need a live internet connection for the pieces to appear.