/**
 *Result:
 * 164 / 164 test cases passed.
 * Status: Accepted
 * Runtime: 1 ms
 * Your runtime beats 17.15% of javasubmissions.
 *Date:
 * 8/20/2016
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
        ListNode p = head;
        while(p!=null && p.next!=null){
            if(p.val==p.next.val)
                p.next = p.next.next;
            else
                p = p.next;
        }
        return head;
    }
}
 
 /**
 * try-catch block really slows the execution. The following code Runtime: 6 ms and beats only 0.91% of javasubmissions.
 */
/*
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode p = head;
        try{
            while(true){
                if(p.val==p.next.val)
                    p.next = p.next.next;
                else
                    p = p.next;
            }
        }
        catch(NullPointerException e){}
        return head;
    }
}
*/

