import collections
class Solution:
    def anagramMappings(self, A, B):
        mapping = collections.defaultdict(list)
        for i, num in enumerate(B):
            mapping[num].append(i)
        res = []
        for num in A:
            res.append(mapping[num].pop())
        return res

