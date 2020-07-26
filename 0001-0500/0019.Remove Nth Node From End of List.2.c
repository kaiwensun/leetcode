/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int removeit(struct ListNode* head, int n) {
    if (!head)
        return 1;
    int dist = removeit(head -> next, n);
    if (dist == n + 1)
        head -> next = head -> next ? head -> next -> next : NULL;
    return dist + 1;
}

struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode dummy;
    dummy.next = head;
    removeit(&dummy, n);
    return dummy.next;
}
