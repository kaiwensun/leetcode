/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct ListNode** splitListToParts(struct ListNode* head, int k, int* returnSize){
    int size = 0;
    for (struct ListNode* p = head; p != NULL; p = p -> next, size++);
    int part_size = size / k;
    int num_of_extra_size_list = size - part_size * k;
    struct ListNode** res = (struct ListNode**) malloc(sizeof(struct ListNode*) * k);
    struct ListNode* p = head;
    for (int i = 0; i < k; i++) {
        *(res + i) = p;
        int this_part_size = i < num_of_extra_size_list ? part_size + 1 : part_size;
        for (int j = 0; j < this_part_size - 1; j++, p = p -> next);
        if (p != NULL) {
            struct ListNode* tmp = p -> next;
            p -> next = NULL;
            p = tmp;
        }
    }
    *returnSize = k;
    return res;
}

