/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
 
 /**
  *Result:
  * 22 / 22 test cases passed.
  * Status: Accepted
  * Runtime: 2 ms
  * Your runtime beats 33.33% of javasubmissions.
  *Date:
  * 8/20/2016
  */ 
public class Solution {
    public boolean isPalindrome(ListNode head) {
        int length = getLength(head);
        ListNode[] middles = relinkSecondHalf(head,length);
        return listsAreSame(middles[0], middles[1]);
    }
    private int getLength(ListNode head){
        int cnt = 0;
        while(head!=null){
            cnt++;
            head = head.next;
        }
        return cnt;
    }
    private ListNode[] relinkSecondHalf(ListNode head, int length){
        ListNode[] middles = new ListNode[2];
        if(length==0){
            middles[0]=null;middles[1]=null;
        }
        else if(length==1){
            middles[0]=head;middles[1]=head;
        }
        else if(length==2){
            middles[0] = head; middles[1] = head.next; head.next = null;
        }
        else{
            ListNode prev = head;
            ListNode curr = prev.next;
            ListNode next = curr.next;
            prev.next = null;
            for(int currindex = 1;currindex<length/2;currindex++){
                curr.next = prev;
                prev = curr;
                curr = next;
                next = curr.next;
            }
            middles[0]=prev;
            if(length%2==0){
                middles[1]=curr;
            }
            else{
                middles[1]=next;
            }
        }
        return middles;
    }
    private boolean listsAreSame(ListNode l1, ListNode l2){
        while(l1!=null && l2!=null){
            if(l1.val!=l2.val)
                return false;
            l1 = l1.next;
            l2 = l2.next;
        }
        return l1==null && l2==null;
    }
}
