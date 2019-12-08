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
