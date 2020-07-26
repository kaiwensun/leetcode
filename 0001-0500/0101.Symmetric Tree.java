/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 /**
  *Recursion Result: 
  * 193 / 193 test cases passed.
  * Status: Accepted
  * Runtime: 1 ms
  * Your runtime beats 26.05% of javasubmissions.
  *Iteration Result:
  * 193 / 193 test cases passed.
  * Status: Accepted
  * Runtime: 4 ms
  * Your runtime beats 2.85% of javasubmissions.
  *Date:
  * 8/19/2016
  */
import java.util.Stack;
public class Solution {
    public boolean isSymmetric(TreeNode root) {
        if(root==null)
            return true;
        //return isSame_recursive(root.left,root.right);
        return isSame_iterative(root.left,root.right);
    }
    private boolean isSame_recursive(TreeNode t1, TreeNode t2){
        if(t1==null || t2==null)
            return t1==t2;
        return t1.val == t2.val && isSame_recursive(t1.left,t2.right) && isSame_recursive(t1.right,t2.left);
    }
    
    class Pair{
        public final TreeNode t1;
        public final TreeNode t2;
        public Pair(TreeNode t1, TreeNode t2){
            this.t1 = t1;
            this.t2 = t2;
        }
    }
    private boolean isSame_iterative(TreeNode t1, TreeNode t2){
        Stack<Pair> stack = new Stack<>();
        stack.push(new Pair(t1,t2));
        while(!stack.empty()){
            Pair p = stack.pop();
            if(p.t1==null || p.t2==null){
                if(p.t1!=p.t2)
                    return false;
            }
            else if(p.t1.val!=p.t2.val){
                return false;
            }
            else{
                stack.push(new Pair(p.t1.left,p.t2.right));
                stack.push(new Pair(p.t1.right,p.t2.left));
            }
        }
        return true;
    }
}
