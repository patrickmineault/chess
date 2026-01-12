Here’s a self‑contained HTML file that implements what you asked for:

- 3 mate‑in‑1 endgame scenarios for White (selectable via dropdown).
- Drag & drop pieces.
- Checks the move with chess.js and gives visual feedback (success / try again).
- Reset button to restore the current position.

Save this as `mate_in_1.html` and open it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Mate in 1 – Endgame Practice</title>

  <!-- Chessboard.js CSS -->
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.css"
  />

  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
      background: #f5f5f5;
    }

    h1 {
      font-size: 24px;
      margin-bottom: 10px;
    }

    #controls {
      margin-bottom: 10px;
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
    }

    label {
      font-weight: bold;
    }

    select,
    button {
      padding: 4px 8px;
      font-size: 14px;
    }

    #board {
      width: 400px;
      max-width: 90vw;
    }

    #status {
      margin-top: 12px;
      min-height: 24px;
    }

    .status {
      padding: 6px 10px;
      border-radius: 4px;
      display: inline-block;
    }

    .status.info {
      background: #e9f3ff;
      color: #084298;
      border: 1px solid #b6d4fe;
    }

    .status.success {
      background: #d1e7dd;
      color: #0f5132;
      border: 1px solid #badbcc;
    }

    .status.error {
      background: #f8d7da;
      color: #842029;
      border: 1px solid #f5c2c7;
    }
  </style>
</head>
<body>
  <h1>Mate in 1 – Endgame Practice</h1>

  <div id="controls">
    <label for="puzzleSelect">Choose a position:</label>
    <select id="puzzleSelect">
      <option value="0">Puzzle 1 – Queen & bishop vs king & rook</option>
      <option value="1">Puzzle 2 – Queen vs king & pawns</option>
      <option value="2">Puzzle 3 – Queen & bishop vs king & pawns</option>
    </select>

    <button id="resetBtn">Reset position</button>
  </div>

  <div id="board"></div>
  <div id="status"></div>

  <!-- chess.js (move legality & checkmate detection) -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.13.4/chess.min.js"></script>

  <!-- chessboard.js (drag & drop board UI) -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.js"></script>

  <script>
    // 3 Mate-in-1 puzzles for White
    const puzzles = [
      {
        // Solution example: 1.Qxg7#
        fen: "5rk1/6pp/7Q/8/3B4/8/8/6K1 w - - 0 1",
        description: "Puzzle 1 – White to move and mate in 1."
      },
      {
        // Solution example: 1.Qf8#
        fen: "7k/5Qpp/8/8/8/8/8/6K1 w - - 0 1",
        description: "Puzzle 2 – White to move and mate in 1."
      },
      {
        // Solution example: 1.Qh8#
        fen: "Q7/7k/6pp/8/8/2B5/8/6K1 w - - 0 1",
        description: "Puzzle 3 – White to move and mate in 1."
      }
    ];

    let board = null;
    let game = null;
    let currentPuzzleIndex = 0;
    let puzzleSolved = false;

    const statusEl = document.getElementById("status");
    const puzzleSelectEl = document.getElementById("puzzleSelect");
    const resetBtn = document.getElementById("resetBtn");

    function setStatus(message, type) {
      statusEl.className = "";
      statusEl.textContent = "";
      if (!message) return;
      statusEl.classList.add("status");
      if (type) statusEl.classList.add(type);
      statusEl.textContent = message;
    }

    function loadPuzzle(index) {
      currentPuzzleIndex = index;
      const puzzle = puzzles[index];

      game = new Chess();
      game.load(puzzle.fen);

      puzzleSolved = false;
      board.position(puzzle.fen, false);
      setStatus(puzzle.description + " (White to move.)", "info");
    }

    function resetCurrentPuzzle() {
      loadPuzzle(currentPuzzleIndex);
    }

    function onDragStart(source, piece, position, orientation) {
      // Prevent moving after success
      if (puzzleSolved) return false;

      // Only allow white pieces to move
      if (piece[0] === "b") return false;

      // Only White's turn
      if (game.turn() !== "w") return false;

      // No moves if game somehow over
      if (game.game_over()) return false;
    }

    function onDrop(source, target) {
      // Attempt the move
      const move = game.move({
        from: source,
        to: target,
        promotion: "q" // standard default
      });

      // Illegal move: snap the piece back
      if (move === null) {
        return "snapback";
      }

      // Make sure board syncs to game state
      window.setTimeout(() => {
        board.position(game.fen());
      }, 0);

      // Evaluate result
      window.setTimeout(() => {
        if (game.in_checkmate()) {
          puzzleSolved = true;
          setStatus("Checkmate! Well done.", "success");
        } else {
          setStatus("That's not checkmate. Try again.", "error");
          // Automatically reset after a short delay
          setTimeout(resetCurrentPuzzle, 800);
        }
      }, 10);
    }

    function onSnapEnd() {
      board.position(game.fen());
    }

    document.addEventListener("DOMContentLoaded", function () {
      const config = {
        draggable: true,
        position: puzzles[0].fen,
        pieceTheme:
          "https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/img/chesspieces/wikipedia/{piece}.png",
        onDragStart: onDragStart,
        onDrop: onDrop,
        onSnapEnd: onSnapEnd
      };

      board = Chessboard("board", config);

      // Start with puzzle 1
      loadPuzzle(0);

      // Puzzle selection
      puzzleSelectEl.addEventListener("change", function () {
        const index = parseInt(this.value, 10) || 0;
        loadPuzzle(index);
      });

      // Reset button
      resetBtn.addEventListener("click", function () {
        resetCurrentPuzzle();
      });
    });
  </script>
</body>
</html>
```

You can tweak the FEN strings in the `puzzles` array to add or change positions, and chess.js will keep validating that the user’s chosen move is a genuine checkmate in one.