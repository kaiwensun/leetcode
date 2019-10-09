/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} v
 * @param {number} d
 * @return {TreeNode}
 */ 
function walk(root, v, d, you_are_right) {
    if (d == 1) {
        var node = new TreeNode(v);
        if (you_are_right) {
            node.right = root;
        } else {
            node.left = root;   
        }
        return node;
    } else {
        if (root) {
            root.left = walk(root.left, v, d - 1, false);
            root.right = walk(root.right, v, d - 1, true);
        }
        return root;
    }
};
var addOneRow = walk;
