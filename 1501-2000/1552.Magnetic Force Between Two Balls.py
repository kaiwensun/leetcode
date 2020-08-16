class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """
        def can_fit(min_diff):
            last = float('-inf')
            fitted = 0
            for posi in position:
                if posi - last >= min_diff:
                    fitted += 1
                    last = posi
                    if fitted >= m:
                        return True
            return False

        position.sort()
        l, r = 1, position[-1] - position[0] + 1
        while l < r:
            mid = (l + r) // 2
            if can_fit(mid):
                l = mid + 1
            else:
                r = mid
        return l if can_fit(l) else l - 1

