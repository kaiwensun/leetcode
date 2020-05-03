class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        src = set()
        dst = set()
        for path in paths:
            src.add(path[0])
            dst.add(path[1])
        return (dst - src).pop()
