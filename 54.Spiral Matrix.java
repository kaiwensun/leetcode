/**
 *Basic idea:
 * Construct the list ring-by-ring, recursively.
 *Result:
 * 22 / 22 test cases passed.
 * Status: Accepted
 * Runtime: 3 ms
 * Your runtime beats 18.28% of java submissions.
 *Date:
 * 10/30/2016
 */
public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        if(matrix==null || matrix.length==0 || matrix[0].length==0){
            return new LinkedList<Integer>();
        }
        return spiralOrder(matrix,0,matrix[0].length-1,0,matrix.length-1);
    }
    private List<Integer> spiralOrder(int[][] matrix ,int l, int r, int t, int b){
        List<Integer> lst = new LinkedList<Integer>();
        if(r<l || b<t){
            return lst;
        }
        if(r==l && t==b){
            lst.add(matrix[l][t]);
            return lst;
        }
        if(r==l){
            for(int row = t;row<=b;row++){
                lst.add(matrix[row][r]);
            }
            return lst;
        }
        if(t==b){
            for(int col = l;col<=r;col++){
                lst.add(matrix[t][col]);
            }
            return lst;
        }

        for(int col = l;col<r;col++){
            lst.add(matrix[t][col]);
        }
        for(int row = t;row<b;row++){
            lst.add(matrix[row][r]);
        }
        for(int col=r;col>l;col--){
            lst.add(matrix[b][col]);
        }
        for(int row = b;row>t;row--){
            lst.add(matrix[row][l]);
        }
        lst.addAll(spiralOrder(matrix,l+1,r-1,t+1,b-1));
        return lst;
    }
}
