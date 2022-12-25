class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        if price[0] == price[-1]:
            return 0

        def can_form_basket(diff):
            prev = price[0]
            cnt = 1
            for p in price:
                if p >= prev + diff:
                    prev = p
                    cnt += 1
                    if cnt == k:
                        return True
            return False
        l = 1
        r = price[-1] - price[0] + 1
        while l < r:
            mid = (l + r) // 2
            if can_form_basket(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1

