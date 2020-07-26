# @param {Character[][]} board
# @return {Void} Do not return anything, modify board in-place instead.
DELTA = [1, 0, -1, 0, 1]
def solve(board)
    if board.any? and board[0].any?
        flip_border(board, 'O', '#')
        flip_all(board, 'O', 'X')
        flip_border(board, '#', 'O')
    end
end

def flip_all(board, from, to)
    for i in 0...board.size
        for j in 0...board[i].size
            board[i][j] = to if board[i][j] == from
        end
    end
end

def flip_border(board, from, to)
    for i in 0...board.size
        flip(board, i, 0, from, to)
        flip(board, i, board[i].size - 1, from, to)
    end
    for j in 0...board[0].size
        flip(board, 0, j, from, to)
        flip(board, board.size - 1, j, from, to)
    end
end

def flip(board, i, j, from, to)
    if 0 <= i && i < board.size && 0 <= j && j < board[0].size
        if board[i][j] == from
            board[i][j] = to
            for k in 0...4
                flip(board, i + DELTA[k], j + DELTA[k + 1], from, to)
            end
        end
    end
end
