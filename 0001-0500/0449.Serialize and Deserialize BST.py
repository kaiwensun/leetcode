# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return str(self.serialize_tuple(root))
    
    def serialize_tuple(self, root):
        if root is None:
            return None
        return root.val, self.serialize_tuple(root.left), self.serialize_tuple(root.right)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        t = eval(data)
        return self.deserialize_tuple(t)
        
    def deserialize_tuple(self, t):
        if t is None:
            return None
        root = TreeNode(t[0])
        root.left = self.deserialize_tuple(t[1])
        root.right = self.deserialize_tuple(t[2])
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
