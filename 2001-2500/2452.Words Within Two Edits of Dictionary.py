from collections import defaultdict

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        Trie = lambda: defaultdict(Trie)
        trie = Trie()

        def put(word, trie):
            p = trie
            for c in word:
                p = p[c]

        def search(word, i, trie, edit):
            if i == len(word):
                return True
            c = word[i]
            if c in trie and search(word, i + 1, trie[c], edit):
                return True
            if edit < 2:
                return any(search(word, i + 1, trie[c], edit + 1) for c in trie.keys())
            return False

        for word in dictionary:
            put(word, trie)
        return [query for query in queries if search(query, 0, trie, 0)]


