class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        seg_tree = [0] * (2 * n)
        def update_seg(start, end, value):
            left = start + n
            right = end + n
            while left < right:
                if left % 2:
                    seg_tree[left] += value
                    left += 1
                if right % 2:
                    right -= 1
                    seg_tree[right] += value
                left /= 2
                right /= 2
        def query(i):
            res, i = 0, i + n
            while i:
                res += seg_tree[i]
                i /= 2
            return res
        for start, end, value in bookings:
            update_seg(start - 1, end, value)
        return [query(i) for i in xrange(n)]
