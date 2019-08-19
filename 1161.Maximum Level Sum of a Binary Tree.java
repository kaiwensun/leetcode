/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int maxLevelSum(TreeNode root) {
        List<Integer> acc = new ArrayList<>();
        dfs(root, 0, acc);
        int res = 0;
        int max = Integer.MIN_VALUE;
        for (int i = 0; i < acc.size(); i++) {
            if (max < acc.get(i)) {
                res = i;
                max = acc.get(i);
            }
        }
        return res + 1;
    }
    
    private void dfs(TreeNode root, int level, List<Integer> acc) {
        if (root == null) {
            return;
        }
        if (acc.size() == level) {
            acc.add(0);
        }
        acc.set(level, acc.get(level) + root.val);
        dfs(root.left, level + 1, acc);
        dfs(root.right, level + 1, acc);
    }
}
