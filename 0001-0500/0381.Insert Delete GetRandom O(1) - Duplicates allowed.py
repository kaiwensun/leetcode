class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._array = [] # [val, val, val, ...]
        self._val_to_index = {} # each k-v pair is val: set([index, index, index, ...])
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self._val_to_index.setdefault(val, set()).add(len(self._array))
        self._array.append(val)
        return len(self._val_to_index[val]) == 1
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        try:
            index = self._val_to_index[val].pop()
            if index == len(self._array) - 1:
                self._array.pop()
            else:
                trail = self._array.pop()
                trail_index = len(self._array)
                self._array[index] = trail
                self._val_to_index[trail].remove(trail_index)
                self._val_to_index[trail].add(index)
            return True
        except:
            return False            
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self._array)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
