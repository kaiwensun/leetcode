class Solution(object):
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        prefixes = set()
        res = set()
        for num in A:
            prefixes = {num | prefix for prefix in prefixes} | {num}
            res |= prefixes
        return len(res)
