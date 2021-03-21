import heapq
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        buy, sell = [], []
        heaps = [buy, sell]
        for price, amount, is_sell in orders:
            sign = 1 if is_sell else -1
            heap = heaps[1 - is_sell]
            while amount and heap and -heap[0][0] >= sign * price:
                diff = min(heap[0][1], amount)
                amount -= diff
                heap[0][1] -= diff
                if heap[0][1] == 0:
                    heapq.heappop(heap)
            if amount != 0:
                heapq.heappush(heaps[is_sell], [sign * price, amount])
        res = 0
        for queue in buy, sell:
            for _, amount in queue:
                res += amount
                res %= MOD
        return res

