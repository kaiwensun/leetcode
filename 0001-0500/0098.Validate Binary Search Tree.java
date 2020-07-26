/**
 * Idea:
 *  recursive. Be alert that there might be multiple Integer.MIN/MAX_value in the tree.
 * Result:
 *  74 / 74 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * Your runtime beats 33.15% of javasubmissions.
 *Date:
 * 8/27/2016
 */

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root,Integer.MIN_VALUE, Integer.MAX_VALUE);
    }
    private boolean isValidBST(TreeNode root, int min, int max){
        return root==null || ((root.left==null || (min<=root.left.val && root.left.val<root.val && isValidBST(root.left,min,root.val-1))) && (root.right==null || (root.val<root.right.val && root.right.val<=max && isValidBST(root.right,root.val+1,max))));
    }
}
