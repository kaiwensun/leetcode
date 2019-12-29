# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        stack1 = [root1] if root1 else []
        stack2 = [root2] if root2 else []
        def fillStack(stack):
            while stack and stack[-1].left:
                stack.append(stack[-1].left)
        fillStack(stack1)
        fillStack(stack2)
        res = []
        while stack1 or stack2:
            if stack1 and stack2:
                stack = stack1 if stack1[-1].val < stack2[-1].val else stack2
            else:
                stack = stack1 or stack2
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
                fillStack(stack)
        return res
