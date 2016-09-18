/**
 *Result:
 * 114 / 114 test cases passed.
 * Status: Accepted
 * Runtime: 6 ms
 * We are in the progress of updating the graph distribution. Please check the distribution again within weeks.
 *Date:
 * 9/17/2016
 */
 
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool hasPathSum(struct TreeNode* root, int sum) {
    if(root==NULL)
        return false;
    if(root->left==root->right && root->left==NULL)
        return root->val == sum;
    return hasPathSum(root->left,sum-root->val) || hasPathSum(root->right,sum-root->val);
}
