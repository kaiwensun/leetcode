import collections
class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        :type text: str
        :rtype: int
        """
        T = lambda: collections.defaultdict(T)
        trie = T()
        res = 0
        for start in xrange(len(text)):
            t = trie
            for i in xrange(start, len(text)):
                t = t[text[i]]
                if "found" in t:
                    continue
                if i - start + 1 > len(text) - i and i - start + 1 > start:
                    break
                t.setdefault("indexes", set()).add(i)
                if start - 1 in t["indexes"]:
                    res += 1
                    t["found"] = True
        return res
