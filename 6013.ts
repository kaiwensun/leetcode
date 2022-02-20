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

function mergeNodes(head: ListNode | null): ListNode | null {
    let p = head.next;
    let q = head.next;
    while (q.next) {
        if (q.val === 0) {
            p = p.next;
        } else {
            const addOn = q.val;
            q.val = 0;
            p.val += addOn;
        }
        q = q.next;
    }
    p.next = null;
    return head.next;
};

