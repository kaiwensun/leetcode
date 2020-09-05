class Solution(object):
    def kEmptySlots(self, bulbs, K):
        """
        :type bulbs: List[int]
        :type K: int
        :rtype: int
        """
        size = K + 1
        buckets = [[float('inf'), float('-inf')] for _ in xrange((len(bulbs) - 1) // size + 1)]
        for i, posi in enumerate(bulbs):
            buck = (posi - 1) // size
            buckets[buck][0] = min(buckets[buck][0], posi)
            buckets[buck][1] = max(buckets[buck][1], posi)
            if buck != 0 and buckets[buck][0] == posi and posi - buckets[buck - 1][1] == size:
                return i + 1
            if buck != len(buckets) - 1 and buckets[buck][1] == posi and buckets[buck + 1][0] - posi == size:
                return i + 1
        return -1
