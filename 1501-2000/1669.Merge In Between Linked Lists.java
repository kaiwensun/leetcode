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
    public ListNode mergeInBetween(ListNode list1, int a, int b, ListNode list2) {
        ListNode dummy = new ListNode();
        dummy.next = list1;
        ListNode p = dummy;
        for (int i = 0; i < a; i++) {
            p = p.next;
        }
        ListNode removed = p.next;
        p.next = list2;
        for (int i = a; i < b; i++) {
            removed = removed.next;
        }
        while (list2.next != null) {
            list2 = list2.next;
        }
        list2.next = removed.next;
        return dummy.next;
    }
}

