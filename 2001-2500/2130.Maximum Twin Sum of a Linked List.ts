i/**
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

function pairSum(head: ListNode | null): number {
    let size = 0, res = 0;
    let first = head;
    function walk(p: ListNode) {
        if (p === null) {
            return;
        }
        size += 1;
        walk(p.next);
        if (size >= 0) {
            size -= 2;
            res = Math.max(res, first.val + p.val);
            first = first.next;
        }
    }
    walk(head);
    return res;
};

