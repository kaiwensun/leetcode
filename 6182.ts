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

function reverseOddLevels(root: TreeNode | null): TreeNode | null {
    function* dfs(node, depth, isLeft) {
        if (node) {
            if (depth % 2) yield node;
            const children = [node.left, node.right];
            if (isLeft) children.reverse();
            for (const child of children) {
                for (const offspring of dfs(child, depth + 1, isLeft)) {
                    yield offspring;
                }
            }
        }
    }
    const [left, right] = [dfs(root.left, 1, true), dfs(node.right, 1, false)];
    while (true) {
        const [l, r] = [left.next(), right.next()];
        if (l.done) break;
        [l.value.val, r.value.val] = [r.value.val, l.value.val];
    }
    return root;
};

