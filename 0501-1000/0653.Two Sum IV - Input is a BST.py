# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        INF = float("inf")
        def genFirst(root, first, second):
            if root:
                for val in genFirst(getattr(root, first), first, second):
                    yield val
                yield root.val
                for val in genFirst(getattr(root, second), first, second):
                    yield val
                    
        lgen = genFirst(root, "left", "right")
        rgen = genFirst(root, "right", "left")
        
        l, r = next(lgen, INF), next(rgen, -INF)

        while l < r:
            print l, r
            if l + r == k:
                if l == r:
                    return l == next(lgen, INF)
                return True
            elif l + r > k:
                r = next(rgen)
            else:
                l = next(lgen)
        return False

