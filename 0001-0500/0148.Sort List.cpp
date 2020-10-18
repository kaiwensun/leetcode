/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        int size = 1;
        ListNode dummy = ListNode(INT_MIN, head);
        ListNode* lastTail = &dummy;
        ListNode* head1 = NULL;
        ListNode* head2 = NULL;
        ListNode* tail1, * tail2;
        while (head1 != dummy.next) {
            head1 = lastTail->next;
            while ((tail1 = forward(head1, size - 1)) && (head2 = forward(tail1, 1))) {
                tail1->next = NULL;
                tail2 = forward(head2, size - 1);
                ListNode* nextHead = forward(tail2, 1);
                if (tail2) {
                    tail2->next = NULL;
                }
                lastTail = sortList(lastTail, head1, head2);
                lastTail->next = nextHead;
                head1 = nextHead;
            }
            size <<= 1;
            lastTail = &dummy;
        }
        return dummy.next;
    }

private:
    ListNode* sortList(ListNode* p, ListNode* head1, ListNode* head2) {
        ListNode *p1 = head1, *p2 = head2;
        while (p1 || p2) {
            if (!p1 || (p2 && p1->val > p2->val)) {
                p->next = p2;
                p2 = p2->next;
            } else {
                p->next = p1;
                p1 = p1->next;
            }
            p = p->next;
        }
        return p;
    }
    
    ListNode* forward(ListNode* head, int step) {
        for (int i = 0; i < step && head; i++) {
            head = head->next;
        }
        return head;
    }
};

