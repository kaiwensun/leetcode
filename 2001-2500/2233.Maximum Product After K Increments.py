from collections import Counter

MOD = 10 ** 9 + 7

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        cnt[max(nums) + 1] = 0
        keys = sorted(cnt.keys())
        cnt[float("inf")] = 0
        i = 0
        while k:
            key = keys[i]
            if i < len(keys) - 1:
                next_key = keys[i + 1]
            else:
                next_key = key + k
            i += 1
            diff = next_key - key
            total_diff = diff * cnt[key]
            if total_diff <= k:
                k -= total_diff
                cnt[next_key] += cnt[key]
                del cnt[key]
            else:
                this_cnt = cnt[key]
                each_bump = k // this_cnt
                additional_cnt = k % this_cnt
                if each_bump:
                    cnt[key + each_bump] += this_cnt
                    del cnt[key]
                cnt[key + each_bump + 1] += additional_cnt
                cnt[key + each_bump] -= additional_cnt
                
                k = 0
            if k == 0 or i == len(keys):
                break
        del cnt[float("inf")]
        res = 1
        for key, value in cnt.items():
            if value:
                res *= pow(key, value, MOD)
                res %= MOD
        return res

