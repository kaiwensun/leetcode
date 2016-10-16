/**
 *Result:
 * 41 / 41 test cases passed.
 * Status: Accepted
 * Runtime: 9 ms
 * Your runtime beats 40.93% of cpp submissions.
 *Date:
 * 10/15/2016
 */

class Solution {
public:
    int minDepth(TreeNode* root) {
        if(root==NULL)
            return 0;
        int l = minDepth(root->left);
        int r = minDepth(root->right);
        if(l==0 && r==0){
            return 1;
        }
        if(l==0)
            return r+1;
        if(r==0)
            return l+1;
        return 1+(l<r?l:r);
    }
};
