/**
 * Definition for node.
 * class Node {
 *     val: boolean
 *     isLeaf: boolean
 *     topLeft: Node | null
 *     topRight: Node | null
 *     bottomLeft: Node | null
 *     bottomRight: Node | null
 *     constructor(val?: boolean, isLeaf?: boolean, topLeft?: Node, topRight?: Node, bottomLeft?: Node, bottomRight?: Node) {
 *         this.val = (val===undefined ? false : val)
 *         this.isLeaf = (isLeaf===undefined ? false : isLeaf)
 *         this.topLeft = (topLeft===undefined ? null : topLeft)
 *         this.topRight = (topRight===undefined ? null : topRight)
 *         this.bottomLeft = (bottomLeft===undefined ? null : bottomLeft)
 *         this.bottomRight = (bottomRight===undefined ? null : bottomRight)
 *     }
 * }
 */

function construct(grid: number[][]): Node | null {
    function build(i: number, j: number, size: number) {
        if (size === 1) {
            return new Node(grid[i][j] === 1, true);
        }
        size /= 2;
        const res = new Node(false, false, build(i, j, size), build(i, j + size, size), build(i + size, j, size), build(i + size, j + size, size));
        for (const child of [res.topLeft, res.topRight, res.bottomLeft, res.bottomRight]) {
            if (!child.isLeaf || child.val !== res.bottomRight.val) {
                return res;
            }
        }
        return res.topLeft;

    }
    return build(0, 0, grid.length);
};

