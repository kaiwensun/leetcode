from collections import defaultdict
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        
        def findMaxXor(trie, num):
            res = 0
            for shift in xrange(30, -1, -1):
                res <<= 1
                bit = num >> shift & 1
                if 1 - bit in trie:
                    res |= 1
                    trie = trie[1 - bit]
                else:
                    trie = trie[bit]
            return res

        def insert(trie, num):
            for shift in xrange(30, -1, -1):
                trie = trie[num >> shift & 1]

        for num in nums:
            res = max(res, findMaxXor(trie, num))
            insert(trie, num)
        return res

