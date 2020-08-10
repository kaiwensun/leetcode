"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        copied = {}
        def dfs(node):
            if node.val not in copied:
                rtn = Node(node.val)
                copied[node.val] = rtn
                for neighbor in node.neighbors:
                    rtn.neighbors.append(dfs(neighbor))
            return copied[node.val]
        return node and dfs(node)
