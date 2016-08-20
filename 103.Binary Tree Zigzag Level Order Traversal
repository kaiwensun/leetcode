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
  *Result:
  * 33 / 33 test cases passed.
  * Status: Accepted
  * Runtime: 3 ms
  * Your runtime beats 12.62% of javasubmissions.
  *Date:
  * 8/20/2016
  */
  
public class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new LinkedList<>();
        Stack<TreeNode> parents = new Stack<>();
        Stack<TreeNode> children = new Stack<>();
        parents.push(root);
        int level = 0;
        while(!parents.isEmpty()){
            List<Integer> row = new LinkedList<>();
            while(!parents.isEmpty()){
                TreeNode node = parents.pop();
                if(node==null)
                    continue;
                row.add(node.val);
                if(level%2==1){
                    children.push(node.right);
                    children.push(node.left);
                }
                else{
                    children.push(node.left);
                    children.push(node.right);
                }
            }
            if(row.isEmpty())
                break;
            result.add(row);
            Stack tmp = parents;
            parents = children;
            children = tmp;
            level++;
        }
        return result;
    }
}
