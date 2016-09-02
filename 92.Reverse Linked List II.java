/**
 *Result:
 * 44 / 44 test cases passed.
 * Status: Accepted
 * Runtime: 0 ms
 * Your runtime beats 9.80% of javasubmissions.
 *Date:
 * 9/2/2016
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
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode prehead = new ListNode(-1);
        prehead.next = head;
        ListNode node_prem = prehead;
        for(int i=0;i<m-1;i++){
            node_prem = node_prem.next;
        }
        ListNode node_m = node_prem.next;
        ListNode node_i = node_m;
        ListNode node_posti = node_m.next;
        for(int i=m;i<n;i++){
            ListNode node_postposti = node_posti.next;
            node_posti.next = node_i;
            node_i = node_posti;
            node_posti = node_postposti;
        }
        node_prem.next = node_i;
        node_m.next = node_posti;
        return prehead.next;
    }
}
