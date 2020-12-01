class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        res = []
        for path in folder:
            if res and path.startswith(res[-1] + "/"):
                continue
            res.append(path)
        return res

