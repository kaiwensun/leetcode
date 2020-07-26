/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 /*
 An excellent solution shared at https://leetcode.com/discuss/47642/simple-and-elegant-solution-in-c
 ListNode *removeElements(ListNode *head, int val)
{
    ListNode **list = &head;

    while (*list != nullptr)
    {
        if ((*list)->val == val)
        {
            *list = (*list)->next;
        }
        else
        {
            list = &(*list)->next;
        }
    }

    return head;
}
 */
struct ListNode* removeElements(struct ListNode* head, int val) {
    struct ListNode* curr = head;
    struct ListNode* prev = NULL;
    while(curr!=NULL)
    {
        if(curr->val == val)
        {
            if(prev==NULL)
            {
                curr = curr->next;
                head = curr;
            }
            else
            {
                prev->next = curr->next;
                curr = curr->next;
            }
            continue;
        }
        prev = curr;
        curr = prev->next;
    }
    return head;
}

