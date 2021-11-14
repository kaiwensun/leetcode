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

function reverseEvenLengthGroups(head: ListNode | null): ListNode | null {
    const dummy = new ListNode(-1, head);
    let size = 1;

    function traverse(pre: ListNode, size: number): [ListNode, number] {
        let cnt = 0;
        while (size-- > 0 && pre?.next) {
            pre = pre.next;
            cnt++;
        }
        return [pre, cnt];
    }

    function reverse(pre: ListNode, size: number): ListNode[] {
        const head = pre?.next;
        let p1 = pre, p2 = head;
        for (let i = 0; i < size; i++) {
            let post = p2?.next;
            p2.next = p1;
            p1 = p2;
            p2 = post;
        }
        return [p1, p2];
    }

    let pre = dummy;
    while (pre.next) {
        let [curTail, cnt] = traverse(pre, size);
        if (cnt % 2 === 0) {
            let curHead = pre?.next;
            let [tail, nextHead] = reverse(pre, cnt);
            curHead.next = nextHead;
            pre.next = tail;
            curTail = curHead;
        }
        pre = curTail;
        size++;
    }
    return dummy.next;
};

