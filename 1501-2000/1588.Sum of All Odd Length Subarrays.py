class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        for i, num in enumerate(arr):
            even_start = i // 2 + 1
            even_end = (len(arr) - 1) // 2 + 1 - even_start + ((i + 1) % 2)
            odd_start = (i + 1) // 2
            odd_end = len(arr) // 2 - odd_start + i % 2
            res += (even_start * even_end + odd_start * odd_end) * num
        return res

