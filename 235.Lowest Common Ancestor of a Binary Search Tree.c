#pragma warning (disable:4996)
#include<stdlib.h>
#include<stdio.h>
/**
* Definition for a binary tree node.
*/ struct TreeNode {
     int val;
     struct TreeNode *left;
     struct TreeNode *right;
 };


struct TreeNode* search(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q, int* both_found) {
	if (root == NULL)
	{
		*both_found = 0;
		return NULL;
	}
	*both_found = 0;
	struct TreeNode* left_result = search(root->left, p, q, both_found);
	if (*both_found)
		return left_result;
	struct TreeNode* right_result = search(root->right, p, q, both_found);
	if (*both_found)
		return right_result;
	if (left_result != NULL && right_result != NULL)
	{
		*both_found = 1;
		return root;
	}
	if (left_result != NULL || right_result != NULL)
	{
		if (root == p || root == q)
			*both_found = 1;
		return root;
	}
	if (root == p || root == q)
		return root;
	else
		return NULL;
}
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q) {
	if (p == q)
		return p;
	int both_found;
	return search(root, p, q, &both_found);
}
int main()
{
	struct TreeNode root;
	struct TreeNode left;
	root.left = &left;
	root.right = NULL;
	root.val = 2;
	left.left = left.right = NULL;
	left.val = 1;
	struct TreeNode* rtn = lowestCommonAncestor(&root, &root, &left);
	printf("%d\n", rtn->val);
	return 0;
}