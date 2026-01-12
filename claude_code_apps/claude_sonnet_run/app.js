const PIECES = {
    K: '♔', Q: '♕', R: '♖', B: '♗', N: '♘', P: '♙',
    k: '♚', q: '♛', r: '♜', b: '♝', n: '♞', p: '♟'
};

const scenarios = [
    {
        name: "Queen Mate",
        position: [
            ['', '', '', '', '', '', '', 'k'],
            ['', '', '', '', '', 'Q', '', ''],
            ['', '', '', '', '', '', 'K', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ],
        description: "Move the queen to deliver checkmate!"
    },
    {
        name: "Two Rooks Mate",
        position: [
            ['', '', '', '', '', '', '', 'k'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', 'R', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', 'K', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['R', '', '', '', '', '', '', '']
        ],
        description: "Move a rook to deliver checkmate!"
    },
    {
        name: "Ladder Mate",
        position: [
            ['', '', '', '', '', '', 'k', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', 'R', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', 'K', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', 'R', '', '', '']
        ],
        description: "Move a rook to deliver checkmate!"
    }
];

let currentScenario = 0;
let board = [];
let selectedSquare = null;
let moveCount = 0;
let initialPosition = [];

function initBoard() {
    board = JSON.parse(JSON.stringify(scenarios[currentScenario].position));
    initialPosition = JSON.parse(JSON.stringify(board));
    moveCount = 0;
    renderBoard();
    hideFeedback();
}

function renderBoard() {
    const boardElement = document.getElementById('board');
    boardElement.innerHTML = '';

    for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
            const square = document.createElement('div');
            square.className = 'square';
            square.className += (row + col) % 2 === 0 ? ' light' : ' dark';
            square.dataset.row = row;
            square.dataset.col = col;

            const piece = board[row][col];
            if (piece) {
                square.textContent = PIECES[piece];
                square.draggable = true;
                square.addEventListener('dragstart', handleDragStart);
            }

            square.addEventListener('dragover', handleDragOver);
            square.addEventListener('drop', handleDrop);
            square.addEventListener('dragend', handleDragEnd);
            square.addEventListener('click', handleSquareClick);

            boardElement.appendChild(square);
        }
    }
}

function handleDragStart(e) {
    const square = e.target;
    const row = parseInt(square.dataset.row);
    const col = parseInt(square.dataset.col);
    const piece = board[row][col];

    if (piece && piece === piece.toUpperCase()) {
        selectedSquare = {row, col};
        square.classList.add('dragging');
        e.dataTransfer.effectAllowed = 'move';
        e.dataTransfer.setData('text/html', square.innerHTML);
    } else {
        e.preventDefault();
    }
}

function handleDragOver(e) {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
    const square = e.currentTarget;
    square.classList.add('drag-over');
    return false;
}

function handleDrop(e) {
    e.preventDefault();
    e.stopPropagation();

    const square = e.currentTarget;
    square.classList.remove('drag-over');

    if (selectedSquare) {
        const toRow = parseInt(square.dataset.row);
        const toCol = parseInt(square.dataset.col);
        makeMove(selectedSquare.row, selectedSquare.col, toRow, toCol);
    }

    return false;
}

function handleDragEnd(e) {
    const squares = document.querySelectorAll('.square');
    squares.forEach(square => {
        square.classList.remove('dragging');
        square.classList.remove('drag-over');
    });
}

function handleSquareClick(e) {
    const square = e.currentTarget;
    const row = parseInt(square.dataset.row);
    const col = parseInt(square.dataset.col);
    const piece = board[row][col];

    if (selectedSquare) {
        if (selectedSquare.row === row && selectedSquare.col === col) {
            selectedSquare = null;
            clearHighlights();
        } else {
            makeMove(selectedSquare.row, selectedSquare.col, row, col);
        }
    } else if (piece && piece === piece.toUpperCase()) {
        selectedSquare = {row, col};
        highlightSquare(row, col);
    }
}

function highlightSquare(row, col) {
    clearHighlights();
    const squares = document.querySelectorAll('.square');
    const index = row * 8 + col;
    squares[index].classList.add('last-move');
}

function clearHighlights() {
    const squares = document.querySelectorAll('.square');
    squares.forEach(square => square.classList.remove('last-move'));
}

function makeMove(fromRow, fromCol, toRow, toCol) {
    const piece = board[fromRow][fromCol];

    if (!piece || piece !== piece.toUpperCase()) {
        selectedSquare = null;
        clearHighlights();
        return;
    }

    board[toRow][toCol] = piece;
    board[fromRow][fromCol] = '';
    moveCount++;

    selectedSquare = null;
    renderBoard();

    setTimeout(() => {
        if (checkMate()) {
            showFeedback('Checkmate! Well done!', 'success');
        } else {
            showFeedback('Not checkmate. Try again!', 'error');
            setTimeout(() => resetPosition(), 1500);
        }
    }, 100);
}

function checkMate() {
    const kingPos = findKing();
    if (!kingPos) return false;

    if (!isKingInCheck(kingPos.row, kingPos.col)) {
        return false;
    }

    const directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],           [0, 1],
        [1, -1],  [1, 0],  [1, 1]
    ];

    for (const [dr, dc] of directions) {
        const newRow = kingPos.row + dr;
        const newCol = kingPos.col + dc;

        if (newRow >= 0 && newRow < 8 && newCol >= 0 && newCol < 8) {
            const targetPiece = board[newRow][newCol];
            if (!targetPiece || targetPiece === targetPiece.toLowerCase()) {
                const originalPiece = board[newRow][newCol];
                board[newRow][newCol] = 'k';
                board[kingPos.row][kingPos.col] = '';

                const stillInCheck = isKingInCheck(newRow, newCol);

                board[kingPos.row][kingPos.col] = 'k';
                board[newRow][newCol] = originalPiece;

                if (!stillInCheck) {
                    return false;
                }
            }
        }
    }

    return true;
}

function findKing() {
    for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
            if (board[row][col] === 'k') {
                return {row, col};
            }
        }
    }
    return null;
}

function isKingInCheck(kingRow, kingCol) {
    if (isAttackedByPawn(kingRow, kingCol)) return true;
    if (isAttackedByKnight(kingRow, kingCol)) return true;
    if (isAttackedByRookOrQueen(kingRow, kingCol)) return true;
    if (isAttackedByBishopOrQueen(kingRow, kingCol)) return true;
    if (isAttackedByKing(kingRow, kingCol)) return true;
    return false;
}

function isAttackedByPawn(row, col) {
    const pawnMoves = [[1, -1], [1, 1]];
    for (const [dr, dc] of pawnMoves) {
        const newRow = row + dr;
        const newCol = col + dc;
        if (newRow >= 0 && newRow < 8 && newCol >= 0 && newCol < 8) {
            if (board[newRow][newCol] === 'P') {
                return true;
            }
        }
    }
    return false;
}

function isAttackedByKnight(row, col) {
    const knightMoves = [
        [-2, -1], [-2, 1], [-1, -2], [-1, 2],
        [1, -2], [1, 2], [2, -1], [2, 1]
    ];
    for (const [dr, dc] of knightMoves) {
        const newRow = row + dr;
        const newCol = col + dc;
        if (newRow >= 0 && newRow < 8 && newCol >= 0 && newCol < 8) {
            if (board[newRow][newCol] === 'N') {
                return true;
            }
        }
    }
    return false;
}

function isAttackedByRookOrQueen(row, col) {
    const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    for (const [dr, dc] of directions) {
        let newRow = row + dr;
        let newCol = col + dc;
        while (newRow >= 0 && newRow < 8 && newCol >= 0 && newCol < 8) {
            const piece = board[newRow][newCol];
            if (piece) {
                if (piece === 'R' || piece === 'Q') {
                    return true;
                }
                break;
            }
            newRow += dr;
            newCol += dc;
        }
    }
    return false;
}

function isAttackedByBishopOrQueen(row, col) {
    const directions = [[1, 1], [1, -1], [-1, 1], [-1, -1]];
    for (const [dr, dc] of directions) {
        let newRow = row + dr;
        let newCol = col + dc;
        while (newRow >= 0 && newRow < 8 && newCol >= 0 && newCol < 8) {
            const piece = board[newRow][newCol];
            if (piece) {
                if (piece === 'B' || piece === 'Q') {
                    return true;
                }
                break;
            }
            newRow += dr;
            newCol += dc;
        }
    }
    return false;
}

function isAttackedByKing(row, col) {
    const directions = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1],           [0, 1],
        [1, -1],  [1, 0],  [1, 1]
    ];
    for (const [dr, dc] of directions) {
        const newRow = row + dr;
        const newCol = col + dc;
        if (newRow >= 0 && newRow < 8 && newCol >= 0 && newCol < 8) {
            if (board[newRow][newCol] === 'K') {
                return true;
            }
        }
    }
    return false;
}

function showFeedback(message, type) {
    const feedback = document.getElementById('feedback');
    feedback.textContent = message;
    feedback.className = `feedback ${type}`;
}

function hideFeedback() {
    const feedback = document.getElementById('feedback');
    feedback.className = 'feedback hidden';
}

function resetPosition() {
    board = JSON.parse(JSON.stringify(initialPosition));
    moveCount = 0;
    selectedSquare = null;
    renderBoard();
    hideFeedback();
}

document.getElementById('scenario').addEventListener('change', (e) => {
    currentScenario = parseInt(e.target.value);
    initBoard();
});

document.getElementById('reset').addEventListener('click', resetPosition);

initBoard();
