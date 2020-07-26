/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root
     * @return Integer
     */
    function goodNodes($root, $mx=-INF) {
        $res = 0;
        if ($root != null) {
            $res += $root->val < $mx ? 0 : 1;
            $res += $this->goodNodes($root->left, max($mx, $root->val));
            $res += $this->goodNodes($root->right, max($mx, $root->val));
        }
        return $res;
    }
}
