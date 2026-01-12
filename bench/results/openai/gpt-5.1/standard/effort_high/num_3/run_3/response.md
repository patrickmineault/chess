Below is a complete, self-contained HTML file that implements a simple “mate in 1 for White” endgame practice app with:

- 3 selectable scenarios  
- Drag-and-drop pieces  
- Reset button  
- Visual feedback (text + board border color)  

It uses `chess.js` for rules/checkmate detection and `chessboard.js` for the draggable board.

Save this as `endgame_practice.html` and open it in a browser.

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Chess Endgame Mate-in-1 Practice</title>

  <!-- Chessboard.js CSS (board and pieces) -->
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.css"
  />

  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f0f2f5;
      margin: 0;
      padding: 20px;
      display: flex;
      flex-direction: column;
      align-items: center;
      color: #333;
    }

    h1 {
      margin-bottom: 10px;
      font-size: 24px;
    }

    #controls {
      margin-bottom: 15px;
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      align-items: center;
      justify-content: center;
    }

    #scenarioSelect {
      padding: 4px 6px;
      font-size: 14px;
    }

    button {
      padding: 6px 10px;
      font-size: 14px;
      border: 1px solid #666;
      border-radius: 3px;
      background: #fff;
      cursor: pointer;
    }

    button:hover {
      background: #eee;
    }

    #board {
      width: 400px;
      max-width: 90vw;
      border: 4px solid #444;
      box-shadow: 0 0 10px rgba(0,0,0,0.25);
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    #board.correct {
      border-color: #2e7d32;
      box-shadow: 0 0 20px rgba(46,125,50,0.7);
    }

    #board.incorrect {
      border-color: #c62828;
      box-shadow: 0 0 20px rgba(198,40,40,0.7);
    }

    #status {
      margin-top: 12px;
      min-height: 20px;
      font-size: 15px;
      text-align: center;
    }

    #status span.label {
      font-weight: bold;
    }
  </style>
</head>
<body>
  <h1>Mate in 1 – Endgame Practice (White to Move)</h1>

  <div id="controls">
    <label for="scenarioSelect">Scenario:</label>
    <select id="scenarioSelect">
      <option value="0">Scenario 1 – Queen vs King (corner)</option>
      <option value="1">Scenario 2 – Queen vs King (edge)</option>
      <option value="2">Scenario 3 – Queen vs King (opposite corner)</option>
    </select>
    <button id="loadBtn">Load Scenario</button>
    <button id="resetBtn">Reset Position</button>
  </div>

  <div id="board"></div>
  <div id="status"></div>

  <!-- Chess rules engine -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.13.4/chess.min.js"></script>
  <!-- Chessboard UI -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.js"></script>

  <script>
    // Mate-in-1 scenarios for White (FEN strings)
    // All are King+Queen vs King endgames, White to move.
    const scenarios = [
      {
        name: 'Scenario 1 – Queen vs King (corner)',
        // White: Kc6, Qe7; Black: Ka8 — one solution: Qb7#
        fen: 'k7/4Q3/2K5/8/8/8/8/8 w - - 0 1'
      },
      {
        name: 'Scenario 2 – Queen vs King (edge)',
        // White: Kf7, Qg6; Black: Kh8 — solution: Qg8#
        fen: '7k/5K2/6Q1/8/8/8/8/8 w - - 0 1'
      },
      {
        name: 'Scenario 3 – Queen vs King (opposite corner)',
        // White: Kc2, Qb5; Black: Ka1 — solution: Qb2#
        fen: '8/8/8/1Q6/8/8/2K5/k7 w - - 0 1'
      }
    ];

    let board = null;
    let game = null;
    let currentScenarioIndex = 0;
    let puzzleFinished = false;

    const statusEl = document.getElementById('status');
    const boardEl = document.getElementById('board');
    const scenarioSelect = document.getElementById('scenarioSelect');
    const loadBtn = document.getElementById('loadBtn');
    const resetBtn = document.getElementById('resetBtn');

    function setStatus(message, color) {
      statusEl.textContent = message;
      statusEl.style.color = color || '#333';
    }

    function clearBoardHighlight() {
      boardEl.classList.remove('correct');
      boardEl.classList.remove('incorrect');
    }

    function loadScenario(index) {
      currentScenarioIndex = index;
      const fen = scenarios[index].fen;
      game = new Chess(fen);
      board.position(fen);
      puzzleFinished = false;
      clearBoardHighlight();
      setStatus('White to move. Find checkmate in one move.');
    }

    function onDragStart(source, piece, position, orientation) {
      // Prevent moves after puzzle resolved/attempted
      if (puzzleFinished) return false;

      // Only allow dragging white pieces
      if (piece[0] !== 'w') return false;

      // Only allow if it's actually White to move
      if (game.turn() !== 'w') return false;

      // If game is somehow over, no moves
      if (game.game_over()) return false;
    }

    function onDrop(source, target, piece, newPos, oldPos, orientation) {
      // Try to make move in game engine
      const move = game.move({
        from: source,
        to: target,
        promotion: 'q' // always promote to queen if needed
      });

      // Illegal move
      if (move === null) return 'snapback';

      // One move only in this puzzle
      puzzleFinished = true;

      // Update board after move animation
      window.setTimeout(function () {
        board.position(game.fen());
      }, 0);

      clearBoardHighlight();

      if (game.in_checkmate()) {
        boardEl.classList.add('correct');
        setStatus('Checkmate! Well done.', '#2e7d32');
      } else if (game.in_check()) {
        boardEl.classList.add('incorrect');
        setStatus('That move gives check, but it is not checkmate. Use "Reset Position" to try again.', '#c62828');
      } else {
        boardEl.classList.add('incorrect');
        setStatus('That move is not checkmate. Use "Reset Position" to try again.', '#c62828');
      }
    }

    function onSnapEnd() {
      board.position(game.fen());
    }

    document.addEventListener('DOMContentLoaded', function () {
      const config = {
        draggable: true,
        position: scenarios[0].fen,
        orientation: 'white',
        onDragStart: onDragStart,
        onDrop: onDrop,
        onSnapEnd: onSnapEnd
      };

      board = Chessboard('board', config);
      loadScenario(0);

      // Scenario selection
      loadBtn.addEventListener('click', function () {
        const index = parseInt(scenarioSelect.value, 10);
        loadScenario(index);
      });

      // Reset current scenario
      resetBtn.addEventListener('click', function () {
        loadScenario(currentScenarioIndex);
      });
    });
  </script>
</body>
</html>
```