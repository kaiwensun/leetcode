/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int dfs(struct TreeNode* root, int topdown) {
    if (root != NULL) {
        root -> val += dfs(root -> right, topdown);
        return dfs(root -> left, root -> val);
    }
    return topdown;
}
struct TreeNode* bstToGst(struct TreeNode* root){
    dfs(root, 0);
    return root;
}

