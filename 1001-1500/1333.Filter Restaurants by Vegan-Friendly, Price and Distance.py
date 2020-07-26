class Solution(object):
    def filterRestaurants(self, res, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        return [r[0] for r in sorted([r for r in res if r[3] <= maxPrice and r[4] <= maxDistance and (not veganFriendly or r[2])], cmp=lambda a, b: cmp(-a[1], -b[1]) or cmp(-a[0], -b[0]))]
