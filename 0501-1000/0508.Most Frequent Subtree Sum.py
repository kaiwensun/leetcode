# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        counter = collections.Counter()
        self.subTreeSum(root, counter)
        rval = []
        maximum = 0
        for k, v in counter.iteritems():
            if v > maximum:
                rval = []
                maximum = v
            if v == maximum:
                rval.append(k)
        return rval
        
    def subTreeSum(self, root, counter):
        if root is None:
            return 0
        leftSum = self.subTreeSum(root.left, counter)
        rightSum = self.subTreeSum(root.right, counter)
        mySum = leftSum + rightSum + root.val
        counter[mySum] += 1
        return mySum
        
