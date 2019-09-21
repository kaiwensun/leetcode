# A brute force solution by counting elements can be even faster

import heapq
class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # ((head, rank_in_turn, row_number, index_in_row))
        heap = [(mat[r][0], 0, r, 0) for r in xrange(len(mat))]
        heapq.heapify(heap)
        curr, cnt = None, 0
        INF = 10001
        while True:
            top = heap[0]
            if top[0] == INF:
                return -1
            if curr == top[0]:
                cnt += 1
                if cnt == len(mat):
                    return curr
            else:
                cnt = 1
                curr = top[0]
            new_ele = (INF if top[3] + 1 == len(mat[top[2]]) else mat[top[2]][top[3] + 1], cnt, top[2], top[3] + 1)
            heapq.heapreplace(heap, new_ele)
