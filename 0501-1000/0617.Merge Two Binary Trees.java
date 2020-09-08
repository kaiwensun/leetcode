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
    public TreeNode mergeTrees(TreeNode t1, TreeNode t2) {
        TreeNode root = null;
        if (t1 == null || t2 == null) {
            if (t1 != null) {
                root = new TreeNode(t1.val);
                root.left = mergeTrees(t1.left, null);
                root.right = mergeTrees(t1.right, null);
            } else if (t2 != null) {
                root = new TreeNode(t2.val);
                root.left = mergeTrees(null, t2.left);
                root.right = mergeTrees(null, t2.right);
            }
        } else {
            root = new TreeNode(t1.val + t2.val);
            root.left = mergeTrees(t1.left, t2.left);
            root.right = mergeTrees(t1.right, t2.right);
        }
        return root;
    }
}
