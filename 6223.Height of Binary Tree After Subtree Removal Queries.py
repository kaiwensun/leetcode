# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        n2node = {}
        def prepare(node, parent, depth):
            """
            return tree_height
            """
            if node:
                setattr(node, 'parent', parent)
                setattr(node, 'depth', depth)
                n2node[node.val] = node
                l = prepare(node.left, node, depth + 1)
                r = prepare(node.right, node, depth + 1)
                setattr(node, 'tree_height', max(l, r) + 1)
                return node.tree_height
            return 0
        prepare(root, None, 0)

        def prepare2(node, outside_height):
            if not node.left and not node.right:
                setattr(node, 'miss_left', max(outside_height, node.depth))
                setattr(node, 'miss_right', max(outside_height, node.depth))
                return
            if not node.left:
                setattr(node, 'miss_left', max(outside_height, node.depth + node.tree_height - 1))
                setattr(node, 'miss_right', max(outside_height, node.depth))
                prepare2(node.right, max(outside_height, node.miss_right))
                return
            if not node.right:
                setattr(node, 'miss_left', max(outside_height, node.depth))
                setattr(node, 'miss_right', max(outside_height, node.depth + node.tree_height - 1))
                prepare2(node.left, max(outside_height, node.miss_left))
                return
            setattr(node, 'miss_left', max(outside_height, node.depth + node.right.tree_height))
            setattr(node, 'miss_right', max(outside_height, node.depth + node.left.tree_height))
            prepare2(node.left, max(outside_height, node.miss_left))
            prepare2(node.right, max(outside_height, node.miss_right))

        prepare2(root, 0)

        def do_query(query):
            node = n2node[query]
            parent = node.parent
            if parent.left == node:
                return parent.miss_left
            if parent.right == node:
                return parent.miss_right

        return [do_query(query) for query in queries]

