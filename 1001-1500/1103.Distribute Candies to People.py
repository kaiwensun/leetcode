class Solution(object):
    def distributeCandies(self, candies, n):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = [0] * n
        base = (1 + n) * n / 2
        total = 0
        turns = 0
        i = 1
        while total + base < candies:
            total += base
            base += n * n
            turns += 1
            i += 1
        if turns:
            for i in xrange(len(res)):
                res[i] = turns * (i + 1) + n * (turns - 1) * turns / 2
        k = turns * n
        i = 0
        distributed = sum(res)
        while distributed < candies:
            k += 1
            res[i] += min(k, candies - distributed)
            distributed += k
            i += 1
        return res
