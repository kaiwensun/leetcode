from collections import Counter
class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) % k != 0:
            return False
        seq_cnt = 0
        cnt = Counter(nums)
        keys = sorted(cnt.keys())
        while keys:
            key = keys.pop()
            value = cnt[key]
            if value == 0:
                continue
            for i in xrange(k):
                cnt[key - i] -= value
                if cnt[key - i] < 0:
                    return False
        return True
