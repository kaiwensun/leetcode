""""
Basic idea:
    split and stack
Result:
    252 / 252 test cases passed.
    Status: Accepted
    Runtime: 48 ms
    Your runtime beats 89.89% of python submissions.
Date:
    2/7/2016
"""

"""
CHEAT:
    import os
    return os.path.abspath(path);
"""

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        #Assume abslute path
        path = path[1:].split('/')
        stack = []
        for d in path:
            if d=='.' or d=='':
                continue
            elif d=='..':
                try:
                    stack.pop()
                except IndexError:
                    pass
            else:
                stack.append(d)
        path = '/'.join(stack)
        return '/'+path
        

