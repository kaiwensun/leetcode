class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        prevSteps = {posi: set() for posi in stones}
        prevSteps[0].add(0)
        for posi in stones:
            for prevStep in prevSteps[posi]:
                for diff in (-1, 0, 1):
                    nextStep = prevStep + diff
                    nextPosi = posi + nextStep
                    if nextPosi == stones[-1]:
                        return True
                    if posi < nextPosi and nextPosi in prevSteps:
                        prevSteps[nextPosi].add(nextStep)
        return False
