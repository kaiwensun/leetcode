/**
 *Basic idea:
 * stack without flag. not maintain original tree.
 *Result:
 * 67 / 67 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * Your runtime beats 67.65% of javasubmissions
 *Date:
 * 9/5/2016
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
    Stack<TreeNode> stack = new Stack<>();
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new LinkedList<>();
        if(root==null)
            return res;
        stack.push(root);
        while(!stack.isEmpty()){
            TreeNode e = stack.peek();
            if(e.left!=null){
                stack.push(e.left);
                e.left=null;
            }
            else if(e.right!=null){
                stack.push(e.right);
                e.right=null;
            }
            else{
                stack.pop();
                res.add(e.val);
            }
        }
        return res;
    }
}
