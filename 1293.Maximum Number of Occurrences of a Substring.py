import collections
class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        T = lambda: collections.defaultdict(T)
        trie = T()
        data = [[trie, set(), i] for i in xrange(len(s))]
        res = 0
        for l in xrange(maxSize):
            for start in xrange(len(s)):
                if data[start] == None:
                    break
                index = start + l
                if index == len(s):
                    break
                this_data = data[start]
                c = s[index]
                this_data[0][c].setdefault("#", 0)
                this_data[0][c]["#"] += 1
                this_data[1].add(c)
                if len(this_data[1]) <= maxLetters and l >= minSize - 1:
                    res = max(res, this_data[0][c]["#"])
                if this_data[0][c]["#"] < res - 1:
                    data[start] = None
                this_data[0] = this_data[0][c]
        return res
