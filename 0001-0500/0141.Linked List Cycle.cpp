/**
 *Result:
 * 16 / 16 test cases passed.
 * Status: Accepted
 * Runtime: 9 ms
 * Your runtime beats 59.39% of cpp submissions.
 *Date:
 * 10/2/2016
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode* foo = new ListNode(-1);
        while(head!=NULL){
            if(head==foo)
                return true;
            ListNode* tmp = head->next;
            head->next = foo;
            head = tmp;
        }
        return false;
    }
};
