"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        stack = root and [root]
        while stack:
            if stack[-1] == "#":
                stack.pop()
                res.append(stack.pop().val)
            else:
                stack.append("#")
                for child in stack[-2].children[::-1]:
                    stack.append(child)
        return res

