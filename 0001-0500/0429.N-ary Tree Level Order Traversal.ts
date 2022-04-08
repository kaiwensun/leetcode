/**
 * Definition for node.
 * class Node {
 *     val: number
 *     children: Node[]
 *     constructor(val?: number) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.children = []
 *     }
 * }
 */

function levelOrder(root: Node | null): number[][] {
    if (!root) return [];
    const res = [];
    const queue = [null, root];
    while (queue.length !== 1) {
        const item = queue.shift();
        if (item) {
            res[res.length - 1].push(item.val);
            item.children.forEach(child => queue.push(child));
        } else {
            res.push([]);
            queue.push(item);
        }
    }
	return res;
};

