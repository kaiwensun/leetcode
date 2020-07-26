/**
 *Result:
 * 226 / 226 test cases passed.
 * Status: Accepted
 * Runtime: 6 ms
 * Your runtime beats 37.42% of c submissions.
 *Date:
 * 11/7/2016
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int height (struct TreeNode* root){
    if(root==NULL){
        return 0;
    }
    int hl = height(root->left);
    int hr = height(root->right);
    if(hl==-1 || hr==-1){
        return -1;
    }
    if(hl==hr || hl-1==hr){
        return hl+1;
    }
    if(hr-1==hl){
        return hr+1;
    }
    return -1;
}
bool isBalanced(struct TreeNode* root) {
    return -1!=height(root);
}
