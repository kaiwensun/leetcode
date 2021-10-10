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
        sm = sum(nums)
        for lsize, lsumset in lsumsets.items():
            rsumset = rsumsets[n - lsize]
            for lsum in lsumset:
                i = bisect.bisect(rsumset, sm / 2 - lsum)
                if i != len(rsumset):
                    res = min(res, abs(sm - lsum - rsumset[i] - lsum - rsumset[i]))
                if i != 0:
                    res = min(res, abs(sm - lsum - rsumset[i - 1] - lsum - rsumset[i - 1]))
        return res

