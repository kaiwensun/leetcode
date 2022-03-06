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

function createBinaryTree(descriptions: number[][]): TreeNode | null {
    const non_roots = new Set<number>();
    const graph = {};
    for (const [parent, child, isLeft] of descriptions) {
        graph[parent] ||= [undefined, undefined];
        graph[parent][1 - isLeft] = child;
        non_roots.add(child);
    }
    let root = descriptions.map(description => description[0]).filter(parent => !non_roots.has(parent))[0];
    function dfs(num: number): TreeNode | null {
        if (!num) {
            return null;
        }
        return new TreeNode(num, dfs(graph[num]?.[0]), dfs(graph[num]?.[1]));
    }
    return dfs(root);
};

