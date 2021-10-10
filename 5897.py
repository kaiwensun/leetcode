class Solution:
    def minimumDifference(self, nums: List[int]) -> int:

        def sumset(start, end):
            acc = defaultdict(set)
            def dfs(i, cnt, sm):
                if i == end:
                    acc[cnt].add(sm)
                    return
                dfs(i + 1, cnt, sm)
                dfs(i + 1, cnt + 1, sm + nums[i])
            
            dfs(start, 0, 0)
            return acc

        n = len(nums) // 2
        lsumsets = sumset(0, n)
        rsumsets = sumset(n, len(nums))
        rsumsets = {key: sorted(value) for key, value in rsumsets.items()}
        res = float("inf")
        lhalf = sum(nums[:n])
        rhalf = sum(nums[n:])
        rh_minus_lh = rhalf - lhalf
        half_of_rh_minus_lh = rh_minus_lh / 2
        for lsize, lsumset in lsumsets.items():
            rsumset = rsumsets[lsize]
            for lsum in lsumset:
                # Define: ~ means "wants to be as close as possible to"
                # sum of selected n values   ~    sum of unselected n values
                # lsum + (rhalf - value)   ~   rsum + (lhalf - lsum)
                # so, rsum   ~   lsum + (rhalf - lhalf) / 2
                # so, binary selecting rsum from rsumset
                i = bisect.bisect(rsumset, lsum + half_of_rh_minus_lh)
                if i != len(rsumset):
                    res = min(res, abs((lsum - rsumset[i]) * 2 + rh_minus_lh))
                if i != 0:
                    res = min(res, abs((lsum - rsumset[i - 1]) * 2 + rh_minus_lh))
        return res

