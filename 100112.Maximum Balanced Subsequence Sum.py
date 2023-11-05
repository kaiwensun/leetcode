class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        res = float("-inf")
        n = len(nums)
        heap = []
        array = sorted((nums[i] - i, i) for i in range(len(nums)))

        segTree = [float("-inf")] * (n * 2)

        def find_max(left, right):
            left += n
            right += n
            mx = float("-inf")
            while left < right:
                if left % 2:
                    mx = max(mx, segTree[left])
                    left += 1
                if right % 2:
                    right -= 1
                    mx = max(mx, segTree[right])
                left //= 2
                right //= 2
            return mx

        def set_value(i, value):
            i += n
            while i:
                if segTree[i] >= value:
                    break
                segTree[i] = value
                i //= 2

        res = float("-inf")
        for j in range(len(array)):
            diff, i = array[j]
            mx = find_max(0, i)
            sm = max(mx, 0) + nums[i]
            set_value(i, sm)
            res = max(sm, res)
        return res

