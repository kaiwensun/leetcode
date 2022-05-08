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

function averageOfSubtree(root: TreeNode | null): number {
    function dfs(root: TreeNode | null) {
        // return [res, sum, cnt]
        if (!root) {
            return [0, 0, 0];
        }
        const [res1, sum1, cnt1] = dfs(root.left);
        const [res2, sum2, cnt2] = dfs(root.right);
        let res = res1 + res2, sum = sum1 + sum2 + root.val, cnt = cnt1 + cnt2 + 1;
        if (Math.floor(sum / cnt) == root.val) {
            res++;
        }
        return [res, sum, cnt];
    }
    return dfs(root)[0];
};

