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
def max_path_sum(root)
    @res = -1.0 / 0
    def dfs(root)
        if root.nil?
            0
        else
            left = dfs(root.left)
            right = dfs(root.right)
            @res = [@res, left + right + root.val].max
            [0, [left, right].max + root.val].max
        end
    end
    dfs(root)
    @res
end
