Below is a self‑contained example using JavaScript plus two small libraries:

- `chess.js` for move legality and checkmate detection  
- `chessboard.js` for the draggable visual board

You can paste this into a single `index.html` file and open it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Mate in 1 – Chess Endgame Practice</title>

  <!-- Chessboard.js CSS -->
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.css"
    integrity="sha512-zra4DTbq3Z+5PfK/HCH3Jf2UZ7690SJykxw9oCLYKPcCxA4uY5SafqEB9OkGytTtq5oxPKRfaF2DfZbxZec/jQ=="
    crossorigin="anonymous"
    referrerpolicy="no-referrer"
  />

  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
      background: #f5f5f5;
    }

    h1 {
      margin-bottom: 10px;
    }

    .app {
      max-width: 520px;
      margin: 0 auto;
      background: #ffffff;
      border-radius: 6px;
      padding: 15px 20px 20px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.15);
    }

    .controls {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
      margin-bottom: 10px;
    }

    label {
      font-weight: bold;
    }

    select, button {
      padding: 4px 8px;
      font-size: 14px;
    }

    #board {
      width: 400px;
      margin: 0 auto;
    }

    .message {
      margin-top: 10px;
      min-height: 1.2em;
      font-weight: bold;
    }

    .message.success {
      color: #1a7f1a;
    }

    .message.error {
      color: #b30000;
    }

    .message.info {
      color: #333;
    }
  </style>
</head>
<body>
<div class="app">
  <h1>Mate in 1 – Practice</h1>

  <div class="controls">
    <label for="scenario-select">Scenario:</label>
    <select id="scenario-select"></select>

    <button id="reset-btn">Reset position</button>
  </div>

  <div id="board"></div>

  <div id="message" class="message info">
    White to move: find mate in one.
  </div>
</div>

<!-- chess.js -->
<script
  src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.13.4/chess.min.js"
  integrity="sha512-xMdyzCF0CgSgFB2V7rqUF+UUMU/6Cjq7kZHigofPO8r/2wZ063VkwrPBUfQxotvLtFGzR0UGfUlfXIqHgp5JXA=="
  crossorigin="anonymous"
  referrerpolicy="no-referrer"
></script>

<!-- chessboard.js -->
<script
  src="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.js"
  integrity="sha512-UtbuuKPQPGNura7wN4XA0phnkfKaI/bpaEmMXtELqhimYXglrujcyB8qPClbKupF7RkiBkF4bTRw02GPO0wF7g=="
  crossorigin="anonymous"
  referrerpolicy="no-referrer"
></script>

<script>
  // --- Scenarios: all "Mate in 1 for White" positions ---
  const scenarios = [
    {
      id: 's1',
      name: 'Scenario 1 – Qxf7#',
      fen: '4rk2/5ppp/8/3Q4/2B5/8/5PPP/4R1K1 w - - 0 1'
      // Solution example: Qxf7#
    },
    {
      id: 's2',
      name: 'Scenario 2 – Rxe8# (back‑rank mate)',
      fen: '4r1k1/6pp/6p1/8/8/8/5PPP/4R1K1 w - - 0 1'
      // Solution example: Rxe8#
    },
    {
      id: 's3',
      name: 'Scenario 3 – K+Q vs K',
      fen: 'k7/2K5/2Q5/8/8/8/8/8 w - - 0 1'
      // Example mates: Qb7#, Qa6#
    }
  ];

  let game;
  let board;
  let currentScenarioIndex = 0;
  let gameOver = false;

  const messageEl = document.getElementById('message');

  function setMessage(text, type) {
    messageEl.textContent = text;
    messageEl.className = 'message ' + (type || 'info');
  }

  function loadScenario(index) {
    currentScenarioIndex = index;
    const fen = scenarios[index].fen;
    game = new Chess(fen);
    gameOver = false;
    board.position(fen);
    setMessage('White to move: find mate in one.', 'info');
  }

  // --- Drag/Drop handlers ---

  function onDragStart(source, piece, position, orientation) {
    // Do not pick up pieces if:
    // - the game is over, or
    // - it's not White to move, or
    // - the piece is Black
    if (gameOver) return false;
    if (game.turn() !== 'w') return false;
    if (piece[0] === 'b') return false;

    return true;
  }

  function onDrop(source, target) {
    if (source === target) return; // ignore trivial drop

    const move = game.move({
      from: source,
      to: target,
      promotion: 'q' // promote to queen if needed
    });

    // Illegal move -> snap the piece back
    if (move === null) {
      return 'snapback';
    }

    // Legal move was made; check puzzle result
    if (game.in_checkmate()) {
      setMessage('Correct! Checkmate.', 'success');
      gameOver = true;
    } else {
      setMessage('That is not checkmate. Try again.', 'error');
      // Undo the move for training (user keeps trying from same position)
      game.undo();
      return 'snapback';
    }
  }

  function onSnapEnd() {
    // Update board after piece snap for visual consistency
    board.position(game.fen());
  }

  // --- Init ---

  document.addEventListener('DOMContentLoaded', function () {
    // Create the board
    const cfg = {
      draggable: true,
      position: scenarios[0].fen,
      orientation: 'white',
      onDragStart: onDragStart,
      onDrop: onDrop,
      onSnapEnd: onSnapEnd
    };
    board = ChessBoard('board', cfg);

    // Create the game
    game = new Chess(scenarios[0].fen);

    // Populate scenario selector
    const select = document.getElementById('scenario-select');
    scenarios.forEach((sc, i) => {
      const opt = document.createElement('option');
      opt.value = i;
      opt.textContent = sc.name;
      select.appendChild(opt);
    });
    select.value = '0';

    select.addEventListener('change', function () {
      const idx = parseInt(this.value, 10);
      loadScenario(idx);
    });

    // Reset button
    document.getElementById('reset-btn').addEventListener('click', function () {
      loadScenario(currentScenarioIndex);
    });

    setMessage('White to move: find mate in one.', 'info');
  });
</script>
</body>
</html>
```

Features:

- 3 selectable “mate in 1” scenarios (via dropdown).
- Drag-and-drop pieces for White only.
- After each attempted move:
  - If it’s checkmate, a green success message appears and the position is left on the board.
  - If it’s not checkmate, a red error message appears and the move is reverted so you can try again.
- “Reset position” button restores the current scenario to its starting FEN.