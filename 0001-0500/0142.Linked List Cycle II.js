/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function (head) {
    if (!head) return head;
    let slow = head, fast = head;
    do {
        slow = slow.next;
        fast = fast.next && fast.next.next;
    } while (fast && slow !== fast);
    if (fast) {
        slow = head;
        while (slow !== fast) {
            slow = slow.next;
            fast = fast.next;
        }
    }
    return fast
};

