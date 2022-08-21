/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function amountOfTime(root: TreeNode | null, start: number): number {
    const tree = {};

    function add(from, to) {
        if (from && to) {
            tree[from.val] ||= [];
            tree[from.val].push(to.val);
        }
    }

    (function graph(root: TreeNode | null) {
        if (!root) return false;
        const inLeft = graph(root.left);
        const inRight = graph(root.right);
        if (inLeft) add(root.left, root);
        else add(root, root.left);
        if (inRight) add(root.right, root);
        else add(root, root.right);
        return inLeft || inRight || root.val === start;
    })(root);
    return (function depth(root) {
        return (tree[root] || []).reduce((acc, child) => Math.max(acc, depth(child)), -1) + 1;
    })(start);
};

