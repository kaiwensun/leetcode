class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        pattern_digest = self.digest(pattern)
        return [word for word in words if self.digest(word) == pattern_digest]
        
    def digest(self, word):
        counter = collections.Counter(word)
        rank = collections.Counter()
        rval = []
        for c in word:
            rval.append((counter[c], rank[counter[c]]))
            counter[c] += 1
        return tuple(rval)
