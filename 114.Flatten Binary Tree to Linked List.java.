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
    public void flatten(TreeNode root) {
        link(root, null);
    }
    
    private TreeNode link(TreeNode root, TreeNode tail) {
        if (root == null) {
            return tail;
        } else if (root.left == null) {
            root.right = link(root.right, tail);
        } else {
            root.right = link(root.left, link(root.right, tail));
            root.left = null;
        }
        return root;
    }
}
