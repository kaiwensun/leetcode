class Solution(object):
    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        self.capicity_cache = {}
        prefixes = self.getPrefixes(weights)
        max_weight = max(weights)
        minimum = max(max_weight, int(math.ceil(prefixes[-1] / D)))
        maximum = min(prefixes[-1], int(math.ceil(prefixes[-1] / D)) + max_weight)
        return self.binary_search_on_capicity(minimum, maximum + 1, weights, prefixes, D)
    log (max(sum(weights) / D, max_weight)) * log (N)

        
    def getPrefixes(self, weights):
        rval = [weights[0]] * len(weights)
        for i in xrange(1, len(weights)):
            rval[i] = rval[i - 1] + weights[i]
        return rval

    def binary_search_on_capicity(self, left, right, weights, prefixes, D):
        while left < right:
            mid = (left + right) / 2
            if self.capicity_works(mid, prefixes, weights, D):
                right = mid
            else:
                left = mid + 1
        return left

    def capicity_works(self, capicity, prefixes, weights, D):
        if capicity in self.capicity_cache:
            return self.capicity_cache[capicity]
        left = 0
        right = len(weights)
        target = capicity
        for i in xrange(D):
            index = bisect.bisect_right(prefixes, target, left, right)
            if index == left != right:
                self.capicity_cache[capicity] = False
                return False
            if left == right:
                self.capicity_cache[capicity] = True
                return True
            left = index
            target = prefixes[index - 1] + capicity
        self.capicity_cache[capicity] = target - capicity >= prefixes[-1]
        return target - capicity >= prefixes[-1]
