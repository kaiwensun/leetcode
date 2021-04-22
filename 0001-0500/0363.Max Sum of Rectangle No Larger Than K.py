from sortedcontainers import SortedSet

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = float("-inf")
        for row_start in range(m):
            prefix_sum = [0] * n
            for row_end in range(row_start, m):
                row_prefix_sum = 0
                for col in range(n):
                    row_prefix_sum += matrix[row_end][col]
                    prefix_sum[col] += row_prefix_sum
                seen = SortedSet([0])
                for num in prefix_sum:
                    index = seen.bisect_right(num - k - 1)
                    if index < len(seen):
                        res = max(res, num - seen[index])
                    seen.add(num)
        return res

