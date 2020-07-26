import functools, collections
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        def calc_compressed_size(cnt):
            return 1 if cnt == 1 else len(str(cnt)) + 1
        
        # s[0..i], delete at most k char, what's the minimum length of encoding?
        @functools.lru_cache(None)
        def dp(i, k):
            if k < 0:
                return float('inf')
            if i < 0:
                return 0
            if k > i:
                return 0
            if k == i:
                return 1
            same = count_same(i)
            this_size = calc_compressed_size(same)
            res = dp(i - same, k) + this_size  # if I do not delete any trailing s[i]
            
            # if I delete certain number of the trailing s[i]
            for deleted in range(1, k + 1):
                if deleted > k:
                    break
                new_end = i - deleted
                res = min(res, dp(new_end, k - deleted))
            deleted_diff = 0
            kept_same = 1
            
            # if I delete certain number of the non s[i] letters in the middle
            for new_end in range(i - 1, -1, -1):
                if s[new_end] == s[i]:
                    kept_same += 1
                else:
                    res = min(res, dp(new_end, k - deleted_diff) + calc_compressed_size(kept_same))
                    deleted_diff += 1
                    if deleted_diff > k:
                        break
            else:
                res = min(res, calc_compressed_size(kept_same - (k - deleted_diff)))
            return res

        @functools.lru_cache(None)
        def count_same(i):
            if i < 0:
                return 0
            if i == 0:
                return 1
            if s[i] == s[i - 1]:
                return 1 + count_same(i - 1)
            return 1
        
        return dp(len(s) - 1, k)