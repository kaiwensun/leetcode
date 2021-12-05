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

function getDirections(root: TreeNode | null, startValue: number, destValue: number): string {
    function dfs(node: TreeNode | null, target: number) {
        if (!node) {
            return null;
        }
        if (node.val === target) {
            return [];
        }
        let res = dfs(node.left, target);
        if (res) {
            res.push('L');
            return res;
        }
        res = dfs(node.right, target);
        if (res) {
            res.push('R');
            return res;
        }
        return null;
    }
    let startPath = dfs(root, startValue);
    let destPath = dfs(root, destValue);
    while (startPath.length && destPath.length && startPath[startPath.length - 1] === destPath[destPath.length - 1]) {
        startPath.pop();
        destPath.pop();
    }
    return startPath.map(_ => 'U').concat(destPath.reverse()).join('');
};

