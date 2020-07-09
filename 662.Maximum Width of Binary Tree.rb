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
def width_of_binary_tree(root)
    minmax = []
    dfs(root, 0, 0, minmax)
    minmax.map{ |min, max| max - min }.max + 1
end

def dfs(root, level, id, minmax)
    if root
        if minmax[level].nil?
            minmax[level] = [id, id]
        else
            minmax[level][0] = [minmax[level][0], id].min
            minmax[level][1] = [minmax[level][1], id].max
        end
        dfs(root.left, level + 1, id * 2 + 1, minmax)
        dfs(root.right, level + 1, id * 2 + 2, minmax)
    end
end
