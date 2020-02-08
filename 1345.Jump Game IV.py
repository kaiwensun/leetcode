import collections, itertools 
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        h2i = collections.defaultdict(list)
        for i, h in enumerate(arr):
            h2i[h].append(i)
        data = [None] * len(arr)
        data[-1] = 0
        queue = collections.deque((len(arr) - 1,))
        while queue and data[0] is None:
            i = queue.popleft()
            for j in itertools.chain([i - 1, i + 1], h2i[arr[i]]):
                if 0 <= j < len(arr) and j != i and data[j] is None:
                    data[j] = data[i] + 1
                    queue.append(j)
        return data[0]
