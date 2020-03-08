from collections import Counter
class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = Counter(s)
        keys = sorted(cnt.keys())
        res = []
        index = 0
        delta = 1
        def nextC():
            index = 0
            delta = 1
            step = 0
            while step < len(s):
                if not (0 <= index < len(keys)):
                    delta *= -1
                    index += delta
                if cnt[keys[index]]:
                    cnt[keys[index]] -= 1
                    step += 1
                    yield keys[index]
                index += delta       
        return ''.join(nextC())
