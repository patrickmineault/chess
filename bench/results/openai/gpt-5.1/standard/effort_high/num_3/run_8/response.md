Here’s a complete, self‑contained HTML file for a small “mate in 1” endgame trainer with 3 selectable scenarios, drag‑and‑drop pieces, reset button, and visual feedback.

Save as `endgame_trainer.html` and open in a browser (requires internet access for the JS/CSS CDNs):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Chess Endgame – Mate in 1 Practice</title>

  <!-- Chessboard.js CSS -->
  <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.css" />

  <style>
    body {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #f5f5f5;
      margin: 0;
      padding: 20px;
    }

    .app {
      max-width: 600px;
      margin: 0 auto;
      background: #fff;
      padding: 20px 20px 30px;
      border-radius: 10px;
      box-shadow: 0 3px 12px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
      margin-top: 0;
      font-size: 1.6rem;
    }

    .controls {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
      justify-content: center;
      margin-bottom: 15px;
    }

    .controls label {
      font-weight: 600;
    }

    select, button {
      padding: 4px 8px;
      font-size: 0.9rem;
    }

    #boardWrapper {
      width: 400px;
      max-width: 100%;
      margin: 0 auto;
      padding: 10px;
      border-radius: 8px;
      border: 2px solid #ccc;
      box-sizing: border-box;
      transition: box-shadow 0.3s ease, border-color 0.3s ease;
      background: #fafafa;
    }

    #boardWrapper.success {
      border-color: #2e7d32;
      box-shadow: 0 0 15px rgba(46, 125, 50, 0.6);
    }

    #boardWrapper.error {
      border-color: #c62828;
      box-shadow: 0 0 15px rgba(198, 40, 40, 0.6);
    }

    #board {
      width: 100%;
    }

    #description {
      text-align: center;
      margin-top: 10px;
      font-size: 0.9rem;
      color: #555;
      min-height: 1.2em;
    }

    .message {
      text-align: center;
      margin-top: 10px;
      font-weight: 600;
      font-size: 0.95rem;
    }
    .message.neutral { color: #333; }
    .message.success { color: #2e7d32; }
    .message.error   { color: #c62828; }
  </style>
</head>
<body>
<div class="app">
  <h1>Chess Endgame – Mate in 1 Trainer</h1>

  <div class="controls">
    <label for="puzzleSelect">Choose position:</label>
    <select id="puzzleSelect">
      <option value="1">Puzzle 1 – Corner mate with queen</option>
      <option value="2">Puzzle 2 – Edge mate with queen</option>
      <option value="3">Puzzle 3 – Mirrored corner mate</option>
    </select>
    <button id="resetBtn">Reset position</button>
  </div>

  <div id="boardWrapper">
    <div id="board"></div>
  </div>

  <div id="description"></div>
  <div id="status" class="message neutral"></div>
</div>

<!-- Chess.js (rules/engine) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.10.2/chess.min.js"></script>
<!-- Chessboard.js (UI with drag & drop) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.js"></script>

<script>
  // Three "mate in 1" puzzles for White
  // FENs are legal positions with White to move.
  var puzzles = {
    '1': {
      name: 'Puzzle 1 – Corner mate with queen',
      fen:  '7k/8/6QK/8/8/8/8/8 w - - 0 1',
      description: 'Use your queen and king to trap the black king in the corner.'
    },
    '2': {
      name: 'Puzzle 2 – Edge mate with queen',
      fen:  'k7/2K5/1Q6/8/8/8/8/8 w - - 0 1',
      description: 'The black king is stuck on the edge. Find a one-move checkmate.'
    },
    '3': {
      name: 'Puzzle 3 – Mirrored corner mate',
      fen:  '8/8/8/8/8/6Q1/5K2/7k w - - 0 1',
      description: 'A mirrored corner pattern. White to move and mate in one.'
    }
  };

  var currentPuzzleKey = '1';
  var game;
  var board;
  var allowMoves = true;

  function setMessage(type, text) {
    var el = document.getElementById('status');
    el.textContent = text;
    el.className = 'message ' + type;
  }

  function highlightBoard(type) {
    var wrapper = document.getElementById('boardWrapper');
    wrapper.classList.remove('success', 'error');
    if (type === 'success') wrapper.classList.add('success');
    if (type === 'error') wrapper.classList.add('error');
  }

  function clearHighlights() {
    var wrapper = document.getElementById('boardWrapper');
    wrapper.classList.remove('success', 'error');
  }

  function initPuzzle(key) {
    currentPuzzleKey = key;
    var puzzle = puzzles[key];

    game = new Chess();
    game.load(puzzle.fen);

    allowMoves = true;
    clearHighlights();
    board.position(puzzle.fen, false);

    document.getElementById('description').textContent = puzzle.description;
    setMessage('neutral', puzzle.name + ' — White to move and mate in 1.');
  }

  function onDragStart(source, piece, position, orientation) {
    // Disable dragging if puzzle is finished or not White to move
    if (!allowMoves) return false;
    if (game.game_over()) return false;
    if (piece[0] === 'b') return false; // don't allow moving black pieces
    if (game.turn() === 'b') return false; // should never happen, but safe
  }

  function evaluatePosition() {
    if (game.in_checkmate()) {
      allowMoves = false;
      setMessage('success', 'Correct! That move is checkmate.');
      highlightBoard('success');
    } else {
      allowMoves = false;
      setMessage('error', 'That move is not mate in 1. Resetting the position...');
      highlightBoard('error');
      setTimeout(function () {
        initPuzzle(currentPuzzleKey);
      }, 1200);
    }
  }

  function onDrop(source, target) {
    if (!allowMoves) {
      return 'snapback';
    }

    var move = game.move({
      from: source,
      to: target,
      promotion: 'q' // just in case (not needed in these puzzles)
    });

    // Illegal move => snap piece back
    if (move === null) {
      return 'snapback';
    }

    // Update board to actual game position (in case of any corrections)
    board.position(game.fen(), true);

    // After the move is complete, evaluate result
    window.setTimeout(evaluatePosition, 100);
  }

  document.addEventListener('DOMContentLoaded', function () {
    // Initialize board
    var config = {
      draggable: true,
      position: puzzles[currentPuzzleKey].fen,
      orientation: 'white',
      onDragStart: onDragStart,
      onDrop: onDrop,
      pieceTheme:
        'https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/img/chesspieces/wikipedia/{piece}.png'
    };
    board = Chessboard('board', config);

    // Load first puzzle
    initPuzzle(currentPuzzleKey);

    // Hook up controls
    var select = document.getElementById('puzzleSelect');
    select.value = currentPuzzleKey;
    select.addEventListener('change', function (e) {
      initPuzzle(e.target.value);
    });

    var resetBtn = document.getElementById('resetBtn');
    resetBtn.addEventListener('click', function () {
      initPuzzle(currentPuzzleKey);
    });
  });
</script>
</body>
</html>
```

This gives you:

- 3 selectable mate-in-1 scenarios for White (dropdown).
- Drag-and-drop pieces (via chessboard.js).
- Legal-move checking and checkmate detection (via chess.js).
- Visual feedback (colored text and board glow) for success/failure.
- Reset button to restore the current position.