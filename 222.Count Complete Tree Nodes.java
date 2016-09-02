/**
 *Basic idea:
 * Call int countNode(TreeNode root,int depth) recursively.
 * If root.right reaches the last level, then root.left must be full;
 * otherwise root.right must be full without the last level.
 * So we need recursively call on either root.right or root.left; not both.
 * Since calcDepth() is recursively called, the time complexity is O(logn * logn).
 *Improved idea:
 * https://discuss.leetcode.com/topic/31392/my-java-solution-with-explanation-which-beats-99/2
 *Result:
 * 18 / 18 test cases passed.
 * Status: Accepted
 * Runtime: 62 ms
 * Your runtime beats 93.99% of javasubmissions.
 *Date:
 * 9/3/2016
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
    private int depth;
    private int cnt;
    public int countNodes(TreeNode root) {
        int depth = calDepth(root);
        return countNode(root,depth);
    }
    private int calDepth(TreeNode root){
        int depth = 0;
        while(root!=null){
            root = root.left;
            depth++;
        }
        return depth;
    }
    private int countNode(TreeNode root,int depth){
        if(root==null)
            return 0;
        if(depth==1)
            return root==null?0:1;
        return calDepth(root.right)==depth-1?(1<<(depth-1))+countNode(root.right, depth-1):countNode(root.left,depth-1)+((1<<(depth-2)));
    }
}
