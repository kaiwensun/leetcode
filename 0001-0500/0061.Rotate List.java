/*
 * Basic idea:
 * 	traceback
 * Result
 *	230 / 230 test cases passed.
 *	Status: Accepted
 *	Runtime: 2 ms
 */
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; next=null;}
    ListNode(int x,ListNode n){val=x;next=n;}
}
class Solution{
    private class ListDescriptor{
        ListNode oldhead;
        ListNode oldtail;
        ListNode newtail;
        ListNode newhead;
        int const_k=-1;
        int listsize=-1;
        public ListDescriptor(ListNode oldhead, int const_k){
            this.oldhead = oldhead;
            this.const_k = const_k;
        }
    }
    public ListNode rotateRight(ListNode head, int k) {
        if (head==null || k<0)
            return null;
        if (k==0)
            return head;
        ListDescriptor dsptr = new ListDescriptor(head,k);
        getSpecialNode(dsptr,head,0);
        dsptr.newtail.next=null;
        return dsptr.newhead;
    }
    private int getSpecialNode(ListDescriptor dsptr, ListNode curhead, int prevlen){
        if(curhead==null){
            dsptr.listsize = prevlen;
            dsptr.const_k = dsptr.const_k%prevlen;
            if(prevlen==1){
                dsptr.newhead=dsptr.newtail=dsptr.oldtail=dsptr.oldhead;
                dsptr.newtail.next=null;
                return 0;
            }
            return -1;
        }
        int rtn = getSpecialNode(dsptr,curhead.next,prevlen+1);
        if(rtn==-1){
            if(prevlen+1==dsptr.listsize){  //i am old tail
                dsptr.oldtail = curhead;
                dsptr.oldtail.next = dsptr.oldhead;
            }
            if(dsptr.listsize==dsptr.const_k+prevlen){  //i am new head
                dsptr.newhead = curhead;
            }
            else if(dsptr.listsize==dsptr.const_k+prevlen+1){   //i am new tail
                dsptr.newtail = curhead;
                dsptr.newtail.next = null;
                if(dsptr.newhead==null)
                	dsptr.newhead=dsptr.oldhead;
                return 0;
            }
            return -1;
        }
        return 0;
    }
}

