// Find good mate-in-1 positions
const PIECES = {
    K: '♔', Q: '♕', R: '♖', B: '♗', N: '♘', P: '♙',
    k: '♚', q: '♛', r: '♜', b: '♝', n: '♞', p: '♟'
};

let board = [];

function findKing() {
    for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
            if (board[row][col] === 'k') return {row, col};
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
            if (board[newRow][newCol] === 'P') return true;
        }
    }
    return false;
}

function isAttackedByKnight(row, col) {
    const knightMoves = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]];
    for (const [dr, dc] of knightMoves) {
        const newRow = row + dr;
        const newCol = col + dc;
        if (newRow >= 0 && newRow < 8 && newCol >= 0 && newCol < 8) {
            if (board[newRow][newCol] === 'N') return true;
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
                if (piece === 'R' || piece === 'Q') return true;
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
                if (piece === 'B' || piece === 'Q') return true;
                break;
            }
            newRow += dr;
            newCol += dc;
        }
    }
    return false;
}

function isAttackedByKing(row, col) {
    const directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];
    for (const [dr, dc] of directions) {
        const newRow = row + dr;
        const newCol = col + dc;
        if (newRow >= 0 && newRow < 8 && newCol >= 0 && newCol < 8) {
            if (board[newRow][newCol] === 'K') return true;
        }
    }
    return false;
}

function checkMate() {
    const kingPos = findKing();
    if (!kingPos) return false;
    if (!isKingInCheck(kingPos.row, kingPos.col)) return false;

    const directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]];

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

                if (!stillInCheck) return false;
            }
        }
    }

    return true;
}

function findMateInOne(position) {
    board = JSON.parse(JSON.stringify(position));
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

    return mateInOneMoves;
}

// Try different knight positions
console.log("=== Knight Mates ===");
const knight2 = [
    ['', '', '', '', '', '', 'k', ''],
    ['', '', '', '', '', 'K', '', ''],
    ['', '', '', '', 'N', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '']
];
console.log("Knight2:");
const k2 = findMateInOne(knight2);
console.log(k2.length > 0 ? k2.slice(0, 3) : []);

// Try bishop with king
const bishop2 = [
    ['', '', '', '', '', '', '', 'k'],
    ['', '', '', '', '', '', 'K', 'B'],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '']
];
console.log("\nBishop2:");
const b2 = findMateInOne(bishop2);
console.log(b2.length > 0 ? b2.slice(0, 3) : []);

// Two rooks
const twoRooks = [
    ['', '', '', '', '', '', '', 'k'],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', 'R', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['R', '', '', '', '', '', 'K', '']
];
console.log("\nTwo Rooks:");
const tr = findMateInOne(twoRooks);
console.log(tr.length > 0 ? tr.slice(0, 3) : []);

// Pawn mate
const pawn1 = [
    ['', '', '', '', '', '', 'k', ''],
    ['', '', '', '', '', 'P', 'K', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '']
];
console.log("\nPawn:");
const p1 = findMateInOne(pawn1);
console.log(p1.length > 0 ? p1.slice(0, 3) : []);
