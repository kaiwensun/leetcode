class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        ranked = sorted((-score, id) for id, score in enumerate(nums))
        rval = [None] * len(nums)
        for rank, e in enumerate(ranked):
            print rank
            if rank == 0:
                award = "Gold Medal"
            elif rank == 1:
                award = "Silver Medal"
            elif rank == 2:
                award = "Bronze Medal"
            else:
                award = str(rank + 1)
            rval[e[1]] = award
        return rval
