from collections import Counter
class Solution(object):
    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        h = Counter()
        prefix = [0]
        xor = 0
        for num in arr:
            xor ^= num
            prefix.append(xor)
        res = 0
        n = len(arr)
        for i in xrange(1, n):
            for j in xrange(i + 1, n + 1):
                for k in xrange(j, n + 1):
                    if prefix[j - 1] ^ prefix[i - 1] == prefix[k] ^ prefix[j - 1]:
                        res += 1
        return res
