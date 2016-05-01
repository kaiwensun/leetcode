/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int count_from_tail(struct ListNode* head,int n,int* rtn);
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    if(head==NULL)
        return NULL;
    int rtn = 0;
    if(n==count_from_tail(head,n,&rtn))
    {
        struct ListNode* p = head->next;
        free(head);
        head = p;
    }
    return head;
}
int count_from_tail(struct ListNode* head,int n,int* rtn)
{
    /* assign rtn=1: tell prev "please delete me"
    */
    if(head==NULL)
    {
        *rtn = 0;
        return 0;
    }
    int cnt = count_from_tail(head->next,n,rtn)+1;
    if(*rtn==1)
    {
        struct ListNode* child = head->next;
        head->next = child->next;
        free(child);
        *rtn = 0;
    }
    if(cnt==n)
        *rtn = 1;
    return cnt;
}

