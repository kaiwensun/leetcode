class Solution(object):
    def minMoves(self, target, maxDoubles):
        """
        :type target: int
        :type maxDoubles: int
        :rtype: int
        """
        def find_bit_size(target):
            res = 0
            while target:
                target >>= 1
                res += 1
            return res

        target_size = find_bit_size(target)
        if maxDoubles + 1 >= target_size:
            return target_size + bin(target).count('1') - 2
        inc_first_bstr = bin(target)[:- maxDoubles] if maxDoubles else bin(target)
        heading = int(inc_first_bstr, 2)
        return heading + maxDoubles + bin(target - (heading << maxDoubles)).count('1') - 1

