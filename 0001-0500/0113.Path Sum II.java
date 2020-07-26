/**
 *Rresult:
 * 114 / 114 test cases passed.
 * Status: Accepted
 * Runtime: 6 ms
 * Your runtime beats 10.40% of javasubmissions.
 *Date:
 * /9/2/2016
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
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        if(root==null){
            return new LinkedList<List<Integer>>();
        }
        if(root.left==null && root.right==null){
            List<List<Integer>> lsts = new LinkedList<List<Integer>>();
            if(sum==root.val){
                List<Integer> lst = new LinkedList<Integer>();
                lst.add(sum);
                lsts.add(lst);
            }
            return lsts;
        }
        List<List<Integer>> l = pathSum(root.left,sum-root.val);
        List<List<Integer>> r = pathSum(root.right,sum-root.val);
        for(List<Integer> list : l)
            list.add(0,root.val);
        for(List<Integer> list : r)
            list.add(0,root.val);
        l.addAll(r);
        return l;
    }
}
