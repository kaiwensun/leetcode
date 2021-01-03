class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        res = 0
        for nb, unit in sorted(boxTypes, key=lambda (nb, unit):-unit):
            res += min(nb, truckSize) * unit
            truckSize -= nb
            if truckSize < 0:
                break
        return res

