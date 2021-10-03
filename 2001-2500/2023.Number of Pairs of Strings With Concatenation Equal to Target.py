from collections import Counter

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        prefix = Counter()
        suffix = Counter()
        res = 0
        for num in nums:
            if len(num) < len(target):
                is_pre = is_suf = False
                if target.startswith(num):
                    is_pre = True
                    prefix[len(num)] += 1
                if target.endswith(num):
                    is_suf = True
                    suffix[len(num)] += 1
                if len(num) << 1 == len(target) and is_pre and is_suf:
                    res -= 1
        for pre, pre_cnt in prefix.items():
            res += suffix[len(target) - pre] * pre_cnt
        return res

