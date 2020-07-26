/**
 *Result:
 * 102 / 102 test cases passed.
 * Status: Accepted
 * Runtime: 3 ms
 * Your runtime beats 28.47% of cpp submissions.
 */
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
        if(root==NULL || (root->left==NULL && root->right==NULL)){
            return 0;
        }
        return sumOfLeftLeaves(root,false);
    }
private:
    int sumOfLeftLeaves(TreeNode* root, bool isLeft){
        if(root==NULL){
            return 0;
        }
        if(root->left==NULL && root->right==NULL){
            return isLeft?root->val:0;
        }
        return sumOfLeftLeaves(root->left,true)+sumOfLeftLeaves(root->right,false);
    }
};
