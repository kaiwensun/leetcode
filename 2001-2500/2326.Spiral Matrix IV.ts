/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function spiralMatrix(m: number, n: number, head: ListNode | null): number[][] {
    const res = [];
    for (let i = 0; i < m; i++) {
        res.push(new Array(n));
    }
    const DIR = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    let i = 0, j = 0, k = 0;
    for (let a = 0; a < m * n; a++) {
        res[i][j] = head ? head.val : -1;
        head = head?.next;
        let ni = i + DIR[k][0], nj = j + DIR[k][1];
        if (ni < 0 || ni >= m || nj < 0 || nj >= n || res[ni][nj] !== undefined) {
            k = (k + 1) % 4;
            ni = i + DIR[k][0];
            nj = j + DIR[k][1];
        }
        i = ni;
        j = nj;
    }
    return res;
};

