# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def bfs(nodes):
            if not nodes:
                return 0
            values = [node.val for node in nodes]
            sorted_arr = sorted(values)
            sorted_map = {v : i for i, v in enumerate(sorted_arr)}
            res = 0
            for i in range(len(values)):
                if values[i] != sorted_arr[i]:
                    j = sorted_map[values[i]]
                    while j != i:
                        values[i], values[j] = values[j], values[i]
                        j = sorted_map[values[i]]
                        res += 1
            children = []
            for node in nodes:
                if node.left: children.append(node.left)
                if node.right: children.append(node.right)
            return res + bfs(children)
        return bfs([root])

