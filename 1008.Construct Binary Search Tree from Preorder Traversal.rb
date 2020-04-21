# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {Integer[]} preorder
# @return {TreeNode}
def bst_from_preorder(preorder)
    @index = 0
    @array = preorder
    def dfs(smallest, biggest)
        if @index < @array.size && smallest <= @array[@index] && @array[@index] <= biggest
            root = TreeNode.new @array[@index]
            @index += 1
            root.left = dfs(smallest, [biggest, root.val].min)
            root.right = dfs([smallest, root.val].max, biggest)
            return root
        end
    end
    dfs(-1.0/0.0, 1.0/0.0)
end
