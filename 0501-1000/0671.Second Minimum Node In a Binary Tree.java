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
    public int findSecondMinimumValue(TreeNode root) {
        PriorityQueue<TreeNode> heap = new PriorityQueue<>(11, new Comparator<TreeNode>() {
            @Override
            public int compare(TreeNode a, TreeNode b) {
                return a.val - b.val;
            }
        });
        int minimum = -1;
        int sndMin = -1;
        if (root != null) {
            heap.add(root);
            minimum = root.val;
        }
        TreeNode[] children = new TreeNode[2];
        while (!heap.isEmpty()) {
            TreeNode minNode = heap.poll();
            if (sndMin != -1 && minNode.val > sndMin) {
                break;
            } else if (minNode.left == null) {
                if (minNode.val > minimum) {
                    if (sndMin == -1 || minNode.val < sndMin) {
                        sndMin = minNode.val;
                    }
                }
            } else {
                children[0] = minNode.left;
                children[1] = minNode.right;
                for (TreeNode child : children) {
                    if (child.val == minimum) {
                        heap.add(child);
                    } else if (sndMin == -1 || child.val <= sndMin) {
                        sndMin = child.val;
                        heap.add(child);
                    }
                }
            }
        }
        return sndMin;
    }
}

