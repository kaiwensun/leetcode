class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        def calc(price):
            i = bisect.bisect_right(items, [price, float("inf")], hi=len(items) - 1)
            return items[i - 1][1]

        items.sort()
        items.append([float("-inf"), 0])
        for i in range(len(items) - 1):
            items[i][1] = max(items[i][1], items[i - 1][1])
        return map(calc, queries)


