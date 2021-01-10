from collections import Counter, defaultdict
class Solution(object):
    def minimumHammingDistance(self, source, target, allowedSwaps):
        """
        :type source: List[int]
        :type target: List[int]
        :type allowedSwaps: List[List[int]]
        :rtype: int
        """
        data = range(len(source))
        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]
        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                data[rx] = ry
        for x, y in allowedSwaps:
            union(x, y)
        counters = defaultdict(Counter)
        for i, num in enumerate(source):
            counters[find(i)][num] += 1
        for i, num in enumerate(target):
            counters[find(i)][num] -= 1
        res = 0
        for counter in counters.values():
            res += sum(map(abs, counter.values()))
        return res // 2

