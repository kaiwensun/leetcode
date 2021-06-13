class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        res = [-1, -1, -1]
        for triplet in triplets:
            for i in xrange(len(triplet)):
                if triplet[i] > target[i]:
                    break
            else:
                for i in xrange(len(triplet)):
                    res[i] = max(res[i], triplet[i])
        return res == target

