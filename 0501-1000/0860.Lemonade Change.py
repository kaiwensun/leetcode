class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        counter = collections.Counter()
        for bill in bills:
            if bill == 20:
                counter[10] -= 1
                counter[5] -= 1
            elif bill == 10:
                counter[5] -= 1
                counter[10] += 1
            else:
                counter[5] += 1
            if counter[10] < 0:
                counter[5] -= 2
                counter[10] = 0
            if counter[5] < 0:
                return False
        return True
