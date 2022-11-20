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

function closestNodes(root: TreeNode | null, queries: number[]): number[][] {
    function queryMin(node: TreeNode | null, query: number) {
        if (node === null) {
            return 0;
        }
        if (node.val === query) {
            return node.val;
        } else if (node.val < query) {
            return queryMin(node.right, query) || node.val;
        } else {
            return queryMin(node.left, query);
        }
    }

    function queryMax(node: TreeNode | null, query: number) {
        if (node === null) {
            return 0;
        }
        if (node.val === query) {
            return node.val;
        } else if (node.val > query) {
            return queryMax(node.left, query) || node.val;
        } else {
            return queryMax(node.right, query);
        }
    }

    return queries.map(query => [queryMin(root, query) || -1, queryMax(root, query) || -1]);
};
