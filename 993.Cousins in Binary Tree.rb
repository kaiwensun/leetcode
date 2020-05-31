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
# @param {Integer} x
# @param {Integer} y
# @return {Boolean}
def is_cousins(root, x, y)
    @res = []
    def walk(root, x, y, depth)
        if root
            if root.val == x || root.val == y
                return true
            end
            if @res.size < 2 && walk(root.left, x, y, depth + 1)
                @res << [root, depth]
            end
            if @res.size < 2 && walk(root.right, x, y, depth + 1)
                @res << [root, depth]
            end
        end
        return false
    end
    walk(root, x, y, 0)
    @res.size == 2 && @res[0][1] == @res[1][1] && @res[0][0].val != @res[1][0].val
end
