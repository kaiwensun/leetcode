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
    public boolean isUnivalTree(TreeNode root) {
        return isUnivalTree(root, root.val);
    }

    private boolean isUnivalTree(TreeNode root, int value) {
        return root == null || (root.val == value && isUnivalTree(root.left, value) && isUnivalTree(root.right, value));
    }
}

