class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return "(%s, (%s, %s))" % (self.val, self.left, self.right)

class Solution:
    def inorderSuccessor(self, root, p):
        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p
        else:
            if root:
                if p.val < root.val:
                    return self.inorderSuccessor(root.left, p) or root
                else:
                    return self.inorderSuccessor(root.right, p)

def run_test():
    array = [5, 3, 6, 2, 4, None, None, 1]
    p = 6

    def buildTree(i):
        if i < len(array) and array[i] is not None:
            return TreeNode(array[i], buildTree(i * 2 + 1), buildTree(i * 2 + 2))

    def getNode(root, value):
        if root is None:
            assert(False)
        if root.val == value:
            return root
        elif root.val < value:
            return getNode(root.right, value)
        else:
            return getNode(root.left, value)

    tree = buildTree(0)
    node = getNode(tree, p)
    sol = Solution()
    res = sol.inorderSuccessor(tree, node)
    print(res)
