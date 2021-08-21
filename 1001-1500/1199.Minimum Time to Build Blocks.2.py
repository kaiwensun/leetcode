# spliting a worker to work on two blocks is equivilant to merging the two blocks into one block of `split + max(block1, block2)`
class Solution(object):
    def minBuildTime(self, blocks, split):
        """
        :type blocks: List[int]
        :type split: int
        :rtype: int
        """
        heapq.heapify(blocks)
        while len(blocks) != 1:
            heapq.heappush(blocks, max(heapq.heappop(blocks), heapq.heappop(blocks)) + split)
        return blocks[0]

