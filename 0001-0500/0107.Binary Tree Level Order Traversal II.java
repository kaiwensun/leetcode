/**
 *Basic idea:
 * DFS
 *Result:
 * 34 / 34 test cases passed.
 * Status: Accepted
 * Runtime: 2 ms
 * Your runtime beats 68.26% of java submissions.
 *Date:
 * 9/8/2016
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
    private List<List<Integer>> res;
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        res = new LinkedList<List<Integer>>();
        dfs(root,0);
        return res;
    }
    private void dfs(TreeNode root, int level){
        if(root==null)
            return;
        if(level==res.size())
            res.add(0,new LinkedList<Integer>());
        List<Integer> row = res.get(res.size()-level-1);
        row.add(root.val);
        dfs(root.left,level+1);
        dfs(root.right,level+1);
    }
}
