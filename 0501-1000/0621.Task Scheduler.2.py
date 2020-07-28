import collections
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = collections.Counter(tasks)
        mx = max(counter.values())
        turns = counter.values().count(mx)
        return max((mx - 1) * (n + 1) + turns, len(tasks))
