/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class TreeIterator {
    private boolean reversed;
    Stack<TreeNode> stack;
    public TreeIterator(TreeNode root, boolean reversed) {
        this.reversed = reversed;
        stack = new Stack<>();
        stack.add(root);
        dive();
    }
    private void dive() {
        TreeNode next = reversed ? stack.peek().right : stack.peek().left;
        while (next != null) {
            stack.add(next);
            next = reversed ? stack.peek().right : stack.peek().left;
        }
    }
    public int getNext() {
        TreeNode resNode = stack.pop();
        TreeNode next = reversed ? resNode.left : resNode.right;
        if (next != null) {
            stack.add(next);
            dive();
        }
        return resNode.val;
    }
    
    public boolean hasNext() {
        return !stack.isEmpty();
    }
}
class Solution {
    public boolean twoSumBSTs(TreeNode root1, TreeNode root2, int target) {
        TreeIterator it1 = new TreeIterator(root1, false);
        TreeIterator it2 = new TreeIterator(root2, true);
        int v1 = it1.getNext();
        int v2 = it2.getNext();
        while (it1.hasNext() && it2.hasNext()) {
            int sum = v1 + v2;
            if (sum == target) {
                return true;
            } else if (sum < target) {
                v1 = it1.getNext();
            } else {
                v2 = it2.getNext();
            }
        }
        return v1 + v2 == target;
    }
}
