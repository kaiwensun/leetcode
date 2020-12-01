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
    public List<Integer> flipMatchVoyage(TreeNode root, int[] voyage) {
        List<Integer> fail = Arrays.asList(-1);
        List<Integer> res = new ArrayList<>();
        if (root.val != voyage[0]) {
            return fail;
        }
        if (flip(root, voyage, 0, res) == -1) {
            return fail;
        }
        return res;
    }

    private int flip(TreeNode root, int[] voyage, int index, List<Integer> res) {
        if (root != null) {
            if (root.val != voyage[index]) {
                return -1;
            }
            index += 1;
            if (root.left == null || voyage[index] == root.left.val) {
                index = flip(root.left, voyage, index, res);
                if (index == -1) return -1;
                return flip(root.right, voyage, index, res);
            } else if (root.right == null || voyage[index] == root.right.val) {
                res.add(root.val);
                index = flip(root.right, voyage, index, res);
                if (index == -1) return -1;
                return flip(root.left, voyage, index, res);
            } else {
                return -1;
            }
        }
        return index;
    }
}

