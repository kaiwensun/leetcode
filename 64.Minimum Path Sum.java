/* Basic idea:
 * 	Dynamic programming, filling table
 * Result:
 * 	61 / 61 test cases passed.
 * 	Status: Accepted
 * 	Runtime: 4 ms
 * 	Your runtime beats 54.00% of java submissions. * 	
 */
public class Solution {
    public int minPathSum(int[][] grid) {
        if(grid==null || grid.length==0 || grid[0]==null || grid[0].length==0)
            return 0;
        int m = grid.length;
        int n = grid[0].length;
        
        //init
        int[][] summation = new int[m][n];
        summation[0][0]=grid[0][0];
        for(int i=1;i<grid.length;i++)
            summation[i][0]=summation[i-1][0]+grid[i][0];
        for(int j=1;j<grid[0].length;j++)
            summation[0][j]=summation[0][j-1]+grid[0][j];
        
        //filling table
        for(int i=1;i<m;i++)
        {
            for(int j=1;j<n;j++)
            {
                summation[i][j]=Math.min(summation[i-1][j],summation[i][j-1])+grid[i][j];
            }
        }
        return summation[m-1][n-1];
    }
}

