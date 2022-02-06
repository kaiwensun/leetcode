from collections import Counter

class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        elif num < 0:
            return -int(''.join(sorted(str(num)[1:], reverse=True)))
        else:
            cnt = Counter(str(num))
            res = []
            for i in range(1, 10):
                if cnt[str(i)]:
                    cnt[str(i)] -= 1
                    res.append(str(i))
                    break
            for i in range(0, 10):
                res.append(str(i) * cnt[str(i)])
            return int("".join(res))


