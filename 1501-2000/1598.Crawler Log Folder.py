class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        depth = 0
        for log in logs:
            if log == "../":
                depth = max(0, depth - 1)
            elif log == "./":
                pass
            else:
                depth += 1
        return depth
