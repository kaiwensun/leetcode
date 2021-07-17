class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for s in strs:
            h = [0] * 26
            for c in s:
                h[ord(c) - ord('a')] += 1
            res[tuple(h)].append(s)
        return res.values()

