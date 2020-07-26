/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

public class Solution {
    private ListNode[] reverseOneGroup(ListNode[] old_phtn, int k){
        ListNode[] phtn = new ListNode[4];  //previous, new_head, new_tail, next
        ListNode head = old_phtn[3];
        ListNode tail = head;
        for(int i=0;i<k-1 && tail!=null;i++){
            tail = tail.next;
        }
        if(tail==null){
            phtn[0] = old_phtn[2];
            phtn[1] = head;
            phtn[2] = tail; //null
            phtn[3] = null;
            return  phtn;
        }else{
            phtn[0] = old_phtn[2];
            phtn[1] = tail;
            phtn[2] = head;
            phtn[3] = tail.next;
            ListNode h = head;
            ListNode n = h.next;
            ListNode nn = n==null?null:n.next;
            for(int i=0;i<k-1;i++){
                n.next = h;
                h = n;
                n = nn;
                nn = n==null?null:n.next;
            }
        }
        return phtn;
    }
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode[] old_phtn = {null,null,null,head};
        while(old_phtn[3]!=null){
            ListNode[] phtn = reverseOneGroup(old_phtn,k);
            if(old_phtn[2]!=null){
                old_phtn[2].next = phtn[1];
            }else{
                head = phtn[1];
            }
            old_phtn = phtn;
        }
        if(old_phtn[2]!=null){
            old_phtn[2].next = null;
        }
        return head;
    }
}
