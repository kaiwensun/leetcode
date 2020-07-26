class Solution(object):
    def findWords(self, board, words):
        T = lambda: collections.defaultdict(T)
        trie = T()
        for word in words:
            reduce(lambda t, c: t[c], word + '#', trie)
        res = []
        def dfs(trie, i, j, path):
            if '#' in trie:
                res.append(''.join(path))
                del trie['#']
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                c = board[i][j]
                if c in trie:
                    delta = (1, 0, -1, 0, 1)
                    path.append(c)
                    board[i][j] = ord(board[i][j])
                    for _ in xrange(4):
                        x, y = i + delta[_], j + delta[_ + 1]
                        dfs(trie[c], x, y, path)
                    path.pop()
                    board[i][j] = chr(board[i][j])
                if len(trie[c]) == 0:
                    del trie[c]
        for r in xrange(len(board)):
            for c in xrange(len(board[0])):
                dfs(trie, r, c, [])
        return res
