from collections import defaultdict

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        seg = nums + nums
        n = len(nums)
        for i in range(n - 1, -1, -1):
            seg[i] = seg[i * 2] & seg[i * 2 + 1]

        def lookup(start, end):
            if start >= end:
                return float("inf")
            start += n
            end += n
            res = seg[start]
            while start < end and start != 0:
                if start % 2 == 1:
                    res &= seg[start]
                    start += 1
                if end % 2 == 1:
                    end -= 1
                    res &= seg[end]
                start >>= 1
                end >>= 1
            return res

        prev_0_posi = defaultdict(list)
        for i in range(32):
            mask = 1 << i
            prev = -1
            for posi, num in enumerate(nums):
                num = mask & num
                prev_0_posi[mask].append(prev)
                if num == 0:
                    prev = posi

        res = float("inf")
        for i, num in enumerate(nums):
            res = min(res, abs(num - k))
            lefts = {arr[i] for arr in prev_0_posi.values()}
            lefts.add(i)
            for left in lefts:
                if left == -1:
                    continue
                val = lookup(left, i + 1)
                res = min(res, abs(val - k))
        return res

