/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode dummy = new ListNode(Integer.MIN_VALUE, head);
        ListNode p = dummy;
        while (p.next != null) {
            if (p.val > p.next.val) {
                insert(dummy, takeOut(p));
            } else {
                p = p.next;
            }
        }
        return dummy.next;
    }
    
    private ListNode takeOut(ListNode p) {
        // assume p.next != null
        ListNode node = p.next;
        p.next = p.next.next;
        return node;
    }
    
    private void insert(ListNode dummy, ListNode node) {
        ListNode p;
        for (p = dummy; p.next != null && p.next.val < node.val; p = p.next) {
            
        }
        node.next = p.next;
        p.next = node;
    }
}

