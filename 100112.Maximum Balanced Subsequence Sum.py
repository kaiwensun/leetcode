class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        n = len(nums)
        array = sorted((nums[i] - i, i) for i in range(len(nums)))

        seg_tree = [float("-inf")] * (n * 2)

        def find_max(left, right):
            left += n
            right += n
            mx = float("-inf")
            while left < right:
                if left % 2:
                    mx = max(mx, seg_tree[left])
                    left += 1
                if right % 2:
                    right -= 1
                    mx = max(mx, seg_tree[right])
                left //= 2
                right //= 2
            return mx

        def set_value(i, value):
            i += n
            while i:
                if seg_tree[i] >= value:
                    break
                seg_tree[i] = value
                i //= 2

        res = float("-inf")
        for j in range(len(array)):
            diff, i = array[j]
            mx = find_max(0, i)
            sm = max(mx, 0) + nums[i]
            set_value(i, sm)
            res = max(sm, res)
        return res

