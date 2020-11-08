from collections import Counter
class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = Counter(s)
        last_num = None
        res = 0
        for k, v in cnt.most_common():
            if last_num is not None and cnt[last_num] <= v:
                diff = v - cnt[last_num] + 1 if cnt[last_num] > 0 else v
                cnt[k] -= diff
                res += diff
            last_num = k
        return res

