import functools
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k != 0:
            return False
        s /= k
        if max(nums) > s:
            return False
        counter = collections.Counter(nums)
        fs = frozenset(counter.items())
        
        @functools.lru_cache(None)
        def dfs(wanted, fs):
            if wanted == 0:
                return len(fs) == 0 or dfs(s, fs)
            for n, cnt in sorted(list(fs), reverse=True):
                if wanted >= n:
                    new_fs = fs - set(((n, cnt),))
                    if cnt != 1:
                        new_fs |= set(((n, cnt - 1),))
                    if dfs(wanted - n, new_fs):
                        return True
            return False
        return dfs(s, fs)
