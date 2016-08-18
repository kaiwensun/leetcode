/**
 *This seems not an efficient solution....
 *Basic idea:
 *  binary search along diagnal, and separate the matrix into four sub-matrices.
 *Result:
 *  127 / 127 test cases passed.
 *  Status: Accepted
 *  Runtime: 33 ms
 *Date:
 *  8/18/2016
 */
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
		try{
			if(matrix.length==0 || matrix[0].length==0)
				return false;
		}
		catch(NullPointerException e){
			return false;
		}
        return searchMatrix(matrix, target,0,0,matrix.length-1,matrix[0].length-1);
    }
    
    private boolean searchMatrix(int[][] matrix, int target, int startrow, int startcol, int endrow, int endcol){
        if(startrow>endrow || startcol > endcol)
            return false;
        int midrow = (startrow+endrow)/2;
        int midcol = (startcol+endcol)/2;
        if(matrix[midrow][midcol]==target)
            return true;
        else if(matrix[midrow][midcol]<target){
            return searchMatrix(matrix,target,midrow+1,midcol+1,endrow,endcol)
            || searchMatrix(matrix,target,midrow+1,startcol,endrow,midcol)
            || searchMatrix(matrix,target,startrow,midcol+1,midrow,endcol);
        }
        else{
            return ((startrow==midrow && startcol==midcol)?false:searchMatrix(matrix,target,startrow,startcol,midrow,midcol))
            || searchMatrix(matrix, target, midrow+1,startcol, endrow, midcol-1)
            || searchMatrix(matrix, target, startrow, midcol+1, midrow-1, endcol);
        }
    }
}
