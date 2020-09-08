/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode root = null;
        for(int num : nums) {
            TreeNode curNode = new TreeNode(num);
            while(!stack.isEmpty() && stack.peek().val < num) {
                curNode.left = stack.pop();
            }
            if (stack.isEmpty()) {
                root = curNode;
            } else {
                stack.peek().right = curNode;
            }
            stack.push(curNode);
        }
        return root;
    }
}

