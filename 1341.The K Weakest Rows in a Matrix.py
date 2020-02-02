class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        return [ele[1] for ele in sorted((sum(row), index) for index, row in enumerate(mat))[:k]]
        
