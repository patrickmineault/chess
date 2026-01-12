Here is a complete, single-file solution. To use this, simply save the code below as an `.html` file (e.g., `chess-practice.html`) and open it in any web browser.

It uses two popular open-source libraries via CDN:
1.  **Chessboard.js** (for the UI and drag-and-drop)
2.  **Chess.js** (for move validation and logic)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mate in 1 Practice</title>
    
    <!-- CSS for Chessboard.js -->
    <link rel="stylesheet"
      href="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.css"
      integrity="sha384-q94+BZtLrkL1/ohfjR8c6L+A6qzNH9R2hBLwyoAfu3i/WCvQjzL2RQJ3uNHDISdU"
      crossorigin="anonymous">

    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
        }

        h1 { color: #333; }

        .container {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
        }

        #myBoard {
            width: 400px;
            margin: 0 auto;
        }

        .controls {
            margin-top: 20px;
            display: flex;
            gap: 10px;
            justify-content: center;
        }

        select, button {
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
            cursor: pointer;
        }

        button {
            background-color: #007bff;
            color: white;
            border: none;
        }

        button:hover {
            background-color: #0056b3;
        }

        #status {
            margin-top: 15px;
            font-weight: bold;
            font-size: 18px;
            height: 24px;
        }

        .success { color: #28a745; }
        .error { color: #dc3545; }
        .neutral { color: #666; }

    </style>
</head>
<body>

    <div class="container">
        <h1>Mate in 1 Practice</h1>
        <div id="status" class="neutral">Select a puzzle to start</div>
        <div id="myBoard"></div>
        
        <div class="controls">
            <select id="scenarioSelect">
                <!-- Options populated by JS -->
            </select>
            <button id="resetBtn">Reset Board</button>
        </div>
        <p style="font-size: 0.9em; color: #777;">White to move. Drag pieces to play.</p>
    </div>

    <!-- jQuery (Required for Chessboard.js) -->
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"
        integrity="sha384-ZvpUoO/+PpLXR1lu4jmpXWu80pZlYUAfxl5NsBMWOEPSjUn/6Z/hRTt8+pR6L4N2"
        crossorigin="anonymous"></script>

    <!-- Chessboard.js -->
    <script src="https://unpkg.com/@chrisoakman/chessboardjs@1.0.0/dist/chessboard-1.0.0.min.js"
        integrity="sha384-8Vi8VHwn3vjQ9eUHUxex3JSN/NFqUg3QbPyX8kWyb93+8AC/pPWTzj+nHtbC5bxD"
        crossorigin="anonymous"></script>

    <!-- Chess.js (Logic) -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.3/chess.min.js"
        integrity="sha512-xRllwz3ikUEKSvzeGIujYyHJQv9Csxm43ccJe+4Kp36nOHhD+nYrx9eJrTcvATpD0h60qMHCPelPt6Ips3fLUQ=="
        crossorigin="anonymous" referrerpolicy="no-referrer"></script>

    <script>
        // --- 1. Puzzle Definitions ---
        const puzzles = [
            {
                name: "1. The Back Rank",
                // White Rook on e1, Black King on g8 trapped by pawns
                fen: "6k1/5ppp/8/8/8/8/8/4R1K1 w - - 0 1", 
                description: "Find the back-rank mate."
            },
            {
                name: "2. The Scholar's Mate Finish",
                // Classic setup aiming for f7
                fen: "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 0 1",
                description: "Typical early game checkmate."
            },
            {
                name: "3. Queen Kiss of Death",
                // King on g6, Queen on f7, Black king on g8
                fen: "6k1/5Q2/6K1/8/8/8/8/8 w - - 0 1",
                description: "Close the net with the Queen."
            }
        ];

        // --- 2. Application Logic ---
        let board = null;
        let game = new Chess();
        let currentPuzzleIndex = 0;
        const $status = $('#status');
        const $select = $('#scenarioSelect');

        // Initialize Option Dropdown
        puzzles.forEach((puzzle, index) => {
            $select.append(`<option value="${index}">${puzzle.name}</option>`);
        });

        // Drag Start Condition
        function onDragStart (source, piece, position, orientation) {
            // Do not pick up pieces if the game is over
            if (game.game_over()) return false;

            // Only allow dragging White pieces (we are playing White)
            if (piece.search(/^b/) !== -1) return false;
        }

        // Drop Handle
        function onDrop (source, target) {
            // see if the move is legal
            const move = game.move({
                from: source,
                to: target,
                promotion: 'q' // NOTE: always promote to a queen for simplicity
            });

            // illegal move
            if (move === null) return 'snapback';

            updateStatus();
        }

        // Snap End (updates board for castling, en passant, promotion)
        function onSnapEnd () {
            board.position(game.fen());
        }

        // Check Logic / Give Feedback
        function updateStatus () {
            if (game.in_checkmate()) {
                $status.text("SUCCESS! CHECKMATE!").removeClass('error neutral').addClass('success');
                // Lock board by doing nothing
            } else {
                // If it was a valid move but NOT checkmate
                $status.text("That is not mate. Try again!").removeClass('success neutral').addClass('error');
                
                // UX: Undo the move after a short delay so they can try again
                setTimeout(() => {
                    game.undo();
                    board.position(game.fen());
                    $status.text("Try again...").removeClass('error').addClass('neutral');
                }, 800);
            }
        }

        function loadPuzzle(index) {
            currentPuzzleIndex = index;
            const puzzle = puzzles[index];
            
            // Load FEN into logic engine
            game.load(puzzle.fen);
            
            // Set Board Position
            board.position(puzzle.fen);
            
            // Reset message
            $status.text(puzzle.description).removeClass('success error').addClass('neutral');
        }

        // --- 3. Events & Initialization ---
        
        // Config for the board
        const config = {
            draggable: true,
            position: 'start',
            onDragStart: onDragStart,
            onDrop: onDrop,
            onSnapEnd: onSnapEnd
        };
        
        board = Chessboard('myBoard', config);

        // Load first puzzle on start
        loadPuzzle(0);

        // Scenario Selector Listener
        $select.change(function() {
            loadPuzzle($(this).val());
        });

        // Reset Button Listener
        $('#resetBtn').on('click', function() {
            loadPuzzle(currentPuzzleIndex);
        });

        // Responsive resize
        $(window).resize(board.resize);

    </script>
</body>
</html>
```

### Features of this App:
1.  **3 Scenarios**:
    *   **Back Rank Mate**: A rook slide to the back rank.
    *   **Scholar's Mate**: Queen takes `f7`.
    *   **Kiss of Death**: Queen moves right next to the King (protected by the White King).
2.  **Logic**: It uses `Chess.js` to ensure moves are legal.
3.  **Correction System**: If you make a valid chess move but it isn't Checkmate, the board turns red, tells you "That is not mate," and automatically resets the piece so you can try again immediately.
4.  **Victory**: If you hit the checkmate, the text turns green.
5.  **Simplicity**: Requires zero installation. Just opens in the browser.