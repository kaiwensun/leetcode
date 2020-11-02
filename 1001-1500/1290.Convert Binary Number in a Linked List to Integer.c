/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


int getDecimalValue(struct ListNode* head){
    int res = 0;
    do {
        res <<= 1;
        res |= head->val;
    } while(head = head->next);
    return res;
}

