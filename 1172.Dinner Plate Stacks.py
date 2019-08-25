class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._table = []
        self._available = []
        self._available_set = set()
        self._capacity = capacity
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self._available:
            index = self._available[0]
            self._table[index].append(val)
            if len(self._table[index]) == self._capacity:
                self.deregister_available(index)
        else:
            self._table.append([val])
            if self._capacity != 1:
                self.register_available(len(self._table) - 1)
        
        

    def pop(self):
        """
        :rtype: int
        """
        if not self._table:
            return -1
        res = self._table[-1].pop()
        self.register_available(len(self._table) - 1)
        while self._table and not self._table[-1]:
            self.deregister_available(len(self._table) - 1)
            self._table.pop()
        return res
            
        

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        if (index >= len(self._table)):
            return -1
        if index == len(self._table) - 1:
            return self.pop()
        if not self._table[index]:
            return -1
        res = self._table[index].pop()
        self.register_available(index)
        return res
    
    def register_available(self, index):
        if index not in self._available_set:
            bisect.insort_left(self._available, index)
            self._available_set.add(index)
        
    def deregister_available(self, index):
        if index in self._available_set:
            i = bisect.bisect_left(self._available, index)
            del self._available[i]
            self._available_set.remove(index)
