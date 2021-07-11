# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        val_to_root = {}
        for root in trees:
            if root.val in val_to_root:
                return None
            val_to_root[root.val] = root

        children = set()
        for root in trees:
            for child in root.left, root.right:
                if child:
                    if child.val in children:
                        return None
                    children.add(child.val)
        for root in trees:
            if root.left:
                val = root.left.val
                if val in val_to_root:
                    root.left = val_to_root[val]
                    del val_to_root[val]
            if root.right:
                val = root.right.val
                if val in val_to_root:
                    root.right = val_to_root[val]
                    del val_to_root[val]
        if len(val_to_root) != 1:
            return None
        super_root = val_to_root.popitem()[1]

        def test_and_count(root, mn, mx):
            if root is None:
                return 0
            if not mn < root.val < mx:
                return None
            l = test_and_count(root.left, mn, root.val)
            if l is None:
                return None
            r = test_and_count(root.right, root.val, mx)
            if r is None:
                return None
            return l + r + 1

        res = test_and_count(super_root, float("-inf"), float("inf"))
        if res is None or res != len(children) + 1:
            None
        else:
            return super_root

