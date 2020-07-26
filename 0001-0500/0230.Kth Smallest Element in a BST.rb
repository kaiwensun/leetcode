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
# @param {Integer} k
# @return {Integer}
def kth_smallest(root, k)
    @seen = 0
    walk(root, k)
end

def walk(root, k)
    if root
        left = walk(root.left, k)
        return left if left
        @seen += 1
        return root.val if @seen == k
        return walk(root.right, k)
    end
end
