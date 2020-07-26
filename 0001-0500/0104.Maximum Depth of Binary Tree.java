/**
 * Basic idea:
 * 	recursion on subtree.
 * Result:
 * 	38 / 38 test cases passed.
 * 	Status: Accepted
 * 	Runtime: 1 ms
 * Date:
 * 	2/7/2016
 */
public class Solution {
    public int maxDepth(TreeNode root) {
        return root==null?0:1+Math.max(maxDepth(root.left),maxDepth(root.right));
    }
}

