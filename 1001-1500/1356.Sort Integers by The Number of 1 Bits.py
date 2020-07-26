class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def count1(a):
            cnt = 0
            while a:
                cnt += 1
                a &= a - 1
            return cnt
        def cmp(a, b):
            c1 = count1(a)
            c2 = count1(b)
            return c1 - c2 or a - b
        return sorted(arr, cmp=cmp)
            
        
