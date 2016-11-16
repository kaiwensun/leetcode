/**
 *Basic idea:
 * Without loss of generation, let's assume list A is k elements longer than list B. (k>=0)
 * If list A is as long as list B, then obviously the returned node will be the intersection
 * if there is an intersection, or null if there is no intersection.
 * If list A is longer than list b, then when b reaches the end of list, a is still k nodes
 * away from the end. Then b goes to the head of list A, continue until a reaches the end of
 * list and goes back to the head of list B.
 * At this point, b is k nodes away from the head of list A. Since list A is k elements longer
 * than list B, we can conclude that both a and b are both lengthOf(list B) away from the end
 * of the list (regardless of the existence of the intersection). Tha means a and b are 
 * same-length away from the intersection (or null).
 * From now on, continue the loop, until we find the intersection (or null).
 *Result:
 * 42 / 42 test cases passed.
 * Status: Accepted
 * Runtime: 43 ms
 * Your runtime beats 70.64% of cpp submissions
 *Date:
 * 11/15/2016
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        ListNode *a = headA, *b = headB;
        while(a!=b){
            a = a==NULL?headB:a->next;
            b = b==NULL?headA:b->next;
        }
        return a;
    }
};
