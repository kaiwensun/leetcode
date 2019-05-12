# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        collection = []
        if K == 0:
            return [target.val]
        def markChildren(root, k):
            if root is not None:
                if k == K:
                    collection.append(root.val)
                markChildren(root.left, k + 1)
                markChildren(root.right, k + 1)

        def searchTarget(root):
            if root is not None:
                if root is target:
                    return 1
                else:
                    for child, child_sibling in ((root.left, root.right), (root.right, root.left)):
                        child_res = searchTarget(child)
                        if child_res is not None:
                            if child_res < K:
                                markChildren(child_sibling, child_res + 1)
                            elif child_res == K:
                                collection.append(root.val)
                            return child_res + 1

        markChildren(target, 0)
        searchTarget(root)
        return collection
