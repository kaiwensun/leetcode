class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        diff = sorted(map(sum, zip(aliceValues, bobValues)), reverse=True)
        if len(diff):
            diff.append(0)
        aliceScore = sum(aliceValues)
        bobScore = sum(bobValues)
        for i in xrange(0, len(aliceValues), 2):
            aliceScore += diff[i]
            bobScore += diff[i + 1]
        return cmp(aliceScore, bobScore)

