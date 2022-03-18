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

function tree2str(root: TreeNode | null): string {
    const res = (function dfs(root: TreeNode | null, res: (string|number)[]) {
        if (root) {
            res.push('(');
            res.push(root.val);
            if (!root.left && root.right) res.push("()");
            dfs(root.left, res);
            dfs(root.right, res);
            res.push(')');
        }
        return res;
    })(root, []).join('');
    return res.slice(1, res.length - 1);
};

