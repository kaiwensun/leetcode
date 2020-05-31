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
# @param {Integer[]} arr
# @return {Boolean}
def is_valid_sequence(root, arr, index=0)
    if index == arr.size - 1
        !root.nil? && root.val == arr[index] && root.left.nil? && root.right.nil?
    elsif !root || root.val != arr[index]
        false
    else
        is_valid_sequence(root.left, arr, index + 1) || is_valid_sequence(root.right, arr, index + 1)
    end
end



=begin
# test

class TreeNode
    attr_accessor :val, :left, :right
    def initialize(val = 0, left = nil, right = nil)
        @val = val
        @left = left
        @right = right
    end
end

def genTree(arr, index=0)
    if index >= arr.size || arr[index].nil?
        nil
    else
        TreeNode.new(arr[index], genTree(arr, index * 2 + 1), genTree(arr, index * 2 + 2))
    end
end

require 'json'
root = JSON.parse("[0,1,0,0,1,0,null,null,1,0,0]")
arr = [0,1,0,1]

root = JSON.parse("[0,1,0,0,1,0,null,null,1,0,0]")
arr = [0,0,1]

root = JSON.parse("[0,1,0,0,1,0,null,null,1,0,0]")
arr = [0,1,1]

root = JSON.parse("[8,3,null,2,1,5,4]")
arr = [8]
def run(root, arr)
    tree = genTree(root)
    puts is_valid_sequence(tree, arr)
end

run(root, arr)
=end
