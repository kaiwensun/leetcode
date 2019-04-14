# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        self.pending_dashes = None
        self.pending_num = None
        self.pointer = 0
        return self.helper(0, S)
    
    def countDashes(self, S):
        start = self.pointer
        while self.pointer < len(S) and S[self.pointer] == '-':
            self.pointer += 1
        return self.pointer - start
    
    def getNum(self, S):
        start = self.pointer
        while self.pointer < len(S) and S[self.pointer] != '-':
            self.pointer += 1
        if start == self.pointer:
            return None  # end of S
        return int(S[start: self.pointer])
        

    def helper(self, depth, S):
        if self.pending_dashes is None:
            self.pending_dashes = self.countDashes(S)
            self.pending_num = self.getNum(S)
            if self.pending_num is None:
                return None
        if self.pending_dashes == depth:
            root = TreeNode(self.pending_num)
            self.pending_dashes = None
            self.pending_num = None
            root.left = self.helper(depth + 1, S)
            root.right = self.helper(depth + 1, S)
            return root
        else:
            return None
