/**
 *Basic Idea:
 *  backtracking
 *Improved Idea:
 *  Use bitwise AND to decide if a number is setable to a slot
 *Basic Idea Result:
 *  6 / 6 test cases passed.
 *  Status: Accepted
 *  Runtime: 10 ms
 *  Your runtime beats 82.67% of javasubmissions.
 *Date:
 *  8/25/2016
 */
public class Solution {
    private boolean[][][] hash = new boolean[3][9][9];
    private char[][] board;
    private final static char[] dict = {'1','2','3','4','5','6','7','8','9'};
    public void solveSudoku(char[][] board) {
        this.board = board;
        init();
        solveSudoku(0,0);
    }
    private boolean solveSudoku(int row, int col){
        int[] index = findNextSlot(row, col);
        if(index==null)
            return true;
        row = index[0];
        col = index[1];
        for(char c : dict){
            if(canSet(row,col,c)){
                setHash(row,col,c);
                board[row][col]=c;
                if(solveSudoku(row,col+1)){
                    return true;
                }
                else{
                    removeHash(row,col,c);
                    board[row][col]='.';
                }
            }
        }
        return false;
    }
    private int[] findNextSlot(int row, int col){
        for(int i=row;i<9;i++){
            for(int j=(i==row?col:0);j<9;j++){
                if(board[i][j]=='.'){
                    return new int[]{i,j};
                }
            }
        }
        return null;
    }
    private void init(){
        for(int row = 0;row<9;row++){
            for(int col=0;col<9;col++){
                if(board[row][col]!='.'){
                    setHash(row,col,board[row][col]);
                }
            }
        }
    }
    private static int getBoxIndex(int row, int col){
        return row/3*3+col/3;
    }
    private void setHash(int row, int col, char c){
        hash[0][row][(int)c-(int)'1'] = true;
        hash[1][col][(int)c-(int)'1'] = true;
        hash[2][getBoxIndex(row,col)][(int)c-(int)'1'] = true;
    }
    private boolean canSet(int row, int col, char c){
        return !(hash[0][row][(int)c-(int)'1'] || hash[1][col][(int)c-(int)'1'] || hash[2][getBoxIndex(row,col)][(int)c-(int)'1']);
    }
    private void removeHash(int row, int col, char c){
        hash[0][row][(int)c-(int)'1'] = false;
        hash[1][col][(int)c-(int)'1'] = false;
        hash[2][getBoxIndex(row,col)][(int)c-(int)'1'] = false;
    }
}
