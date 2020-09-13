import heapq
from collections import deque, defaultdict
class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_index = 0
        value_based_heap = []  # can be optimized without using heap
        index_based_heap = []
        taken_indexes = [False] * len(s) # index in s
        t_index = 0
        while t_index < len(t):
            assert(s_index == len(s) or not taken_indexes[s_index])
            while index_based_heap and taken_indexes[index_based_heap[0]]:
                heapq.heappop(index_based_heap)
            while value_based_heap and taken_indexes[value_based_heap[0][1]]:
                heapq.heappop(value_based_heap)
            if value_based_heap and t[t_index] == value_based_heap[0][0]:
                v, i = heapq.heappop(value_based_heap)
                assert(not taken_indexes[i])
                taken_indexes[i] = True
                t_index += 1
            elif index_based_heap and t[t_index] == s[index_based_heap[0]]:
                i = heapq.heappop(index_based_heap)
                assert(not taken_indexes[i])
                taken_indexes[i] = True
                t_index += 1
            elif s_index < len(s):
                heapq.heappush(value_based_heap, (s[s_index], s_index))
                heapq.heappush(index_based_heap, s_index)
                s_index += 1
            else:
                return False
        return True

