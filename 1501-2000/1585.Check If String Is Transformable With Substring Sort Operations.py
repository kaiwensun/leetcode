import heapq
from collections import deque, defaultdict
class Solution(object):
    def isTransformable(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index_based_queue_l = index_based_queue_r = 0
        value_based_queue = []
        taken_indexes = [False] * len(s) # index in s
        t_index = 0
        while t_index < len(t):
            assert(index_based_queue_r == len(s) or not taken_indexes[index_based_queue_r])
            while index_based_queue_l < index_based_queue_r and taken_indexes[index_based_queue_l]:
                index_based_queue_l += 1
            while value_based_queue and taken_indexes[value_based_queue[0][1]]:
                heapq.heappop(value_based_queue)
            if value_based_queue and t[t_index] == value_based_queue[0][0]:
                v, i = heapq.heappop(value_based_queue)
                assert(not taken_indexes[i])
                taken_indexes[i] = True
                t_index += 1
            elif index_based_queue_l < index_based_queue_r and t[t_index] == s[index_based_queue_l]:
                assert(not taken_indexes[index_based_queue_l])
                taken_indexes[index_based_queue_l] = True
                t_index += 1
                index_based_queue_l += 1
            elif index_based_queue_r < len(s):
                heapq.heappush(value_based_queue, (s[index_based_queue_r], index_based_queue_r))
                index_based_queue_r += 1
            else:
                return False
        return True

