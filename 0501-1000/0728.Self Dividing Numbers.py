import bisect
table = []
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self_dividing(num):
            d = num
            while d:
                if d % 10 == 0 or num % (d % 10):
                    return False
                d /= 10
            return True

        def fill_table():
            table.extend(i for i in xrange(1, 10001) if is_self_dividing(i))

        if not table:
            fill_table()
        lindex = bisect.bisect_left(table, left)
        rindex = bisect.bisect_right(table, right)
        return table[lindex:rindex]
