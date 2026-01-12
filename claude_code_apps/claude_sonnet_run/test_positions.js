// Test script to validate chess positions and find mate-in-1
const PIECES = {
    K: '♔', Q: '♕', R: '♖', B: '♗', N: '♘', P: '♙',
    k: '♚', q: '♛', r: '♜', b: '♝', n: '♞', p: '♟'
};

// Copy all the chess logic from app.js
let board = [];

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

function testPosition(position, name) {
    console.log(`\nTesting: ${name}`);
    board = JSON.parse(JSON.stringify(position));

    // Print the position
    console.log("Position:");
    for (let row = 0; row < 8; row++) {
        let rowStr = (8 - row) + " ";
        for (let col = 0; col < 8; col++) {
            const piece = board[row][col];
            rowStr += piece ? PIECES[piece] + " " : ". ";
        }
        console.log(rowStr);
    }
    console.log("  a b c d e f g h");

    // Find all white pieces
    const whitePieces = [];
    for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
            const piece = board[row][col];
            if (piece && piece === piece.toUpperCase() && piece !== 'K') {
                whitePieces.push({row, col, piece});
            }
        }
    }

    console.log(`\nWhite pieces: ${whitePieces.length}`);

    // Try all possible moves for white pieces
    const mateInOneMoves = [];
    for (const {row: fromRow, col: fromCol, piece} of whitePieces) {
        // Try all squares
        for (let toRow = 0; toRow < 8; toRow++) {
            for (let toCol = 0; toCol < 8; toCol++) {
                if (toRow === fromRow && toCol === fromCol) continue;

                const targetPiece = board[toRow][toCol];
                if (targetPiece && targetPiece === targetPiece.toUpperCase()) continue;

                // Make the move
                const originalPiece = board[toRow][toCol];
                board[toRow][toCol] = piece;
                board[fromRow][fromCol] = '';

                if (checkMate()) {
                    const fromSquare = String.fromCharCode(97 + fromCol) + (8 - fromRow);
                    const toSquare = String.fromCharCode(97 + toCol) + (8 - toRow);
                    mateInOneMoves.push(`${PIECES[piece]} ${fromSquare} to ${toSquare}`);
                }

                // Undo the move
                board[fromRow][fromCol] = piece;
                board[toRow][toCol] = originalPiece;
            }
        }
    }

    if (mateInOneMoves.length > 0) {
        console.log(`✓ Valid! Found ${mateInOneMoves.length} mate-in-1 move(s):`);
        mateInOneMoves.forEach(move => console.log(`  - ${move}`));
    } else {
        console.log("✗ Invalid! No mate-in-1 found.");
    }

    return mateInOneMoves.length > 0;
}

// Test the current scenarios
const scenarios = [
    {
        name: "Scenario 1: Rook Mate",
        position: [
            ['', '', '', '', '', '', 'R', 'k'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', 'K', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
    },
    {
        name: "Scenario 2: Queen Mate",
        position: [
            ['', '', '', '', '', '', '', 'k'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', 'K', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', 'Q', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', '']
        ]
    },
    {
        name: "Scenario 3: Two Rooks Mate",
        position: [
            ['', '', '', '', '', '', '', 'k'],
            ['', '', '', '', '', '', 'R', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', 'K', '', '', '', 'R']
        ]
    }
];

console.log("=== Testing Chess Positions ===");
scenarios.forEach(scenario => testPosition(scenario.position, scenario.name));
