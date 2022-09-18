from collections import defaultdict

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        def put(trie, word):
            for c in word:
                trie = trie[c]
                trie.setdefault("#", 0)
                trie["#"] += 1

        def get(trie, word):
            res = 0
            for c in word:
                trie = trie[c]
                res += trie["#"]
            return res
        
        for word in words:
            put(trie, word)
        return [get(trie, word) for word in words]

