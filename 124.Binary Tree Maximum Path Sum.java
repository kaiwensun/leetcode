/**
 *Basic Idea:
 * DFS and keep record of the max sum of the tree AND the max sum passing through the root.
 *Result:
 * 92 / 92 test cases passed.
 * Status: Accepted
 * Runtime: 3 ms
 * Your runtime beats 16.83% of javasubmissions.
 *Date:
 * 8/31/2016
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
    public int maxPathSum(TreeNode root) {
        return maxPathSumFromRootAndNot(root)[1];
    }
    
    /**
     * @return a size-2 array. the first num is the max sum of path from root;
     * the second is the max sum of path in the (sub)tree.
     */
    int[] maxPathSumFromRootAndNot(TreeNode root){
        if(root==null){
            return new int[]{Integer.MIN_VALUE,Integer.MIN_VALUE};
        }
        int left[] = maxPathSumFromRootAndNot(root.left);
        int right[] = maxPathSumFromRootAndNot(root.right);
        int rtn[] = new int[2];
        rtn[0] = Math.max(0,Math.max(left[0],right[0]))+root.val;
        rtn[1] = Math.max(left[1],right[1]);

        int through = root.val;
        if(left[0]>0)
            through += left[0];
        if(right[0]>0)
            through += right[0];
        rtn[1] = Math.max(rtn[1],through);
        return rtn;
    }
}
