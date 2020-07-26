from collections import Counter
class Solution(object):
    def canReorderDoubled(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        counter = Counter(A)
        for n in counter.keys():
            if not self.dfs_lookdown(counter, n):
                return False
        return True
            
    def dfs_lookdown(self, counter, n):
        if counter[n] == 0:
            return True
        if n == 0:
            if counter[0] % 2:
                return False
            counter[0] = 0
            return True
        else:
            if n % 2:
                return self.dfs_lookup(counter, n)
            else:
                possible = self.dfs_lookdown(counter, n / 2)
                if not possible:
                    return False
                return self.dfs_lookup(counter, n)

    def dfs_lookup(self, counter, n):
        if counter[n] == 0:
            if counter[n * 2]:
                return self.dfs_lookup(counter, n * 2)
            return True
        else:
            if counter[n * 2] < counter[n]:
                return False
            else:
                counter[n * 2] -= counter[n]
                counter[n] = 0
                return self.dfs_lookup(counter, n * 2)
