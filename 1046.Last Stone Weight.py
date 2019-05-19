import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        pairs = [(-s, s) for s in stones]
        heapq.heapify(pairs)
        rem = 0
        while len(pairs) > 1:
            _, s1 = heapq.heappop(pairs)
            _, s2 = heapq.heappop(pairs)
            diff = abs(s1 - s2)
            if diff: 
                heapq.heappush(pairs, (-diff, diff))
        return pairs[0][1] if pairs else 0
