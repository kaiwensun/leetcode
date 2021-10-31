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

function isCritical(prev: ListNode) {
    return (prev.val < prev.next.val && prev.next.val > prev.next.next.val) || (prev.val > prev.next.val && prev.next.val < prev.next.next.val);
}
function nodesBetweenCriticalPoints(head: ListNode | null): number[] {
    let first = undefined;
    let last = undefined;
    let p = head;
    let prev = head;
    let i = 1;
    const res = [undefined, undefined];
    while (prev?.next?.next) {
        if (isCritical(prev)) {
            if (first !== undefined) {
                res[0] = Math.min(res[0] || Infinity, i - last);
                res[1] = i - first;
            }
            first ||= i;
            last = i;
        }
        i++;
        prev = prev.next;
    }
    return [res[0] || -1, res[1] || -1];
};

