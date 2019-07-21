class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        dominoes = sorted(map(sorted, dominoes))
        res = 0
        i = 0
        while i < len(dominoes):
            j = i + 1
            while j < len(dominoes):
                if dominoes[i] != dominoes[j]:
                    break
                j += 1
            res += (j - i) * (j - i - 1) // 2
            i = j
        return res
