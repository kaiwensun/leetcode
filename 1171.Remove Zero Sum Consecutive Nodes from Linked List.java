/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeZeroSumSublists(ListNode head) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        for (ListNode sweeperHeadDummy = dummy; sweeperHeadDummy != null && sweeperHeadDummy.next != null; sweeperHeadDummy = sweeperHeadDummy.next) {
            ListNode sweeperHead = sweeperHeadDummy.next;
            boolean changed = true;
            while (changed) {
                changed = false;
                int sum = 0;
                for (ListNode curr = sweeperHead; curr != null; curr = curr.next) {
                    sum += curr.val;
                    if (sum == 0) {
                        sweeperHead = curr.next;
                        sweeperHeadDummy.next = sweeperHead;
                        changed = true;
                    }
                }
            }
        }
        return dummy.next;
    }
}
