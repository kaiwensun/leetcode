class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda p:(-p[0], p[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
