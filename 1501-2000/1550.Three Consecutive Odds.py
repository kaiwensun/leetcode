class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        cnt = 0
        for a in arr:
            if a % 2 == 1:
                cnt += 1
            else:
                cnt = 0
            if cnt == 3:
                return True
        return False
