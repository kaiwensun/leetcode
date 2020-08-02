class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def countTrailingZero(row):
            cnt = 0
            for i in xrange(len(row) - 1, - 1, -1):
                if row[i] == 0:
                    cnt += 1
                else:
                    break
            return cnt

        n = len(grid[0])
        records = [countTrailingZero(row) for row in grid]
        res = 0
        for expected_size in xrange(n - 1, -1, -1):
            target_index = n - expected_size - 1
            for i in xrange(n):
                record = records[i]
                if record >= expected_size:
                    res += i - target_index
                    records[target_index + 1 : i + 1] = records[target_index : i]
                    records[target_index] = -1
                    break
            else:
                return -1
        return res

