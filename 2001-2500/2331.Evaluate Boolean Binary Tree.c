/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


bool evaluateTree(struct TreeNode* root){
    return root->val <= 1 ? 1 == root->val : (root->val == 2 ?
        evaluateTree(root->left) || evaluateTree(root->right) :
        evaluateTree(root->left) && evaluateTree(root->right));
}

