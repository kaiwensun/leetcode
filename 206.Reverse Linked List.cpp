/**
 *Result:
 * 27 / 27 test cases passed.
 * Status: Accepted
 * Runtime: 6 ms
 * Your runtime beats 48.10% of cpp submissions.
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* newhead = NULL;
        while(head!=NULL){
            ListNode* tmp = head->next;
            head->next = newhead;
            newhead = head;
            head = tmp;
        }
        return newhead;
    }
};
