import math
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        def get_num(row, index):
            mx = (1 << row) - 1
            if row % 2:
                return (mx >> 1) + 1 + index
            else:
                return mx - index
        def get_coordinate(num):
            mask = num
            for i in xrange(1, 6):
                mask |= mask >> i
            mx = mask
            row = 1
            while mask != 1:
                row += 1
                mask >>= 1
            if row % 2:
                index = label - ((mx >> 1) + 1)
            else:
                index = mx - label
            return row, index
        row, index = get_coordinate(label)
        res = [get_num(row, index)]
        while res[-1] != 1:
            row -= 1
            index //= 2
            res.append(get_num(row, index))
        return reversed(res)
