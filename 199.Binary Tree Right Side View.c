/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
#define max(x, y) ((x) < (y) ? (y) : (x))
void dfs(struct TreeNode* root, int depth, int* view, int* viewSize, int returnSize) {
    if (!root || *viewSize == returnSize) {
        return;
    }
    if (depth == *viewSize) {
        view[(*viewSize)++] = root->val;
    }
    dfs(root->right, depth + 1, view, viewSize, returnSize);
    dfs(root->left, depth + 1, view, viewSize, returnSize);
}

int getDepth(struct TreeNode* root) {
   if (root) {
       int left = getDepth(root->left);
       int right = getDepth(root->right);
       return max(left, right) + 1;
   } else {
       return 0;
   }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rightSideView(struct TreeNode* root, int* returnSize){
    *returnSize = getDepth(root);
    int* view = malloc(sizeof(int) * *returnSize);
    int viewSize = 0;
    dfs(root, 0, view, &viewSize, *returnSize);
    return view;
}

