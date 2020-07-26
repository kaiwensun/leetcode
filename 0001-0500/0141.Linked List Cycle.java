/**
 *Result:
 * 16 / 16 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * Your runtime beats 9.48% of java submissions.
 *Date:
 * 10/2/2016
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        while(head!=null){
            if(head==head.next)
                return true;
            ListNode next = head.next;
            head.next = head;
            head = next;
        }
        return false;
    }
}
