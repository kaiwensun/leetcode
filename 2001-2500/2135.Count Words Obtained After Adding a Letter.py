from collections import defaultdict
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def convert(word):
            res = 0
            for c in word:
                res |= 1 << ord(c) - ord('a')
            return res

        res = 0
        starts = defaultdict(set)

        for startWord in startWords:
            n = len(startWord)
            starts[n].add(convert(startWord))
        for targetWord in targetWords:
            n = len(targetWord)
            target = convert(targetWord)
            for i in range(26):
                if target ^ (1 << i) in starts[n - 1]:
                    res += 1
                    break
        return res

