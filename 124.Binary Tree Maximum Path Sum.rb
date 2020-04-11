# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} root
# @return {Integer}
def max_path_sum(root)
    @res = root.val
    def dfs(root)
        if root
            l, r = dfs(root.left), dfs(root.right)
            l, r = [l, 0].max, [r, 0].max
            @res = [@res, l + r + root.val].max
            [l + root.val, r + root.val].max
        else
            -1.0 / 0.0
        end
    end
    dfs root
    @res
end
