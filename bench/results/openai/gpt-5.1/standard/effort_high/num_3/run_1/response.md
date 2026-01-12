Here’s a complete minimal app (single HTML file) that does what you asked:

- 3 mate-in-1 scenarios, selectable
- Drag-and-drop pieces
- White only moves
- Visual feedback after the move
- Reset to start position for the current scenario

It uses `chess.js` for rules and `chessboard.js` for the board and drag & drop.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Chess Endgame Mate in 1 Practice</title>

  <!-- Chessboard.js CSS -->
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/chessboard.js/1.0.0/chessboard-1.0.0.min.css"
  />

  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
      text-align: center;
    }

    #board {
      width: 400px;
      margin: 20px auto;
    }

    #controls {
      margin-bottom: 10px;
    }

    #status {
      margin-top: 10px;
      font-weight: bold;
      min-height: 1.5em;
    }

    #status.success {
      color: green;
    }

    #status.error {
      color: red;
    }

    #status.info {
      color: #555;
    }

    select,
    button {
      margin: 0 5px;
      padding: 4px 8px;
      font-size: 14px;
    }
  </style>
</head>
<body>
  <h2>Mate in 1 – Endgame Practice (White to move)</h2>

  <div id="controls">
    <label for="scenarioSelect">Scenario:</label>
    <select id="scenarioSelect">
      <option value="1">
        1) King + Queen vs King (black king a8)
      </option>
      <option value="2">
        2) King + Queen vs King (black king h8)
      </option>
      <option value="3">
        3) King + Rook vs King (black king h8)
      </option>
    </select>

    <button id="resetBtn">Reset position</button>
  </div>

  <div id="board"></div>
  <div id="status"></div>

  <!-- Chess.js (rules) -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.3/chess.min.js"></script>

  <!-- Chessboard.js (board + drag-and-drop) -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/chessboard.js/1.0.0/chessboard-1.0.0.min.js"></script>

  <script>
    // ======= Scenarios (all are "White to move, mate in 1") =======
    const scenarios = {
      "1": {
        name: "King + Queen vs King (black king on a8)",
        // White: Kc6, Qb6; Black: Ka8
        fen: "k7/8/1QK5/8/8/8/8/8 w - - 0 1"
      },
      "2": {
        name: "King + Queen vs King (black king on h8)",
        // White: K g6, Q g6; Black: K h8
        fen: "7k/8/6QK/8/8/8/8/8 w - - 0 1"
      },
      "3": {
        name: "King + Rook vs King (black king on h8)",
        // White: K g6, R g1; Black: K h8  (Rg7#)
        fen: "7k/8/6K1/8/8/8/8/6R1 w - - 0 1"
      }
    };

    let board = null;
    const game = new Chess();
    let currentScenario = "1";
    let hasMoved = false; // only allow one white move per attempt

    // ======= UI helpers =======
    function setMessage(text, type) {
      const el = document.getElementById("status");
      el.textContent = text;
      el.className = type || "";
    }

    function clearMessage() {
      setMessage("", "");
    }

    // ======= Chessboard.js event handlers =======
    function onDragStart(source, piece, position, orientation) {
      // Disallow dragging if:
      // - puzzle already attempted (one move made)
      // - game over in terms of rules
      // - trying to move black piece
      // - not white's turn (shouldn’t happen in these puzzles)
      if (hasMoved || game.game_over()) return false;
      if (piece[0] === "b") return false;
      if (game.turn() !== "w") return false;
      return true;
    }

    function onDrop(source, target) {
      // Attempt to make the move
      const move = game.move({
        from: source,
        to: target,
        promotion: "q" // irrelevant here, but required by chess.js interface
      });

      // Illegal move -> snap back
      if (move === null) return "snapback";

      hasMoved = true; // only one white move allowed

      // After the move is visually updated, evaluate the result
      window.setTimeout(evaluatePosition, 100);
    }

    function onSnapEnd() {
      board.position(game.fen());
    }

    function evaluatePosition() {
      if (game.in_checkmate()) {
        setMessage("Correct! Checkmate.", "success");
      } else if (game.in_stalemate()) {
        setMessage("Stalemate (not mate). Reset and try again.", "error");
      } else if (game.in_check()) {
        setMessage(
          "That's check but not checkmate. Reset the position and try again.",
          "info"
        );
      } else {
        setMessage(
          "That is not checkmate. Reset the position and try again.",
          "error"
        );
      }
    }

    // ======= Scenario management =======
    function loadScenario(id) {
      currentScenario = id;
      const fen = scenarios[id].fen;
      game.load(fen);
      hasMoved = false;
      board.position(fen);
      setMessage(
        scenarios[id].name + " – White to move and mate in 1.",
        "info"
      );
    }

    function resetPosition() {
      loadScenario(currentScenario);
    }

    // ======= Init =======
    function init() {
      const config = {
        draggable: true,
        position: scenarios[currentScenario].fen,
        orientation: "white",
        pieceTheme:
          "https://cdnjs.cloudflare.com/ajax/libs/chessboard.js/1.0.0/img/chesspieces/wikipedia/{piece}.png",
        onDragStart: onDragStart,
        onDrop: onDrop,
        onSnapEnd: onSnapEnd
      };

      board = Chessboard("board", config);
      game.load(scenarios[currentScenario].fen);

      document
        .getElementById("scenarioSelect")
        .addEventListener("change", function () {
          loadScenario(this.value);
        });

      document
        .getElementById("resetBtn")
        .addEventListener("click", resetPosition);

      loadScenario(currentScenario);
    }

    window.addEventListener("load", init);
  </script>
</body>
</html>
```

You can save this as `index.html` and open it in a browser.  
Each scenario is mate in one for White; drag a white piece to the correct square, then use “Reset position” or switch scenarios as needed.