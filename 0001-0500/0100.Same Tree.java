/**
 * Basic idea:
 * 	recursion on subtree.
 * Result:
 * 	54 / 54 test cases passed.
 * 	Status: Accepted
 * 	Runtime: 0 ms
 * Date:
 * 	2/7/2016
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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p==null || q==null)
            return p==q;
        return p.val==q.val && isSameTree(p.left,q.left) && isSameTree(p.right,q.right);
    }
}

