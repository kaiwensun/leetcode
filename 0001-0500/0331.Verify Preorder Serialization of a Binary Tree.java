/**
 * Basic idea:
 * 	recursively call a function to find the end of a (sub)tree; use exception mechanism to handle invalid tree structure.
 * Result:
 * 	149 / 149 test cases passed.
 * 	Status: Accepted
 * 	Runtime: 2 ms
 * 	Your runtime beats 99.51% of java submissions.
 * Date:
 * 	2/7/2016
 */
public class Solution {
    String preorder;
    public boolean isValidSerialization(String preorder) {
        this.preorder = preorder;
        try{
            if (getTreeEnd(0)==preorder.length()-1)
                return true;
            else
                return false;
        }
        catch(IndexOutOfBoundsException e){
            return false;
        }
    }
    private int getTreeEnd(int rootindex)throws IndexOutOfBoundsException
    {
        if(preorder.charAt(rootindex)=='#')
            return rootindex;
        int left_tree_root = preorder.indexOf(',',rootindex);
        if(left_tree_root<0)
            return -1;
        int right_tree_root = getTreeEnd(left_tree_root+1)+2;
        int right_tree_end = getTreeEnd(right_tree_root);
        return getTreeEnd(right_tree_end);
    }
}

