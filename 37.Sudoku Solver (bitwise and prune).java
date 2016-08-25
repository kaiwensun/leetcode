/**
 *Idea:
 *  Backtracking. Bitwise operation to save memory space. Pre-prune to reduce search space.
 *Result:
 *  6 / 6 test cases passed.
 *  Status: Accepted
 *  Runtime: 12 ms
 *  Your runtime beats 80.78% of javasubmissions.
 *Date:
 *  8/25/2016
 */
public class Solution {
    private int[][]hash = new int[3][9];
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
        for(char c : getPossibleChar(row, col)){
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
        int bit = 1<<((int)c-(int)'1');
        hash[0][row] |= bit;
        hash[1][col] |= bit;
        hash[2][getBoxIndex(row,col)] |= bit;
    }
    private void removeHash(int row, int col, char c){
        int bit = ~(1<<((int)c-(int)'1'));
        hash[0][row] &= bit;
        hash[1][col] &= bit;
        hash[2][getBoxIndex(row,col)] &= bit;
    }
    private LinkedList<Character> getPossibleChar(int row, int col){
        int bit = (~(hash[0][row] | hash[1][col] |  hash[2][getBoxIndex(row,col)])) & 0x01ff;
        LinkedList<Character> possi = new LinkedList<>();
        for(char c='1';c<='9';c++){
            if(bit%2==1)
                possi.add(c);
            bit = bit>>1;
        }
        return possi;
    }
}

