# @param {Character[][]} board
# @param {String[]} words
# @return {String[]}

DELTA = [1, 0, -1, 0, 1]
def find_words(board, words)
    trie = Trie()
    for word in words
        p = trie
        for c in word.each_char
            p = p[c]
        end
        p["#"] = word.freeze
    end
    res, seen = Set.new, Set.new
    for i in 0...board.size
        for j in 0...board[0].size
            dfs(i, j, board, seen, trie, res)
        end
    end
    res.to_a
end

def Trie
    return Hash.new { |h, k| h[k] = Trie() }
end

def dfs(i, j, board, seen, trie, res)
    if 0 <= i && i < board.size && 0 <= j && j < board[0].size && !seen.include?([i, j])
        if trie.include? board[i][j]
            trie = trie[board[i][j]]
            seen << [i, j]
            if trie.include? "#"
                res << trie["#"]
            end
            for k in 0...4
                dfs(i + DELTA[k], j + DELTA[k + 1], board, seen, trie, res)
            end
            seen.delete [i, j]
        end
    end
end
