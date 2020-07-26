/** 328	Odd Even Linked List
70 / 70 test cases passed.
Status: Accepted
Runtime: 1 ms
*/
class Solution {
    public ListNode oddEvenList(ListNode head) {
        if(head==null)
            return null;
        ListNode oddlst = new ListNode(-1);
        ListNode evnlst = new ListNode(-1);
        ListNode op=oddlst;
        ListNode ep=evnlst;
        ListNode p = head;
        for(int i=1;p!=null;i++)
        {
            if(i%2==1)
            {
                op.next = p;
                op=p;                
            }
            else
            {
                ep.next = p;
                ep=p;                
            }
            p=p.next;
        }
        op.next=null;
        ep.next=null;
        if(oddlst.next==null)
            return evnlst.next;
        op.next = evnlst.next;
        return oddlst.next;
    }
}

