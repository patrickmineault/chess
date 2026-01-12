```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Chess Endgame – Mate in 1 Trainer</title>

  <!-- Chessboard.js styles -->
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.css"
  />

  <style>
    body {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #f5f5f5;
      margin: 0;
      padding: 20px;
      text-align: center;
    }

    h1 {
      margin-bottom: 10px;
    }

    #controls {
      margin-bottom: 15px;
    }

    #controls label,
    #controls select,
    #controls button {
      font-size: 14px;
    }

    #controls select {
      margin: 0 6px;
      padding: 3px 6px;
    }

    #controls button {
      margin-left: 8px;
      padding: 4px 10px;
      cursor: pointer;
    }

    #board {
      width: 400px;
      max-width: 90vw;
      margin: 10px auto;
    }

    #scenarioTitle {
      margin-top: 5px;
      font-size: 16px;
      font-weight: 600;
    }

    .status {
      margin-top: 12px;
      font-size: 15px;
      min-height: 1.2em;
    }

    .status.info {
      color: #333;
    }

    .status.success {
      color: #1a7f37;
      font-weight: 600;
    }

    .status.error {
      color: #c92c2c;
      font-weight: 600;
    }
  </style>
</head>
<body>
  <h1>Chess Endgame – Mate in 1 Trainer</h1>

  <div id="controls">
    <label>
      Scenario:
      <select id="scenarioSelect">
        <option value="0">Scenario 1</option>
        <option value="1">Scenario 2</option>
        <option value="2">Scenario 3</option>
      </select>
    </label>

    <button id="resetBtn">Reset Position</button>
  </div>

  <div id="scenarioTitle"></div>
  <div id="board"></div>
  <div id="status" class="status"></div>

  <!-- Dependencies -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/chess.js/0.13.4/chess.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/chessboard-js/1.0.0/chessboard-1.0.0.min.js"></script>

  <script>
    document.addEventListener('DOMContentLoaded', function () {
      // Three mate-in-1 positions for White (all legal FENs, White to move)
      const scenarios = [
        {
          name: 'Scenario 1 – Queen & King vs King',
          // White: Kg1, Qg1; Black: Kh3
          fen: '8/8/8/8/8/7k/8/6QK w - - 0 1'
        },
        {
          name: 'Scenario 2 – Rook & King vs King',
          // White: Kg6, Rf5; Black: Kh8 (Rf8# is mate)
          fen: '7k/8/6K1/5R2/8/8/8/8 w - - 0 1'
        },
        {
          name: 'Scenario 3 – Queen & King vs King (different pattern)',
          // White: Kc6, Qg7; Black: Ka8 (Qb7# is mate)
          fen: 'k7/6Q1/2K5/8/8/8/8/8 w - - 0 1'
        }
      ];

      let game = new Chess(scenarios[0].fen);
      let solved = false;
      let currentScenarioIndex = 0;

      const statusEl = document.getElementById('status');
      const scenarioTitleEl = document.getElementById('scenarioTitle');

      function setStatus(message, type) {
        statusEl.textContent = message;
        statusEl.className = 'status ' + (type || '');
      }

      let board; // will be initialized below

      function loadScenario(index) {
        currentScenarioIndex = index;
        solved = false;

        const scenario = scenarios[index];
        game = new Chess(scenario.fen);

        // Chessboard.js only needs the piece placement part of the FEN
        const piecePlacement = scenario.fen.split(' ')[0];
        board.position(piecePlacement, false);

        scenarioTitleEl.textContent = scenario.name;
        setStatus('White to move. Find mate in 1.', 'info');
      }

      function onDragStart(source, piece, position, orientation) {
        // Do not allow moves if puzzle is solved
        if (solved) return false;

        // Only allow White to move
        if (game.turn() !== 'w') return false;

        // Only allow dragging white pieces
        if (piece[0] !== 'w') return false;

        return true;
      }

      function onDrop(source, target) {
        const move = game.move({
          from: source,
          to: target,
          promotion: 'q' // auto-queen if a pawn promotes
        });

        // Illegal move: snap back
        if (move === null) {
          return 'snapback';
        }

        // Legal move: evaluate board
        if (game.in_checkmate()) {
          solved = true;
          setStatus('Checkmate! Well done.', 'success');
        } else if (game.in_check()) {
          setStatus('That gives check, but it is not checkmate. Try again or reset.', 'info');
        } else {
          setStatus('Not checkmate. Try again or reset the position.', 'error');
        }
      }

      function onSnapEnd() {
        // Update the board position to match the game
        board.position(game.fen());
      }

      const config = {
        draggable: true,
        position: scenarios[0].fen.split(' ')[0],
        orientation: 'white',
        onDragStart: onDragStart,
        onDrop: onDrop,
        onSnapEnd: onSnapEnd
      };

      // Support both Chessboard and ChessBoard globals (depending on version)
      if (window.Chessboard) {
        board = Chessboard('board', config);
      } else {
        board = ChessBoard('board', config);
      }

      // Scenario selection
      const selectEl = document.getElementById('scenarioSelect');
      selectEl.addEventListener('change', function () {
        const index = parseInt(this.value, 10);
        loadScenario(index);
      });

      // Reset button
      document.getElementById('resetBtn').addEventListener('click', function () {
        loadScenario(currentScenarioIndex);
      });

      // Initialize first scenario
      loadScenario(0);
    });
  </script>
</body>
</html>
```