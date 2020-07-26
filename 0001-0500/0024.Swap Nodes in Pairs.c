/*
 * 思路：既然要交换两个节点A和B，那么我们只要能掌控住A的前驱和B的后继，那么我们想怎么折腾A和B都可以。
 */
struct ListNode* swapPairs(struct ListNode* head) {
    struct ListNode* newhead = (struct ListNode*)malloc(sizeof(struct ListNode));
    newhead->next = head;
    struct ListNode* prev = newhead, *left, *right, *tail;
    while(true){
        if(NULL!=prev && NULL!=(left=prev->next) && NULL!=(right=left->next))
        {
            tail = right->next;
            prev->next = right;
            right->next = left;
            left->next = tail;
            prev = left;
        }
        else
            break;
    }
    head = newhead->next;
    free(newhead);
    return head;
}

