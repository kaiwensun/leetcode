class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self._stack = []
        self._maxSize = maxSize
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self._stack) < self._maxSize:
            self._stack.append([x, 0])
        

    def pop(self):
        """
        :rtype: int
        """
        if self._stack:
            ele = self._stack.pop()
            if self._stack:
                self._stack[-1][1] += ele[1]
            return sum(ele)
        else:
            return -1
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        if len(self._stack):
            index = min(k, len(self._stack)) - 1
            self._stack[index][1] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
