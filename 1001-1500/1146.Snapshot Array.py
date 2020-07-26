class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self._tmp = {}
        self._snap_id = 0
        self._array = [[] for _ in xrange(length)]

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self._tmp[index] = val
        
        

    def snap(self):
        """
        :rtype: int
        """
        for index, value in self._tmp.iteritems():
            self._array[index].append((self._snap_id, value))
        self._tmp.clear()
        self._snap_id += 1
        return self._snap_id - 1
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        # if not self._array[index]:
        #     return 0
        snap_index = bisect.bisect_left(self._array[index], (snap_id, float('inf')))
        return snap_index and self._array[index][snap_index - 1][1]
        
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
