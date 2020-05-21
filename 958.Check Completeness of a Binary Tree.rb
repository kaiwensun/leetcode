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
# @return {Boolean}
def is_complete_tree(root)
    @max_depth = nil
    @cur_depth = nil
    dfs(root, 0)
end

def dfs(root, depth)
    if root
        dfs(root.left, depth + 1) && dfs(root.right, depth + 1)
    else
        if @max_depth.nil?
            @max_depth = @cur_depth = depth
        elsif depth > @cur_depth || (depth != @max_depth && depth != @max_depth - 1)
            return false
        end
        @cur_depth = depth
        true
    end
end
