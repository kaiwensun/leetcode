class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        candies.sort(reverse=True)

        def can_allocate(each):
            kids = k
            for candy in candies:
                kids -= candy // each
                if kids <= 0:
                    return True
            return False

        l = 1
        r = candies[0] + 1
        while l < r:
            mid = (l + r) // 2
            if can_allocate(mid):
                l = mid + 1
            else:
                r = mid
        return l - 1

