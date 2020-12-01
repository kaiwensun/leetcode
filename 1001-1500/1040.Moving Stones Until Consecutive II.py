class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        stones.sort()
        mx = max(stones[-1] - stones[1], stones[-2] - stones[0]) - len(stones) + 2
        i = j = size = 0
        if stones[-1] - stones[0] <= len(stones):
            mn = stones[-1] - stones[0] - len(stones) + 1
        elif (stones[-1] - stones[1] == len(stones) - 2 and stones[1] - stones[0] > 2) or (stones[-2] - stones[0] == len(stones) - 2 and stones[-1] - stones[-2] > 2):
            mn = 2
        else:
            while j < len(stones):
                while j < len(stones) and stones[j] - stones[i] < len(stones):
                    size = max(size, j - i + 1)
                    j += 1
                i += 1
            mn = len(stones) - size
        return mn, mx

