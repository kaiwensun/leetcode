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
# @return {Integer}
def sum_numbers(root, prefix=0)
    if root.nil?
        0
    elsif root.left.nil? && root.right.nil?
        prefix * 10 + root.val
    else
        sum_numbers(root.left, prefix * 10 + root.val) + sum_numbers(root.right, prefix * 10 + root.val)
    end
end
