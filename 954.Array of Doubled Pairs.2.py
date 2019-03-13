from collections import Counter
class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        counter = Counter(A)
        if counter[0] % 2:
            return False
        counter[0] = 0
        for n in counter.keys():
            if counter[n] == 0:
                continue
            k = n
            while k % 2 == 0 and counter[k / 2]:
                k /= 2
            while counter[k]:
                if counter[k] > counter[k * 2]:
                    return False
                counter[k * 2] -= counter[k]
                counter[k] = 0
                k *= 2
                if not counter[k]:
                    k *= 2
        return True
