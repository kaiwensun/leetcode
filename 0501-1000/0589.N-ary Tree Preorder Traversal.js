/**
 * // Definition for a Node.
 * function Node(val, children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */
/**
 * @param {Node} root
 * @return {number[]}
 */
var preorder = function(root) {
    function walk(root) {
        if (root != null) {
            res.push(root.val);
            if (root.children != null) {
                root.children.forEach(walk);
            }
        }
    }
    res = []
    walk(root);
    return res;
};
