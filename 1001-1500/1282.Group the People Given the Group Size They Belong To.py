class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for size, p in sorted((size, p) for p, size in enumerate(groupSizes)):
            res[-1].append(p)
            if len(res[-1]) == size:
                res.append([])
        return res[:-1]

# comment: order is not that important. try bucket sort (in essence, grouping), to decrease complexity from O(n log n) to O(n).
