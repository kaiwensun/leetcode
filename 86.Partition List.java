/**
 *Basic Idea:
 * Scan the original list and construct two lists.
 *Result:
 * 166 / 166 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * Your runtime beats 4.23% of javasubmissions.
 *Date:
 * 8/31/2016
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
    public ListNode partition(ListNode head, int x) {
        ListNode ls = new ListNode(-1);
        ListNode ge = new ListNode(-1);
        ListNode l = ls;
        ListNode g = ge;
        for(ListNode p = head;p!=null;p = p.next){
            if(p.val < x){
                l.next = p;
                l = p;
            }
            else{
                g.next = p;
                g = p;
            }
        }
        l.next = ge.next;
        g.next = null;
        return ls.next;
    }
}
