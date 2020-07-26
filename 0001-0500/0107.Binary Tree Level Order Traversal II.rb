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
# @return {Integer[][]}
def level_order_bottom(root)
    res = []
    if root
        row = [root]
        next_row = []
        until row.empty?
            next_row = []
            res << []
            for node in row
                res[-1] << node.val
                next_row << node.left if node.left
                next_row << node.right if node.right
            end
            row = next_row
        end
    end
    res.reverse
end
