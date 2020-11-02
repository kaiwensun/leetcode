/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        int res = 0;
        for (ListNode node = head; node != null; node = node.next) {
            res <<= 1;
            res |= node.val;
        }
        return res;
    }
}

