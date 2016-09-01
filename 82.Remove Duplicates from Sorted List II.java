/**
 *Result:
 * 168 / 168 test cases passed.
 * Status: Accepted
 * Runtime: 2 ms
 * Your runtime beats 2.75% of javasubmissions.
 *Date:
 * 9/1/2016
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode prehead = new ListNode(-1);
        ListNode p1 = head;
        ListNode p2 = prehead;
        while(p1!=null){
            if(p1.next==null){
                p2.next = p1;
                p2 = p1;
                break;
            }
            else if(p1.val==p1.next.val){
                int val = p1.val;
                while(p1!=null && p1.val==val){
                    p1 = p1.next;
                }
            }
            else{
                p2.next = p1;
                p2 = p1;
                p1 = p1.next;
            }
        }
        p2.next = null;
        return prehead.next;
    }
}
