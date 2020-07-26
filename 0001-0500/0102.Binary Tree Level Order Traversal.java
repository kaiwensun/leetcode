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
  * 34 / 34 test cases passed.
  * Status: Accepted
  * Runtime: 3 ms
  * Your runtime beats 13.06% of javasubmissions.
  *Date:
  * 8/19/2016
  */ 
import java.util.LinkedList;
import java.util.Queue;
public class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new LinkedList<>();
        Queue<TreeNode> parents = new LinkedList<>();
        Queue<TreeNode> children = new LinkedList<>();
        parents.add(root);
        while(!parents.isEmpty()){
            List<Integer> row = new LinkedList<>();
            while(!parents.isEmpty()){
                TreeNode node = parents.remove();
                if(node==null)
                    continue;
                row.add(node.val);
                children.add(node.left);
                children.add(node.right);
            }
            if(row.isEmpty())
                break;
            result.add(row);
            Queue tmp = parents;
            parents = children;
            children = tmp;
        }
        return result;
    }
}
