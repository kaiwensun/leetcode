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
def count_nodes(root)
    # return 0 if root.nil?
    lheight = leftHeight(root)
    rheight = rightHeight(root)
    if lheight == rheight
        return (1 << lheight) - 1
    else
        return count_nodes(root.left) + count_nodes(root.right) + 1
    end
end

def leftHeight(root)
    cnt = 0
    while root
        root = root.left
        cnt += 1
    end
    return cnt
end

def rightHeight(root)
    cnt = 0
    while root
        root = root.right
        cnt += 1
    end
    return cnt
end
