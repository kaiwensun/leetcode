/**
 *Basic idea:
 * Determine the range of subtree arrays, and solve recursivelly.
 *Improved O(n) idea:
 * Using stack. https://discuss.leetcode.com/topic/795/the-iterative-solution-is-easier-than-you-think
 *Result:
 * 202 / 202 test cases passed.
 * Status: Accepted
 * Runtime: 21 ms
 * Your runtime beats 21.54% of javasubmissions.
 *Date:
 * 9/2/2016
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
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return buildTree(preorder,0,preorder.length,inorder,0,inorder.length);
    }
    private TreeNode buildTree(int[] preorder, int pl, int pr, int[] inorder, int il, int ir){
        
        for(int i=il;i<ir;i++){
            if(inorder[i]==preorder[pl]){
                int lsize = i-il;
                TreeNode ltree = buildTree(preorder,pl+1,pl+1+lsize,inorder,il,il+lsize);
                TreeNode rtree = buildTree(preorder,pl+1+lsize,pr,inorder, il+1+lsize,ir);
                TreeNode root = new TreeNode(preorder[pl]);
                root.left = ltree;
                root.right = rtree;
                return root;
            }
        }
        return null;
    }
}
