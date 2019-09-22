import collections
class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        s = list(s)
        uf = range(len(s))
        def find(a):
            if uf[a] == a:
                return a
            uf[a] = find(uf[a])
            return uf[a]
        def union(a, b):
            uf[find(a)] = uf[find(b)]
            
        for a, b in pairs:
            union(a, b)
        groups = collections.defaultdict(list)
        for i in xrange(len(s)):
            groups[find(i)].append(i)
        for group in groups.values():
            for index, c in zip(group, sorted(map(s.__getitem__, group))):
                s[index] = c
        return ''.join(s)
