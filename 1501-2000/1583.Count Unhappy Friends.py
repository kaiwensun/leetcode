class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        wants = [None] * n
        for x, y in pairs:
            wants[x] = set(preferences[x][:preferences[x].index(y)])
            wants[y] = set(preferences[y][:preferences[y].index(x)])
        unhappy = set()
        for x in xrange(n):
            for y in xrange(x + 1, n):
                if x == 1 and y == 3:
                    print(wants[x], wants[y])
                if y in wants[x] and x in wants[y]:
                    unhappy.add(x)
                    unhappy.add(y)
        return len(unhappy)

