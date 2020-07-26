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
def diameter_of_binary_tree(root)
    res = 0
    def dfs(root, &blk)
        if root
            l = dfs(root.left, &blk)
            r = dfs(root.right, &blk)
            blk.call (l + r + 1)
            [l, r].max + 1
        else
            0
        end
    end
    dfs(root) { |x| res = [res, x].max }
    [res - 1, 0].max
end
