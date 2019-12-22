import collections
class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        T = lambda: collections.defaultdict(T)
        trie = T()
        data = [[trie, set(), i] for i in xrange(len(s))]
        res = 0
        for l in xrange(minSize):
            for start in xrange(len(s)):
                index = start + l
                if index == len(s):
                    break
                this_data = data[start]
                c = s[index]
                this_data[1].add(c)
                if len(this_data[1]) <= maxLetters and l == minSize - 1:
                    this_data[0][c].setdefault("#", 0)
                    this_data[0][c]["#"] += 1
                    res = max(res, this_data[0][c]["#"])
                this_data[0] = this_data[0][c]
        return res
