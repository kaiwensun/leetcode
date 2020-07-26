class Solution(object):
    def dietPlanPerformance(self, calories, k, lower, upper):
        """
        :type calories: List[int]
        :type k: int
        :type lower: int
        :type upper: int
        :rtype: int
        """
        point = 0
        calories.append(0)
        s = sum(calories[:k])
        for i in xrange(k, len(calories)):
            if s < lower:
                point -= 1
            elif s > upper:
                point += 1
            s -= calories[i - k]
            s += calories[i]
        return point
