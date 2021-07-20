/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
    struct ListNode* a = headA, *b = headB;
    if (a == NULL || b == NULL) return NULL;
    while (true) {
        if (a == b) return a;
        if (a->next == NULL && b->next == NULL) return NULL;
        a = a->next == NULL ? headB : a -> next;
        b = b->next == NULL ? headA : b -> next;
    }
}

