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

class Solution {
    private readonly head: ListNode;
    constructor(head: ListNode | null) {
        this.head = head;
    }

    getRandom(): number {
        let res = this.head;
        let p = this.head?.next;
        let size = 1;
        while (p) {
            if (Math.floor(Math.random() * (++size)) === 0) {
                res = p;
            }
            p = p.next;
        }
        return res?.val;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(head)
 * var param_1 = obj.getRandom()
 */

