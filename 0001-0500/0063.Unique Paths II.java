/* Basic idea:
 * 	dynamic programming, filling table
 * Result:
 * 	43 / 43 test cases passed.
 * 	Status: Accepted
 * 	Runtime: 1 ms
 */
public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if(obstacleGrid==null || obstacleGrid.length==0 || obstacleGrid[0].length==0)
            return 0;
        int height = obstacleGrid.length;
        int width = obstacleGrid[0].length;
        int[][] numpath = new int[height][width];

        //init
        numpath[0][0]=1-obstacleGrid[0][0];
        for(int i=1;i<height;i++)
            numpath[i][0] = (obstacleGrid[i][0]==0 && numpath[i-1][0]==1)?1:0;
        for(int j=1;j<width;j++)
            numpath[0][j] = (obstacleGrid[0][j]==0 && numpath[0][j-1]==1)?1:0;
        
        //fill table
        for(int i=1;i<height;i++)
        {
            for(int j=1;j<width;j++)
            {
                numpath[i][j] = obstacleGrid[i][j]==1?0:(numpath[i-1][j]+numpath[i][j-1]);
            }
        }
        return numpath[height-1][width-1];
     }
}

