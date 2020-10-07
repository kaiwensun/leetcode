# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @param {Integer} val
# @return {TreeNode}
def insert_into_bst(root, val)
    if root.nil?
        TreeNode.new(val)
    else
        if root.val < val
            root.right = self.insert_into_bst(root.right, val)
        else
            root.left = self.insert_into_bst(root.left, val)
        end
        root
    end
end

