from collections import Counter
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        cnt = Counter(arr)
        half = 0
        uniq = 0
        for val in sorted(cnt.values(), reverse=True):
            uniq += 1
            half += val
            if half >= (len(arr) + 1) // 2:
                break
        return uniq
