import collections
class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        children = set(leftChild) | set(rightChild)
        children.discard(-1)
        if len(children) != n - 1:
            return False
        visited = [False] * n
        def dfs(root):
            if root != -1:
                if visited[root]:
                    return False
                visited[root] = True
                return dfs(leftChild[root]) and dfs(rightChild[root])
            return True
        return dfs((set(range(n)) - children).pop())
