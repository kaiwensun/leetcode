/**
 *Basic Idea:
 * Dynamic Programming. Keep record of the length of the longest increasing path from each entry.
 * Don't forget there might be multiple valley.
 *Result:
 * 137 / 137 test cases passed.
 * Status: Accepted
 * Runtime: 17 ms
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
                if(isVally(row,col)){
                    maxlen = Math.max(maxlen,findIncSteps(row,col,Integer.MIN_VALUE));
                }
            }
        }
        return maxlen;
    }
    
    boolean isVally(int row, int col){
        int c = matrix[row][col];
        //System.out.println("c="+c+",row and col = "+row+" "+col);
        return (steps[row][col]==0)
        && (col==0 || matrix[row][col-1]>=c)
        && (col==matrix[0].length-1 || matrix[row][col+1]>=c)
        && (row==0 || matrix[row-1][col]>=c)
        && (row==matrix.length-1 || matrix[row+1][col]>=c);
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
