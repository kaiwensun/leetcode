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

function removeNodes(head: ListNode | null): ListNode | null {
    function recurse(head: ListNode | null) {
        if (head === null) {
            return [null, 0];
        }
        const res = recurse(head.next);
        res[1] = Math.max(res[1], head.val);
        head.next = res[0];
        if (res[1] <= head.val) {
            res[0] = head;
        }
        return res;
    }
    return recurse(head)[0];
};

