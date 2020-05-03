# Dijkstra
import heapq
class Solution(object):
    
    def kthSmallest(self, mat, k):
        visited = {(0, ) * len(mat)}
        sm = sum(row[0] for row in mat)
        heap = [(sm, (0, ) * len(mat))]
        for i in xrange(k):
            item = heapq.heappop(heap)
            res = item[0]
            indexes = list(item[1])
            for j in xrange(len(mat)):
                if indexes[j] + 1 < len(mat[j]):
                    new_sm = res - mat[j][indexes[j]] + mat[j][indexes[j] + 1]
                    indexes[j] += 1
                    new_indexes = tuple(indexes)
                    if new_indexes not in visited:
                        visited.add(new_indexes)
                        heapq.heappush(heap, (new_sm, tuple(new_indexes)))
                    indexes[j] -= 1
        return res
