#pragma warning (disable:4996)
#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#define bool short
#define true 1
#define false 0
struct Node{
	int value;
	int id;
	struct Node* next;
};
struct Node* insert(int new_value, int new_id, struct Node* old_list)
{
	struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
	new_node->value = new_value;
	new_node->id = new_id;
	new_node->next = old_list;
	return new_node;
}
void deleteNextNode(struct Node* node)
{
	if (node == NULL || node->next == NULL)
		return;
	struct Node* tmp = node->next;
	node->next = node->next->next;
	free(tmp);	
}
bool check(struct Node* list, int value, int id, int k)
{
	/* return true: find collision*/
	if (list == NULL)
		return false;
	if (id - list->id <= k && list->value == value)
		return true;
	for (struct Node* p = list; p->next != NULL;)
	{
		if (id - p->next->id > k)
		{
			deleteNextNode(p);
			continue;
		}
		if (p->next->value == value)
			return true;
		p = p->next;
	}
	return false;
}
bool containsNearbyDuplicate(int* nums, int numsSize, int k) {
	if (k == 0)
		return false;
	struct Node** hash = (struct Node**)malloc(sizeof(struct Node*)*k);
	memset(hash, NULL, sizeof(struct Node*)*k);
	for (int id = 0; id < numsSize; id++)
	{
		int hash_id = nums[id]%k;
		if (check(hash[hash_id], nums[id], id, k))
			return true;
		hash[hash_id] = insert(nums[id], id, hash[hash_id]);
	}
	return false;
}
int main()
{
	int nums[3] = { 1, 2, 1 };
	int numsSize = 3;
	int k = 0;
	char* rtn = containsNearbyDuplicate(nums, numsSize, k) ? "true" : "false";;
	printf("%s", rtn);
	return 0;
}