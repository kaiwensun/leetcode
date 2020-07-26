/**
 *Result:
 * 28 / 28 test cases passed.
 * Status: Accepted
 * Runtime: 8 ms
 * Sorry. We do not have enough accepted submissions.
 *Date:
 * 10/15/2016
 */
public class Solution {
    public int countBattleships(char[][] board) {
        int h = countHorizontal(board);
        int v = countVertical(board);
        int s = countSinglePoint(board);
        return h+v+s;
    }
    private int countHorizontal(char[][] board){
        int cnt = 0;
        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[0].length;j++){
                if(board[i][j]=='.')
                    continue;
                int tail = toRightMost(board,i,j);
                if(tail==j)
                    continue;
                cnt++;
                j = tail+1;
            }
        }
        return cnt;
    }
    private int countVertical(char[][] board){
        int cnt = 0;
        for(int j=0;j<board[0].length;j++){
            for(int i=0;i<board.length;i++){
                if(board[i][j]=='.')
                    continue;
                int tail = toDownMost(board,i,j);
                if(tail==i)
                    continue;
                cnt++;
                i = tail+1;
            }
        }
        return cnt;
    }
    private int countSinglePoint(char[][] board){
        int cnt = 0;
        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[0].length;j++){
                if(board[i][j]=='X'){
                    if(!isHorizontal(board,i,j) && !isVertical(board,i,j)){
                        cnt++;
                    }
                }
            }
        }
        return cnt;
    }
    private int toRightMost(char[][] board, int i,int j){
        while(j+1<board[0].length && board[i][j+1]=='X')
            j++;
        return j;
    }
    
    private int toDownMost(char[][] board, int i,int j){
        while(i+1<board.length && board[i+1][j]=='X')
            i++;
        return i;
    }
    
    private boolean isHorizontal(char[][] board, int i,int j){
        if(board[0].length<=1)
            return false;
        int l = j-1, r=j+1;
        return (l>=0 && board[i][l]=='X')||(r<board[0].length && board[i][r]=='X');
    }
    private boolean isVertical(char[][] board, int i,int j){
        if(board.length<=1)
            return false;
        int t = i-1, d=i+1;
        return (t>=0 && board[t][j]=='X')||(d<board.length && board[d][j]=='X');
    }
}
