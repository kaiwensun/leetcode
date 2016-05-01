/**
 * Basic idea:
 *	Dynamic programming, filling table. for(treesize = 1 to n) for(start = 1to n-treesize+1) generate the list of trees and fill them to table cell. To generate the list of trees, for(root = start to end) for (every combination of leftsubtree and rightsubtree) add the new tree to the list.
 * Result:
 * 	9 / 9 test cases passed.
 * 	Status: Accepted
 * 	Runtime: 4 ms
 */


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
import java.util.ArrayList;
class Solution {

    //table[j][i] indicates a list of trees whose numbers ranges from i to j inclusive (i<=j)
    private ArrayList<ArrayList<ArrayList<TreeNode>>> table;

    public ArrayList<TreeNode> generateTrees(int n) 
    {
        if(n==0)
            return new ArrayList<TreeNode>();
        
        table = new ArrayList<ArrayList<ArrayList<TreeNode>>>(n+2);
        for(int i=0;i<=n+1;i++)
        {
        	table.add(new ArrayList<ArrayList<TreeNode>>(n+2));
        	for(int j=0;j<=i+1;j++)
        	{
        		table.get(i).add(new ArrayList<TreeNode>());
        	}
        }

        //tree size = 1. use only part of matrix where i<=j for table[j][i]
        for(int i=1;i<=n;i++)
        {
            table.get(i).get(i).add(new TreeNode(i));
            table.get(i-1).get(i).add(null);
        }
        table.get(n).get(n+1).add(null);
        
        //fill table
        for(int treeSize = 2;treeSize<=n;treeSize++)
        {
            for(int start = 1;start<=n-treeSize+1;start++)
            {
                generateTreeList(start, treeSize);
            }
        }
        return table.get(n).get(1);
    }
    
    
    private ArrayList<TreeNode> generateTreeList(int start, int treeSize)
    {
        for(int root = start;root<start+treeSize;root++)
        {
            for(TreeNode left_subtree : table.get(root-1).get(start))
            {
                for(TreeNode right_subtree : table.get(start+treeSize-1).get(root+1))
                {
                    TreeNode root_node = new TreeNode(root);
                    root_node.left = left_subtree;
                    root_node.right = right_subtree;
                    table.get(start+treeSize-1).get(start).add(root_node);
                }
            }
        }
        return table.get(start+treeSize-1-1).get(start-1);
    }
}

