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

function isPalindrome(head: ListNode | null): boolean {
    const arr = [];
    let p = head;
    while (p) {
        arr.push(p.val);
        p = p.next;
    }
    for (const skipLeft of [true, false]) {
        let left = -1, right = arr.length;
        let mismatch = false, broken = false;
        while (++left < --right) {
            if (arr[left] !== arr[right]) {
                if (mismatch) {
                    broken = true;
                    break;
                }
                mismatch = true;
                if (skipLeft) {
                    right++;
                } else {
                    left--;
                }
            }
        }
        if (!broken) {
            return true;
        }
    }
    return false;
};

