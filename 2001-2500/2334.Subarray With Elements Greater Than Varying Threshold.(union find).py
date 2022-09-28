class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        size = [1] * len(nums)
        data = list(range(len(nums)))

        def find(x):
            if data[x] != x:
                data[x] = find(data[x])
            return data[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                data[rx] = ry
                size[ry] += size[rx]

        for i, num in sorted(enumerate(nums), key=lambda item: list(reversed(item)), reverse=True):
            if i - 1 >= 0 and nums[i - 1] >= num:
                union(i, i - 1)
            if i + 1 < len(nums) and nums[i + 1] >= num:
                union(i, i + 1)
            if (threshold < num * size[find(i)]):
                return size[find(i)]
        return -1

