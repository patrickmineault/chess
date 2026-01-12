// Properly validate chess positions
const PIECES = {
    K: '♔', Q: '♕', R: '♖', B: '♗', N: '♘', P: '♙',
    k: '♚', q: '♛', r: '♜', b: '♝', n: '♞', p: '♟'
};

let board = [];

function findKings() {
    let whiteKing = null;
    let blackKing = null;
    for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
            if (board[row][col] === 'K') whiteKing = {row, col};
            if (board[row][col] === 'k') blackKing = {row, col};
        }
    }
    return {whiteKing, blackKing};
}

function isPositionValid() {
    const {whiteKing, blackKing} = findKings();

    // Both kings must exist
    if (!whiteKing || !blackKing) return false;

    // Kings cannot be adjacent
    const rowDiff = Math.abs(whiteKing.row - blackKing.row);
    const colDiff = Math.abs(whiteKing.col - blackKing.col);
    if (rowDiff <= 1 && colDiff <= 1) return false;

    // White king should not be in check (it's white's turn)
    if (isSquareAttackedBy(whiteKing.row, whiteKing.col, 'black')) return false;

    return true;
}

function isSquareAttackedBy(row, col, color) {
    if (color === 'black') {
        if (isAttackedByBlackPawn(row, col)) return true;
        if (isAttackedByPiece(row, col, 'n')) return true;
        if (isAttackedByRookOrQueen(row, col, 'r', 'q')) return true;
        if (isAttackedByBishopOrQueen(row, col, 'b', 'q')) return true;
        if (isAttackedByPiece(row, col, 'k')) return true;
    } else {
        if (isAttackedByWhitePawn(row, col)) return true;
        if (isAttackedByPiece(row, col, 'N')) return true;
        if (isAttackedByRookOrQueen(row, col, 'R', 'Q')) return true;
        if (isAttackedByBishopOrQueen(row, col, 'B', 'Q')) return true;
        if (isAttackedByPiece(row, col, 'K')) return true;
    }
    return false;
}

function isAttackedByBlackPawn(row, col) {
    const pawnMoves = [[-1, -1], [-1, 1]]; // Black pawns attack upward
    for (const [dr, dc] of pawnMoves) {
        const newRow = row + dr;
        const newCol = col + dc;
        if (newRow >= 0 && newRow < 8 && newCol >= 0 && newCol < 8) {
            if (board[newRow][newCol] === 'p') return true;
        }
    }
    return false;
}

function isAttackedByWhitePawn(row, col) {
    const pawnMoves = [[1, -1], [1, 1]]; // White pawns attack downward
    for (const [dr, dc] of pawnMoves) {
        const newRow = row + dr;
        const newCol = col + dc;
        if (newRow >= 0 && newRow < 8 && newCol >= 0 && newCol < 8) {
            if (board[newRow][newCol] === 'P') return true;
        }
    }
    return false;
}

function isAttackedByPiece(row, col, piece) {
    const isKnight = piece.toLowerCase() === 'n';
    const isKing = piece.toLowerCase() === 'k';

    let moves;
    if (isKnight) {
        moves = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]];
    } else if (isKing) {
        moves = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];
    } else {
        return false;
    }

    for (const [dr, dc] of moves) {
        const newRow = row + dr;
        const newCol = col + dc;
        if (newRow >= 0 && newRow < 8 && newCol >= 0 && newCol < 8) {
            if (board[newRow][newCol] === piece) return true;
        }
    }
    return false;
}

function isAttackedByRookOrQueen(row, col, rook, queen) {
    const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    for (const [dr, dc] of directions) {
        let newRow = row + dr;
        let newCol = col + dc;
        while (newRow >= 0 && newRow < 8 && newCol >= 0 && newCol < 8) {
            const piece = board[newRow][newCol];
            if (piece) {
                if (piece === rook || piece === queen) return true;
                break;
            }
            newRow += dr;
            newCol += dc;
        }
    }
    return false;
}

function isAttackedByBishopOrQueen(row, col, bishop, queen) {
    const directions = [[1, 1], [1, -1], [-1, 1], [-1, -1]];
    for (const [dr, dc] of directions) {
        let newRow = row + dr;
        let newCol = col + dc;
        while (newRow >= 0 && newRow < 8 && newCol >= 0 && newCol < 8) {
            const piece = board[newRow][newCol];
            if (piece) {
                if (piece === bishop || piece === queen) return true;
                break;
            }
            newRow += dr;
            newCol += dc;
        }
    }
    return false;
}

function checkMate() {
    const {blackKing} = findKings();
    if (!blackKing) return false;

    // Black king must be in check
    if (!isSquareAttackedBy(blackKing.row, blackKing.col, 'white')) return false;

    const directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];

    for (const [dr, dc] of directions) {
        const newRow = blackKing.row + dr;
        const newCol = blackKing.col + dc;

        if (newRow >= 0 && newRow < 8 && newCol >= 0 && newCol < 8) {
            const targetPiece = board[newRow][newCol];
            if (!targetPiece || targetPiece === targetPiece.toLowerCase()) {
                const originalPiece = board[newRow][newCol];
                board[newRow][newCol] = 'k';
                board[blackKing.row][blackKing.col] = '';

                const stillInCheck = isSquareAttackedBy(newRow, newCol, 'white');

                board[blackKing.row][blackKing.col] = 'k';
                board[newRow][newCol] = originalPiece;

                if (!stillInCheck) return false;
            }
        }
    }

    return true;
}

function findMateInOne(position) {
    board = JSON.parse(JSON.stringify(position));

    // First check if position is valid
    if (!isPositionValid()) {
        return {valid: false, mates: []};
    }

    const whitePieces = [];
    for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
            const piece = board[row][col];
            if (piece && piece === piece.toUpperCase() && piece !== 'K') {
                whitePieces.push({row, col, piece});
            }
        }
    }

    const mateInOneMoves = [];
    for (const {row: fromRow, col: fromCol, piece} of whitePieces) {
        for (let toRow = 0; toRow < 8; toRow++) {
            for (let toCol = 0; toCol < 8; toCol++) {
                if (toRow === fromRow && toCol === fromCol) continue;
                const targetPiece = board[toRow][toCol];
                if (targetPiece && targetPiece === targetPiece.toUpperCase()) continue;

                const originalPiece = board[toRow][toCol];
                board[toRow][toCol] = piece;
                board[fromRow][fromCol] = '';

                if (checkMate()) {
                    const fromSquare = String.fromCharCode(97 + fromCol) + (8 - fromRow);
                    const toSquare = String.fromCharCode(97 + toCol) + (8 - toRow);
                    mateInOneMoves.push(`${PIECES[piece]} ${fromSquare} to ${toSquare}`);
                }

                board[fromRow][fromCol] = piece;
                board[toRow][toCol] = originalPiece;
            }
        }
    }

    return {valid: true, mates: mateInOneMoves};
}

// Test some classic positions
console.log("=== Testing Classic Mate-in-1 Positions ===\n");

// Back rank mate
const backRank = [
    ['r', '', '', '', '', 'r', 'k', ''],
    ['p', 'p', 'p', '', '', 'p', 'p', 'p'],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['P', 'P', 'P', '', '', 'P', 'P', 'P'],
    ['R', '', '', '', '', '', 'K', '']
];
console.log("1. Back Rank Mate:");
let result = findMateInOne(backRank);
console.log(`Valid: ${result.valid}`);
if (result.valid && result.mates.length > 0) {
    console.log(`Mates: ${result.mates.slice(0, 3)}`);
} else {
    console.log("No mates found");
}

// Queen and King vs King
const queenKing = [
    ['', '', '', '', '', '', '', 'k'],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', 'Q', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', 'K', '', '']
];
console.log("\n2. Queen + King vs King:");
result = findMateInOne(queenKing);
console.log(`Valid: ${result.valid}`);
if (result.valid && result.mates.length > 0) {
    console.log(`Mates: ${result.mates.slice(0, 3)}`);
} else {
    console.log("No mates found");
}

// Rook and King vs King
const rookKing = [
    ['', '', '', '', '', '', '', 'k'],
    ['', '', '', '', '', '', 'R', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', 'K', '', ''],
    ['', '', '', '', '', '', '', '']
];
console.log("\n3. Rook + King vs King:");
result = findMateInOne(rookKing);
console.log(`Valid: ${result.valid}`);
if (result.valid && result.mates.length > 0) {
    console.log(`Mates: ${result.mates.slice(0, 3)}`);
} else {
    console.log("No mates found");
}
