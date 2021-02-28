import bisect
class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        toppingCostSet = {0}
        for toppingCost in toppingCosts:
            for cost in list(toppingCostSet):
                toppingCostSet |= {cost + toppingCost, cost + 2 * toppingCost}
        toppingCostList = sorted(toppingCostSet)
        toppingCostList = [-float("inf")] + toppingCostList + [float("inf")]
        res = float("inf")
        for baseCost in baseCosts:
            i = bisect.bisect(toppingCostList, target - baseCost)
            for j in i, i - 1:
                if abs(baseCost + toppingCostList[j] - target) < abs(res - target):
                    res = baseCost + toppingCostList[j]
                elif abs(baseCost + toppingCostList[j] - target) == abs(res - target):
                    res = min(res, baseCost + toppingCostList[j])
        return res

