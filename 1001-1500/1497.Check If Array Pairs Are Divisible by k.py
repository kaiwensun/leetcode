import collections
class Solution:
    def canArrange(self, nums: List[int], k: int) -> bool:
        counter = collections.Counter([num % k for num in nums])
        res = 0
        for i in range(1, (k + 1) // 2):
            if counter[i] != counter[k - i]:
                return False
        if counter[0] % 2 == 1:
            return False
        if k % 2 == 0:
            if counter[k // 2] % 2 == 1:
                return False
        return True
