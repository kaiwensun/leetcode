# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def genVals(root):
            if root:
                for node in genVals(root.left):
                    yield node 
                yield root.val
                for node in genVals(root.right):
                    yield node
        res = []
        tree1, tree2 = genVals(root1), genVals(root2)
        INF = float('inf')
        val1, val2 = next(tree1, INF), next(tree2, INF)
        while val1 != INF or val2 != INF:
            if val1 < val2:
                res.append(val1)
                val1 = next(tree1, INF)
            else:
                res.append(val2)
                val2 = next(tree2, INF)
        return res

