/**
 *Basic idea:
 * Three phases:
 * First, recursively call to merge the original list and the new list, one after the other, node by node.
 * Second, during the return of the recursion, construct the random ptr for the new list.
 * Third, split the merged list to the original one and the deep-copied one.
 * The idea is from https://discuss.leetcode.com/topic/7594/a-solution-with-constant-space-complexity-o-1-and-linear-time-complexity-o-n
 *Result:
 * 11 / 11 test cases passed.
 * Status: Accepted
 * Runtime: 2 ms
 * Your runtime beats 72.87% of java submissions.
 *Date:
 * 9/25/2016
 */
 
/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if(head==null)
            return null;
        RandomListNode newhead = new RandomListNode(head.label);
        mergeCopyRandomList(head,newhead);
        seperateTwoList(head);
        return newhead;
    }
    
    private void mergeCopyRandomList(RandomListNode head, RandomListNode newhead){
        if(head==null){
            return;
        }
        RandomListNode next = head.next;
        RandomListNode newNext = next==null?null:new RandomListNode(next.label);
        head.next = newhead;
        newhead.next = next;
        mergeCopyRandomList(next,newNext);
        //so far, all the next ptrs in newhead list are good.
        newhead.random = head.random==null?null:head.random.next;
    }
    
    private void seperateTwoList(RandomListNode head){
        if(head==null)
            return;
        RandomListNode ori = head;
        RandomListNode cpy = head.next;
        while(ori!=null){
            ori.next = cpy.next;
            ori = ori.next;
            if(ori!=null){
                cpy.next = ori.next;
                cpy = cpy.next;
            }
        }
    }
}
