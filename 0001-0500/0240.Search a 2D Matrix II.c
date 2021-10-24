/**
 *Basic idea:
 * search along diagnal. each comparation excludes either one row or one colume.
 *Result:
 * 127 / 127 test cases passed.
 * Status: Accepted
 * Runtime: 52 ms
 * Your runtime beats 94.44% of c submissions.
 *Date:
 * 9/19/2016
 */
bool searchMatrix(int** matrix, int matrixRowSize, int* matrixColSize, int target) {
    int c = 0;
    int r = matrixRowSize-1;
    while(r>=0 && c<*matrixColSize){
        int t = matrix[r][c];
        if(t==target)
            return true;
        if(t>target)
            r--;
        else
            c++;
    }
    return false;
}
