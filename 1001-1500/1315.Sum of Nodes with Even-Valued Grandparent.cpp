/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int sumEvenGrandparent(TreeNode* root) {
        return walk(root, false, false);
    }
    
    int walk(TreeNode* root, bool cntRoot, bool cntChildren) {
        int res = 0;
        if (root != NULL) {
            if (cntRoot) res += root->val;
            res += walk(root->left, cntChildren, root->val % 2 == 0);
            res += walk(root->right, cntChildren, root->val % 2 == 0);
        }
        return res;
    }
};
