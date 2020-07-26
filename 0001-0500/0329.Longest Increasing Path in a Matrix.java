/**
 *Basic Idea:
 * Dynamic Programming. Keep record of the length of the longest increasing path from each entry.
 * <del>Don't forget there might be multiple valley.</del> It is not necessary to search from a valley.
 *Result:
 * 137 / 137 test cases passed.
 * Status: Accepted
 * Runtime: 16 ms
 * Your runtime beats 66.10% of javasubmissions.
 *Date:
 * 8/20/2016
 */ 
public class Solution {
    private int[][] matrix;
    private int[][] steps;
    public int longestIncreasingPath(int[][] matrix) {
        if(matrix==null || matrix.length == 0 || matrix[0].length==0)
            return 0;
        this.matrix = matrix;
        this.steps = new int[matrix.length][matrix[0].length];
        int maxlen = -1;
        for(int row = 0; row < matrix.length;row++){
            for(int col = 0;col<matrix[0].length;col++){
                maxlen = Math.max(maxlen,findIncSteps(row,col,Integer.MIN_VALUE));
            }
        }
        return maxlen;
    }

    private int findIncSteps(int row, int col, int value){
        if(row<0 || row>=matrix.length || col<0 || col>=matrix[0].length)
            return 0;
        if(matrix[row][col]<=value)
            return 0;
        if(steps[row][col]!=0)
            return steps[row][col];
        value = matrix[row][col];
        int step = 1+Math.max(findIncSteps(row-1,col,value),Math.max(findIncSteps(row+1,col,value),Math.max(findIncSteps(row,col-1,value),findIncSteps(row,col+1,value))));
        steps[row][col] = step;
        return step;
        
    }
}
