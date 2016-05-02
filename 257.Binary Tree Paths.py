"""
Result:
  209 / 209 test cases passed.
  Status: Accepted
  Runtime: 44 ms
  Your runtime beats 90.56% of pythonsubmissions.
Date:
  5/1/2016
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        collection = []
        if root!=None:
            self.collectTreePaths(root,str(root.val),collection)
        return collection
    
    def collectTreePaths(self, root, curpath, collection):
        if root==None:
            return
        if root.left==None and root.right==None:
            collection.append(curpath)
            return
        if root.left!=None:
            self.collectTreePaths(root.left, curpath+"->"+str(root.left.val),collection)
        if root.right!=None:
            self.collectTreePaths(root.right, curpath+"->"+str(root.right.val),collection)
