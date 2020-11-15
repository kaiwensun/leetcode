class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.arr = [None] * n
        self.ptr = 0
        

    def insert(self, id, value):
        """
        :type id: int
        :type value: str
        :rtype: List[str]
        """
        self.arr[id - 1] = value
        res = []
        while self.ptr < len(self.arr) and self.arr[self.ptr] is not None:
            res.append(self.arr[self.ptr])
            self.ptr += 1
        return res
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)

