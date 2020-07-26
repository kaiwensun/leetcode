class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefixes = [0] * (len(arr) + 1)
        for i in xrange(len(arr)):
            prefixes[i + 1] = prefixes[i] ^ arr[i]
        return [prefixes[r + 1] ^ prefixes[l] for l, r in queries]
