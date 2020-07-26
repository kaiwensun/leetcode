# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        def gen(node):
            if node:
                for num in gen(node.left):
                    yield num
                yield node.val
                for num in gen(node.right):
                    yield num
        self.generator = gen(root)
        self.buffer = next(self.generator, None)
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        res, self.buffer = self.buffer, next(self.generator, None)
        return res
        
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.buffer is not None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
