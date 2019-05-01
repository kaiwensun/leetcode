class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        prev = collections.defaultdict(list)
        q = collections.deque([beginWord, '#'])
        next_set = set()
        found = False
        while len(q) > 1:
            cur = q.popleft()
            if cur == '#':
                if found:
                    break
                wordList = wordList - next_set
                next_set.clear()
                q.append('#')
                continue
            for i in xrange(len(cur)):
                for c in string.ascii_lowercase:
                    nxt = cur[:i] + c + cur[i + 1:]
                    if nxt in wordList:
                        prev[nxt].append(cur)
                        if nxt not in next_set:
                            q.append(nxt)
                            next_set.add(nxt)
                        
        else:
            print prev
            results = []
            self.dfs(endWord, [], prev, beginWord, results)
            return results
        return []
        
    def dfs(self, s, path, prev, start, results):
        path.append(s)
        if s == start:
            r = list(reversed(path))
            results.append(r)
        else:
            for p in prev[s]:
                self.dfs(p, path, prev, start, results)
        path.pop()
