class StockSpanner(object):

    def __init__(self):
        self._stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        cnt = 1
        while self._stack and self._stack[-1][0] <= price:
            cnt += self._stack.pop()[1]
        self._stack.append((price, cnt))
        return cnt


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
