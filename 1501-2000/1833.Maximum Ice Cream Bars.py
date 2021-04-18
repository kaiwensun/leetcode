class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        res = 0
        for cost in costs:
            if coins < cost:
                break
            res += 1
            coins -= cost
        return res

