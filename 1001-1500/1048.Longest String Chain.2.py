import functools
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        len2words = collections.defaultdict(list)
        for word in words:
            len2words[len(word)].append(word)
        def isPre(w1, w2):
            # assume len(w1) + 1 == len(w2)
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    return w1[i:] == w2[i + 1:]
            return True
        @functools.lru_cache(len(words) + 1)
        def getLongest(word):
            if word is None:
                return 0
            return max([getLongest(follow) for follow in len2words[len(word) + 1] if isPre(word, follow)] or [0]) + 1
        return max(getLongest(word) for word in words)
