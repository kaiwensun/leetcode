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

function replaceValueInTree(root: TreeNode | null): TreeNode | null {
    let queue = [root];
    while (queue.length) {
        let childrenSum = 0;
        const nextQueue = [];
        for (const parent of queue) {
            for (const child of [parent.left, parent.right]) {
                if (child) {
                    nextQueue.push(child);
                    childrenSum += child.val;
                }
            }
        }
        for (const parent of queue) {
            const brosers = (parent.left?.val || 0) + (parent.right?.val || 0);
            parent.left && (parent.left.val = childrenSum - brosers);
            parent.right && (parent.right.val = childrenSum - brosers);
        }
        queue = nextQueue;
    }
    root.val = 0;
    return root;
};

