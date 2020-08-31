/**
 *Basic idea:
 * use hashmap to match original node and new node.
 * when the recursion reaches the end of list, the new list is well-constructed in terms of ptr next.
 * and the hashmap is well-constructed.
 * when the recursion returns, construct the random ptr.
 *Result:
 * Line 20: java.lang.StackOverflowError
 * (There is a testcase with 10050 nodes, while the recursion overflows at about 4000th nodes. Shorter testcases will be good.)
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
        HashMap<RandomListNode,RandomListNode> matcher = new HashMap<>();
        return deepCopySimpleList(head,matcher);
    }
    
    private RandomListNode deepCopySimpleList(RandomListNode head, HashMap<RandomListNode,RandomListNode> matcher){
        if(head==null){
            return null;
        }
        RandomListNode newhead = new RandomListNode(head.label);
        matcher.put(head,newhead);
        newhead.next = deepCopySimpleList(head.next,matcher);
        newhead.random = head.random==null?null:matcher.get(head.random);
        return newhead;
    }
}
