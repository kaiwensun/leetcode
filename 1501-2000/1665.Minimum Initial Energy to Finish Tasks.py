class Solution(object):
    def minimumEffort(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        energy = 0
        for task in sorted(tasks, key=lambda t: (t[1] - t[0], t[1])):
            energy = max(energy + task[0], task[1])
        return energy

