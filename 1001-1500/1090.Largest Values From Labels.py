class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        counter = collections.Counter()
        S = res = 0
        for value, label in sorted(zip(values, labels), reverse=True):
            if counter[label] < use_limit:
                S += 1
                res += value
                counter[label] += 1
            if S == num_wanted:
                break
        return res
