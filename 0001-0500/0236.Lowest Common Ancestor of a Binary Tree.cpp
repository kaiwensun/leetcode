/**
 * 31 / 31 test cases passed.
 * Status: Accepted
 * Runtime: 26 ms
 * Your runtime beats 28.97% of cpp submissions.
 *Date:
 * 12/11/2016
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root==NULL || root==p || root==q) return root;
        TreeNode* left = lowestCommonAncestor(root->left,p,q);
        TreeNode* right = lowestCommonAncestor(root->right,p,q);
        return left?(right?root:left):right;
    }
};
