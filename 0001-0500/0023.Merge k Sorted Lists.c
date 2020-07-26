#include<stdlib.h>
#include<stdio.h>

struct ListNode {
    int val;
    struct ListNode *next;
};
struct ListNode* merge2lists(struct ListNode* l1, struct ListNode* l2)
{
	struct ListNode* header = (struct ListNode*)malloc(sizeof(struct ListNode));
	header->next = NULL;
	header->val = -1;
	struct ListNode* p = header;
	while (l1 != NULL&&l2 != NULL)
	{
		if (l1->val < l2->val)
		{
			p->next = l1;
			l1 = l1->next;
		}
		else
		{
			p->next = l2;
			l2 = l2->next;
		}
		p = p->next;
		p->next = NULL;
	}
	if (l1 == NULL)
		p->next = l2;
	else
		p->next = l1;
	p = header->next;
	free(header);
	return p;
}
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
	for (int step = 1; step < listsSize; step *= 2)
	{
		int i;
		for (i = 0; i < listsSize; i += step*2)
		{
			int j = i + step;
			if (j < listsSize)
			{
				lists[i] = merge2lists(lists[i], lists[j]);
				lists[j] = NULL;
			}
		}
	}
	return lists[0];
}



void init_ListNode(struct ListNode* node, int x)
{
	node->val = x;
	node->next = NULL;
}

int main()
{
	struct ListNode* first_list = (struct ListNode*)(malloc(sizeof(struct ListNode)));
	init_ListNode(first_list, 1);
	first_list->next = (struct ListNode*)malloc(sizeof(struct ListNode));
	init_ListNode(first_list->next, 4);

	struct ListNode* second_list = (struct ListNode*)(malloc(sizeof(struct ListNode)));
	init_ListNode(second_list, 3);
	second_list->next = (struct ListNode*)malloc(sizeof(struct ListNode));
	init_ListNode(second_list->next, 6);

	struct ListNode* vec[2] = { first_list, second_list };

	struct ListNode* result = mergeKLists(vec, 2);
	while (result != NULL)
	{
		printf("%d ", result->val);
		result = result->next;
	}
	return 0;
}

