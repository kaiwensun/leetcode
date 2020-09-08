from collections import Counter
class FreqStack(object):

    def __init__(self):
        self.counter = {}
        self.elements = [set() for _ in xrange(10000)]
        self.orders = [[] for _ in xrange(10000)]
        self.most_freq = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.counter.setdefault(x, 0)
        if self.counter[x] != 0:
            self.elements[self.counter[x]].remove(x)
        self.counter[x] += 1
        self.elements[self.counter[x]].add(x)
        self.orders[self.counter[x]].append(x)
        self.most_freq = max(self.most_freq, self.counter[x])
        
    def pop(self):
        """
        :rtype: int
        """
        while not self.elements[self.most_freq]:
            self.most_freq -= 1
        while self.orders[self.most_freq][-1] not in self.elements[self.most_freq]:
            self.orders[self.most_freq].pop()
        x = self.orders[self.most_freq].pop()
        self.elements[self.most_freq].remove(x)
        self.counter[x] -= 1
        if self.counter[x] != 0:
            self.elements[self.counter[x]].add(x)
        return x
        
        
        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()

