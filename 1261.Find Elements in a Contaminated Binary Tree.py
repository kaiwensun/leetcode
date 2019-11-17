# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements(object):

    
    def __init__(self, root, val=0):
        """
        :type root: TreeNode
        """
        if val == 0:
            self.ele = set()
        if root is None:
            return
        self.ele.add(val)
        root.val = val
        self.__init__(root.left, val * 2 + 1)
        self.__init__(root.right, val * 2 + 2)
        

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.ele

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
