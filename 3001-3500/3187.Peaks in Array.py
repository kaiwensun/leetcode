class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        seg_tree = [0] * (n * 2)
        def update_peak(i, delta):
            i += n
            while i:
                seg_tree[i] += delta
                i //= 2
        def count_peak(l, r):
            l += n
            r += n
            res = 0
            while l < r:
                if l % 2:
                    res += seg_tree[l]
                    l += 1
                if r % 2:
                    r -= 1
                    res += seg_tree[r]
                l //= 2
                r //= 2
            return res
        def is_peak(i):
            return 0 < i < n - 1 and nums[i - 1] < nums[i] > nums[i + 1]
        for i in range(n):
            if is_peak(i):
                update_peak(i, 1)
        res = []
        for op, a, b in queries:
            if op == 1:
                res.append(count_peak(a + 1, b))
            else:
                old_is_peaks = [is_peak(i) for i in range(a - 1, a + 2)]
                nums[a] = b
                new_is_peaks = [is_peak(i) for i in range(a - 1, a + 2)]
                for j in range(3):
                    if old_is_peaks[j] and not new_is_peaks[j]:
                        update_peak(a + j - 1, -1)
                    elif not old_is_peaks[j] and new_is_peaks[j]:
                        update_peak(a + j - 1, 1)
        return res

