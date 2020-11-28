class RLEIterator(object):

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.A_pointer = 0
        self.curr_consumed_cnt = 0
        

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n > 0 and self.A_pointer < len(self.A):
            remaining = self.A[self.A_pointer] - self.curr_consumed_cnt
            diff = min(remaining, n)
            n -= diff
            self.curr_consumed_cnt += diff
            if n == 0:
                return self.A[self.A_pointer + 1]
            else:
                self.curr_consumed_cnt = 0
                self.A_pointer += 2
        return -1

        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
