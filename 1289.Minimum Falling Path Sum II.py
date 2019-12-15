class Path:
    def __init__(self, index, val):
        self.index = index
        self.val = val

class Solution(object):
    def minFallingPathSum(self, arr):
        """
        :type arr: List[List[int]]
        :rtype: int
        """
        
        def find_min_2(row):
            mins = [Path(-1, float('inf'))] * 2
            for i, num in enumerate(row):
                if num < mins[1].val:
                    mins[1] = Path(i, num)
                if mins[1].val < mins[0].val:
                    mins[0], mins[1] = mins[1], mins[0]
            return mins
        prev = [Path(-1, 0)] * 2
        for row in arr:
            curr = find_min_2(row)
            curr[0].val += prev[1].val if curr[0].index == prev[0].index else prev[0].val
            curr[1].val += prev[1].val if curr[1].index == prev[0].index else prev[0].val
            if curr[0].val > curr[1].val:
                curr[0], curr[1] = curr[1], curr[0]
            prev = curr
        return prev[0].val
