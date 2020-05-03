import heapq
class Solution(object):
    
    def kthSmallest(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: int
        """
        visited = set()
        def gen(indexes, sm):
            if indexes in visited:
                while True:
                    yield float('inf')
            visited.add(indexes)
            yield sm
            heap = []
            for row_index in xrange(len(mat)):
                if indexes[row_index] + 1 < len(mat[row_index]):
                    new_indexes = list(indexes)
                    new_indexes[row_index] += 1
                    new_indexes = tuple(new_indexes)
                    new_sm = sm + mat[row_index][indexes[row_index] + 1] - mat[row_index][indexes[row_index]]
                    heap.append([None, gen(new_indexes, new_sm), new_indexes])
                    heap[-1][0] = next(heap[-1][1])
            while not heap:
                yield float('inf')
            heapq.heapify(heap)
            while True:
                yield heap[0][0]
                heapq.heapreplace(heap, [next(heap[0][1]), heap[0][1]])
        res = sum(row[0] for row in mat)
        main_gen = gen((0, ) * len(mat), res)
        for i in xrange(k):
            res = next(main_gen)
        return res
