/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class CBTInserter {

    private List<TreeNode> tree;
    public CBTInserter(TreeNode root) {
        tree = new ArrayList<>();
        tree.add(null);
        tree.add(root);
        for (int i = 2; i <= tree.size(); i++) {
            if (i % 2 == 0) {
                if (tree.get(i / 2).left != null) {
                    tree.add(tree.get(i / 2).left);
                }
            } else {
                if (tree.get(i / 2).right != null) {
                    tree.add(tree.get(i / 2).right);
                }
            }
        }
    }

    public int insert(int v) {
        TreeNode node = new TreeNode(v);
        int parent = tree.size() / 2;
        if (tree.size() % 2 == 0) {
            tree.get(parent).left = node;
        } else {
            tree.get(parent).right = node;
        }
        tree.add(node);
        return tree.get(parent).val;
    }
    
    public TreeNode get_root() {
        return tree.get(1);
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.insert(v);
 * TreeNode param_2 = obj.get_root();
 */
