class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort()
        res = len(stockPrices) - 1
        prev_k = float("inf")
        for i in range(1, len(stockPrices) - 1):
            x1, y1 = stockPrices[i - 1]
            x2, y2 = stockPrices[i]
            x3, y3 = stockPrices[i + 1]
            if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
                res -= 1
        return res

