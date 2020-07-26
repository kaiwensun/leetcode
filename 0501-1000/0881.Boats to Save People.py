class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i, j = 0, len(people) - 1
        rval = 0
        while i <= j:
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
            rval += 1
        return rval
