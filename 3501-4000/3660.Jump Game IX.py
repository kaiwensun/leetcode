from collections import defaultdict

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        smallest_right_to = list(nums)
        for i in range(n - 2, -1, -1):
            smallest_right_to[i] = min(smallest_right_to[i], smallest_right_to[i + 1])

        uf_data = list(range(n))
        def find(x):
            if uf_data[x] != x:
                uf_data[x] = find(uf_data[x])
            return uf_data[x]
        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx != ry:
                uf_data[rx] = ry

        biggest_index = 0
        for i, num in enumerate(nums):
            biggest = nums[biggest_index]
            if biggest <= num:
                if i + 1 < n and smallest_right_to[i + 1] < biggest:
                    union(biggest_index, i)
                biggest_index = i
            else:
                union(biggest_index, i)

        biggest_values = defaultdict(int)
        for i in range(n):
            root = find(i)
            biggest_values[root] = max(biggest_values[root], nums[i])

        return [
            biggest_values[find(i)] for i in range(n)
        ]

