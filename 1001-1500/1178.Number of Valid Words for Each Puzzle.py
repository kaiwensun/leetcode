class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        
        def insertTrie(trie, word):
            if len(word) <= 7:
                for c in word:
                    trie = trie[c]
                trie['#'] = trie.get('#', 0) + 1

        def query(trie, puzzle_list, head, index):
            res = trie.get('#', 0) if head is None else 0
            while index < len(puzzle_list):
                c = puzzle_list[index]
                if c in trie:
                    p = puzzle_list[index]
                    c_missmatches = False
                    while c > p:
                        index += 1
                        if index == len(puzzle_list) or c < puzzle_list[index]:
                            c_missmatches = True
                            break
                        p = puzzle_list[index]
                    if c_missmatches:
                        continue
                    res += query(trie[c], puzzle_list, None if c == head else head, index)
                index += 1
            return res

        T = lambda: collections.defaultdict(T)
        trie = T()
        for word in words:
            insertTrie(trie, sorted(set(word)))
        return [query(trie, sorted(set(puzzle)), puzzle[0], 0) for puzzle in puzzles]
